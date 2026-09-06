

# Partner APIs
<a name="partner_apis"></a>

The following APIs can only be called by AWS accounts associated with registered partners. The sections that follow provide sample requests and sample responses for each of the APIs.
+  [CreatePartnerEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreatePartnerEventSource.html) 
+  [DeletePartnerEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeletePartnerEventSource.html) 
+  [DescribePartnerEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribePartnerEventSource.html) 
+  [ListPartnerEventSources](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListPartnerEventSources.html) 
+  [ListPartnerEventSourceAccounts](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListPartnerEventSourceAccounts.html) 
+  [PutPartnerEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPartnerEvents.html) 

## CreatePartnerEventSource
<a name="_createpartnereventsource"></a>

### Sample request
<a name="CreatePartnerEventSource_SampleRequest"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>,
SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,
Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.CreatePartnerEventSource

{
  "Account": "000000000101",
  "Name": "aws.partner/partner_x/acct1/channel1"
}
```

### Sample response
<a name="CreatePartnerEventSource_SampleResponse"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>

{
 
  "EventSourceArn": "arn:aws:events:us-east-2::event-source/aws.partner/partner_x/acct1/channel1"
}
```

## DeletePartnerEventSource
<a name="_deletepartnereventsource"></a>

### Sample request
<a name="DeletePartnerEventSource_SampleRequest"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>,
SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,
Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.DeletePartnerEventSource

{
  "Account": "000000000101",
  "Name": "aws.partner/partner_x/acct1/channel1"
}
```

### Sample response
<a name="DeletePartnerEventSource_SampleResponse"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## DescribePartnerEventSource
<a name="_describepartnereventsource"></a>

### Sample request
<a name="DescribePartnerEventSource_SampleRequest"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>,
SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,
Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.DescribePartnerEventSource

{
  "Name": "aws.partner/partner_x/acct1/channel1"
}
```

### Sample response
<a name="DescribePartnerEventSource_SampleResponse"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>

{
 
  "Arn": "arn:aws:events:us-east-2::event-source/aws.partner/partner_x/acct1/channel1",
  "Name": "aws.partner/partner_x/acct1/channel1"
}
```

## ListPartnerEventSources
<a name="_listpartnereventsources"></a>

### Sample request
<a name="ListPartnerEventSources_SampleRequest"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>,
SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,
Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.ListPartnerEventSources

{
  "NamePrefix": "aws.partner/partner_x/acct1/"
}
```

### Sample response
<a name="ListPartnerEventSources_SampleResponse"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>

{
  "PartnerEventSources": [
    {
     
      "Arn": "arn:aws:events:us-east-2::event-source/aws.partner/partner_x/acct1/channel1",
      "Name": "aws.partner/partner_x/acct1/channel1"
    },
    {
      "Arn": "arn:aws:events:us-east-2::event-source/aws.partner/partner_x/acct1/channel2",
      "Name": "aws.partner/partner_x/acct1/channel2"
    },
    {
      "Arn": "arn:aws:events:us-east-2::event-source/aws.partner/partner_x/acct1/channel3",
      "Name": "aws.partner/partner_x/acct1/channel3"
    }
  ]
}
```

## ListPartnerEventSourceAccounts
<a name="_listpartnereventsourceaccounts"></a>

### Sample request
<a name="ListPartnerEventSourceAccounts_SampleRequest"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>,
SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,
Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.ListPartnerEventSourceAccounts

{
  "EventSourceName": "aws.partner/partner_x/acct1/channel1"
}
```

### Sample response
<a name="ListPartnerEventSourceAccounts_SampleResponse"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>

{
  "PartnerEventSourceAccounts": [
    {
      "Account": "000000000101",
      "CreationTime": "2018-11-20T22:03:15",
      "State": "PENDING"
    }
  ]
}
```

## PutPartnerEvents
<a name="_putpartnerevents"></a>

### Sample request
<a name="PutPartnerEvents_SampleRequest"></a>

```
POST / HTTP/1.1
Host: events.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>,
SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,
Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSEvents.PutPartnerEvents

{
"Entries": [
  {
      "Source": "aws.partner/partner_x/acct1/channel1",
      "Detail": "{ \"key1\": \"value1\", \"key2\": \"value2\" }",
      "Resources": [
        "resource1",
        "resource2"
      ],
      "DetailType": "myDetailType",
    },
    {
      "Source": "aws.partner/partner_x/acct2/channel1",
      "Detail": "{ \"key1\": \"value3\", \"key2\": \"value4\" }",
      "Resources": [
        "resource1",
        "resource2"
      ],
      "DetailType": "myDetailType"
    }
  ]
}
```

### Sample response
<a name="PutPartnerEvents_SampleResponse"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>

{
 "FailedEntryCount": 0,
 "Entries": [
   {
     "EventId": "11710aed-b79e-4468-a20b-bb3c0c3b4860"
   },
   {
     "EventId": "d804d26a-88db-4b66-9eaf-9a11c708ae82"
   }
 ]
}
```