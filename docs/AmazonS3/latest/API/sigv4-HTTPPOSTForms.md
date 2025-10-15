# Creating an HTML Form (Using AWS Signature Version
 4)

###### Topics

* [HTML Form Declaration](#HTTPPOSTFormDeclaration "#HTTPPOSTFormDeclaration")
* [HTML Form Fields](#sigv4-HTTPPOSTFormFields "#sigv4-HTTPPOSTFormFields")
To allow users to upload content to Amazon S3 by using their browsers (HTTP POST requests),
 you use HTML forms. HTML forms consist of a form declaration and form fields. The form
 declaration contains high-level information about the request. The form fields contain
 detailed request information.

This section describes how to create HTML forms. For a working example of
 browser-based upload using HTTP POST and related signature calculations for request
 authentication, see [Example: Browser-Based Upload using HTTP POST (Using AWS
 Signature Version 4)](sigv4-post-example.md "sigv4-post-example.md").

The form and policy must be UTF-8 encoded. You can apply UTF-8 encoding to the form by
 specifying `charset=UTF-8` in the `content` attribute. The
 following is an example of UTF-8 encoding in the HTML heading.


```
<html>
  <head>
    ...
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    ...
  </head>
  <body>
```
Following is an example of UTF-8 encoding in a request header.


```
Content-Type: text/html; charset=UTF-8
```
###### Note

The form data and boundaries (excluding the contents of the file) cannot exceed
 20KB.


## HTML Form Declaration


The HTML form declaration has the following three attributes:


 



* `action` – The URL that processes the request, which must
 be set to the URL of the bucket. For example, if the name of your bucket is
 `examplebucket`, the URL is
 `http://examplebucket.s3.amazonaws.com/`.


###### Note

The key name is specified in a form field.
* `method` – The method must be POST.
* `enctype` – The enclosure type (`enctype`) must
 be set to multipart/form-data for both file uploads and text area uploads.
 For more information about `enctype`, see [RFC 1867](http://www.ietf.org/rfc/rfc1867.txt "http://www.ietf.org/rfc/rfc1867.txt").

This is a form declaration for the bucket `examplebucket`.



```
<form action="http://examplebucket.s3.amazonaws.com/" method="post"

enctype="multipart/form-data">
```

## HTML Form Fields


The following table describes a list of fields that you can use within a form. Among other
 fields, there is a signature field that you can use to authenticate requests. There
 are fields for you to specify the signature calculation algorithm
 (`x-amz-algorithm`), the credential scope
 (`x-amz-credential`) that you used to generate the signing key, and
 the date (`x-amz-date`) used to calculate the signature. Amazon S3 uses this
 information to re-create the signature. If the signatures match, Amazon S3 processes the
 request.


###### Note

The variable `${filename}` is automatically replaced with the name of the file
 provided by the user and is recognized by all form fields. If the browser or
 client provides a full or partial path to the file, only the text following the
 last slash (/) or backslash (\) is used (for example, `C:\Program
 Files\directory1\file.txt` is interpreted as `file.txt`).
 If no file or file name is provided, the variable is replaced with an empty
 string.


If you don't provide elements required for authenticated requests, such as the
 `policy` element, the request is assumed to be anonymous and will
 succeed only if you have configured the bucket for public read and write. 




| Element Name | Description | Required |
| --- | --- | --- |
| `acl` | An Amazon S3 access control list (ACL). If an invalid ACL is specified, Amazon S3 denies the
 request. For more information about ACLs, see [Using Amazon S3
 ACLs](../userguide/S3_ACLs_UsingACLs.md "../userguide/S3_ACLs_UsingACLs.md").
Type: String
Default: private
 
Valid Values: `private | public-read | public-read-write | aws-exec-read | authenticated-read | bucket-owner-read | bucket-owner-full-control` 
 | No |
| `Cache-Control`
`Content-Type`
`Content-Disposition`
`Content-Encoding`
`Expires` | REST-specific headers. For more information, see [PutObject](API_PutObject.md "API_PutObject.md"). | No |
| `key` | The key name of the uploaded object.
To use the file name provided by the user, use the ${filename}
 variable. For example, if you upload a file
 `photo1.jpg` and you specify
 `/user/user1/${filename}` as key name, the file
 is stored as `/user/user1/photo1.jpg`.
For more information, see [Object Key and
 Metadata](../userguide/UsingMetadata.md "../userguide/UsingMetadata.md") in the
 *Amazon Simple Storage Service User Guide*. | Yes |
| `policy` | The base64-encoded security policy that describes what is permitted in the request.
 For authenticated requests, a policy is required. 
Requests without a security policy are considered anonymous
 and will succeed only on a publicly writable bucket.  | Required for authenticated requests |
| `success_action_redirect` | The URL to which the client is redirected upon successful
 upload.
If `success_action_redirect` is not specified, or
 Amazon S3 cannot interpret the URL, Amazon S3 returns the empty document
 type that is specified in the `success_action_status`
 field.
If the upload fails, Amazon S3 returns an error and does not
 redirect the user to another URL.
 | No |
| `success_action_status` | The status code returned to the client upon successful upload
 if `success_action_redirect` is not specified.
Valid values are `200`, `201`, or
 `204` (default).
If the value is set to 200 or 204, Amazon S3 returns an empty
 document with the specified status code.
If the value is set to 201, Amazon S3 returns an XML document with
 a 201 status code. For information about the content of the XML
 document, see [POST Object](RESTObjectPOST.md "RESTObjectPOST.md").
If the value is not set or is invalid, Amazon S3 returns an empty
 document with a 204 status code. 
NoteSome versions of the Adobe Flash player do not properly
 handle HTTP responses with an empty body. To support uploads
 through Adobe Flash, we recommend setting
 `success_action_status` to 201. | No |
| `x-amz-algorithm` | The signing algorithm used to authenticate the request. For
 AWS Signature Version 4, the value is
 `AWS4-HMAC-SHA256`.
 This field is required if a policy document is included with
 the request. | Required for authenticated requests |
| `x-amz-credential` |  In addition to your access key ID, this field also
 provides scope information identifying region and service for
 which the signature is valid. This should be the same scope you
 used in calculating the signing key for signature calculation.
 It is a string of the following
 form:```<your-access-key-id>`/`<date>`/`<aws-region>`/`<aws-service>`/aws4_request`` For example:
``AKIAIOSFODNN7EXAMPLE/20130728/us-east-1/s3/aws4_request``
 
 For Amazon S3, the *aws-service* string is
 `s3`. For a list of Amazon S3 `aws-region`
 strings, see [Regions and
 Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region "https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region") in the *AWS General Reference*.
 This is required if a policy document is included with the
 request. | Required for authenticated requests |
| `x-amz-date` | It is the date value in ISO8601 format. For example,
 `20130728T000000Z`. 
It is the same date you used in creating the signing key (for
 example, 20130728). This must also be the same value you provide
 in the policy (`x-amz-date`) that you signed. 
This is required if a policy document is included with the
 request. | Required for authenticated requests |
| `x-amz-security-token` | A security token used by Amazon DevPay and session credentials
 If the request is using Amazon DevPay, it requires two
 `x-amz-security-token` form fields: one for the
 product token and one for the user token. For more information,
 see [Using
 DevPay](../userguide/UsingDevPay.md "../userguide/UsingDevPay.md") in the
 *Amazon Simple Storage Service User Guide*.
If the request is using session credentials, it requires one
 `x-amz-security-token` form. For more
 information, see [Requesting Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html") in the
 *IAM User Guide*. | No |
| `x-amz-signature` | (AWS Signature Version 4) The HMAC-SHA256 hash of the security
 policy. 
 This field is required if a policy document is included with
 the request. | Required for authenticated requests |
| `x-amz-meta-*` | Field names starting with this prefix are user-defined
 metadata. Each one is stored and returned as a set of key-value
 pairs. Amazon S3 doesn't validate or interpret user-defined metadata.
 For more information, see [PutObject](API_PutObject.md "API_PutObject.md"). | No |
| `x-amz-*` | See POST Object ([POST Object](RESTObjectPOST.md "RESTObjectPOST.md") for other
 `x-amz-*` headers. | No |
| `file` | File or text content. 
The file or content must be the last field in the form.
You cannot upload more than one file at a time. | Yes |


Conditional items are required for authenticated requests and are optional for
 anonymous requests. 


Now that you know how to create forms, next you can create a security policy that you can
 sign. For more information, see [POST Policy](sigv4-HTTPPOSTConstructPolicy.md "sigv4-HTTPPOSTConstructPolicy.md").
