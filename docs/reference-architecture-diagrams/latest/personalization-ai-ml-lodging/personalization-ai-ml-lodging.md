# Personalization Using AI/ML for Lodging

Publication date: **August 25, 2022 ([Diagram history](#perslodge-history "#perslodge-history"))**

With this architecture, you can personalize and improve the customer experience for lodging
companies. Proactively recognize service changes and failures, recover from them, and interact
with guests on their preferred channel. The solution uses [Amazon Personalize](../../../personalize/latest/dg.md "../../../personalize/latest/dg.md") for targeted offers, [Amazon Pinpoint](../../../pinpoint/latest/userguide.md "../../../pinpoint/latest/userguide.md") for multi-channel delivery, and [Amazon SageMaker AI](../../../sagemaker/latest/dg.md "../../../sagemaker/latest/dg.md") for custom artificial
intelligence and machine learning (AI/ML) models.

## Personalization AI/ML diagram

![How to personalize customer communications for lodging by using Amazon Personalize, Amazon Pinpoint, and Amazon SageMaker AI.](images/personalization-ai-ml-lodging.png)

The following steps describe the architecture:

1. Build on top of the operational data platform. Use [Amazon Simple Storage Service](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md") as the data lake foundation. Ingest
   data from systems of record through [AWS Transfer Family](../../../transfer/latest/userguide.md "../../../transfer/latest/userguide.md") and AWS Data Exchange. Process data
   by using [AWS Glue](../../../glue/latest/dg.md "../../../glue/latest/dg.md") and [Amazon EMR](../../../emr/latest/ManagementGuide.md "../../../emr/latest/ManagementGuide.md").
2. Use Amazon Pinpoint to deliver operational communications over channels such as email, SMS,
   push, voice, or in-app messaging. Amazon Pinpoint stores all interactions with delivery status for
   tracking. Take into account customer channel preferences.
3. Use Amazon Personalize to create segmentations, target lists, and personalized offers from data
   lake content. Use Amazon Pinpoint to deliver these offers based on customer preferences. Record all
   offers and customer interactions to refine future recommendations.
4. Improve personalization effectiveness by using Master Data Management (MDM)
   integration. Unify guest profiles across systems of record.
5. Create new AI/ML models for customer lifetime value, segmentation, and specialized
   offers. Use SageMaker AI and the raw and curated data in the data lakes. (Optional) Extend the
   capability by adding domains such as point of sale (POS) and survey systems.

## Further reading

For additional information, see the following resources:

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture/ "https://aws.amazon.com/architecture/")
- [AWS
  Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To receive updates about this reference architecture diagram, subscribe to the RSS
feed.

| Change              | Description                                     | Date            |
| ------------------- | ----------------------------------------------- | --------------- |
| Initial publication | Reference architecture diagram first published. | August 25, 2022 |

###### RSS subscription requirement

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you
are using.
