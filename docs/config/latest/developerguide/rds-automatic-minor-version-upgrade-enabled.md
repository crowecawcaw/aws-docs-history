# rds-automatic-minor-version-upgrade-enabled

Checks if Amazon Relational Database Service (RDS) database instances are configured for automatic minor version upgrades. The rule is NON_COMPLIANT if the value of 'autoMinorVersionUpgrade' is false.

**Identifier:** RDS_AUTOMATIC_MINOR_VERSION_UPGRADE_ENABLED

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## Proactive Evaluation

For steps on how to run this rule in proactive mode,
see [Evaluating Your Resources with AWS Config Rules](evaluating-your-resources.md#evaluating-your-resources-proactive "evaluating-your-resources.md#evaluating-your-resources-proactive").
For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](../APIReference/API_StartResourceEvaluation.md "../APIReference/API_StartResourceEvaluation.md") API needs to include the following inputs, encoded as a string:

```
"ResourceConfiguration":
...
{
    "AutoMinorVersionUpgrade": `BOOLEAN`\*,
    "Engine": `String`\*
}
...

```

\*For more information on valid values for these inputs, see [AutoMinorVersionUpgrade](../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.md#cfn-rds-dbinstance-autominorversionupgrade "../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.md#cfn-rds-dbinstance-autominorversionupgrade") and [Engine](../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.md#cfn-rds-dbinstance-engine "../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.md#cfn-rds-dbinstance-engine") in the AWS CloudFormation User Guide.

For more information on proactive evaluation, see [Evaluation Mode](evaluate-config-rules.md "evaluate-config-rules.md").

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
