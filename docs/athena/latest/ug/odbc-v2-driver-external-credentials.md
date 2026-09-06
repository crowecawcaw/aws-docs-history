

# External credentials
<a name="odbc-v2-driver-external-credentials"></a>

External credentials is a generic authentication plugin that you can use to connect to any external SAML based identity provider. To use the plugin, you pass an executable file that returns a SAML response.

## Authentication type
<a name="odbc-v2-driver-driver-external-credentials-authentication-type"></a>



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| AuthenticationType | Required | IAM Credentials | AuthenticationType=External Credentials; | 

## Executable path
<a name="odbc-v2-driver-driver-external-credentials-executable-path"></a>

The path to the executable that has the logic of your custom SAML-based credential provider. The output of the executable must be the parsed SAML response from the identity provider.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| ExecutablePath | Required | none | ExecutablePath=C:\\Users\\{{user\_name}}\\{{external\_credential.exe}} | 

## Argument list
<a name="odbc-v2-driver-driver-external-credentials-argument-list"></a>

The list of arguments that you want to pass to the executable.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| ArgumentList | Optional | none | ArgumentList={{arg1}} {{arg2}} {{arg3}} | 