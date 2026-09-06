

# Monitor performance evaluation failure events
<a name="performance-evaluation-events"></a>

You can monitor failures of automated evaluations as well as S3 exports of contact evaluations using EventBridge and CloudWatch. You can use these events to investigate and fix failures. The following guide is a walk through of the process of creating custom EventBridge rules to monitor performance evaluation failure events.

## Step-by-step guide
<a name="performance-evaluation-events-guide"></a>

This is a guide on how to create an EventBridge rule to log Connect Customer failed auto-evaluation submission events and failed S3 exports of contact evaluations in your AWS console.

1. Log into your AWS account and navigate to the EventBridge console. Choose **Rules** under the **Buses** section.  
![The Rules tab under the Buses section in the EventBridge console.](http://docs.aws.amazon.com/connect/latest/adminguide/images/perf-eval-eventbridge-rules-tab.png)

1. Choose **Create rule** with the default Event bus selected.  
![The Create rule button with the default Event bus selected.](http://docs.aws.amazon.com/connect/latest/adminguide/images/perf-eval-eventbridge-create-rule.png)

1. Give the rule a name and select **Rule with an event pattern** for the Rule type. Choose **Next**.  
![The rule name and Rule with an event pattern option selected.](http://docs.aws.amazon.com/connect/latest/adminguide/images/perf-eval-eventbridge-rule-name.png)

1. With **AWS events or EventBridge partner events** selected under **Events**, select the **Use pattern form** option under **Event pattern**. This is where you will define the pattern to match for triggering the rule.

1. Type and select **Amazon Connect** under the **AWS service** dropdown to narrow down the event types. Select the desired event type in the dropdown below. Choose **Next** after the pattern is set up.

   To subscribe to EventBridge event types, create a custom EventBridge rule that matches the following:
   + `"source"` = `"aws.connect"`
   + `"detail-type"` can be one of the following:
     + `"Contact Lens Automated Evaluation Submission Failed"`
     + `"Contact Lens Evaluation Export Failed"`  
![The event pattern with Amazon Connect selected as the AWS service.](http://docs.aws.amazon.com/connect/latest/adminguide/images/perf-eval-eventbridge-event-pattern.png)

1. In the next step, you can configure the target(s) to process/receive the matched events. For simplicity, select the **CloudWatch log group** option under **Select a target** and choose a log group.

1. Choose **Next** and advance to the final **Review and create** step. Choose **Create rule** once more to complete the rule creation process.

1. Now, if the rule is in the **Enabled** state and a matching event occurs, corresponding logs should show up in the configured CloudWatch log group with the relevant IDs under the metadata section and the failure reason under the data section.  
![CloudWatch log group showing matched EventBridge events.](http://docs.aws.amazon.com/connect/latest/adminguide/images/perf-eval-cloudwatch-log-group.png)  
![CloudWatch log detail showing metadata and failure reason.](http://docs.aws.amazon.com/connect/latest/adminguide/images/perf-eval-cloudwatch-log-detail.png)

## Example EventBridge payload
<a name="performance-evaluation-events-payload"></a>

The following is an example EventBridge payload when the rule is matched:

```
{  
  "version": "0",  
  "id": "00005435-d12d-c93b-d9d2-b64cba85fbb6",
  "detail-type": "Contact Lens Automated Evaluation Submission Failed",  
  "source": "aws.connect",  
  "account": "Your AWS account ID",  
  "time": "2025-10-02T10:34:56Z",  
  "region": "us-west-2",
  "resources": [],  
  "detail": {  
    "version": "1.0.0",  
    "metadata": {  
      "contactId": "4266f8e9-8420-4ee7-96cd-515d2edae1f2",
      "instanceId": "d9b0b09d-7dab-47e5-9f82-d6787fbc068c",
      "formId": "8b1365bd-1415-41a9-a491-af226e1bda4e"
    },  
    "data": {  
      "reasonCode": "ANALYSIS_FILE_ERROR",
      "message": "Automated contact evaluation submission failed due to an error when searching/retrieving/parsing the analysis file."
    }  
  }  
}
```

## Common errors
<a name="performance-evaluation-events-errors"></a>

The following errors might occur when the system eventually fails to process evaluations after multiple retry attempts.

### Automated evaluation submission errors
<a name="automated-evaluation-submission-errors"></a>


| Error | Error message | 
| --- | --- | 
| AUTOMATED\_SUBMISSION\_FAILED | Automated contact evaluation submission failed because some of the questions could not be answered. Please verify the evaluation form or the Connect Customer rule configurations. | 
| ANALYSIS\_FILE\_ERROR | Automated contact evaluation submission failed due to an error when searching/retrieving/parsing the analysis file. | 
| INTERNAL\_SERVER\_ERROR | Automated contact evaluation submission failed due to an internal server error. Please expect delayed processing. | 
| QUOTA\_EXCEEDED\_ERROR | Automated contact evaluation submission failed because the remaining quota for using generative AI to automatically answer evaluation questions for the contact is insufficient. | 

### Evaluation S3 export errors
<a name="evaluation-s3-export-errors"></a>


| Error | Error message | 
| --- | --- | 
| S3\_BUCKET\_ACCESS\_DENIED | Contact evaluation JSON export failed due to insufficient permissions. | 
| S3\_STORAGE\_NOT\_CONFIGURED | The export S3 bucket is not configured for your instance. | 
| INTERNAL\_SERVER\_ERROR | Contact evaluation JSON export failed due to an internal server error. Please expect delayed delivery of the export file. | 