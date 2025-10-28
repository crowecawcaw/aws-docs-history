# ec2-managedinstance-applications-blacklisted

Checks if none of the specified applications are installed on the instance. Optionally, specify the version. Newer versions will not be denylisted. Optionally, specify the platform to apply the rule only to instances running that platform.

**Identifier:** EC2_MANAGEDINSTANCE_APPLICATIONS_BLACKLISTED

**Resource Types:** AWS::SSM::ManagedInstanceInventory

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS Secret - West, Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

applicationNames
Type: CSV

Comma-separated list of application names. Optionally, specify versions appended with ':' (for example, 'Chrome:0.5.3, Firefox').

###### Note

The application names must be an exact match. For example, use `firefox` on Linux or `firefox-compat`
on Amazon Linux. In addition, AWS Config does not currently support wildcards for the _applicationNames_ parameter (for example, `firefox*`).

platformType (Optional)
Type: String

Platform type (for example, 'Linux' or 'Windows').

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
