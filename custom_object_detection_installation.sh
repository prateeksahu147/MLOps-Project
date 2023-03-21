# Protobuf Installation/Compilation*
TFOD_PATH=./tfod

if [ -d "$TFOD_PATH" ];
then
    echo "Custom object detection source code already exist at '$RESEARCH_DIR_PATH'."
else
	echo "Cloning Custom object detection source code from TFOD API"
	mkdir tfod
	cd tfod
	git clone https://github.com/tensorflow/models.git
	cd .. || exit
fi

#==============================================*
# Protobuf Installation/Compilation*
#==============================================*
RESEARCH_DIR_PATH=./tfod/models/research
PROTOS_PY_FILE=./tfod/models/research/object_detection/protos/*.py
PROTOS_FILE=./tfod/models/research/object_detection/protos/*.proto

if [ -e "$PROTOS_PY_FILE" ];
then
    echo "Conversion from .proto files to .py is already done..."
else
  cd ./tfod/models/research/ || exist
  sudo protoc object_detection/protos/*.proto --python_out=.
  echo "Protoc files complied for custom object detection modeling."
  cd - || exit
fi
#cd $RESEARCH_DIR_PATH || exit
#var=$(pwd)
#echo "The current working directory $var."
#sudo protoc object_detection/protos/*.proto --python_out=.
#echo "Protoc files complied for custom object detection modeling."
#cd -

#==============================================*
# COCO API installation
#==============================================*
COCO_API_PATH=/tfod/models/research/cocoapi
PYTHON_API_PATH=$COCO_API_PATH/PythonAPI

if [ -d "$COCO_API_PATH" ];
then
  echo "COCO API already exist at '$COCO_API_PATH'."
else
	echo "Cloning COCO API"

	git clone https://github.com/cocodataset/cocoapi.git $COCO_API_PATH
  # Use for Compilation
  sudo make $PYTHON_API_PATH
fi

#==============================================*
# Custom TFOD package installation
#==============================================*
SETUP_PY_FILE=$RESEARCH_DIR_PATH/setup.py


if [ -e "$SETUP_PY_FILE" ];
then
    echo "setup.py already exist at '$SETUP_PY_FILE'."
else
	echo "Copy setup.py from object_detection/packages/tf2/ to research"
  cp $RESEARCH_DIR_PATH/object_detection/packages/tf2/setup.py $RESEARCH_DIR_PATH
fi

if [ -e "$SETUP_PY_FILE" ];
then
    cd $RESEARCH_DIR_PATH || exit
    python3 -m pip install .
    python3 $RESEARCH_DIR_PATH/object_detection/builders/model_builder_tf2_test.py
    cd -
fi





