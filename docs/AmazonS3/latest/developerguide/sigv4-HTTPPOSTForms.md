# Creating an HTML Form (Using AWS Signature Version 4)

###### Topics

- [HTML Form Declaration](#HTTPPOSTFormDeclaration "#HTTPPOSTFormDeclaration")
- [HTML Form Fields](#sigv4-HTTPPOSTFormFields "#sigv4-HTTPPOSTFormFields")
  To allow users to upload content to Amazon S3 by using their browsers (HTTP POST requests),
  you use HTML forms. HTML forms consist of a form declaration and form fields. The form
  declaration contains high-level information about the request. The form fields contain
  detailed request information.

This section describes how to create HTML forms. For a working example of
browser-based upload using HTTP POST and related signature calculations for request
authentication, see [Example: Browser-Based Upload using HTTP POST (Using AWS Signature Version 4)](sigv4-post-example.md "sigv4-post-example.md").

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

- `action` – The URL that processes the request, which must
  be set to the URL of the bucket. For example, if the name of your bucket is
  `examplebucket`, the URL is
  `http://examplebucket.s3.amazonaws.com/`.

###### Note

The key name is specified in a form field.

- `method` – The method must be POST.
- `enctype` – The enclosure type (`enctype`) must
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

| Element Name                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Required                            |
| --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ----------------- | ------------- | ------------------ | ----------------- | -------------------------- | --- |
| `acl`                                                                                         | An Amazon S3 access control list (ACL). If an invalid ACL is specified, Amazon S3 denies the<br>request. For more information about ACLs, see [Using Amazon S3<br>ACLs](../userguide/S3_ACLs_UsingACLs.md "../userguide/S3_ACLs_UsingACLs.md").<br>Type: String<br>Default: private<br>Valid Values: `private                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | public-read                         | public-read-write | aws-exec-read | authenticated-read | bucket-owner-read | bucket-owner-full-control` | No  |
| `Cache-Control`<br>`Content-Type`<br>`Content-Disposition`<br>`Content-Encoding`<br>`Expires` | REST-specific headers. For more information, see [PutObject](../API/API_PutObject.md "../API/API_PutObject.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | No                                  |
| `key`                                                                                         | The key name of the uploaded object.<br>To use the file name provided by the user, use the ${filename}<br>variable. For example, if you upload a file<br>`photo1.jpg` and you specify<br>`/user/user1/${filename}`as key name, the file<br>is stored as`/user/user1/photo1.jpg`.<br>For more information, see [Object Key and<br>Metadata](../userguide/UsingMetadata.md "../userguide/UsingMetadata.md") in the<br>_Amazon Simple Storage Service User Guide_.                                                                                                                                                                                                                                                                                                                                                               | Yes                                 |
| `policy`                                                                                      | The base64-encoded security policy that describes what is permitted in the request.<br>For authenticated requests, a policy is required.<br>Requests without a security policy are considered anonymous<br>and will succeed only on a publicly writable bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Required for authenticated requests |
| `success_action_redirect`                                                                     | The URL to which the client is redirected upon successful<br>upload.<br>If `success_action_redirect` is not specified, or<br>Amazon S3 cannot interpret the URL, Amazon S3 returns the empty document<br>type that is specified in the `success_action_status`<br>field.<br>If the upload fails, Amazon S3 returns an error and does not<br>redirect the user to another URL.                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No                                  |
| `success_action_status`                                                                       | The status code returned to the client upon successful upload<br>if `success_action_redirect` is not specified.<br>Valid values are `200`, `201`, or<br>`204` (default).<br>If the value is set to 200 or 204, Amazon S3 returns an empty<br>document with the specified status code.<br>If the value is set to 201, Amazon S3 returns an XML document with<br>a 201 status code. For information about the content of the XML<br>document, see [POST Object](RESTObjectPOST.md "RESTObjectPOST.md").<br>If the value is not set or is invalid, Amazon S3 returns an empty<br>document with a 204 status code.<br>NoteSome versions of the Adobe Flash player do not properly<br>handle HTTP responses with an empty body. To support uploads<br>through Adobe Flash, we recommend setting<br>`success_action_status` to 201. | No                                  |
| `x-amz-algorithm`                                                                             | The signing algorithm used to authenticate the request. For<br>AWS Signature Version 4, the value is<br>`AWS4-HMAC-SHA256`.<br>This field is required if a policy document is included with<br>the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Required for authenticated requests |
| `x-amz-credential`                                                                            | In addition to your access key ID, this field also<br>provides scope information identifying region and service for<br>which the signature is valid. This should be the same scope you<br>used in calculating the signing key for signature calculation.<br>It is a string of the following<br>form:```<your-access-key-id>`/`<date>`/`<aws-region>`/`<aws-service>`/aws4_request`` For example:<br>`AKIAIOSFODNN7EXAMPLE/20130728/us-east-1/s3/aws4_request`<br>For Amazon S3, the *aws-service<br>• string is<br>`s3`. For a list of Amazon S3 `aws-region`<br>strings, see [Regions and<br>Endpoints](../../../general/latest/gr/rande.md#s3_region "../../../general/latest/gr/rande.md#s3_region") in the *AWS General Reference\*.<br>This is required if a policy document is included with the<br>request.            | Required for authenticated requests |
| `x-amz-date`                                                                                  | It is the date value in ISO8601 format. For example,<br>`20130728T000000Z`.<br>It is the same date you used in creating the signing key (for<br>example, 20130728). This must also be the same value you provide<br>in the policy (`x-amz-date`) that you signed.<br>This is required if a policy document is included with the<br>request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Required for authenticated requests |
| `x-amz-security-token`                                                                        | A security token used by Amazon DevPay and session credentials<br>If the request is using Amazon DevPay, it requires two<br>`x-amz-security-token` form fields: one for the<br>product token and one for the user token. For more information,<br>see [Using<br>DevPay](../userguide/UsingDevPay.md "../userguide/UsingDevPay.md") in the<br>_Amazon Simple Storage Service User Guide_.<br>If the request is using session credentials, it requires one<br>`x-amz-security-token` form. For more<br>information, see [Requesting Temporary Security Credentials](../../../IAM/latest/UserGuide/id_credentials_temp_request.md "../../../IAM/latest/UserGuide/id_credentials_temp_request.md") in the<br>_IAM User Guide_.                                                                                                    | No                                  |
| `x-amz-signature`                                                                             | (AWS Signature Version 4) The HMAC-SHA256 hash of the security<br>policy.<br>This field is required if a policy document is included with<br>the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Required for authenticated requests |
| `x-amz-meta-*`                                                                                | Field names starting with this prefix are user-defined<br>metadata. Each one is stored and returned as a set of key-value<br>pairs. Amazon S3 doesn't validate or interpret user-defined metadata.<br>For more information, see [PutObject](../API/API_PutObject.md "../API/API_PutObject.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | No                                  |
| `x-amz-*`                                                                                     | See POST Object ([POST Object](RESTObjectPOST.md "RESTObjectPOST.md") for other<br>`x-amz-*` headers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | No                                  |
| `file`                                                                                        | File or text content.<br>The file or content must be the last field in the form.<br>You cannot upload more than one file at a time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Yes                                 |

Conditional items are required for authenticated requests and are optional for
anonymous requests.

Now that you know how to create forms, next you can create a security policy that you can
sign. For more information, see [POST Policy](sigv4-HTTPPOSTConstructPolicy.md "sigv4-HTTPPOSTConstructPolicy.md").
