**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# How recommendations work in Amazon Pinpoint

In a typical workflow, your team performs a series of activities to create and use a
recommender model with Amazon Pinpoint. In general, those activities are:

1. In Amazon Personalize, create a solution for the model and deploy it as an Amazon Personalize campaign. Then train,
   evaluate, and update the model in a continuous cycle to refine the predictions and
   recommendations that it makes.
2. Configure Amazon Pinpoint to connect to the Amazon Personalize campaign. Use the configuration settings for the
   connection to specify how you want to retrieve and process data from the Amazon Personalize campaign.
3. Create one or more email, push notification, or SMS message templates. Design those
   templates to include message variables that refer to recommended attributes. A _message variable_ is a placeholder that refers to a specific attribute.
   A _recommended attribute_ is an attribute that temporarily
   stores data that Amazon Pinpoint retrieves from an Amazon Personalize campaign.
4. Create one or more Amazon Pinpoint campaigns that use the message templates. Or, if you created email
   templates in the preceding activity, create one or more journey activities that use those
   templates.
   After your team performs these activities, Amazon Pinpoint does the following each time it sends a
   message that includes recommendations from the model:

5. Evaluates the settings and contents of the message and message template.
6. Determines that you connected the message template to a recommender model.
7. Checks the configuration settings that you entered for using the recommender model.
8. Finds one or more message variables for recommended attributes that you created for the
   recommender model.
9. Connects to the Amazon Personalize campaign that you specified in the configuration settings for the
   recommender model.
10. For each message recipient:
    1. Retrieves recommendations from the Amazon Personalize campaign.
    2. Adds the recommendations to the recommended attributes that you created for the
       recommender model.
    3. Replaces each message variable with the corresponding value of the recommended attribute.
       If you configured the model to enhance recommendations by using an AWS Lambda function, Amazon Pinpoint
       uses that function as part of this step.

11. Sends a version of the message that contains the personalized recommendations for each
    message recipient.
