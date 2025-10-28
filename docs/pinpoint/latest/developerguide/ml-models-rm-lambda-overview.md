**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Add recommender model recommendations to messages in Amazon Pinpoint

To use a recommender model with Amazon Pinpoint, you start by creating an Amazon Personalize solution and
deploying that solution as an Amazon Personalize campaign. Then, you create a configuration for the
recommender model in Amazon Pinpoint. In the configuration, you specify settings that determine how to
retrieve and process recommendation data from the Amazon Personalize campaign. This includes whether to
invoke an AWS Lambda function to perform additional processing of the data that's
retrieved.

Amazon Personalize is an AWS service that's designed to help you create ML models that provide
real-time, personalized recommendations for customers who use your applications. Amazon Personalize guides
you through the process of creating and training an ML model, and then preparing and deploying
the model as an Amazon Personalize campaign. You can then retrieve real-time, personalized recommendations
from the campaign. To learn more about Amazon Personalize, see the [Amazon Personalize Developer Guide](../../../personalize/latest/dg/what-is-personalize.md "../../../personalize/latest/dg/what-is-personalize.md").

AWS Lambda is a compute service that you can use to run code without provisioning or
managing servers. You package your code and upload it to AWS Lambda as a _Lambda function_. AWS Lambda then runs the function when the function
is invoked. A function can be invoked manually by you, automatically in response to events, or
in response to requests from applications or services, including Amazon Pinpoint. For information about
creating and invoking Lambda functions, see the [AWS Lambda Developer Guide](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md").

After you create an Amazon Pinpoint configuration for a recommender model, you can add
recommendations from the model to messages that you send from campaigns and journeys. You do
this by using message templates that contain message variables for recommended attributes. A
_recommended attribute_ is a dynamic endpoint or user
attribute that's designed to store recommendation data. You define these attributes when you
create the configuration for a recommender model.

You can use variables for recommended attributes in the following types of message
templates:

- Email templates, for email messages that you send from campaigns or journeys.
- Push notification templates, for push notifications that you send from
  campaigns.
- SMS templates, for SMS text messages that you send from campaigns.
  For more information about using recommender models with Amazon Pinpoint, see [Machine Learning Models](../userguide/ml-models.md "../userguide/ml-models.md") in the _Amazon Pinpoint User Guide_.

If you configure Amazon Pinpoint to invoke a Lambda function that processes recommendation data,
Amazon Pinpoint performs the following general tasks each time it sends personalized recommendations in
a message for a campaign or journey:

1. Evaluates and processes the configuration settings and contents of the message and
   message template.
2. Determines that the message template is connected to a recommender model.
3. Evaluates the configuration settings for connecting to and using the model. These are
   defined by the [Recommender
   Model](../apireference/recommenders-recommender-id.md "../apireference/recommenders-recommender-id.md") resource for the model.
4. Detects one or more message variables for recommended attributes that are defined by
   the configuration settings for the model.
5. Retrieves recommendation data from the Amazon Personalize campaign that's specified in the
   configuration settings for the model. It uses the [GetRecommendations](../../../personalize/latest/dg/API_RS_GetRecommendations.md "../../../personalize/latest/dg/API_RS_GetRecommendations.md") operation
   of the Amazon Personalize Runtime API to perform this task.
6. Adds the appropriate recommendation data to a dynamic recommended attribute
   (`RecommendationItems`) for each message recipient.
7. Invokes your Lambda function and sends the recommendation data for each recipient to
   that function for processing.

The data is sent as a JSON object that contains the endpoint definition for each
recipient. Each endpoint definition includes a `RecommendationItems` field that
contains an ordered array of 1–5 values. The number of values in the array depends
on the configuration settings for the model. 8. Waits for your Lambda function to process the data and return the results.

The results are a JSON object that contains an updated endpoint definition for each
recipient. Each updated endpoint definition contains a new `Recommendations`
object. This object contains 1–10 fields, one for each custom recommended attribute
that you defined in the configuration settings for the model. Each of these fields stores
enhanced recommendation data for the endpoint. 9. Uses the updated endpoint definition for each recipient to replace each message
variable with the appropriate value for that recipient. 10. Sends a version of the message that contains the personalized recommendations for each
message recipient.
To customize and enhance recommendations in this way, start by creating a Lambda function
that processes the endpoint definitions sent by Amazon Pinpoint, and returns updated endpoint
definitions. Next, assign a Lambda function policy to the function and authorize Amazon Pinpoint to
invoke the function. Then, configure the recommender model in Amazon Pinpoint. When you configure the
model, specify the function to invoke and define the recommended attributes to use.
