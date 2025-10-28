# Partner APIs

The following APIs can only be called by AWS accounts associated with registered partners. The sections that follow provide sample requests and sample responses for each of the APIs.

- [CreatePartnerEventSource](../APIReference/API_CreatePartnerEventSource.md "../APIReference/API_CreatePartnerEventSource.md")
- [DeletePartnerEventSource](../APIReference/API_DeletePartnerEventSource.md "../APIReference/API_DeletePartnerEventSource.md")
- [DescribePartnerEventSource](../APIReference/API_DescribePartnerEventSource.md "../APIReference/API_DescribePartnerEventSource.md")
- [ListPartnerEventSources](../APIReference/API_ListPartnerEventSources.md "../APIReference/API_ListPartnerEventSources.md")
- [ListPartnerEventSourceAccounts](../APIReference/API_ListPartnerEventSourceAccounts.md "../APIReference/API_ListPartnerEventSourceAccounts.md")
- [PutPartnerEvents](../APIReference/API_PutPartnerEvents.md "../APIReference/API_PutPartnerEvents.md")

## CreatePartnerEventSource

### Sample request

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

### Sample request

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

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## DescribePartnerEventSource

### Sample request

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

### Sample request

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

### Sample request

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

### Sample request

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
