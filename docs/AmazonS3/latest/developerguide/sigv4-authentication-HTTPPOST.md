

# Authenticating Requests: Browser-Based Uploads Using POST (AWS Signature Version 4)
<a name="sigv4-authentication-HTTPPOST"></a>

Amazon S3 supports HTTP POST requests so that users can upload content directly to Amazon S3. Using HTTP POST to upload content simplifies uploads and reduces upload latency where users upload data to store in Amazon S3. This section describes how you authenticate HTTP POST requests. For more information about HTTP POST requests, how to create a form, create a POST policy, and an example, see [Browser-Based Uploads Using POST (AWS Signature Version 4)](sigv4-UsingHTTPPOST.md).

To authenticate an HTTP POST request you do the following:

 

1. The form must include the following fields to provide signature and relevant information that Amazon S3 can use to re-calculate the signature upon receiving the request:


<table>
<thead>
  <tr><th>Element Name</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><code>policy</code></td><td>The Base64-encoded security policy that describes what is permitted in the request. For signature calculation this policy is the string you sign. Amazon S3 must get this policy so it can re-calculate the signature.</td></tr>
  <tr><td><code>x-amz-algorithm</code></td><td>The signing algorithm used. For AWS Signature Version 4, the value is <code>AWS4-HMAC-SHA256</code>.</td></tr>
  <tr><td><code>x-amz-credential</code></td><td>In addition to your access key ID, this provides scope information you used in calculating the signing key for signature calculation. <br />It is a string of the following form:<br /><code>&lt;your-access-key-id&gt;/&lt;date&gt;/&lt;aws-region&gt;/&lt;aws-service&gt;/aws4_request </code><br />For example:<br /> <code> AKIAIOSFODNN7EXAMPLE/20130728/us-east-1/s3/aws4_request</code>. . <br />For Amazon S3, the <i>aws-service</i> string is <code>s3</code>. For a list of Amazon S3 <code>aws-region</code> strings, see <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region">Regions and Endpoints</a> in the <i>AWS General Reference</i>. </td></tr>
  <tr><td><code>x-amz-date</code></td><td>It is the date value in ISO8601 format. For example, <code>20130728T000000Z</code>. <br />It is the same date you used in creating the signing key. This must also be the same value you provide in the policy (<code>x-amz-date</code>) that you signed. </td></tr>
  <tr><td><code>x-amz-signature</code></td><td>(AWS Signature Version 4) The HMAC-SHA256 hash of the security policy. <br />For more information on options for the signature, see <a href="https://docs.aws.amazon.com/general/latest/gr/sigv4-add-signature-to-request.html">Add the signature to the HTTP request</a> in the <i>AWS General Reference</i>.</td></tr>
</tbody>
</table>


1. The POST policy must include the following elements:


<table>
<thead>
  <tr><th>Element Name</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><code>x-amz-algorithm</code></td><td> The signing algorithm that you used to calculation the signature. For AWS Signature Version 4, the value is <code>AWS4-HMAC-SHA256</code>. </td></tr>
  <tr><td><code>x-amz-credential</code></td><td>In addition to your access key ID, this provides scope information you used in calculating the signing key for signature calculation. <br />It is a string of the following form:<br /><code>&lt;your-access-key-id&gt;/&lt;date&gt;/&lt;aws-region&gt;/&lt;aws-service&gt;/aws4_request </code><br />For example, <br /> <code> AKIAIOSFODNN7EXAMPLE/20130728/us-east-1/s3/aws4_request</code>. . </td></tr>
  <tr><td><code>x-amz-date</code></td><td> The date value specified in the ISO8601 formatted string. For example, "20130728T000000Z". The date must be the same that you used in creating the signing key for signature calculation. </td></tr>
</tbody>
</table>


1. For signature calculation the POST policy is the string to sign.

## Calculating a Signature
<a name="sigv4-signature-calc-post"></a>

 The following diagram illustrates the signature calculation process. 

![AWS signature calculation process with StringToSign, SigningKey, and Signature steps.](https://docs.aws.amazon.com/AmazonS3/latest/developerguide/images/sigV4-post.png)






**To Calculate a signature**

1. Create a policy using UTF-8 encoding.

1. Convert the UTF-8-encoded policy to Base64. The result is the string to sign.

1. Create the signature as an HMAC-SHA256 hash of the string to sign. You will provide the signing key as key to the hash function.

1. Encode the signature by using hex encoding.

For more information about creating HTML forms, security policies, and an example, see the following subtopics:


+ [Creating an HTML Form (Using AWS Signature Version 4)](sigv4-HTTPPOSTForms.md)
+ [POST Policy](sigv4-HTTPPOSTConstructPolicy.md)
+ [Example: Browser-Based Upload using HTTP POST (Using AWS Signature Version 4)](sigv4-post-example.md)