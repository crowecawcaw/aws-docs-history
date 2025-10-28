# HdfsNameNode

The NameNode of the Hadoop Distributed File System (HDFS). The NameNode manages the file
system's namespace. The NameNode performs operations such as opening, closing, and renaming
files and directories. The NameNode contains the information to map blocks of data to the
DataNodes.

## Contents

**Hostname**

The hostname of the NameNode in the HDFS cluster. This value is the IP address or Domain
Name Service (DNS) name of the NameNode. An agent that's installed on-premises uses this
hostname to communicate with the NameNode in the network.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])$`

Required: Yes

**Port**

The port that the NameNode uses to listen to client requests.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 65536.

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/HdfsNameNode.md "../../../goto/SdkForCpp/datasync-2018-11-09/HdfsNameNode.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/HdfsNameNode.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/HdfsNameNode.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/HdfsNameNode.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/HdfsNameNode.md")
