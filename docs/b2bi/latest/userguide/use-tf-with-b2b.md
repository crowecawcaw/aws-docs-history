# Using Transfer Family with B2B Data Interchange

[AWS Transfer Family](../../../transfer/latest/userguide/what-is-aws-transfer-family.md "../../../transfer/latest/userguide/what-is-aws-transfer-family.md") is a
secure data transfer service that enables you to move files into and out of AWS over
industry standard protocols such as SFTP, AS2, FTPS, and FTP.

You have two options to receive X12 from your trading partner using AWS Transfer Family:

- Your trading partner sends the X12 file to your Transfer Family SFTP or AS2 server.
- You retrieve X12 EDI documents from your trading partner's SFTP server using your
  Transfer Family SFTP connector.
  In either case, inbound X12 EDI documents should be written to the dedicated partner
  prefix nested within the input directory of any trading capability associated with a
  partnership (for example,
  `s3://EDI-bucket/input-EDI/`partnership-id``),
  so that B2B Data Interchange can automatically pick up the file for processing.

Similarly, you have two options to send the generated X12 to your trading partner:

- Your trading partner retrieves X12 EDI documents from your Transfer Family SFTP
  server.
- You send X12 EDI documents to your trading partner's server using your Transfer Family SFTP
  or AS2 connector.
  In the case where your trading partner retrieves X12 EDI documents from your Transfer Family SFTP
  server, you provide your partner with authenticated access to the prefix within the output
  directory of the trading capability associated with the trading partnership (for example,
  `s3://EDI-bucket/output-EDI/`<capability-id>`/`<partnership-id>``).
  In the case where you send X12 EDI documents to your trading partner's server with your Transfer Family
  SFTP or AS2 connector, you provide the absolute path of the X12 EDI document in your [StartFileTransfer](../../../transfer/latest/APIReference/API_StartFileTransfer.md "../../../transfer/latest/APIReference/API_StartFileTransfer.md") API operation.

You can automate the sending of X12 EDI documents to your trading partners using the B2B Data Interchange
events published to Amazon EventBridge. To learn more about how to create rules for these events, see
[Managing AWS B2B Data Interchange events using Amazon EventBridge](eventbridge.md "eventbridge.md").

###### Note

You can use either mechanism to also send EDI acknowledgements to your trading
partner. For more details, see [EDI acknowledgements](edi-ack.md "edi-ack.md")

For a self-paced learning experience, go through the [EDI document exchange
with AWS B2B Data Interchange Workshop](https://catalog.workshops.aws/getting-started-b2b-data-interchange/ "https://catalog.workshops.aws/getting-started-b2b-data-interchange/"), created by the B2B Data Interchange service team. In this workshop, you learn
how to receive and transform EDI documents from your business partners using AWS B2B Data Interchange and
AWS Transfer Family.
