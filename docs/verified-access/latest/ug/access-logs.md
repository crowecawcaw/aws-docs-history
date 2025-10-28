# Verified Access logs

After AWS Verified Access evaluates each access request, it logs all access attempts. This provides you
with centralized visibility into application access, and helps you quickly respond to
security incidents and audit requests. Verified Access supports the Open Cybersecurity Schema
Framework (OCSF) logging format.

When you enable logging, you need to configure a destination for the logs to be sent. The
IAM principal being used to configure the logging destination needs to have certain
permissions for logging to work properly. The required IAM permissions for each logging
destination can be seen in the [Verified Access logging permissions](access-logs-permissions.md "access-logs-permissions.md") section. Verified Access supports the following
destinations for publishing access logs:

- Amazon CloudWatch Logs log groups
- Amazon S3 buckets
- Amazon Data Firehose delivery streams

###### Contents

- [Verified Access logging versions](logging-versions.md "logging-versions.md")
- [Verified Access logging permissions](access-logs-permissions.md "access-logs-permissions.md")
- [Enable or disable Verified Access logs](access-logs-enable.md "access-logs-enable.md")
- [Enable or disable Verified Access trust context](include-trust-context.md "include-trust-context.md")
- [OCSF version 0.1 log examples for Verified Access](ocsfv01-examples.md "ocsfv01-examples.md")
- [OCSF version 1.0.0-rc.2 log examples for
  Verified Access](ocsfv1-examples.md "ocsfv1-examples.md")
