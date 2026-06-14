# POST Policy

###### Topics

- [Expiration](#sigv4-HTTPPOSTExpiration "#sigv4-HTTPPOSTExpiration")
- [Condition Matching](#sigv4-ConditionMatching "#sigv4-ConditionMatching")
- [Conditions](#sigv4-PolicyConditions "#sigv4-PolicyConditions")
- [Character Escaping](#sigv4-HTTPPOSTEscaping "#sigv4-HTTPPOSTEscaping")
  The policy required for making authenticated requests using HTTP POST is a UTF-8 and
  base64-encoded document written in JavaScript Object Notation (JSON) that specifies
  conditions that the request must meet. Depending on how you design your policy document,
  you can control the access granularity per-upload, per-user, for all uploads, or
  according to other designs that meet your needs.

This section describes the POST policy. For example signature calculations using POST
policy, see [Example: Browser-Based Upload using HTTP POST (Using AWS Signature Version 4)](sigv4-post-example.md "sigv4-post-example.md").

###### Note

Although the policy document is optional, we highly recommend that you use one in
order to control what is allowed in the request. If you make the bucket publicly
writable, you have no control at all over which users can write to your
bucket.

The following is an example of a POST policy document.

```
{ "expiration": "2007-12-01T12:00:00.000Z",
  "conditions": [
    {"acl": "public-read" },
    {"bucket": "johnsmith" },
    ["starts-with", "$key", "user/eric/"],
  ]
}
```

The POST policy always contains the `expiration` and
`conditions` elements. The example policy uses two condition matching
types (exact matching and starts-with matching). The following sections describe these
elements.

## Expiration

The `expiration` element specifies the expiration date and time of the
POST policy in ISO8601 GMT date format. For example,
`2013-08-01T12:00:00.000Z` specifies that the POST policy is not
valid after midnight GMT on August 1, 2013.

## Condition Matching

Following is a table that describes condition matching types that you can use to
specify POST policy conditions (described in the next section). Although you must
specify at least one condition for each form field that you specify in the form, you can
create more complex matching criteria by specifying multiple conditions for a form
field.

| Condition Match Type                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Exact Matches                                    | The form field value must match the value specified. This<br>example indicates that the ACL must be set to<br>public-read:<br>`<br>{"acl": "public-read" }<br>`<br>This example is an alternate way to indicate that the ACL must<br>be set to public-read:<br>`<br>[ "eq", "$acl", "public-read" ]<br>`                                                                                                                                                                                                                                                                                  |
| Starts With                                      | The value must start with the specified value. This example<br>indicates that the object key must start with user/user1:<br>`<br>["starts-with", "$key", "user/user1/"]<br>`                                                                                                                                                                                                                                                                                                                                                                                                              |
| Matching Content-Types in a Comma-Separated List | Content-Types values for a `starts-with` condition that include commas are interpreted as lists. Each value in the list must meet the condition for the whole condition to pass. For example,given the following condition:<br>`<br>["starts-with", "$Content-Type", "image/"]<br>`<br>The following value would pass the condition:<br>`<br>"image/jpg,image/png,image/gif"<br>`<br>The following value would not pass the condition:<br>`<br>["image/jpg,text/plain"]<br>`<br>NoteData elements other than `Content-Type` are treated as strings, regardless of the presence of commas. |
| Matching Any Content                             | To configure the POST policy to allow any content within a<br>form field, use `starts-with` with an empty value<br>(""). This example allows any value for<br>`success_action_redirect`:<br>`<br>["starts-with", "$success_action_redirect", ""]<br>`                                                                                                                                                                                                                                                                                                                                     |
| Specifying Ranges                                | For form fields that accept a range, separate the upper and<br>lower limit with a comma. This example allows a file size from 1<br>to 10 MiB:<br>`<br>["content-length-range", 1048576, 10485760]<br>`                                                                                                                                                                                                                                                                                                                                                                                    |

The specific conditions supported in a POST policy are described in [Conditions](#sigv4-PolicyConditions "#sigv4-PolicyConditions").

## Conditions

The `conditions` in a POST policy is an array of objects, each of which is used
to validate the request. You can use these conditions to restrict what is allowed in
the request. For example, the preceding policy conditions require the
following:

- Request must specify the `johnsmith` bucket name.
- Object key name must have the `user/eric` prefix.
- Object ACL must be set to `public-read`.

Each form field that you specify in a form (except `x-amz-signature`,
`file`, `policy`, and field names that have an
`x-ignore-` prefix) must appear in the list of conditions.

###### Note

All variables within the form are expanded prior to validating the POST policy.
Therefore, all condition matching should be against the expanded form fields.
Suppose that you want to restrict your object key name to a specific prefix
(`user/user1`). In this case, you set the key form field to
`user/user1/${filename}`. Your POST policy should be `[
 "starts-with", "$key", "user/user1/" ]` (do not enter `[
 "starts-with", "$key", "user/user1/${filename}" ]`). For more
information, see [Condition Matching](#sigv4-ConditionMatching "#sigv4-ConditionMatching").

Policy document conditions are described in the following table.

| Element Name                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `acl`                                                                                         | Specifies the ACL value that must be used in the form<br>submission.<br>This condition supports exact matching and<br>`starts-with` condition match type discussed in<br>the following section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `bucket`                                                                                      | Specifies the acceptable bucket name.<br>This condition supports exact matching condition match<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `content-length-range`                                                                        | The minimum and maximum allowable size for the uploaded<br>content.<br>This condition supports `content-length-range`<br>condition match type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `Cache-Control`<br>`Content-Type`<br>`Content-Disposition`<br>`Content-Encoding`<br>`Expires` | REST-specific headers. For more information, see [POST Object](RESTObjectPOST.md "RESTObjectPOST.md").<br>This condition supports exact matching and<br>`starts-with` condition match type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `key`                                                                                         | The acceptable key name or a prefix of the uploaded<br>object.<br>This condition supports exact matching and<br>`starts-with` condition match type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `success_action_redirect`<br>`redirect`                                                       | The URL to which the client is redirected upon successful<br>upload.<br>This condition supports exact matching and<br>`starts-with` condition match type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `success_action_status`                                                                       | The status code returned to the client upon successful upload<br>if `success_action_redirect` is not specified.<br>This condition supports exact matching.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `x-amz-algorithm`                                                                             | The signing algorithm that must be used during signature<br>calculation. For AWS Signature Version 4, the value is<br>`AWS4-HMAC-SHA256`.<br>This condition supports exact matching.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `x-amz-credential`                                                                            | The credentials that you used to calculate the signature. It<br>provides access key ID and scope information identifying region<br>and service for which the signature is valid. This should be the<br>same scope you used in calculating the signing key for signature<br>calculation.<br>It is a string of the following form:<br>``<your-access-key-id>`/`<date>`/`<aws-region>`/`<aws-service>`/aws4_request`<br>For example:<br>`AKIAIOSFODNN7EXAMPLE/20130728/us-east-1/s3/aws4_request`<br>For Amazon S3, the aws-service string is `s3`. For a<br>list of Amazon S3 `aws-region` strings, see [Regions and<br>Endpoints](../../../general/latest/gr/rande.md#s3_region "../../../general/latest/gr/rande.md#s3_region") in the _AWS General Reference_.<br>This is required if a POST policy document is included with the<br>request.<br>This condition supports exact matching. |
| `x-amz-date`                                                                                  | The date value specified in the ISO8601 formatted string. For<br>example, `20130728T000000Z`. The date must be same<br>that you used in creating the signing key for signature<br>calculation.<br>This is required if a POST policy document is included with<br>the request.<br>This condition supports exact matching.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `x-amz-security-token`                                                                        | Amazon DevPay security token.<br>Each request that uses Amazon DevPay requires two<br>`x-amz-security-token` form fields: one for the<br>product token and one for the user token. As a result, the<br>values must be separated by commas. For example, if the user<br>token is `eW91dHViZQ==` and the product token is<br>`b0hnNVNKWVJIQTA=`, you set the POST policy entry<br>to: `{ "x-amz-security-token":<br>"eW91dHViZQ==,b0hnNVNKWVJIQTA=" }`.<br>For more information about Amazon DevPay, see [Using DevPay](../userguide/UsingDevPay.md "../userguide/UsingDevPay.md") in<br>the _Amazon Simple Storage Service User Guide_.                                                                                                                                                                                                                                                    |
| `x-amz-meta-*`                                                                                | User-specified metadata.<br>This condition supports exact matching and<br>`starts-with` condition match type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `x-amz-*`                                                                                     | See POST Object ([POST Object](RESTObjectPOST.md "RESTObjectPOST.md") for other<br>`x-amz-*` headers.<br>This condition supports exact matching.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

###### Note

If your toolkit adds more form fields (for example, Flash adds `filename`),
you must add them to the POST policy document. If you can control this
functionality, prefix `x-ignore-` to the field so Amazon S3 ignores the
feature and it won't affect future versions of this feature.

## Character Escaping

Characters that must be escaped within a POST policy document are described in the
following table.

| Escape Sequence | Description            |
| --------------- | ---------------------- |
| \\              | Backslash              |
| \$              | Dollar symbol          |
| \b              | Backspace              |
| \f              | Form feed              |
| \n              | New line               |
| \r              | Carriage return        |
| \t              | Horizontal tab         |
| \v              | Vertical tab           |
| \u`xxxx`        | All Unicode characters |

Now that you are acquainted with forms and policies, and understand how signing
works, you can try a POST upload example. You need to write the code to calculate
the signature. The example provides a sample form, and a POST policy that you can
use to test your signature calculations. For more information, see [Example: Browser-Based Upload using HTTP POST (Using AWS Signature Version 4)](sigv4-post-example.md "sigv4-post-example.md").
