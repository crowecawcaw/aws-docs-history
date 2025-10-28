# AWS CloudFormation Ingest: Examples

Find here some detailed examples of how to use the **Create stack with CloudFormation template** change type.

To download a set of sample CloudFormation templates per AWS Region, see
[Sample Templates](../../../AWSCloudFormation/latest/UserGuide/cfn-sample-templates.md "../../../AWSCloudFormation/latest/UserGuide/cfn-sample-templates.md").

For reference information on AWS CloudFormation resources, see
[AWS Resource and Property Types Reference](../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md "../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md").
However, AMS supports a smaller set of resources, which are described in [AMS CloudFormation ingest](ams-cfn-ingest.md "ams-cfn-ingest.md").

###### Note

AMS advises you to gather all IAM or other policy-related resources and submit them in a single Management | Other | Other | Create
change type (ct-1e1xtak34nx76). For example, combine all needed IAM roles, IAM instance profiles, IAM policy updates for existing IAM roles,
S3 bucket policies, SNS/SQS policies, and so forth, and then submit a ct-1e1xtak34nx76 RFC so that these pre-existing resources can be referenced inside
the future CFN Ingest templates.

###### Topics

- [AWS CloudFormation Ingest examples: Defining resources](cfn-ingest-ex-define-resource.md "cfn-ingest-ex-define-resource.md")
- [CloudFormation Ingest examples: 3-tier Web application](cfn-ingest-ex-3-tier.md "cfn-ingest-ex-3-tier.md")
