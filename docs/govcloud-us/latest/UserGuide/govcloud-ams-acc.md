# AWS Managed Services - AMS Accelerate in AWS GovCloud (US)

AMS Accelerate is a service for configuring and managing your AWS infrastructure. For
more information, see the [service
description.](../../../managedservices/latest/accelerate-guide/acc-sd.md "../../../managedservices/latest/accelerate-guide/acc-sd.md")

## How AMS Accelerate differs for AWS GovCloud (US)

Some services available in other AWS Regions are not available or have limitations
in AWS GovCloud (US) Regions.

- Not supported in AWS GovCloud (US) Regions:
  - [Amazon Macie](../../../macie/latest/user/what-is-macie.md "../../../macie/latest/user/what-is-macie.md")
  - [Self-service reporting](../../../managedservices/latest/accelerate-guide/self-service-reporting.md "../../../managedservices/latest/accelerate-guide/self-service-reporting.md")
  - [Enable AMS to use your own CloudTrail trail](../../../managedservices/latest/accelerate-guide/acc-onb-trail-choices.md "../../../managedservices/latest/accelerate-guide/acc-onb-trail-choices.md")
  - [Cost optimization with AMS Resource Scheduler](../../../managedservices/latest/accelerate-guide/acc-resource-scheduler.md "../../../managedservices/latest/accelerate-guide/acc-resource-scheduler.md")
  - [Customer-provided tags](../../../managedservices/latest/accelerate-guide/acc-tag-cust-provided.md "../../../managedservices/latest/accelerate-guide/acc-tag-cust-provided.md")
  - [Amazon Route 53 DNS firewall event monitoring in Service Incident Response](../../../managedservices/latest/accelerate-guide/security-incident-response.md "../../../managedservices/latest/accelerate-guide/security-incident-response.md")
  - [Trusted Remediator](../../../managedservices/latest/accelerate-guide/trusted-remediator.md "../../../managedservices/latest/accelerate-guide/trusted-remediator.md")
  - [Amazon Route 53 Resolver DNS Firewall](../../../managedservices/latest/accelerate-guide/acc-sec-data-protect.md#acc-sec-data-protect-r53 "../../../managedservices/latest/accelerate-guide/acc-sec-data-protect.md#acc-sec-data-protect-r53")
  - [Monitoring and Incident Management for Amazon EKS](../../../managedservices/latest/accelerate-guide/acc-what-is-mon-inc-eks.md "../../../managedservices/latest/accelerate-guide/acc-what-is-mon-inc-eks.md")
  - [AWS Config periodic recording for the AWS::EC2::Instance resource type](../../../managedservices/latest/accelerate-guide/acc-sec-compliance.md#acc-sec-compliance-reduct-config-spend "../../../managedservices/latest/accelerate-guide/acc-sec-compliance.md#acc-sec-compliance-reduct-config-spend")
  - [Application aware incident notifications in AMS](../../../managedservices/latest/accelerate-guide/app-aware-inc-notifications.md "../../../managedservices/latest/accelerate-guide/app-aware-inc-notifications.md")

- Different in AWS GovCloud (US) Regions:
  - Outbound [Service notifications](../../../managedservices/latest/accelerate-guide/service-notices.md "../../../managedservices/latest/accelerate-guide/service-notices.md") are not sent to AWS account primary
    emails. Reports go to smaller, more targeted lists.
  - Accelerate [Compliance and conformance](../../../managedservices/latest/accelerate-guide/acc-sec-compliance.md "../../../managedservices/latest/accelerate-guide/acc-sec-compliance.md") is limited by the AWS Config
    managed rules available in your AWS Region.

- Differences in other AWS services. Some examples:
  - Not all [AWS Config in AWS GovCloud (US)](govcloud-config.md "govcloud-config.md") managed rules are available in all
    Regions. The [Developer Guide](../../../config/latest/developerguide/managed-rules-by-aws-config.md "../../../config/latest/developerguide/managed-rules-by-aws-config.md") lists all managed rules, and the applicable
    Regions for each rule.
  - GuardDuty: For information about the differences in
    AWS GovCloud (US) Regions, see [Amazon GuardDuty in AWS GovCloud (US)](govcloud-guardduty.md "govcloud-guardduty.md").

## Documentation for AMS Accelerate

For information, see the [AMS Accelerate
documentation](../../../managedservices/latest/accelerate-guide/what-is.md "../../../managedservices/latest/accelerate-guide/what-is.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Resource names
- Tags
- Communications between customers and AMS Accelerate, such as service requests
  and incident reports.
