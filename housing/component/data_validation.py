from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.artifact_entity import DataValidationArtifact
import os , sys
import pandas as pd
import numpy as np
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import json


class DataValidation:

    def __init__(self, data_validation_config: DataValidationConfig,
                 data_ingestion_artifact: DataIngestionArtifact):
        try:
            logging.info(f"{'='*20} Data Validation log started.{'='*20} \n\n")
            self.data_validation_config =  data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise HousingException(e, sys) from e
        
    def get_train_and_test_df(self):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df,test_df
        except Exception as e:
            raise HousingException(e, sys) from e

    
        
    def is_train_test_file_exists(self):
        try: 
            logging.info("Checking if training and test file is available")
            is_train_file_exist = False
            is_test_file_exist = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)

            is_available= is_train_file_exist and is_test_file_exist

            logging.info(f"is train and test file exists?-> {is_available}")

            if not is_available:
                    training_file = self.data_ingestion_artifact.train_file_path
                    testing_file = self.data_ingestion_artifact.test_file_path
                    message = f"Training file :{training_file} or Testing file: {testing_file}" \
                    "is not present"
                    raise Exception(message)
            return is_available
        except Exception as e:
            raise HousingException(e, sys) from e
    
    def detect_outliers(self):
        try:
            pass
        except Exception as e:
             raise HousingException(e, sys) from e
         
        
    def validate_dataset_schema(self)-> bool:
        try:
            validation_status =False


            validation_status =True
            return validation_status
        except Exception as e:
                raise HousingException(e, sys) from e
        
    
        
    
            
    def get_and_save_data_drift_report(self):
        try:
            report = Report(metrics=[DataDriftPreset()])

            # Load train and test data
            train_df, test_df = self.get_train_and_test_df()
            # ✅ Run the data drift report 
            report.run(reference_data=train_df, current_data=test_df)          
            
            #Convert the report to JSON
            report_dict = report.as_dict()

            def convert_numpy(obj):
                if isinstance(obj, np.bool_):  # Convert np.bool_ to bool
                    return bool(obj)
                if isinstance(obj, np.integer):  # Convert np.int_ to int
                    return int(obj)
                if isinstance(obj, np.floating):  # Convert np.float_ to float
                    return float(obj)
                return obj  # Return original object if no conversion needed
            
            # Save the report as a JSON file
            report_file_path = self.data_validation_config.report_file_path
            report_dir = os.path.dirname(report_file_path)
            os.makedirs(report_dir, exist_ok=True)

            
            # ✅ Save the JSON report with NumPy conversion

            with open(report_file_path, "w", encoding="utf-8") as report_file:
                 json.dump(report_dict, report_file, indent=6,default=convert_numpy)


            return report_dict
        except Exception as e:
            raise HousingException(e, sys) from e
        
    def save_data_drift_report_page(self):
        try:
            # ✅ Create the new Evidently report
            report = Report(metrics=[DataDriftPreset()])
             # ✅ Load train and test data
            train_df, test_df = self.get_train_and_test_df()

        # ✅ Run the data drift report
            report.run(reference_data=train_df, current_data=test_df)

        # ✅ Define the report file path
            report_page_file_path = self.data_validation_config.report_page_file_path
            report_page_dir = os.path.dirname(report_page_file_path)
            os.makedirs(report_page_dir, exist_ok=True)

            # ✅ Save the report as an HTML file
            report.save_html(report_page_file_path)
    

        except Exception as e:
             raise HousingException(e, sys) from e
        
    def is_data_drift_found(self)->bool:
        try:
            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()
            return True
        except Exception as e:
            raise HousingException(e,sys) from e
            
    def initiate_data_validation(self)-> DataValidationArtifact:
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()
            self.is_data_drift_found()

            data_validation_artifact = DataValidationArtifact(
                 schema_file_path=self.data_validation_config.schema_file_path,
                 report_file_path=self.data_validation_config.report_file_path,
                 report_page_file_path=self.data_validation_config.report_page_file_path,
                 is_validated=True,
                 message="Data Validation Performed Successfully."
            )
            logging.info(f"Data Validation Artifact: {data_validation_artifact}") 
            return data_validation_artifact
        except Exception as e:
                raise HousingException(e, sys) from e
        
    def __del__(self):
        logging.info(f"{'>>'*30}Data Valdaition log completed.{'<<'*30} \n\n")
        

            
        
        
        
            

        
            
