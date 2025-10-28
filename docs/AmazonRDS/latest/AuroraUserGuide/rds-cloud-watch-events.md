# Creating a rule that triggers on an Amazon Aurora event

Using Amazon EventBridge, you can automate AWS services and respond to system events such as application
availability issues or resource changes.

###### Topics

- [Tutorial: Log DB instance state changes using
  Amazon EventBridge](#log-rds-instance-state "#log-rds-instance-state")

## Tutorial: Log DB instance state changes using

Amazon EventBridge

In this tutorial, you create an AWS Lambda function that logs the state changes for an instance.
You then create a rule that runs the function whenever there is a state change of an existing RDS DB instance. The tutorial assumes that you
have a small running test instance that you can shut down temporarily.

###### Important

Don't perform this tutorial on a running production DB instance.

###### Topics

- [Step 1: Create an AWS Lambda function](#rds-create-lambda-function "#rds-create-lambda-function")
- [Step 2: Create a rule](#rds-create-rule "#rds-create-rule")
- [Step 3: Test the rule](#rds-test-rule "#rds-test-rule")

### Step 1: Create an AWS Lambda function

Create a Lambda function to log the state change events. You specify this function when you create your rule.

###### To create a Lambda function

1. Open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. If you're new to Lambda, you see a welcome page. Choose **Get Started Now**. Otherwise, choose **Create
   function**.
3. Choose **Author from scratch**.
4. On the **Create function** page, do the following:
   1. Enter a name and description for the Lambda function. For example, name the function `RDSInstanceStateChange`.
   2. In **Runtime**, select **Node.js 16x**.
   3. For **Architecture**, choose **x86_64**.
   4. For **Execution role**, do either of the following:
      - Choose **Create a new role with basic Lambda permissions**.
      - For **Existing role**, choose **Use an existing role**. Choose the role that you want to use.

   5. Choose **Create function**.

5. On the **RDSInstanceStateChange** page, do the following:
   1. In **Code source**, select **index.js**.
   2. In the **index.js** pane, delete the existing code.
   3. Enter the following code:

   ```
   console.log('Loading function');

   exports.handler = async (event, context) => {
       console.log('Received event:', JSON.stringify(event));
   };
   ```

   4. Choose **Deploy**.

### Step 2: Create a rule

Create a rule to run your Lambda function whenever you launch an Amazon RDS instance.

###### To create the EventBridge rule

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule. For example, enter `RDSInstanceStateChangeRule`.
5. Choose **Rule with an event pattern**, and then choose **Next**.
6. For **Event source**, choose **AWS events or EventBridge partner events**.
7. Scroll down to the **Event pattern** section.
8. For **Event source**, choose **AWS services**.
9. For **AWS service**, choose **Relational Database Service (RDS)**.
10. For **Event type**, choose **RDS DB Instance Event**.
11. Leave the default event pattern. Then choose **Next**.
12. For **Target types**, choose **AWS service**.
13. For **Select a target**, choose **Lambda function**.
14. For **Function**, choose the Lambda function that you created. Then choose **Next**.
15. In **Configure tags**, choose **Next**.
16. Review the steps in your rule. Then choose **Create rule**.

### Step 3: Test the rule

To test your rule, shut down an RDS DB instance. After waiting a few minutes for the instance to shut down, verify that your Lambda function
was invoked.

###### To test your rule by stopping a DB instance

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Stop an RDS DB instance.
3. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
4. In the navigation pane, choose **Rules**, choose the name of the rule that you created.
5. In **Rule details**, choose **Monitoring**.

You are redirected to the Amazon CloudWatch console. If you are not redirected, click **View the metrics in CloudWatch**. 6. In **All metrics**, choose the name of the rule that you created.

The graph should indicate that the rule was invoked. 7. In the navigation pane, choose **Log groups**. 8. Choose the name of the log group for your Lambda function
(**/aws/lambda/`function-name`**). 9. Choose the name of the log stream to view the data provided by the function for the instance that you launched. You should see a received
event similar to the following:

```
{
    "version": "0",
    "id": "12a345b6-78c9-01d2-34e5-123f4ghi5j6k",
    "detail-type": "RDS DB Instance Event",
    "source": "aws.rds",
    "account": "111111111111",
    "time": "2021-03-19T19:34:09Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:rds:us-east-1:111111111111:db:testdb"
    ],
    "detail": {
        "EventCategories": [
            "notification"
        ],
        "SourceType": "DB_INSTANCE",
        "SourceArn": "arn:aws:rds:us-east-1:111111111111:db:testdb",
        "Date": "2021-03-19T19:34:09.293Z",
        "Message": "DB instance stopped",
        "SourceIdentifier": "testdb",
        "EventID": "RDS-EVENT-0087"
    }
}
```

For more examples of RDS events in JSON format, see [Overview of events for Aurora](working-with-events.md#rds-cloudwatch-events.sample "working-with-events.md#rds-cloudwatch-events.sample"). 10. (Optional) When you're finished, you can open the Amazon RDS console and start the instance that you stopped.
