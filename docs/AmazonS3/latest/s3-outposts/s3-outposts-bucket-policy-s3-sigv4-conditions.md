# AWS Signature Version 4

(SigV4) authentication-specific policy keys

The following table shows the condition keys related to AWS Signature Version 4 (SigV4)
authentication that you can use with Amazon S3 on Outposts. In a bucket policy, you can add these
conditions to enforce specific behavior when requests are authenticated by using Signature
Version 4. For example policies, see [Bucket policy
examples that use Signature Version 4-related condition keys](#s3-outposts-bucket-policy-sig-v4-condition-key-example "#s3-outposts-bucket-policy-sig-v4-condition-key-example"). For more
information about authenticating requests using Signature Version 4, see [Authenticating requests (AWS Signature Version 4)](../API/sig-v4-authenticating-requests.md "../API/sig-v4-authenticating-requests.md") in the
_Amazon Simple Storage Service API Reference_

| Applicable keys                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `s3-outposts:authType`             | S3 on Outposts supports various methods of authentication. To restrict<br>incoming requests to use a specific authentication method, you can use<br>this optional condition key. For example, you can use this condition key<br>to allow only the HTTP `Authorization` header to be used in<br>request authentication.<br>Valid values:<br>`REST-HEADER`<br>`REST-QUERY-STRING`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `s3-outposts:signatureAge`         | The length of time, in milliseconds, that a signature is valid in an<br>authenticated request.<br>This condition works only for presigned URLs.<br>In Signature Version 4, the signing key is valid for up to seven days.<br>Therefore, the signatures are also valid for up to seven days. For more<br>information, see [Introduction to signing requests](../API/sig-v4-authenticating-requests.md#signing-request-intro "../API/sig-v4-authenticating-requests.md#signing-request-intro") in the<br>_Amazon Simple Storage Service API Reference_. You can use this condition to<br>further limit the signature age.<br>Example value: `600000`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `s3-outposts:x-amz-content-sha256` | You can use this condition key to disallow unsigned content in your<br>bucket.<br>When you use Signature Version 4, for requests that use the<br>`Authorization` header, you add the<br>`x-amz-content-sha256` header in the signature<br>calculation and then set its value to the hash payload.<br>You can use this condition key in your bucket policy to deny any<br>uploads where the payloads are not signed. For example:<br>• Deny uploads that use the `Authorization` header to<br>authenticate requests but don't sign the payload. For more<br>information, see [Transferring payload in a single chunk](../API/sig-v4-header-based-auth.md "../API/sig-v4-header-based-auth.md") in the<br>_Amazon Simple Storage Service API Reference_.<br>• Deny uploads that use presigned URLs. Presigned URLs always<br>have an `UNSIGNED_PAYLOAD`. For more information, see<br>[Authenticating requests](../API/sigv4-query-string-auth.md#query-string-auth-v4-signing "../API/sigv4-query-string-auth.md#query-string-auth-v4-signing") and [Authentication methods](../API/sig-v4-authenticating-requests.md "../API/sig-v4-authenticating-requests.md") in the<br>_Amazon Simple Storage Service API Reference_.<br>Valid value: `UNSIGNED-PAYLOAD` |

## Bucket policy

examples that use Signature Version 4-related condition keys

To use the following examples, replace the `user input
 placeholders` with your own information.

###### Example : `s3-outposts:signatureAge`

The following bucket policy denies any S3 on Outposts presigned URL request on objects
in `example-outpost-bucket` if the signature is more than 10 minutes old.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Deny a presigned URL request if the signature is more than 10 minutes old",
 "Effect": "Deny",
 "Principal": {"AWS":"`444455556666`"},
 "Action": "s3-outposts:*",
 "Resource": "arn:aws:s3-outposts:`us-east-1`:`111122223333`:outpost/`op-01ac5d28a6a232904`/bucket/`example-outpost-bucket`/object/*",
 "Condition": {
 "NumericGreaterThan": {"s3-outposts:signatureAge": 600000},
 "StringEquals": {"s3-outposts:authType": "REST-QUERY-STRING"}
 }
 }
 ]
}`

```

###### Example : `s3-outposts:authType`

The following bucket policy allows only requests that use the
`Authorization` header for request authentication. Any presigned URL
requests will be denied since presigned URLs use query parameters to provide request
and authentication information. For more information, see [Authentication
methods](../API/sig-v4-authenticating-requests.md "../API/sig-v4-authenticating-requests.md") in the _Amazon Simple Storage Service API Reference_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow only requests that use the Authorization header for request authentication. Deny presigned URL requests.",
 "Effect": "Deny",
 "Principal": {"AWS":"`111122223333`"},
 "Action": "s3-outposts:*",
 "Resource": "arn:aws:s3-outposts:`us-east-1`:`111122223333`:outpost/`op-01ac5d28a6a232904`/bucket/`example-outpost-bucket`/object/*",
 "Condition": {
 "StringNotEquals": {
 "s3-outposts:authType": "REST-HEADER"
 }
 }
 }
 ]
}`

```

###### Example : `s3-outposts:x-amz-content-sha256`

The following bucket policy denies any uploads with unsigned payloads, such as uploads
that are using presigned URLs. For more information, see [Authenticating requests](../API/sigv4-query-string-auth.md#query-string-auth-v4-signing "../API/sigv4-query-string-auth.md#query-string-auth-v4-signing") and [Authentication
methods](../API/sig-v4-authenticating-requests.md "../API/sig-v4-authenticating-requests.md") in the _Amazon Simple Storage Service API Reference_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Deny uploads with unsigned payloads.",
 "Effect": "Deny",
 "Principal": {"AWS":"`111122223333`"},
 "Action": "s3-outposts:*",
 "Resource": "arn:aws:s3-outposts:`us-east-1`:`111122223333`:outpost/`op-01ac5d28a6a232904`/bucket/`example-outpost-bucket`/object/*",
 "Condition": {
 "StringEquals": {
 "s3-outposts:x-amz-content-sha256": "UNSIGNED-PAYLOAD"
 }
 }
 }
 ]
}`

```
