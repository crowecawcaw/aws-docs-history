

# AWS Transfer Family events
<a name="events-ref-transfer"></a>

Transfer Family sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Transfer Family service events
<a name="events-ref-transfer-events"></a>

Transfer Family sends the following events directly to EventBridge: 
+ AS2 MDN Receive Completed
+ AS2 MDN Receive Failed
+ AS2 MDN Send Completed
+ AS2 MDN Send Failed
+ AS2 Payload Receive Completed
+ AS2 Payload Receive Failed
+ AS2 Payload Send Completed
+ AS2 Payload Send Failed
+ FTP Server Directory Create Completed
+ FTP Server Directory Create Failed
+ FTP Server Directory Delete Completed
+ FTP Server Directory Delete Failed
+ FTP Server File Delete Completed
+ FTP Server File Delete Failed
+ FTP Server File Download Completed
+ FTP Server File Download Failed
+ FTP Server File Rename Completed
+ FTP Server File Rename Failed
+ FTP Server File Upload Completed
+ FTP Server File Upload Failed
+ FTPS Server Directory Create Completed
+ FTPS Server Directory Create Failed
+ FTPS Server Directory Delete Completed
+ FTPS Server Directory Delete Failed
+ FTPS Server File Delete Completed
+ FTPS Server File Delete Failed
+ FTPS Server File Download Completed
+ FTPS Server File Download Failed
+ FTPS Server File Rename Completed
+ FTPS Server File Rename Failed
+ FTPS Server File Upload Completed
+ FTPS Server File Upload Failed
+ SFTP Server Directory Create Completed
+ SFTP Server Directory Create Failed
+ SFTP Server Directory Delete Completed
+ SFTP Server Directory Delete Failed
+ SFTP Server File Delete Completed
+ SFTP Server File Delete Failed
+ SFTP Server File Download Completed
+ SFTP Server File Download Failed
+ SFTP Server File Rename Completed
+ SFTP Server File Rename Failed
+ SFTP Server File Upload Completed
+ SFTP Server File Upload Failed
+ SFTP Connector File Send Completed
+ SFTP Connector File Send Failed
+ SFTP Connector File Retrieve Completed
+ SFTP Connector File Retrieve Failed
+ SFTP Connector Directory Listing Completed
+ SFTP Connector Directory Listing Failed
+ SFTP Connector Remote Move Completed
+ SFTP Connector Remote Move Failed
+ SFTP Connector Remote Delete Completed
+ SFTP Connector Remote Delete Failed

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.transfer

```
{
  "source": ["aws.transfer"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.transfer"],
  "detail-type": ["{{AS2 MDN Receive Completed}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Transfer Family events delivered via AWS CloudTrail
<a name="event-ref-transfer-events-via-CT"></a>

AWS CloudTrail sends events originating from Transfer Family to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.transfer
+ `eventSource`: transfer.amazonaws.com

```
{
  "source": ["aws.transfer"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["transfer.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.transfer"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["transfer.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```