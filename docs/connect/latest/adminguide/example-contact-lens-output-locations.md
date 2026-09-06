# Output file locations for files analyzed by conversational analytics

Following are examples of what the path looks like for conversational analytics output files when they are stored in the Amazon S3 bucket for
your instance.

###### Timestamp in the file path

The date and timestamp in the output file path correspond to the
`ConnectedToAgentTimestamp`, not the
`InitiationTimestamp`. If the contact spans a UTC day boundary,
the file appears under the date when the agent connected, not the date when
the contact started.

- Original analyzed transcript file (JSON)

  - /connect-instance-
    bucket/**Analysis/Voice**/2020/02/04/`contact's_ID`\_analysis\_2020-02-04T21:14:16Z.json
  - /connect-instance-
    bucket/**Analysis/Chat**/2020/02/04/`contact's_ID`\_analysis\_2020-02-04T21:14:16Z.json
  - /connect-instance-
    bucket/**Analysis/Email**/2026/03/10/`contact's_ID`\_analysis\_20260310T22:35\_UTC.json

- Redacted analyzed transcript file in (JSON)

  - /connect-instance-
    bucket/**Analysis/Voice/Redacted**/2020/02/04/`contact's_ID`\_**analysis\_redacted**\_2020-02-04T21:14:16Z.json
  - /connect-instance-
    bucket/**Analysis/Chat/Redacted**/2020/02/04/`contact's_ID`\_**analysis\_redacted**\_2020-02-04T21:14:16Z.json
  - /connect-instance-
    bucket/**Analysis/Email/Redacted**/2026/03/10/`contact's_ID`\_**analysis\_redacted**\_20260310T22:35\_UTC.json

- Redacted audio file

  - /connect-instance-
    bucket/**Analysis/Voice/Redacted**/2020/02/04/`contact's_ID`\_**call\_recording\_redacted**\_2020-02-04T21:14:16Z.**wav**

###### Deleting recordings

To fully remove a recording, you must delete both the redacted and
unredacted files. If you delete only one version, the other version remains
accessible.
