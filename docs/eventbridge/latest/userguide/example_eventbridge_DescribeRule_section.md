

# Use `DescribeRule` with an AWS SDK or CLI
<a name="example_eventbridge_DescribeRule_section"></a>

The following code examples show how to use `DescribeRule`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Learn the basics](example_eventbridge_Scenario_GettingStarted_section.md) 

------
#### [ .NET ]

**SDK for .NET**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/EventBridge#code-examples). 
Get the state of a rule using the rule description.  

```
    /// <summary>
    /// Get the state for a rule by the rule name.
    /// </summary>
    /// <param name="ruleName">The name of the rule.</param>
    /// <param name="eventBusName">The optional name of the event bus. If empty, uses the default event bus.</param>
    /// <returns>The state of the rule.</returns>
    public async Task<RuleState> GetRuleStateByRuleName(string ruleName, string? eventBusName = null)
    {
        var ruleResponse = await _amazonEventBridge.DescribeRuleAsync(
            new DescribeRuleRequest()
            {
                Name = ruleName,
                EventBusName = eventBusName
            });
        return ruleResponse.State;
    }
```
+  For API details, see [DescribeRule](https://docs.aws.amazon.com/goto/DotNetSDKV3/eventbridge-2015-10-07/DescribeRule) in *AWS SDK for .NET API Reference*. 

------
#### [ CLI ]

**AWS CLI**  
**To display information about a CloudWatch Events rule**  
This example displays information about the rule named DailyLambdaFunction:  

```
aws events describe-rule --name {{"DailyLambdaFunction"}}
```
+  For API details, see [DescribeRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-rule.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/eventbridge#code-examples). 

```
    public static void checkRule(EventBridgeClient eventBrClient, String eventRuleName) {
        try {
            DescribeRuleRequest ruleRequest = DescribeRuleRequest.builder()
                    .name(eventRuleName)
                    .build();

            DescribeRuleResponse response = eventBrClient.describeRule(ruleRequest);
            System.out.println("The state of the rule is " + response.stateAsString());

        } catch (EventBridgeException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [DescribeRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/DescribeRule) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/eventbridge#code-examples). 

```
suspend fun checkRule(eventRuleName: String?) {
    val ruleRequest =
        DescribeRuleRequest {
            name = eventRuleName
        }

    EventBridgeClient.fromEnvironment { region = "us-east-1" }.use { eventBrClient ->
        val response = eventBrClient.describeRule(ruleRequest)
        println("The state of the rule is $response")
    }
}
```
+  For API details, see [DescribeRule](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using EventBridge with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.