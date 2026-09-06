

# Manage worker subscriptions
<a name="workteam-private-sns-manage-topic"></a>

If you subscribe a work team to a topic after you've already created the work team, the individual work team members who were added to the team when the work team was created are not automatically subscribed to the topic. For information about subscribing workers' email addresses to the topic, see [Subscribing an Endpoint to an Amazon SNS Topic](https://docs.aws.amazon.com/sns/latest/dg/sns-tutorial-create-subscribe-endpoint-to-topic.html) in the *Amazon SNS Developer Guide*.

The only situation in which workers are automatically subscribed to your topic is when you create or import an Amazon Cognito user group at the time that you create a work team ***and*** you set up the topic subscription when you create that work team. For more information about creating and managing your workteams with Amazon Cognito, see [Create Work Teams (Amazon Cognito Console)](sms-workforce-management-private-cognito.md#create-work-teams-cog).