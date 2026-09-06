

# root-account-hardware-mfa-enabled
<a name="root-account-hardware-mfa-enabled"></a>

Checks if your AWS account is enabled to use multi-factor authentication (MFA) hardware device to sign in with root credentials. The rule is NON\_COMPLIANT if any virtual MFA devices are permitted for signing in with root credentials.

**Note**  
**Not Applicable for Accounts Without Root User Credentials**  
This rule returns `NOT_APPLICABLE` if root user credentials are not present.  
**Managed Rules and Global IAM Resource Types**  
The global IAM resource types onboarded before February 2022 (`AWS::IAM::Group`, `AWS::IAM::Policy`, `AWS::IAM::Role`, and `AWS::IAM::User`) can only be recorded by AWS Config in AWS Regions where AWS Config was available before February 2022. These resource types cannot be recorded in Regions supported by AWS Config after February 2022. For a list of those Regions, see [Recording AWS Resources \| Global Resources](https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html#select-resources-all).  
If you record a global IAM resource type in at least one Region, periodic rules that report compliance on the global IAM resource type will run evaluations in all Regions where the periodic rule is added, even if you have not enabled the recording of the global IAM resource type in the Region where the periodic rule was added.  
To avoid unnecessary evaluations, you should only deploy periodic rules that report compliance on a global IAM resource type to one of the supported Regions. For a list of which managed rules are supported in which Regions, see [List of AWS Config Managed Rules by Region Availability](https://docs.aws.amazon.com/config/latest/developerguide/managing-rules-by-region-availability.html).



**Identifier:** ROOT\_ACCOUNT\_HARDWARE\_MFA\_ENABLED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1341c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).