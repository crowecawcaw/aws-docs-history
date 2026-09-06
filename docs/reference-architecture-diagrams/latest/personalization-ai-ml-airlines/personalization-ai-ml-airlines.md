

# Personalization Using AI/ML for Airlines
<a name="personalization-ai-ml-airlines"></a>

Publication date: **November 14, 2019 ([Diagram history](#personalization-airlines-history))**

With this architecture, you can personalize customer communications for airlines. Airlines often require multiple providers to build separate operational email, notification, and campaign systems. These systems typically do not work well together. They do not scale to meet new data feeds and new channels of communication.

This personalization workflow addresses these challenges by integrating multiple AWS services to personalize the customer communication experience. This reference architecture uses the [Traveler 360 Data Platform for Airlines](../traveler-360-airlines/traveler-360-airlines.html) as its foundation. It offers personalization with artificial intelligence (AI) and machine learning (ML) services.

## Personalization AI/ML for airlines diagram
<a name="personalization-airlines-diagram"></a>

![Architecture for airline personalization using Amazon Personalize, Amazon Pinpoint, and Amazon SageMaker AI.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/personalization-ai-ml-airlines/images/personalization_ai-ml-travel_ra.png)


The following steps describe the architecture:

1. Use [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/userguide/) for operational and notification communications. Deliver messages across email, SMS, voice, and push channels.

1. Use [Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/) for segmentation, target lists, and personalized offers from the data lake. Use Amazon Pinpoint to deliver those personalized offers.

1. Improve effectiveness with master data management (MDM) integration. MDM provides a unified traveler profile for accurate targeting.

1. Extend capability by adding shopping data, baggage sortation, and baggage reconciliation domains to the data platform.

1. Create new artificial intelligence and machine learning (AI/ML) models. Use [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for customer lifetime value and segmentation models.

## Further reading
<a name="personalization-airlines-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="personalization-airlines-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#personalization-airlines-history) | Reference architecture diagram first published. | November 14, 2019 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.