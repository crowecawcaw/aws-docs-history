

# Monitoring usage in the console
<a name="monitor-usage-transfer-console"></a>

 You can get information about your server's metrics on its **Server details** page. This provides you with a single place to monitor your file-transfers workloads. You can track how many files you have exchanged with your partners and closely track their usage using a centralized dashboard. For details, see [View SFTP, FTPS, and FTP server details](configuring-servers-view-info.md). The following table describes the metrics available for Transfer Family. 



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



 The **Monitoring** section contains four, individual graphs. These graphs show the bytes in, bytes out, files in, and files out. 

![The Monitoring console section showing the BytesIn, BytesOut, FilesIn, and FilesOut graphs.](http://docs.aws.amazon.com/transfer/latest/userguide/images/metrics.png)


For servers that have the AS2 protocol enabled, there is an **AS2 Monitoring** section below the **Monitoring** information. This section contains details for the number of inbound messages, both successful and failed.

![The AS2 Monitoring console section showing the InboundMessages, and InboundMessagesFailed details.](http://docs.aws.amazon.com/transfer/latest/userguide/images/as2-metrics-inbound.png)


 To open the selected graph in its own window, choose the expand icon (![Expand icon](http://docs.aws.amazon.com/transfer/latest/userguide/images/expand.png)). You can also click a graph's vertical ellipsis icon (![Vertical ellipsis icon](http://docs.aws.amazon.com/transfer/latest/userguide/images/vertical-ellipsis.png)) to open a dropdown menu with the following items: 
+ **Enlarge** – Opens the selected graph in its own window.
+ **Refresh** – Reloads the graph with the most recent data.
+ **View in metrics** – Opens the corresponding metrics details in Amazon CloudWatch.
+ **View logs** – Opens the corresponding log group in CloudWatch.