On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Resource CSV file script

The script scans the source AWS account to get a list of active datasets and
their respective active model versions. The script writes the list to a CSV file
named _import_input_file\_{current_time}.csv_. You use the CSV
file as input to the next script ([Resource configuration script](bulk-import-resources-resource-configuration-script.md "bulk-import-resources-resource-configuration-script.md")).

The script populates the required fields and populates optional fields with `None`.
If desired, you can supply your own values. Make sure you match datasets with the
corresponding respective model version. You must not delete optional
columns from the CSV file.

- **Current_model_name** — (Required)
  The current name of the model in the source AWS account.
- **New_model_name** — (Required) A
  name for the model in the target AWS account. By default the model name is
  the current model name. You can rename the model, if desired.
- **Current_dataset_name** — (Required)
  The current name of the active dataset in the source AWS account. This is
  the dataset name related to the model populated in Current_model_name
  field.
- **New_dataset_name** — (Required) The
  name for the imported dataset in the target AWS account. By default the
  dataset name is the value in `Current_dataset_name`. You can
  rename the dataset, if desired. If you only want to import the model and not
  import the dataset, use the existing active dataset name that's in the target AWS account.
  Additionally change the value of `Source_dataset_arn` to `None`.
- **Version(s)** — (Required) The total
  number of versions that the model has.
- **Version_to_import** — (Required)
  The model version which will be imported. By default the script populates
  `Version_to_import` with the active model version. You can specify a different
  model version, if desired.
- **Import?(Yes/No)** — (Required)
  Specifies if the script will import the dataset and model. By default the
  value is `Yes` If you don't want to import the dataset and model, change the
  value to `No`.
- **Target_account_id** — (Required) The
  ID of the target AWS account ID to which the script will import the
  resources. You enter this value when you run the script, but you can change
  the value as desired.
- **Source_dataset_arn** — (Required)
  The ARN of the dataset that will be imported. At the target AWS account in
  case If you don’t want to the import dataset and just want to perform import
  model, do the following:
  - Change the value of `Source_dataset_arn` to
    `None`.
  - Change the value of `New_dataset_name` to the existing
    active dataset name, in the target AWS account.

- **Source_model_arn** — (Required)
  The ARN of the source model that the script will import.
- **Label_s3_bucket** — The
  name of the Amazon S3 bucket in the target AWS account where the label file exists. By
  default the script populates this value as `None`. We recommend that you leave this
  value unchanged, unless you want to use a different Amazon S3 bucket.
- **Label_s3_prefix** — The Amazon S3 bucket
  prefix path in the target AWS account where the label exists. By default the
  script populates this value as None. We recommend that you leave this value
  unchanged, unless you want to use a different Amazon S3 prefix.
- **Role_arn** — The ARN of the role
  that grants permission to read the label file at the target AWS account.
  By default the script populates this value as `None`. We
  recommend that you leave this value unchanged, unless you want to use a
  different role ARN.
- **kms_key_id** — The ID of
  the server-side AWS Key Management Service key. By default, the script populates this value as
  `None`. We recommend that you leave this value unchanged,
  unless you want to use a different server-side AWS KMS key ID.

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
