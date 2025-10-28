# ListHypervisors

Lists your hypervisors.

## Request Syntax

```
{
   "MaxResults": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[MaxResults](#API_BGW_ListHypervisors_RequestSyntax "#API_BGW_ListHypervisors_RequestSyntax")**

The maximum number of hypervisors to list.

Type: Integer

Valid Range: Minimum value of 1.

Required: No

**[NextToken](#API_BGW_ListHypervisors_RequestSyntax "#API_BGW_ListHypervisors_RequestSyntax")**

The next item following a partial list of returned resources. For example, if a request is
made to return `maxResults` number of resources, `NextToken` allows you
to return more items in your list starting at the location pointed to by the next
token.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1000.

Pattern: `.+`

Required: No

## Response Syntax

```
{
   "Hypervisors": [
      {
         "Host": "***string***",
         "HypervisorArn": "***string***",
         "KmsKeyArn": "***string***",
         "Name": "***string***",
         "State": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Hypervisors](#API_BGW_ListHypervisors_ResponseSyntax "#API_BGW_ListHypervisors_ResponseSyntax")**

A list of your `Hypervisor` objects, ordered by their Amazon Resource Names
(ARNs).

Type: Array of [Hypervisor](API_BGW_Hypervisor.md "API_BGW_Hypervisor.md") objects

**[NextToken](#API_BGW_ListHypervisors_ResponseSyntax "#API_BGW_ListHypervisors_ResponseSyntax")**

The next item following a partial list of returned resources. For example, if a request is
made to return `maxResults` number of resources, `NextToken` allows you
to return more items in your list starting at the location pointed to by the next
token.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1000.

Pattern: `.+`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InternalServerException**

The operation did not succeed because an internal error occurred. Try again later.

**ErrorCode**

A description of which internal error occured.

HTTP Status Code: 500

**ThrottlingException**

TPS has been limited to protect against intentional or unintentional
high request volumes.

**ErrorCode**

Error: TPS has been limited to protect against intentional or unintentional
high request volumes.

HTTP Status Code: 400

**ValidationException**

The operation did not succeed because a validation error occurred.

**ErrorCode**

A description of what caused the validation error.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backup-gateway-2021-01-01/ListHypervisors.md "../../../goto/cli2/backup-gateway-2021-01-01/ListHypervisors.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-gateway-2021-01-01/ListHypervisors.md "../../../goto/DotNetSDKV3/backup-gateway-2021-01-01/ListHypervisors.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-gateway-2021-01-01/ListHypervisors.md "../../../goto/SdkForCpp/backup-gateway-2021-01-01/ListHypervisors.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-gateway-2021-01-01/ListHypervisors.md "../../../goto/SdkForGoV2/backup-gateway-2021-01-01/ListHypervisors.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/ListHypervisors.md "../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/ListHypervisors.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/ListHypervisors.md "../../../goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/ListHypervisors.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-gateway-2021-01-01/ListHypervisors.md "../../../goto/SdkForKotlin/backup-gateway-2021-01-01/ListHypervisors.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-gateway-2021-01-01/ListHypervisors.md "../../../goto/SdkForPHPV3/backup-gateway-2021-01-01/ListHypervisors.md")
- [AWS SDK for Python](../../../goto/boto3/backup-gateway-2021-01-01/ListHypervisors.md "../../../goto/boto3/backup-gateway-2021-01-01/ListHypervisors.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/ListHypervisors.md "../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/ListHypervisors.md")
