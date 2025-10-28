# EDI acknowledgements

B2B Data Interchange automatically generates acknowledgements that you can return to your trading partner
to communicate that the file was received and to report errors. The generated
acknowledgement is stored in your Amazon S3 bucket alongside the transformed EDI, and an event is
emitted by the B2B Data Interchange service to Amazon EventBridge.

The service generates the following types of acknowledgements:

- _TA1 interchange acknowledgements_: A TA1 is an interchange
  acknowledgement used to confirm the receipt of X12 EDI interchanges and to report
  syntactical errors. It reports the status of the processing of an interchange header
  and trailer by the addressed receiver or the non-delivery by a network provider. TA1
  interchange acknowledgements are generated for all interchanges.
- _997 functional acknowledgements_: the 997 is a functional
  acknowledgement used to confirm receipt of X12 EDI transactions and to report
  transactional errors. A 997 acknowledgement serves as a response to an individual
  EDI message or group of messages. It contains information about the receipt of the
  upstream transaction, such as whether it has been accepted, accepted with errors or
  rejected. Most finance, transportation, supply chain, and communication &
  control transactions generate a 997 functional acknowledgement.
- _999 functional acknowledgements_: there are two types of 999
  functional acknowledgement, as follows:

      + 999 functional acknowledgement for HIPAA transactions: the service
       generates *999 X231* acknowledgements for all X12 version
       5010 HIPAA transactions.
      + 999 functional acknowledgement for non-HIPAA transactions: the service
       generates *999* acknowledgements for all other
       healthcare-related X12 transactions.

  You have the option to disable acknowledgement generation for processed inbound EDI
  documents. To do this, choose **Do not generate** in the
  **Generated Acknowledgments Documents** section of your partnership
  configuration. For functional acknowledgements, you can also opt to generate acknowledgments
  without the AK2 loop by selecting **Generate without AK2 loop** in the
  **Functional (997 and 999 Acknowledgements)** box. These
  acknowledgement settings are configured at the partnership level and apply to all inbound
  EDI documents processed within that partnership.

###### Note

The service generates either a 999 or 997 acknowledgement, but never both.

For details of the generated events, see [AWS B2B Data Interchange events detail reference](events-detail-reference.md "events-detail-reference.md").

One example use case is as follows: Retailer B responds with an EDI 997 Functional
Acknowledgement, which communicates to Vendor A that their EDI 810 Invoice was received and
is syntactically valid.

1. Retailer B receives X12 EDI 810 Invoice from Vendor A.
2. Retailer B responds with an EDI 997 Functional Acknowledgement, which communicates
   to Vendor A that their EDI 810 Invoice was received and is syntactically
   valid.
   B2B Data Interchange creates events when generating acknowledgements (for both successful and failed
   scenarios). The primary value of generating these events is for returning the
   acknowledgement to the trading partner. You can use AWS Transfer Family (or any other data transfer
   service) to send these acknowledgements to your trading partner.

To learn more about using B2Bi acknowledgement events to return acknowledgements to your
trading partner, see [Details fields for transformation
events](events-detail-reference.md#detail-fields-transform "events-detail-reference.md#detail-fields-transform").

## Acknowledgement output paths

This section describes the output paths for acknowledgement files saved to
Amazon S3.

Let's assume that a customer configures their EDI trading capability to have the
following input and output directories.

- Input: s3://amzn-s3-demo-bucket/IN/
- Output: s3://amzn-s3-demo-bucket/OUT/

In this example, the absolute paths for the EDI input document and the transformed
JSON or XML output are as follows:

- Inbound EDI: s3://amzn-s3-demo-bucket/IN/TP_ID/edi214xml-test83.txt
- Transformed output:
  s3://amzn-s3-demo-bucket/OUT/TP_ID/edi214xml-test83.txt.2023-11-21T19:26:49.774Z.xml

The path of the acknowledgement depends on whether the inbound X12 EDI document is
transformed using a trading capability or transformed by directly invoking the
`StartTransformerJob` API operation.

When using a trading capability, the format for the acknowledgement files is
s3://amzn-s3-demo-bucket/OUT/TP_ID/ACK/`filename`.`timestamp`.997
(.TA1 for TA1 acknowledgements).

When invoking the `StartTransformerJob` API directly, acknowledgements will
be written into a dedicated ACK prefix within the output location specified in the
request. See the following example paths.

Acknowledgement use case example

The following are examples for the acknowledgement output filenames:

- 997 acknowledgement:
  `s3://amzn-s3-demo-bucket/OUT/TP_ID/ACK/edi214xml-test83.txt.2023-11-21T19:26:49.774Z.997`
- 999 X231 acknowledgement:
  `s3://amzn-s3-demo-bucket/OUT/TP_ID/ACK/edi835x221.xml-test83.txt.2023-11-21T19:26:49.774Z.999x231`
- TA1 acknowledgement:
  `s3://amzn-s3-demo-bucket/OUT/TP_ID/ACK/edi214xml-test83.txt.2023-11-21T19:26:49.774Z.TA1`

For direct transformer API calls, the format is
`s3://amzn-s3-demo-bucket/OUT/ACK/`filename`.`timestamp`.997`
(`.TA1` for TA1 acknowledgements).
