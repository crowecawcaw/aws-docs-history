

# Authenticating Requests: Browser-Based Uploads Using POST (AWS Signature Version 4)
<a name="sigv4-authentication-HTTPPOST"></a>

Amazon S3 supports HTTP POST requests so that users can upload content directly to Amazon S3. Using HTTP POST to upload content simplifies uploads and reduces upload latency where users upload data to store in Amazon S3. This section describes how you authenticate HTTP POST requests. For more information about HTTP POST requests, how to create a form, create a POST policy, and an example, see [Browser-Based Uploads Using POST (AWS Signature Version 4)](sigv4-UsingHTTPPOST.md).

To authenticate an HTTP POST request you do the following:

 

1. The form must include the following fields to provide signature and relevant information that Amazon S3 can use to re-calculate the signature upon receiving the request:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonS3/latest/developerguide/sigv4-authentication-HTTPPOST.html)

1. The POST policy must include the following elements:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonS3/latest/developerguide/sigv4-authentication-HTTPPOST.html)

1. For signature calculation the POST policy is the string to sign.

## Calculating a Signature
<a name="sigv4-signature-calc-post"></a>

 The following diagram illustrates the signature calculation process. 

![AWS signature calculation process with StringToSign, SigningKey, and Signature steps.](http://docs.aws.amazon.com/AmazonS3/latest/developerguide/images/sigV4-post.png)






**To Calculate a signature**

1. Create a policy using UTF-8 encoding.

1. Convert the UTF-8-encoded policy to Base64. The result is the string to sign.

1. Create the signature as an HMAC-SHA256 hash of the string to sign. You will provide the signing key as key to the hash function.

1. Encode the signature by using hex encoding.

For more information about creating HTML forms, security policies, and an example, see the following subtopics:


+ [Creating an HTML Form (Using AWS Signature Version 4)](sigv4-HTTPPOSTForms.md)
+ [POST Policy](sigv4-HTTPPOSTConstructPolicy.md)
+ [Example: Browser-Based Upload using HTTP POST (Using AWS Signature Version 4)](sigv4-post-example.md)