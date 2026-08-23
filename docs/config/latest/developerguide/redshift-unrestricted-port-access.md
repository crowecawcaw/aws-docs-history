# redshift-unrestricted-port-access

Checks if security groups associated with an Amazon Redshift cluster have inbound rules that allow unrestricted incoming traffic. The rule is NON\_COMPLIANT if there are inbound rules that allow unrestricted incoming traffic to the Redshift cluster port.

**Identifier:** REDSHIFT\_UNRESTRICTED\_PORT\_ACCESS

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
