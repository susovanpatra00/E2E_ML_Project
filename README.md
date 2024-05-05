## Wine Quality Prediction

1. Create Python Environment
2. Connect to github repo
3. Create the file 'template.py'
4. Create other files using the 'template.py'
5. Update 'requirements.txt'
6. Update 'setup.py'
7. Install Libraries for the environment using 'requirements.txt'
8. Implement Logging in the src __init__.py as it will work for all inside the src
9. Implement commonly used functions in utils/common.py 
10. Now create a file '01_data_ingestion.ipynb' inside research for data ingestion research part.
11. Our workflow is 1st config.yaml and as we will work for data ingestion,,we need to update the 
    config.yaml for data ingestion related config
12. We will update the src/constants/__init__.py ,, we will give the paths to the config, schema and 
    params.yaml files
13. We will complete the whole Data Ingestion process inside the '01_data_ingestion.ipynb'
    (Entity -> Configuration Manager -> Components -> Pipeline)
14. Now we will just copy paste the portions to their respective places
    (Entity -> src/entity/config_entity.py) (Configuration Manager -> src/config/configuration.py)
    (Components -> src/components/data_ingestion.py) 
    (Pipeline -> src/pipeline/stage_01_data_ingestion.py)
15. 






### Workflows
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml