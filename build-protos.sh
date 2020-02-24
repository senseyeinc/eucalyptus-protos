# builds protos using python's grpcio-tools.

# Check for Python
PYTHON_BIN="$(command -v python3 || command -v python)"
if ! [ -x "$PYTHON_BIN" ]; then
	echo "Python interpreter not found." >&2
	exit 1
fi
echo "Found Python interpreter at: $PYTHON_BIN"

OUTPUT_PATH=./eucalyptus_protos/python_protos
INPUT_PATH=./eucalyptus_protos/protobuf

echo "Input path: $INPUT_PATH"
echo "Output path: $OUTPUT_PATH"

# make build proto dir
mkdir -p $INPUT_PATH;
mkdir -p $OUTPUT_PATH;

# Generate protoc
echo "Building Protos..."
$PYTHON_BIN -m grpc_tools.protoc -I$INPUT_PATH --python_out=$OUTPUT_PATH --grpc_python_out=$OUTPUT_PATH $INPUT_PATH/*.proto

# Replace with relative imports
if [ `uname -s` == 'Darwin' ]; then
    # Darwin (Mac) sed
    sed -i '' 's/^\(import.*_pb2\)/from . \1/' $OUTPUT_PATH/*pb2*.py
else
    # Linux sed
    sed 's/^\(import.*_pb2\)/from . \1/' -i $OUTPUT_PATH/*pb2*.py
fi

# Create init file
touch $OUTPUT_PATH/__init__.py

echo "Build Complete"
