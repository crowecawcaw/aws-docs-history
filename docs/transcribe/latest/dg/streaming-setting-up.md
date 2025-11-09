# Setting up a streaming transcription

This section expands on the main [streaming](streaming.md "streaming.md") section. It's
intended to provide information for users who want to set up their stream with HTTP/2 or
WebSockets directly, rather than with an AWS SDK. The information in this
section can also be used to build your own SDK.

###### Important

We strongly recommend using SDKs rather than using HTTP/2 and WebSockets
directly. SDKs are the simplest and most reliable method for transcribing data streams. To start
streaming using an AWS SDK, see [Transcribing with the AWS SDKs](getting-started-sdk-streaming.md "getting-started-sdk-streaming.md").

The key components for an [HTTP/2 protocol](https://http2.github.io/ "https://http2.github.io/") for
streaming transcription requests with Amazon Transcribe are:

- A header frame. This contains the HTTP/2 headers for your request, and a signature in the
  authorization header that Amazon Transcribe uses as a seed signature to sign the data
  frames.
- One or more message frames in [event stream
  encoding](#streaming-event-stream "#streaming-event-stream") that contain metadata and raw audio bytes.
- An end frame. This is a signed message in [event
  stream encoding](#streaming-event-stream "#streaming-event-stream") with an empty body.

###### Note

Amazon Transcribe only supports one stream per HTTP/2 session. If you attempt to use multiple
streams, your transcription request fails.

1. Attach the following policy to the IAM role that makes the request.
   See [Adding IAM policies](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policy-api "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policy-api") for more information.
2. To start the session, send an HTTP/2 request to Amazon Transcribe.

```
POST /stream-transcription HTTP/2
host: transcribestreaming.`us-west-2`.amazonaws.com
X-Amz-Target: com.amazonaws.transcribe.Transcribe.`StartStreamTranscription`
Content-Type: application/vnd.amazon.eventstream
X-Amz-Content-Sha256: `string`
X-Amz-Date: `YYYYMMDD`T`HHMMSS`Z
Authorization: AWS4-HMAC-SHA256 Credential=`access-key`/`YYYYMMDD`/`us-west-2`/transcribe/aws4_request, SignedHeaders=content-type;host;x-amz-content-sha256;x-amz-date;x-amz-target;x-amz-security-token, Signature=`string`
x-amzn-transcribe-language-code: `en-US`
x-amzn-transcribe-media-encoding: `flac`
x-amzn-transcribe-sample-rate: `16000`
transfer-encoding: chunked
```

Additional operations and parameters are listed in the [API Reference](../APIReference/API_Reference.md "../APIReference/API_Reference.md"); parameters common to all
AWS API operations are listed in the [Common Parameters](../APIReference/CommonParameters.md "../APIReference/CommonParameters.md") section.

Amazon Transcribe sends the following response:

```
HTTP/2.0 200
x-amzn-transcribe-language-code: en-US
x-amzn-transcribe-media-encoding: flac
x-amzn-transcribe-sample-rate: 16000
x-amzn-request-id: 8a08df7d-5998-48bf-a303-484355b4ab4e
x-amzn-transcribe-session-id: b4526fcf-5eee-4361-8192-d1cb9e9d6887
content-type: application/json
```

3. Create an audio event that contains your audio data. Combine the headers—described
   in the following table—with a chunk of audio bytes in an event-encoded message. To
   create the payload for the event message, use a buffer in raw-byte format.

| Header name byte length | Header name (string) | Header value type | Value string byte length | Value string (UTF-8)     |
| ----------------------- | -------------------- | ----------------- | ------------------------ | ------------------------ |
| 13                      | :content-type        | 7                 | 24                       | application/octet-stream |
| 11                      | :event-type          | 7                 | 10                       | AudioEvent               |
| 13                      | :message-type        | 7                 | 5                        | event                    |

Binary data in this example request are base64-encoded. In an actual request,
data are raw bytes.

```
:content-type: "application/vnd.amazon.eventstream"
:event-type: "AudioEvent"
:message-type: "event"
UklGRjzxPQBXQVZFZm10IBAAAAABAAEAgD4AAAB9AAACABAAZGF0YVTwPQAAAAAAAAAAAAAAAAD//wIA/f8EAA==
```

4.  Create an audio message that contains your audio data.
    1. Your audio message data frame contains event-encoding headers that
       include the current date and a signature for the audio chunk and the audio
       event.

    | Header name byte length | Header name (string) | Header value type | Value string byte length | Value               |
    | ----------------------- | -------------------- | ----------------- | ------------------------ | ------------------- |
    | 16                      | :chunk-signature     | 6                 | varies                   | generated signature |
    | 5                       | :date                | 8                 | 8                        | timestamp           |

    Binary data in this request are base64-encoded. In an actual request, data
    are raw bytes.

    ```
    :date: 2019-01-29T01:56:17.291Z
    :chunk-signature: `signature`

    AAAA0gAAAIKVoRFcTTcjb250ZW50LXR5cGUHABhhcHBsaWNhdGlvbi9vY3RldC1zdHJlYW0LOmV2ZW50LXR5
    cGUHAApBdWRpb0V2ZW50DTptZXNzYWdlLXR5cGUHAAVldmVudAxDb256ZW50LVR5cGUHABphcHBsaWNhdGlv
    bi94LWFtei1qc29uLTEuMVJJRkY88T0AV0FWRWZtdCAQAAAAAQABAIA+AAAAfQAAAgAQAGRhdGFU8D0AAAAA
    AAAAAAAAAAAA//8CAP3/BAC7QLFf
    ```

    2. Construct a string to sign, as outlined in [Create a string to sign for Signature
       Version 4](../../../general/latest/gr/sigv4-create-string-to-sign.md "../../../general/latest/gr/sigv4-create-string-to-sign.md"). Your string follows this format:

    ```
    String stringToSign =
    "AWS4-HMAC-SHA256" +
    "\n" +
    `DateTime` +
    "\n" +
    `Keypath` +
    "\n" +
    Hex(`priorSignature`) +
    "\n" +
    HexHash(`nonSignatureHeaders`) +
    "\n" +
    HexHash(`payload`);
    ```

        * **DateTime**: The date and time the signature is created. The format
         is YYYYMMDDTHHMMSSZ, where YYYY=year, MM=month, DD=day, HH=hour, MM=minute,
         SS=seconds, and 'T' and 'Z' are fixed characters. For more information, refer to
         [Handling
         Dates in Signature Version 4](../../../general/latest/gr/sigv4-date-handling.md "../../../general/latest/gr/sigv4-date-handling.md").
        * **Keypath**: The signature scope in the format
         `date/region/service/aws4_request`. For example,
         `20220127/us-west-2/transcribe/aws4_request`.
        * **Hex**: A function that encodes input into a hexadecimal
         representation.
        * **priorSignature**: The signature for the previous frame. For the
         first data frame, use the signature of the header frame.
        * **HexHash**: A function that first creates a SHA-256 hash of its
         input and then uses the Hex function to encode the hash.
        * **nonSignatureHeaders**: The DateTime header encoded as a
         string.
        * **payload**: The byte buffer containing the audio event
         data.

    3. Derive a signing key from your AWS secret access key and use it to sign the
       `stringToSign`. For a greater degree of protection, the derived key is specific
       to the date, service, and AWS Region. For more information, see
       [Calculate the signature for
       AWSSignature Version 4](../../../general/latest/gr/sigv4-calculate-signature.md "../../../general/latest/gr/sigv4-calculate-signature.md").

    Make sure you implement the `GetSignatureKey` function to
    derive your signing key. If you have not yet derived a signing key, refer to
    [Examples
    of how to derive a signing key for Signature Version 4](../../../general/latest/gr/signature-v4-examples.md "../../../general/latest/gr/signature-v4-examples.md").

    ```
    String signature = HMACSHA256(derivedSigningKey, stringToSign);
    ```

        * **HMACSHA256**: A function that creates a signature using
         the SHA-256 hash function.
        * **derivedSigningKey**: The Signature Version 4 signing
         key.
        * **stringToSign**: The string you calculated for the data
         frame.

    After you've calculated the signature for the data frame, construct a byte buffer
    containing the date, signature, and audio event payload. Send the byte array to
    Amazon Transcribe for transcription.

5.  To indicate the audio stream is complete, send an end frame (an empty data frame)
    that contains only the date and signature. You construct this end frame the same way
    that you construct a data frame.

Amazon Transcribe responds with a stream of transcription events, sent to your application.
This response is event stream encoded. It contains the standard prelude and the following
headers.

| Header name byte length | Header name (string) | Header value type | Value string byte length | Value string (UTF-8) |
| ----------------------- | -------------------- | ----------------- | ------------------------ | -------------------- |
| 13                      | :content-type        | 7                 | 16                       | application/json     |
| 11                      | :event-type          | 7                 | 15                       | TranscriptEvent      |
| 13                      | :message-type        | 7                 | 5                        | event                |

The events are sent in raw-byte format. In this example, the bytes are
base64-encoded.

```
AAAAUwAAAEP1RHpYBTpkYXRlCAAAAWiXUkMLEDpjaHVuay1zaWduYXR1cmUGACCt6Zy+uymwEK2SrLp/zVBI
5eGn83jdBwCaRUBJA+eaDafqjqI=
```

To see the transcription results, decode the raw bytes using event stream encoding.

```
:content-type: "application/vnd.amazon.eventstream"
:event-type: "TranscriptEvent"
:message-type: "event"

{
    "Transcript":
        {
            "Results":
                [
                    `results`
                ]
        }
}
```

6. To end your stream, send an empty audio event to Amazon Transcribe. Create the audio
   event exactly like any other, except with an empty payload. Sign the event and
   include the signature in the `:chunk-signature` header, as
   follows:

```
:date: 2019-01-29T01:56:17.291Z
:chunk-signature: `signature`
```

### Handling HTTP/2 streaming errors

If an error occurs when processing your media stream, Amazon Transcribe sends an exception
response. The response is event stream encoded.

The response contains the standard prelude and the following headers:

| Header name byte length | Header name (string) | Header value type | Value string byte length | Value string (UTF-8) |
| ----------------------- | -------------------- | ----------------- | ------------------------ | -------------------- |
| 13                      | :content-type        | 7                 | 16                       | application/json     |
| 11                      | :event-type          | 7                 | 19                       | BadRequestException  |
| 13                      | :message-type        | 7                 | 9                        | exception            |

When the exception response is decoded, it contains the following information:

```
:content-type: "application/vnd.amazon.eventstream"
:event-type: "BadRequestException"
:message-type: "exception"

`Exception message`
```

The key components for a [WebSocket
protocol](https://tools.ietf.org/html/rfc6455 "https://tools.ietf.org/html/rfc6455") for streaming transcription requests with Amazon Transcribe are:

- The upgrade request. This contains the query parameters for your request, and a signature
  that Amazon Transcribe uses as a seed signature to sign the data frames.
- One or more message frames in [event stream
  encoding](#streaming-event-stream "#streaming-event-stream") that contain metadata and raw audio bytes.
- An end frame. This is a signed message in [event
  stream encoding](#streaming-event-stream "#streaming-event-stream") with an empty body.

###### Note

Amazon Transcribe only supports one stream per WebSocket session. If you attempt to
use multiple streams, your transcription request fails.

1. Attach the following policy to the IAM role that makes the request.
   See [Adding IAM policies](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policy-api "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policy-api") for more information.
2. To start the session, create a presigned URL in the following format. Line breaks
   have been added for readability.

```
GET wss://transcribestreaming.`us-west-2`.amazonaws.com:8443/stream-transcription-websocket?
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=`access-key`%2F`YYYYMMDD`%2F`us-west-2`%2F`transcribe`%2Faws4_request
&X-Amz-Date=`YYYYMMDD`T`HHMMSS`Z
&X-Amz-Expires=`300`
&X-Amz-Security-Token=`security-token`
&X-Amz-Signature=`string`
&X-Amz-SignedHeaders=content-type%3Bhost%3Bx-amz-date
&language-code=`en-US`
&media-encoding=`flac`
&sample-rate=`16000`
```

###### Note

The maximum value for `X-Amz-Expires` is 300 (5 minutes).

Additional operations and parameters are listed in the [API Reference](../APIReference/API_Reference.md "../APIReference/API_Reference.md"); parameters common to all
AWS API operations are listed in the [Common Parameters](../APIReference/CommonParameters.md "../APIReference/CommonParameters.md") section.

To construct the URL for your request and create the [Signature Version 4 signature](../../../general/latest/gr/signing_aws_api_requests.md "../../../general/latest/gr/signing_aws_api_requests.md"),
refer to the following steps. Examples are in pseudocode.

    1. Create a canonical request. A canonical request is a string that includes information
     from your request in a standardized format. This ensures that when AWS receives the
     request, it can calculate the same signature you created for your URL. For more information,
     see [Create a Canonical Request for
     Signature Version 4](../../../general/latest/gr/sigv4-create-canonical-request.md "../../../general/latest/gr/sigv4-create-canonical-request.md").



    ```
    # HTTP verb
    method = "GET"
    # Service name
    service = "transcribe"
    # Region
    region = "`us-west-2`"
    # Amazon Transcribe streaming endpoint
    endpoint = "wss://transcribestreaming.`us-west-2`.amazonaws.com:8443"
    # Host
    host = "transcribestreaming.`us-west-2`.amazonaws.com:8443"
    # Date and time of request
    amz-date = `YYYYMMDD`T`HHMMSS`Z
    # Date without time for credential scope
    datestamp = `YYYYMMDD`
    ```
    2. Create a canonical URI, which is the part of the URI between the domain and the
     query string.



    ```
    canonical_uri = "/stream-transcription-websocket"
    ```
    3. Create the canonical headers and signed headers. Note the trailing `\n`
     in the canonical headers.




    	* Append the lowercase header name followed by a colon ( : ).
    	* Append a comma-separated list of values for that header. Do not sort values in
    	 headers that have multiple values.
    	* Append a new line (`\n`).

    ```
    canonical_headers = "host:" + host + "\n"
    signed_headers = "host"
    ```
    4. Match the algorithm to the hashing algorithm. Use
     `SHA-256`.



    ```
    algorithm = "AWS4-HMAC-SHA256"
    ```
    5. Create the credential scope, which scopes the derived key to the date,
     AWS Region, and service. For example, ``20220127`/`us-west-2`/transcribe/aws4_request`.



    ```
    credential_scope = datestamp + "/" + region + "/" + service + "/" + "aws4_request"
    ```
    6. Create the canonical query string. Query string values must be URI-encoded and sorted
     by name.




    	* Sort the parameter names by character code point in ascending order. Parameters
    	 with duplicate names should be sorted by value. For example, a parameter name that
    	 begins with the uppercase letter F precedes a parameter name that begins with the
    	 lowercase letter b.
    	* Do not URI-encode any of the unreserved characters that RFC 3986 defines:
    	 A-Z, a-z, 0-9, hyphen ( - ), underscore ( \_ ), period ( . ), and tilde ( ~ ).
    	* Percent-encode all other characters with %XY, where X and Y are hexadecimal
    	 characters (0-9 and uppercase A-F). For example, the space character must be
    	 encoded as %20 (don't include '+', as some encoding schemes do); extended UTF-8
    	 characters must be in the form %XY%ZA%BC.
    	* Double-encode any equals ( = ) characters in parameter values.

    ```
    canonical_querystring  = "X-Amz-Algorithm=" + algorithm
    canonical_querystring += "&X-Amz-Credential="+ URI-encode(access key + "/" + credential_scope)
    canonical_querystring += "&X-Amz-Date=" + amz_date
    canonical_querystring += "&X-Amz-Expires=300"
    canonical_querystring += "&X-Amz-Security-Token=" + token
    canonical_querystring += "&X-Amz-SignedHeaders=" + signed_headers
    canonical_querystring += "&language-code=en-US&media-encoding=flac&sample-rate=16000"
    ```
    7. Create a hash of the payload. For a `GET` request, the payload is an
     empty string.



    ```
    payload_hash = HashSHA256(("").Encode("utf-8")).HexDigest()
    ```
    8. Combine the following elements to create the canonical request.



    ```
    canonical_request = method + '\n'
       + canonical_uri + '\n'
       + canonical_querystring + '\n'
       + canonical_headers + '\n'
       + signed_headers + '\n'
       + payload_hash
    ```

3. Create the string to sign, which contains meta information about your request. You use
   the string to sign in the next step when you calculate the request signature. For more
   information, see [Create a String to Sign for Signature
   Version 4](../../../general/latest/gr/sigv4-create-string-to-sign.md "../../../general/latest/gr/sigv4-create-string-to-sign.md").

```
string_to_sign=algorithm + "\n"
   + amz_date + "\n"
   + credential_scope + "\n"
   + HashSHA256(canonical_request.Encode("utf-8")).HexDigest()
```

4. Calculate the signature. To do this, derive a signing key from your AWS secret access key.
   For a greater degree of protection, the derived key is specific to the date, service, and
   AWS Region. Use this derived key to sign the request. For more information, see
   [Calculate
   the Signature for AWS Signature Version 4](../../../general/latest/gr/sigv4-calculate-signature.md "../../../general/latest/gr/sigv4-calculate-signature.md").

Make sure you implement the `GetSignatureKey` function to derive your signing
key. If you have not yet derived a signing key, refer to [Examples of how to derive a signing key
for Signature Version 4](../../../general/latest/gr/signature-v4-examples.md "../../../general/latest/gr/signature-v4-examples.md").

```
#Create the signing key
signing_key = GetSignatureKey(secret_key, datestamp, region, service)

# Sign the string_to_sign using the signing key
signature = HMAC.new(signing_key, (string_to_sign).Encode("utf-8"), Sha256()).HexDigest
```

The function `HMAC(key, data)` represents an HMAC-SHA256 function that
returns results in binary format. 5. Add signing information to the request and create the request URL.

After you calculate the signature, add it to the query string. For more information, see
[Add
the Signature to the Request](../../../general/latest/gr/sigv4-add-signature-to-request.md "../../../general/latest/gr/sigv4-add-signature-to-request.md").

First, add the authentication information to the query string.

```
canonical_querystring += "&X-Amz-Signature=" + signature
```

Second, create the URL for the request.

```
request_url = endpoint + canonical_uri + "?" + canonical_querystring
```

Use the request URL with your WebSocket library to make the request to
Amazon Transcribe. 6. The request to Amazon Transcribe must include the following headers. Typically these headers
are managed by your WebSocket client library.

```
Host: transcribestreaming.`us-west-2`.amazonaws.com:8443
Connection: Upgrade
Upgrade: websocket
Origin: `URI-of-WebSocket-client`
Sec-WebSocket-Version: `13`
Sec-WebSocket-Key: `randomly-generated-string`
```

7. When Amazon Transcribe receives your WebSocket request, it responds with a WebSocket
   upgrade response. Typically your WebSocket library manages this response and sets up
   a socket for communications with Amazon Transcribe.

The following is the response from Amazon Transcribe. Line breaks have been added for
readability.

```
HTTP/1.1 101 WebSocket Protocol Handshake

Connection: upgrade
Upgrade: websocket
websocket-origin: wss://transcribestreaming.us-west-2.amazonaws.com:8443
websocket-location: transcribestreaming.us-west-2.amazonaws.com:8443/stream-transcription-websocket?
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE%2F20220208%2Fus-west-2%2Ftranscribe%2Faws4_request
&X-Amz-Date=20220208T235959Z
&X-Amz-Expires=300
&X-Amz-Signature=`Signature Version 4 signature`
&X-Amz-SignedHeaders=host
&language-code=en-US
&session-id=`String`
&media-encoding=flac
&sample-rate=16000
x-amzn-RequestId: `RequestId`
Strict-Transport-Security: max-age=`31536000`
sec-websocket-accept: `hash-of-the-`Sec-WebSocket-Key`-header`
```

8. Make your WebSocket streaming request.

After the WebSocket connection is established, the client can start sending a sequence of
audio frames, each encoded using [event stream
encoding](#streaming-event-stream "#streaming-event-stream").

Each data frame contains three headers combined with a chunk of raw audio bytes; the
following table describes these headers.

| Header name byte length | Header name (string) | Header value type | Value string byte length | Value string (UTF-8)     |
| ----------------------- | -------------------- | ----------------- | ------------------------ | ------------------------ |
| 13                      | :content-type        | 7                 | 24                       | application/octet-stream |
| 11                      | :event-type          | 7                 | 10                       | AudioEvent               |
| 13                      | :message-type        | 7                 | 5                        | event                    |

9. To end the data stream, send an empty audio chunk in an event stream encoded
   message.

The response contains event stream encoded raw bytes in the payload. It contains the
standard prelude and the following headers.

| Header name byte length | Header name (string) | Header value type | Value string byte length | Value string (UTF-8) |
| ----------------------- | -------------------- | ----------------- | ------------------------ | -------------------- |
| 13                      | :content-type        | 7                 | 16                       | application/json     |
| 11                      | :event-type          | 7                 | 15                       | TranscriptEvent      |
| 13                      | :message-type        | 7                 | 5                        | event                |

When you decode the binary response, you end up with a JSON structure containing the
transcription results.

### Handling WebSocket streaming errors

If an exception occurs while processing your request, Amazon Transcribe responds with a terminal
WebSocket frame containing an event stream encoded response. This response contains the headers
described in the following table; the body of the response contains a descriptive error message. After
sending the exception response, Amazon Transcribe sends a close frame.

| Header name byte length | Header name (string) | Header value type | Value string byte length | Value string (UTF-8) |
| ----------------------- | -------------------- | ----------------- | ------------------------ | -------------------- |
| 13                      | :content-type        | 7                 | 16                       | application/json     |
| 15                      | :exception-type      | 7                 | varies                   | varies, see below    |
| 13                      | :message-type        | 7                 | 9                        | exception            |

The `exception-type` header contains one of the following values:

- `**BadRequestException**`: There was a client error
  when the stream was created, or an error occurred while streaming data. Make
  sure that your client is ready to accept data and try your request again.
- `**InternalFailureException**`: Amazon Transcribe had a
  problem during the handshake with the client. Try your request again.
- `**LimitExceededException**`: The client exceeded the
  concurrent stream limit. For more information, see [Amazon Transcribe Limits](../../../general/latest/gr/aws_service_limits.md#limits-amazon-transcribe "../../../general/latest/gr/aws_service_limits.md#limits-amazon-transcribe"). Reduce the number of streams that
  you're transcribing.
- `**UnrecognizedClientException**`: The WebSocket upgrade
  request was signed with an incorrect access key or secret key. Make sure you're correctly
  creating the access key and try your request again.

Amazon Transcribe can also return any of the common service errors. For a list, see
[Common
Errors](../APIReference/CommonErrors.md "../APIReference/CommonErrors.md").

## Event stream encoding

Amazon Transcribe uses a format called event stream encoding for streaming
transcriptions.

Event stream encoding provides bidirectional communication between a client and a server.
Data frames sent to the Amazon Transcribe streaming service are encoded in this format. The
response from Amazon Transcribe also uses this encoding.

Each message consists of two sections: the prelude and the data. The prelude consists
of:

1. The total byte length of the message
2. The combined byte length of all headers

The data section consists of:

1. Headers
2. Payload

Each section ends with a 4-byte big-endian integer cyclic redundancy check (CRC)
checksum. The message CRC checksum is for both the prelude section and the data section.
Amazon Transcribe uses CRC32 (often referred to as GZIP CRC32) to calculate both CRCs. For more
information about CRC32, see
[_GZIP file format specification
version 4.3_](https://www.ietf.org/rfc/rfc1952.txt "https://www.ietf.org/rfc/rfc1952.txt").

Total message overhead, including the prelude and both checksums, is 16 bytes.

The following diagram shows the components that make up a message and a header. There
are multiple headers per message.

![A schematic of the components of a message and a header for a streaming transcription.](images/frame-diagram-frame-overview.png)

Each message contains the following components:

- **Prelude**: Consists of two, 4-byte fields, for a fixed total of 8
  bytes.
  - _First 4 bytes_: The big-endian integer byte-length of the
    entire message, inclusive of this 4-byte length field.
  - _Second 4 bytes_: The big-endian integer byte-length of
    the 'headers' portion of the message, excluding the 'headers' length field
    itself.

- **Prelude CRC**: The 4-byte CRC checksum for the prelude portion
  of the message, excluding the CRC itself. The prelude has a separate CRC from
  the message CRC. That ensures that Amazon Transcribe can detect corrupted
  byte-length information immediately without causing errors, such as buffer
  overruns.
- **Headers**: Metadata annotating the message; for example,
  message type and content type. Messages have multiple headers, which are key:value
  pairs, where the key is a UTF-8 string. Headers can appear in any order in the 'headers'
  portion of the message, and each header can appear only once.
- **Payload**: The audio content to be transcribed.
- **Message CRC**: The 4-byte CRC checksum from the start of the
  message to the start of the checksum. That is, everything in the message except the
  CRC itself.

The header frame is the authorization frame for the streaming transcription. Amazon Transcribe uses the authorization header's value as the seed for generating a chain
of authorization headers for the data frames in the request.

Each header contains the following components; there are multiple headers per frame.

- **Header name byte-length**: The byte-length of the header
  name.
- **Header name**: The name of the header that indicates the header
  type. For valid values, see the following frame descriptions.
- **Header value type**: A number indicating the header value. The
  following list shows the possible values for the header and what they indicate.
  - `0` – TRUE
  - `1` – FALSE
  - `2` – BYTE
  - `3` – SHORT
  - `4` – INTEGER
  - `5` – LONG
  - `6` – BYTE ARRAY
  - `7` – STRING
  - `8` – TIMESTAMP
  - `9` – UUID

- **Value string byte length**: The byte length of the header value
  string.
- **Header value**: The value of the header string. Valid values for
  this field depend on the type of header. See [Setting up an HTTP/2 stream](#streaming-http2 "#streaming-http2") or
  [Setting up a WebSocket stream](#streaming-websocket "#streaming-websocket") for more information.

## Data frames

Each streaming request contains one or more data frames. There are two steps to creating
a data frame:

1. Combine raw audio data with metadata to create the payload of your request.
2. Combine the payload with a signature to form the event message that is sent to
   Amazon Transcribe.

The following diagram shows how this works.

![The components of a data frame for a streaming transcription.](images/streaming10.png)
