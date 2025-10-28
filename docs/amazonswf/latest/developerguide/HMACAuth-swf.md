# Calculating the HMAC-SHA Signature for Amazon SWF

Every request to Amazon SWF must be authenticated. The AWS SDKs automatically sign your requests
and manage your token-based authentication. However, if you want to write your own HTTP
`POST` requests, you need to create an
`x-amzn-authorization` value for the HTTP `POST Header`
content as part of your request authentication.

For more information about formatting headers, see [HTTP Header Contents](UsingJSON-swf.md#HTTPHeader "UsingJSON-swf.md#HTTPHeader"). For the AWS SDK for Java implementation of AWS Version 3
signing, see the [AWSSigner.java](https://github.com/aws/aws-sdk-java/blob/master/aws-java-sdk-core/src/main/java/com/amazonaws/auth/AWS3Signer.java "https://github.com/aws/aws-sdk-java/blob/master/aws-java-sdk-core/src/main/java/com/amazonaws/auth/AWS3Signer.java") class.

## Creating a Request Signature

Before you create an HMAC-SHA request signature, you must get your
AWS credentials (the Access Key ID and the Secret Key).

###### Important

You can use either SHA1 or SHA256 to sign your requests. However, make sure that
you use the same method throughout the signing process. The method you choose must
match the value of the `Algorithm` name in the HTTP header.

### To create the request signature

1.  Create a canonical form of the HTTP request headers. The canonical form of the
    HTTP header includes the following:

        * `host`
        * Any header element starting with `x-amz-`

    For more information about the included headers, see [HTTP Header Contents](UsingJSON-swf.md#HTTPHeader "UsingJSON-swf.md#HTTPHeader").

        1. For each header name-value pair, convert the header name (but not the
         header value) to lowercase.
        2. Build a map of the header name to comma-separated header values.



        ```
        x-amz-example: value1
        x-amz-example: value2  =>  x-amz-example:value1,value2
        ```

        For more information, see [Section 4.2 of RFC 2616](http://tools.ietf.org/html/rfc2616 "http://tools.ietf.org/html/rfc2616").
        3. For each header name-value pair, convert the name-value pair into a
         string in the format `headerName:headerValue`. Trim any
         whitespace from the beginning and end of both `headerName` and
         `headerValue`, with no spaces on each side of the
         colon.



        ```
        x-amz-example1:value1,value2
        x-amz-example2:value3
        ```
        4. Insert a new line (`U+000A`) after each converted string,
         including the last string.
        5. Sort the collection of converted strings alphabetically, by header
         name.

2.  Create a string-to-sign value that includes the following items:
    - Line `1`: The HTTP method (`POST`),
      followed by a newline.
    - Line `2`: The request URI (`/`), followed
      by a newline.
    - Line `3`: An empty string followed by a newline.

    ###### Note

    Typically, the query string appears here, but Amazon SWF doesn't use a
    query string.
    - Lines `4–n`: The string representing the canonicalized
      request headers that you computed in Step 1, followed by a newline. This
      newline creates a blank line between the headers and the body of the HTTP
      request. For more information, see [RFC
      2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html "http://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html").
    - The request body, _not_ followed by a newline.

3.  Compute the SHA256 or SHA1 digest of the string-to-sign value. Use the same SHA
    method throughout the process.
4.  Compute and Base64-encode the HMAC-SHA using either a SHA256 or a SHA1 digest
    (depending on the method you used) of the value resulting from the previous step
    and the temporary secret access key from the AWS Security Token
    Service using the `GetSessionToken` API action.

###### Note

Amazon SWF expects an equals sign (`=`) at the end of the Base64-encoded HMAC-SHA
value. If your Base64 encoding routine doesn't include the appended equals sign,
append one to the end of the value.

For more information about using temporary security credentials with Amazon SWF and
other AWS services, see [AWS Services
That Work with IAM](../../../STS/latest/UsingSTS/UsingTokens.md "../../../STS/latest/UsingSTS/UsingTokens.md") in the
_IAM User Guide_. 5. Place the resulting value as the value for the `Signature`
name in the `x-amzn-authorization` header of the HTTP request
to Amazon SWF. 6. Amazon SWF verifies the request and performs the specified operation.
