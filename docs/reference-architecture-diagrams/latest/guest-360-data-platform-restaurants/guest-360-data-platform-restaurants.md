

# Guest 360 Data Platform for Restaurants
<a name="guest-360-data-platform-restaurants"></a>

Publication date: **November 17, 2020 ([Diagram history](#g360rest-history))**

With this architecture, you can build a guest 360-degree data platform for restaurant companies. Identify known and unknown guests across all channels. Use guest interaction activity to create personalized offers, campaigns, and acquisition strategies. The solution combines Master Data Management (MDM) and Customer Data Platform (CDP) capabilities with [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/), and [Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/).

## Guest 360 restaurants diagram
<a name="g360rest-diagram"></a>

![How to build a guest 360-degree data platform for restaurants by using AWS services.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/guest-360-data-platform-restaurants/images/guest-360-data-platform-restaurants.png)


The following steps describe the architecture:

1. Build the restaurant data platform with critical data domains such as orders, loyalty, and locations.

1. Use MDM tools to create a unified guest profile. Identify loyalty and reward members and guests based on attributes provided during purchases and registration.

1. Use CDP tag management and first-party cookies to collect activity on web and mobile channels. Identify anonymous users. (Optional) Use third-party cookies and mobile device IDs to augment activity data. Add first-party loyalty and unified guest data to identify known and anonymous guests.

1. Use open standards to build the data lake by using Amazon Simple Storage Service, AWS Glue, and [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/). Process and curate all guest activity in the data lake, including loyalty, purchases, marketing interactions, and web and mobile interactions.

1. Use [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) and serverless architecture to deliver microservices and events for an operational data store. Use guest 360-degree microservices and business events to personalize guest offers.

1. Derive insights from the data lake to create outbound campaigns by using [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/userguide/) and Amazon Personalize. Create inbound campaigns on web and mobile by using Amazon Personalize.

1. Use CDP integrations with Demand Side Platforms (DSPs) and ad exchanges. Create and run customer acquisition campaigns and measure results.

## Further reading
<a name="g360rest-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="g360rest-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#g360rest-history) | Reference architecture diagram first published. | November 17, 2020 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.