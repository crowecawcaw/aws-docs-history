# Evaluating Your Resources with AWS Config Rules

When you create custom rules or use managed rules, AWS Config evaluates your resources against
those rules. You can run on-demand evaluations for resources against your rules. For
example, this is helpful when you create a custom rule and want to check that AWS Config is
correctly evaluating your resources or to identify if there is an issue with the evaluation
logic of your AWS Lambda function.

###### Example

1. You create a custom rule that evaluates whether your IAM users have active
   access keys.
2. AWS Config evaluates your resources against your custom rule.
3. An IAM user who doesn't have an active access key exists in your account. Your
   rule doesn't correctly flag this resource as NON_COMPLIANT.
4. You fix the rule and start the evaluation again.
5. Because you fixed your rule, the rule correctly evaluates your resources, and
   flags the IAM user resource as NON_COMPLIANT.
   When you add a rule to your account, you can specify when in the resource creation and
   management process that you want AWS Config to evaluate your resources. The resource creation and management process is known as resource provisioning. You choose the
   _evaluation mode_ to specify when in this process you want AWS Config to evaluate your resources.

Depending on the rule, AWS Config can evaluate your resource configurations before a
resource has been deployed, after a resource has been deployed, or both. Evaluating a
resource before it has been deployed is **proactive evaluation**. Evaluating a
resource after it has been deployed is **detective evaluation**.

Use proactive evaluation to evaluate resources before they have been deployed. This allows you to evaluate whether a set of resource properties, if used to define an AWS resource,
would be COMPLIANT or NON_COMPLIANT given the set of proactive rules that you have in your account in your Region.

The [Resource type schema](../../../cloudformation-cli/latest/userguide/resource-type-schema.md "../../../cloudformation-cli/latest/userguide/resource-type-schema.md") states the properties of a resource. You can find the resource type schema in "_AWS public extensions_" within the AWS CloudFormation registry or with the following CLI commmand:

```
aws cloudformation describe-type --type-name "AWS::S3::Bucket" --type `RESOURCE`
```

