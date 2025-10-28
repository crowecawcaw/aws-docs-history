# CreateLocationSmb

Creates a transfer _location_ for a Server Message Block (SMB) file
server. AWS DataSync can use this location as a source or destination for
transferring data.

Before you begin, make sure that you understand how DataSync accesses SMB
file servers. For more information, see [Providing DataSync access to SMB file servers](create-smb-location.md#configuring-smb-permissions "create-smb-location.md#configuring-smb-permissions").

## Request Syntax

```
{
   "AgentArns": [ "`string`" ],
   "AuthenticationType": "`string`",
   "DnsIpAddresses": [ "`string`" ],
   "Domain": "`string`",
   "KerberosKeytab": `blob`,
   "KerberosKrb5Conf": `blob`,
   "KerberosPrincipal": "`string`",
   "MountOptions": {
      "Version": "`string`"
   },
   "Password": "`string`",
   "ServerHostname": "`string`",
   "Subdirectory": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ],
   "User": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[AgentArns](#API_CreateLocationSmb_RequestSyntax "#API_CreateLocationSmb_RequestSyntax")**

Specifies the DataSync agent (or agents) that can connect to your SMB file
server. You specify an agent by using its Amazon Resource Name (ARN).

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 4 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

Required: Yes

**[AuthenticationType](#API_CreateLocationSmb_RequestSyntax "#API_CreateLocationSmb_RequestSyntax")**

Specifies the authentication protocol that DataSync uses to connect to your SMB
file server. DataSync supports `NTLM` (default) and `KERBEROS`
authentication.

For more information, see [Providing DataSync access to SMB file servers](create-smb-location.md#configuring-smb-permissions "create-smb-location.md#configuring-smb-permissions").

Type: String

Valid Values: `NTLM | KERBEROS`

Required: No

**[DnsIpAddresses](#API_CreateLocationSmb_RequestSyntax "#API_CreateLocationSmb_RequestSyntax")**

Specifies the IPv4 or IPv6 addresses for the DNS servers that your SMB file server belongs to.
This parameter applies only if `AuthenticationType` is set to
`KERBEROS`.

If you have multiple domains in your environment, configuring this parameter makes sure
that DataSync connects to the right SMB file server.

Type: Array of strings

Array Members: Maximum number of 2 items.

Length Constraints: Minimum length of 7. Maximum length of 39.

Pattern: `\A((25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}|([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6}))\z`

Required: No

**[Domain](#API_CreateLocationSmb_RequestSyntax "#API_CreateLocationSmb_RequestSyntax")**

Specifies the Windows domain name that your SMB file server belongs to. This parameter
applies only if `AuthenticationType` is set to `NTLM`.

If you have multiple domains in your environment, configuring this parameter makes sure
that DataSync connects to the right file server.

Type: String

Length Constraints: Maximum length of 253.

Pattern: `^[A-Za-z0-9]((\.|-+)?[A-Za-z0-9]){0,252}$`

Required: No

**[KerberosKeytab](#API_CreateLocationSmb_RequestSyntax "#API_CreateLocationSmb_RequestSyntax")**

Specifies your Kerberos key table (keytab) file, which includes mappings between your
Kerberos principal and encryption keys.

To avoid task execution errors, make sure that the Kerberos principal that you use to
create the keytab file matches exactly what you specify for `KerberosPrincipal`.

Type: Base64-encoded binary data object

Length Constraints: Maximum length of 65536.

Required: No

**[KerberosKrb5Conf](#API_CreateLocationSmb_RequestSyntax "#API_CreateLocationSmb_RequestSyntax")**

Specifies a Kerberos configuration file (`krb5.conf`) that defines your
Kerberos realm configuration.

The file must be base64 encoded. If you're using the AWS CLI, the encoding is
done for you.

Type: Base64-encoded binary data object

Length Constraints: Maximum length of 131072.

Required: No

**[KerberosPrincipal](#API_CreateLocationSmb_RequestSyntax "#API_CreateLocationSmb_RequestSyntax")**

Specifies a Kerberos principal, which is an identity in your Kerberos realm that has
permission to access the files, folders, and file metadata in your SMB file server.

A Kerberos principal might look like `HOST/kerberosuser@MYDOMAIN.ORG`.

Principal names are case sensitive. Your DataSync task execution will fail if
the principal that you specify for this parameter doesn’t exactly match the principal that you
use to create the keytab file.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `^.+$`

Required: No

**[MountOptions](#API_CreateLocationSmb_RequestSyntax "#API_CreateLocationSmb_RequestSyntax")**

Specifies the version of the SMB protocol that DataSync uses to access your SMB
file server.

Type: [SmbMountOptions](API_SmbMountOptions.md "API_SmbMountOptions.md") object

Required: No

**[Password](#API_CreateLocationSmb_RequestSyntax "#API_CreateLocationSmb_RequestSyntax")**

Specifies the password of the user who can mount your SMB file server and has permission
to access the files and folders involved in your transfer. This parameter applies only if
`AuthenticationType` is set to `NTLM`.

Type: String

Length Constraints: Maximum length of 104.

Pattern: `^.{0,104}$`

Required: No

**[ServerHostname](#API_CreateLocationSmb_RequestSyntax "#API_CreateLocationSmb_RequestSyntax")**

Specifies the domain name or IP address (IPv4 or IPv6) of the SMB file server that your DataSync agent connects to.

###### Note

If you're using Kerberos authentication, you must specify a domain name.

Type: String

Length Constraints: Maximum length of 255.

Pattern: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-:]*[A-Za-z0-9])$`

Required: Yes

**[Subdirectory](#API_CreateLocationSmb_RequestSyntax "#API_CreateLocationSmb_RequestSyntax")**

Specifies the name of the share exported by your SMB file server where DataSync
will read or write data. You can include a subdirectory in the share path (for example,
`/path/to/subdirectory`). Make sure that other SMB clients in your network can
also mount this path.

To copy all data in the subdirectory, DataSync must be able to mount the SMB
share and access all of its data. For more information, see [Providing DataSync access to SMB file servers](create-smb-location.md#configuring-smb-permissions "create-smb-location.md#configuring-smb-permissions").

Type: String

Length Constraints: Maximum length of 4096.

Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`

Required: Yes

**[Tags](#API_CreateLocationSmb_RequestSyntax "#API_CreateLocationSmb_RequestSyntax")**

Specifies labels that help you categorize, filter, and search for your AWS
resources. We recommend creating at least a name tag for your location.

Type: Array of [TagListEntry](API_TagListEntry.md "API_TagListEntry.md") objects

Array Members: Minimum number of 0 items. Maximum number of 50 items.

Required: No

**[User](#API_CreateLocationSmb_RequestSyntax "#API_CreateLocationSmb_RequestSyntax")**

Specifies the user that can mount and access the files, folders, and file metadata in your
SMB file server. This parameter applies only if `AuthenticationType` is set to
`NTLM`.

For information about choosing a user with the right level of access for your transfer,
see [Providing DataSync access to SMB file servers](create-smb-location.md#configuring-smb-permissions "create-smb-location.md#configuring-smb-permissions").

Type: String

Length Constraints: Maximum length of 104.

Pattern: `^[^\x22\x5B\x5D/\\:;|=,+*?\x3C\x3E]{1,104}$`

Required: No

## Response Syntax

```
{
   "LocationArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[LocationArn](#API_CreateLocationSmb_ResponseSyntax "#API_CreateLocationSmb_ResponseSyntax")**

The ARN of the SMB location that you created.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InternalException**

This exception is thrown when an error occurs in the AWS DataSync
service.

HTTP Status Code: 500

**InvalidRequestException**

This exception is thrown when the client submits a malformed request.

HTTP Status Code: 400

## Examples

### Sample Request

The following example creates a location for an SMB file server.

```
{
   "AgentArns":[
      "arn:aws:datasync:us-east-2:111222333444:agent/agent-0b0addbeef44b3nfs",
      "arn:aws:datasync:us-east-2:111222333444:agent/agent-2345noo35nnee1123ovo3"
   ],
   "Domain":"AMAZON",
   "MountOptions":{
      "Version":"SMB3"
   },
   "Password":"string",
   "ServerHostname":"MyServer.amazon.com",
   "Subdirectory":"share",
   "Tags":[
      {
         "Key":"department",
         "Value":"finance"
      }
   ],
   "User":"user-1"
}

```

### Sample Response

A response returns the location ARN of your SMB file server.

```
{
    "LocationArn": "arn:aws:datasync:us-east-1:111222333444:location/loc-0f01451b140b2af49"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/CreateLocationSmb.md "../../../goto/cli2/datasync-2018-11-09/CreateLocationSmb.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/CreateLocationSmb.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/CreateLocationSmb.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/CreateLocationSmb.md "../../../goto/SdkForCpp/datasync-2018-11-09/CreateLocationSmb.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/CreateLocationSmb.md "../../../goto/SdkForGoV2/datasync-2018-11-09/CreateLocationSmb.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationSmb.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationSmb.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationSmb.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationSmb.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/CreateLocationSmb.md "../../../goto/SdkForKotlin/datasync-2018-11-09/CreateLocationSmb.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationSmb.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationSmb.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/CreateLocationSmb.md "../../../goto/boto3/datasync-2018-11-09/CreateLocationSmb.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationSmb.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationSmb.md")
