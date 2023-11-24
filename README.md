### Development Environment
- Python 3.10
- Module dependencies can be found from 'requirement.txt'

### Download the build of GRPC.Tools
Current version: 2.51.0
https://nuget.info/packages/Grpc.Tools/2.51.0

Latest build
https://nuget.info/packages/Grpc.Tools

### Build Protobuf

python protobuilder.py generate_proto_code --lang=cs --source="proto/ugrpc_pipe" --output="<UnityProject>/Assets/Editor/Pipeline/gRPC/Protobuf"
python protobuilder.py generate_proto_code --lang=py --source="proto/ugrpc_pipe" --output="<Python Pipeline Project>/unity-grpc-build-proto-pipe"

Example:

python protobuilder.py generate_proto_code --lang=cs --source="proto/ugrpc_pipe" --output="P:/Dev/SyngularXR/Syngar/Assets/Plugins/ugrpc/Editor/Protobuf"
python protobuilder.py generate_proto_code --lang=py --source="proto/ugrpc_pipe" --output="D:/Dev/Syngar_Pipeline/unity-grpc-build-proto-pipe"