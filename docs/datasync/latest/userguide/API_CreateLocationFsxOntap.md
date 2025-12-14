# CreateLocationFsxOntap

Creates a transfer _location_ for an Amazon FSx for NetApp ONTAP file
system. AWS DataSync can use this location as a source or destination for
transferring data.

Before you begin, make sure that you understand how DataSync
[accesses FSx for ONTAP file systems](create-ontap-location.md#create-ontap-location-access "create-ontap-location.md#create-ontap-location-access").

## Request Syntax

```
{
   "Protocol": {
      "NFS": {
         "MountOptions": {
            "Version": "`string`"
         }
      },
      "SMB": {
         "Domain": "`string`",
         "MountOptions": {
            "Version": "`string`"
         },
         "Password": "`string`",
         "User": "`string`"
      }
   },
   "SecurityGroupArns": [ "`string`" ],
   "StorageVirtualMachineArn": "`string`",
   "Subdirectory": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[Protocol](#API_CreateLocationFsxOntap_RequestSyntax "#API_CreateLocationFsxOntap_RequestSyntax")**

Specifies the data transfer protocol that AWS DataSync uses to access your
Amazon FSx file system.

Type: [FsxProtocol](API_FsxProtocol.md "API_FsxProtocol.md") object

Required: Yes

**[SecurityGroupArns](#API_CreateLocationFsxOntap_RequestSyntax "#API_CreateLocationFsxOntap_RequestSyntax")**

Specifies the Amazon EC2 security groups that provide access to your file system's
preferred subnet.

The security groups must allow outbound traffic on the following ports (depending on the
protocol you use):

- **Network File System (NFS)**: TCP ports 111, 635, and
  2049
- **Server Message Block (SMB)**: TCP port 445

Your file system's security groups must also allow inbound traffic on the same
ports.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 5 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:security-group/sg-[a-f0-9]+$`

Required: Yes

**[StorageVirtualMachineArn](#API_CreateLocationFsxOntap_RequestSyntax "#API_CreateLocationFsxOntap_RequestSyntax")**

Specifies the ARN of the storage virtual machine (SVM) in your file system where you want
to copy data to or from.

Type: String

Length Constraints: Maximum length of 162.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):fsx:[a-z\-0-9]+:[0-9]{12}:storage-virtual-machine/fs-[0-9a-f]+/svm-[0-9a-f]{17,}$`

Required: Yes

**[Subdirectory](#API_CreateLocationFsxOntap_RequestSyntax "#API_CreateLocationFsxOntap_RequestSyntax")**

Specifies a path to the file share in the SVM where you want to transfer data to or
from.

You can specify a junction path (also known as a mount point), qtree path (for NFS file
shares), or share name (for SMB file shares). For example, your mount path might be
`/vol1`, `/vol1/tree1`, or `/share1`.

###### Note

Don't specify a junction path in the SVM's root volume. For more information, see [Managing FSx for ONTAP storage virtual machines](../../../fsx/latest/ONTAPGuide/managing-svms.md "../../../fsx/latest/ONTAPGuide/managing-svms.md") in the _Amazon FSx for NetApp ONTAP User Guide_.

Type: String

Length Constraints: Maximum length of 255.

Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`

Required: No

**[Tags](#API_CreateLocationFsxOntap_RequestSyntax "#API_CreateLocationFsxOntap_RequestSyntax")**

Specifies labels that help you categorize, filter, and search for your AWS
resources. We recommend creating at least a name tag for your location.

Type: Array of [TagListEntry](API_TagListEntry.md "API_TagListEntry.md") objects

Array Members: Minimum number of 0 items. Maximum number of 50 items.

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

**[LocationArn](#API_CreateLocationFsxOntap_ResponseSyntax "#API_CreateLocationFsxOntap_ResponseSyntax")**

Specifies the ARN of the FSx for ONTAP file system location that you
create.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InternalException**

This exception is thrown when an error occurs in the AWS DataSync
service.

HTTP Status Code: 500

**InvalidRequestException**

This exception is thrown when the client submits a malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/CreateLocationFsxOntap.md "../../../goto/cli2/datasync-2018-11-09/CreateLocationFsxOntap.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/CreateLocationFsxOntap.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/CreateLocationFsxOntap.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/CreateLocationFsxOntap.md "../../../goto/SdkForCpp/datasync-2018-11-09/CreateLocationFsxOntap.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/CreateLocationFsxOntap.md "../../../goto/SdkForGoV2/datasync-2018-11-09/CreateLocationFsxOntap.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationFsxOntap.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationFsxOntap.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationFsxOntap.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationFsxOntap.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/CreateLocationFsxOntap.md "../../../goto/SdkForKotlin/datasync-2018-11-09/CreateLocationFsxOntap.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationFsxOntap.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationFsxOntap.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/CreateLocationFsxOntap.md "../../../goto/boto3/datasync-2018-11-09/CreateLocationFsxOntap.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationFsxOntap.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationFsxOntap.md")
