# Tutorial: Log the state of an Amazon EC2 instance

using EventBridge

You can create an [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") function that logs a state change for an [Amazon EC2](../../../AWSEC2/latest/UserGuide/concepts.md "../../../AWSEC2/latest/UserGuide/concepts.md") instance. Then
you can create a [rule](eb-rules.md "eb-rules.md") that runs your Lambda function whenever
there is a state transition or a transition to one or more states that are of interest. In
this tutorial, you log the launch of any new instance.

###### Steps:

- [Step 1: Create an AWS Lambda
  function](#eb-ec2-create-lambda-function "#eb-ec2-create-lambda-function")
- [Step 2: Create a rule](#eb-ec2-create-rule "#eb-ec2-create-rule")
- [Step 3: Test the rule](#eb-api-test-rule "#eb-api-test-rule")
- [Step 4: Confirm success](#success "#success")
- [Step 5: Clean up your resources](#cleanup "#cleanup")

## Step 1: Create an AWS Lambda

function

Create a Lambda function to log the state change [events](eb-events.md "eb-events.md"). When you create your rule in Step 2, you specify this
function.

###### To create a Lambda function

1. Open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose **Create function**.
3. Choose **Author from scratch**.
4. Enter a name and description for the Lambda function. For example, name
   the function `LogEC2InstanceStateChange`.
5. Leave the rest of the options as the defaults and choose **Create function**.
6. On the **Code** tab of the function page, double-click **index.js**.
7. Replace the existing code with the following code.

```
'use strict';

exports.handler = (event, context, callback) => {
    console.log('LogEC2InstanceStateChange');
    console.log('Received event:', JSON.stringify(event, null, 2));
    callback(null, 'Finished');
};
```

8. Choose **Deploy**.

## Step 2: Create a rule

Create a rule to run the Lambda function you created in Step 1. The rule runs when you
launch an Amazon EC2 instance.

###### To create the EventBridge rule

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule. For example, name the rule `TestRule`
5. For **Event bus**, choose the event bus that you want
   to associate with this rule. If you want this rule to match events that come
   from your account, select **default**. When an
   AWS service in your account emits an event, it always goes to your account’s
   default event bus.
6. For **Rule type**, choose **Rule with an event
   pattern**.
7. Choose **Next**.
8. For **Event source**, choose
   **AWS services**.
9. For **Event pattern**, do the following:
   1. For **Event source**, select **EC2** from the drop-down list.
   2. For **Event type**, choose **EC2 Instance
      State-change Notification** from the drop-down list.
   3. Choose **Specific states(s)** and choose **running** from the drop-down list.
   4. Choose **Any instance**

10. Choose **Next**.
11. For **Target types**, choose **AWS service**.
12. For **Select a target**, choose **Lambda
    function** from the drop-down list.
13. For **Function**, select the Lambda function that you created
    in the **Step 1: Create a Lambda function** section. In this example, select `LogEC2InstanceStateChange`.
14. Choose **Next**.
15. Choose **Next**.
16. Review the details of the rule and choose **Create rule**.

## Step 3: Test the rule

You can test your rule by stopping an Amazon EC2 instance using the Amazon EC2 console. Wait a
few minutes for the instance to stop, and then check your AWS Lambda metrics on the CloudWatch
console to verify that your function ran.

###### To test your rule by stopping an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Launch an instance. For more information, see [Launch Your
   Instance](../../../AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.md "../../../AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.md") in the _Amazon EC2 User Guide_.
3. Stop the instance. For more information, see [Stop and Start Your Instance](../../../AWSEC2/latest/UserGuide/Stop_Start.md "../../../AWSEC2/latest/UserGuide/Stop_Start.md") in
   the _Amazon EC2 User Guide_.
4. To view the output from your Lambda function, do the following:
   1. Open the CloudWatch console at
      [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
   2. In the navigation pane, choose **Logs**.
   3. Select the name of the log group for your Lambda function
      (`/aws/lambda/`function-name``).
   4. Select the name of the log stream to view the data provided by the
      function for the instance that you stopped.

5. (Optional) When you're finished, terminate the stopped instance. For more
   information, see [Terminate
   Your Instance](../../../AWSEC2/latest/UserGuide/terminating-instances.md "../../../AWSEC2/latest/UserGuide/terminating-instances.md") in the _Amazon EC2 User Guide_.

## Step 4: Confirm success

If you see the Lambda event in the CloudWatch logs, you've successfully completed this tutorial. If the event isn't in your CloudWatch logs, start troubleshooting by verifying the rule was created successfully
and, if the rule looks correct, verify the code of your Lambda function is correct.

## Step 5: Clean up your resources

You can now delete the resources that you created for this tutorial, unless you want to retain them. By deleting AWS resources that you are no longer using, you prevent unnecessary charges to your AWS account.

###### To delete the EventBridge rule(s)

1. Open the [Rules page](https://console.aws.amazon.com/events/home#/rules "https://console.aws.amazon.com/events/home#/rules") of the EventBridge console.
2. Select the rule(s) that you created.
3. Choose **Delete**.
4. Choose **Delete**.

###### To delete the Lambda function(s)

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Select the function(s) that you created.
3. Choose **Actions**, **Delete**.
4. Choose **Delete**.
