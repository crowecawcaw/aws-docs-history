# SharedDirectory

Details about the shared directory in the directory owner account for which the share
request in the directory consumer account has been accepted.

## Contents

**CreatedDateTime**

The date and time that the shared directory was created.

Type: Timestamp

Required: No

**LastUpdatedDateTime**

The date and time that the shared directory was last updated.

Type: Timestamp

Required: No

**OwnerAccountId**

Identifier of the directory owner account, which contains the directory that has been
shared to the consumer account.

Type: String

Pattern: `^(\d{12})$`

Required: No

**OwnerDirectoryId**

Identifier of the directory in the directory owner account.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: No

**SharedAccountId**

Identifier of the directory consumer account that has access to the shared directory
(`OwnerDirectoryId`) in the directory owner account.

Type: String

Pattern: `^(\d{12})$`

Required: No

**SharedDirectoryId**

Identifier of the shared directory in the directory consumer account. This identifier is
different for each directory owner account.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: No

**ShareMethod**

The method used when sharing a directory to determine whether the directory should be
shared within your AWS organization (`ORGANIZATIONS`) or with any AWS account
by sending a shared directory request (`HANDSHAKE`).

Type: String

Valid Values: `ORGANIZATIONS | HANDSHAKE`

Required: No

**ShareNotes**

A directory share request that is sent by the directory owner to the directory consumer.
The request includes a typed message to help the directory consumer administrator determine
whether to approve or reject the share invitation.

Type: String

Length Constraints: Maximum length of 1024.

Required: No

**ShareStatus**

Current directory status of the shared AWS Managed Microsoft AD directory.

Type: String

Valid Values: `Shared | PendingAcceptance | Rejected | Rejecting | RejectFailed | Sharing | ShareFailed | Deleted | Deleting`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/SharedDirectory.md "../../../goto/SdkForCpp/ds-2015-04-16/SharedDirectory.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/SharedDirectory.md "../../../goto/SdkForJavaV2/ds-2015-04-16/SharedDirectory.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/SharedDirectory.md "../../../goto/SdkForRubyV3/ds-2015-04-16/SharedDirectory.md")
