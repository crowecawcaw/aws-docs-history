

# Configure automatic renewal events
<a name="configure-auto-renewals-events"></a>

With AWS Certificate Manager exportable public certificates and Amazon EventBridge, you can configure automatic certificate renewals events.

1. Set up an Amazon EventBridge event to monitor certificate renewals. For more information, see [Amazon EventBridge support for ACM](https://docs.aws.amazon.com/acm/latest/userguide/cloudwatch-events.html).

1. Create automation to handle certificate deployment when renewals occur. For more information, see [Initiating actions with Amazon EventBridge in ACM](example-actions.md).

1. Configure EventBridge events to alert you of any renewal or deployment failures.