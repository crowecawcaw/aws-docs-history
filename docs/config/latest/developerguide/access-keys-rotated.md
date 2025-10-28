# access-keys-rotated

Checks if active IAM access keys are rotated (changed) within the number of days specified in `maxAccessKeyAge`. The rule is NON_COMPLIANT if access keys are not rotated within the specified time period. The default value is 90 days.

###### Warning

Do not provide your access keys to unauthorized parties, even to help [find your account identifiers](../../../general/latest/gr/acct-identifiers.md "../../../general/latest/gr/acct-identifiers.md"). By doing this, you might give someone permanent access to your account. The security [best practice](../../../accounts/latest/reference/best-practices.md "../../../accounts/latest/reference/best-practices.md") is to remove passwords and access keys when users no longer need them.

###### Note

**Resource Type Marked as Noncompliant in the Console**

If this rule finds that any of your access keys are noncompliant, the `AWS::IAM::User` resource type will also be marked as noncompliant in the AWS console.

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

**Limitations**

This rule does not apply to AWS account root user access keys. To delete or rotate your root user access keys, use your root user credentials to sign in to the My Security Credentials page in the AWS Management Console at [https://aws.amazon.com/console/](https://aws.amazon.com/console/ "https://aws.amazon.com/console/").

**Identifier:** ACCESS_KEYS_ROTATED

**Resource Types:** AWS::IAM::User

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), Middle East (UAE), AWS Secret - West, Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

maxAccessKeyAge
Type: int
Default: 90

Maximum number of days without rotation. Default 90.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
