# describeImage

Get detailed information about an existing image.

###### Topics

- [Request syntax](#describe-image-request "#describe-image-request")
- [Request body](#describe-image-request-body "#describe-image-request-body")
- [Response syntax](#describe-image-response "#describe-image-response")
- [Response body](#describe-image-response-body "#describe-image-response-body")
- [Example](#describe-image-example "#describe-image-example")

## Request syntax

```
GET /v3/images/custom/{`imageId`}
{
  "region": "string"
}
```

## Request body

**imageId**

The ID of the image.

Type: string

Required: Yes

**region**

The AWS Region in which the image was created.

Type: string

Required: No

## Response syntax

```
{
  "imageId": "string",
  "region": "string",
  "version": "string",
  "imageBuildStatus": "BUILD_IN_PROGRESS",
  "imageBuildLogsArn": "string",
  "cloudformationStackStatus": "CREATE_IN_PROGRESS",
  "cloudformationStackStatusReason": "string",
  "cloudformationStackArn": "string",
  "creationTime": "2019-08-24T14:15:22Z",
  "cloudformationStackCreationTime": "2019-08-24T14:15:22Z",
  "cloudformationStackTags": [
    {
      "key": "string",
      "value": "string"
    }
  ],
  "imageConfiguration": {
    "url": "string"
  },
  "imagebuilderImageStatus": "PENDING",
  "imagebuilderImageStatusReason": "string",
  "ec2AmiInfo": {
    "amiId": "string",
    "tags": [
      {
        "key": "string",
        "value": "string"
      }
    ],
    "amiName": "string",
    "architecture": "string",
    "state": "PENDING",
    "description": "string"
  }
}
```

## Response body

**imageId**

The ID of the image to retrieve detailed information for.

Type: string

**imageBuildStatus**

The image build status.

Type: string

Valid values: `BUILD_IN_PROGRESS | BUILD_FAILED | BUILD_COMPLETE |
 DELETE_IN_PROGRESS | DELETE_FAILED | DELETE_COMPLETE`

**imageConfiguration**

**url**

The URL of the image configuration file.

Type: string

**region**

The AWS Region in which the image is created.

Type: string

**version**

The AWS ParallelCluster version that's used to build the image.

Type: string

**cloudformationStackArn**

The Amazon Resource Name (ARN) of the main CloudFormation stack.

Type: string

**cloudformationStackCreationTime**

The time when the CloudFormation stack was created.

Type: datetime

**cloudformationStackStatus**

The CloudFormation stack status.

Type: string

Valid values: `CREATE_IN_PROGRESS | CREATE_FAILED | CREATE_COMPLETE |
 ROLLBACK_IN_PROGRESS | ROLLBACK_FAILED | ROLLBACK_COMPLETE | DELETE_IN_PROGRESS |
 DELETE_FAILED | DELETE_COMPLETE | UPDATE_IN_PROGRESS |
 UPDATE_COMPLETE_CLEANUP_IN_PROGRESS | UPDATE_COMPLETE | UPDATE_ROLLBACK_IN_PROGRESS
 | UPDATE_ROLLBACK_FAILED | UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS |
 UPDATE_ROLLBACK_COMPLETE`

**cloudformationStackStatusReason**

The reason for the CloudFormation stack status.

Type: string

**cloudformationStackTags**

The list of tags for the CloudFormation stack.

**key**

The tag name.

Type: string

**value**

The tag value.

Type: string

**creationTime**

The times when the image was created.

Type: datetime

**ec2AmiInfo**

**amiId**

The Amazon EC2 AMI ID.

Type: string

**amiName**

The Amazon EC2 AMI name.

Type: string

**architecture**

The Amazon EC2 AMI architecture.

Type: string

**state**

The state of the Amazon EC2 AMI.

Type: string

Valid values: `PENDING | AVAILABLE | INVALID | DEREGISTERED | TRANSIENT
 | FAILED | ERROR`

**tags**

List of Amazon EC2 AMI Tags.

**key**

Tag name.

Type: string

**value**

Tag value.

Type: string

**imagebuilderImageStatus**

The ImageBuilder Image status.

Type: string

Valid values: `PENDING | CREATING | BUILDING | TESTING | DISTRIBUTING |
 INTEGRATING | AVAILABLE | CANCELLED | FAILED | DEPRECATED | DELETED`

**imagebuilderImageStatusReason**

The reason the ImageBuilder Image has that status.

Type: string

**imageBuildLogsArn**

The Amazon Resource Name (ARN) of the logs for the image build process.

Type: string

## Example

Python
Request

```
`$` `describe_image(`custom-image-id`)`
```

200 Response

```
`{
 "cloudformation_stack_arn": "arn:aws:cloudformation:us-east-1:123456789012:stack/custom-image-id/6accc570-b080-11ec-845e-0e2dc6386985",
 "cloudformation_stack_creation_time": datetime.datetime(2022, 3, 30, 23, 23, 33, 731000, tzinfo=tzlocal()),
 "cloudformation_stack_status": "CREATE_IN_PROGRESS",
 "cloudformation_stack_tags": [
 {
 "key": "parallelcluster:version", "value": "3.2.1"
 },
 {
 "key": "parallelcluster:image_name",
 "value": 'custom-image-id"
 },
 {
 "key": "parallelcluster:custom-image-id",
 "value": "custom-image-id"
 },
 {
 "key": 'parallelcluster:amzn-s3-demo-bucket",
 "value": '`amzn-s3-demo-bucket`"
 },
 {
 "key": "parallelcluster:s3_image_dir",
 "value": "parallelcluster/3.2.1/images/custom-image-id-1234567890abcdef0"
 },
 {
 "key": "parallelcluster:build_log",
 "value": "arn:aws:logs:us-east-1:123456789012:log-group:/aws/imagebuilder/ParallelClusterImage-custom-image-id"
 },
 {
 "key": "parallelcluster:build_config",
 "value": "s3://`amzn-s3-demo-bucket`/parallelcluster/3.2.1/images/custom-image-id-1234567890abcdef0/configs/image-config.yaml"
 }
 ],
 "image_build_logs_arn": "arn:aws:logs:us-east-1:123456789012:log-group:/aws/imagebuilder/ParallelClusterImage-alinux2-image",
 "image_build_status": "BUILD_IN_PROGRESS",
 "image_configuration": {
 "url": "https://`amzn-s3-demo-bucket`.s3.amazonaws.com/parallelcluster/3.2.1/images/custom-image-id-1234567890abcdef0/configs/image-config.yaml?..."
 },
 "image_id": 'custom-image-id',
 "imagebuilder_image_status": "PENDING",
 "region": "us-east-1",
 "version": "3.2.1"
}`
```
