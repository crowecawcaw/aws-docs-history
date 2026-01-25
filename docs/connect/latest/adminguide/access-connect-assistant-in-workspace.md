# Access Connect assistant in the Connect agent workspace

If you're using the CCP that is provided with Amazon Connect, after you enable the Connect assistant, share the
following URL with your agents so they can access it:

- **https://`instance
 name`.my.connect.aws/agent-app-v2/**
  If you access your instance using the **awsapps.com** domain, use the
  following URL:

- **https://`instance
 name`.awsapps.com/connect/agent-app-v2/**
  For help finding your instance name, see [Find your Amazon Connect instance name](find-instance-name.md "find-instance-name.md").

By using the new URL, your agents can view the CCP and Connect assistant in the same browser
window.

If CCP is embedded in your agent's application, see [Initialization for CCP, Customer Profiles, and Connect assistant](https://github.com/amazon-connect/amazon-connect-streams/blob/master/Documentation.md#initialization-for-ccp-customer-profiles-and-wisdom " https://github.com/amazon-connect/amazon-connect-streams/blob/master/Documentation.md#initialization-for-ccp-customer-profiles-and-wisdom ") in the _Amazon Connect
Streams Documentation_ for information about how to include the Connect assistant.

For more information about the agent's experience using Connect AI agents, see [Search for content using Connect AI agents](search-for-answers.md "search-for-answers.md").

## Security profile permissions for the

Connect assistant

Assign the following **Agent Applications** permission to the agent's
security profile:

- **Connect assistant - Access**: Enables agents to search for and view
  content. They can also receive automatic recommendations during calls if
  Contact Lens conversational analytics is enabled.

For information about how to add more permissions to an existing security profile,
see [Update security profiles in Amazon Connect](update-security-profiles.md "update-security-profiles.md").

By default, the **Admin** security profile already has permissions to
perform all Connect assistant activities.
