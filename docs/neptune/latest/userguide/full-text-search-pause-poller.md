# Disabling (pausing) the stream poller process

1. Sign in to the AWS Management Console and open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, select **Rules**.
3. Select the rule whose name contains the name you supplied as **Application
   Name** in the CloudFormation template that you used to set up the stream poller.
4. Choose **Disable**.
5. Open the Step Functions console at
   [https://console.aws.amazon.com/states/](https://console.aws.amazon.com/states/ "https://console.aws.amazon.com/states/").
6. Select the running step function that corresponds to the stream poller process.
   Again, the name of that step function contains the name you supplied as **Application
   Name** in the CloudFormation template that you used to set up the stream poller. You can
   filter by function execution status to see only **Running** functions.
7. Choose **Stop**.
