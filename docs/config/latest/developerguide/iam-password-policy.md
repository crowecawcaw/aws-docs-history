

# iam-password-policy
<a name="iam-password-policy"></a>

Checks if the account password policy for AWS Identity and Access Management (IAM) users meets the specified requirements indicated in the parameters. The rule is NON\_COMPLIANT if the account password policy does not meet the specified requirements. 

**Important**  
The `true` and `false` values for the rule parameters are case-sensitive. If `true` is not provided in lowercase, it will be treated as `false.`

**Note**  
**Evaluation Result for the Default IAM Password Policy**  
This rule is marked as NON\_COMPLIANT when the default IAM password policy is used.  
**Managed Rules and Global IAM Resource Types**  
The global IAM resource types onboarded before February 2022 (`AWS::IAM::Group`, `AWS::IAM::Policy`, `AWS::IAM::Role`, and `AWS::IAM::User`) can only be recorded by AWS Config in AWS Regions where AWS Config was available before February 2022. These resource types cannot be recorded in Regions supported by AWS Config after February 2022. For a list of those Regions, see [Recording AWS Resources \| Global Resources](https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html#select-resources-all).  
If you record a global IAM resource type in at least one Region, periodic rules that report compliance on the global IAM resource type will run evaluations in all Regions where the periodic rule is added, even if you have not enabled the recording of the global IAM resource type in the Region where the periodic rule was added.  
To avoid unnecessary evaluations, you should only deploy periodic rules that report compliance on a global IAM resource type to one of the supported Regions. For a list of which managed rules are supported in which Regions, see [List of AWS Config Managed Rules by Region Availability](https://docs.aws.amazon.com/config/latest/developerguide/managing-rules-by-region-availability.html).

**Identifier:** IAM\_PASSWORD\_POLICY

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

RequireUppercaseCharacters (Optional)Type: booleanDefault: true  
Require at least one uppercase character in password.

RequireLowercaseCharacters (Optional)Type: booleanDefault: true  
Require at least one lowercase character in password.

RequireSymbols (Optional)Type: booleanDefault: true  
Require at least one symbol in password.

RequireNumbers (Optional)Type: booleanDefault: true  
Require at least one number in password.

MinimumPasswordLength (Optional)Type: intDefault: 14  
Password minimum length.

PasswordReusePrevention (Optional)Type: intDefault: 24  
Number of passwords before allowing reuse.

MaxPasswordAge (Optional)Type: intDefault: 90  
Number of days before password expiration.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d929c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).