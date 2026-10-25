

# Update online evaluation
<a name="update-online-evaluations"></a>

The `UpdateOnlineEvaluationConfig` API modifies an existing online evaluation configuration, allowing you to change evaluators, data sources, execution settings, and other parameters. Updates do not interrupt running evaluations.

Updates can only be made when your evaluation configuration is in `ACTIVE`, `UPDATE_FAILED`, or `ERROR` status. If the configuration is currently being created, updated, or deleted, you’ll receive a conflict error and should retry after the operation completes.

## Execution control
<a name="execution-control"></a>

The execution status parameter controls whether your online evaluation configuration actively processes agent traces. Understanding these states helps you manage evaluation costs and performance.
+  **Enabling evaluation** – When changing from DISABLED to ENABLED, the system provisions the service to begin processing traces from your specified data sources.
+  **Disabling evaluation** – When changing from ENABLED to DISABLED, the system stops processing new traces while preserving your configuration for future use.

## Code samples for AgentCore CLI, AgentCore SDK, and AWS SDK
<a name="update-online-evaluations-code-samples"></a>

The following code samples demonstrate how to update online evaluation configurations using different development approaches. Choose the method that best fits your development environment and preferences.

**Example**  

1. 

   If you created the configuration with `agentcore add online-eval`, change it in the `onlineEvalConfigs` array in `agentcore/agentcore.json` and run `agentcore deploy`. To pause the configuration, set its `enableOnCreate` to `false` and deploy. To resume it, set `enableOnCreate` to `true` and deploy.

   For a configuration created outside a project, update it by ID. Run `agentcore eval online-eval list` to find the configuration ID.

   ```
   agentcore eval online-eval update \
     --id <ONLINE_EVAL_ID> \
     --sampling-rate 5 \
     --evaluators Builtin.GoalSuccessRate Builtin.Helpfulness
   ```

   To control whether the evaluation job of a configuration created outside a project is running (`ENABLED` or `DISABLED`), pause and resume it by ID:

   ```
   # Pause a running online evaluation
   agentcore eval online-eval pause --id <ONLINE_EVAL_ID>
   
   # Resume a paused online evaluation
   agentcore eval online-eval resume --id <ONLINE_EVAL_ID>
   ```
**Note**  
The configuration must be in `ACTIVE`, `UPDATE_FAILED`, or `ERROR` lifecycle status before you can update it.

1. 

   ```
   from bedrock_agentcore_starter_toolkit import Evaluation
   
   # Initialize the evaluation client
   eval_client = Evaluation()
   config_id = "config-abc123"
   print(f"\nUsing config_id: {config_id}")
   
   # update description
   eval_client.update_online_config(
       config_id=config_id,
       description="Updated description for online evaluation"
   )
   print("✅ Description updated")
   ```

1. 

   ```
   import boto3
   
   client = boto3.client('bedrock-agentcore-control')
   
   update_config_response = client.update_online_evaluation_config(
       onlineEvaluationConfigId='your_config_id',
       description="Updated description for online evaluation"
   )
   ```

1. 

   ```
   aws bedrock-agentcore-control update-online-evaluation-config \
       --online-evaluation-config-id your_config_id \
       --description "Updated description for online evaluation"
   ```

## Console
<a name="update-online-evaluations-console"></a>

Modify your online evaluation configuration settings using the console’s editing interface, which provides form validation and guided configuration options.

 **To update an online evaluation configuration** 

1. Open the Amazon Bedrock AgentCore console.

1. In the navigation pane, choose **Evaluation**.

1. In the **Evaluation configurations** card, view the table that lists the evaluation configurations you have created.

1. Choose one of the following methods to update the configuration:
   + Choose the evaluation configuration name to view its details, then choose **Edit** in the upper right of the details page.
   + Select the evaluation configuration so that it is highlighted, then choose **Edit** at the top of the **Evaluation configurations** card.

1. Update the fields as needed.

1. Choose **Update evaluation configuration** to save the changes.