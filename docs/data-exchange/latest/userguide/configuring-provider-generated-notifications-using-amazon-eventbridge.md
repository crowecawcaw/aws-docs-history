# Configuring AWS Data Exchange provider-generated notifications using Amazon EventBridge

AWS Data Exchange delivers provider-generated notifications using Amazon EventBridge. Your role must be able to
create Amazon EventBridge rules, a target, and must be able to subscribe to a data product.

AWS Data Exchange events are published to your default Amazon EventBridge event bus in the same AWS Region as
where your data set is located. Use the following steps to create an Amazon EventBridge rule for
provider-generated notifications:

###### To create an Amazon EventBridge rule for provider-generated notifications

1. Create a target for the Amazon EventBridge rule. For a simple Lambda function in Python do the
   following:
   1. Navigate to the AWS Lambda console.
   2. Choose **Create function** and select **Author from
      scratch**.
   3. Provide a function name and select **Python 3.10** as the
      **runtime**. Choose **Create function**.
   4. Enter the following code for **lambda_function.py**:

   ```
   import json


   def lambda_handler(event, context):
       print(" ".join(["Event of type", event["detail-type"], "received!"]))
       print(" ".join(["Details", json.dumps(event["detail"])]))

       return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")
       }
   ```

2. Navigate to the EventBridge console.
3. Navigate to the **Rules** and select the default event bus.
4. Choose **Create rule** and provide the **Name** and
   optional **Description**. Make sure the **Rule** type is
   **Rule with an event pattern**.
5. Choose **Next**.
   1. Make sure the **Event source** is **AWS events** or
      **EventBridge partner events**. Under **Creation method**,
      select **Custom pattern** (JSON editor). Under **Event
      pattern**, enter the following JSON:

   ```
   {
       "source": ["aws.dataexchange"],
       "detail-type": ["Data Set Update Delayed", "Data Updated in Data Set", "Deprecation Planned for Data Set", "Schema Change Planned for Data Set"]
   }
   ```

6. Choose **Next**.
   1. For **Target 1**, select **AWS service** and choose
      **Lambda function**.
   2. For the **function**, select the function created in Step 1. Complete
      the creation of the rule.

   This Lambda function will be triggered any time a provider-generated notification is
   delivered. From the **Monitor** tab in the Lambda console, you can view
   recent invocations of the function.
