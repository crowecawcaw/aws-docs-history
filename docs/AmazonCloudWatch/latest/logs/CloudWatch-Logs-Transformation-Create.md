# Create and manage log

transformers

A log transformer includes one or more _processors_ that are in a
logical pipeline together. Each processor is applied to a log event, one after the other
in the order that they are listed in the transformer configuration.

Some processors are of the _parser_ type. Each transformer must
have at least one parser, and the first processor in a transformer must be a
parser.

Some of the parsers are built-in parsers that are configured for a certain type of
AWS vended log.

Other processor types are string mutators, JSON mutators, and data processors.

You can create transformers for individual log groups, and you can also create
account-level transformers that apply to all or many log groups in your account. If a
log group has a log group-level transformer, that transformer overrides any
account-level transformer that would otherwise apply to that log group. You can have as
many as 20 account-level transformers in a Region in your account.

You must follow these guidelines when you create a transformer:

- If you include a pre-configured parser for a type of AWS vended logs, it
  must be the first processor listed in the transformer. You can include only one
  such processor in a transformer.
- You can include only one `grok` processor in a transformer.
- You must have at least one parser-type processor in a transformer. You can
  include as many as five parser-type processors. This limit of five includes both
  built-in parsers and configurable parsers.
- You can have as many as 20 processors in a transformer.
- You can include only one **addKeys** processor in a
  transformer.
- You can include only one **copyValue** processor in a
  transformer.
- Each transformer can extract up to 200 fields from a log event.
- Each log event **MUST** be below 512KB. Total size of log events can still go over 512KB.
  For more information about all supported processors and their syntax, see [Processors that you can
  use](CloudWatch-Logs-Transformation-Processors.md "CloudWatch-Logs-Transformation-Processors.md").

###### Topics

- [Create an
  account-level transformer policy](CloudWatchLogs-Transformer-CreateAccountLevel.md "CloudWatchLogs-Transformer-CreateAccountLevel.md")
- [Edit or delete an
  account-level transformer policy](CloudWatchLogs-Transformer-EditAccountLevel.md "CloudWatchLogs-Transformer-EditAccountLevel.md")
- [Create a log-group-level
  log transformer from scratch](CloudWatch-Logs-Transformation-CreateNew.md "CloudWatch-Logs-Transformation-CreateNew.md")
- [Create a log-group-level
  transformer by copying an existing one](CloudWatch-Logs-Transformation-Copy.md "CloudWatch-Logs-Transformation-Copy.md")
- [Edit a log-group-level
  transformer](CloudWatch-Logs-Transformation-Edit.md "CloudWatch-Logs-Transformation-Edit.md")
- [Delete a log-group-level
  transformer](CloudWatch-Logs-Transformation-Delete.md "CloudWatch-Logs-Transformation-Delete.md")
