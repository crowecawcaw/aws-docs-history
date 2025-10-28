# Log Archive account

The Log Archive account serves as the central hub for archiving logs across your AMS multi-account landing zone
environment. There is an S3 bucket in the account that contains copies of AWS CloudTrail and
AWS Config log files from each of the AMS multi-account landing zone environment accounts.
You could use this account for your Centralised Logging solution with AWS Firehose, or Splunk, and so forth.
AMS access to this account is limited to a few users; restricted to auditors and security teams for compliance and
forensic investigations related to account activity.

![Log Archive Account diagram showing Aggregated CloudTrail Logs and Aggregated Config Logs icons.](images/malzLogAccount.png)
