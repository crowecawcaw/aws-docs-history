

# Customer APIs
<a name="customer_apis"></a>

The APIs in this topic are for use by customers. The sections that follow provide sample requests and sample responses for each of the APIs.
+  [ActivateEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ActivateEventSource.html) 
+  [CreateEventBus](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateEventBus.html) 
+  [DeleteEventBus](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteEventBus.html) 
+  [DescribeEventSource](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeEventSource.html) 
+  [ListEventBuses](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListEventBuses.html) 
+  [ListEventSources](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListEventSources.html) 
+  [PutRule](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutRule.html) 

## ActivateEventSource
<a name="_activateeventsource"></a>

### Sample request
<a name="ActivateEventSource_SampleRequest"></a>

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
<a name="ActivateEventSource_SampleResponse"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## CreateEventBus
<a name="_createeventbus"></a>

### Sample request
<a name="CreateEventBus_SampleRequest"></a>

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
<a name="CreateEventBus_SampleResponse"></a>

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
<a name="_deleteeventbus"></a>

### Sample request
<a name="DeleteEventBus_SampleRequest"></a>

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
<a name="DeleteEventBus_SampleResponse"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## DescribeEventSource
<a name="_describeeventsource"></a>

### Sample request
<a name="DescribeEventSource_RequestSample"></a>

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
<a name="DescribeEventSource_ResponseSample"></a>

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
<a name="_listeventbuses"></a>

### Sample request
<a name="ListEventBuses_RequestSample"></a>

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
<a name="ListEventBuses_ResponseSample"></a>

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
<a name="_listeventsources"></a>

### Sample request
<a name="ListEventSources_RequestSample"></a>

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
<a name="ListEventSources_ResponseSample"></a>

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
<a name="_putrule"></a>

### Sample request
<a name="PutRule_RequestSample"></a>

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
<a name="PutRule_ResponseSample"></a>

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