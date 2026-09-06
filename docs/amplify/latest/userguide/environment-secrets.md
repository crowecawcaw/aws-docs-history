

# Managing environment secrets
<a name="environment-secrets"></a>

With the release of Amplify Gen 2, the workflow for environment secrets is streamlined to centralize the management of secrets and environment variables in the Amplify console. For instructions on setting and accessing secrets for an Amplify Gen 2 app, see [Secrets and environment vars](https://docs.amplify.aws/react/deploy-and-host/fullstack-branching/secrets-and-vars/) in the *Amplify Documentation*.

Environment secrets for a Gen 1 app are similar to environment variables, but they are AWS Systems Manager Parameter Store key value pairs that can be encrypted. Some values must be encrypted, such as the Sign in with Apple private key for Amplify.

## Using AWS Systems Manager to set environment secrets for an Amplify Gen 1 application
<a name="set-environment-secrets"></a>

Use the following instructions to set an environment secret for a Gen 1 Amplify app using the AWS Systems Manager console.

**To set an environment secret**

1. Sign in to the AWS Management Console and open the [AWS Systems Manager console](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Application Management**, then choose **Parameter Store**.

1. On the **AWS Systems Manager Parameter Store** page, choose **Create parameter**.

1. On the **Create parameter** page, in the **Parameter details** section, do the following:

   1. For **Name**, enter a parameter in the format **/amplify/{your\_app\_id}/{your\_backend\_environment\_name}/{your\_parameter\_name}**.

   1. For **Type**, choose **SecureString**.

   1. For **KMS key source**, choose **My current account** to use the default key for your account.

   1. For **Value**, enter your secret value to encrypt.

1. Choose, **Create parameter**.

**Note**  
Amplify only has access to the keys under the `/amplify/{your_app_id}/{your_backend_environment_name}` for the specific environment build. You must specify the default AWS KMS key to allow Amplify to decrypt the value.

## Accessing environment secrets for a Gen 1 application
<a name="access-environment-secrets"></a>

Environment secrets for a Gen 1 application are stored in `process.env.secrets` as a JSON string.

## Amplify environment secrets reference
<a name="amplify-environment-secrets"></a>

Specify an Systems Manager parameter in the format `/amplify/{your_app_id}/{your_backend_environment_name}/AMPLIFY_SIWA_CLIENT_ID`.

You can use the following environment secrets that are accessible by default within the Amplify console.



| Variable name | Description | Example value | 
| --- | --- | --- | 
| AMPLIFY\_SIWA\_CLIENT\_ID | The Sign in with Apple client ID | `com.yourapp.auth` | 
| AMPLIFY\_SIWA\_TEAM\_ID | The Sign in with Apple team ID | `ABCD123` | 
| AMPLIFY\_SIWA\_KEY\_ID | The Sign in with Apple key ID | `ABCD123` | 
| AMPLIFY\_SIWA\_PRIVATE\_KEY | The Sign in with Apple private key | -----BEGIN PRIVATE KEY-----<br />\*\*\*\*......<br />-----END PRIVATE KEY----- | 