

# JWT
<a name="odbc-v2-driver-jwt"></a>

The JWT (JSON Web Token) plugin provides an interface that uses JSON Web Tokens to assume an Amazon IAM role. The configuration depends on the identity provider. For information about configuring federation for Google Cloud and AWS, see [Configure workload identity federation with AWS or Azure](https://cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds) in the Google Cloud documentation.

## Authentication type
<a name="odbc-v2-driver-jwt-authentication-type"></a>



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| AuthenticationType | Required | IAM Credentials | AuthenticationType=JWT; | 

## Preferred role
<a name="odbc-v2-driver-jwt-preferred-role"></a>

The Amazon Resource Name (ARN) of the role to assume. For more information about ARN roles, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| preferred\_role | Optional | none | preferred\_role=arn:aws:IAM::123456789012:id/user1; | 

## Session duration
<a name="odbc-v2-driver-jwt-session-duration"></a>

The duration, in seconds, of the role session. For more information about session duration, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| duration | Optional | 900 | duration=900; | 

## JSON web token
<a name="odbc-v2-driver-jwt-json-web-token"></a>

The JSON web token that is used to retrieve IAM temporary credentials using the [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html) AWS STS API action. For information about generating JSON web tokens for Google Cloud Platform (GCP) users, see [Using JWT OAuth tokens](https://cloud.google.com/apigee/docs/api-platform/security/oauth/using-jwt-oauth) in the Google Cloud documentation.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| web\_identity\_token | Required | none | web\_identity\_token=eyJhbGc...<remainder of token>; | 

## Role session name
<a name="odbc-v2-driver-jwt-role-session-name"></a>

A name for the session. A common technique is to use the name or identifier of the user of your application as the role session name. This conveniently associates the temporary security credentials that your application uses with the corresponding user.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| role\_session\_name | Required | none | role\_session\_name=familiarname; | 