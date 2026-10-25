

# Delete online evaluation
<a name="delete-online-evaluations"></a>

The `DeleteOnlineEvaluationConfig` API permanently removes an online evaluation configuration and stops all associated evaluation processing. This asynchronous operation disables the evaluation service and cleans up all related resources.

An online evaluation can only be deleted when the configuration is in `ACTIVE`, `UPDATE_FAILED`, `CREATE_FAILED`, or `ERROR` status. Configurations currently being created, updated, or deleted must complete their operations before another deletion is allowed.

## Code samples for AgentCore CLI, AgentCore SDK, and AWS SDK
<a name="delete-online-evaluations-code-samples"></a>

The following code samples demonstrate how to delete online evaluation configurations using different development approaches. Choose the method that best fits your development environment and preferences.

**Example**  

1. 

   If you added the configuration with `agentcore add online-eval`, remove it from the project and deploy:

   ```
   agentcore remove online-eval --name <ONLINE_EVAL_NAME>
   agentcore deploy
   ```

   You can also run `agentcore remove` and choose the configuration.

   To delete a configuration that is not part of a project, delete it by ID:

   ```
   agentcore eval online-eval delete --id <ONLINE_EVAL_ID>
   ```

1. 

   ```
   from bedrock_agentcore_starter_toolkit import Evaluation
   
   # Initialize the evaluation client
   eval_client = Evaluation()
   config_id = "config-abc123"
   print(f"\nUsing config_id: {config_id}")
   
   eval_client.delete_online_config(
        config_id=config_id,
        delete_execution_role=True  # Also delete the IAM role
   )
   ```

1. 

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   delete_config_response = client.delete_online_evaluation_config(
       onlineEvaluationConfigId='your_config_id'
   )
   ```

1. 

   ```
   aws bedrock-agentcore-control delete-online-evaluation-config \
       --online-evaluation-config-id your_config_id
   ```

## Console
<a name="delete-online-evaluations-console"></a>

Permanently remove an online evaluation configuration using the console interface, which includes confirmation prompts to prevent accidental deletion.

 **To delete an online evaluation configuration** 

1. Open the Amazon Bedrock AgentCore console.

1. In the navigation pane, choose **Evaluation**.

1. In the **Evaluation configurations** card, view the table that lists the evaluation configurations you have created.

1. Choose one of the following methods to delete the configuration:
   + Choose the evaluation configuration name to view its details, then choose **Delete** in the upper right of the details page.
   + Select the evaluation configuration so that it is highlighted, then choose **Delete** at the top of the **Evaluation configurations** card.

1. Enter `confirm` to confirm the deletion.

1. Choose **Delete** to delete the configuration.