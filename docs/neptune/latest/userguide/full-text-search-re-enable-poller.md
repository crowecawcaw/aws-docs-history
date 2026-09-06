

# Re-enabling the stream poller process
<a name="full-text-search-re-enable-poller"></a>

1. Sign in to the AWS Management Console and open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. In the navigation pane, select **Rules**.

1. Select the rule whose name contains the name you supplied as **Application Name** in the CloudFormation template that you used to set up the stream poller.

1. Choose **Enable**. The event rule based on the specified scheduled interval will now trigger a new execution of the step function.