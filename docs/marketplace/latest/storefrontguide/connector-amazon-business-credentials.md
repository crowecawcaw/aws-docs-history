

# Getting Amazon Business API credentials
<a name="connector-amazon-business-credentials"></a>

The connector uses an Amazon Business API application registered for your business. The application authorizes access through Login with Amazon (LWA). To authorize the application, your Amazon Business administrator must administer all legal entities under that Amazon Business account.

**To get the API credentials**

1. Sign in to the Solution Provider Portal, find your app, and choose **View** under **LWA credentials**. For instructions, see [View your app information and credentials](https://developer-docs.amazon.com/amazon-business/docs/viewing-your-application-information-and-credentials) on the Amazon Business API documentation website.

1. Copy the **LWA client ID** and the matching **client secret**. Keep them private.

1. Start the authorization with the app's registered application ID and exact redirect URI. For instructions, see [Authorize your Amazon Business API apps](https://developer-docs.amazon.com/amazon-business/docs/step-1-authorize-your-amazon-business-api-apps) on the Amazon Business API documentation website. The application ID used for consent is different from the LWA client ID.

1. Have your Amazon Business administrator sign in to the intended business and choose **Allow**.

1. Have your API application administrator complete the authorization code exchange in Amazon's instructions and securely store the returned refresh token. For more information, see [Refresh tokens](https://developer.amazon.com/docs/login-with-amazon/refresh-token.html) on the Login with Amazon documentation website.

You enter the following values in the connector.


| Value | Source | 
| --- | --- | 
|  **LWA client ID**  | The client identifier from your API application's LWA credentials | 
|  **LWA client secret**  | The matching secret from the same application | 
|  **Refresh token**  | The token returned after your business authorizes that application | 

**Use matching credentials**  
All three values must belong to the same application and business authorization. AWS Marketplace Storefront gets access tokens for you, so enter the **refresh token** in the connector, not an access token. Never include credentials in screenshots or support messages.

The connector test verifies API access. For instructions, see [Configuring the Amazon Business connector](connector-amazon-business-configure.md).

## Related topics
<a name="connector-amazon-business-credentials-related"></a>
+  [Amazon Business connector](connector-amazon-business.md) 
+  [Configuring the Amazon Business connector](connector-amazon-business-configure.md) 