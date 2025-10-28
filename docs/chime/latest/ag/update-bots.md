**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Update chatbots

As the Amazon Chime account administrator, you can use the Amazon Chime API with the AWS SDK or
AWS CLI to view your chatbot details. You can also enable or stop your chatbots from
being used in your account. You can also regenerate security tokens for your chatbot.

For more information, see the following topics in the _Amazon Chime API Reference_:

- [GetBot](../APIReference/API_GetBot.md "../APIReference/API_GetBot.md") – Gets your chatbot details, such as bot email address and bot type.
- [UpdateBot](../APIReference/API_UpdateBot.md "../APIReference/API_UpdateBot.md") – Enables or stops a chatbot from being used in your account.
- [RegenerateSecurityToken](../APIReference/API_RegenerateSecurityToken.md "../APIReference/API_RegenerateSecurityToken.md") – Regenerates the security token for your chatbot.
  You can also change the `PutEventsConfiguration` for your chatbot. For
  example, if your chatbot was initially configured to use an outbound HTTPS
  endpoint, you can delete the previous events configuration and put a new events
  configuration for a Lambda function ARN.

For more information, see the following topics in the _Amazon Chime API Reference_:

- [DeleteEventsConfiguration](../APIReference/API_DeleteEventsConfiguration.md "../APIReference/API_DeleteEventsConfiguration.md")
- [PutEventsConfiguration](../APIReference/API_PutEventsConfiguration.md "../APIReference/API_PutEventsConfiguration.md")
