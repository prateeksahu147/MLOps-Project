Neural_Roots_Drive_Path=/Users/prateeksahu/Library/CloudStorage/GoogleDrive-rootsneural@gmail.com
Image_Path=$Neural_Roots_Drive_Path/.shortcut-targets-by-id/1J0Q7HiMFYw1FYbllt0uhOFSph5DOt7g2/PotholeCaseStudy/workspace/pothole_training/annotations/images/test
ls $Image_Path
Label_Map_Path=$Neural_Roots_Drive_Path/.shortcut-targets-by-id/1J0Q7HiMFYw1FYbllt0uhOFSph5DOt7g2/PotholeCaseStudy/workspace/pothole_training/annotations/label_map.pbtxt
Tf_Record=/Users/prateeksahu/PycharmProjects/MLOps-Project/data/preprocessed/tf_record/test.record
Csv_Path=/Users/prateeksahu/PycharmProjects/MLOps-Project/data/preprocessed/csv/train.csv
python3 test.py -x $Image_Path -l $Label_Map_Path -o $Tf_Record -c $Csv_Path
