# EDI splitting

AWS B2B Data Interchange supports splitting of inbound X12 EDI documents that contain multiple
transactions into individually processed single-transaction documents. This capability
increases the maximum supported file size for multi-transaction EDI documents from 150MB to
5GB and enables independent processing of each transaction, even when trading partners send
them batched in a single EDI file.

With EDI splitting, each resulting single-transaction document is independently validated
and processed, emitting its own set of logs and EventBridge events. This enables individual
post-processing and downstream business-system ingestions. For example, you can use the
"Split Transformation Completed" events to trigger AWS Glue ETL jobs to automatically ingest
valid transactions into your purpose-built data lake, while using the "Split Transformation
Failed" events to notify your trading partner of issues with individual transactions of
their EDI document.

## How EDI Splitting Works

When EDI Splitting is enabled, AWS B2B Data Interchange processes each X12 EDI file as
follows:

1. The service parses and validates the EDI file, generates acknowledgement
   documents for the entire original document (if requested), and identifies the
   individual transactions within the EDI interchange
2. The service generates individual, temporary EDI files for each transaction,
   maintaining all header and trailer-level information from the original EDI
   interchange within each separated transaction.
3. The service processes each split file individually, applying validation and
   any configured transformations.
4. Individual EventBridge events are published for each post-split file processing,
   enabling automated downstream workflows.

When splitting is enabled, validation errors are handled as follows:

- If an inbound EDI document fails validation because of issues in its
  interchange or functional group header/trailer segments, it will not be split
  and will fail processing altogether.
- If an inbound EDI document fails validation because of issues in segments
  contained in one of its transactions, the document will still be split, and
  individual post-split documents will be processed by the service.

## Key Benefits

EDI Splitting offers several key benefits:

- _Increased File Size Support_: With splitting enabled,
  AWS B2B Data Interchange can handle X12 EDI files up to 5GB, compared to the standard 150MB
  limit for non-split files.
- _Independent Transaction Processing_: Each transaction is
  processed independently, allowing valid transactions to proceed even if others
  in the batch contain errors.
- _Granular Event-Driven Workflows_: Individual EventBridge events
  for each transaction enable fine-grained control over downstream
  processing.
- _Improved Error Handling_: Transaction-level validation
  provides more precise error reporting and enables targeted reprocessing of
  failed transactions.
- _Simplified Integration_: Individual transaction processing
  simplifies integration with downstream business systems that expect
  single-transaction inputs.

## Limits and Considerations

AWS B2B Data Interchange has the following limits for EDI Splitting:

- Maximum of 100 transactions per split file
- Increased file size limit of 5GB for split-enabled files (compared to 150MB
  for non-split files)
- Splitting is only available by transaction, not by functional group or other
  criteria

When implementing EDI splitting, consider the following:

- _Acknowledgments_: AWS B2B Data Interchange currently generates only a
  single functional and technical ACK document for the original inbound X12 EDI
  document, not individual ACK documents for each post-split document.
- _API Limitations_: Direct invocation of a Transformer via
  `StartTransformerJob` API does not support splitting. Attempting
  to use `StartTransformerJob` to launch a Transformer that is
  configured to split input documents will result in an error.
- _Billing_: There are no extra charges for splitting an
  inbound X12 EDI document. You will be billed based on the original inbound X12
  EDI file and not the individual post-split X12 EDI files.
- _Exceeding Transaction Limits_: X12 EDI documents that
  contain more than 100 transactions will not be split, and AWS B2B Data Interchange will fail an
  attempt to process such documents, recording a relevant error message into your
  CloudWatch logs and emitting a relevant error event to EventBridge.

If you have an EDI file that contains more than 100 transactions, you have two
options:

- Pre-process the file and break it down into multiple EDI files, each
  containing no more than 100 transactions (recommended approach).
- Request an increase in the quota of the volume of transactions an EDI document
  could be split by. For more information on how to request a quota increase, see
  [Quotas for AWS B2B Data Interchange](b2bi-quotas.md "b2bi-quotas.md").

For more information about service quotas, see [Quotas for AWS B2B Data Interchange](b2bi-quotas.md "b2bi-quotas.md").
