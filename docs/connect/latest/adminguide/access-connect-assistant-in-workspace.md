

# Access Connect assistant in the Connect agent workspace
<a name="access-connect-assistant-in-workspace"></a>

If you're using the CCP that is provided with Connect Customer, after you enable the Connect assistant, share the following URL with your agents so they can access it:
+ **https://{{instance name}}.my.connect.aws/agent-app-v2/**

If you access your instance using the **awsapps.com** domain, use the following URL: 
+ **https://{{instance name}}.awsapps.com/connect/agent-app-v2/**

For help finding your instance name, see [Find your Connect Customer instance name](find-instance-name.md).

By using the new URL, your agents can view the CCP and Connect assistant in the same browser window.

If CCP is embedded in your agent's application, see [Initialization for CCP, Customer Profiles, and Connect assistant](https://github.com/amazon-connect/amazon-connect-streams/blob/master/Documentation.md#initialization-for-ccp-customer-profiles-and-wisdom) in the *Connect Customer Streams Documentation* for information about how to include the Connect assistant. 

For more information about the agent's experience using agent assist, see [Search for content using Connect Customer agent assist](search-for-answers.md).

## Security profile permissions for the Connect assistant
<a name="security-profile-connect-assistant"></a>

Assign the following **Agent Applications** permission to the agent's security profile:
+ **Connect assistant - Access**: Enables agents to search for and view content. They can also receive automatic recommendations during calls if conversational analytics is enabled.

For information about how to add more permissions to an existing security profile, see [Update security profiles in Connect Customer](update-security-profiles.md).

By default, the **Admin** security profile already has permissions to perform all Connect assistant activities.