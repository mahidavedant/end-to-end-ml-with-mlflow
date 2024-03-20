"""
src/mlProject/components/data_validation.py

Data Validation.
"""
# 6. Update the components
import pandas as pd
from mlProject.logging.customLogger import logger
from mlProject.entity.config_entity import DataValidationConfig

class DataValidation:
  def __init__(self, config: DataValidationConfig):
    self.config = config

  def validate_all_columns(self) -> bool:
    try:
      validation_status = None

      data = pd.read_csv(self.config.unzip_data_dir)
      all_columns = list(data.columns)
      all_dtypes = [data[col].dtype for col in all_columns]

      all_schema = self.config.all_schema.keys()

      # Validate if all columns are present with correct datatypes
      for col, dtype in zip(all_columns, all_dtypes):
        # set status to False if not validated schema and write to status file
        # else (true) write to status file
        if col not in all_schema or dtype != self.config.all_schema[col]:
          validation_status = False
          with open(self.config.STATUS_FILE, 'w') as f:
            f.write(f"Validation Status: {validation_status}")
        else:
          validation_status = True
          with open(self.config.STATUS_FILE, 'w') as f:
            f.write(f"Validation Status: {validation_status}")

      return validation_status

    except Exception as e:
      raise e
