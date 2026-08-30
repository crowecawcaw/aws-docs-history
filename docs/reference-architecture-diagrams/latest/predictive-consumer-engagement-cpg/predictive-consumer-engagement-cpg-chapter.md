# Personalization and Predictive Consumer Engagement for CPG

## Overview

Consumer expectations evolve and behaviors change rapidly. Consumer packaged goods (CPG)
companies have many channels to communicate with consumers. However, sending the right
message at the right time on the right channel remains difficult.

Consumers lose patience with brands that cannot support seamless transitions between
mobile, web, email, SMS, and in-person engagements. This architecture delivers personalized
experiences that surprise and delight your consumers.

Publication date: July 8, 2021

![Data flowing from batch and real-time clickstream sources through AWS Glue DataBrew, Amazon Kinesis, and Amazon Data Firehose into Amazon Simple Storage Service, with Amazon Personalize providing recommendations and Amazon Pinpoint delivering personalized notifications.](images/predictive-consumer-engagement-cpg.png)

**Download:** [Architecture diagram (PDF)](samples/predictive-consumer-engagement-cpg.zip.md "samples/predictive-consumer-engagement-cpg.zip.md")

## Architecture

The following steps describe the architecture:

1. You ingest data into AWS by using batch processing. [AWS GlueDataBrew](../../../databrew/latest/dg.md "../../../databrew/latest/dg.md") cleans and normalizes data. This prepares data for
   analytics and machine learning (ML) applications.
2. [Amazon Kinesis](../../../streams/latest/dev.md "../../../streams/latest/dev.md") captures
   real-time event data. Amazon Data Firehose loads event data into an [Amazon Simple Storage Service
   (Amazon S3)](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md") bucket for potential retraining and future use.
3. The [Amazon Personalize](../../../personalize/latest/dg.md "../../../personalize/latest/dg.md") event tracker
   captures real-time event data. This data is added to the Interactions dataset within
   Amazon Personalize. It updates the model with data from consumers' most recent activity.
4. Three types of input data are stored: interactions (user activity stream data),
   items (descriptions such as category and availability), and users (attributes such as
   age and loyalty membership).
5. Product recommendations are retrieved from Amazon Personalize through a serving layer. The
   recommendations are displayed on the web or mobile.
6. Personalized notifications are sent to consumers through [Amazon Pinpoint](../../../pinpoint/latest/userguide.md "../../../pinpoint/latest/userguide.md"). This
   uses the predictive recommendations from Amazon Personalize for targeted campaigns.

## Diagram history

To receive updates about this reference architecture diagram, subscribe to the RSS
feed.

| Change              | Description                                     | Date         |
| ------------------- | ----------------------------------------------- | ------------ |
| Initial publication | Reference architecture diagram first published. | July 8, 2021 |

###### RSS subscription requirement

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you
are using.
