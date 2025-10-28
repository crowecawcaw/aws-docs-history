# deleteImage

Initiate the deletion of the custom AWS ParallelCluster image.

###### Topics

- [Request syntax](#delete-image-request "#delete-image-request")
- [Request body](#delete-image-request-body "#delete-image-request-body")
- [Response syntax](#delete-image-response "#delete-image-response")
- [Response body](#delete-image-response-body "#delete-image-response-body")
- [Example](#delete-image-example "#delete-image-example")

## Request syntax

```
DELETE /v3/images/custom/{`imageId`}
{
  "force": boolean,
  "region": "string"
}
```

## Request body

**imageId**

The ID of the image.

Type: string

Required: Yes

**force**

If set to `true`, force the AMI delete. Use this parameter if there are instances
that use the AMI or if the AMI is shared. The default is `false`.

Type: boolean

Required: No

**region**

The AWS Region in which the image was created.

Type: string

Required: No

## Response syntax

```
{
  "image": {
    "imageId": "string",
    "ec2AmiInfo": {
      "amiId": "string"
    },
    "region": "string",
    "version": "string",
    "cloudformationStackArn": "string",
    "imageBuildStatus": "DELETE_IN_PROGRESS",
    "cloudformationStackStatus": "DELETE_IN_PROGRESS"
  }
}
```

## Response body

**image**

**cloudformationStackArn**

The Amazon resource name (ARN) of the main CloudFormation stack.

Type: string

**cloudformationStackStatus**

The CloudFormation stack status.

Type: string

Valid values: `CREATE_IN_PROGRESS | CREATE_FAILED | CREATE_COMPLETE |
 ROLLBACK_IN_PROGRESS | ROLLBACK_FAILED | ROLLBACK_COMPLETE |
 DELETE_IN_PROGRESS | DELETE_FAILED | DELETE_COMPLETE | UPDATE_IN_PROGRESS |
 UPDATE_COMPLETE_CLEANUP_IN_PROGRESS | UPDATE_COMPLETE |
 UPDATE_ROLLBACK_IN_PROGRESS | UPDATE_ROLLBACK_FAILED |
 UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS |
 UPDATE_ROLLBACK_COMPLETE`

**ec2AmiInfo**

**amiId**

The Amazon EC2 AMI ID.

Type: string

**imageBuildStatus**

The image build status.

Type: string

Valid values: `BUILD_IN_PROGRESS | BUILD_FAILED | BUILD_COMPLETE |
 DELETE_IN_PROGRESS | DELETE_FAILED | DELETE_COMPLETE`

**imageId**

The ID of the image.

Type: string

**region**

The AWS Region in which the image is created.

Type: string

**version**

The AWS ParallelCluster version that's used to build the image.

Type: string

## Example

Python
Request

```
`$` `delete_image(`custom-image-id`)`
```

200 Response

```
`{
 "image": {
 "image_build_status": "DELETE_IN_PROGRESS",
 "image_id": "custom-image-id",
 "region": "us-east-1",
 "version": "3.2.1"
 }
}`
```
