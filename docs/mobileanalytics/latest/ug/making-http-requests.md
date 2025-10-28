# Making HTTP Requests to Mobile Analytics

###### Note

Amazon Mobile Analytics was discontinued on April 30, 2018. The features that were
previously provided by Mobile Analytics are now provided by Amazon Pinpoint. If you're new to
Mobile Analytics, you should use Amazon Pinpoint instead. If you currently use Mobile Analytics, see
[Migrating from Amazon Mobile Analytics to Amazon Pinpoint](migrate.md "migrate.md").

If you don't use the [AWS Mobile SDK](https://aws.amazon.com/mobile/sdk "https://aws.amazon.com/mobile/sdk"), you can perform Mobile Analytics operations
over HTTP using the POST request method. The POST method requires you to specify the
operation in the header of the request and provide the data for the operation in JSON
format in the body of the request.

## HTTP Header Contents

Mobile Analytics requires the following information in the header of an HTTP request:

**Host**

The Mobile Analytics endpoint. This value must be
`https://mobileanalytics.us-east-1.amazonaws.com`

**X-Amz-Date**

The date. Must be specified in ISO 8601 standard format, in UTC time.
For example:

`20130315T092054Z`

**Authorization**

The set of authorization parameters that AWS uses to ensure the
validity and authenticity of the request. For more information, see
[Signature Version 4 Signing Process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md").

**User Agent**

Information about the user agent originating the request.

**X-Amz-Client-Context**

Information about the client interacting with Mobile Analytics. Data in a client
context describes the app and the environment in which it runs. For
details about the contents of the client context, see [PutEvents](PutEvents.md#putEvents-request-client-context-header "PutEvents.md#putEvents-request-client-context-header").

**X-Amz-Security-Token**

If you sign your request using temporary security credentials, you
must include the corresponding security token in your request by adding
the `X-Amz-Security-Token` header.

For information on signing requests using temporary security
credentials in your REST API requests, see [Signing and Authenticating
REST Requests](../../../AmazonS3/latest/userguide/RESTAuthentication.md "../../../AmazonS3/latest/userguide/RESTAuthentication.md").

**Content-Type**

Specifies JSON and the version. For example, `Content-Type:
 application/json`

**Content-Length**

The payload size in bytes.

### HTTP Header Example

The following is an example header for an HTTP request for Mobile Analytics.

```
POST /2014-06-05/events HTTP/1.1
Host: mobileanalytics.us-east-1.amazonaws.com
X-Amz-Date: `<Date>`
Authorization: AWS4-HMAC-SHA256 Credential=`<access_key>`/20140709/us-east-1/mobileanalytics/aws4_request, SignedHeaders=content-length;content-type;host;user-agent;x-amz-client-context;x-amz-date;x-amz-security-token;x-amz-target, Signature=`<signature>`
User-Agent: `<User agent string>`
x-amz-Client-Context: {"client":{"client_id":"`<client_id>`","app_title":"`<app_title>`","app_version_name":"`<app_version_name>`","app_version_code":"`<app_version_code>`","app_package_name":"`<app_package_name>`"},"custom":{},"env":{"platform":"`<platform>`","model":"`<model>`","make":"`<make>`","platform_version":"`<platform_version>`","locale":"`<locale>`”}}
x-amz-security-token: `<Security token>`
Content-Type: application/json
Content-Length: `<Payload size bytes>`
Connection: Keep-Alive
```

## HTTP Body Content

The body of an HTTP request contains the data for the operation specified in the
header of the HTTP request. The data must be formatted according to the JSON data
schema for Mobile Analytics. For the PutEvents operation, the body content of the HTTP request
consists of an array of one or more events.

### HTTP Body Example

The following is an example of the body for an HTTP request for Mobile Analytics.

```
{
  "events": [
    {
      "eventType": "`<Event type>`",
      "timestamp": "`<ISO 8601 date>`",
      "session": {
                  "id": "`<Session id>`",
                  "startTimestamp": "`<ISO 8601 date>`"
      },
      "attributes": {
                     "`<Optional string name>`": "`<Optional string value>`",
                     ...
                     "`<Optional string name>`": "`<Optional string value>`"
      },
      "metrics": {
                  "`<Optional string name>`": `<Optional numeric value>`,
                   ...
                  "`<Optional string name>`": `<Optional numeric value>`
      }
    },
    ...
  ]
}
```
