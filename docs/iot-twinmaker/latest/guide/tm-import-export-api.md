# Performing bulk import and export operations

This topic covers how to perform bulk import and export operations and how to handle errors
in your transfer jobs. It provides examples of transfer jobs using CLI commands.

The AWS IoT TwinMaker API Reference contains information on the [CreateMetadataTransferJob](../apireference/API_CreateMetadataTransferJob.md "../apireference/API_CreateMetadataTransferJob.md") and other API actions.

###### Topics

- [metadataTransferJob prerequisites](#tm-import-export-prereqs "#tm-import-export-prereqs")
- [IAM permissions](#tm-import-export-prereqs-permissions "#tm-import-export-prereqs-permissions")
- [Run a bulk operation](#tm-import-export-procedure "#tm-import-export-procedure")
- [Error handling](#tm-import-export-error-handling "#tm-import-export-error-handling")
- [Import metadata templates](#tm-import-metadata-templates "#tm-import-metadata-templates")
- [AWS IoT TwinMaker metadataTransferJob examples](#tm-import-export-cli-examples "#tm-import-export-cli-examples")

## metadataTransferJob prerequisites

Please complete the following prerequisites before you run a metadataTransferJob:

- Create an AWS IoT TwinMaker workspace. The workspace can be the import destination
  or export source for a metadataTransferJob. For information on creating a workspace
  see, [Create a workspace](twinmaker-gs-workspace.md "twinmaker-gs-workspace.md").
- Create an Amazon S3 bucket to store resources. For more information on using
  Amazon S3 see, [What is Amazon S3?](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md")

## IAM permissions

When you perform bulk operations you need to create an IAM policy with permissions
to allow for the exchange of AWS resources between Amazon S3, AWS IoT TwinMaker, AWS IoT SiteWise, and your
local machine. For more information on creating IAM policies, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md").

The policy statements for AWS IoT TwinMaker, AWS IoT SiteWise and Amazon S3 are listed here:

- **AWS IoT TwinMaker policy**:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:GetBucketLocation",
 "s3:ListBucket",
 "s3:AbortMultipartUpload",
 "s3:ListBucketMultipartUploads",
 "s3:ListMultipartUploadParts"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iottwinmaker:GetWorkspace",
 "iottwinmaker:CreateEntity",
 "iottwinmaker:GetEntity",
 "iottwinmaker:UpdateEntity",
 "iottwinmaker:GetComponentType",
 "iottwinmaker:CreateComponentType",
 "iottwinmaker:UpdateComponentType",
 "iottwinmaker:ListEntities",
 "iottwinmaker:ListComponentTypes",
 "iottwinmaker:ListTagsForResource",
 "iottwinmaker:TagResource",
 "iottwinmaker:UntagResource"
 ],
 "Resource": "*"
 }
 ]
}`

```

- **AWS IoT SiteWise policy**:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:GetBucketLocation",
 "s3:ListBucket",
 "s3:AbortMultipartUpload",
 "s3:ListBucketMultipartUploads",
 "s3:ListMultipartUploadParts"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iotsitewise:CreateAsset",
 "iotsitewise:CreateAssetModel",
 "iotsitewise:UpdateAsset",
 "iotsitewise:UpdateAssetModel",
 "iotsitewise:UpdateAssetProperty",
 "iotsitewise:ListAssets",
 "iotsitewise:ListAssetModels",
 "iotsitewise:ListAssetProperties",
 "iotsitewise:ListAssetModelProperties",
 "iotsitewise:ListAssociatedAssets",
 "iotsitewise:DescribeAsset",
 "iotsitewise:DescribeAssetModel",
 "iotsitewise:DescribeAssetProperty",
 "iotsitewise:AssociateAssets",
 "iotsitewise:DisassociateAssets",
 "iotsitewise:AssociateTimeSeriesToAssetProperty",
 "iotsitewise:DisassociateTimeSeriesFromAssetProperty",
 "iotsitewise:BatchPutAssetPropertyValue",
 "iotsitewise:BatchGetAssetPropertyValue",
 "iotsitewise:TagResource",
 "iotsitewise:UntagResource",
 "iotsitewise:ListTagsForResource"
 ],
 "Resource": "*"
 }
 ]
}`

```

