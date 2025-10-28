# Configure automatic renewal

events

With AWS Certificate Manager exportable public certificates and Amazon EventBridge, you can configure automatic certificate
renewals events.

1. Set up an Amazon EventBridge event to monitor certificate renewals. For more
   information, see [Amazon EventBridge support for
   ACM](cloudwatch-events.md "cloudwatch-events.md").
2. Create automation to handle certificate deployment when renewals occur. For
   more information, see [Initiating actions with Amazon EventBridge in ACM](example-actions.md "example-actions.md").
3. Configure EventBridge events to alert you of any renewal or deployment
   failures.
