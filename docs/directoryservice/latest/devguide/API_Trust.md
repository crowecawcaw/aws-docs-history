# Trust

Describes a trust relationship between an AWS Managed Microsoft AD directory and an external
domain.

## Contents

**CreatedDateTime**

The date and time that the trust relationship was created.

Type: Timestamp

Required: No

**DirectoryId**

The Directory ID of the AWS directory involved in the trust relationship.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: No

**LastUpdatedDateTime**

The date and time that the trust relationship was last updated.

Type: Timestamp

Required: No

**RemoteDomainName**

The Fully Qualified Domain Name (FQDN) of the external domain involved in the trust
relationship.

Type: String

Length Constraints: Maximum length of 1024.

Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?$`

Required: No

**SelectiveAuth**

Current state of selective authentication for the trust.

Type: String

Valid Values: `Enabled | Disabled`

Required: No

**StateLastUpdatedDateTime**

The date and time that the TrustState was last updated.

Type: Timestamp

Required: No

**TrustDirection**

The trust relationship direction.

Type: String

Valid Values: `One-Way: Outgoing | One-Way: Incoming | Two-Way`

Required: No

**TrustId**

The unique ID of the trust relationship.

Type: String

Pattern: `^t-[0-9a-f]{10}$`

Required: No

**TrustState**

The trust relationship state.

Type: String

Valid Values: `Creating | Created | Verifying | VerifyFailed | Verified | Updating | UpdateFailed | Updated | Deleting | Deleted | Failed`

Required: No

**TrustStateReason**

The reason for the TrustState.

Type: String

Required: No

**TrustType**

The trust relationship type. `Forest` is the default.

Type: String

Valid Values: `Forest | External`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/Trust.md "../../../goto/SdkForCpp/ds-2015-04-16/Trust.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/Trust.md "../../../goto/SdkForJavaV2/ds-2015-04-16/Trust.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/Trust.md "../../../goto/SdkForRubyV3/ds-2015-04-16/Trust.md")
