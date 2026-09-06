

# AWS Managed Services - Accelerate in AWS GovCloud (US)
<a name="govcloud-ams-acc"></a>

AWS Managed Services - Accelerate is a service for configuring and managing your AWS infrastructure. For more information, see the [service description.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sd.html) 

## How AWS Managed Services - Accelerate differs
<a name="_how_aws_managed_services_accelerate_differs"></a>

The following differences apply to AWS Managed Services - Accelerate:
+ The following features are not available in AWS GovCloud (US) Regions:
  +  [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) 
  +  [Self-service reporting](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/self-service-reporting.html) - Patch and Backup daily reports are available. All other self-service reports are not available.
  +  [Enable AMS to use your own CloudTrail trail](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-onb-trail-choices.html) 
  +  [Cost optimization with AMS Resource Scheduler](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-resource-scheduler.html) 
  +  [Customer-provided tags](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-tag-cust-provided.html) 
  +  [Amazon Route 53 DNS firewall event monitoring in Service Incident Response](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/security-incident-response.html) 
  +  [Trusted Remediator](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/trusted-remediator.html) 
  +  [Amazon Route 53 Resolver DNS Firewall](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sec-data-protect.html#acc-sec-data-protect-r53) 
  +  [Monitoring and Incident Management for Amazon EKS](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-what-is-mon-inc-eks.html) 
  +  [AWS Config periodic recording for the AWS::EC2::Instance resource type](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sec-compliance.html#acc-sec-compliance-reduct-config-spend) 
  +  [Application aware incident notifications in AMS](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/app-aware-inc-notifications.html) 
+ The following features differ in AWS GovCloud (US) Regions:
  + Outbound [Service notifications](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/service-notices.html) are not sent to AWS account primary emails. Reports go to smaller, more targeted lists.
  + Accelerate [Compliance and conformance](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sec-compliance.html) is limited by the AWS Config managed rules available in your AWS Region.
+ Other AWS service differences that affect AWS Managed Services - Accelerate:
  + Not all [AWS Config in AWS GovCloud (US)](govcloud-config.md) managed rules are available in all Regions. The [Developer Guide](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) lists all managed rules, and the applicable Regions for each rule.
  + GuardDuty: For information about the differences in AWS GovCloud (US) Regions, see [Amazon GuardDuty in AWS GovCloud (US)](govcloud-guardduty.md).

## Documentation
<a name="govcloud-docs-81"></a>
+  [AWS Managed Services - Accelerate documentation](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/what-is.html) 

## Export-controlled content
<a name="govcloud-itar-content-120"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Resource names
+ Tags
+ Communications between customers and AWS Managed Services - Accelerate, such as service requests and incident reports.