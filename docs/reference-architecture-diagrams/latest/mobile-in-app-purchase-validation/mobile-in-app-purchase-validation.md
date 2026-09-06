

# Mobile In-App Purchase Validation on AWS
<a name="mobile-in-app-purchase-validation"></a>

Publication date: **January 1, 2021 ([Diagram history](#iap-history))**

This architecture provides a serverless solution for validating in-app purchases from the Google Play Store and Apple App Store, and for managing refunds. The architecture uses [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), and [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) to process transactions securely at scale.

## Mobile In-App Purchase Validation on AWS diagram
<a name="iap-diagram"></a>

![Reference architecture diagram showing how to validate in-app purchases and manage refunds on AWS with a serverless backend.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/mobile-in-app-purchase-validation/images/mobile-in-app-purchase-validation.png)


The following steps describe the purchase validation flow:

1. The mobile game client makes a purchase by using the OS-specific SDK and stores the receipt locally.

1. The game client makes an API request to API Gateway to validate the receipt and receive purchased items.

1. The Lambda function checks the **Transactions** table in DynamoDB to validate that the receipt has not been used previously.

1. The Lambda function validates the receipt through the Google Play Store or Apple App Store API.

1. After validation, the Lambda function adds items to the **PlayerData** table in DynamoDB and adds the receipt to the **Transactions** table with any additional metadata.

1. The client receives a success message, locally synchronizes the purchased items data, and deletes the local receipt copy.

The following steps describe the refund flow:

1. API Gateway receives notifications on refunded transactions on iOS. A scheduled Lambda function queries refunded transactions on Android.

1. Refunded transactions are pushed to an [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/) queue by the Lambda functions.

1. A Lambda function handles the refund, including any additional actions like closing the player account.

1. A Lambda function updates the DynamoDB tables to remove items and mark the transaction as refunded.

## Further reading
<a name="iap-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="iap-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#iap-history) | Reference architecture diagram first published. | January 1, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.