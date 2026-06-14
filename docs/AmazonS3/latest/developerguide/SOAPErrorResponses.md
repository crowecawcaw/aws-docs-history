# SOAP Error Responses

###### Note

SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on August 31, 2025. We recommend that you use either the REST API or the AWS SDKs.

In SOAP, an error result is returned to the client as a SOAP fault, with the HTTP
response code 500. If you do not receive a SOAP fault, then your request was successful.
The Amazon S3 SOAP fault code is comprised of a standard SOAP 1.1 fault code (either
"Server" or "Client") concatenated with the Amazon S3-specific error code. For example:
"Server.InternalError" or "Client.NoSuchBucket". The SOAP fault string element contains
a generic, human readable error message in English. Finally, the SOAP fault detail
element contains miscellaneous information relevant to the error.

For example, if you attempt to delete the object "Fred", which does not exist, the
body of the SOAP response contains a "NoSuchKey" SOAP fault.

The following example shows a sample SOAP error response.

```
<soapenv:Body>
  <soapenv:Fault>
    <Faultcode>soapenv:Client.NoSuchKey</Faultcode>
    <Faultstring>The specified key does not exist.</Faultstring>
    <Detail>
      <Key>Fred</Key>
    </Detail>
  </soapenv:Fault>
  </soapenv:Body>
```

The following table explains the SOAP error response elements

| Name          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Detail`      | Container for the key involved in the error<br>Type: Container<br>Ancestor: Body.Fault                                                                                                                                                                                                                                                                                                                                                                                  |
| `Fault`       | Container for error information.<br>Type: Container<br>Ancestor: Body                                                                                                                                                                                                                                                                                                                                                                                                   |
| `Faultcode`   | The fault code is a string that uniquely identifies an error<br>condition. It is meant to be read and understood by programs that<br>detect and handle errors by type. For more information, see [List of Error Codes](ErrorResponses.md#ErrorCodeList "ErrorResponses.md#ErrorCodeList").<br>Type: String<br>Ancestor: Body.Fault                                                                                                                                      |
| `Faultstring` | The fault string contains a generic description of the error<br>condition in English. It is intended for a human audience. Simple<br>programs display the message directly to the end user if they<br>encounter an error condition they don't know how or don't care to<br>handle. Sophisticated programs with more exhaustive error handling<br>and proper internationalization are more likely to ignore the fault<br>string.<br>Type: String<br>Ancestor: Body.Fault |
| `Key`         | Identifies the key involved in the error<br>Type: String<br>Ancestor: Body.Fault                                                                                                                                                                                                                                                                                                                                                                                        |
