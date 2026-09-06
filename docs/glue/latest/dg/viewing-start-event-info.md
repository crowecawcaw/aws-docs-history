

# Viewing the EventBridge events that started a workflow
<a name="viewing-start-event-info"></a>

You can view the event ID of the Amazon EventBridge event that started your workflow. If your workflow was started by a batch of events, you can view the event IDs of all events in the batch.

For workflows with a batch size greater than one, you can also see which batch condition started the workflow: the arrival of the number of events in the batch size, or the expiration of the batch window.

**To view the EventBridge events that started a workflow (console)**

1. Sign in to the AWS Management Console and open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/).

1. In the navigation pane, choose **Workflows**.

1. Select the workflow. Then at the bottom, choose the **History** tab.

1. Select a workflow run, and then choose **View run details**.

1. On the run details page, locate the **Run properties** field, and look for the **aws:eventIds** key.

   The value for that key is a list of EventBridge event IDs.

**To view the EventBridge events that started a workflow (AWS API)**
+ Include the following code in your Python script.

  ```
  workflow_params = glue_client.get_workflow_run_properties(Name=workflow_name,RunId=workflow_run_id)
  batched_events = workflow_params['aws:eventIds']
  ```

  `batched_events` will be a list of strings, where each string is an event ID.

**See also**  
[*Amazon EventBridge User Guide*](https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html)
[Overview of workflows in AWS Glue](workflows_overview.md)