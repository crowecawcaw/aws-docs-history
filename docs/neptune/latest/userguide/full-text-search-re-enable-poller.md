# Re-enabling the stream poller process

1. Sign in to the AWS Management Console and open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, select **Rules**.
3. Select the rule whose name contains the name you supplied as **Application
   Name** in the CloudFormation template that you used to set up the stream poller.
4. Choose **Disable**. The event rule based on the specified
   scheduled interval will now trigger a new execution of the step function.
