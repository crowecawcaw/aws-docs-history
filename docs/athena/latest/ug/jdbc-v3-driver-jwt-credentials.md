

# JWT credentials
<a name="jdbc-v3-driver-jwt-credentials"></a>

With this authentication type, you can use a JSON web token (JWT) obtained from an external identity provider as a connection parameter to authenticate with Athena. The external credentials provider must already be federated with AWS.

## Credentials provider
<a name="jdbc-v3-driver-jwt-credentials-provider"></a>

The credentials provider that will be used to authenticate requests to AWS. Set the value of this parameter to `JWT`.



| Parameter name | Alias | Parameter type | Default value | Value to use | 
| --- | --- | --- | --- | --- | 
| CredentialsProvider | AWSCredentialsProviderClass (deprecated) | Required | none | JWT | 

## JWT web identity token
<a name="jdbc-v3-driver-jwt-web-identity-token"></a>

The JWT token obtained from an external federated identity provider. This token will be used to authenticate with Athena.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| JwtWebIdentityToken | web\_identity\_token (deprecated) | Required | none | 

## JWT role ARN
<a name="jdbc-v3-driver-jwt-role-arn"></a>

The Amazon Resource Name (ARN) of the role to assume. For information about assuming roles, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| JwtRoleArn | role\_arn (deprecated) | Required | none | 

## JWT role session name
<a name="jdbc-v3-driver-jwt-role-session-name"></a>

The name of the session when you use JWT credentials for authentication. The name can be any name that you choose.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| JwtRoleSessionName | role\_session\_name (deprecated) | Required | none | 

## Role session duration
<a name="jdbc-v3-driver-jwt-role-session-duration"></a>

The duration, in seconds, of the role session. For more information, see [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html) in the *AWS Security Token Service API Reference*.



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| RoleSessionDuration | Duration (deprecated) | Optional | 3600 | 