

 **This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/).

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/).

# Get Vault Access Policy (GET access-policy)
<a name="api-GetVaultAccessPolicy"></a>

## Description
<a name="api-GetVaultAccessPolicy-description"></a>

This operation retrieves the `access-policy` subresource set on the vault—for more information on setting this subresource, see [Set Vault Access Policy (PUT access-policy)](api-SetVaultAccessPolicy.md). If there is no access policy set on the vault, the operation returns a `404 Not found` error. For more information about vault access policies, see [Vault Access Policies](vault-access-policy.md).

## Requests
<a name="api-GetVaultAccessPolicy-requests"></a>

To return the current vault access policy, send an HTTP `GET` request to the URI of the vault's `access-policy` subresource.

### Syntax
<a name="api-GetVaultAccessPolicy-requests-syntax"></a>

```
1. GET /{{AccountId}}/vaults/{{vaultName}}/access-policy HTTP/1.1
2. Host: glacier.{{Region}}.amazonaws.com
3. Date: {{Date}}
4. Authorization: {{SignatureValue}}
5. x-amz-glacier-version: 2012-06-01
```

 

**Note**  
The `AccountId` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

### Request Parameters
<a name="api-GetVaultAccessPolicy-requests-parameters"></a>

This operation does not use request parameters.

### Request Headers
<a name="api-GetVaultAccessPolicy-requests-headers"></a>

This operation uses only request headers that are common to all operations. For information about common request headers, see [Common Request Headers](api-common-request-headers.md).

### Request Body
<a name="api-GetVaultAccessPolicy-requests-elements"></a>

This operation does not have a request body.

## Responses
<a name="api-GetVaultAccessPolicy-responses"></a>

In response, Amazon Glacier (Amazon Glacier) returns the vault access policy in JSON format in the body of the response. 

### Syntax
<a name="api-GetVaultAccessPolicy-responses-syntax"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: x-amzn-RequestId
Date: Date
Content-Type: application/json
Content-Length: length
				
{
  "Policy": "string"
}
```

### Response Headers
<a name="api-GetVaultAccessPolicy-responses-headers"></a>

This operation uses only response headers that are common to most responses. For information about common response headers, see [Common Response Headers](api-common-response-headers.md).

### Response Body
<a name="api-GetVaultAccessPolicy-responses-elements"></a>

The response body contains the following JSON fields.

 **Policy**   
The vault access policy as a JSON string, which uses "\\" as an escape character.  
 Type: String

### Errors
<a name="api-GetVaultAccessPolicy-responses-errors"></a>

For information about Amazon Glacier exceptions and error messages, see [Error Responses](api-error-responses.md).

## Examples
<a name="api-GetVaultAccessPolicy-examples"></a>

The following example demonstrates how to get a vault access policy.

### Example Request
<a name="api-GetVaultAccessPolicy-example-request"></a>

In this example, a `GET` request is sent to the URI of a vault's `access-policy` subresource.

```
1. GET /-/vaults/examplevault/access-policy HTTP/1.1
2. Host: glacier.us-west-2.amazonaws.com
3. x-amz-Date: 20170210T120000Z
4. x-amz-glacier-version: 2012-06-01
5. Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
```

### Example Response
<a name="api-GetVaultAccessPolicy-example-response"></a>

If the request was successful, Amazon Glacier returns the vault access policy as a JSON string in the body of the response. The returned JSON string uses "\\" as an escape character, as shown in the [Set Vault Access Policy (PUT access-policy)](api-SetVaultAccessPolicy.md) examples. However, the following example shows the returned JSON string without escape characters for readability. 

```
 1. HTTP/1.1 200 OK
 2. x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
 3. Date: Wed, 10 Feb 2017 12:00:00 GMT
 4. Content-Type: application/json
 5. Content-Length: length
 6. 
 7. {
 8.   "Policy": "
 9.     {
10.       "Version": "2012-10-17",		 	 	 
11.       "Statement": [
12.         {
13.           "Sid": "allow-time-based-deletes",
14.           "Principal": {
15.             "AWS": "999999999999"
16.           },
17.           "Effect": "Allow",
18.           "Action": "glacier:Delete*",
19.           "Resource": [
20.             "arn:aws:glacier:us-west-2:999999999999:vaults/examplevault"
21.           ],
22.           "Condition": {
23.             "DateGreaterThan": {
24.               "aws:CurrentTime": "2018-12-31T00:00:00Z"
25.             }
26.           }
27.         }
28.       ]
29.     }        
30.   "
31. }
```

## Related Sections
<a name="related-sections-GetVaultAccessPolicy"></a>

 
+ [Delete Vault Access Policy (DELETE access-policy)](api-DeleteVaultAccessPolicy.md)

 
+ [Set Vault Access Policy (PUT access-policy)](api-SetVaultAccessPolicy.md)

## See Also
<a name="api-GetVaultAccessPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific Amazon SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/reference/glacier/get-vault-access-policy.html) 