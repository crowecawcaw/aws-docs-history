# Turning on Proactive Evaluation for AWS Config Rules

You can use the AWS Config console or the AWS SDKs to turn on proactive evaluation
rules. For a list of resource types and managed rules that support proactive evaluation, see [Components of a Rule | Evaluation Modes](evaluate-config_components.md#evaluate-config_use-managed-rules-proactive-detective "evaluate-config_components.md#evaluate-config_use-managed-rules-proactive-detective").

###### Topics

- [Using the console](#evaluate-config_turn-on-proactive-rules-console "#evaluate-config_turn-on-proactive-rules-console")
- [Using the AWS SDKs](#evaluate-config_turn-on-proactive-rules-cli "#evaluate-config_turn-on-proactive-rules-cli")

## Turning on Proactive Evaluation (Console)

The **Rules** page shows your rules and their current compliance
results in a table. The result for each rule is **Evaluating...**
until AWS Config finishes evaluating your resources against the rule. You can update the
results with the refresh button.

When AWS Config finishes evaluations, you can see the
rules and resource types that are compliant or noncompliant. For more information,
see [Viewing Compliance Information and Evaluation Results for your AWS Resources with AWS Config](evaluate-config_view-compliance.md "evaluate-config_view-compliance.md").

###### Note

AWS Config evaluates only the resource types that it is recording. For example, if you add
the **cloudtrail-enabled** rule but don't record the CloudTrail trail
resource type, AWS Config can't evaluate whether the trails in your account are compliant or
noncompliant. For more information, see [Recording AWS Resources with AWS Config](select-resources.md "select-resources.md").

You can use _proactive evaluation_ to evaluate resources before they have been deployed. This allows you to evaluate whether a set of resource properties, if used to define an AWS resource,
would be COMPLIANT or NON_COMPLIANT given the set of proactive rules that you have in your account in your Region.

The [Resource type schema](../../../cloudformation-cli/latest/userguide/resource-type-schema.md "../../../cloudformation-cli/latest/userguide/resource-type-schema.md") states the properties of a resource. You can find the resource type schema in "_AWS public extensions_" within the AWS CloudFormation registry or with the following CLI commmand:

```
aws cloudformation describe-type --type-name "AWS::S3::Bucket" --type `RESOURCE`
```

For more information, see [Managing extensions through the AWS CloudFormation registry](../../../AWSCloudFormation/latest/UserGuide/registry.md#registry-view "../../../AWSCloudFormation/latest/UserGuide/registry.md#registry-view")
and [AWS resource and property types reference](../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md "../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md") in the AWS CloudFormation User Guide.

###### Note

Proactive rules do not remediate resources that are flagged as NON_COMPLIANT or prevent them from being deployed.

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

## Turning on Proactive Evaluation

(AWS SDKs)

You can use _proactive evaluation_ to evaluate resources before they have been deployed. This allows you to evaluate whether a set of resource properties, if used to define an AWS resource,
would be COMPLIANT or NON_COMPLIANT given the set of proactive rules that you have in your account in your Region.

The [Resource type schema](../../../cloudformation-cli/latest/userguide/resource-type-schema.md "../../../cloudformation-cli/latest/userguide/resource-type-schema.md") states the properties of a resource. You can find the resource type schema in "_AWS public extensions_" within the AWS CloudFormation registry or with the following CLI commmand:

```
aws cloudformation describe-type --type-name "AWS::S3::Bucket" --type `RESOURCE`
```

For more information, see [Managing extensions through the AWS CloudFormation registry](../../../AWSCloudFormation/latest/UserGuide/registry.md#registry-view "../../../AWSCloudFormation/latest/UserGuide/registry.md#registry-view")
and [AWS resource and property types reference](../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md "../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md") in the AWS CloudFormation User Guide.

###### Note

Proactive rules do not remediate resources that are flagged as NON_COMPLIANT or prevent them from being deployed.

**To turn on proactive evaluation**

Use the [`put-config-rule`](../../../cli/latest/reference/configservice/put-config-rule.md "../../../cli/latest/reference/configservice/put-config-rule.md") command and enable `PROACTIVE` for `EvaluationModes`.

After you have turned on proactive evaluation,
you can use the [start-resource-evaluation](../../../cli/latest/reference/configservice/start-resource-evaluation.md "../../../cli/latest/reference/configservice/start-resource-evaluation.md") CLI command and [get-resource-evaluation-summary](../../../cli/latest/reference/configservice/get-resource-evaluation-summary.md "../../../cli/latest/reference/configservice/get-resource-evaluation-summary.md") CLI command to check if the resources you specify in these commands would be flagged as NON_COMPLIANT by the proactive rules in your account in your Region.

For example, start with the **start-resource-evaluation** command:

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

Then, use the `ResourceEvaluationId` with the **get-resource-evaluation-summary** to check the evaluation result:

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
use the [get-compliance-details-by-resource](../../../cli/latest/reference/configservice/get-compliance-details-by-resource.md "../../../cli/latest/reference/configservice/get-compliance-details-by-resource.md") CLI command.

###### Note

For a list of managed rules that support proactive evaluation, see [List of AWS Config Managed Rules by Evaluation Mode](managed-rules-by-evaluation-mode.md "managed-rules-by-evaluation-mode.md").

You can use _proactive evaluation_ to evaluate resources before they have been deployed. This allows you to evaluate whether a set of resource properties, if used to define an AWS resource,
would be COMPLIANT or NON_COMPLIANT given the set of proactive rules that you have in your account in your Region.

The [Resource type schema](../../../cloudformation-cli/latest/userguide/resource-type-schema.md "../../../cloudformation-cli/latest/userguide/resource-type-schema.md") states the properties of a resource. You can find the resource type schema in "_AWS public extensions_" within the AWS CloudFormation registry or with the following CLI commmand:

```
aws cloudformation describe-type --type-name "AWS::S3::Bucket" --type `RESOURCE`
```

For more information, see [Managing extensions through the AWS CloudFormation registry](../../../AWSCloudFormation/latest/UserGuide/registry.md#registry-view "../../../AWSCloudFormation/latest/UserGuide/registry.md#registry-view")
and [AWS resource and property types reference](../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md "../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md") in the AWS CloudFormation User Guide.

###### Note

Proactive rules do not remediate resources that are flagged as NON_COMPLIANT or prevent them from being deployed.

**To turn on proactive evaluation for a rule**

Use the [PutConfigRule](../APIReference/API_PutConfigRule.md "../APIReference/API_PutConfigRule.md") action and enable `PROACTIVE` for `EvaluationModes`.

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

###### Note

For a list of managed rules that support proactive evaluation, see [List of AWS Config Managed Rules by Evaluation Mode](managed-rules-by-evaluation-mode.md "managed-rules-by-evaluation-mode.md").