For more information, see [Managing extensions through the CloudFormation registry](../../../AWSCloudFormation/latest/UserGuide/registry.md#registry-view "../../../AWSCloudFormation/latest/UserGuide/registry.md#registry-view")
and [AWS resource and property types reference](../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md "../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md") in the AWS CloudFormation User Guide.

###### Note

Proactive rules do not remediate resources that are flagged as NON_COMPLIANT or prevent them from being deployed.

### Evaluating your Resources

###### To turn on proactive evalution

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. In the AWS Management Console menu, verify that the Region selector is set to a
   Region that supports AWS Config rules. For the list of supported AWS
   Regions, see [AWS Config
   Regions and Endpoints](../../../general/latest/gr/rande.md#awsconfig_region "../../../general/latest/gr/rande.md#awsconfig_region") in the
   _Amazon Web Services General Reference_.
3. In the left navigation, choose **Rules**. For a list of managed rules that support proactive evaluation, see [List of AWS Config Managed Rules by Evaluation Mode](managed-rules-by-evaluation-mode.md "managed-rules-by-evaluation-mode.md").
4. Choose a rule, and then choose **Edit rule** for the
   rule that you want to update.
5. For **Evaluation mode**, choose **Turn on proactive evaluation** to allow you to run evaluations on the configuration settings of your resources before they are deployed.
6. Choose **Save**.

###### Note

You can also turn on proactive evaluation using the [`put-config-rule`](../../../cli/latest/reference/configservice/put-config-rule.md "../../../cli/latest/reference/configservice/put-config-rule.md") command
and enabling `PROACTIVE` for `EvaluationModes` or using the [PutConfigRule](../APIReference/API_PutConfigRule.md "../APIReference/API_PutConfigRule.md") action and enabling `PROACTIVE` for `EvaluationModes`.

After you have turned on proactive evaluation,
you can use the [StartResourceEvaluation](../APIReference/API_StartResourceEvaluation.md "../APIReference/API_StartResourceEvaluation.md") API and [GetResourceEvaluationSummary](../APIReference/API_GetResourceEvaluationSummary.md "../APIReference/API_GetResourceEvaluationSummary.md") API to check if the resources you specify in these commands would be flagged as NON_COMPLIANT by the proactive rules in your account in your Region.

For example, start with the StartResourceEvaluation API:

```
aws configservice start-resource-evaluation --evaluation-mode PROACTIVE
                --resource-details '{"ResourceId":"`MY_RESOURCE_ID`",
                                     "ResourceType":"`AWS::RESOURCE::TYPE`",
                                     "ResourceConfiguration":"`RESOURCE_DEFINITION_AS_PER_THE_RESOURCE_CONFIGURATION_SCHEMA`",
                                     "ResourceConfigurationSchemaType":"CFN_RESOURCE_SCHEMA"}'

```

You should receive the `ResourceEvaluationId` in the output:

```
{
    "ResourceEvaluationId": "MY_RESOURCE_EVALUATION_ID"
}
```

Then, use the `ResourceEvaluationId` with the GetResourceEvaluationSummary API to check the evaluation result:

```
aws configservice get-resource-evaluation-summary
    --resource-evaluation-id `MY_RESOURCE_EVALUATION_ID`
```

You should receive output similiar to the following:

```
{
    "ResourceEvaluationId": "MY_RESOURCE_EVALUATION_ID",
    "EvaluationMode": "PROACTIVE",
    "EvaluationStatus": {
        "Status": "SUCCEEDED"
    },
    "EvaluationStartTimestamp": "2022-11-15T19:13:46.029000+00:00",
    "Compliance": "COMPLIANT",
    "ResourceDetails": {
        "ResourceId": "MY_RESOURCE_ID",
        "ResourceType": "AWS::RESOURCE::TYPE",
        "ResourceConfiguration": "RESOURCE_DEFINITION_AS_PER_THE_RESOURCE_CONFIGURATION_SCHEMA"
    }
}
```

To see additional information about the evaluation result, such as which rule flagged a resource as NON_COMPLIANT,
use the [GetComplianceDetailsByResource](../APIReference/API_GetComplianceDetailsByResource.md "../APIReference/API_GetComplianceDetailsByResource.md") API.

Use detective evaluation to evaluate resources that have already been
deployed. This allows you to evaluate the configuration settings of your
existing resources.

### Evaluating your Resources

(Console)

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. In the AWS Management Console menu, check that the region selector is set to a Region that
   supports AWS Config rules. For the list of supported regions, see [AWS Config Regions and Endpoints](../../../general/latest/gr/awsconfig.md "../../../general/latest/gr/awsconfig.md")
   in the _Amazon Web Services General Reference_.
3. In the navigation pane, choose **Rules**. The
   **Rules** page shows the name, associated remediation
   action, and compliance status of each rule.
4. Choose a rule from the table.
5. From the **Actions** dropdown list, choose
   **Re-evaluate**.
6. AWS Config starts evaluating the resources against your rule.

###### Note

You can re-evaluate a rule one time each minute. You must wait for AWS Config to complete the
evaluation for your rule before you start another evaluation. You can't run an
evaluation if at the same time the rule is being updated or if the rule is being
deleted.

### Evaluating your Resources (CLI)

- Use the **start-config-rules-evaluation** command:

```
$ **aws configservice start-config-rules-evaluation --config-rule-names `ConfigRuleName`**
```

AWS Config starts evaluating the recorded resource configurations against your
rule. You can also specify multiple rules in your request:

```
$ **aws configservice start-config-rules-evaluation --config-rule-names `ConfigRuleName1` `ConfigRuleName2` `ConfigRuleName3`**
```

### Evaluating your Resources (API)

Use the [StartConfigRulesEvaluation](../APIReference/API_StartConfigRulesEvaluation.md "../APIReference/API_StartConfigRulesEvaluation.md") action.
