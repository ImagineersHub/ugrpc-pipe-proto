### Development Environment

- Python 3.10
- Module dependencies can be found from 'requirement.txt'

### Download the build of GRPC.Tools

Current version: 2.51.0
https://nuget.info/packages/Grpc.Tools/2.51.0

Latest build
https://nuget.info/packages/Grpc.Tools

### Build Protobuf

#### Batch export (Recommended):

`python protobuilder.py batch_export`

#### Export Commands:

python protobuilder.py generate_proto_code --lang=cs --source="proto/ugrpc_pipe" --output="<UnityProject>/Assets/Editor/Pipeline/gRPC/Protobuf"
python protobuilder.py generate_proto_code --lang=py --source="proto/ugrpc_pipe" --output="<Python Pipeline Project>/unity-grpc-build-proto-pipe"

Example:

python protobuilder.py generate_proto_code --lang=cs --source="proto/ugrpc_pipe" --output="P:\ImagineersHub\epochdot-grpc-unity\Assets\Plugins\UGrpc\Runtime\Protobuf"

python protobuilder.py generate_proto_code --lang=py --source="proto/ugrpc_pipe" --output="P:\ImagineersHub\ugrpc-pipe-python"
python protobuilder.py generate_proto_code --lang=py --source="proto/ugrpc_pipe" --output="P:\Project\syngar-amfitrack-server\protobuf"
