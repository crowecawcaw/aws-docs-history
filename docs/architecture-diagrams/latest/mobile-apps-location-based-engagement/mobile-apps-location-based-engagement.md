# Mobile Apps for Location-based Engagement

Publication date: **July 8, 2021 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture is built around Amazon Location Service features such as maps, trackers, and geofence collections. Mobile users carry their devices all the time and everywhere. Adding location awareness to apps enables you to offer an enhanced experience, such as sending real-time messages and information based on user location.

## Mobile Apps for Location-based engagement

![Reference architecture diagram showing how Amazon Location Service can be used to add location awareness to apps to enable you to offer an enhanced experience, such as sending real-time messages and information based on user location.](images/mobile-apps-location-based-engagement.png)

1. A web app deployed by **AWS Amplify** is used by
   operations and business users to create messages, business rules for engagements, and
   geofences that initiate messages.
2. Operations are performed via a GraphQL API provided by **AWS AppSync**, to interact with a single API and a standardized access layer. The
   web app leverages **Amplify** libraries to make requests to
   **AWS AppSync**.
3. Data for messages and rules is stored in **DynamoDB**
   tables.
4. When creating a rule for engagements, an **AWS Lambda**
   function also creates a geofence on a Geofence collection.
5. The mobile app leverages **Amplify** libraries to make
   requests to the **AWS AppSync** API. Geolocations are sent to a
   tracker to follow the device’s position.
6. Position is evaluated against geofences. Events are initiated on **Amazon EventBridge** when a device enters or exits a geofence.
7. A **Lambda** function processes events and notifies users
   either via **AWS AppSync** or **Amazon Pinpoint**.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/mobile-apps-location-based-engagement.md "samples/mobile-apps-location-based-engagement.md").

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date         |
| ------------------- | ----------------------------------------------- | ------------ |
| Initial publication | Reference architecture diagram first published. | July 8, 2021 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
