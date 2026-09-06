

# Example: Browser-Based Upload using HTTP POST (Using AWS Signature Version 4)
<a name="sigv4-post-example"></a>

This section shows an example of using an HTTP POST request to upload content directly to Amazon S3.

For more information on Signature Version 4, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html).

## Uploading a File to Amazon S3 Using HTTP POST
<a name="sigv4-post-example-file-upload"></a>

This example provides a sample POST policy and a form that you can use to upload a file. The topic uses the example policy and fictitious credentials to show you the workflow and resulting signature and policy hash. You can use this data as test suite to verify your signature calculation code.

The example uses the following example credentials the signature calculations. You can use these credentials to verify your signature calculation code. However, you must then replace these with your own credentials when sending requests to AWS.


| Parameter | Value | 
| --- | --- | 
| AWSAccessKeyId | AKIAIOSFODNN7EXAMPLE | 
| AWSSecretAccessKey | wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY | 

### Sample Policy and Form
<a name="sigv4-post-example-file-upload-policy"></a>

The following POST policy supports uploads to Amazon S3 with specific conditions.

```
 1. { "expiration": "2015-12-30T12:00:00.000Z",
 2.   "conditions": [
 3.     {"bucket": "sigv4examplebucket"},
 4.     ["starts-with", "$key", "user/user1/"],
 5.     {"acl": "public-read"},
 6.     {"success_action_redirect": "http://sigv4examplebucket.s3.amazonaws.com/successful_upload.html"},
 7.     ["starts-with", "$Content-Type", "image/"],
 8.     {"x-amz-meta-uuid": "14365123651274"},
 9.     {"x-amz-server-side-encryption": "AES256"},
10.     ["starts-with", "$x-amz-meta-tag", ""],
11. 
12.     {"x-amz-credential": "AKIAIOSFODNN7EXAMPLE/20151229/us-east-1/s3/aws4_request"},
13.     {"x-amz-algorithm": "AWS4-HMAC-SHA256"},
14.     {"x-amz-date": "20151229T000000Z" }
15.   ]
16. }
```

This POST policy sets the following conditions on the request:
+ The upload must occur before noon UTC on December 30, 2015.
+ The content can be uploaded only to the `sigv4examplebucket`. The bucket must be in the region that you specified in the credential scope (`x-amz-credential` form parameter), because the signature you provided is valid only within this scope.
+ You can provide any key name that starts with `user/user1`. For example, `user/user1/MyPhoto.jpg`.
+ The ACL must be set to `public-read`.
+ If the upload succeeds, the user's browser is redirected to `http://sigv4examplebucket.s3.amazonaws.com/successful_upload.html`.
+ The object must be an image file.
+ The `x-amz-meta-uuid` tag must be set to `14365123651274`. 
+ The `x-amz-meta-tag` can contain any value.

The following is a Base64-encoded version of this POST policy. You use this value as your StringToSign in signature calculation.

```
1. eyAiZXhwaXJhdGlvbiI6ICIyMDE1LTEyLTMwVDEyOjAwOjAwLjAwMFoiLA0KICAiY29uZGl0aW9ucyI6IFsNCiAgICB7ImJ1Y2tldCI6ICJzaWd2NGV4YW1wbGVidWNrZXQifSwNCiAgICBbInN0YXJ0cy13aXRoIiwgIiRrZXkiLCAidXNlci91c2VyMS8iXSwNCiAgICB7ImFjbCI6ICJwdWJsaWMtcmVhZCJ9LA0KICAgIHsic3VjY2Vzc19hY3Rpb25fcmVkaXJlY3QiOiAiaHR0cDovL3NpZ3Y0ZXhhbXBsZWJ1Y2tldC5zMy5hbWF6b25hd3MuY29tL3N1Y2Nlc3NmdWxfdXBsb2FkLmh0bWwifSwNCiAgICBbInN0YXJ0cy13aXRoIiwgIiRDb250ZW50LVR5cGUiLCAiaW1hZ2UvIl0sDQogICAgeyJ4LWFtei1tZXRhLXV1aWQiOiAiMTQzNjUxMjM2NTEyNzQifSwNCiAgICB7IngtYW16LXNlcnZlci1zaWRlLWVuY3J5cHRpb24iOiAiQUVTMjU2In0sDQogICAgWyJzdGFydHMtd2l0aCIsICIkeC1hbXotbWV0YS10YWciLCAiIl0sDQoNCiAgICB7IngtYW16LWNyZWRlbnRpYWwiOiAiQUtJQUlPU0ZPRE5ON0VYQU1QTEUvMjAxNTEyMjkvdXMtZWFzdC0xL3MzL2F3czRfcmVxdWVzdCJ9LA0KICAgIHsieC1hbXotYWxnb3JpdGhtIjogIkFXUzQtSE1BQy1TSEEyNTYifSwNCiAgICB7IngtYW16LWRhdGUiOiAiMjAxNTEyMjlUMDAwMDAwWiIgfQ0KICBdDQp9
```

When you copy/paste the preceding policy, it should have carriage returns and new lines for your computed hash to match this value (ie. ASCII text, with CRLF line terminators).

Using example credentials to create a signature, the signature value is as follows (in signature calculation, the date is same as the `x-amz-date` in the policy (20151229):

```
8afdbf4008c03f22c2cd3cdb72e4afbb1f6a588f3255ac628749a66d7f09699e
```

The following example form specifies the preceding POST policy and supports a POST request to the `sigv4examplebucket`. Copy/paste the content in a text editor and save it as exampleform.html. You can then upload image files to the specific bucket using the exampleform.html. Your request will succeed if the signature you provide matches the signature Amazon S3 calculates.

**Note**  
You must update the bucket name, dates, credential, policy, and signature with valid values for this to successfully upload to S3. 

```
 1. <html>
 2.   <head>
 3.     
 4.     <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
 5.     
 6.   </head>
 7.   <body>
 8. 
 9.   <form action="http://sigv4examplebucket.s3.amazonaws.com/" method="post" enctype="multipart/form-data">
10.     Key to upload: 
11.     <input type="input"  name="key" value="user/user1/${filename}" /><br />
12.     <input type="hidden" name="acl" value="public-read" />
13.     <input type="hidden" name="success_action_redirect" value="http://sigv4examplebucket.s3.amazonaws.com/successful_upload.html" />
14.     Content-Type: 
15.     <input type="input"  name="Content-Type" value="image/jpeg" /><br />
16.     <input type="hidden" name="x-amz-meta-uuid" value="14365123651274" /> 
17.     <input type="hidden" name="x-amz-server-side-encryption" value="AES256" /> 
18.     <input type="text"   name="X-Amz-Credential" value="AKIAIOSFODNN7EXAMPLE/20151229/us-east-1/s3/aws4_request" />
19.     <input type="text"   name="X-Amz-Algorithm" value="AWS4-HMAC-SHA256" />
20.     <input type="text"   name="X-Amz-Date" value="20151229T000000Z" />
21. 
22.     Tags for File: 
23.     <input type="input"  name="x-amz-meta-tag" value="" /><br />
24.     <input type="hidden" name="Policy" value='{{<Base64-encoded policy string>}}' />
25.     <input type="hidden" name="X-Amz-Signature" value="{{<signature-value>}}" />
26.     File: 
27.     <input type="file"   name="file" /> <br />
28.     <!-- The elements after this will be ignored -->
29.     <input type="submit" name="submit" value="Upload to Amazon S3" />
30.   </form>
31.   
32. </html>
```

The post parameters are case insensitive. For example, you can specify `x-amz-signature` or `X-Amz-Signature`.