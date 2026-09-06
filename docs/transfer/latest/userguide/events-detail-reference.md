

# Transfer Family events detail reference
<a name="events-detail-reference"></a>

All events from AWS services have a common set of fields containing metadata about the event. These metadata can include the AWS service that is the source of the event, the time the event was generated, the account and Region in which the event took place, and others. For definitions of these general fields, see [Event structure reference](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events-structure.html) in the *Amazon EventBridge User Guide*. 

In addition, each event has a `detail` field that contains data specific to that particular event. The following reference defines the detail fields for the various Transfer Family events.

When you use EventBridge to select and manage Transfer Family events, consider the following:
+ The `source` field for all events from Transfer Family is set to `aws.transfer`.
+ The `detail-type` field specifies the event type. 

  For example, `FTP Server File Download Completed`.
+ The `detail` field contains the data that is specific to that particular event. 

For information on constructing event patterns that enable rules to match Transfer Family events, see [Event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) in the *Amazon EventBridge User Guide*.

For more information on events and how EventBridge processes them, see [Amazon EventBridge events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html) in the *Amazon EventBridge User Guide*.

**Topics**
+ [SFTP, FTPS, and FTP server events](#event-detail-server-events)
+ [SFTP connector events](#event-detail-sftp-connector-events)
+ [AS2 events](#event-detail-as2-server-events)

## SFTP, FTPS, and FTP server events
<a name="event-detail-server-events"></a>

The following are the detail fields for SFTP, FTPS, and FTP server events:
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

The `source` and `detail-type` fields are included below because they contain specific values for Transfer Family events. For definitions of the other metadata fields that are included in all events, see [Event structure reference](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events-structure.html) in the *Amazon EventBridge User Guide*.

```
{
  . . .,
  "detail-type": "string",
  "source": "aws.transfer",
  . . .,
  "detail": {
    "failure-code" : "string",
    "status-code" : "string",
    "protocol" : "string",
    "bytes" : "number",
    "client-ip" : "string",
    "failure-message" : "string",
    "end-timestamp" : "string",
    "etag" : "string",
    "file-path" : "string",
    "original-file-path" : "string",
    "renamed-file-path" : "string",
    "directory-path" : "string",
    "server-id" : "string",
    "username" : "string",
    "session-id" : "string",
    "start-timestamp" : "string"
  }
}
```

`detail-type`  <a name="event-detail-server-events-detail-type"></a>
Identifies the type of event.  
For this event, the value is one of the SFTP, FTPS, or FTP server event names listed previously.

`source`  <a name="event-detail-server-events-source"></a>
Identifies the service that generated the event. For Transfer Family events, this value is `aws.transfer`.

`detail`  <a name="sftp-server-detail"></a>
A JSON object that contains information about the event. The service generating the event determines the content of this field.  
For this event, the data includes the following:    
`failure-code`  <a name="sftp-server-failure-code"></a>
Category for why the transfer failed. Values: `PARTIAL_UPLOAD | PARTIAL_DOWNLOAD | UNKNOWN_ERROR`  
`status-code`  <a name="sftp-server-status-code"></a>
Whether the transfer is successful. Values: `COMPLETED | FAILED`.  
`protocol`  <a name="sftp-server-protocol"></a>
The protocol used for the transfer. Values: `SFTP | FTPS | FTP`  
`bytes`  <a name="sftp-server-bytes"></a>
The number of bytes transferred.  
`client-ip`  <a name="sftp-server-client-ip"></a>
The IP address for the client involved in the transfer  
`failure-message`  <a name="sftp-server-failure-message"></a>
For failed transfers, the details for why the transfer failed.  
`end-timestamp`  <a name="sftp-server-end-timestamp"></a>
For successful transfers, the timestamp for when the file finishes being processed.  
`etag`  <a name="sftp-server-etag"></a>
The entity tag (only used for Amazon S3 files).  
`file-path`  <a name="sftp-server-file-path"></a>
The path to the file being transferred, deleted, or otherwise operated on.  
`original-file-path`  <a name="sftp-server-original-file-path"></a>
For file rename events, the original path of the file before renaming.  
`renamed-file-path`  <a name="sftp-server-renamed-file-path"></a>
For file rename events, the new path of the file after renaming.  
`directory-path`  <a name="sftp-server-directory-path"></a>
For directory create and delete events, the path of the directory.  
`server-id`  <a name="sftp-server-server-id"></a>
The unique ID for the Transfer Family server.  
`username`  <a name="sftp-server-username"></a>
The user that is performing the transfer.  
`session-id`  <a name="sftp-server-session-id"></a>
The unique identifier for the transfer session.  
`start-timestamp`  <a name="sftp-server-start-timestamp"></a>
For successful transfers, the timestamp for when file processing begins.

**Example SFTP Server File Download Failed example event**  <a name="event-detail-server-events.example"></a>
The following example shows an event where a download failed on an SFTP server (Amazon EFS is the storage being used).  

```
{
    "version": "0",
    "id": "event-ID",
    "detail-type": "SFTP Server File Download Failed",
    "source": "aws.transfer",
    "account": "958412138249",
    "time": "2024-01-29T17:20:27Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:transfer:us-east-1:958412138249:server/s-1234abcd5678efghi"
    ],
    "detail": {
        "failure-code": "PARTIAL_DOWNLOAD",
        "status-code": "FAILED",
        "protocol": "SFTP",
        "bytes": 4100,
        "client-ip": "IP-address",
        "failure-message": "File was partially downloaded.",
        "end-timestamp": "2024-01-29T17:20:27.749749117Z",
        "file-path": "/fs-1234abcd5678efghi/user0/test-file",
        "server-id": "s-1234abcd5678efghi",
        "username": "test",
        "session-id": "session-ID",
        "start-timestamp": "2024-01-29T17:20:16.706282454Z"
    }
}
```

**Example FTP Server File Upload Completed example event**  <a name="event-detail-server-events.example"></a>
The following example shows an event where an upload completed successfully on an FTP server (Amazon S3 is the storage being used).  

```
{
    "version": "0",
    "id": "event-ID",
    "detail-type": "FTP Server File Upload Completed",
    "source": "aws.transfer",
    "account": "958412138249",
    "time": "2024-01-29T16:31:43Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:transfer:us-east-1:958412138249:server/s-1111aaaa2222bbbb3"
    ],
    "detail": {
        "status-code": "COMPLETED",
        "protocol": "FTP",
        "bytes": 1048576,
        "client-ip": "10.0.0.141",
        "end-timestamp": "2024-01-29T16:31:43.311866408Z",
        "etag": "b6d81b360a5672d80c27430f39153e2c",
        "file-path": "/amzn-s3-demo-bucket/test/1mb_file",
        "server-id": "s-1111aaaa2222bbbb3",
        "username": "test",
        "session-id": "event-ID",
        "start-timestamp": "2024-01-29T16:31:42.462088327Z"
    }
}
```

**Example SFTP Server File Delete Completed example event**  <a name="event-detail-server-events.example"></a>
The following example shows an event where a file was successfully deleted on an SFTP server.  

```
{
    "version": "0",
    "id": "event-ID",
    "detail-type": "SFTP Server File Delete Completed",
    "source": "aws.transfer",
    "account": "958412138249",
    "time": "2025-05-15T14:30:27Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:transfer:us-east-1:958412138249:server/s-1234abcd5678efghi"
    ],
    "detail": {
        "status-code": "COMPLETED",
        "protocol": "SFTP",
        "client-ip": "IP-address",
        "end-timestamp": "2025-05-15T14:30:27.749749117Z",
        "file-path": "/fs-1234abcd5678efghi/user0/test-file-to-delete.txt",
        "server-id": "s-1234abcd5678efghi",
        "username": "test",
        "session-id": "session-ID",
        "start-timestamp": "2025-05-15T14:30:26.706282454Z"
    }
}
```

**Example SFTP Server File Rename Completed example event**  <a name="event-detail-server-events.example"></a>
The following example shows an event where a file was successfully renamed on an SFTP server.  

```
{
    "version": "0",
    "id": "event-ID",
    "detail-type": "SFTP Server File Rename Completed",
    "source": "aws.transfer",
    "account": "958412138249",
    "time": "2025-05-15T15:45:12Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:transfer:us-east-1:958412138249:server/s-1234abcd5678efghi"
    ],
    "detail": {
        "status-code": "COMPLETED",
        "protocol": "SFTP",
        "client-ip": "IP-address",
        "end-timestamp": "2025-05-15T15:45:12.749749117Z",
        "original-file-path": "/fs-1234abcd5678efghi/user0/old-filename.txt",
        "renamed-file-path": "/fs-1234abcd5678efghi/user0/new-filename.txt",
        "server-id": "s-1234abcd5678efghi",
        "username": "test",
        "session-id": "session-ID",
        "start-timestamp": "2025-05-15T15:45:11.706282454Z"
    }
}
```

**Example SFTP Server Directory Create Completed example event**  <a name="event-detail-server-events.example"></a>
The following example shows an event where a directory was successfully created on an SFTP server.  

```
{
    "version": "0",
    "id": "event-ID",
    "detail-type": "SFTP Server Directory Create Completed",
    "source": "aws.transfer",
    "account": "958412138249",
    "time": "2025-05-15T16:20:05Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:transfer:us-east-1:958412138249:server/s-1234abcd5678efghi"
    ],
    "detail": {
        "status-code": "COMPLETED",
        "protocol": "SFTP",
        "client-ip": "IP-address",
        "end-timestamp": "2025-05-15T16:20:05.749749117Z",
        "directory-path": "/fs-1234abcd5678efghi/user0/new-directory",
        "server-id": "s-1234abcd5678efghi",
        "username": "test",
        "session-id": "session-ID",
        "start-timestamp": "2025-05-15T16:20:04.706282454Z"
    }
}
```

## SFTP connector events
<a name="event-detail-sftp-connector-events"></a>

**Note**  
These events are delivered to EventBridge at a durable level, as described in [Delivery level for AWS service events](https://docs.aws.amazon.com/eventbridge/latest/ref/event-delivery-level.html) in the *Amazon EventBridge Events Reference*.

The following are the detail fields for SFTP connector events:
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

The `source` and `detail-type` fields are included below because they contain specific values for Transfer Family events. For definitions of the other metadata fields that are included in all events, see [Event structure reference](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events-structure.html) in the *Amazon EventBridge User Guide*.

```
{
  . . .,
  "detail-type": "string",
  "source": "aws.transfer",
  . . .,
  "detail": {
    "operation" : "string",
    "max-items" : "number",
    "connector-id" : "string",
    "output-directory-path" : "string",
    "listing-id" : "string",
    "transfer-id" : "string",
    "file-transfer-id" : "string",
    "url" : "string",
    "file-path" : "string",
    "status-code" : "string",
    "failure-code" : "string",
    "failure-message" : "string",
    "start-timestamp" : "string",
    "end-timestamp" : "string",
    "local-directory-path" : "string",
    "remote-directory-path" : "string"
    "item-count" : "number"
    "truncated" : "boolean"
    "bytes" : "number",
    "egress-type" : "string",
    "vpc-lattice-resource-configuration-arn" : "string",
    "vpc-lattice-port-number" : "number",
    "local-file-location" : {
      "domain" : "string",
      "bucket" : "string",
      "key" : "string"
    },
    "output-file-location" : {
      "domain" : "string",
      "bucket" : "string",
      "key" : "string"
    }
  }
}
```

`detail-type`  <a name="event-detail-sftp-connector-events-detail-type"></a>
Identifies the type of event.  
For this event, the value is one of the SFTP connector event names listed previously.

`source`  <a name="event-detail-sftp-connector-events-source"></a>
Identifies the service that generated the event. For Transfer Family events, this value is `aws.transfer`.

`detail`  <a name="sftp-connector-detail"></a>
A JSON object that contains information about the event. The service that generates the event determines the content of this field.  
For this event, the data includes the following:    
`max-items`  <a name="sftp-connector-max-items"></a>
The maximum number of directory/file names to return.  
`operation`  <a name="sftp-connector-operation"></a>
Whether the `StartFileTransfer` request is sending or retrieving a file. Values: `SEND|RETRIEVE`.  
`connector-id`  <a name="sftp-connector-connector-id"></a>
The unique identifier for the SFTP connector being used.  
`output-directory-path`  <a name="sftp-connector-output-directory-path"></a>
The path (bucket and prefix) in Amazon S3 to store the results of the file/directory listing.  
`listing-id`  <a name="sftp-connector-listing-id"></a>
A unique identifier for the `StartDirectoryListing` API operation. This identifier can be used to check CloudWatch logs to see the status of listing request.  
`transfer-id`  <a name="sftp-connector-transfer-id"></a>
The unique identifier for the transfer event (a `StartFileTransfer` request).  
`file-transfer-id`  <a name="sftp-connector-file-transfer-id"></a>
The unique identifier for the file being transferred.  
`url`  <a name="sftp-connector-url"></a>
The URL of the partner's AS2 or SFTP endpoint.  
`file-path`  <a name="sftp-connector-file-path"></a>
The location and file that is being sent or retrieved.  
`status-code`  <a name="sftp-connector-status-code"></a>
Whether the transfer is successful. Values: `FAILED | COMPLETED`.   
`failure-code`  <a name="sftp-connector-failure-code"></a>
For failed transfers, the reason code for why the transfer failed. Values: `ASSUME_ROLE_ERROR | UNSUPPORTED_OPERATION_ERROR | CONNECTION_ERROR | READ_FILE_ERROR | WRITE_FILE_ERROR | TIMEOUT_ERROR | LIST_DIRECTORY_ERROR | SEND_FILE_NOT_FOUND | RETRIEVE_FILE_NOT_FOUND | DIRECTORY_NOT_FOUND | FILE_NOT_FOUND | PATH_NOT_FOUND | RENAME_ERROR | DELETE_ERROR | INTERNAL_ERROR | UNKNOWN_ERROR`.   
`failure-message`  <a name="sftp-connector-failure-message"></a>
For failed transfers, the details for why the transfer failed.  
`start-timestamp`  <a name="sftp-connector-start-timestamp"></a>
For successful transfers, the timestamp for when file processing begins.  
`end-timestamp`  <a name="sftp-connector-end-timestamp"></a>
For successful transfers, the timestamp for when file processing completes.  
`local-directory-path`  <a name="sftp-connector-local-directory-path"></a>
For `RETRIEVE` requests, the location in which to place the retrieved file.  
`remote-directory-path`  <a name="sftp-connector-remote-directory-path"></a>
For `SEND` requests, the file directory in which to place the file on the partner's SFTP server. This is the value for the `RemoteDirectoryPath` that the user passed to the `StartFileTransfer` request. You can specify a default directory on the partner's SFTP server. If so, this field is empty.  
`item-count`  <a name="sftp-connector-item-count"></a>
The number of items (directories and files) returned for the listing request.  
`truncated`  <a name="sftp-connector-truncated"></a>
Whether the list output contains all of the items contained in the remote directory or not.  
`bytes`  <a name="sftp-connector-bytes"></a>
The number of bytes being transferred. The value is 0 for failed transfers.  
`egress-type`  <a name="sftp-connector-egress-type"></a>
Type of egress configuration for the connector. Values: `SERVICE_MANAGED` or `VPC_LATTICE`.  
`vpc-lattice-resource-configuration-arn`  <a name="sftp-connector-vpc-lattice-resource-configuration-arn"></a>
ARN of the VPC\_LATTICE Resource Configuration that defines the target SFTP server location. This field is null for service-managed connectors.  
`vpc-lattice-port-number`  <a name="sftp-connector-vpc-lattice-port-number"></a>
Port number for connecting to the SFTP server through VPC\_LATTICE.  
`local-file-location`  <a name="sftp-connector-local-file-location"></a>
This parameter contains the details of the location of the AWS storage file.     
`domain`  <a name="sftp-connector-domain"></a>
The storage being used. Currently, the only value is `S3`.  
`bucket`  <a name="sftp-connector-bucket"></a>
The container for the object in Amazon S3.  
`key`  <a name="sftp-connector-key"></a>
The name assigned to the object in Amazon S3.  
`output-file-location`  <a name="sftp-connector-output-file-location"></a>
This parameter contains the details of the location for where to store the results of the directory listing in AWS storage.    
`domain`  <a name="sftp-connector-output-domain"></a>
The storage being used. Currently, the only value is `S3`.  
`bucket`  <a name="sftp-connector-output-bucket"></a>
The container for the object in Amazon S3.  
`key`  <a name="sftp-connector-output-key"></a>
The name assigned to the object in Amazon S3.

**Example SFTP Connector File Send Failed example event**  <a name="event-detail-sftp-connector-events.example"></a>
The following example shows an event where an SFTP connector failed while trying to send a file to a remote SFTP server.  

```
{
    "version": "0",
    "id": "event-ID",
    "detail-type": "SFTP Connector File Send Failed",
    "source": "aws.transfer",
    "account": "123456789012",
    "time": "2024-01-24T19:30:45Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:transfer:us-east-1:123456789012:connector/c-f1111aaaa2222bbbb3"
    ],
    "detail": {
        "operation": "SEND",
        "connector-id": "c-f1111aaaa2222bbbb3",
        "transfer-id": "transfer-ID",
        "file-transfer-id": "file-transfer-ID",
        "url": "sftp://s-21a23456789012a.server.transfer.us-east-1.amazonaws.com",
        "file-path": "/amzn-s3-demo-bucket/testfile.txt",
        "status-code": "FAILED",
        "failure-code": "CONNECTION_ERROR",
        "failure-message": "Unknown Host",
        "remote-directory-path": "",
        "bytes": 0,
        "start-timestamp": "2024-01-24T18:29:33.658729Z",
        "end-timestamp": "2024-01-24T18:29:33.993196Z",
        "local-file-location": {
            "domain": "S3",
            "bucket": "amzn-s3-demo-bucket",
            "key": "testfile.txt"
        }
    }
}
```

**Example SFTP Connector File Retrieve Completed example event**  <a name="event-detail-sftp-connector-events.example"></a>
The following example shows an event where an SFTP connector successfully retrieved a file sent from a remote SFTP server.  

```
{
    "version": "0",
    "id": "event-ID",
    "detail-type": "SFTP Connector File Retrieve Completed",
    "source": "aws.transfer",
    "account": "123456789012",
    "time": "2024-01-24T18:28:08Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:transfer:us-east-1:123456789012:connector/c-f1111aaaa2222bbbb3"
    ],
    "detail": {
        "operation": "RETRIEVE",
        "connector-id": "c-fc68000012345aa18",
        "transfer-id": "file-transfer-ID",
        "file-transfer-id": "file-transfer-ID",
        "url": "sftp://s-21a23456789012a.server.transfer.us-east-1.amazonaws.com",
        "file-path": "testfile.txt",
        "status-code": "COMPLETED",
        "local-directory-path": "/amzn-s3-demo-bucket",
        "bytes": 63533,
        "start-timestamp": "2024-01-24T18:28:07.632388Z",
        "end-timestamp": "2024-01-24T18:28:07.774898Z",
        "local-file-location": {
            "domain": "S3",
            "bucket": "amzn-s3-demo-bucket",
            "key": "testfile.txt"
        }
    }
}
```

**Example SFTP Connector Directory Listing Completed example event**  <a name="event-detail-sftp-connector-events.example"></a>
The following example shows an event where a start directory listing call retrieved a listing file from a remote SFTP server.  

```
{
    "version": "0",
    "id": "event-ID",
    "detail-type": "SFTP Connector Directory Listing Completed",
    "source": "aws.transfer",
    "account": "123456789012",
    "time": "2024-01-24T18:28:08Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:transfer:us-east-1:123456789012:connector/c-f1111aaaa2222bbbb3"
    ],
    "detail": {
        "max-items": 10000,
        "connector-id": "c-fc68000012345aa18",
        "output-directory-path": "/amzn-s3-demo-bucket/example/file-listing-output",
        "listing-id": "123456-23aa-7980-abc1-1a2b3c4d5e",
        "url": "sftp://s-21a23456789012a.server.transfer.us-east-1.amazonaws.com",        
        "status-code": "COMPLETED",
        "remote-directory-path": "/home",
        "item-count": 10000,
        "truncated": true,
        "start-timestamp": "2024-01-24T18:28:07.632388Z",
        "end-timestamp": "2024-01-24T18:28:07.774898Z",
        "output-file-location": {
            "domain": "S3",
            "bucket": "amzn-s3-demo-bucket",
            "key": "c-fc1ab90fd0d047e7a-70987273-49nn-4006-bab1-1a7290cc412ba.json"
        }
    }
}
```

## AS2 events
<a name="event-detail-as2-server-events"></a>

**Note**  
These events are delivered to EventBridge at a durable level, as described in [Delivery level for AWS service events](https://docs.aws.amazon.com/eventbridge/latest/ref/event-delivery-level.html) in the *Amazon EventBridge Events Reference*.

The following are the detail fields for AS2 events:
+ AS2 Payload Receive Completed
+ AS2 Payload Receive Failed
+ AS2 Payload Send Completed
+ AS2 Payload Send Failed
+ AS2 MDN Receive Completed
+ AS2 MDN Receive Failed
+ AS2 MDN Send Completed
+ AS2 MDN Send Failed

The `source` and `detail-type` fields are included below because they contain specific values for Transfer Family events. For definitions of the other metadata fields that are included in all events, see [Event structure reference](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events-structure.html) in the *Amazon EventBridge User Guide*.

```
{
   . . .,
  "detail-type": "string",
  "source": "aws.transfer",
  . . .,
  "detail": {    
    "s3-attributes" : {
      "file-bucket" : "string",
      "file-key" : "string",
      "json-bucket" : "string",
      "json-key" : "string", 
      "mdn-bucket" : "string",
      "mdn-key" : "string"
      }
    "mdn-subject" : "string",
    "mdn-message-id" : "string",
    "disposition" : "string",
    "bytes" : "number",
    "as2-from" : "string",
    "as2-message-id" : "string",
    "as2-to" : "string",
    "connector-id" : "string",
    "client-ip" : "string",
    "agreement-id" : "string",
    "server-id" : "string",
    "requester-file-name" : "string",
    "message-subject" : "string",
    "start-timestamp" : "string",
    "end-timestamp" : "string",
    "status-code" : "string",
    "failure-code" : "string",
    "failure-message" : "string",
    "transfer-id" : "string"
  }
}
```

`detail-type`  <a name="event-detail-as2-server-events-detail-type"></a>
Identifies the type of event.  
For this event, the value is one of the AS2 events listed previously.

`source`  <a name="event-detail-as2-server-events-source"></a>
Identifies the service that generated the event. For Transfer Family events, this value is `aws.transfer`.

`detail`  <a name="as2-server-detail"></a>
A JSON object that contains information about the event. The service generating the event determines the content of this field.    
`s3-attributes`  <a name="as2-server-s3-attributes"></a>
Identifies the Amazon S3 bucket and key for the file being transferred. For MDN events, it also identifies the bucket and key for the MDN file.    
`file-bucket`  <a name="as2-server-s3-file-bucket"></a>
The container for the object in Amazon S3.  
`file-key`  <a name="as2-server-s3-file-key"></a>
The name assigned to the object in Amazon S3.  
`json-bucket`  <a name="as2-server-s3-json-bucket"></a>
For COMPLETED or FAILED transfers, the container for the JSON file.  
`json-key`  <a name="as2-server-s3-json-key"></a>
For COMPLETED or FAILED transfers, the name assigned to the JSON file in Amazon S3.  
`mdn-bucket`  <a name="as2-server-s3-mdn-bucket"></a>
For MDN events, the container for the MDN file.  
`mdn-key`  <a name="as2-server-s3-mdn-key"></a>
For MDN events, the name assigned to the MDN file in Amazon S3.   
`mdn-subject`  <a name="as2-server-mdn-subject"></a>
For MDN events, a text description for the message disposition.  
`mdn-message-id`  <a name="as2-server-mdn-message-id"></a>
For MDN events, a unique ID for the MDN message.  
`disposition`  <a name="as2-server-disposition"></a>
For MDN events, the category for the disposition.  
`bytes`  <a name="as2-server-bytes"></a>
The number of bytes in the message.  
`as2-from`  <a name="as2-server-as2-from"></a>
The AS2 trading partner that is sending the message.  
`as2-message-id`  <a name="as2-server-as2-message-id"></a>
A unique identifier for the AS2 message being transferred.  
`as2-to`  <a name="as2-server-as2-to"></a>
The AS2 trading partner that is receiving the message.  
`connector-id`  <a name="as2-server-connector-id"></a>
For AS2 messages being sent from a Transfer Family server to a trading partner, the unique identifier for the AS2 connector being used.  
`client-ip`  <a name="as2-server-client-ip"></a>
For server events (transfers from a trading partner to a Transfer Family server), the IP address for the client involved in the transfer.   
`agreement-id`  <a name="as2-server-agreement-id"></a>
For server events, the unique identifier for the AS2 agreement.  
`server-id`  <a name="as2-server-server-id"></a>
For server events, a unique ID only for the Transfer Family server.  
`requester-file-name`  <a name="as2-server-requester-file-name"></a>
For payload events, the original name for the file received during the transfer.  
`message-subject`  <a name="as2-server-message-subject"></a>
A text description for the subject of the message.  
`start-timestamp`  <a name="as2-server-start-timestamp"></a>
For successful transfers, the timestamp for when file processing begins.  
`end-timestamp`  <a name="as2-server-end-timestamp"></a>
For successful transfers, the timestamp for when file processing completes.  
`status-code`  <a name="as2-server-status-code"></a>
The code that corresponds to the state of the AS2 message transfer process. Valid values: `COMPLETED | FAILED | PROCESSING`.  
`failure-code`  <a name="as2-server-failure-code"></a>
For failed transfers, the category for why the transfer failed.  
`failure-message`  <a name="as2-server-failure-message"></a>
For failed transfers, the details for why the transfer failed.  
`transfer-id`  <a name="as2-server-transfer-id"></a>
The unique identifier for the transfer event.

**Example AS2 Payload Receive Completed example event**  <a name="event-detail-as2-server-events.example"></a>

```
{
    "version": "0",
     "id": "event-ID",
    "detail-type": "AS2 Payload Receive Completed",
    "source": "aws.transfer",
    "account": "076722215406",
    "time": "2024-02-07T06:47:05Z",
    "region": "us-east-1",
    "resources": ["arn:aws:transfer:us-east-1:076722215406:connector/c-1111aaaa2222bbbb3"],
    "detail": {
        "s3-attributes": {
            "file-key": "/inbound/processed/testAs2Message.dat",
            "file-bucket": "amzn-s3-demo-bucket"
        },
        "client-ip": "client-IP-address",
        "requester-file-name": "testAs2MessageVerifyFile.dat",
        "end-timestamp": "2024-02-07T06:47:06.040031Z",
        "as2-from": "as2-from-ID",
        "as2-message-id": "as2-message-ID",
        "message-subject": "Message from AS2 tests",
        "start-timestamp": "2024-02-07T06:47:05.410Z",
        "status-code": "PROCESSING",
        "bytes": 63,
        "as2-to": "as2-to-ID",
        "agreement-id": "a-1111aaaa2222bbbb3",
        "server-id": "s-1234abcd5678efghi"
    }
}
```

**Example AS2 MDN Receive Failed example event**  <a name="event-detail-as2-server-events.example"></a>

```
{
  "version": "0",
  "id": "event-ID",
  "detail-type": "AS2 MDN Receive Failed",
  "source": "aws.transfer",
  "account": "889901007463",
  "time": "2024-02-06T22:05:09Z",
  "region": "us-east-1",
  "resources": ["arn:aws:transfer:us-east-1:076722215406:server/s-1111aaaa2222bbbb3"],
  "detail": {      
      "mdn-subject": "Your Requested MDN Response re: Test run from Id 123456789abcde to partner ijklmnop987654",
      "s3-attributes": {
          "json-bucket": "amzn-s3-demo-bucket1",
          "file-key": "/as2Integ/TestOutboundWrongCert.dat",
          "file-bucket": "amzn-s3-demo-bucket2",
          "json-key": "/as2Integ/failed/TestOutboundWrongCert.dat.json"
      },
      "mdn-message-id": "MDN-message-ID",
      "end-timestamp": "2024-02-06T22:05:09.479878Z",
      "as2-from": "PartnerA",
      "as2-message-id": "as2-message-ID",
      "connector-id": "c-1234abcd5678efghj",
      "message-subject": "Test run from Id 123456789abcde to partner ijklmnop987654",
      "start-timestamp": "2024-02-06T22:05:03Z",
      "failure-code": "VERIFICATION_FAILED_NO_MATCHING_KEY_FOUND",
      "status-code": "FAILED",
      "as2-to": "MyCompany",
      "failure-message": "No public certificate matching message signature could be found in profile: p-1234abcd5678efghj",
      "transfer-id": "transfer-ID"
  }
}
```