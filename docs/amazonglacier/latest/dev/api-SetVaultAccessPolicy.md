

 **This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/).

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/).

# Set Vault Access Policy (PUT access-policy)
<a name="api-SetVaultAccessPolicy"></a>

## Description
<a name="api-SetVaultAccessPolicy-description"></a>

This operation configures an access policy for a vault and will overwrite an existing policy. To configure a vault access policy, send a `PUT` request to the `access-policy` subresource of the vault. You can set one access policy per vault and the policy can be up to 20 KB in size. For more information about vault access policies, see [Vault Access Policies](vault-access-policy.md). 

## Requests
<a name="api-SetVaultAccessPolicy-requests"></a>

### Syntax
<a name="api-SetVaultAccessPolicy-requests-syntax"></a>

To set a vault access policy, send an HTTP `PUT` request to the URI of the vault's `access-policy` subresource as shown in the following syntax example.

```
 1. PUT /{{AccountId}}/vaults/{{vaultName}}/access-policy HTTP/1.1
 2. Host: glacier.{{Region}}.amazonaws.com
 3. Date: {{Date}}
 4. Authorization: {{SignatureValue}}
 5. Content-Length: {{Length}}
 6. x-amz-glacier-version: 2012-06-01
 7. 			
 8. {
 9.   "Policy": "string"
10. }
```

 

**Note**  
The `AccountId` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '`-`' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

### Request Parameters
<a name="api-SetVaultAccessPolicy-requests-parameters"></a>

This operation does not use request parameters.

### Request Headers
<a name="api-SetVaultAccessPolicy-requests-headers"></a>

This operation uses only request headers that are common to all operations. For information about common request headers, see [Common Request Headers](api-common-request-headers.md).

### Request Body
<a name="api-SetVaultAccessPolicy-requests-elements"></a>

The request body contains the following JSON fields.

 **Policy**   
The vault access policy as a JSON string, which uses "\\" as an escape character.  
 Type: String   
 Required: Yes

## Responses
<a name="api-SetVaultAccessPolicy-responses"></a>

In response, Amazon Glacier returns `204 No Content` if the policy is accepted.

### Syntax
<a name="api-SetVaultAccessPolicy-response-syntax"></a>

```
HTTP/1.1 204 No Content
x-amzn-RequestId: x-amzn-RequestId
Date: Date
```

### Response Headers
<a name="api-SetVaultAccessPolicy-responses-headers"></a>

This operation uses only response headers that are common to most responses. For information about common response headers, see [Common Response Headers](api-common-response-headers.md).

### Response Body
<a name="api-SetVaultAccessPolicy-responses-elements"></a>

This operation does not return a response body.

### Errors
<a name="api-SetVaultAccessPolicy-responses-errors"></a>

For information about Amazon Glacier exceptions and error messages, see [Error Responses](api-error-responses.md).

## Examples
<a name="api-SetVaultAccessPolicy-examples"></a>

### Example Request
<a name="api-SetVaultAccessPolicy-example-request"></a>

The following example sends an HTTP `PUT` request to the URI of the vault's `access-policy` subresource. The `Policy` JSON string uses "\\" as an escape character.

```
1. PUT /-/vaults/examplevault/access-policy HTTP/1.1
2. Host: glacier.us-west-2.amazonaws.com
3. x-amz-Date: 20170210T120000Z
4. Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20141123/us-west-2/glacier/aws4_request,SignedHeaders=host;x-amz-date;x-amz-glacier-version,Signature=9257c16da6b25a715ce900a5b45b03da0447acf430195dcb540091b12966f2a2
5. Content-Length: length
6. x-amz-glacier-version: 2012-06-01
7. 
8. {"Policy":"{\"Version\":\"2012-10-17\",		 	 	 \"Statement\":[{\"Sid\":\"Define-owner-access-rights\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::999999999999:root\"},\"Action\":\"glacier:DeleteArchive\",\"Resource\":\"arn:aws:glacier:us-west-2:999999999999:vaults/examplevault\"}]}"}
```

### Example Response
<a name="api-SetVaultAccessPolicy-example-response"></a>

If the request was successful, Amazon Glacier (Amazon Glacier) returns a `HTTP 204 No Content` as shown in the following example.

```
1. HTTP/1.1 204 No Content
2. x-amzn-RequestId: AAABZpJrTyioDC_HsOmHae8EZp_uBSJr6cnGOLKp_XJCl-Q
3. Date: Wed, 10 Feb 2017 12:02:00 GMT
```

## Related Sections
<a name="related-sections-SetVaultAccessPolicy"></a>

 
+ [Delete Vault Access Policy (DELETE access-policy)](api-DeleteVaultAccessPolicy.md)

 
+ [Get Vault Access Policy (GET access-policy)](api-GetVaultAccessPolicy.md)

## See Also
<a name="api-SetVaultAccessPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific Amazon SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/reference/glacier/set-vault-access-policy.html) 