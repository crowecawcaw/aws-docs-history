

# Disabling (pausing) the stream poller process
<a name="full-text-search-pause-poller"></a>

1. Sign in to the AWS Management Console and open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. In the navigation pane, select **Rules**.

1. Select the rule whose name contains the name you supplied as **Application Name** in the CloudFormation template that you used to set up the stream poller.

1. Choose **Disable**.

1. Open the Step Functions console at [https://console.aws.amazon.com/states/](https://console.aws.amazon.com/states/).

1. Select the running step function that corresponds to the stream poller process. Again, the name of that step function contains the name you supplied as **Application Name** in the CloudFormation template that you used to set up the stream poller. You can filter by function execution status to see only **Running** functions.

1. Choose **Stop**.