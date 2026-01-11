# iam-user-mfa-enabled

Checks if the AWS Identity and Access Management (IAM) users have multi-factor authentication (MFA) enabled. The rule is NON_COMPLIANT if MFA is not enabled for at least one IAM user.

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

**Identifier:** IAM_USER_MFA_ENABLED

**Resource Types:** AWS::IAM::User

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
