# Salesforce Client Secret

## Secret Value Fields

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "consumerKey": "`client ID`",
  "consumerSecret": "`client secret`",
  "baseUri": "https://`domain`.my.salesforce.com",
  "appId": "`app ID`",
  "consumerId": "`consumer ID`"
}
```

consumerKey

The consumer key, also known as the client ID, is the credential identifier
for the OAuth 2.0 credentials. You can retrieve the consumer key directly from the Salesforce
External Client App Manager OAuth settings.

consumerSecret

The consumer secret, also known as the client secret, is the private password used with the
consumer key to authenticate using the OAuth 2.0 client credentials flow. You can retrieve the consumer
secret directly from the Salesforce External Client App Manager OAuth settings..

baseUri

The base URI is your Salesforce Org's base URL used to interact with Salesforce APIs. This takes the form of the following example:
`https://`domainName`.my.salesforce.com`.

appId

The App ID is the identifier for your Salesforce External Client Application (ECA).
You can retrieve this by calling the Salesforce OAuth Usage endpoint. It
must begin with `0x` and contain only alphanumeric
characters. This field refers to the external_client_app_identifier in the [Salesforce rotation guide](https://help.salesforce.com/s/articleView?id=xcloud.eca_stage_oauth_credentials.htm&type=5 "https://help.salesforce.com/s/articleView?id=xcloud.eca_stage_oauth_credentials.htm&type=5").

consumerId

The consumer ID is the identifier for your Salesforce External Client Application (ECA) consumer.
You can retrieve this by calling the Salesforce OAuth Credentials by App ID endpoint. This field refers to the consumer_id in the [Salesforce rotation guide](https://help.salesforce.com/s/articleView?id=xcloud.eca_stage_oauth_credentials.htm&type=5 "https://help.salesforce.com/s/articleView?id=xcloud.eca_stage_oauth_credentials.htm&type=5").

## Secret Metadata Fields

The following are the metadata fields required to rotate a secret held by
Salesforce.

```
{
  "apiVersion": "`v65.0`",
  "adminSecretArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:`SalesforceClientSecret`"
}
```

apiVersion

The Salesforce API version is your Salesforce organization's API version. The version should be at least v65.0. It must be in the
format `vXX.X` where
`X` is a numeric
character.

adminSecretArn

(Optional) The admin secret ARN is the Amazon Resource Name (ARN) for the secret that contains
the administrative OAuth credentials that are to used to rotate this Salesforce client secret. At a minimum
the admin secret should contain a consumerKey and consumerSecret value within the secret structure. It is an
optional field and if omitted, during rotation Secrets Manager will use the OAuth credentials within
this secret to authenticate with Salesforce.

## Usage Flow

Customers storing Salesforce Secrets in AWS Secrets Manager have an option to rotate a secret with the credentials stored in the same secret or use the credentials
in the Admin secret for rotation. You can create your secret using the [CreateSecret](../apireference/API_CreateSecret.md "../apireference/API_CreateSecret.md") call with the secret
value containing the fields mentioned above and secret type as SalesforceClientSecret. The rotation configurations can be set using a
[RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md") call. This call requires the specification of the metadata fields as in the example above -
If you opt for a rotation using credentials in the same secret, you can skip the adminSecretArn field. Additionally,
customers must provide a role ARN in the [RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md") call which grants the service the required permissions to
rotate the secret. For an example of a permissions policy see [Security and Permissions](mes-security.md "mes-security.md").

For customers opting to rotate their secrets using a seperate set of credentials (stored in an Admin Secret), be sure to
create the Admin Secret in AWS Secrets Manager following the exact same steps as your consumer secret.
You must provide the ARN of this Admin Secret in the rotation metadata in a [RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md") call for your consumer secret.

The rotation logic follows the guidance provided by Salesforce.
