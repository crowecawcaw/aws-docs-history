# ListFragments

Returns a list of [Fragment](API_reader_Fragment.md "API_reader_Fragment.md") objects from the specified stream and
timestamp range within the archived data.

Listing fragments is eventually consistent. This means that even if the producer
receives an acknowledgment that a fragment is persisted, the result might not be
returned immediately from a request to `ListFragments`. However, results are
typically available in less than one second.

###### Note

You must first call the `GetDataEndpoint` API to get an endpoint.
Then send the `ListFragments` requests to this endpoint using the [--endpoint-url
parameter](../../../cli/latest/reference.md "../../../cli/latest/reference.md").

###### Important

If an error is thrown after invoking a Kinesis Video Streams archived media API,
in addition to the HTTP status code and the response body, it includes the following
pieces of information:

- `x-amz-ErrorType` HTTP header – contains a more specific error
  type in addition to what the HTTP status code provides.
- `x-amz-RequestId` HTTP header – if you want to report an issue to
  AWS, the support team can better diagnose the problem if given the Request
  Id.
  Both the HTTP status code and the ErrorType header can be utilized to make
  programmatic decisions about whether errors are retry-able and under what
  conditions, as well as provide information on what actions the client programmer
  might need to take in order to successfully try again.

For more information, see the **Errors** section at
the bottom of this topic, as well as [Common Errors](CommonErrors.md "CommonErrors.md").

## Request Syntax

```
POST /listFragments HTTP/1.1
Content-type: application/json

{
   "FragmentSelector": {
      "FragmentSelectorType": "`string`",
      "TimestampRange": {
         "EndTimestamp": `number`,
         "StartTimestamp": `number`
      }
   },
   "MaxResults": `number`,
   "NextToken": "`string`",
   "StreamARN": "`string`",
   "StreamName": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[FragmentSelector](#API_reader_ListFragments_RequestSyntax "#API_reader_ListFragments_RequestSyntax")**

Describes the timestamp range and timestamp origin for the range of fragments to
return.

###### Note

This is only required when the `NextToken` isn't passed in the API.

Type: [FragmentSelector](API_reader_FragmentSelector.md "API_reader_FragmentSelector.md") object

Required: No

**[MaxResults](#API_reader_ListFragments_RequestSyntax "#API_reader_ListFragments_RequestSyntax")**

The total number of fragments to return. If the total number of fragments available is
more than the value specified in `max-results`, then a [ListFragments:NextToken](#KinesisVideo-reader_ListFragments-response-NextToken "#KinesisVideo-reader_ListFragments-response-NextToken") is provided in the output that you can use
to resume pagination.

The default value is 100.

Type: Long

Valid Range: Minimum value of 1. Maximum value of 1000.

Required: No

**[NextToken](#API_reader_ListFragments_RequestSyntax "#API_reader_ListFragments_RequestSyntax")**

A token to specify where to start paginating. This is the [ListFragments:NextToken](#KinesisVideo-reader_ListFragments-response-NextToken "#KinesisVideo-reader_ListFragments-response-NextToken") from a previously truncated
response.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 4096.

Pattern: `[a-zA-Z0-9+/]+={0,2}`

Required: No

**[StreamARN](#API_reader_ListFragments_RequestSyntax "#API_reader_ListFragments_RequestSyntax")**

The Amazon Resource Name (ARN) of the stream from which to retrieve a fragment list. Specify either this parameter or the `StreamName` parameter.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: No

**[StreamName](#API_reader_ListFragments_RequestSyntax "#API_reader_ListFragments_RequestSyntax")**

The name of the stream from which to retrieve a fragment list. Specify either this parameter or the `StreamARN` parameter.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Fragments": [
      {
         "FragmentLengthInMilliseconds": ***number***,
         "FragmentNumber": "***string***",
         "FragmentSizeInBytes": ***number***,
         "ProducerTimestamp": ***number***,
         "ServerTimestamp": ***number***
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Fragments](#API_reader_ListFragments_ResponseSyntax "#API_reader_ListFragments_ResponseSyntax")**

A list of archived [Fragment](API_reader_Fragment.md "API_reader_Fragment.md") objects from the stream that meet the
selector criteria. Results are in no specific order, even across pages.

If there are no fragments in the stream that meet the selector criteria, an empty list
is returned.

Type: Array of [Fragment](API_reader_Fragment.md "API_reader_Fragment.md") objects

**[NextToken](#API_reader_ListFragments_ResponseSyntax "#API_reader_ListFragments_ResponseSyntax")**

If the returned list is truncated, the operation returns this token to use to retrieve
the next page of results. This value is `null` when there are no more results
to return.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 4096.

Pattern: `[a-zA-Z0-9+/]+={0,2}`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientLimitExceededException**

Kinesis Video Streams has throttled the request because you have exceeded a limit. Try making the call later. For information about limits, see [Kinesis Video Streams quotas](limits.md "limits.md").

HTTP Status Code: 400

**InvalidArgumentException**

A specified parameter exceeds its restrictions, is not supported, or can't be
used.

HTTP Status Code: 400

**NotAuthorizedException**

Status Code: 403, The caller is not authorized to perform an operation on the given
stream, or the token has expired.

HTTP Status Code: 401

**ResourceNotFoundException**

`GetImages` will throw this error when Kinesis Video Streams can't find the stream
that you specified.

`GetHLSStreamingSessionURL` and `GetDASHStreamingSessionURL` throw
this error if a session with a `PlaybackMode` of `ON_DEMAND` or
`LIVE_REPLAY` is requested for a stream that has no fragments within the
requested time range, or if a session with a `PlaybackMode` of
`LIVE` is requested for a stream that has no fragments within the last 30
seconds.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesis-video-reader-data-2017-09-30/ListFragments.md "../../../goto/cli2/kinesis-video-reader-data-2017-09-30/ListFragments.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kinesis-video-reader-data-2017-09-30/ListFragments.md "../../../goto/DotNetSDKV4/kinesis-video-reader-data-2017-09-30/ListFragments.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesis-video-reader-data-2017-09-30/ListFragments.md "../../../goto/SdkForCpp/kinesis-video-reader-data-2017-09-30/ListFragments.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesis-video-reader-data-2017-09-30/ListFragments.md "../../../goto/SdkForGoV2/kinesis-video-reader-data-2017-09-30/ListFragments.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesis-video-reader-data-2017-09-30/ListFragments.md "../../../goto/SdkForJavaV2/kinesis-video-reader-data-2017-09-30/ListFragments.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesis-video-reader-data-2017-09-30/ListFragments.md "../../../goto/SdkForJavaScriptV3/kinesis-video-reader-data-2017-09-30/ListFragments.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesis-video-reader-data-2017-09-30/ListFragments.md "../../../goto/SdkForKotlin/kinesis-video-reader-data-2017-09-30/ListFragments.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesis-video-reader-data-2017-09-30/ListFragments.md "../../../goto/SdkForPHPV3/kinesis-video-reader-data-2017-09-30/ListFragments.md")
- [AWS SDK for Python](../../../goto/boto3/kinesis-video-reader-data-2017-09-30/ListFragments.md "../../../goto/boto3/kinesis-video-reader-data-2017-09-30/ListFragments.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesis-video-reader-data-2017-09-30/ListFragments.md "../../../goto/SdkForRubyV3/kinesis-video-reader-data-2017-09-30/ListFragments.md")
