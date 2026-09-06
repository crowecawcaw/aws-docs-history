

# emr-master-no-public-ip
<a name="emr-master-no-public-ip"></a>

Checks if Amazon EMR clusters' master nodes have public IPs. The rule is NON\_COMPLIANT if the master node has a public IP. 

**Note**  
This rule checks clusters that are in RUNNING or WAITING state. This rule requires you to enable recording for the `AWS::EC2::Instance` resource type in order to have an accurate evaluation.

**Identifier:** EMR\_MASTER\_NO\_PUBLIC\_IP

**Resource Types:** AWS::EMR::Cluster, AWS::EC2::Instance

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d809c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).