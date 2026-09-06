

# JWT with identity center integration
<a name="jdbc-v3-driver-jwt-tip-credentials"></a>

This authentication type allows you to use a JSON web token (JWT) obtained from an external identity provider as a connection parameter to authenticate with Athena. You can use this plugin, to enable support for corporate identities via trusted identity propagation. For more information on how to use trusted identity propagation with drivers, see [Use Trusted identity propagation with Amazon Athena drivers](using-trusted-identity-propagation.md). You can also [configure and deploy resources using CloudFormation](using-trusted-identity-propagation-cloudformation.md).

With trusted identity propagation, identity context is added to an IAM role to identify the user requesting access to AWS resources. For information on enabling and using trusted identity propagation, see [What is trusted identity propagation?](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation.html).

## Credentials provider
<a name="jdbc-v3-driver-jwt-tip-credentials-provider"></a>

The credentials provider that will be used to authenticate requests to AWS. Set the value of this parameter to `JWT_TIP`.



| Parameter name | Alias | Parameter type | Default value | Value to use | 
| --- | --- | --- | --- | --- | 
| CredentialsProvider | AWSCredentialsProviderClass (deprecated) | Required | none | JWT\_TIP | 

## JWT web identity token
<a name="jdbc-v3-driver-jwt-tip-web-identity-token"></a>

The JWT token obtained from an external federated identity provider. This token will be used to authenticate with Athena. Token Caching is enabled by default and allows the same Identity Center access token to be used across driver connections. We recommend to provide a fresh JWT token upon "Testing Connection" as the exchanged token is present only during driver instance is active.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| JwtWebIdentityToken | web\_identity\_token (deprecated) | Required | none | 

## WorkgroupArn
<a name="jdbc-v3-driver-jwt-tip-workgroup-arn"></a>

The Amazon Resource Name (ARN) of the Amazon Athena workgroup. For more information about workgroups, see [WorkGroup](https://docs.aws.amazon.com/athena/latest/APIReference/API_WorkGroup.html).



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| WorkGroupArn | none | Required | primary | 

## JWT application role ARN
<a name="jdbc-v3-driver-jwt-tip-application-role-arn"></a>

The ARN of the role to assume. This role is used for JWT exchange, getting IAM Identity Center customer managed application ARN through workgroup tags, and getting access role ARN. For more information about assuming roles, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html).



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| ApplicationRoleArn | none | Required | none | 

## JWT role session name
<a name="jdbc-v3-driver-jwt-tip-role-session-name"></a>

The name of the session when authenticating with JWT credentials. It can be any name of your choice.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| JwtRoleSessionName | role\_session\_name (deprecated) | Required | none | 

## Role session duration
<a name="jdbc-v3-driver-jwt-tip-session-duration"></a>

The duration, in seconds, of the role session. For more information, see [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html).



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| RoleSessionDuration | Duration (deprecated) | Optional | 3600 | 

## JWT access role ARN
<a name="jdbc-v3-driver-jwt-tip-access-role-arn"></a>

The ARN of the role to assume. This is the role assumed by the Athena service to make calls on the behalf of you. For more information about assuming roles, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| AccessRoleArn | none | Optional | none | 

## IAM Identity Center customer managed application ARN
<a name="jdbc-v3-driver-jwt-tip-customer-idc-application-arn"></a>

The ARN of IAM Identity Center customer managed application. For more information, see [customer managed applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps.html).



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| CustomerIdcApplicationArn | none | Optional | none | 