# Enable authentication for Apple Messages for Business

To begin the setup process, first navigate to your Identity Provider.

## Identity Provider Configuration

The following Connect Customer domain must be registered as an allowed Redirect URI for the
Identity Provider(s) used for authentication:

```
https://participant.connect.`region`.amazonaws.com/participant/authentication/update

```

## Integration with Amazon Cognito

You can [add your Identity Provider(s)](../../../cognito/latest/developerguide/cognito-user-pools-identity-provider.md "../../../cognito/latest/developerguide/cognito-user-pools-identity-provider.md") to an existing Amazon Cognito user pool or create
a new [Amazon Cognito user
pools](../../../cognito/latest/developerguide/cognito-user-identity-pools.md "../../../cognito/latest/developerguide/cognito-user-identity-pools.md").

Within this user pool you can create an [app
client](../../../cognito/latest/developerguide/user-pool-settings-client-apps.md "../../../cognito/latest/developerguide/user-pool-settings-client-apps.md") and select some or all of your Identity Providers. Take note of
the app client's client ID. For this app client, the following Connect Customer domain must be
added as an Allowed callback URL:

```
https://participant.connect.`region`.amazonaws.com/participant/authentication/update

```

###### Note

You must select **Don't generate a client secret**  when
configuring the Amazon Cognito app client. Only Amazon Cognito app clients without client secrets
are supported.

## Configure your Amazon Cognito app client with the Apple Messages for Business Portal

On **Integrated OAuth2 Authentication**, configure your Amazon Cognito
app client client ID as the **Client Identifier** and your Amazon Cognito
user pool domain's [authorization
endpoint](../../../cognito/latest/developerguide/authorization-endpoint.md "../../../cognito/latest/developerguide/authorization-endpoint.md") as the **OAuth URL**.

![Customer authentication for Amazon Cognito user pools.](images/configuring-your-cognito-app-client-with-the-apple-messages-for-business-portal.png)

## Configure your user pools with Connect Customer

On the **Customer authentication** page on the Connect Customer console
associate the user pool that will be used for the authentication.

![Customer authentication for Amazon Cognito user pools.](images/configuring-your-user-pools-with-connect.png)

## Enable Connect Customer Customer Profiles

**Enable Customer Profiles**

On the **Customer Profiles** page in Connect Customer console, make sure that
Customer Profiles is enabled for your instance. If **No Customer Profiles domain associated with this
instance of Connect Customer.** is displayed, then see [Enable Customer Profiles for your Connect Customer instance](enable-customer-profiles.md "enable-customer-profiles.md").

![Enable customer profiles in the Connect Customer console.](images/apple-messages-for-business-configuring-amazon-connect-customer-profiles.png)

### Grant Customer Profile permission(s) to security profiles (optional)

To grant users (agent, admin) permissions to view/edit/publish Customer
Profiles in Agent Workspace, see [Update Customer Profiles permissions for agents](security-profile-customer-profile-agent.md "security-profile-customer-profile-agent.md"). After
permission(s) are granted to security profile(s), users should be able to access
the features in the Agent Workspace.

For a detailed list of permissions, see [Customer Profiles security profile
permissions](security-profile-list.md#customerprofiles-permissions-list "security-profile-list.md#customerprofiles-permissions-list").

## Configure the Authenticate Customer flow block

For instructions, see [Flow block in Connect Customer: Authenticate Customer](authenticate-customer.md "authenticate-customer.md").
