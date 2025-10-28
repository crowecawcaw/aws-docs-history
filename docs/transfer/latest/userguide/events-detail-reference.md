# Transfer Family events detail reference

All events from AWS services have a common set of fields containing
metadata about the event. These metadata can include the AWS service that
is the source of the event, the time the event was generated, the account and Region in
which the event took place, and others. For definitions of these general fields, see
[Event structure
reference](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the _Amazon EventBridge User Guide_.

In addition, each event has a `detail` field that contains data specific to
that particular event. The following reference defines the detail fields for the various
Transfer Family events.

When you use EventBridge to select and manage Transfer Family events, consider the
following:

- The `source` field for all events from Transfer Family is set to
  `aws.transfer`.
- The `detail-type` field specifies the event type.

For example, `FTP Server File Download Completed`.

- The `detail` field contains the data that is specific to that
  particular event.
  For information on constructing event patterns that enable rules to match Transfer Family
  events, see [Event patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md") in
  the _Amazon EventBridge User Guide_.

For more information on events and how EventBridge processes them, see [Amazon EventBridge events](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md") in the _Amazon EventBridge User
Guide_.

###### Topics

- [SFTP, FTPS, and FTP server
  events](#event-detail-server-events "#event-detail-server-events")
- [SFTP connector events](#event-detail-sftp-connector-events "#event-detail-sftp-connector-events")
- [AS2 events](#event-detail-as2-server-events "#event-detail-as2-server-events")

## SFTP, FTPS, and FTP server

events

The following are the detail fields for SFTP, FTPS, and FTP server events:

- FTP Server Directory Create Completed
- FTP Server Directory Create Failed
- FTP Server Directory Delete Completed
- FTP Server Directory Delete Failed
- FTP Server File Delete Completed
- FTP Server File Delete Failed
- FTP Server File Download Completed
- FTP Server File Download Failed
- FTP Server File Rename Completed
- FTP Server File Rename Failed
- FTP Server File Upload Completed
- FTP Server File Upload Failed
- FTPS Server Directory Create Completed
- FTPS Server Directory Create Failed
- FTPS Server Directory Delete Completed
- FTPS Server Directory Delete Failed
- FTPS Server File Delete Completed
- FTPS Server File Delete Failed
- FTPS Server File Download Completed
- FTPS Server File Download Failed
- FTPS Server File Rename Completed
- FTPS Server File Rename Failed
- FTPS Server File Upload Completed
- FTPS Server File Upload Failed
- SFTP Server Directory Create Completed
- SFTP Server Directory Create Failed
- SFTP Server Directory Delete Completed
- SFTP Server Directory Delete Failed
- SFTP Server File Delete Completed
- SFTP Server File Delete Failed
- SFTP Server File Download Completed
- SFTP Server File Download Failed
- SFTP Server File Rename Completed
- SFTP Server File Rename Failed
- SFTP Server File Upload Completed
- SFTP Server File Upload Failed

The `source` and `detail-type` fields are included below because they contain specific values for Transfer Family events. For
definitions of the other metadata fields that are included in all events, see [Event structure
reference](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the _Amazon EventBridge User Guide_.

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

`detail-type`

Identifies the type of event.

For this event, the value is one of the SFTP, FTPS, or FTP server
event names listed previously.

`source`

Identifies the service that generated the event. For Transfer Family events, this
value is `aws.transfer`.

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

For this event, the data includes the following:

`failure-code`

Category for why the transfer failed. Values:
`PARTIAL_UPLOAD | PARTIAL_DOWNLOAD |
 UNKNOWN_ERROR`

`status-code`

Whether the transfer is successful. Values:
`COMPLETED | FAILED`.

`protocol`

The protocol used for the transfer. Values: `SFTP |
 FTPS | FTP`

`bytes`

The number of bytes transferred.

`client-ip`

The IP address for the client involved in the
transfer

`failure-message`

For failed transfers, the details for why the transfer
failed.

`end-timestamp`

For successful transfers, the timestamp for when the file
finishes being processed.

`etag`

The entity tag (only used for Amazon S3 files).

`file-path`

The path to the file being transferred, deleted, or
otherwise operated on.

`original-file-path`

For file rename events, the original path of the file
before renaming.

`renamed-file-path`

For file rename events, the new path of the file after
renaming.

`directory-path`

For directory create and delete events, the path of the
directory.

`server-id`

The unique ID for the Transfer Family server.

`username`

The user that is performing the transfer.

`session-id`

The unique identifier for the transfer session.

`start-timestamp`

For successful transfers, the timestamp for when file
processing begins.

###### Example SFTP Server File Download Failed

example event

The following example shows an event where a download failed on an SFTP server
(Amazon EFS is the storage being used).

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

###### Example FTP Server File Upload Completed

example event

The following example shows an event where an upload completed successfully on
an FTP server (Amazon S3 is the storage being used).

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

###### Example SFTP Server File Delete Completed

example event

The following example shows an event where a file was successfully deleted on
an SFTP server.

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

###### Example SFTP Server File Rename Completed

example event

The following example shows an event where a file was successfully renamed on
an SFTP server.

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

###### Example SFTP Server Directory Create Completed

example event

The following example shows an event where a directory was successfully
created on an SFTP server.

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

###### Note

These events are delivered to EventBridge at a durable level, as
described in [Delivery level for
AWS service events](../../../eventbridge/latest/ref/event-delivery-level.md "../../../eventbridge/latest/ref/event-delivery-level.md") in the _Amazon EventBridge Events Reference_.

The following are the detail fields for SFTP connector events:

- SFTP Connector File Send Completed
- SFTP Connector File Send Failed
- SFTP Connector File Retrieve Completed
- SFTP Connector File Retrieve Failed
- SFTP Connector Directory Listing Completed
- SFTP Connector Directory Listing Failed
- SFTP Connector Remote Move Completed
- SFTP Connector Remote Move Failed
- SFTP Connector Remote Delete Completed
- SFTP Connector Remote Delete Failed

The `source` and `detail-type` fields are included below because they contain specific values for Transfer Family events. For
definitions of the other metadata fields that are included in all events, see [Event structure
reference](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the _Amazon EventBridge User Guide_.

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

`detail-type`

Identifies the type of event.

For this event, the value is one of the SFTP connector event names
listed previously.

`source`

Identifies the service that generated the event. For Transfer Family events,
this value is `aws.transfer`.

`detail`

A JSON object that contains information about the event. The service
that generates the event determines the content of this field.

For this event, the data includes the following:

`max-items`

The maximum number of directory/file names to
return.

`operation`

Whether the `StartFileTransfer` request is
sending or retrieving a file. Values:
`SEND|RETRIEVE`.

`connector-id`

The unique identifier for the SFTP connector being
used.

`output-directory-path`

The path (bucket and prefix) in Amazon S3 to store the results
of the file/directory listing.

`listing-id`

A unique identifier for the
`StartDirectoryListing` API operation. This
identifier can be used to check CloudWatch logs to see the status
of listing request.

`transfer-id`

The unique identifier for the transfer event (a
`StartFileTransfer` request).

`file-transfer-id`

The unique identifier for the file being
transferred.

`url`

The URL of the partner's AS2 or SFTP endpoint.

`file-path`

The location and file that is being sent or
retrieved.

`status-code`

Whether the transfer is successful. Values: `FAILED |
 COMPLETED`.

`failure-code`

For failed transfers, the reason code for why the transfer
failed.

`failure-message`

For failed transfers, the details for why the transfer
failed.

`start-timestamp`

For successful transfers, the timestamp for when file
processing begins.

`end-timestamp`

For successful transfers, the timestamp for when file
processing completes.

`local-directory-path`

For `RETRIEVE` requests, the location in which
to place the retrieved file.

`remote-directory-path`

For `SEND` requests, the file directory in
which to place the file on the partner's SFTP server. This
is the value for the `RemoteDirectoryPath` that
the user passed to the `StartFileTransfer`
request. You can specify a default directory on the
partner's SFTP server. If so, this field is empty.

`item-count`

The number of items (directories and files) returned for
the listing request.

`truncated`

Whether the list output contains all of the items
contained in the remote directory or not.

`bytes`

The number of bytes being transferred. The value is 0 for
failed transfers.

`egress-type`

Type of egress configuration for the connector. Values:
`SERVICE_MANAGED` or
`VPC_LATTICE`.

`vpc-lattice-resource-configuration-arn`

ARN of the VPC_LATTICE Resource Configuration that defines
the target SFTP server location. This field is null for
service-managed connectors.

`vpc-lattice-port-number`

Port number for connecting to the SFTP server through
VPC_LATTICE.

`local-file-location`

This parameter contains the details of the location of the
AWS storage file.

`domain`

The storage being used. Currently, the only
value is `S3`.

`bucket`

The container for the object in Amazon S3.

`key`

The name assigned to the object in Amazon S3.

`output-file-location`

This parameter contains the details of the location for
where to store the results of the directory listing in AWS
storage.

`domain`

The storage being used. Currently, the only
value is `S3`.

`bucket`

The container for the object in Amazon S3.

`key`

The name assigned to the object in Amazon S3.

###### Example SFTP Connector File Send Failed

example event

The following example shows an event where an SFTP connector failed while
trying to send a file to a remote SFTP server.

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

###### Example SFTP Connector File Retrieve Completed

example event

The following example shows an event where an SFTP connector successfully
retrieved a file sent from a remote SFTP server.

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

###### Example SFTP Connector Directory Listing Completed

example event

The following example shows an event where a start directory listing call
retrieved a listing file from a remote SFTP server.

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

###### Note

These events are delivered to EventBridge at a durable level, as
described in [Delivery level for
AWS service events](../../../eventbridge/latest/ref/event-delivery-level.md "../../../eventbridge/latest/ref/event-delivery-level.md") in the _Amazon EventBridge Events Reference_.

The following are the detail fields for AS2 events:

- AS2 Payload Receive Completed
- AS2 Payload Receive Failed
- AS2 Payload Send Completed
- AS2 Payload Send Failed
- AS2 MDN Receive Completed
- AS2 MDN Receive Failed
- AS2 MDN Send Completed
- AS2 MDN Send Failed

The `source` and `detail-type` fields are included below because they contain specific values for Transfer Family events. For
definitions of the other metadata fields that are included in all events, see [Event structure
reference](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the _Amazon EventBridge User Guide_.

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

`detail-type`

Identifies the type of event.

For this event, the value is one of the AS2 events listed
previously.

`source`

Identifies the service that generated the event. For Transfer Family events,
this value is `aws.transfer`.

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

`s3-attributes`

Identifies the Amazon S3 bucket and key for the file being
transferred. For MDN events, it also identifies the bucket
and key for the MDN file.

`file-bucket`

The container for the object in Amazon S3.

`file-key`

The name assigned to the object in Amazon S3.

`json-bucket`

For COMPLETED or FAILED transfers, the
container for the JSON file.

`json-key`

For COMPLETED or FAILED transfers, the name
assigned to the JSON file in Amazon S3.

`mdn-bucket`

For MDN events, the container for the MDN
file.

`mdn-key`

For MDN events, the name assigned to the MDN
file in Amazon S3.

`mdn-subject`

For MDN events, a text description for the message
disposition.

`mdn-message-id`

For MDN events, a unique ID for the MDN message.

`disposition`

For MDN events, the category for the disposition.

`bytes`

The number of bytes in the message.

`as2-from`

The AS2 trading partner that is sending the
message.

`as2-message-id`

A unique identifier for the AS2 message being
transferred.

`as2-to`

The AS2 trading partner that is receiving the
message.

`connector-id`

For AS2 messages being sent from a Transfer Family server to a
trading partner, the unique identifier for the AS2 connector
being used.

`client-ip`

For server events (transfers from a trading partner to a
Transfer Family server), the IP address for the client involved in the
transfer.

`agreement-id`

For server events, the unique identifier for the AS2
agreement.

`server-id`

For server events, a unique ID only for the Transfer Family
server.

`requester-file-name`

For payload events, the original name for the file
received during the transfer.

`message-subject`

A text description for the subject of the message.

`start-timestamp`

For successful transfers, the timestamp for when file
processing begins.

`end-timestamp`

For successful transfers, the timestamp for when file
processing completes.

`status-code`

The code that corresponds to the state of the AS2 message
transfer process. Valid values: `COMPLETED | FAILED |
 PROCESSING`.

`failure-code`

For failed transfers, the category for why the transfer
failed.

`failure-message`

For failed transfers, the details for why the transfer
failed.

`transfer-id`

The unique identifier for the transfer event.

###### Example AS2 Payload Receive Completed

example event

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

###### Example AS2 MDN Receive Failed

example event

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
