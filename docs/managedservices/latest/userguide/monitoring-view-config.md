End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](SunsetPlan.md "SunsetPlan.md").

# Viewing the monitoring configuration for an AMS account

There are two key parts to the monitoring configuration of an account that you can view:

- CloudWatch Alarms: You can view all the CW alarms in the account by going to the CloudWatch console
  and selecting different services of interest.
- CloudWatch Events:

  - **Multi-Account Landing Zone**: CloudWatch Events monitored in the account can be
    found by filtering for all CW event rules with the string `"ams-"`.
  - **Single-Account Landing Zone**: CloudWatch Events monitored in the account can be
    found by filtering for all CW event rules with the string `"mc-"`.
