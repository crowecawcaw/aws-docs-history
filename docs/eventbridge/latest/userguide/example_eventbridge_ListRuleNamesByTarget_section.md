# Use `ListRuleNamesByTarget` with an AWS SDK or CLI

The following code examples show how to use `ListRuleNamesByTarget`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Learn the basics](example_eventbridge_Scenario_GettingStarted_section.md "example_eventbridge_Scenario_GettingStarted_section.md")

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/EventBridge#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/EventBridge#code-examples").

List all of the rule names using the target.

```
    /// <summary>
    /// List names of all rules matching a target.
    /// </summary>
    /// <param name="targetArn">The ARN of the target.</param>
    /// <returns>The list of rule names.</returns>
    public async Task<List<string>> ListAllRuleNamesByTarget(string targetArn)
    {
        var results = new List<string>();
        var request = new ListRuleNamesByTargetRequest()
        {
            TargetArn = targetArn
        };
        ListRuleNamesByTargetResponse response;
        do
        {
            response = await _amazonEventBridge.ListRuleNamesByTargetAsync(request);
            results.AddRange(response.RuleNames);
            request.NextToken = response.NextToken;

        } while (response.NextToken is not null);

        return results;
    }


```

- For API details, see
  [ListRuleNamesByTarget](../../../goto/DotNetSDKV3/eventbridge-2015-10-07/ListRuleNamesByTarget.md "../../../goto/DotNetSDKV3/eventbridge-2015-10-07/ListRuleNamesByTarget.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To display all the rules that have a specified target**

This example displays all rules that have the Lambda function named "MyFunctionName" as the target:

```
`aws events list-rule-names-by-target --target-arn `"arn:aws:lambda:us-east-1:123456789012:function:MyFunctionName"``

```

- For API details, see
  [ListRuleNamesByTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-rule-names-by-target.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-rule-names-by-target.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/eventbridge#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/eventbridge#code-examples").

List all of the rule names by using the target.

```
    public static void listTargetRules(EventBridgeClient eventBrClient, String topicArn) {
        ListRuleNamesByTargetRequest ruleNamesByTargetRequest = ListRuleNamesByTargetRequest.builder()
                .targetArn(topicArn)
                .build();

        ListRuleNamesByTargetResponse response = eventBrClient.listRuleNamesByTarget(ruleNamesByTargetRequest);
        List<String> rules = response.ruleNames();
        for (String rule : rules) {
            System.out.println("The rule name is " + rule);
        }
    }


```

- For API details, see
  [ListRuleNamesByTarget](../../../goto/SdkForJavaV2/eventbridge-2015-10-07/ListRuleNamesByTarget.md "../../../goto/SdkForJavaV2/eventbridge-2015-10-07/ListRuleNamesByTarget.md")
  in _AWS SDK for Java 2.x API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/eventbridge#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/eventbridge#code-examples").

```
suspend fun listTargetRules(topicArnVal: String?) {
    val ruleNamesByTargetRequest =
        ListRuleNamesByTargetRequest {
            targetArn = topicArnVal
        }

    EventBridgeClient.fromEnvironment { region = "us-east-1" }.use { eventBrClient ->
        val response = eventBrClient.listRuleNamesByTarget(ruleNamesByTargetRequest)
        response.ruleNames?.forEach { rule ->
            println("The rule name is $rule")
        }
    }
}


```

- For API details, see
  [ListRuleNamesByTarget](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using EventBridge with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
