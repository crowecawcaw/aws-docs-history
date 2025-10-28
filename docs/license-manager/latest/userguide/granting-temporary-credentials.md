# Get temporary credentials for ISV customers

without an AWS account

For customers without an AWS account, you can use entitlements in the same manner that
you do for your customers with an AWS account. Use the following procedure to get
temporary AWS credentials for your customers without an AWS account. The API calls must
be made in the home Region.

###### To get temporary credentials to use in calling the License Manager API

1. Call the [CreateToken](../APIReference/API_CreateToken.md "../APIReference/API_CreateToken.md") API
   action to get a refresh token encoded as a JWT token.
2. Call the [GetAccessToken](../APIReference/API_GetAccessToken.md "../APIReference/API_GetAccessToken.md")
   API action, specifying the refresh token that you received from
   `CreateToken` in the previous step, to receive a temporary access
   token.
3. Call the [AssumeRoleWithWebIdentity](../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md "../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md") API action, specifying the access token that
   you received from `GetAccessToken` in the previous step, and the
   **AWSLicenseManagerConsumptionRole** role that you created, to
   get temporary AWS credentials.

###### To create a token from the AWS License Manager console

1. From the [License Manager
   console](https://console.aws.amazon.com/license-manager "https://console.aws.amazon.com/license-manager"), navigate to the License details page for the specific license
   entitlement you want to use without an AWS account.
2. Choose **Create token** to generate a temporary access
   token.

###### Note

The first time you generate a temporary access token, you will be asked to
create a service role so that License Manager can access services on your behalf. The
following service role is created:
`AWSLicenseManagerConsumptionRole`. 3. Download the `token.csv` file, or copy the token string when it is
generated.

###### Important

This is the only time you can view or download this token. We recommend that
you download the token and store the file in a secure location. You can create new
tokens at any time, up to the [service
limit](https://console.aws.amazon.com/servicequotas/home/services/license-manager/quotas "https://console.aws.amazon.com/servicequotas/home/services/license-manager/quotas").
