# Browser-Based Uploads Using
 POST (AWS Signature Version 4)

This section discusses how to upload files directly to Amazon S3 through a browser using HTTP POST
 requests. It also contains information about how to use the AWS Amplify JavaScript library
 for browser-based file uploads to Amazon S3.

###### Topics

* [POST Object](RESTObjectPOST.md "RESTObjectPOST.md")
* [POST Object restore](RESTObjectPOSTrestore.md "RESTObjectPOSTrestore.md")
* [Browser-Based Uploads Using HTTP POST](#sigv4-UsingHTTPPOST-how-to "#sigv4-UsingHTTPPOST-how-to")
* [Calculating a Signature](#sigv4-post-signature-calc "#sigv4-post-signature-calc")
* [Creating an HTML Form (Using AWS Signature Version
 4)](sigv4-HTTPPOSTForms.md "sigv4-HTTPPOSTForms.md")
* [POST Policy](sigv4-HTTPPOSTConstructPolicy.md "sigv4-HTTPPOSTConstructPolicy.md")
* [Example: Browser-Based Upload using HTTP POST (Using AWS
 Signature Version 4)](sigv4-post-example.md "sigv4-post-example.md")
* [Browser-based uploads to Amazon S3 using
 the AWS Amplify library](browser-based-uploads-aws-amplify.md "browser-based-uploads-aws-amplify.md")

## Browser-Based Uploads Using HTTP POST


Amazon S3 supports HTTP POST requests so that users can upload content directly to Amazon S3. By
 using POST, end users can authenticate requests without having to pass data through a
 secure intermediary node that protects your credentials. Thus, HTTP POST has the
 potential to reduce latency.


The following figure shows an Amazon S3 upload using a POST request.



![Comparison of S3 PUT and POST methods for file transfer from customer to Amazon S3.](../../../images/AmazonS3/latest/API/images/s3_post.png)


1. The user accesses your page from a web browser.
2. Your webpage contains an
 HTML
 form that contains all the information necessary for the user to upload
 content to Amazon S3.
3. The user uploads content to Amazon S3 through the web browser.

The process for sending browser-based POST requests is as follows:


 



1. Create a security policy specifying conditions that restrict what you want to allow in the
 request, such as the bucket name where objects can be uploaded, and key name
 prefixes that you want to allow for the object that is being created.
2. Create a signature that is based on the policy. For authenticated requests, the form must
 include a valid signature and the policy.
3. Create an HTML form that your users can access in order to upload objects to
 your Amazon S3 bucket.

The following section describes how to create a signature to authenticate a request.
 For information about creating forms and security policies, see [Creating an HTML Form (Using AWS Signature Version
 4)](sigv4-HTTPPOSTForms.md "sigv4-HTTPPOSTForms.md").


## Calculating a Signature


For authenticated requests, the HTML form must include fields for a security policy
 and a signature. 


 



* A security policy (see [POST Policy](sigv4-HTTPPOSTConstructPolicy.md "sigv4-HTTPPOSTConstructPolicy.md")) controls what is allowed in
 the request.
* The security policy is the `StringToSign` (see [Introduction to Signing Requests](sig-v4-authenticating-requests.md#signing-request-intro "sig-v4-authenticating-requests.md#signing-request-intro")) in
 your signature calculation.

 



![StringToSign, Signing Key, and Signature](../../../images/AmazonS3/latest/API/images/sigV4-post.png)



###### To Calculate a signature

1. Create a policy using UTF-8 encoding.
2. Convert the UTF-8-encoded policy bytes to base64. The result is the
 `StringToSign`.
3. Create a signing key.
4. Use the signing key to sign the `StringToSign` using HMAC-SHA256 signing
 algorithm.

For more information about creating HTML forms, security policies, and an example, see
 the following:




* [Creating an HTML Form (Using AWS Signature Version
 4)](sigv4-HTTPPOSTForms.md "sigv4-HTTPPOSTForms.md")
* [POST Policy](sigv4-HTTPPOSTConstructPolicy.md "sigv4-HTTPPOSTConstructPolicy.md")
* [Example: Browser-Based Upload using HTTP POST (Using AWS
 Signature Version 4)](sigv4-post-example.md "sigv4-post-example.md")
