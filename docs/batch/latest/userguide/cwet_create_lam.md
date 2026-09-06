

# Tutorial: Create the Lambda function
<a name="cwet_create_lam"></a>

 In this procedure, you create a simple Lambda function to serve as a target for AWS Batch event stream messages. 

**To create a target Lambda function**

1. Open the AWS Lambda console at [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/).

1. Choose **Create function**, **Author from scratch**. 

1. For **Function name**, enter **batch-event-stream-handler**.

1. For **Runtime**, choose **Python 3.8**.

1. Choose **Create function**.

1. In the **Code source** section, edit the sample code to match the following example:

   ```
   import json
   
   
   def lambda_handler(event, _context):
       # _context is not used
       del _context
       if event["source"] != "aws.batch":
           raise ValueError("Function only supports input from events with a source type of: aws.batch")
   
       print(json.dumps(event))
   ```

   This is a simple Python 3.8 function that prints the events sent by AWS Batch. If everything is configured correctly, at the end of this tutorial, the event details appear in the CloudWatch Logs log stream that's associated with this Lambda function.

1. Choose **Deploy**.