# GetClusterSnapshot

Returns information about a specific elastic cluster snapshot

## Request Syntax

```
GET /cluster-snapshot/`snapshotArn` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[snapshotArn](#API_elastic_GetClusterSnapshot_RequestSyntax "#API_elastic_GetClusterSnapshot_RequestSyntax")**

The ARN identifier of the elastic cluster snapshot.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "snapshot": {
      "adminUserName": "***string***",
      "clusterArn": "***string***",
      "clusterCreationTime": "***string***",
      "kmsKeyId": "***string***",
      "snapshotArn": "***string***",
      "snapshotCreationTime": "***string***",
      "snapshotName": "***string***",
      "snapshotType": "***string***",
      "status": "***string***",
      "subnetIds": [ "***string***" ],
      "vpcSecurityGroupIds": [ "***string***" ]
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[snapshot](#API_elastic_GetClusterSnapshot_ResponseSyntax "#API_elastic_GetClusterSnapshot_ResponseSyntax")**

Returns information about a specific elastic cluster snapshot.

Type: [ClusterSnapshot](API_elastic_ClusterSnapshot.md "API_elastic_ClusterSnapshot.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

An exception that occurs when there are not sufficient permissions to perform an action.

**message**

An error message explaining why access was denied.

HTTP Status Code: 403

**InternalServerException**

There was an internal server error.

HTTP Status Code: 500

**ResourceNotFoundException**

The specified resource could not be located.

**message**

An error message describing the failure.

**resourceId**

The ID of the resource that could not be located.

**resourceType**

The type of the resource that could not be found.

HTTP Status Code: 404

**ThrottlingException**

ThrottlingException will be thrown when request was denied due to request throttling.

**retryAfterSeconds**

The number of seconds to wait before retrying the operation.

HTTP Status Code: 429

**ValidationException**

A structure defining a validation exception.

**fieldList**

A list of the fields in which the validation exception occurred.

**message**

An error message describing the validation exception.

**reason**

The reason why the validation exception occurred (one of `unknownOperation`,
`cannotParse`, `fieldValidationFailed`, or `other`).

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-elastic-2022-11-28/GetClusterSnapshot.md "../../../goto/cli2/docdb-elastic-2022-11-28/GetClusterSnapshot.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-elastic-2022-11-28/GetClusterSnapshot.md "../../../goto/DotNetSDKV4/docdb-elastic-2022-11-28/GetClusterSnapshot.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-elastic-2022-11-28/GetClusterSnapshot.md "../../../goto/SdkForCpp/docdb-elastic-2022-11-28/GetClusterSnapshot.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-elastic-2022-11-28/GetClusterSnapshot.md "../../../goto/SdkForGoV2/docdb-elastic-2022-11-28/GetClusterSnapshot.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/GetClusterSnapshot.md "../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/GetClusterSnapshot.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/GetClusterSnapshot.md "../../../goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/GetClusterSnapshot.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-elastic-2022-11-28/GetClusterSnapshot.md "../../../goto/SdkForKotlin/docdb-elastic-2022-11-28/GetClusterSnapshot.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-elastic-2022-11-28/GetClusterSnapshot.md "../../../goto/SdkForPHPV3/docdb-elastic-2022-11-28/GetClusterSnapshot.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-elastic-2022-11-28/GetClusterSnapshot.md "../../../goto/boto3/docdb-elastic-2022-11-28/GetClusterSnapshot.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/GetClusterSnapshot.md "../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/GetClusterSnapshot.md")
