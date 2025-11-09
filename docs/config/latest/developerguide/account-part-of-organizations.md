# account-part-of-organizations

Checks if an AWS account is part of AWS Organizations. The rule is NON_COMPLIANT if an AWS account is not part of AWS Organizations or AWS Organizations master account ID does not match rule parameter `MasterAccountId`.

###### Note

**Managed Rules and Global IAM Resource Types**

The global IAM resource types onboarded before February 2022
(`AWS::IAM::Group`, `AWS::IAM::Policy`, `AWS::IAM::Role`, and `AWS::IAM::User`)
can only be recorded by AWS Config in AWS Regions where AWS Config was available before February 2022.
These resource types cannot be recorded in Regions supported by AWS Config after February 2022.
For a list of those Regions,
see [Recording AWS Resources | Global Resources](select-resources.md#select-resources-all "select-resources.md#select-resources-all").

If you record a global IAM resource type in at least one Region,
periodic rules that report compliance on the global IAM resource type will run evaluations in all Regions
where the periodic rule is added, even if you have not enabled the recording of the global IAM resource type
in the Region where the periodic rule was added.

To avoid unnecessary evaluations, you should only deploy periodic rules that report compliance on a global IAM resource type to one of the supported Regions.
For a list of which managed rules are supported in which Regions,
see [List of AWS Config Managed Rules by Region Availability](managing-rules-by-region-availability.md "managing-rules-by-region-availability.md").

**Identifier:** ACCOUNT_PART_OF_ORGANIZATIONS

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), AWS Secret - West Region

**Parameters:**

MasterAccountId (Optional)
Type: String

The master account ID for an AWS account.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
