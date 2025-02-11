from housing.pipeline.pipeline import Pipeline
from housing.config.configuration import Configuration  # Adjust import as needed
from housing.logger import logging

logging.info("🚀 Starting the script...")

config = Configuration()  # Load configuration
pipeline = Pipeline(config=config)  # Pass the config
print("✅ Running pipeline...")
pipeline.run_pipeline()
logging.info("🎯 Pipeline execution completed!")
