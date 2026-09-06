

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Best Practices
<a name="cfn-ingest-best-practices"></a>

Following are some best practices you can use to migrate resources using the AMS CloudFormation ingest process:
+ **Submit IAM and other policy-related resources in one CT**– If you can use automated CTs such as CloudFormation Ingest to deploy IAM roles, we recommend you do so. In other cases, AMS recommends that you gather all IAM or other policy-related resources and submit them in a single Management \| Other \| Other \| Create change type (ct-1e1xtak34nx76). For example, combine needed all IAM roles, IAM Amazon EC2 instance profiles, IAM policy updates for existing IAM roles, Amazon S3 bucket policies, Amazon SNS/Amazon SQS policies, and so forth, and submit a ct-1e1xtak34nx76 RFC so that these pre-existing resources can simply be referenced inside the future CloudFormation ingest templates.
+ **EC2 instances are bootstrapped and successfully joined to the domain** – This is done automatically as a best practice. To ensure that the Amazon EC2 instances launched via a CloudFormation ingest stack are bootstrapped and join the domain successfully, AMS includes a CreationPolicy and an UpdatePolicy for an Auto Scaling group resource (that is, if these policies don't already exist).
+ **Amazon RDS DB instance parameter must be specified**– When creating an Amazon RDS database via CloudFormation ingest, you must specify the `DBSnapshotIdentifier` parameter in order to restore from a previous DB snapshot. This is required because CloudFormation ingest does not currently handle sensitive data.

For an example of how to use a CloudFormation template for AMS CloudFormation template ingest, see [CloudFormation Ingest: Examples](cfn-ingest-examples.md).