# Systems Manager Automation Runbook Reference

To help you get started quickly, AWS Systems Manager provides predefined runbooks. These runbooks
are maintained by Amazon Web Services, AWS Support, and AWS Config. The Runbook Reference describes each of
the predefined runbooks provided by Systems Manager, Support, and AWS Config.

###### Important

If you run an automation workflow that invokes other services by using an AWS Identity and Access Management
(IAM) service role, be aware that the service role must be configured with
permission to invoke those services. This requirement applies to all AWS
Automation runbooks (`AWS-*` runbooks) such as the
`AWS-ConfigureS3BucketLogging`,
`AWS-CreateDynamoDBBackup`, and
`AWS-RestartEC2Instance` runbooks, to name a few. This
requirement also applies to any custom Automation runbooks you create that
invoke other AWS services by using actions that call other services. For
example, if you use the `aws:executeAwsApi`,
`aws:createStack`, or `aws:copyImage` actions, then
you must configure the service role with permission to
invoke those services. You can enable permissions to other AWS services by
adding an IAM inline policy to the role. For more information, see [Add an Automation inline policy to invoke other AWS services](../../../systems-manager/latest/userguide/automation-permissions.md#automation-role-add-inline-policy "../../../systems-manager/latest/userguide/automation-permissions.md#automation-role-add-inline-policy").

This reference includes topics that describe each of the Systems Manager runbooks that are owned by
AWS, AWS Support, and AWS Config. Runbooks are organized by the relevant AWS service. Each page
provides an explanation of the required and optional parameters that you can specify when
using the runbook. Each page also lists the steps in the runbook and the output of the
automation, if any.

This reference does _not_ include a separate page for runbooks that
require approval such as the `AWS-CreateManagedLinuxInstanceWithApproval` or
`AWS-StopEC2InstanceWithApproval` runbook. Any runbook name that includes
`WithApproval`, means the runbook includes the [`aws:approve`](../../../systems-manager/latest/userguide/automation-action-approve.md "../../../systems-manager/latest/userguide/automation-action-approve.md") action. This action temporarily pauses an automation until designated principals
either approve or reject the action. After the required number of approvals is reached, the
automation resumes.

For information about running automations, see [Running a simple automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md"). For information about running automations on multiple targets, see
[Running automations that use targets and rate controls](../../../systems-manager/latest/userguide/automation-working-targets-and-rate-controls.md "../../../systems-manager/latest/userguide/automation-working-targets-and-rate-controls.md").

###### Topics

- [View runbook content](#view-automation-json "#view-automation-json")
- [API Gateway](automation-ref-abp.md "automation-ref-abp.md")
- [AWS Batch](automation-ref-batch.md "automation-ref-batch.md")
- [CloudFormation](automation-ref-cfn.md "automation-ref-cfn.md")
- [CloudFront](automation-ref-cf.md "automation-ref-cf.md")
- [CloudTrail](automation-ref-ct.md "automation-ref-ct.md")
- [CloudWatch](automation-ref-cw.md "automation-ref-cw.md")
- [Amazon DocumentDB](automation-ref-docdb.md "automation-ref-docdb.md")
- [CodeBuild](automation-ref-acb.md "automation-ref-acb.md")
- [AWS CodeDeploy](automation-ref-acd.md "automation-ref-acd.md")
- [AWS Config](automation-ref-cc.md "automation-ref-cc.md")
- [Amazon Connect](automation-ref-con.md "automation-ref-con.md")
- [AWS Directory Service](automation-ref-ads.md "automation-ref-ads.md")
- [AWS AppSync](automation-ref-apsy.md "automation-ref-apsy.md")
- [Amazon Athena](automation-ref-ate.md "automation-ref-ate.md")
- [DynamoDB](automation-ref-ddb.md "automation-ref-ddb.md")
- [AWS Database Migration Service](automation-ref-dms.md "automation-ref-dms.md")
- [Amazon EBS](automation-ref-ebs.md "automation-ref-ebs.md")
- [Amazon EC2](automation-ref-ec2.md "automation-ref-ec2.md")
- [Amazon ECS](automation-ref-ecs.md "automation-ref-ecs.md")
- [Amazon EFS](automation-ref-efs.md "automation-ref-efs.md")
- [Amazon EKS](automation-ref-eks.md "automation-ref-eks.md")
- [Elastic Beanstalk](automation-ref-aeb.md "automation-ref-aeb.md")
- [ELB](automation-ref-elb.md "automation-ref-elb.md")
- [Amazon EMR](automation-ref-emr.md "automation-ref-emr.md")
- [Amazon OpenSearch Service](automation-ref-opensearch.md "automation-ref-opensearch.md")
- [EventBridge](automation-ref-ev.md "automation-ref-ev.md")
- [AWS Glue](automation-ref-glu.md "automation-ref-glu.md")
- [Amazon FSx](automation-ref-fsx.md "automation-ref-fsx.md")
- [GuardDuty](automation-ref-gdu.md "automation-ref-gdu.md")
- [IAM](automation-ref-iam.md "automation-ref-iam.md")
- [Incident Detection and Response](automation-ref-idr.md "automation-ref-idr.md")
- [Amazon Kinesis Data Streams](automation-ref-aks.md "automation-ref-aks.md")
- [AWS KMS](automation-ref-kms.md "automation-ref-kms.md")
- [Lambda](automation-ref-lam.md "automation-ref-lam.md")
- [Amazon Managed Workflows for Apache Airflow](automation-ref-mwaa.md "automation-ref-mwaa.md")
- [Neptune](automation-ref-neptune.md "automation-ref-neptune.md")
- [Amazon RDS](automation-ref-rds.md "automation-ref-rds.md")
- [Amazon Redshift](automation-ref-rs.md "automation-ref-rs.md")
- [Amazon S3](automation-ref-s3.md "automation-ref-s3.md")
- [Amazon SES](automation-ref-ses.md "automation-ref-ses.md")
- [SageMaker AI](automation-ref-sm.md "automation-ref-sm.md")
- [Secrets Manager](automation-ref-asm.md "automation-ref-asm.md")
- [Security Hub](automation-ref-ash.md "automation-ref-ash.md")
- [AWS Shield](automation-ref-shd.md "automation-ref-shd.md")
- [Amazon SNS](automation-ref-sns.md "automation-ref-sns.md")
- [Amazon SQS](automation-ref-sqs.md "automation-ref-sqs.md")
- [Step Functions](automation-ref-sfn.md "automation-ref-sfn.md")
- [Systems Manager](automation-ref-sys.md "automation-ref-sys.md")
- [Third-party](automation-ref-third-party.md "automation-ref-third-party.md")
- [Amazon VPC](automation-ref-vpc.md "automation-ref-vpc.md")
- [AWS WAF](automation-ref-waf.md "automation-ref-waf.md")
- [Amazon WorkSpaces](automation-ref-wsp.md "automation-ref-wsp.md")
- [X-Ray](automation-ref-xray.md "automation-ref-xray.md")

## View runbook content

You can view the content for runbooks in the Systems Manager console.

###### To view runbook content

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Documents**.

-or-

If the AWS Systems Manager home page opens first, choose the menu icon (
![Horizontal black and white striped pattern forming a simple geometric design.](images/menu-icon-small.png)
) to open the
navigation pane, and then choose **Documents** in the navigation
pane. 3. In the **Categories** section, choose **Automation
documents**. 4. Choose a runbook, and then choose **View details**. 5. Choose the **Content** tab.
