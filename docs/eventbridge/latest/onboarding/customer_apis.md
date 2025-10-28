# Customer APIs

The APIs in this topic are for use by customers. The sections that follow provide sample requests and sample responses for each of the APIs.

- [ActivateEventSource](../APIReference/API_ActivateEventSource.md "../APIReference/API_ActivateEventSource.md")
- [CreateEventBus](../APIReference/API_CreateEventBus.md "../APIReference/API_CreateEventBus.md")
- [DeleteEventBus](../APIReference/API_DeleteEventBus.md "../APIReference/API_DeleteEventBus.md")
- [DescribeEventSource](../APIReference/API_DescribeEventSource.md "../APIReference/API_DescribeEventSource.md")
- [ListEventBuses](../APIReference/API_ListEventBuses.md "../APIReference/API_ListEventBuses.md")
- [ListEventSources](../APIReference/API_ListEventSources.md "../APIReference/API_ListEventSources.md")
- [PutRule](../APIReference/API_PutRule.md "../APIReference/API_PutRule.md")

## ActivateEventSource

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
X-Amz-Target: AWSEvents.ActivateEventSource

{
 "Name": "partner_x/acct1/channel1"
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

## CreateEventBus

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
X-Amz-Target: AWSEvents.CreateEventBus

{
  "EventSourceName": "aws.partner/partner_x/acct1/channel1",
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
 
  "EventBusArn": "arn:aws:events:us-east-2:000000000101:event-bus/aws.partner/partner_x/acct1/channel1"
}
```

## DeleteEventBus

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
X-Amz-Target: AWSEvents.DeleteEventBus

{
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

## DescribeEventSource

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
X-Amz-Target: AWSEvents.DescribeEventSource

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
  "Arn": "arn:aws:events:us-east-2::event-source/partner_x/acct1/channel1",
  "CreationTime": "2018-11-20T22:03:15",
  "CreatedBy": "partner_x",
  "Name": "aws.partner/partner_x/acct1/channel1",
  "State": "ACTIVE"
}
```

## ListEventBuses

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
X-Amz-Target: AWSEvents.ListEventBuses

{
  "Limit": "3"
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
  "EventBuses": [
    {
 
    "Arn": "arn:aws:events:us-east-2:000000000101:event-bus/default",
      "Name": "default"
    },
    {
      "Arn": "arn:aws:events:us-east-2:000000000101:event-bus/my-bus",
      "Name": "my-bus"
    },
    {
 
    "Arn": "arn:aws:events:us-east-2:000000000101:event-bus/partner_x/acct1/channel1",
      "Name": "partner_x/acct1/channel1"
    },
    {
      "Arn": "arn:aws:events:us-east-2:000000000101:event-bus/partner_y/acct1/trigger1",
      "Name": "partner_y/acct1/trigger1"
    },
    {
     
      "Arn": "arn:aws:events:us-east-2:000000000101:event-bus/partner_z/acct1/repo1",
      "Name": "partner_z/acct1/repo1"
    }
  ],
  "NextToken": "AAAAAAAAAAAAAAA"
}
```

## ListEventSources

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
X-Amz-Target: AWSEvents.ListEventSources

{
  "Limit": "3"
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
  "EventSources": [
    {
 
    "Arn": "arn:aws:events:us-east-2::event-source/partner_x/acct1/channel1",
      "CreatedBy": "partner_x",
      "CreationTime": "2018-11-20T22:03:15",
      "Name": "aws.partner/partner_x/acct1/channel1",
      "State": "ACTIVE"
    },
    {
      "Arn": "arn:aws:events:us-east-2::event-source/partner_y/acct1/trigger1",
      "CreatedBy": "partner_y",
      "CreationTime": "2018-12-12T13:52:52",
      "Name": "partner_y/acct1/trigger1",
      "State": "DELETED"
    },
    {
     
      "Arn": "arn:aws:events:us-east-2::event-source/partner_z/acct1/repo1",
      "CreatedBy": "partner_z",
      "CreationTime": "2018-12-20T00:09:55",
      "ExpirationTime": "2019-01-03T00:09:55",
      "Name": "partner_z/acct1/repo1",
      "State": "PENDING"
    }
  ],
  "NextToken": "AAAAAAAAAAAAAAA"
}
```

## PutRule

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
X-Amz-Target: AWSEvents.PutRule

{
  "Name": "everything",
  "EventBusName": "aws.partner/partner_x/acct1/channel1", 
  "EventPattern": "{ \"account\": [\"000000000101\"] }"
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
 "RuleArn":
 "arn:aws:events:us-east-2:000000000101:rule/aws.partner/partner_x/acct1/channel1/everything"
}
```
