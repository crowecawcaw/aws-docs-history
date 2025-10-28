# codedeploy-ec2-minimum-healthy-hosts-configured

Checks if the deployment group for EC2/On-Premises Compute Platform is configured with a minimum healthy hosts fleet percentage or host count greater than or equal to the input threshold. The rule is NON_COMPLIANT if either is below the threshold.

**Identifier:** CODEDEPLOY_EC2_MINIMUM_HEALTHY_HOSTS_CONFIGURED

**Resource Types:** AWS::CodeDeploy::DeploymentGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

minimumHealthyHostsFleetPercent (Optional)
Type: int
Default: 66

Minimum percentage of healthy hosts fleet during deployment. Default value is set to 66 percent.

minimumHealthyHostsHostCount (Optional)
Type: int
Default: 1

Minimum number of healthy hosts in fleet during deployment. Default value is set to 1.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
