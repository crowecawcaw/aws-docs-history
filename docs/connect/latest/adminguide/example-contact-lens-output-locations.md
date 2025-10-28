# Output file locations for

files analyzed by Contact Lens conversational analytics

Following are examples of what the path looks like for Contact Lens
conversational analytics output files when they are stored in the Amazon S3 bucket for
your instance.

- Original analyzed transcript file (JSON)
  - /connect-instance-
    bucket/**Analysis/Voice**/2020/02/04/`contact's_ID`\_analysis_2020-02-04T21:14:16Z.json
  - /connect-instance-
    bucket/**Analysis/Chat**/2020/02/04/`contact's_ID`\_analysis_2020-02-04T21:14:16Z.json

- Redacted analyzed transcript file in (JSON)
  - /connect-instance-
    bucket/**Analysis/Voice/Redacted**/2020/02/04/`contact's_ID`\_**analysis_redacted**\_2020-02-04T21:14:16Z.json
  - /connect-instance-
    bucket/**Analysis/Chat/Redacted**/2020/02/04/`contact's_ID`\_**analysis_redacted**\_2020-02-04T21:14:16Z.json

- Redacted audio file
  - /connect-instance-
    bucket/**Analysis/Voice/Redacted**/2020/02/04/`contact's_ID`\_**call_recording_redacted**\_2020-02-04T21:14:16Z.**wav**

###### Important

To delete a recording, you must delete the files for both the redacted and
unredacted recordings.
