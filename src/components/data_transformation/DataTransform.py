from dataclasses import dataclass
import os
from src.components.data_transformation.TfRecord import TfRecord
import  tensorflow as tf
from settings import BASE_DIR

@dataclass
class DataTransformConfig:
    image_dir: str = os.path.join(BASE_DIR, 'data', 'pdf')
    csv_path: str = os.path.join(BASE_DIR, 'data', "image")
    output_path: str = os.path.join(BASE_DIR, 'data', "csv")
    xml_dir: str = os.path.join(BASE_DIR, 'data', "csv")
    labels_path: str = os.path.join(BASE_DIR, 'data', "csv")


class DataTransform:
    def __int__(self):
        self.data_transform_config=DataTransformConfig()
        self.tf_record_obj=TfRecord(self.label_map)
        if self.data_transform_config.image_dir is None:
            self.image_dir = self.data_transform_config.xml_dir

    def transform(self):
        writer = tf.python_io.TFRecordWriter(self.data_transform_config.output_path)
        path = os.path.join(self.data_transform_configimage_dir)
        examples = self.tf_record_obj.xml_to_csv(self.data_transform_configxml_dir)
        grouped = self.tf_record_obj.split(examples, 'filename')

        for group in grouped:
            try:
                tf_example = self.tf_record_obj.create_tf_example(group, path)
                writer.write(tf_example.SerializeToString())
            except Exception as e:
                raise e
        writer.close()
        print('Successfully created the TFRecord file: {}'.format(self.data_transform_config.output_path))
        if self.data_transform_config.csv_path is not None:
            examples.to_csv(self.data_transform_config.csv_path, index=None)
            print('Successfully created the CSV file: {}'.format(self.data_transform_config.csv_path))

