import fileinput
import os
import subprocess
import sys
from enum import Enum
from os.path import abspath, dirname

import fire

from compipe.utils.io_helper import get_files, warm_up_path
from compipe.utils.logging import logger

DIR = dirname(abspath(__file__))

GRPC_PLUGIN_TOOL = os.path.join(
    DIR, 'Tools', sys.platform, 'grpc_csharp_plugin')
PROTOC_TOOL = os.path.join(DIR, 'Tools', sys.platform, 'protoc')

# add 'exe' executable extension for win32 platform
if sys.platform == 'win32':
    GRPC_PLUGIN_TOOL += '.exe'
    PROTOC_TOOL += '.exe'


class Lang(Enum):
    cs = 'csharp'
    py = 'python'


def resolve_grpc_import_error(export_dir):
    # only edit the module reference headers for *_grpc.py script
    name_pattern = '_grpc'
    # looking for the grpc script files from the specified path
    matched = get_files([export_dir], ext_patterns=['py'])
    # iterate all the grpc script files
    for grpc_file in matched:
        file_name, _ = os.path.splitext(os.path.basename(grpc_file))
        # resolve the protocol buffer module name
        protocol_buf_name = file_name[:-(len(name_pattern)-1)]
        print(grpc_file)
        print(protocol_buf_name)
        # iterate all lines from the specified file
        for line in fileinput.input(grpc_file, inplace=True):
            # check the module reference
            if line.startswith(f'from {protocol_buf_name} import'):
                # fix the syntax to support import module from a sub_directory
                line = f'from . {line} import'
            # write into file
            sys.stdout.write(line)


class ProtoBuilder:

    def generate_proto_code(self, library: str = 'proto',
                            source: str = 'proto',
                            output: str = 'export',
                            lang: str = 'cs'):

        # resolve the source / output to absolute path
        if not os.path.isabs(library):
            library = os.path.join(DIR, library)
        if not os.path.isabs(output):
            output = os.path.join(DIR, output)
        if not os.path.isabs(source):
            source = os.path.join(DIR, source)

        # retrieve all *.proto files from source folder
        proto_files = get_files([source], ext_patterns=['proto'])

        # create the output directories if the path doesn't exit
        warm_up_path(path=output)

        # resolve the process parameter for a specific language
        if Lang[lang] == Lang.cs:
            # generate protocol buffers and grpc for csharp code
            param = [os.path.join(DIR, PROTOC_TOOL),
                     f'-I="{library}"',
                     f'--csharp_out="{output}"',
                     f'--grpc_out="{output}"',
                     f'--plugin=protoc-gen-grpc={GRPC_PLUGIN_TOOL}']

        else:
            # generate protocol buffers and grpc for python code
            # execute python script from activated virtualenv

            # involve a sub package folder if the value was specified.
            # python_output_path = os.path.join(output,package) if package else output

            param = [f'{sys.executable} -m grpc_tools.protoc',
                     f'--proto_path="{library}"',
                     f'--python_out="{output}"',
                     f'--python_betterproto_out="{output}"',
                     f'--grpc_python_out="{output}"']

        for proto_file in proto_files:
            logger.debug(f'Build proto ({Lang[lang].value}): {proto_file}')
            print(' '.join([*param, proto_file]))
            # start to trigger the process of building proto code for a specific language
            process = subprocess.Popen(
                ' '.join([*param, proto_file]), stdout=subprocess.PIPE)
            output_logs, _ = process.communicate()

            if output_logs:
                logger.debug(output_logs.decode("utf-8"))

    def batch_export(self):
        # --lang=cs --source="proto/ugrpc_pipe" --output="P:/ImagineersHub/epochdot-grpc-unity/Assets/Plugins/UGrpc/Runtime/Protobuf"
        self.generate_proto_code(lang='cs',
                                 source='proto/ugrpc_pipe',
                                 output='P:/ImagineersHub/epochdot-grpc-unity/Assets/Plugins/UGrpc/Runtime/Protobuf')
        # --lang=py --source="proto/ugrpc_pipe" --output="P:/Syngar_Pipeline/unity-grpc-build-proto-pipe"
        self.generate_proto_code(lang='py',
                                 source='proto/ugrpc_pipe',
                                 output='P:/ImagineersHub/ugrpc-pipe-python')


def main():
    fire.Fire(ProtoBuilder(), name='protobuilder')


if __name__ == '__main__':
    main()
