# Output file locations for files analyzed by conversational analytics

Following are examples of what the path looks like for conversational analytics output files when they are stored in the Amazon S3 bucket for
your instance.

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

###### Important

To delete a recording, you must delete the files for both the redacted and
unredacted recordings.
