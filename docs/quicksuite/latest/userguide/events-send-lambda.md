# Creating rules to send Amazon Quick Sight events to

AWS Lambda

In this tutorial, you create an AWS Lambda function that logs the asset events in the
Amazon Quick Sight account. You then create a rule that runs the function whenever there is an
asset change. This tutorial assumes that you already signed up for Amazon Quick Sight.

###### Step 1: Create a Lambda function

Create a Lambda function to log the state change events. You specify this function
when you create your rule.

1. Sign in to the AWS Management Console and open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. If you're new to Lambda, you see a welcome page. Choose **Get Started
   Now**. Otherwise, choose **Create
   function**.
3. Choose **Author from scratch**.
4. On the Create function page, enter a name and description for the Lambda
   function. For example, name the function
   `QuickSightAssetChangeFn`.
5. In **Runtime**, select **Node.js
   18.x**.
6. For **Architecture**, choose
   **x86_64**.
7. For **Execution role**, choose either **Create a
   new role with basic Lambda permissions** or **Use an
   existing role** and choose the role you want.
8. Choose **Create function**.
9. On the **QuickSightAssetChange** page, choose
   **index.js**.
10. In the **index.js** pane, delete the existing code.
11. Enter the following code snippet.

```
console.log('Loading function');
exports.handler = async (event, context) => {
  console.log('Received QuickSight event:', JSON.stringify(event));
};
```

12. Choose **Deploy**.

###### Step 2: Create a rule

Create a rule to run your Lambda function whenever you create/update/delete a
Amazon Quick Sight asset.

1. Sign in to the AWS Management Console and open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule. For example, enter
   `QuickSightAssetChangeRule`.
5. Select **default** Event bus.
6. Choose **Rule with an event pattern**, and then choose
   **Next**.
7. For **Event source**, choose **AWS events or EventBridge
   partner events**.
8. In the **Creation method** section, choose **Custom
   pattern (JSON editor)**.
9. In the **Event pattern** text box, enter the following
   snippet and choose **Next**.

```
{
  "source": ["aws.quicksight"]
}
```

Alternatively, you can create the rule that only subscribes to a subset of
event types in Amazon Quick Sight. For example, the following rule will only triggered when
an asset is added to or removed from a folder with id
`77e307e8-b41b-472a-90e8-fe3f471537be`.

```
{
  "source": ["aws.quicksight"],
  "detail-type": ["QuickSight Folder Membership Updated"],
  "detail": {
    "folderId": "77e307e8-b41b-472a-90e8-fe3f471537be"
  }
}
```

10. For **Target types**, choose **AWS
    service** and **Lambda function**.
11. For **Function**, choose the Lambda function that you
    created. Then choose **Next**.
12. In **Configure tags**, choose
    **Next**.
13. Review the steps in your rule. Then choose **Create
    rule**.

###### Step 3: Test the rule

To test your rule, create an analysis. After waiting a minute, verify that your
Lambda function was invoked.

1. Open the Amazon Quick Sight console at [https://quicksight.aws.amazon.com/](https://quicksight.aws.amazon.com/ "https://quicksight.aws.amazon.com/").
2. Create a new analysis.
3. In the navigation pane, choose **Rules**, choose the name
   of the rule that you created.
4. In **Rule details**, choose
   **Monitoring**.
5. You will be redirected to the Amazon CloudWatch console. If you are not redirected,
   choose **View the metrics in CloudWatch**.
6. In **All metrics**, choose the name of the rule that you
   created. The graph indicates that the rule was invokved.
7. In the navigation pane, choose **Log groups**.
8. Choose the name of the log group for your Lambda function. For example,
   `/aws/lambda/function-name`.
9. Choose the name of the log stream to view the data provided by the function
   for the instance that you launched. You should see a received event similar to
   the following:

```
{
  "version": "0",
  "id": "3acb26c8-397c-4c89-a80a-ce672a864c55",
  "detail-type": "QuickSight Analysis Creation Successful",
  "source": "aws.quicksight",
  "account": "123456789012",
  "time": "2023-10-30T22:06:31Z",
  "region": "us-east-1",
  "resources": ["arn:aws:quicksight:us-east-1:123456789012:analysis/e5f37119-e24c-4874-901a-af9032b729b5"],
  "detail": {
    "analysisId": "e5f37119-e24c-4874-901a-af9032b729b5"
  }
}
```

For an example of Amazon Quick Sight event in JSON format, see [Overview of events for
Amazon Quick Sight](../../../quicksight/latest/developerguide/events.md "../../../quicksight/latest/developerguide/events.md").
