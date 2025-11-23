# The IAM Roles Anywhere authentication signing

process

The signing process is identical to SigV4, with the exception of the keys used, the signature algorithm, and the addition of headers related to the X.509 certificate and trust chain. For more information, see [AWS Signature Version 4 for API requests](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md"), which should be treated as authoritative unless specifically addressed in this user guide.

###### Topics

- [Task 1: Create a canonical request](#authentication-task1 "#authentication-task1")
- [Task 2: Create a string to sign](#authentication-task2 "#authentication-task2")
- [Task 3: Calculate the signature](#authentication-task3 "#authentication-task3")
- [Task 4: Add the signature to the HTTP request](#authentication-task4 "#authentication-task4")

## Task 1: Create a canonical request

To begin the signing process, create a string that includes information from your request in a standardized (canonical) format. This ensures that when the request is received, the string to sign can be calculated in the same way you did. This string will then be used for signature verification by IAM Roles Anywhere.

Follow the steps below to create a canonical version of the request. Otherwise, your version and the version calculated by AWS won't match, and the request will be denied.

The following example shows the pseudocode to create a canonical request.

###### Example Canonical request pseudocode

```

    CanonicalRequest =
      `HttpRequestMethod` + '\n' +
      `CanonicalUri` + '\n' +
      `CanonicalQueryString` + '\n' +
      `CanonicalHeaders` + '\n' +
      `SignedHeaders` + '\n' +
      Lowercase(Hex(SHA256(`RequestPayload`)))

```

A canonical request has the above structure, in which specific elements of the request are transformed into a canonical value and concatenated together with other elements, joined with a newline character.

The following examples shows how to construct the canonical form of a request to IAM Roles Anywhere. The original request might look like this as it is sent from the client to AWS.

###### Example Request

```

    POST /sessions HTTP/1.1
    Host: rolesanywhere.us-east-1.amazonaws.com
    Content-Type: application/json
    X-Amz-Date: 20211103T120000Z
    X-Amz-X509: {`base64-encoded DER data`}
    {
      "durationSeconds": `number`,
      "profileArn": `string`,
      "roleArn": `string`,
      "trustAnchorArn": `string`
    }

```

**To create a canonical request, concatenate the following components from each step into a single string:**

1. The `HttpRequestMethod` is the verb of the HTTP request, in upper case. From the example, `POST`.
2. The `CanonicalUri` is the path of the request up until the query string delimiter `?`. From the example, `/sessions`. The path MUST be normalized according to RFC 3986, with redundant and relative path components removed. Path segments MUST be URI-encoded twice.
3. The `CanonicalQueryString` is the string following `?` in the request URI. If the request does not include a query string, use an empty string (essentially, a blank line). The example request does not include a query string, therefore we will use an empty string. To construct the canonical query string, complete the following steps:
   1. Sort the parameter names by character code point in ascending order. Parameters with duplicate names should be sorted by value. For example, a parameter name that begins with the uppercase letter F precedes a parameter name that begins with a lowercase letter b.
   2. URI-encode each parameter name and value according to the following rules:
      1. Do not URI-encode any of the unreserved characters that RFC 3986 defines: A-Z, a-z, 0-9, hyphen ( ‐ ), underscore ( \_ ), period ( . ), and tilde ( ˜ ).
      2. Percent-encode all other characters with %XY, where X and Y are hexadecimal characters (0-9 and uppercase A-F). For example, the space character must be encoded as %20 (not using '+', as some encoding schemes do) and extended UTF-8 characters must be in the form %XY%ZA%BC.
      3. Double-encode any equals ( = ) characters in parameter values.

   3. Build the canonical query string by starting with the first parameter name in the sorted list.
   4. For each parameter, append the URI-encoded parameter name, followed by the equals sign character (=), followed by the URI-encoded parameter value. Use an empty string for parameters that have no value.
   5. Append the ampersand character (&) after each parameter value, except for the last value in the list.

4. The `CanonicalHeaders` is a string capturing the header key and value that are included in the signature. The field is structured as follows:

```

    CanonicalHeaders =
      `CanonicalHeadersEntry0 + CanonicalHeadersEntry1 + ... + CanonicalHeadersEntryN`
    CanonicalHeadersEntry =
      Lowercase(`HeaderName`) + ':' + Trimall(`HeaderValue`) + '\n'

```

Lowercase represents a function that converts all characters to lowercase. The `TrimAll` function removes excess white space before and after values, and converts sequential spaces to a single space.

###### Important

The signing certificate MUST be presented in the header `X-Amz-X509`, as base64-encoded Distinguished Encoding Rules (DER), and the `X-Amz-X509` header MUST be included in `CanonicalHeaders` and `SignedHeaders`

If the client is providing the chain of intermediate certificates, the `X-Amz-X509-Chain` MUST be added to the request as well.

Build the canonical headers list by sorting the (lowercase) headers by character code and then iterating through the header names. Construct each header according to the following rules:

    * Append the lowercase header name followed by a colon.
    * Append a comma-separated list of values for that header. Do not sort the values in headers that have multiple values.
    * Append a new line ('\n').

5. The `SignedHeaders` is a list of the header names, sorted by lowercase character code, delimited by semi-colon. For example – `content-type;host;x-amz-date;x-amz-x509`
6. A hash of the request payload is appended to the canonical request. The bytes of the request are encoded as UTF-8, hashed with SHA-256, the resulting bytes hex encoded, and finally lowercased.
7. To construct the finished canonical request, combine all the components from each step as a single string. As noted, each component ends with a newline character. If you follow the canonical request pseudocode explained earlier, the resulting canonical request is shown in the following example.

**Example Canonical request**

```

    POST
    /sessions

    content-type:application/json
    host:rolesanywhere.us-east-1.amazonaws.com
    x-amz-date:20211103T120000Z
    x-amz-x509:{base64-encoded DER data}

    content-type;host;x-amz-date;x-amz-x509
    e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

```

8. Create a digest (hash) of the canonical request with the same algorithm that you used to hash the payload. The bytes of the request are encoded as UTF-8, hashed with SHA-256, the resulting bytes hex encoded, and finally lowercased.

## Task 2: Create a string to sign

The “string to sign” is the actual input to the signing algorithm, and includes meta information about the request, along with the canonical request created in the previous step.

###### Example StringToSign pseudocode

```
 StringToSign = `Algorithm` + '\n' + `RequestDateTime` + '\n' + `CredentialScope` + '\n' + `HashedCanonicalRequest`
```

###### The structure is as follows:

1. The `Algorithm` is a string that indicates how the signature is calculated. It must be one of `AWS4-X509-RSA-SHA256`, `AWS4-X509-ECDSA-SHA256` or `AWS4-X509-MLDSA` and MUST be supported by the key type of the signing certificate's private key. For example, if the signing certificate has an RSA private key, the full algorithm string will be `AWS4-X509-RSA-SHA256`.
2. The `RequestDateTime` is a string derived at time of the signing operation, at second granularity, in UTC, formatted as ISO8601 basic, YYYYMMDD’T’HHMMSS’Z’. For example, `20211101T121030Z`.
3. The CredentialScope is structured field of the form `Date + '/' + Region + '/' + Service + '/aws4_request’`. The Region and service name strings must be UTF-8 encoded. For example, `20211101/us-east-1/rolesanywhere/aws4_request`.
4. Finally, append a newline followed by the HashedCanonicalRequest computed in the previous step.

## Task 3: Calculate the signature

```

    Signature = HexEncode(`SigningAlgorithm(CertPrivateKey,StringToSign)`)

```

SigningAlgorithm must be one of the following algorithms

- SHA256WithRSA
- SHA256WithECDSA
- ML-DSA-44
- ML-DSA-65
- ML-DSA-87

## Task 4: Add the signature to the HTTP request

The signature derived from the previous step is added to the HTTP request in the `Authorization` header field. The `Authorization` header is attached to the request and validated for authentication. It is partitioned into multiple fields – signing algorithm, credentials, signed headers, and the actual signature. The header of the authentication mechanism based on X.509 differs from a SigV4 header in two ways:

- Algorithm. As described above, instead of `AWS4-HMAC-SHA256`, the algorithm field will have the values of the form `AWS4-X509-RSA-SHA256`, `AWS4-X509-ECDSA-SHA256` or `AWS4-X509-MLDSA` depending on whether an RSA, Elliptic Curve algorithm or ML-DSA is used. This, in turn, is determined by the key bound to the signing certificate.
- Scope field/credentials. As specified above, the serial number of the certificate used to sign the request will be in place of the Access Key ID (credential) in the Scope field.

###### The structure of the field is as follows:

```

      Authorization: {`Algorithm`} Credential={`CredentialString`}, SignedHeaders={`SignedHeaders`}, Signature={`Signature`}

```

1. The `Algorithm` must be one of `AWS4-X509-RSA-SHA256`, `AWS4-X509-ECDSA-SHA256` or `AWS4-X509-MLDSA`.
2. The `Credential` is constructed via `{SerialNumber}/{Scope}` where serial number is the decimal representation of the serial number of the signing certificate, and `Scope` is the value constructed as input to the `StringToSign`. For example:

```

    Credential=11111222223333344444/20201105/us-east-1/rolesanywhere/aws4_request

```

3. The `SignedHeaders` is a comma-delimited list of the headers signed as part of the request.
4. The `Signature` is the hex encoded output of the previous step.
