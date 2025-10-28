# QopConfiguration

The Quality of Protection (QOP) configuration specifies the Remote Procedure Call (RPC)
and data transfer privacy settings configured on the Hadoop Distributed File System (HDFS)
cluster.

## Contents

**DataTransferProtection**

The data transfer protection setting configured on the HDFS cluster. This setting
corresponds to your `dfs.data.transfer.protection` setting in the
`hdfs-site.xml` file on your Hadoop cluster.

Type: String

Valid Values: `DISABLED | AUTHENTICATION | INTEGRITY | PRIVACY`

Required: No

**RpcProtection**

The RPC protection setting configured on the HDFS cluster. This setting corresponds to
your `hadoop.rpc.protection` setting in your `core-site.xml` file on
your Hadoop cluster.

Type: String

Valid Values: `DISABLED | AUTHENTICATION | INTEGRITY | PRIVACY`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/QopConfiguration.md "../../../goto/SdkForCpp/datasync-2018-11-09/QopConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/QopConfiguration.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/QopConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/QopConfiguration.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/QopConfiguration.md")
