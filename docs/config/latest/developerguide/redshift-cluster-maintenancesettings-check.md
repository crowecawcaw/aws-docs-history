# redshift-cluster-maintenancesettings-check

Checks if Amazon Redshift clusters have the specified maintenance settings. The rule is NON_COMPLIANT if the automatic upgrades to major version is disabled.

**Identifier:** REDSHIFT_CLUSTER_MAINTENANCESETTINGS_CHECK

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Mexico (Central) Region

**Parameters:**

allowVersionUpgrade
Type: boolean
Default: true

Allow version upgrade is enabled.

preferredMaintenanceWindow (Optional)
Type: String

Scheduled maintenance window for clusters (for example, Mon:09:30-Mon:10:00).

automatedSnapshotRetentionPeriod (Optional)
Type: int
Default: 1

Number of days to retain automated snapshots.

## Proactive Evaluation

For steps on how to run this rule in proactive mode,
see [Evaluating Your Resources with AWS Config Rules](evaluating-your-resources.md#evaluating-your-resources-proactive "evaluating-your-resources.md#evaluating-your-resources-proactive").
For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](../APIReference/API_StartResourceEvaluation.md "../APIReference/API_StartResourceEvaluation.md") API needs to include the following inputs, encoded as a string:

```
"ResourceConfiguration":
...
{
    "AutomatedSnapshotRetentionPeriod": `Integer`\*,
    "PreferredMaintenanceWindow": `String`\*,
    "AllowVersionUpgrade": `BOOLEAN`\*
}
...

```

\*For more information on valid values for these inputs, see [AutomatedSnapshotRetentionPeriod](../../../AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.md#cfn-redshift-cluster-automatedsnapshotretentionperiod "../../../AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.md#cfn-redshift-cluster-automatedsnapshotretentionperiod"), [PreferredMaintenanceWindow](../../../AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.md#cfn-redshift-cluster-preferredmaintenancewindow "../../../AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.md#cfn-redshift-cluster-preferredmaintenancewindow"), and [AllowVersionUpgrade](../../../AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.md#cfn-redshift-cluster-allowversionupgrade "../../../AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.md#cfn-redshift-cluster-allowversionupgrade") in the AWS CloudFormation User Guide.

For more information on proactive evaluation, see [Evaluation Mode](evaluate-config-rules.md "evaluate-config-rules.md").

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
