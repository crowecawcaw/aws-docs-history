

# Browser-Based Uploads Using POST (AWS Signature Version 4)
<a name="sigv4-UsingHTTPPOST"></a>

This section discusses how to upload files directly to Amazon S3 through a browser using HTTP POST requests. It also contains information about how to use the AWS Amplify JavaScript library for browser-based file uploads to Amazon S3.

**Topics**
+ [POST Object](RESTObjectPOST.md)
+ [POST Object restore](RESTObjectPOSTrestore.md)
+ [Browser-Based Uploads Using HTTP POST](#sigv4-UsingHTTPPOST-how-to)
+ [Calculating a Signature](#sigv4-post-signature-calc)
+ [Creating an HTML Form (Using AWS Signature Version 4)](sigv4-HTTPPOSTForms.md)
+ [POST Policy](sigv4-HTTPPOSTConstructPolicy.md)
+ [Example: Browser-Based Upload using HTTP POST (Using AWS Signature Version 4)](sigv4-post-example.md)
+ [Browser-based uploads to Amazon S3 using the AWS Amplify library](browser-based-uploads-aws-amplify.md)

## Browser-Based Uploads Using HTTP POST
<a name="sigv4-UsingHTTPPOST-how-to"></a>

Amazon S3 supports HTTP POST requests so that users can upload content directly to Amazon S3. By using POST, end users can authenticate requests without having to pass data through a secure intermediary node that protects your credentials. Thus, HTTP POST has the potential to reduce latency.

The following figure shows an Amazon S3 upload using a POST request.

![Comparison of S3 PUT workflow with customer to server to S3, versus POST workflow with direct customer to S3 transfer.](http://docs.aws.amazon.com/AmazonS3/latest/developerguide/images/s3_post.png)


1.  The user accesses your page from a web browser. 

1.  Your webpage contains an HTML form that contains all the information necessary for the user to upload content to Amazon S3. 

1.  The user uploads content to Amazon S3 through the web browser. 

The process for sending browser-based POST requests is as follows:

 

1. Create a security policy specifying conditions that restrict what you want to allow in the request, such as the bucket name where objects can be uploaded, and key name prefixes that you want to allow for the object that is being created.

1. Create a signature that is based on the policy. For authenticated requests, the form must include a valid signature and the policy.

1. Create an HTML form that your users can access in order to upload objects to your Amazon S3 bucket.

The following section describes how to create a signature to authenticate a request. For information about creating forms and security policies, see [Creating an HTML Form (Using AWS Signature Version 4)](sigv4-HTTPPOSTForms.md).

## Calculating a Signature
<a name="sigv4-post-signature-calc"></a>

For authenticated requests, the HTML form must include fields for a security policy and a signature. 

 
+ A security policy (see [POST Policy](sigv4-HTTPPOSTConstructPolicy.md)) controls what is allowed in the request.
+ The security policy is the `StringToSign` (see [Introduction to Signing Requests](sig-v4-authenticating-requests.md#signing-request-intro)) in your signature calculation.

 

![StringToSign, Signing Key, and Signature.](http://docs.aws.amazon.com/AmazonS3/latest/developerguide/images/sigV4-post.png)






**To Calculate a signature**

1. Create a policy using UTF-8 encoding.

1. Convert the UTF-8-encoded policy bytes to base64. The result is the `StringToSign`.

1. Create a signing key.

1. Use the signing key to sign the `StringToSign` using HMAC-SHA256 signing algorithm.

For more information about creating HTML forms, security policies, and an example, see the following:


+ [Creating an HTML Form (Using AWS Signature Version 4)](sigv4-HTTPPOSTForms.md)
+ [POST Policy](sigv4-HTTPPOSTConstructPolicy.md)
+ [Example: Browser-Based Upload using HTTP POST (Using AWS Signature Version 4)](sigv4-post-example.md)

