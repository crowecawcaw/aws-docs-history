

# Using CloudWatch metrics for Transfer Family servers
<a name="metrics"></a>

**Note**  
 You can also get metrics for Transfer Family from within the Transfer Family console itself. For details, see [Monitoring usage in the console](monitor-usage-transfer-console.md) 

You can get information about your server using CloudWatch metrics. A *metric* represents a time-ordered set of data points that are published to CloudWatch. When using metrics, you must specify the Transfer Family namespace, metric name, and [dimension](#cw-dimensions). For more information about metrics, see [Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Metric) in the *Amazon CloudWatch User Guide*.

 The following table describes the CloudWatch metrics for Transfer Family.



- ** `AWS/Transfer` **
  - **Metric:** `BytesIn` / **Description:** The total number of bytes transferred into the server.<br />**Reporting criteria**:+  For SFTP/FTP/FTPS: emitted every 5 minutes while a connection is established to the Transfer Family server. If no files or bytes are transferred in the period, "0" is emitted. <br />+  For AS2: when the customer receives a message in their AS2 server and emitted as soon as the inbound message has finished processing <br />**Units**: Count<br />**Period**: 5 minutes
  - **Metric:** `BytesOut` / **Description:** The total number of bytes transferred out of the server.<br />**Reporting criteria**:+  For SFTP/FTP/FTPS: emitted every 5 minutes while a connection is established to the Transfer Family server. If no files or bytes are transferred in the period, "0" is emitted. <br />+  For AS2: when the customer calls `StartFileTransfer` from their AS2 connector and emitted as soon as the outbound message has finished processing. <br />**Units**: Count<br />**Period**: 5 minutes
  - **Metric:**  `FilesIn`  / **Description:** The total number of files transferred into the server.<br />For servers using the AS2 protocol, this metric represents the number of messages received.<br />**Reporting criteria**:+  For SFTP/FTP/FTPS: emitted every 5 minutes while a connection is established to the Transfer Family server. If no files or bytes are transferred in the period, "0" is emitted. <br />+  For AS2: when the customer receives a message in their AS2 server and emitted as soon as the inbound message has finished processing. <br />**Units**: Count<br />**Period**: 5 minutes
  - **Metric:**  `FilesOut`  / **Description:** The total number of files transferred out of the server.<br />**Reporting criteria**:+  For SFTP/FTP/FTPS: emitted every 5 minutes while a connection is established to the Transfer Family server. If no files or bytes are transferred in the period, "0" is emitted. <br />+  For AS2: when the customer calls `StartFileTransfer` from their AS2 connector and emitted as soon as the outbound message has finished processing. <br />**Units**: Count<br />**Period**: 5 minutes
  - **Metric:**  `InboundMessage`  / **Description:** The total number of AS2 messages successfully received from a trading partner.<br />**Reporting criteria**: When the customer receives a message in their AS2 server and emitted as soon as the inbound message has finished processing successfully<br />**Units**: Count<br />**Period**: 5 minutes
  - **Metric:**  `InboundFailedMessage`  / **Description:** The total number of AS2 messages that were unsuccessfully received from a trading partner. That is, a trading partner sent a message, but the Transfer Family server was not able to successfully process it.<br />**Reporting criteria**: When the customer receives a message in their AS2 server and emitted as soon as the inbound message has finished processing unsuccessfully<br />**Units**: Count<br />**Period**: 5 minutes
  - **Metric:**  `OnUploadExecutionsStarted`  / **Description:** The total number of workflow executions started on the server.<br />**Reporting criteria**: Triggered every time an execution starts<br />**Units**: Count<br />**Period**: 1 minute
  - **Metric:**  `OnUploadExecutionsSuccess`  / **Description:** The total number of successful workflow executions on the server.<br />**Reporting criteria**: Triggered every time an execution successfully finishes<br />**Units**: Count<br />**Period**: 1 minute
  - **Metric:**  `OnUploadExecutionsFailed`  / **Description:** The total number of unsuccessful workflow executions on the server.<br />**Reporting criteria**: Triggered every time an execution does not successfully finish<br />**Units**: Count<br />**Period**: 1 minute
  - **Metric:** `OutboundMessage` / **Description:** The total number of AS2 messages successfully sent to a a trading partner.<br />**Reporting criteria**: When the customer calls `StartFileTransfer` from their AS2 connector and emitted as soon as the outbound message has finished processing successfully<br />**Units**: Count<br />**Period**: 5 minutes
  - **Metric:** `OutboundFailedMessage` / **Description:** The total number of AS2 messages that were unsuccessfully sent to a trading partner. <br />**Reporting criteria**: When the customer calls `StartFileTransfer` from their AS2 connector and emitted as soon as the outbound message has finished processing unsuccessfully<br />**Units**: Count<br />**Period**: 5 minutes



## Transfer Family dimensions
<a name="cw-dimensions"></a>

A *dimension* is a name/value pair that is part of the identity of a metric. For more information about dimensions, see [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension) in the *Amazon CloudWatch User Guide*.

The following table describes the CloudWatch dimensions for Transfer Family.


| Dimension | Description | 
| --- | --- | 
| `ServerId` | The unique ID of the server. | 
| `ConnectorId` | The unique ID of the connector. Used for AS2, for `OutboundMessage` and `OutboundFailedMessage` | 