

# ebs-snapshot-public-restorable-check
<a name="ebs-snapshot-public-restorable-check"></a>

Checks if Amazon Elastic Block Store (Amazon EBS) snapshots are not publicly restorable. The rule is NON\_COMPLIANT if one or more individual snapshots with RestorableByUserIds field are set to all. 



**Identifier:** EBS\_SNAPSHOT\_PUBLIC\_RESTORABLE\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Europe (Spain) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d531c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).