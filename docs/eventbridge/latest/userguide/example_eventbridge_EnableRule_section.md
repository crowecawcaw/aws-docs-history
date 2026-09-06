

# Use `EnableRule` with an AWS SDK or CLI
<a name="example_eventbridge_EnableRule_section"></a>

The following code examples show how to use `EnableRule`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Learn the basics](example_eventbridge_Scenario_GettingStarted_section.md) 

------
#### [ .NET ]

**SDK for .NET**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/EventBridge#code-examples). 
Enable a rule by its rule name.  

```
    /// <summary>
    /// Enable a particular rule on an event bus.
    /// </summary>
    /// <param name="ruleName">The name of the rule.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> EnableRuleByName(string ruleName)
    {
        var ruleResponse = await _amazonEventBridge.EnableRuleAsync(
            new EnableRuleRequest()
            {
                Name = ruleName
            });
        return ruleResponse.HttpStatusCode == HttpStatusCode.OK;
    }
```
+  For API details, see [EnableRule](https://docs.aws.amazon.com/goto/DotNetSDKV3/eventbridge-2015-10-07/EnableRule) in *AWS SDK for .NET API Reference*. 

------
#### [ CLI ]

**AWS CLI**  
**To enable a CloudWatch Events rule**  
This example enables the rule named DailyLambdaFunction, which had been previously disabled:  

```
aws events enable-rule --name {{"DailyLambdaFunction"}}
```
+  For API details, see [EnableRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/enable-rule.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/eventbridge#code-examples). 
Enable a rule by using its rule name.  

```
    public static void changeRuleState(EventBridgeClient eventBrClient, String eventRuleName, Boolean isEnabled) {
        try {
            if (!isEnabled) {
                System.out.println("Disabling the rule: " + eventRuleName);
                DisableRuleRequest ruleRequest = DisableRuleRequest.builder()
                        .name(eventRuleName)
                        .build();

                eventBrClient.disableRule(ruleRequest);
            } else {
                System.out.println("Enabling the rule: " + eventRuleName);
                EnableRuleRequest ruleRequest = EnableRuleRequest.builder()
                        .name(eventRuleName)
                        .build();
                eventBrClient.enableRule(ruleRequest);
            }

        } catch (EventBridgeException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [EnableRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/EnableRule) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/eventbridge#code-examples). 

```
suspend fun changeRuleState(
    eventRuleName: String,
    isEnabled: Boolean?,
) {
    if (!isEnabled!!) {
        println("Disabling the rule: $eventRuleName")
        val ruleRequest =
            DisableRuleRequest {
                name = eventRuleName
            }
        EventBridgeClient { region = "us-east-1" }.use { eventBrClient ->
            eventBrClient.disableRule(ruleRequest)
        }
    } else {
        println("Enabling the rule: $eventRuleName")
        val ruleRequest =
            EnableRuleRequest {
                name = eventRuleName
            }
        EventBridgeClient.fromEnvironment { region = "us-east-1" }.use { eventBrClient ->
            eventBrClient.enableRule(ruleRequest)
        }
    }
}
```
+  For API details, see [EnableRule](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using EventBridge with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.