# ListLocations

Returns a list of source and destination locations.

If you have more locations than are returned in a response (that is, the response
returns only a truncated list of your agents), the response contains a token that you can
specify in your next request to fetch the next page of locations.

## Request Syntax

```
{
   "Filters": [
      {
         "Name": "`string`",
         "Operator": "`string`",
         "Values": [ "`string`" ]
      }
   ],
   "MaxResults": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[Filters](#API_ListLocations_RequestSyntax "#API_ListLocations_RequestSyntax")**

You can use API filters to narrow down the list of resources returned by
`ListLocations`. For example, to retrieve all tasks on a specific source
location, you can use `ListLocations` with filter name `LocationType S3`
and `Operator Equals`.

Type: Array of [LocationFilter](API_LocationFilter.md "API_LocationFilter.md") objects

Required: No

**[MaxResults](#API_ListLocations_RequestSyntax "#API_ListLocations_RequestSyntax")**

The maximum number of locations to return.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 100.

Required: No

**[NextToken](#API_ListLocations_RequestSyntax "#API_ListLocations_RequestSyntax")**

An opaque string that indicates the position at which to begin the next list of
locations.

Type: String

Length Constraints: Maximum length of 65535.

Pattern: `[a-zA-Z0-9=_-]+`

Required: No

## Response Syntax

```
{
   "Locations": [
      {
         "LocationArn": "***string***",
         "LocationUri": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Locations](#API_ListLocations_ResponseSyntax "#API_ListLocations_ResponseSyntax")**

An array that contains a list of locations.

Type: Array of [LocationListEntry](API_LocationListEntry.md "API_LocationListEntry.md") objects

**[NextToken](#API_ListLocations_ResponseSyntax "#API_ListLocations_ResponseSyntax")**

An opaque string that indicates the position at which to begin returning the next list
of locations.

Type: String

Length Constraints: Maximum length of 65535.

Pattern: `[a-zA-Z0-9=_-]+`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InternalException**

This exception is thrown when an error occurs in the AWS DataSync
service.

HTTP Status Code: 500

**InvalidRequestException**

This exception is thrown when the client submits a malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/ListLocations.md "../../../goto/cli2/datasync-2018-11-09/ListLocations.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/ListLocations.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/ListLocations.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/ListLocations.md "../../../goto/SdkForCpp/datasync-2018-11-09/ListLocations.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/ListLocations.md "../../../goto/SdkForGoV2/datasync-2018-11-09/ListLocations.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/ListLocations.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/ListLocations.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/ListLocations.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/ListLocations.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/ListLocations.md "../../../goto/SdkForKotlin/datasync-2018-11-09/ListLocations.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/ListLocations.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/ListLocations.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/ListLocations.md "../../../goto/boto3/datasync-2018-11-09/ListLocations.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/ListLocations.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/ListLocations.md")
