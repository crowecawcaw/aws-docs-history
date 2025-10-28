# Customer Managed mode

AWS Managed Services (AMS) Customer Managed mode provides a governance model that is flexible and can be adapted to your requirements.
This can be considered a fallback option for services and applications that AMS is unable to
operate for you. AMS does not operate infrastructure hosted in accounts created under this mode.
However, you can leverage centralized multi-account management in this mode. The following Multi-Account Landing Zone
features can be leveraged in this mode:

- Automated Account deployment
- Connectivity through Transit Gateway in networking account
- AMS Config Rules library
- Store copies of logs in logging account
- Aggregation of customer managed Guard Duty alerts to Security account
- Consolidated Billing
- Enablement of custom Service Control Policies.
  For example: If you want to run workloads on Ubuntu Pro, which is not an Operating System managed
  by AMS, you could use a customer managed account for hosting it. You can also consolidate workloads
  through customer managed accounts, to take advantage of the bulk discount on Reserved Instances/Sharing Plans
  available through sharing across an AWS organization.
