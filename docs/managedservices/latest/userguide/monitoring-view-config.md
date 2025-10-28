# Viewing the monitoring configuration for an AMS account

There are two key parts to the monitoring configuration of an account that you can view:

- CloudWatch Alarms: You can view all the CW alarms in the account by going to the CloudWatch console
  and selecting different services of interest.
- CloudWatch Events:
  - **Multi-Account Landing Zone**: CloudWatch Events monitored in the account can be
    found by filtering for all CW event rules with the string `"ams-"`.
  - **Single-Account Landing Zone**: CloudWatch Events monitored in the account can be
    found by filtering for all CW event rules with the string `"mc-"`.
