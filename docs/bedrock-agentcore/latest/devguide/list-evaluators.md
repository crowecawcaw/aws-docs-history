

# List evaluators
<a name="list-evaluators"></a>

The `ListEvaluators` API returns a paginated list of all custom evaluators in your account and Region, including both your custom evaluators and built-in evaluators. Built-in evaluators are returned first.

 **Filtering:** The API supports pagination through nextToken and maxResults parameters (1-100 results per page). Each evaluator summary includes type (Builtin or Custom), status, level, and lock state.

 **Summary information:** Returns essential metadata including ARN, name, description, evaluation level, creation and update timestamps, and current lock status for quick overview and selection.

**Topics**
+ [Code samples for AgentCore SDK and AWS SDK](#list-evaluators-code-samples)
+ [Console](#list-evaluators-console)

## Code samples for AgentCore SDK and AWS SDK
<a name="list-evaluators-code-samples"></a>

The following code samples demonstrate how to list evaluators using different development approaches. Choose the method that best fits your development environment and preferences.

**Example**  

1. 

   ```
   from bedrock_agentcore_starter_toolkit import Evaluation
   
   eval_client = Evaluation()
   
   available_evaluators = eval_client.list_evaluators()
   ```

1. 

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   list_configs_response = client.list_evaluators(maxResults=20)
   ```

1. 

   ```
   aws bedrock-agentcore-control list-evaluators \
       --max-results 20
   ```

## Console
<a name="list-evaluators-console"></a>

Use the console to view and manage your custom evaluators through a visual interface that displays evaluator details in an organized table format.

 **To list custom evaluators** 

1. Open the Amazon Bedrock AgentCore console.

1. In the navigation pane, choose **Evaluation**.

1. Choose **Custom evaluators** next to Evaluation configurations.

1. In the **Custom evaluators** card, view the table that lists the custom evaluators you have created.