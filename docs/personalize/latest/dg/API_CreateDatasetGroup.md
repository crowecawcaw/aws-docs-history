# CreateDatasetGroup

Creates an empty dataset group. A dataset group is a container for
Amazon Personalize resources. A dataset group can contain at most three datasets, one
for each type of dataset:

- Item interactions
- Items
- Users
- Actions
- Action interactions
  A dataset group can be a Domain dataset group, where you specify a
  domain and use pre-configured resources like recommenders, or a
  Custom dataset group, where you use custom resources, such as a solution
  with a solution version, that you deploy with a campaign. If you start
  with a Domain dataset group, you can still add custom resources such as
  solutions and solution versions trained with recipes for custom use cases
  and deployed with campaigns.

A dataset group can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE
  FAILED
- DELETE PENDING
  To get the status of the dataset group, call [DescribeDatasetGroup](API_DescribeDatasetGroup.md "API_DescribeDatasetGroup.md"). If the status shows as CREATE FAILED, the
  response includes a `failureReason` key, which describes why
  the creation failed.

###### Note

You must wait until the `status` of the dataset group is
`ACTIVE` before adding a dataset to the group.

You can specify an AWS Key Management Service (KMS) key to encrypt the datasets in
the group. If you specify a KMS key, you must also include an AWS Identity and Access Management
(IAM) role that has permission to access the key.

###### APIs that require a dataset group ARN in the request

- [CreateDataset](API_CreateDataset.md "API_CreateDataset.md")
- [CreateEventTracker](API_CreateEventTracker.md "API_CreateEventTracker.md")
- [CreateSolution](API_CreateSolution.md "API_CreateSolution.md")

###### Related APIs

- [ListDatasetGroups](API_ListDatasetGroups.md "API_ListDatasetGroups.md")
- [DescribeDatasetGroup](API_DescribeDatasetGroup.md "API_DescribeDatasetGroup.md")
- [DeleteDatasetGroup](API_DeleteDatasetGroup.md "API_DeleteDatasetGroup.md")

## Request Syntax

```
{
   "domain": "`string`",
   "kmsKeyArn": "`string`",
   "name": "`string`",
   "roleArn": "`string`",
   "tags": [
      {
         "tagKey": "`string`",
         "tagValue": "`string`"
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[domain](#API_CreateDatasetGroup_RequestSyntax "#API_CreateDatasetGroup_RequestSyntax")**

The domain of the dataset group. Specify a domain to create a
Domain dataset group. The domain you specify determines the default
schemas for datasets and the use cases available for recommenders. If you
don't specify a domain, you create a Custom dataset group with solution
versions that you deploy with a campaign.

Type: String

Valid Values: `ECOMMERCE | VIDEO_ON_DEMAND`

Required: No

**[kmsKeyArn](#API_CreateDatasetGroup_RequestSyntax "#API_CreateDatasetGroup_RequestSyntax")**

The Amazon Resource Name (ARN) of a AWS Key Management Service (KMS) key used to
encrypt the datasets.

Type: String

Length Constraints: Maximum length of 2048.

Pattern: `arn:aws.*:kms:.*:[0-9]{12}:key/.*`

Required: No

**[name](#API_CreateDatasetGroup_RequestSyntax "#API_CreateDatasetGroup_RequestSyntax")**

The name for the new dataset group.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: Yes

**[roleArn](#API_CreateDatasetGroup_RequestSyntax "#API_CreateDatasetGroup_RequestSyntax")**

The ARN of the AWS Identity and Access Management (IAM) role that has permissions to access
the AWS Key Management Service (KMS) key. Supplying an IAM role is only valid when also
specifying a KMS key.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

Required: No

**[tags](#API_CreateDatasetGroup_RequestSyntax "#API_CreateDatasetGroup_RequestSyntax")**

A list of [tags](tagging-resources.md "tagging-resources.md") to apply to the dataset group.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

## Response Syntax

```
{
   "datasetGroupArn": "***string***",
   "domain": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[datasetGroupArn](#API_CreateDatasetGroup_ResponseSyntax "#API_CreateDatasetGroup_ResponseSyntax")**

The Amazon Resource Name (ARN) of the new dataset group.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

**[domain](#API_CreateDatasetGroup_ResponseSyntax "#API_CreateDatasetGroup_ResponseSyntax")**

The domain for the new Domain dataset group.

Type: String

Valid Values: `ECOMMERCE | VIDEO_ON_DEMAND`

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**LimitExceededException**

The limit on the number of requests per second has been exceeded.

HTTP Status Code: 400

**ResourceAlreadyExistsException**

The specified resource already exists.

HTTP Status Code: 400

**TooManyTagsException**

You have exceeded the maximum number of tags you can apply to this resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/CreateDatasetGroup.md "../../../goto/cli2/personalize-2018-05-22/CreateDatasetGroup.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/CreateDatasetGroup.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/CreateDatasetGroup.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/CreateDatasetGroup.md "../../../goto/SdkForCpp/personalize-2018-05-22/CreateDatasetGroup.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/CreateDatasetGroup.md "../../../goto/SdkForGoV2/personalize-2018-05-22/CreateDatasetGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateDatasetGroup.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateDatasetGroup.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateDatasetGroup.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateDatasetGroup.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/CreateDatasetGroup.md "../../../goto/SdkForKotlin/personalize-2018-05-22/CreateDatasetGroup.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateDatasetGroup.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateDatasetGroup.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/CreateDatasetGroup.md "../../../goto/boto3/personalize-2018-05-22/CreateDatasetGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateDatasetGroup.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateDatasetGroup.md")
