

# Mobile Apps for Location-based Engagement
<a name="mobile-apps-location-based-engagement"></a>

Publication date: **July 8, 2021 ([Diagram history](#diagram-history))**

This architecture is built around Amazon Location Service features such as maps, trackers, and geofence collections. Mobile users carry their devices all the time and everywhere. Adding location awareness to apps enables you to offer an enhanced experience, such as sending real-time messages and information based on user location. 

## Mobile Apps for Location-based engagement
<a name="diagram1"></a>

![Reference architecture diagram showing how Amazon Location Service can be used to add location awareness to apps to enable you to offer an enhanced experience, such as sending real-time messages and information based on user location.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/mobile-apps-location-based-engagement/images/mobile-apps-location-based-engagement.png)


1. A web app deployed by **AWS Amplify** is used by operations and business users to create messages, business rules for engagements, and geofences that initiate messages. 

1. Operations are performed via a GraphQL API provided by **AWS AppSync**, to interact with a single API and a standardized access layer. The web app leverages **Amplify** libraries to make requests to **AWS AppSync**. 

1. Data for messages and rules is stored in **DynamoDB** tables. 

1. When creating a rule for engagements, an **AWS Lambda** function also creates a geofence on a Geofence collection. 

1. The mobile app leverages **Amplify** libraries to make requests to the **AWS AppSync** API. Geolocations are sent to a tracker to follow the device’s position. 

1. Position is evaluated against geofences. Events are initiated on **Amazon EventBridge** when a device enters or exits a geofence. 

1. A **Lambda** function processes events and notifies users either via **AWS AppSync** or **Amazon Pinpoint**. 

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | July 8, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.