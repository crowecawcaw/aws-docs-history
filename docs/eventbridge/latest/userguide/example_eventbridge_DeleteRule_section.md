

# Use `DeleteRule` with an AWS SDK or CLI
<a name="example_eventbridge_DeleteRule_section"></a>

The following code examples show how to use `DeleteRule`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Learn the basics](example_eventbridge_Scenario_GettingStarted_section.md) 

------
#### [ .NET ]

**SDK for .NET**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/EventBridge#code-examples). 
Delete a rule by its name.  

```
    /// <summary>
    /// Delete an event rule by name.
    /// </summary>
    /// <param name="ruleName">The name of the event rule.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DeleteRuleByName(string ruleName)
    {
        var response = await _amazonEventBridge.DeleteRuleAsync(
            new DeleteRuleRequest()
            {
                Name = ruleName
            });

        return response.HttpStatusCode == HttpStatusCode.OK;
    }
```
+  For API details, see [DeleteRule](https://docs.aws.amazon.com/goto/DotNetSDKV3/eventbridge-2015-10-07/DeleteRule) in *AWS SDK for .NET API Reference*. 

------
#### [ CLI ]

**AWS CLI**  
**To delete a CloudWatch Events rule**  
This example deletes the rule named EC2InstanceStateChanges:  

```
aws events delete-rule --name {{"EC2InstanceStateChanges"}}
```
+  For API details, see [DeleteRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/delete-rule.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/eventbridge#code-examples). 

```
    public static void deleteRuleByName(EventBridgeClient eventBrClient, String ruleName) {
        DeleteRuleRequest ruleRequest = DeleteRuleRequest.builder()
                .name(ruleName)
                .build();

        eventBrClient.deleteRule(ruleRequest);
        System.out.println("Successfully deleted the rule");
    }
```
+  For API details, see [DeleteRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/DeleteRule) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/eventbridge#code-examples). 

```
suspend fun deleteRuleByName(ruleName: String?) {
    val ruleRequest =
        DeleteRuleRequest {
            name = ruleName
        }
    EventBridgeClient.fromEnvironment { region = "us-east-1" }.use { eventBrClient ->
        eventBrClient.deleteRule(ruleRequest)
        println("Successfully deleted the rule")
    }
}
```
+  For API details, see [DeleteRule](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using EventBridge with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.