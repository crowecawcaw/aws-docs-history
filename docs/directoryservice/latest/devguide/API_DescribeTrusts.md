

# DescribeTrusts
<a name="API_DescribeTrusts"></a>

Obtains information about the trust relationships for this account.

If no input parameters are provided, such as DirectoryId or TrustIds, this request describes all the trust relationships belonging to the account.

## Request Syntax
<a name="API_DescribeTrusts_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "TrustIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeTrusts_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_DescribeTrusts_RequestSyntax) **   <a name="DirectoryService-DescribeTrusts-request-DirectoryId"></a>
The Directory ID of the AWS directory that is a part of the requested trust relationship.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: No

 ** [Limit](#API_DescribeTrusts_RequestSyntax) **   <a name="DirectoryService-DescribeTrusts-request-Limit"></a>
The maximum number of objects to return.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** [NextToken](#API_DescribeTrusts_RequestSyntax) **   <a name="DirectoryService-DescribeTrusts-request-NextToken"></a>
The *DescribeTrustsResult.NextToken* value from a previous call to [DescribeTrusts](#API_DescribeTrusts). Pass null if this is the first call.  
Type: String  
Required: No

 ** [TrustIds](#API_DescribeTrusts_RequestSyntax) **   <a name="DirectoryService-DescribeTrusts-request-TrustIds"></a>
A list of identifiers of the trust relationships for which to obtain the information. If this member is null, all trust relationships that belong to the current account are returned.  
An empty list results in an `InvalidParameterException` being thrown.  
Type: Array of strings  
Pattern: `^t-[0-9a-f]{10}$`   
Required: No

## Response Syntax
<a name="API_DescribeTrusts_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Trusts": [ 
      { 
         "CreatedDateTime": number,
         "DirectoryId": "string",
         "LastUpdatedDateTime": number,
         "RemoteDomainName": "string",
         "SelectiveAuth": "string",
         "StateLastUpdatedDateTime": number,
         "TrustDirection": "string",
         "TrustId": "string",
         "TrustState": "string",
         "TrustStateReason": "string",
         "TrustType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeTrusts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeTrusts_ResponseSyntax) **   <a name="DirectoryService-DescribeTrusts-response-NextToken"></a>
If not null, more results are available. Pass this value for the *NextToken* parameter in a subsequent call to [DescribeTrusts](#API_DescribeTrusts) to retrieve the next set of items.  
Type: String

 ** [Trusts](#API_DescribeTrusts_ResponseSyntax) **   <a name="DirectoryService-DescribeTrusts-response-Trusts"></a>
The list of Trust objects that were retrieved.  
It is possible that this list contains less than the number of items specified in the *Limit* member of the request. This occurs if there are less than the requested number of items left to retrieve, or if the limitations of the operation have been exceeded.  
Type: Array of [Trust](API_Trust.md) objects

## Errors
<a name="API_DescribeTrusts_Errors"></a>

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

 ** UnsupportedOperationException **   
The operation is not supported.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

## Examples
<a name="API_DescribeTrusts_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_DescribeTrusts_Example_1"></a>

This example illustrates one usage of DescribeTrusts.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 61
X-Amz-Target: DirectoryService_20150416.DescribeTrusts
X-Amz-Date: 20161214T210907Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=fc201f050b631958cf6c5e186c5c897e82a974dad41b0e3c141a811003fa3c9b

 {
   "DirectoryId":"d-926example",
   "TrustIds": ["t-9267353df0"]
 }
```

### Example Response
<a name="API_DescribeTrusts_Example_2"></a>

This example illustrates one usage of DescribeTrusts.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 8e6560bd-c241-11e6-a4dc-e5519684970a
Content-Type: application/x-amz-json-1.1
Content-Length: 406
Date: Wed, 14 Dec 2016 21:09:09 GMT

 {
   "Trusts": [
     {
       "CreatedDateTime": 1481749250.657,
       "DirectoryId": "d-926example",
       "LastUpdatedDateTime": 1481749260.156,
       "RemoteDomainName": "sales.example.com",
       "StateLastUpdatedDateTime": 1481749260.156,
       "TrustDirection": "One-Way: Outgoing",
       "TrustId": "t-9267353df0",
       "TrustState": "Failed",
       "TrustStateReason": "The specified domain either does not exist or could not be contacted. Name: sales.example.com",
       "TrustType": "Forest"
     }
   ]
 }
```

## See Also
<a name="API_DescribeTrusts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/DescribeTrusts) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/DescribeTrusts) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DescribeTrusts) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/DescribeTrusts) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DescribeTrusts) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeTrusts) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/DescribeTrusts) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/DescribeTrusts) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/DescribeTrusts) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DescribeTrusts) 