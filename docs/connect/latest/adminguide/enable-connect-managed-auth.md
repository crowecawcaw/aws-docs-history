# Enable customer authentication for hosted

communication widgets

This topic explains how to set up authentication if you're using the Amazon Connect hosted
communication widget for chat. You enable customer authentication for your Amazon Connect
instance, and then enable an authentication message that displays a link which opens a
popup to the Amazon Cognito hosted UI.

## Required IAM policies

If you use custom IAM policies to manage access to the Amazon Connect console, see [Required permissions
for custom IAM policies](security-iam-amazon-connect-permissions.md "security-iam-amazon-connect-permissions.md") for a list of
the permissions needed to access the **Customer authentication**
page.

## Enable customer authentication in your Amazon Connect

instance

1. Open the Amazon Connect console at
   [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/ "https://console.aws.amazon.com/connect/").
2. On the instances page, choose the instance alias. The instance alias is also
   your **instance name**, which appears in your Amazon Connect
   URL. The following image shows the **Amazon Connect virtual contact center instances** page, with a box
   around the instance alias.

![The Amazon Connect virtual contact center instances page, the instance alias.](images/instance.png) 3. On the left navigation menu, choose **Applications**,
**Customer Authentication**. If you don't see this
option, it may not be available in your AWS Region. For information about
where customer authentication is available, see [Customer authentication availability by
Region](regions.md#customerauthentication_region "regions.md#customerauthentication_region"). 4. On the **Customer authentication** page, choose
**Create user pool in Amazon Cognito**. This opens the Amazon Cognito
console. 5. Create a new user pool with your identity provider. For instructions, see
[Getting started with user pools](../../../cognito/latest/developerguide/getting-started-user-pools.md "../../../cognito/latest/developerguide/getting-started-user-pools.md") in the _Amazon Cognito
Developer Guide_.

###### Note

You must select **Don't generate a client secret**
when you configure your Amazon Cognito app client. Only Amazon Cognito app clients without
client secrets are supported. For more information, see [Application-specific settings with app clients](../../../cognito/latest/developerguide/user-pool-settings-client-apps.md "../../../cognito/latest/developerguide/user-pool-settings-client-apps.md") in the
_Amazon Cognito Developer Guide_. 6. After you have created an Amazon Cognito user pool, return to the
**Customer authentication** page and choose
**Associate User Pool**. 7. In the **User Pool** section, choose the user pool you
created from the dropdown menu, and then choose
**Confirm**.

This associates the user pool to your Amazon Connect instance. It enables the [Authenticate Customer](authenticate-customer.md "authenticate-customer.md") flow block to access the
user pool. 8. Continue to the next step: [Enable the authentication message](#enable-auth-message "#enable-auth-message").

## Enable the authentication message

To enable the authentication message, add the authentication parameters snippet
variable at the end of your snippet. For information about adding snippet variables,
see [Supported widget snippet fields in Amazon Connect that are
customizable](supported-snippet-fields.md "supported-snippet-fields.md"). The following code is an example of
the authentication parameters snippet you need to add.

```
amazon_connect('authenticationParameters', {
    redirectUri: '`your_redirect_url`', // https://example.com
    identityProvider: '`your_identity_provider_name`' //optional
 });
```

Where:

- `redirectUri` is the redirect URI you configured in your IdP
  (Identity Provider) and Amazon Cognito. This is where your customer is automatically
  directed after signing in. In this page you can check the URL parameters and
  if there is a code and state, you can call the [UpdateParticipantAuthentication](../APIReference/API_UpdateParticipantAuthentication.md "../APIReference/API_UpdateParticipantAuthentication.md") API with those values. After
  the API call completes, close the popup; the customer is returned to the
  chat experience.
- `identityProvider` is the identity provider name you configured
  in Amazon Cognito. This field is optional. If a value is provided, then the sign in
  link automatically directs the customer to the login page of the identity
  provider instead of to the Amazon Cognito-managed login page where they would have to
  select an identity provider to use for login.

When the flow reaches the [Authenticate Customer](authenticate-customer.md "authenticate-customer.md") block, you can register a callback
and store the state locally to validate in the redirect URI, as shown in the
following example code snippet:

```
amazon_connect('registerCallback', {
       'AUTHENTICATION_INITIATED' : (eventName, data) => {
            console.log(data.state)
        },
      });
```

After you enable customer authentication, add an [Authenticate Customer](authenticate-customer.md "authenticate-customer.md")
block to your flow. This block authenticates chat contacts during the flow, and
route them to specific paths based on the authentication result.