- **Amazon S3 policy**:

```
{
    "Effect": "Allow",
    "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:GetBucketLocation",
        "s3:ListBucket",
        "s3:AbortMultipartUpload",
        "s3:ListBucketMultipartUploads",
        "s3:ListMultipartUploadParts"
    ],
    "Resource": "*"
}
```

Alternatively you can scope your Amazon S3 policy to only access a single Amazon S3
bucket, see the following policy.

**Amazon S3 single bucket scoped policy**

```
{
    "Effect": "Allow",
    "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:GetBucketLocation",
        "s3:ListBucket",
        "s3:AbortMultipartUpload",
        "s3:ListBucketMultipartUploads",
        "s3:ListMultipartUploadParts"
    ],
    "Resource": [
        "arn:aws:s3:::`bucket name`",
        "arn:aws:s3:::`bucket name`/*"
    ]
}
```

### Set access control for a metadataTransferJob

To control what kind of jobs a user can access, add the following IAM policy
to the role used to call AWS IoT TwinMaker.

###### Note

This policy only allows access to AWS IoT TwinMaker import and export jobs
that transfer resources to and from Amazon S3.

```
{
    "Effect": "Allow",
    "Action": [
        "iottwinmaker:*DataTransferJob*"
    ],
    "Resource": "*",
    "Condition": {
        "StringLikeIfExists": {
            "iottwinmaker:sourceType": [
                "s3",
                "iottwinmaker"
            ],
            "iottwinmaker:destinationType": [
                "iottwinmaker",
                "s3"
            ]
        }
    }
}
```

## Run a bulk operation

This section covers how to perform bulk import and export operations.

###### Import data from Amazon S3 to AWS IoT TwinMaker

1. Specify the resources you want to transfer using the AWS IoT TwinMaker metadataTransferJob
   schema. Create and store your schema file in your Amazon S3 bucket.

