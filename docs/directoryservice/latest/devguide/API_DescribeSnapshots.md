

# DescribeSnapshots
<a name="API_DescribeSnapshots"></a>

Obtains information about the directory snapshots that belong to this account.

This operation supports pagination with the use of the *NextToken* request and response parameters. If more results are available, the *DescribeSnapshots.NextToken* member contains a token that you pass in the next call to [DescribeSnapshots](#API_DescribeSnapshots) to retrieve the next set of items.

You can also specify a maximum number of return results with the *Limit* parameter.

## Request Syntax
<a name="API_DescribeSnapshots_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "SnapshotIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeSnapshots_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_DescribeSnapshots_RequestSyntax) **   <a name="DirectoryService-DescribeSnapshots-request-DirectoryId"></a>
The identifier of the directory for which to retrieve snapshot information.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: No

 ** [Limit](#API_DescribeSnapshots_RequestSyntax) **   <a name="DirectoryService-DescribeSnapshots-request-Limit"></a>
The maximum number of objects to return.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** [NextToken](#API_DescribeSnapshots_RequestSyntax) **   <a name="DirectoryService-DescribeSnapshots-request-NextToken"></a>
The *DescribeSnapshotsResult.NextToken* value from a previous call to [DescribeSnapshots](#API_DescribeSnapshots). Pass null if this is the first call.  
Type: String  
Required: No

 ** [SnapshotIds](#API_DescribeSnapshots_RequestSyntax) **   <a name="DirectoryService-DescribeSnapshots-request-SnapshotIds"></a>
A list of identifiers of the snapshots to obtain the information for. If this member is null or empty, all snapshots are returned using the *Limit* and *NextToken* members.  
Type: Array of strings  
Pattern: `^s-[0-9a-f]{10}$`   
Required: No

## Response Syntax
<a name="API_DescribeSnapshots_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Snapshots": [ 
      { 
         "DirectoryId": "string",
         "Name": "string",
         "SnapshotId": "string",
         "StartTime": number,
         "Status": "string",
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSnapshots_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeSnapshots_ResponseSyntax) **   <a name="DirectoryService-DescribeSnapshots-response-NextToken"></a>
If not null, more results are available. Pass this value in the *NextToken* member of a subsequent call to [DescribeSnapshots](#API_DescribeSnapshots).  
Type: String

 ** [Snapshots](#API_DescribeSnapshots_ResponseSyntax) **   <a name="DirectoryService-DescribeSnapshots-response-Snapshots"></a>
The list of [Snapshot](API_Snapshot.md) objects that were retrieved.  
It is possible that this list contains less than the number of items specified in the *Limit* member of the request. This occurs if there are less than the requested number of items left to retrieve, or if the limitations of the operation have been exceeded.  
Type: Array of [Snapshot](API_Snapshot.md) objects

## Errors
<a name="API_DescribeSnapshots_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClientException **   
A client exception has occurred.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** EntityDoesNotExistException **   
The specified entity could not be found.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** InvalidNextTokenException **   
The `NextToken` value is not valid.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** InvalidParameterException **   
One or more parameters are not valid.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** ServiceException **   
An exception has occurred in AWS Directory Service.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 500

## Examples
<a name="API_DescribeSnapshots_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_DescribeSnapshots_Example_1"></a>

This example illustrates one usage of DescribeSnapshots.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 76
X-Amz-Target: DirectoryService_20150416.DescribeSnapshots
X-Amz-Date: 20161214T164618Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request, 
 SignedHeaders=content-type;host;x-amz-date;x-amz-target, 
 Signature=602552c456c471537cbafaec3b7712674bdc20574c076dace469f3848fa8ab7a

 {
   "DirectoryId": "d-926example", 
   "Limit": 0, 
   "SnapshotIds": ["s-9267f6da4e"]
 }
```

### Example Response
<a name="API_DescribeSnapshots_Example_2"></a>

This example illustrates one usage of DescribeSnapshots.

```
HTTP/1.1 200 OK
x-amzn-RequestId: d7b33e7e-c21c-11e6-91f4-6dbff6648f8a
Content-Type: application/x-amz-json-1.1
Content-Length: 138
Date: Wed, 14 Dec 2016 16:46:21 GMT

{
   "Snapshots":[
      {
         "DirectoryId":"d-926example",
         "SnapshotId":"s-9267f6da4e",
         "StartTime":1.481289211615E9,
         "Status":"Completed",
         "Type":"Auto"
      }
   ]
}
```

## See Also
<a name="API_DescribeSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/DescribeSnapshots) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/DescribeSnapshots) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DescribeSnapshots) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/DescribeSnapshots) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DescribeSnapshots) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeSnapshots) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/DescribeSnapshots) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/DescribeSnapshots) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/DescribeSnapshots) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DescribeSnapshots) 