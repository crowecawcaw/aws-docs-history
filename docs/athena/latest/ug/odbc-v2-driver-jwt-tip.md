

# JWT Trusted identity propagation credentials provider
<a name="odbc-v2-driver-jwt-tip"></a>

This authentication type allows you to use a JSON web token (JWT) obtained from an external identity provider as a connection parameter to authenticate with Athena. You can use this plugin, to enable support for corporate identities via trusted identity propagation.

With trusted identity propagation, identity context is added to an IAM role to identify the user requesting access to AWS resources. For information on enabling and using trusted identity propagation, see [What is trusted identity propagation?](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation.html).

## Authentication type
<a name="odbc-v2-driver-jwt-tip-authentication-type"></a>



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| AuthenticationType | Required | IAM Credentials | AuthenticationType=JWT\_TIP; | 

## JWT web identity token
<a name="odbc-v2-driver-jwt-tip-web-identity-token"></a>

The JWT token obtained from an external federated identity provider. This token will be used to authenticate with Athena. Token caching is enabled by default and allows the same Identity Center access token to be used across driver connections. We recommend to provide a fresh JWT token upon "Testing Connection" as the exchanged token is present only during the duration driver instance is active.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| web\_identity\_token | Required | none | web\_identity\_token=eyJhbGc...<remainder of token>; | 

## Workgroup Arn
<a name="odbc-v2-driver-jwt-tip-workgroup-arn"></a>

The Amazon Resource Name (ARN) of the Amazon Athena workgroup. For more information about workgroups, see [WorkGroup](https://docs.aws.amazon.com/athena/latest/APIReference/API_WorkGroup.html).



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| WorkGroupArn | Required | none | WorkgroupArn=arn:aws:athena:us-west-2:111122223333:workgroup/primary | 

## JWT application role ARN
<a name="odbc-v2-driver-jwt-tip-application-role-arn"></a>

The ARN of the role to assume. This role is used for JWT exchange, getting IAM Identity Center Customer Managed application ARN through workgroup tags, and getting Access Role ARN. For more information about assuming roles, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html).



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| ApplicationRoleArn | Required | none | ApplicationRoleArn=arn:aws:iam::111122223333:role/applicationRole; | 

## Role session name
<a name="odbc-v2-driver-jwt-tip-role-session-name"></a>

A name for the session. It can be anything you like, but typically you pass the name or identifier that's associated with the user who is using your application. That way, the temporary security credentials that your application will use are associated with that user.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| role\_session\_name | Required | none | role\_session\_name=familiarname; | 

## Session duration
<a name="odbc-v2-driver-jwt-tip-session-duration"></a>

The duration, in seconds, of the role session. For more information about session duration, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html).



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| duration | Optional | 3600 | duration=900; | 

## JWT access role ARN
<a name="odbc-v2-driver-jwt-tip-access-role-arn"></a>

The ARN of the role to assume. This is the role that Athena assumes to make calls on your behalf. For more information about assuming roles, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html).



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| AccessRoleArn | Optional | none | AccessRoleArn=arn:aws:iam::111122223333:role/accessRole; | 

## IAM Identity Center customer managed application ARN
<a name="odbc-v2-driver-jwt-tip-customer-idc-application-arn"></a>

The ARN of IAM Identity Center customer managed IDC application. For more information about Customer Managed Applications, see [customer managed applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps.html).



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| CustomerIdcApplicationArn | Optional | none | CustomerIdcApplicationArn=arn:aws:sso::111122223333:application/ssoins-111122223333/apl-111122223333 | 

## Enable file cache
<a name="odbc-v2-driver-jwt-tip-file-cache"></a>

Enables a temporary credentials cache. This connection parameter allows you to cache temporary credentials and reuse it between multiple processes. Use this option to reduce the number of web identity tokens when you use BI tools such as Microsoft Power BI. By default, the driver uses `%USERPROFILE%` in Windows and `HOME` path to write the file caches. Ensure that you provide read and write access for the path present in these two environment variables, for a better experience.

**Note**  
Starting in v2.1.0.0, cached credentials are stored as plaintext JSON in the `user-profile/.athena-odbc/` directory with file permissions restricted to the owning user, consistent with how the AWS CLI protects locally stored credentials.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| JwtTipFileCache | Optional | 0 | JwtTipFileCache=1; | 