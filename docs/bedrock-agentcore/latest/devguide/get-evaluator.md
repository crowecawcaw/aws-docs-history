

# Get evaluator
<a name="get-evaluator"></a>

The `GetEvaluator` API retrieves complete details of a specific custom or built-in evaluator including its configuration, status, and lock state.

 **Lock status:** The response includes lockedForModification indicating whether the evaluator is in use by an enabled evaluation configuration. Locked evaluators cannot be modified.

Use this API to inspect evaluator settings, verify configuration changes, and check availability for modification or deletion.

**Topics**
+ [Code samples for AgentCore SDK and AWS SDK](#get-evaluators-code-samples)
+ [Console](#get-evaluator-console)

## Code samples for AgentCore SDK and AWS SDK
<a name="get-evaluators-code-samples"></a>

The following code samples demonstrate how to get evaluator details using different development approaches. Choose the method that best fits your development environment and preferences.

**Example**  

1. 

   ```
   from bedrock_agentcore_starter_toolkit import Evaluation
   
   eval_client = Evaluation()
   
   eval_client.get_evaluator(evaluator_id="your_evaluator_id")
   ```

1. 

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   list_configs_response = client.get_evaluator(evaluatorId='your_evaluator_id')
   ```

1. 

   ```
   aws bedrock-agentcore-control get-evaluator \
       --evaluator-id 'your_evaluator_id'
   ```

## Console
<a name="get-evaluator-console"></a>

View detailed information about a specific custom evaluator, including its configuration, status, and usage history through the console interface.

 **To get custom evaluator details** 

1. Open the Amazon Bedrock AgentCore console.

1. In the navigation pane, choose **Evaluation**.

1. Choose **Custom evaluators** next to Evaluation configurations.

1. In the **Custom evaluators** card, view the table that lists the custom evaluators you have created.

1. To view information for a specific custom evaluator, choose the custom evaluator name to view its details.