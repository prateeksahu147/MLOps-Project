PROTOS_PY_FILE=/tfod/models/research/object_detection/protos/*.py
PROTOS_FILE=/tfod/models/research/object_detection/protos/*.proto
new_path=$PROTOS_PY_FILE$PROTOS_FILE
echo "$new_path"

COCO_API_PATH=/tfod/models/research/cocoapi
PYTHON_API_PATH=$COCO_API_PATH/PythonAPI
echo "$PYTHON_API_PATH"