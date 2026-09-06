

# Provide DaaS to Fleet Customers: Subscription flow
<a name="provide-daas-subscription"></a>

Publication date: **February 16, 2023 ([Diagram history](#daas-sub-history))**

With this architecture, you can onboard new fleet customers requesting data subscriptions. Manage subscriptions for specific vehicle data packages such as alerts, telematics, and diagnostics. The solution uses [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) for the subscription API, [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) for processing, and [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) for resource provisioning.

## DaaS subscription flow diagram
<a name="daas-sub-diagram"></a>

![Reference architecture diagram showing DaaS subscription management by using Amazon API Gateway, Lambda, and AWS Step Functions.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/provide-daas-to-fleet-customers/images/provide-daas-subscription.png)


The following steps describe the subscription onboarding workflow for this architecture:

1. Invoke the Subscription API through Amazon API Gateway to onboard new customers. Request subscriptions for specific vehicle data packages (such as VIN, Customer ID, alerts, or telematics data).

1. Store customer data subscription request details in the [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) database by using Lambda.

1. Upload or update bulk reference data (such as customer-to-vehicle VIN mapping) into an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) bucket. Load the data into the database with Lambda.

1. Invoke a workflow to provision customer-specific AWS resources with AWS Step Functions. Create resources such as customer-specific [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/) queues or [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) rules.

## Further reading
<a name="daas-sub-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="daas-sub-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](provide-daas-data-flow.md#daas-flow-history) | Reference architecture diagram first published. | February 16, 2023 | 
| [Initial publication](#daas-sub-history) | Reference architecture diagram first published. | February 16, 2023 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.