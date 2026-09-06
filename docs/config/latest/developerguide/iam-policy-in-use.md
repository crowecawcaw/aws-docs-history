

# iam-policy-in-use
<a name="iam-policy-in-use"></a>

Checks whether the IAM policy ARN is attached to an IAM user, or a group with one or more IAM users, or an IAM role with one or more trusted entity. 

**Note**  
**Managed Rules and Global IAM Resource Types**  
The global IAM resource types onboarded before February 2022 (`AWS::IAM::Group`, `AWS::IAM::Policy`, `AWS::IAM::Role`, and `AWS::IAM::User`) can only be recorded by AWS Config in AWS Regions where AWS Config was available before February 2022. These resource types cannot be recorded in Regions supported by AWS Config after February 2022. For a list of those Regions, see [Recording AWS Resources \| Global Resources](https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html#select-resources-all).  
If you record a global IAM resource type in at least one Region, periodic rules that report compliance on the global IAM resource type will run evaluations in all Regions where the periodic rule is added, even if you have not enabled the recording of the global IAM resource type in the Region where the periodic rule was added.  
To avoid unnecessary evaluations, you should only deploy periodic rules that report compliance on a global IAM resource type to one of the supported Regions. For a list of which managed rules are supported in which Regions, see [List of AWS Config Managed Rules by Region Availability](https://docs.aws.amazon.com/config/latest/developerguide/managing-rules-by-region-availability.html).

**Identifier:** IAM\_POLICY\_IN\_USE

**Resource Types:** AWS::::Account

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

policyARNType: String  
An IAM policy ARN to be checked.

policyUsageType (Optional)Type: String  
Specify whether you expect the policy to be attached to an IAM user, group or role. Valid values are IAM\_USER, IAM\_GROUP, IAM\_ROLE, or ANY. Default value is ANY.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d935c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).