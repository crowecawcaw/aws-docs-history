On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Resource configuration script

This script configures the resource policies to let the target AWS
account bulk import the resources. By using the CSV file
(_import_input_file\_{current_time}.csv_ ) that the [Resource CSV file script](bulk-import-resources-resource-generation-script.md "bulk-import-resources-resource-generation-script.md") creates, the script configures the resource policy for each dataset and model
version ARN. The script updates existing resource policies for source datasets and
model version ARNs to grant permissions to the target AWS account, along with any
existing conditions.

After running this script, you can bulk import resources to the target AWS
account by running the [Bulk import script](bulk-import-trigger-script.md "bulk-import-trigger-script.md").

## Script

```
import boto3
import os
import csv
import time
import json
from botocore.config import Config
from datetime import datetime
import sys
import datetime


# By default these optional parameters are populated as None
label_s3_bucket = "None"
label_s3_prefix = "None"
kms_key_id = "None"
role_arn = "None"


def getTotalNumberOfModelVersions(model_name):
    total_length = 0
    try:
        response = lookoutequipment_client.list_model_versions(
            ModelName=model_name)
        total_length = len(response.get('ModelVersionSummaries'))
        next_token = response.get("NextToken")
        while next_token is not None:
            response = lookoutequipment_client.list_model_versions(
                ModelName=model_name, NextToken=next_token)
            next_token += len(response.get('ModelVersionSummaries'))
        return total_length
    except Exception as e:
        print("Exception thrown while listing models for model name:", model_name)


config = Config(connect_timeout=30, read_timeout=30,
                retries={'max_attempts': 3})
region_name = input(
    "Please enter the region to run the script('us-east-1', 'ap-northeast-2', 'eu-west-1'): ")

lookoutequipment_client = boto3.client(
    service_name='lookoutequipment',
    region_name=region_name,
    config=config,
    endpoint_url='https://lookoutequipment.{region_name}.amazonaws.com'.format(
        region_name=region_name),
)


response = lookoutequipment_client.list_models()
target_account = None
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"import_input_file_{formatted_time}.csv"
target_account = input("Please enter the target account id: ")
if len(target_account) != 12:
    print("Target account id is not valid hence terminating the script execution..")
    sys.exit()
with open(file_name, "a") as f:
    f.write("Current_model_name,New_model_name,Current_dataset_name,New_dataset_name,Version(s),Version_to_import,Import?(yes/no),Target_account_id,Source_dataset_arn,Source_model_arn,Label_s3_bucket,Label_s3_prefix,Role_arn,kms_key_id" + '\n')
for model in response.get('ModelSummaries'):
    with open(file_name, "a") as f:
        f.write(model.get('ModelName') + "," + model.get('ModelName') + "," + model.get('DatasetName') + "," + model.get('DatasetName') + "," + str(getTotalNumberOfModelVersions(model.get('ModelName'))) + "," + str(model.get(
            'ActiveModelVersion')) + "," + "yes" + "," + target_account + "," + model.get('DatasetArn') + "," + model.get('ModelArn') + "," + label_s3_bucket + "," + label_s3_prefix + "," + role_arn + "," + kms_key_id + '\n')
next_token = response.get("NextToken")
while next_token is not None:
    response = lookoutequipment_client.list_models(NextToken=next_token)
    for model in response.get('ModelSummaries'):
        with open(file_name, "a") as f:
            f.write(model.get('ModelName') + "," + model.get('ModelName') + "," + model.get('DatasetName') + "," + model.get('DatasetName') + "," + str(getTotalNumberOfModelVersions(model.get('ModelName'))) + "," + str(model.get(
                'ActiveModelVersion')) + "," + "yes" + "," + target_account + "," + model.get('DatasetArn') + "," + model.get('ModelArn') + "," + label_s3_bucket + "," + label_s3_prefix + "," + role_arn + "," + kms_key_id + '\n')
    next_token = response.get("NextToken")

print("All the active models have been scanned and written to a file:", file_name)

```
