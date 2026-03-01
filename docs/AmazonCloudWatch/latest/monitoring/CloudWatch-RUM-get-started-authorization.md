# Authorize your web application to send data to AWS

You have four options to set up data authentication:

- Use Amazon Cognito and let CloudWatch RUM create a new Amazon Cognito identity pool for the
  application. This method requires the least effort to set up.

The identity pool will contain an unauthenticated identity. This allows
the CloudWatch RUM web client to send data to CloudWatch RUM without authenticating the
user of the application.

The Amazon Cognito identity pool has an attached IAM role. The Amazon Cognito
unauthenticated identity allows the web client to assume the IAM role that
is authorized to send data to CloudWatch RUM.

- Use Amazon Cognito for authentication. If you use this, you can use an existing
  Amazon Cognito identity pool or create a new one to use with this app monitor. If you
  use an existing identity pool, you must also modify the IAM role that is
  attached to the identity pool. Use this option for identity pools that
  support unauthenticated users. You can use identity pools only from the same
  Region.
- Use authentication from an existing identity provider that you have
  already set up. In this case, you must get credentials from the identity
  provider and your application must forward these credentials to the RUM web
  client.

Use this option for identity pools that support only authenticated
users.

- Use resource-based policies to manage access to your app monitor. This
  includes the ability to send unauthenticated requests to CloudWatch RUM without
  AWS credentials. To learn more about resource based policies and RUM, see
  [Using resource-based policies with CloudWatch RUM](CloudWatch-RUM-resource-policies.md "CloudWatch-RUM-resource-policies.md").
  The following sections include more details about these options.

## Use an existing Amazon Cognito identity pool

If you choose to use a Amazon Cognito identity pool, you specify the identity pool when
you add the application to CloudWatch RUM. The pool must support enabling access to
unauthenticated identities. You can use identity pools only from the same
Region.

You also must add the following permissions to the IAM policy that is
attached to the IAM role that is associated with this identity pool.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "rum:PutRumEvents"
 ],
 "Resource": "arn:aws:rum:`us-east-1`:`123456789012`:appmonitor/`app monitor name`"
 }
 ]
}`

```

Amazon Cognito will then send the necessary security token to enable your application
to access CloudWatch RUM.

## Third-party provider

If you choose to use private authentication from a third-party provider, you
must get credentials from the identity provider and forward them to AWS. The
best way to do this is by using a _security token vendor_.
You can use any security token vendor, including Amazon Cognito with AWS Security Token Service. For more
information about AWS STS, see [Welcome to the AWS Security Token Service API
Reference](../../../STS/latest/APIReference/welcome.md "../../../STS/latest/APIReference/welcome.md").

If you want to use Amazon Cognito as the token vendor in this scenario, you can
configure Amazon Cognito to work with an authentication provider. For more information,
see [Getting Started with Amazon Cognito Identity Pools (Federated
Identities)](../../../cognito/latest/developerguide/getting-started-with-identity-pools.md "../../../cognito/latest/developerguide/getting-started-with-identity-pools.md").

After you configure Amazon Cognito to work with your identity provider, you also need
to do the following:

- Create an IAM role with the following permissions. Your application
  will use this role to access AWS.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "rum:PutRumEvents",
 "Resource": "arn:aws:rum:`us-east-2`:`123456789012`:appmonitor/`AppMonitorName`"
 }
 ]
}`

```

- Add the following to your application to have it pass the credentials
  from your provider to CloudWatch RUM. Insert the line so that it runs after a
  user has signed in to your application and the application has received
  the credentials to use to access AWS.

```
cwr('setAwsCredentials', {/* Credentials or CredentialProvider */});
```

For more information about credential providers in the AWS JavaScript SDK,
see [Setting credentials in a web browser](../../../sdk-for-javascript/v3/developer-guide/setting-credentials-browser.md "../../../sdk-for-javascript/v3/developer-guide/setting-credentials-browser.md") in the v3 developer guide for
SDK for JavaScript, [Setting credentials in a web browser](../../../sdk-for-javascript/v2/developer-guide/setting-credentials-browser.md "../../../sdk-for-javascript/v2/developer-guide/setting-credentials-browser.md") in the v2 developer guide for
SDK for JavaScript, , and [@aws-sdk/credential-providers](https://www.npmjs.com/package/@aws-sdk/credential-providers "https://www.npmjs.com/package/@aws-sdk/credential-providers").

You can also use the SDK for the CloudWatch RUM web client to configure the web
client authentication methods. For more information about the web client SDK,
see [CloudWatch RUM web
client SDK](https://github.com/aws-observability/aws-rum-web "https://github.com/aws-observability/aws-rum-web").
