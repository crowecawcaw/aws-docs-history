# StopSearchJob

This operations ends a search job.

Only a search job with a status of `RUNNING`
can be stopped.

## Request Syntax

```
PUT /search-jobs/`SearchJobIdentifier`/actions/cancel HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[SearchJobIdentifier](#API_BKS_StopSearchJob_RequestSyntax "#API_BKS_StopSearchJob_RequestSyntax")**

The unique string that specifies the search job.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You do not have sufficient access to perform this action.

**message**

User does not have sufficient access to perform this action.

HTTP Status Code: 403

**ConflictException**

This exception occurs when a conflict with a previous successful
operation is detected. This generally occurs when the previous
operation did not have time to propagate to the host serving the
current request.

A retry (with appropriate backoff logic) is the recommended
response to this exception.

**message**

Updating or deleting a resource can cause an inconsistent state.

**resourceId**

Identifier of the resource affected.

**resourceType**

Type of the resource affected.

HTTP Status Code: 409

**InternalServerException**

An internal server error occurred. Retry your request.

**message**

Unexpected error during processing of request.

**retryAfterSeconds**

Retry the call after number of seconds.

HTTP Status Code: 500

**ResourceNotFoundException**

The resource was not found for this request.

Confirm the resource information, such as the ARN or type is correct
and exists, then retry the request.

**message**

Request references a resource which does not exist.

**resourceId**

Hypothetical identifier of the resource affected.

**resourceType**

Hypothetical type of the resource affected.

HTTP Status Code: 404

**ThrottlingException**

The request was denied due to request throttling.

**message**

Request was unsuccessful due to request throttling.

**quotaCode**

This is the code unique to the originating service with the quota.

**retryAfterSeconds**

Retry the call after number of seconds.

**serviceCode**

This is the code unique to the originating service.

HTTP Status Code: 429

**ValidationException**

The input fails to satisfy the constraints specified by a service.

**message**

The input fails to satisfy the constraints specified by an Amazon service.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backupsearch-2018-05-10/StopSearchJob.md "../../../goto/cli2/backupsearch-2018-05-10/StopSearchJob.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backupsearch-2018-05-10/StopSearchJob.md "../../../goto/DotNetSDKV3/backupsearch-2018-05-10/StopSearchJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backupsearch-2018-05-10/StopSearchJob.md "../../../goto/SdkForCpp/backupsearch-2018-05-10/StopSearchJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backupsearch-2018-05-10/StopSearchJob.md "../../../goto/SdkForGoV2/backupsearch-2018-05-10/StopSearchJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backupsearch-2018-05-10/StopSearchJob.md "../../../goto/SdkForJavaV2/backupsearch-2018-05-10/StopSearchJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backupsearch-2018-05-10/StopSearchJob.md "../../../goto/SdkForJavaScriptV3/backupsearch-2018-05-10/StopSearchJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backupsearch-2018-05-10/StopSearchJob.md "../../../goto/SdkForKotlin/backupsearch-2018-05-10/StopSearchJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backupsearch-2018-05-10/StopSearchJob.md "../../../goto/SdkForPHPV3/backupsearch-2018-05-10/StopSearchJob.md")
- [AWS SDK for Python](../../../goto/boto3/backupsearch-2018-05-10/StopSearchJob.md "../../../goto/boto3/backupsearch-2018-05-10/StopSearchJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backupsearch-2018-05-10/StopSearchJob.md "../../../goto/SdkForRubyV3/backupsearch-2018-05-10/StopSearchJob.md")
