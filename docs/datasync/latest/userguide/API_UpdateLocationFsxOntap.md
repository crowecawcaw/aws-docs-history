# UpdateLocationFsxOntap

Modifies the following configuration parameters of the Amazon FSx for NetApp ONTAP
transfer location that you're using with AWS DataSync.

For more information, see [Configuring DataSync
transfers with FSx for ONTAP](create-ontap-location.md "create-ontap-location.md").

## Request Syntax

```
{
   "LocationArn": "`string`",
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
   "Subdirectory": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[LocationArn](#API_UpdateLocationFsxOntap_RequestSyntax "#API_UpdateLocationFsxOntap_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the FSx for ONTAP transfer location
that you're updating.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

**[Protocol](#API_UpdateLocationFsxOntap_RequestSyntax "#API_UpdateLocationFsxOntap_RequestSyntax")**

Specifies the data transfer protocol that DataSync uses to access your Amazon FSx file system.

Type: [FsxUpdateProtocol](API_FsxUpdateProtocol.md "API_FsxUpdateProtocol.md") object

Required: No

**[Subdirectory](#API_UpdateLocationFsxOntap_RequestSyntax "#API_UpdateLocationFsxOntap_RequestSyntax")**

Specifies a path to the file share in the storage virtual machine (SVM) where you want to
transfer data to or from.

You can specify a junction path (also known as a mount point), qtree path (for NFS file
shares), or share name (for SMB file shares). For example, your mount path might be
`/vol1`, `/vol1/tree1`, or `/share1`.

###### Note

Don't specify a junction path in the SVM's root volume. For more information, see [Managing FSx for ONTAP storage virtual machines](../../../fsx/latest/ONTAPGuide/managing-svms.md "../../../fsx/latest/ONTAPGuide/managing-svms.md") in the _Amazon FSx for NetApp ONTAP User Guide_.

Type: String

Length Constraints: Maximum length of 255.

Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`

Required: No

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/UpdateLocationFsxOntap.md "../../../goto/cli2/datasync-2018-11-09/UpdateLocationFsxOntap.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateLocationFsxOntap.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateLocationFsxOntap.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationFsxOntap.md "../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationFsxOntap.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationFsxOntap.md "../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationFsxOntap.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationFsxOntap.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationFsxOntap.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationFsxOntap.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationFsxOntap.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationFsxOntap.md "../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationFsxOntap.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationFsxOntap.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationFsxOntap.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/UpdateLocationFsxOntap.md "../../../goto/boto3/datasync-2018-11-09/UpdateLocationFsxOntap.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationFsxOntap.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationFsxOntap.md")
