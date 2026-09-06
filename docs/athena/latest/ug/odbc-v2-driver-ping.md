

# Ping
<a name="odbc-v2-driver-ping"></a>

Ping is a SAML based plugin that works with the [PingFederate](https://www.pingidentity.com/en/platform/capabilities/authentication-authority/pingfederate.html) identity provider.

## Authentication type
<a name="odbc-v2-driver-ping-authentication-type"></a>



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| AuthenticationType | Required | IAM Credentials | AuthenticationType=Ping; | 

## User ID
<a name="odbc-v2-driver-ping-user-id"></a>

The user name for the PingFederate server.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| UID | Required | none | UID=pingusername@domain.com; | 

## Password
<a name="odbc-v2-driver-ping-password"></a>

The password for the PingFederate server.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| PWD | Required | none | PWD=pingpassword; | 

## Preferred role
<a name="odbc-v2-driver-ping-preferred-role"></a>

The Amazon Resource Name (ARN) of the role to assume. If your SAML assertion has multiple roles, you can specify this parameter to choose the role to be assumed. This role should be present in the SAML assertion. For more information about ARN roles, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*. 



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| preferred\_role | Optional | none | preferred\_role=arn:aws:iam::123456789012:id/user1; | 

## Session duration
<a name="odbc-v2-driver-ping-session-duration"></a>

The duration, in seconds, of the role session. For more information about session duration, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| duration | Optional | 900 | duration=900; | 

## IdP host
<a name="odbc-v2-driver-ping-idp-host"></a>

The address for your Ping server. To find your address, visit the following URL and view the **SSO Application Endpoint** field.

```
https://{{your-pf-host-#}}:9999/pingfederate/{{your-pf-app#}}/spConnections         
```



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| idp\_host | Required | none | idp\_host=ec2-1-83-65-12.compute-1.amazonaws.com; | 

## IdP port
<a name="odbc-v2-driver-ping-idp-port"></a>

The port number to use to connect to your IdP host.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| idp\_port | Required | None | idp\_port=443; | 

## Partner SPID
<a name="odbc-v2-driver-ping-partner-spid"></a>

The service provider address. To find the service provider address, visit the following URL and view the **SSO Application Endpoint** field.

```
https://{{your-pf-host-#}}:9999/pingfederate/{{your-pf-app#}}/spConnections         
```



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| partner\_spid | Required | None | partner\_spid=https://us-east-1.signin.aws.amazon.com/platform/saml/<...>; | 

## Ping URI param
<a name="odbc-v2-driver-ping-uri-param"></a>

Passes a URI argument for an authentication request to Ping. Use this parameter to bypass the Lake Formation single role limitation. Configure Ping to recognize the passed parameter, and verify that the role passed exists in the list of roles assigned to the user. Then, send a single role in the SAML assertion.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| ping\_uri\_param | Optional | None | ping\_uri\_param=role=my\_iam\_role; | 