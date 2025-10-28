# Making HTTP Requests to Amazon SWF

If you don't use one of the AWS SDKs, you can perform Amazon Simple Workflow Service (Amazon SWF) operations over HTTP using the POST
request method. The POST method requires that you specify the operation in the header of the request and provide
the data for the operation in JSON format in the body of the request.

## HTTP Header Contents

Amazon SWF requires the following information in the header of an HTTP request:

- `host` The Amazon SWF endpoint.
- `x-amz-date` You must provide the time stamp in either the HTTP
  `Date` header or the AWS `x-amz-date
header` (some HTTP client libraries don't let you set the
  `Date` header). When an
  `x-amz-date` header is present, the system
  ignores any `Date` header when authenticating the
  request.

The date must be specified in one of the following three formats, as specified in the HTTP/1.1 RFC:

    + Sun, 06 Nov 1994 08:49:37 GMT (RFC 822, updated by RFC 1123)
    + Sunday, 06-Nov-94 08:49:37 GMT (RFC 850, obsoleted by RFC 1036)
    + Sun Nov 6 08:49:37 1994 (ANSI C's asctime() format)

- `x-amzn-authorization` The signed request parameters in
  the format:

```
AWS3 AWSAccessKeyId=####,Algorithm=HmacSHA256, [,SignedHeaders=Header1;Header2;...]
Signature=S(StringToSign)
```

`AWS3` – This is an AWS implementation-specific tag that denotes the authentication
version used to sign the request (currently, for Amazon SWF this value is always
`AWS3`).

`AWSAccessKeyId` – Your AWS Access Key ID.

`Algorithm` – The algorithm used to create the HMAC-SHA
value of the string-to-sign, such as `HmacSHA256` or
`HmacSHA1`.

`Signature` – Base64( Algorithm( StringToSign, SigningKey )
). For details see [Calculating the HMAC-SHA Signature for Amazon SWF](HMACAuth-swf.md "HMACAuth-swf.md")

`SignedHeaders` – (Optional) If present, must contain a list
of all the HTTP Headers used in the Canonicalized HttpHeaders calculation. A
single semicolon character (;) (ASCII character 59) must be used as the
delimiter for list values.

- `x-amz-target` – The destination service of the request and
  the operation for the data, in the format

`com.amazonaws.swf.service.model.SimpleWorkflowService. + `<action>``

For example, `com.amazonaws.swf.service.model.SimpleWorkflowService.RegisterDomain`

- `content-type` – The type needs to specify JSON and the character set,
  as `application/json; charset=UTF-8`

The following is an example header for an HTTP request to create a domain.

```
POST http://swf.us-east-1.amazonaws.com/ HTTP/1.1
Host: swf.us-east-1.amazonaws.com
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.25) Gecko/20111212 Firefox/3.6.25 ( .NET CLR 3.5.30729; .NET4.0E)
Accept: application/json, text/javascript, */*
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive
Content-Type: application/json; charset=UTF-8
X-Requested-With: XMLHttpRequest
X-Amz-Date: Fri, 13 Jan 2012 18:42:12 GMT
X-Amz-Target: com.amazonaws.swf.service.model.SimpleWorkflowService.RegisterDomain
Content-Encoding: amz-1.0
X-Amzn-Authorization: AWS3 AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE,Algorithm=HmacSHA256,SignedHeaders=Host;X-Amz-Date;X-Amz-Target;Content-Encoding,Signature=tzjkF55lxAxPhzp/BRGFYQRQRq6CqrM254dTDE/EncI=
Referer: http://swf.us-east-1.amazonaws.com/explorer/index.html
Content-Length: 91
Pragma: no-cache
Cache-Control: no-cache

{"name": "867530902",
 "description": "music",
 "workflowExecutionRetentionPeriodInDays": "60"}
```

Here is an example of the corresponding HTTP response.

```
HTTP/1.1 200 OK
Content-Length: 0
Content-Type: application/json
x-amzn-RequestId: 4ec4ac3f-3e16-11e1-9b11-7182192d0b57
```

## HTTP Body Content

The body of an HTTP request contains the data for the operation
specified in the header of the HTTP request. Use the JSON data
format to convey data values and data structure, simultaneously.
Elements can be nested within other elements using bracket
notation. For example, the following shows a request to list all
workflow executions that started between two specified points in
time—using Unix Time notation.

```
{
 "domain": "867530901",
 "startTimeFilter":
 {
   "oldestDate": 1325376070,
	 "latestDate": 1356998399
 },
 "tagFilter":
 {
   "tag": "music purchase"
 }
}
```

## Sample Amazon SWF JSON Request and Response

The following example shows a request to Amazon SWF for a description of the domain that we created previously.
Then it shows the Amazon SWF response.

### HTTP POST Request

```
POST http://swf.us-east-1.amazonaws.com/ HTTP/1.1
Host: swf.us-east-1.amazonaws.com
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.25) Gecko/20111212 Firefox/3.6.25 ( .NET CLR 3.5.30729; .NET4.0E)
Accept: application/json, text/javascript, */*
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive
Content-Type: application/json; charset=UTF-8
X-Requested-With: XMLHttpRequest
X-Amz-Date: Sun, 15 Jan 2012 03:13:33 GMT
X-Amz-Target: com.amazonaws.swf.service.model.SimpleWorkflowService.DescribeDomain
Content-Encoding: amz-1.0
X-Amzn-Authorization: AWS3 AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE,Algorithm=HmacSHA256,SignedHeaders=Host;X-Amz-Date;X-Amz-Target;Content-Encoding,Signature=IFJtq3M366CHqMlTpyqYqd9z0ChCoKDC5SCJBsLifu4=
Referer: http://swf.us-east-1.amazonaws.com/explorer/index.html
Content-Length: 21
Pragma: no-cache
Cache-Control: no-cache

{"name": "867530901"}
```

### Amazon SWF Response

```
HTTP/1.1 200 OK
Content-Length: 137
Content-Type: application/json
x-amzn-RequestId: e86a6779-3f26-11e1-9a27-0760db01a4a8

{"configuration":
  {"workflowExecutionRetentionPeriodInDays": "60"},
 "domainInfo":
  {"description": "music",
   "name": "867530901",
   "status": "REGISTERED"}
}
```

Notice the protocol (`HTTP/1.1`) is followed by a status code
(`200`). A code value of `200` indicates a successful operation.

Amazon SWF doesn't serialize null values. If your JSON parser is set to serialize null values for requests, Amazon SWF
ignores them.
