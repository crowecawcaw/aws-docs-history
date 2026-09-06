

# Create an EventBridge rule for an Amazon ECR source (console)
<a name="create-cwe-ecr-source-console"></a>

**To create an EventBridge rule for use in CodePipeline operations (Amazon ECR source)**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. In the navigation pane, choose **Events**.

1. Choose **Create rule**, and then under **Event source**, from **Service Name**, choose **Elastic Container Registry (ECR)**.

1. In **Event Source**, choose **Event Pattern**.

   Choose **Edit**, and then paste the following example event pattern in the **Event Source** window for a `eb-test` repository with an image tag of `cli-testing`:

   ```
   {
       "detail-type": [
           "ECR Image Action"
       ],
       "source": [
           "aws.ecr"
       ],
       "detail": {
           "action-type": [
               "PUSH"
           ],
           "image-tag": [
               "latest"
           ],
           "repository-name": [
               "eb-test"
           ],
           "result": [
               "SUCCESS"
           ]
       }
   }
   ```
**Note**  
To view the full event pattern supported for Amazon ECR events, see [Amazon ECR Events and EventBridge](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ecr-eventbridge.html) or [Amazon Elastic Container Registry Events](https://docs.aws.amazon.com/eventbridge/latest/userguide/event-types.html#ecr-event-types).

1. Choose **Save**.

   In the **Event Pattern Preview** pane, view the rule.

1. In **Targets**, choose **CodePipeline**.

1. Enter the pipeline ARN for the pipeline to be started by this rule.
**Note**  
You can find the pipeline ARN in the metadata output after you run the **get-pipeline** command. The pipeline ARN is constructed in this format:   
arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}  
Sample pipeline ARN:  
`arn:aws:codepipeline:us-east-2:80398EXAMPLE:MyFirstPipeline`

1. Create or specify an IAM service role that grants EventBridge permissions to invoke the target associated with your EventBridge rule (in this case, the target is CodePipeline). 
   + Choose **Create a new role for this specific resource** to create a service role that gives EventBridge permissions to start your pipeline executions.
   + Choose **Use existing role** to enter a service role that gives EventBridge permissions to start your pipeline executions.

1. (Optional) To specify source overrides with a specific image ID, use the input transformer to pass the data as JSON parameters. You can also use the input transformer to pass pipeline variables.
   + Expand **Additional settings**.

     Under **Configure target input**, choose **Configure input transformer**.

     In the dialog window, choose **Enter my own**. In the **Input path** box, type the following key-value pairs.

     ```
     {"revisionValue": "$.detail.image-digest"}
     ```
   + In the **Template** box, type the following key-value pairs.

     ```
     {
         "sourceRevisions": [
             {
                 "actionName": "Source",
                 "revisionType": "IMAGE_DIGEST",
                 "revisionValue": "<{{revisionValue}}>"
             }
         ],
          "variables": [
             {
                 "name": "{{Variable_Name}}",
                 "value": "{{Variable_Value}}"
             }
         ]
     }
     ```
   + Choose **Confirm**.

1. Review your rule setup to make sure it meets your requirements.

1. Choose **Configure details**.

1. On the **Configure rule details** page, enter a name and description for the rule, and then choose **State** to enable the rule.

1. If you're satisfied with the rule, choose **Create rule**.