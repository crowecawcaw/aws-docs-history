On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Bulk import script

This script scans the CSV file that the [Resource CSV file script](bulk-import-resources-resource-generation-script.md "bulk-import-resources-resource-generation-script.md") creates. For
each row the script calls `ImportDataset` on the source dataset ARN.
After the dataset import successfully finishes, the script then calls
`ImportModelVersion` on the dataset’s respective model version. If
desired, you can call `ImportModelVersion` on an existing active dataset
by populating the existing dataset name in the columns
`Current_dataset_name` and `New_dataset_name`. You must
also set the `Source_dataset_arn` value to `None`.

The script outputs an import results CSV file (_import_result_file\_{current_time}.csv_) that lists the following:

- **Source_resource_arn** — The ARN of the source dataset or source model.
- **Is_import_successful?** — Yes, if the resource import was successful. Otherwise, No.
- **type** — The type of the dataset (`dataset` or `model_version`).
- **Source_resource_name** — The name of the source resource.
- **New resource_name** — The new name for the resource in the target AWS account.
- **Version_to_import** — The model version in the source AWS account that was identified for import.
- **Failed_reason** — If the value of `Is_import_successful` is `No`, provides a reason for the failure.

## Script

```
import boto3
import os
import csv
import time
import string
import random
import json
from botocore.config import Config
from datetime import datetime
import sys
import datetime


def activate_model_version(model_name, version, model_version_arn):
    try:
        response = lookoutequipment_client.update_active_model_version(
            ModelName=model_name, ModelVersion=version)
        print("Activated the model version: {} for the copied model:{}:".format(
            version, model_name))
    except Exception as e:
        print("Error while activating the model version:", e)
        with open(final_result_file, "a") as f:
            f.write(f"{model_version_arn},No,{e}\n")


config = Config(connect_timeout=30, read_timeout=30,
                retries={'max_attempts': 3})
region_name = input(
    "Please enter the region to run the script('us-east-1', 'ap-northeast-2', 'eu-west-1'): ")

lookoutequipment_client = boto3.client(
    service_name='lookoutequipment',
    region_name=region_name,
    config=config,
    endpoint_url=f'https://lookoutequipment.{region_name}.amazonaws.com'
)

labels_configuration = {
    'S3InputConfiguration': {
        'Bucket': 's3-amzn-demo-bucket',
        'Prefix': 'path/to/label_files/'
    }
}


source_input_file = input(
    "Please enter the source file name to start the import: ")
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")
final_result_file = f"import_result_file_{formatted_time}.csv"

with open(final_result_file, "a") as f:
    f.write("Source_resource_arn,Is_import_successful?,Type,Source_resource_name,New_resource_name,Version_to_import,Failed_reason" + '\n')
with open(source_input_file) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        client_token = ''.join(random.choices(
            string.ascii_lowercase + string.digits, k=10))
        if len(row) < 14 or len(row) > 14:
            print(
                "Skipping this Row as it doesn't match the format: Current_model_name,New_model_name,Current_dataset_Name,New_dataset_name,Version(s),Version_to_import,Import?(yes/no),Target_account_id,Source_dataset_arn,Source_model_arn,Label_s3_bucket,Label_s3_prefix,Role_arn,kms_key_id")
            continue
        if row[6].lower() == "no":
            print(f"skipping import for model {row[9]}")
            with open(final_result_file, "a") as f:
                f.write(
                    f"{row[9]},No,skipped import as the input file says 'no' for import\n")
            continue
        if row[0] == "Current_model_name" and row[1] == "New_model_name":
            continue
        is_dataset_import_success = True
        # import dataset logic
        if 'dataset' in row[8]:
            is_dataset_import_success = False
            print("Triggering import for dataset:", row[8])
            datasetnamefinal = None
            if row[3] == "None":
                datasetnamefinal = row[8].split(":")[5].split("/")[1]
            else:
                datasetnamefinal = row[3]
            import_status = None

            request = {
                'SourceDatasetArn': row[8],
                'DatasetName': datasetnamefinal,
                'ClientToken': client_token
            }

            if row[13] != "None":
                request['ServerSideKmsKeyId'] = row[13]

            try:
                response = lookoutequipment_client.import_dataset(**request)
                print("Latest response for the import dataset is:", response)
                import_status = response.get("Status")
                if import_status == "SUCCESS":
                    is_dataset_import_success = True
            except Exception as e:
                print("Error while importing a dataset:", e)
                with open(final_result_file, "a") as f:
                    f.write(
                        f"{row[8]},No,dataset,{row[2]},{row[3]},None,{e}\n")
                continue

            timeout_seconds = 900  # 15 minutes in seconds
            start_time = time.time()
            print("Latest import_status for dataset is:", import_status)
            while import_status != "SUCCESS" and is_dataset_import_success != True:
                response = lookoutequipment_client.import_dataset(**request)
                print("Latest response for the import dataset is:", response)
                import_status = response.get("Status")
                if import_status == "SUCCESS":
                    is_dataset_import_success = True
                    print("Import dataset completed for arn:", row[8])
                    with open(final_result_file, "a") as f:
                        f.write(
                            f"{row[8]},Yes,dataset,{row[2]},{row[3]},None,\n")
                if import_status == "FAILED":
                    print("import dataset has failed hence skipping the import model")
                    with open(final_result_file, "a") as f:
                        f.write(
                            f"{row[8]},No,dataset,{row[2]},{row[3]},None,check ingestion job {response.get('JobId')} failure reason\n")
                    continue
                elapsed_time = time.time() - start_time
                if elapsed_time >= timeout_seconds:
                    print("Timeout reached. Exiting..")
                    is_dataset_import_success = False
                    with open(final_result_file, "a") as f:
                        f.write(
                            f"{row[8]},No,dataset,{row[2]},{row[3]},None,Timed out checking the success status for import\n")
                    continue

                time.sleep(15)

        # import model logic
        if 'model' in row[9] and is_dataset_import_success:
            is_model_import_success = False
            model_version_arn = row[9] + "/model-version/" + row[5]
            print("Triggering import for model version:", model_version_arn)
            new_model_name = row[1]
            request = {
                'SourceModelVersionArn': model_version_arn,
                'DatasetName': datasetnamefinal,
                'ModelName': new_model_name,
                'ClientToken': client_token
            }

            if row[13] != "None":
                request['ServerSideKmsKeyId'] = row[13]

            if row[12] != "None":
                request['RoleArn'] = row[12]

            if row[10] != "None" and row[11] != "None":
                # populate label bucket and prefix if provided
                labels_configuration['S3InputConfiguration']['Bucket'] = row[10]
                labels_configuration['S3InputConfiguration']['Prefix'] = row[11]
                request['LabelsInputConfiguration'] = labels_configuration

            import_status = None

            try:
                response = lookoutequipment_client.import_model_version(
                    **request)
                print("Latest response for the import model is:", response)
                import_status = response.get("Status")
                if import_status == "SUCCESS":
                    is_model_import_success = True
            except Exception as e:
                print("Error while importing the model:", e)
                with open(final_result_file, "a") as f:
                    f.write(
                        f"{model_version_arn},No,model_version,{row[0]},{row[1]},{row[5]},{e}\n")
                continue

            timeout_seconds = 900  # 15 minutes in seconds
            start_time = time.time()
            while import_status != "SUCCESS" and is_model_import_success != True:
                response = lookoutequipment_client.import_model_version(
                    **request)
                import_status = response.get("Status")
                print("Latest response for the import model is:", response)
                if import_status == "SUCCESS":
                    is_model_import_success = True
                    activate_model_version(response.get("ModelName"), response.get(
                        "ModelVersion"), model_version_arn)
                    with open(final_result_file, "a") as f:
                        f.write(
                            f"{model_version_arn},Yes,model_version,{row[0]},{row[1]},{row[5]},None\n")
                if import_status == "FAILED":
                    print("Import model failed for arn:", model_version_arn)
                    with open(final_result_file, "a") as f:
                        f.write(
                            f"{model_version_arn},No,model_version,{row[0]},{row[1]},{row[5]},check model version arn {response.get('ModelVersionArn')} details to know the failure reason\n")
                    continue

                elapsed_time = time.time() - start_time
                if elapsed_time >= timeout_seconds:
                    print("Timeout reached. Exiting..")
                    with open(final_result_file, "a") as f:
                        f.write(
                            f"{model_version_arn},No,Timed out checking the success status for import\n")
                    continue

                time.sleep(15)

            print("Import model completed for arn:", model_version_arn)
print(
    f"Import for all the dataset/models in the input file is completed, Check the results file {final_result_file} for details")

```