For example schemas, see [Import metadata templates](#tm-import-metadata-templates "#tm-import-metadata-templates"). 2. Create a request body and save it as a JSON file. The request body specifies
the source and destination for the transfer job. Make sure to specify your Amazon S3
bucket as the source and your AWS IoT TwinMaker workspace as the destination.

The following is an example of a request body:

```
{
    "metadataTransferJobId": "`your-transfer-job-Id`",
    "sources": [{
        "type": "s3",
        "s3Configuration": {
            "location": "arn:aws:s3:::`amzn-s3-demo-bucket`/your_import_data.json"
        }
    }],
    "destination": {
        "type": "iottwinmaker",
        "iotTwinMakerConfiguration": {
            "workspace": "arn:aws:iottwinmaker:us-east-1:111122223333:workspace/`your-worksapce-name`"
        }
    }
}
```

Record the file name you gave your request body, you will need it in the next
step. In this example the request body is named
`createMetadataTransferJobImport.json`. 3. Run the following CLI command to invoke `CreateMetadataTransferJob`
(replace the input-json file name with the name you gave your request body):

```
aws iottwinmaker create-metadata-transfer-job --region us-east-1 \
--cli-input-json file://createMetadataTransferJobImport.json
```

This creates a metadataTransferJob and begins the process of the transferring
your selected resources.

###### Export data from AWS IoT TwinMaker to Amazon S3

1. Create a JSON request body with the appropriate filters to choose the
   resources you want to export. For this example we use:

```
{
    "metadataTransferJobId": "`your-transfer-job-Id`",
    "sources": [{
        "type": "iottwinmaker",
        "iotTwinMakerConfiguration": {
            "workspace": "arn:aws:iottwinmaker:us-east-1:111122223333:workspace/`your-workspace-name`",
            "filters": [{
                "filterByEntity": {
                    "entityId": "parent"
                }},
                {
                "filterByEntity": {
                    "entityId": "child"
                }},
                {
                "filterByComponentType": {
                    "componentTypeId": "component.type.minimal"
                }}
            ]
        }
    }],
    "destination": {
        "type": "s3",
        "s3Configuration": {
            "location": "arn:aws:s3:::`amzn-s3-demo-bucket`"
        }
    }
}
```

The `filters` array lets you specify which resources will be
exported. In this example we filter by `entity`, and
`componentType`.

Make sure to specify your AWS IoT TwinMaker workspace as the source and your Amazon S3
bucket as the destination of the metadata transfer job.

Save your request body and record the file name, you will need it in the
next step. For this example, we named our request body
`createMetadataTransferJobExport.json`. 2. Run the following CLI command to invoke `CreateMetadataTransferJob`
(replace the input-json file name with the name you gave your request body):

```
aws iottwinmaker create-metadata-transfer-job --region us-east-1 \
--cli-input-json file://createMetadataTransferJobExport.json
```

This creates a metadataTransferJob and begins the process of the transferring
your selected resources.

To check or update the status of a transfer job, use the following commands:

- To cancel a job use the [CancelMetadataTransferJob](../apireference/API_CancelMetadataTransferJob.md "../apireference/API_CancelMetadataTransferJob.md") API action. When you call CancelMetadataTransferJob,
  the API only cancels a running metadataTransferJob, and any resources already exported
  or imported are not affected by this API call.
- To retrieve information on a specific job use the [GetMetadataTransferJob](../apireference/API_GetMetadataTransferJob.md "../apireference/API_GetMetadataTransferJob.md") API action.

Or, you can call GetMetadataTransferJob on an existing transfer job with the
following CLI command:

```
aws iottwinmaker get-metadata-transfer-job --job-id `ExistingJobId`
```

If you call GetMetadataTransferJob on a non-existing AWS IoT TwinMaker import or export
job, you get a `ResourceNotFoundException` error in response.

- To list current jobs, use the [ListMetadataTransferJobs](../apireference/API_ListMetadataTransferJobs.md "../apireference/API_ListMetadataTransferJobs.md") API action.

Here is a CLI example that calls ListMetadataTransferJobs with AWS IoT TwinMaker as the
destinationType and `s3` as the sourceType:

```
aws iottwinmaker list-metadata-transfer-jobs --destination-type iottwinmaker --source-type s3
```

###### Note

You can change the values for the sourceType and destinationType
parameters to match your import or export job's source and destination.

For more examples of CLI commands that invoke these API actions, see
[AWS IoT TwinMaker metadataTransferJob examples](#tm-import-export-cli-examples "#tm-import-export-cli-examples").

If you encounter any errors during the transfer job, see
[Error handling](#tm-import-export-error-handling "#tm-import-export-error-handling").

## Error handling

After you create and run a transfer job, you can call GetMetadataTransferJob
to diagnose any errors that occurred:

```
aws iottwinmaker get-metadata-transfer-job \
--metadata-transfer-job-id `your_metadata_transfer_job_id` \
--region us-east-1
```

Once you see the state of the job turn to `COMPLETED`, you can verify
the results of the job. GetMetadataTransferJob returns an object called
[`MetadataTransferJobProgress`](../apireference/API_MetadataTransferJobProgress.md "../apireference/API_MetadataTransferJobProgress.md") which contains the following fields:

- **failedCount:** Indicates the number of resources
  that failed during the transfer process.
- **skippedCount:** Indicates the number of resources
  that were skipped during the transfer process.
- **succeededCount:** Indicates the number of
  resources that succeeded during the transfer process.
- **totalCount:** Indicates the total count of
  resources involved in the transfer process.

Additionally, a reportUrl element is returned which contains a pre-signed URL.
If your transfer job has errors you wish to investigate further, then you can download a full
error report using this URL.

## Import metadata templates

You can import many components, componentTypes, or entities with a single bulk import
operation. The examples in this section show how to do this.

template: Importing entities
Use the following template format for a job that imports entities:

```
{
  "entities": [
    {
      "description": "string",
      "entityId": "string",
      "entityName": "string",
      "parentEntityId": "string",
      "tags": {
        "string": "string"
      },
      "components": {
        "string": {
          "componentTypeId": "string",
          "description": "string",
          "properties": {
            "string": {
              "definition": {
                "configuration": {
                  "string": "string"
                },
                "dataType": "DataType",
                "defaultValue": "DataValue",
                "displayName": "string",
                "isExternalId": "boolean",
                "isRequiredInEntity": "boolean",
                "isStoredExternally": "boolean",
                "isTimeSeries": "boolean"
              },
              "value": "DataValue"
            }
          },
          "propertyGroups": {
            "string": {
              "groupType": "string",
              "propertyNames": [
                "string"
              ]
            }
          }
        }
      }
    }
  ]
}
```

template: Importing componentTypes
Use the following template format for a job that imports componentTypes:

```
{
  "componentTypes": [
    {
      "componentTypeId": "string",
      "componentTypeName": "string",
      "description": "string",
      "extendsFrom": [
        "string"
      ],
      "functions": {
        "string": {
          "implementedBy": {
            "isNative": "boolean",
            "lambda": {
              "functionName": "`Telemetry-tsDataReader`",
              "arn": "`Telemetry-tsDataReaderARN`"
            }
          },
          "requiredProperties": [
            "string"
          ],
          "scope": "string"
        }
      },
      "isSingleton": "boolean",
      "propertyDefinitions": {
        "string": {
          "configuration": {
            "string": "string"
          },
          "dataType": "DataType",
          "defaultValue": "DataValue",
          "displayName": "string",
          "isExternalId": "boolean",
          "isRequiredInEntity": "boolean",
          "isStoredExternally": "boolean",
          "isTimeSeries": "boolean"
        }
      },
      "propertyGroups": {
        "string": {
          "groupType": "string",
          "propertyNames": [
            "string"
          ]
        }
      },
      "tags": {
        "string": "string"
      }
    }
  ]
}
```

template: Importing components
Use the following template format for a job that imports components:

```
{
  "entityComponents": [
    {
      "entityId": "string",
      "componentName": "string",
      "componentTypeId": "string",
      "description": "string",
      "properties": {
        "string": {
          "definition": {
            "configuration": {
              "string": "string"
            },
            "dataType": "DataType",
            "defaultValue": "DataValue",
            "displayName": "string",
            "isExternalId": "boolean",
            "isRequiredInEntity": "boolean",
            "isStoredExternally": "boolean",
            "isTimeSeries": "boolean"
          },
          "value": "DataValue"
        }
      },
      "propertyGroups": {
        "string": {
          "groupType": "string",
          "propertyNames": [
            "string"
          ]
        }
      }
    }
  ]
}
```

## AWS IoT TwinMaker metadataTransferJob examples

Use the following commands to manage your metadata transfers:

- [CreateMetadataTransferJob](../apireference/API_CreateMetadataTransferJob.md "../apireference/API_CreateMetadataTransferJob.md") API action.

CLI command example:

```
aws iottwinmaker create-metadata-transfer-job --region us-east-1 \
--cli-input-json file://`yourTransferFileName`.json
```

- To cancel a job use the [CancelMetadataTransferJob](../apireference/API_CancelMetadataTransferJob.md "../apireference/API_CancelMetadataTransferJob.md") API action.

CLI command example:

```
aws iottwinmaker cancel-metadata-transfer-job
--region us-east-1 \
--metadata-transfer-job-id `job-to-cancel-id`
```

When you call CancelMetadataTransferJob, it only cancels a specific
metadata transfer job, and any resources already exported or imported are not
affected.

- To retrieve information on a specific job use the [GetMetadataTransferJob](../apireference/API_GetMetadataTransferJob.md "../apireference/API_GetMetadataTransferJob.md") API action.

CLI command example:

```
aws iottwinmaker get-metadata-transfer-job \
--metadata-transfer-job-id `your_metadata_transfer_job_id` \
--region us-east-1 \
```

- To list current jobs use the [ListMetadataTransferJobs](../apireference/API_ListMetadataTransferJobs.md "../apireference/API_ListMetadataTransferJobs.md") API action.

You can filter the results returned by ListMetadataTransferJobs using a JSON
file. See the following procedure using the CLI:

    1. Create a CLI input JSON file to specify the filters you want to use:



    ```
    {
        "sourceType": "s3",
        "destinationType": "iottwinmaker",
        "filters": [{
            "workspaceId": "workspaceforbulkimport"
        },
        {
            "state": "COMPLETED"
        }]
    }
    ```

    Save it and record the file name, you will need it when entering
     the CLI command.
    2. Use the JSON file as an argument to the following CLI command:



    ```
    aws iottwinmaker list-metadata-transfer-job --region us-east-1 \
    --cli-input-json file://ListMetadataTransferJobsExample.json
    ```
