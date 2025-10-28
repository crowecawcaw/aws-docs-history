**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Use a recommender model in Amazon Pinpoint with AWS Lambda

In Amazon Pinpoint, you can retrieve personalized recommendations from a recommender model and add
them to messages that you send from campaigns and journeys. A _recommender model_ is a type of machine learning (ML) model that finds patterns in
data and generates predictions and recommendations based on the patterns that it finds. It
predicts what a particular user will prefer from a given set of products or items, and it
provides that information as a set of recommendations for the user.

By using recommender models with Amazon Pinpoint, you can send personalized recommendations to
message recipients based on each recipient’s attributes and behavior. With AWS Lambda, you can
also customize and enhance these recommendations. For example, you can dynamically transform a
recommendation from a single text value (such as a product name or ID) to more sophisticated
content (such as a product name, description, and image). And you can do it in real time, when
Amazon Pinpoint sends the message.

This feature is available in the following AWS Regions: US East (N. Virginia);
US West (Oregon); Asia Pacific (Mumbai); Asia Pacific (Sydney); and,
Europe (Ireland).

## Authorize Amazon Pinpoint to invoke a Lambda

function using the AWS CLI and the Lambda add-permission command

After you assign a Lambda function policy to a function, you can add permissions that
allow Amazon Pinpoint to invoke the function for a specific project, campaign, or journey. You can do
this using the AWS Command Line Interface (AWS CLI) and the Lambda [`add-permission`](../../../cli/latest/reference/lambda/add-permission.md "../../../cli/latest/reference/lambda/add-permission.md") command.
The following example shows how to do this for a specific project
(`projectId`):

```
`$` `aws lambda add-permission \
--function-name `function-name` \
--statement-id `sid` \
--action lambda:InvokeFunction \
--principal pinpoint.us-east-1.amazonaws.com \
--source-arn arn:aws:mobiletargeting:us-east-1:`accountId`:recommenders/*`
```

The preceding example is formatted for Unix, Linux, and macOS. For Microsoft Windows,
replace the backslash (\) line-continuation character with a caret (^).

If the command runs successfully, you see output similar to the following:

```
`{
 "Statement": "{\"Sid\":\"sid\",
 \"Effect\":\"Allow\",
 \"Principal\":{\"Service\":\"pinpoint.us-east-1.amazonaws.com\"},
 \"Action\":\"lambda:InvokeFunction\",
 \"Resource\":\"arn:aws:lambda:us-east-1:111122223333:function:function-name\",
 \"Condition\":
 {\"ArnLike\":
 {\"AWS:SourceArn\":
 \"arn:aws:mobiletargeting:us-east-1:111122223333:recommenders/*\"}}}"
}`
```

The `Statement` value is a JSON string version of the statement that was added
to the Lambda function policy.

## Configure Amazon Pinpoint to invoke the Lambda function for a recommender model

To configure Amazon Pinpoint to invoke the Lambda function for a recommender model, specify the
following Lambda-specific configuration settings for the model:

- `RecommendationTransformerUri` – This property specifies the name or
  Amazon Resource Name (ARN) of the Lambda function.
- `Attributes` – This object is a map that defines the custom
  recommended attributes that the function adds to each endpoint definition. Each of these
  attributes can be used as a message variable in a message template.

You can specify these settings by using the [Recommender Models](../apireference/recommenders.md "../apireference/recommenders.md") resource of the Amazon Pinpoint API (when you create the configuration for
a model) or the [Recommender
Model](../apireference/recommenders-recommender-id.md "../apireference/recommenders-recommender-id.md") resource of the Amazon Pinpoint API (if you update the configuration for a model). You
can also define these settings by using the Amazon Pinpoint console.

For more information about using recommender models with Amazon Pinpoint, see [Machine Learning Models](../userguide/ml-models.md "../userguide/ml-models.md") in the _Amazon Pinpoint User Guide_.
