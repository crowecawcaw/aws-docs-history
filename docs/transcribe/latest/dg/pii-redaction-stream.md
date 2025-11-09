# Redacting or identifying PII in a real-time stream

When redacting personally identifiable information (PII) from a streaming transcription,
Amazon Transcribe replaces each identified instance of PII with `[PII]` in your
transcript.

An additional option available for streaming transcriptions is _PII
identification_. When you activate PII Identification, Amazon Transcribe labels the PII
in your transcription results under an `Entities` object. For an output sample, see
[Example redacted streaming output](pii-redaction-output.md#pii-redaction-output-stream "pii-redaction-output.md#pii-redaction-output-stream")
and [Example PII identification output](pii-redaction-output.md#pii-redaction-output-id "pii-redaction-output.md#pii-redaction-output-id").

Redaction and identification of PII with streaming transcriptions is available with these English dialects: Scottish (`en-AB`), Australia (`en-AU`), Canada (`en-CA`), British (`en-GB`), Ireland (`en-IE`), India (`en-IN`), New Zealand (`en-NZ`), United States (`en-US`), Wales (`en-WL`), and South Africa (`en-ZA`); Spanish dialects: US (`es-US`), Spain (`es-ES`); French dialects: French (`fr-FR`), Canada (`fr-CA`); Portuguese dialects: Portugal (`pt-PT`), Brazil (`pt-BR`); Italian dialect: Italy (`it-IT`); and German dialects: Germany (`de-DE`), Swiss (`de-CH`).

PII identification and redaction for streaming jobs is performed only upon complete
transcription of the audio segments.

Types of PII Amazon Transcribe can recognize for streaming
transcriptions| PII type | Description |
| --- | --- |
| `ADDRESS` | A physical address, such as *100 Main Street, Anytown, USA<br>• or<br>*Suite #12, Building 123*. An address can include a street, building, location, city,<br>state, country, county, zip, precinct, neighborhood, and more. |
| `ALL` | Redact or identify all PII types listed in this table. |
| `BANK_ACCOUNT_NUMBER` | A US bank account number. These are typically between 10<br>• 12 digits long, but<br>Amazon Transcribe also recognizes bank account numbers when only the last 4 digits are<br>present. |
| `BANK_ROUTING` | A US bank account routing number. These are typically 9 digits long, but<br>Amazon Transcribe also recognizes routing numbers when only the last 4 digits are<br>present. |
| `CREDIT_DEBIT_CVV` | A 3-digit card verification code (CVV) that is present on VISA, MasterCard, and<br>Discover credit and debit cards. In American Express credit or debit cards, it is a 4-digit numeric<br>code. |
| `CREDIT_DEBIT_EXPIRY` | The expiration date for a credit or debit card. This number is usually 4 digits long and<br>formatted as month/year or MM/YY. For example, Amazon Transcribe can recognize expiration<br>dates such as *01/21*, *01/2021*, and<br>*Jan 2021*. |
| `CREDIT_DEBIT_NUMBER` | The number for a credit or debit card. These numbers can vary from 13 to 16 digits in<br>length, but Amazon Transcribe also recognizes credit or debit card numbers when only the last 4<br>digits are present. |
| `EMAIL` | An email address, such as *efua.owusu@email.com*. |
| `NAME` | An individual's name. This entity type does not include titles, such as Mr., Mrs., Miss,<br>or Dr. Amazon Transcribe does not apply this entity type to names that are part of organizations<br>or addresses. For example, Amazon Transcribe recognizes the *John Doe<br>Organization<br>• as an organization, and \*Jane Doe Street<br>• as an<br>address. |
| `PHONE` | A phone number. This entity type also includes fax and pager numbers. |
| `PIN` | A 4-digit personal identification number (PIN) that allows someone to access their<br>bank account information. |
| `SSN` | A Social Security Number (SSN) is a 9-digit number that is issued to US citizens,<br>permanent residents, and temporary working residents. Amazon Transcribe also recognizes Social<br>Security Numbers when only the last 4 digits are present. |
| `AGE` | An individual's age, including the quantity and unit of time. For example, in the phrase "I am 40 years old," Amazon Transcribe recognizes "40 years" as an age. |
| `DATE_TIME` | A date can include a year, month, day, day of week, or time of day. For example, Amazon Transcribe recognizes "January 19, 2020" or "11 am" as dates. Amazon Transcribe will recognize partial dates, date ranges, and date intervals. It will also recognize decades, such as "the 1990s". |
| `LICENSE_PLATE` | A license plate for a vehicle is issued by the state or country where the vehicle is registered. The format for passenger vehicles is typically five to eight digits, consisting of upper-case letters and numbers. The format varies depending on the location of the issuing state or country. |
| `PASSPORT_NUMBER` | A unique identifier assigned to an individual's passport. The format typically includes a combination of letters and numbers and varies by country. |
| `PASSWORD` | An alphanumeric string that is used as a password, such as "\*very20special#pass\*". |
| `USERNAME` | A user name that identifies an account, such as a login name, screen name, nick name, or handle. |
| `VEHICLE_IDENTIFICATION_NUMBER` | A Vehicle Identification Number (VIN) uniquely identifies a vehicle. VIN content and format are defined in the ISO 3779 specification. Each country has specific codes and formats for VINs. |

You can start a streaming transcription using the AWS Management Console, WebSocket, or
HTTP/2.

1. Sign into the [AWS Management Console](https://console.aws.amazon.com/transcribe/ "https://console.aws.amazon.com/transcribe/").
2. In the navigation pane, choose **Real-time transcription**. Scroll down to
   **Content removal settings** and expand this field if it is minimized.

![Amazon Transcribe console screenshot: the 'real-time transcription' page.](images/redaction-stream1.png) 3. Toggle on **PII Identification & redaction**.

![Amazon Transcribe console screenshot: the expanded 'content removal settings' panel.](images/redaction-stream2.png) 4. Select **Identification only** or **Identification &
redaction**, then select the PII entity types you want to identify or redact in your
transcript.

![Amazon Transcribe console screenshot: list of PII types that can be selected.](images/redaction-stream3.png) 5. You're now ready to transcribe your stream. Select **Start streaming**
and begin speaking. To end your dictation, select **Stop streaming**.
This example creates a presigned URL that uses PII redaction (or PII identification)
in a WebSocket stream. Line breaks have been added for readability. For more information
on using WebSocket streams with Amazon Transcribe, see
[Setting up a WebSocket stream](streaming-setting-up.md#streaming-websocket "streaming-setting-up.md#streaming-websocket").
For more detail on parameters, see
[`StartStreamTranscription`](../APIReference/API_streaming_StartStreamTranscription.md "../APIReference/API_streaming_StartStreamTranscription.md").

```
GET wss://transcribestreaming.`us-west-2`.amazonaws.com:8443/stream-transcription-websocket?
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=`AKIAIOSFODNN7EXAMPLE`%2F`20220208`%2F`us-west-2`%2F`transcribe`%2Faws4_request
&X-Amz-Date=`20220208`T`235959`Z
&X-Amz-Expires=`300`
&X-Amz-Security-Token=`security-token`
&X-Amz-Signature=`string`
&X-Amz-SignedHeaders=content-type%3Bhost%3Bx-amz-date
&language-code=`en-US`
&media-encoding=`flac`
&sample-rate=`16000`
&pii-entity-types=`NAME`,`ADDRESS`
&content-redaction-type=PII (or &content-identification-type=PII)
```

You cannot use both `content-identification-type` and
`content-redaction-type` in the same request.

Parameter definitions can be found in the [API Reference](../APIReference/API_Reference.md "../APIReference/API_Reference.md"); parameters common to
all AWS API operations are listed in the [Common Parameters](../APIReference/CommonParameters.md "../APIReference/CommonParameters.md")
section.

This example creates an HTTP/2 request with PII identification or PII redaction enabled.
For more information on using HTTP/2 streaming with Amazon Transcribe, see
[Setting up an HTTP/2 stream](streaming-setting-up.md#streaming-http2 "streaming-setting-up.md#streaming-http2"). For
more detail on parameters and headers specific to Amazon Transcribe, see
[`StartStreamTranscription`](../APIReference/API_streaming_StartStreamTranscription.md "../APIReference/API_streaming_StartStreamTranscription.md").

```
POST /stream-transcription HTTP/2
host: transcribestreaming.`us-west-2`.amazonaws.com
X-Amz-Target: com.amazonaws.transcribe.Transcribe.`StartStreamTranscription`
Content-Type: application/vnd.amazon.eventstream
X-Amz-Content-Sha256: `string`
X-Amz-Date: `20220208`T`235959`Z
Authorization: AWS4-HMAC-SHA256 Credential=`access-key`/`20220208`/`us-west-2`/transcribe/aws4_request, SignedHeaders=content-type;host;x-amz-content-sha256;x-amz-date;x-amz-target;x-amz-security-token, Signature=`string`
x-amzn-transcribe-language-code: `en-US`
x-amzn-transcribe-media-encoding: `flac`
x-amzn-transcribe-sample-rate: `16000`
x-amzn-transcribe-content-identification-type: PII (or x-amzn-transcribe-content-redaction-type: PII)
x-amzn-transcribe-pii-entity-types: ``NAME`,`ADDRESS``
transfer-encoding: chunked
```

You cannot use both `content-identification-type` and
`content-redaction-type` in the same request.

Parameter definitions can be found in the [API Reference](../APIReference/API_Reference.md "../APIReference/API_Reference.md"); parameters common to
all AWS API operations are listed in the [Common Parameters](../APIReference/CommonParameters.md "../APIReference/CommonParameters.md")
section.

###### Note

PII redaction for streaming is only supported in these AWS Regions: Asia Pacific (Seoul),
Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), EU (Frankfurt), EU (Ireland), EU
(London), US East (N. Virginia), US East (Ohio), and US West (Oregon).
