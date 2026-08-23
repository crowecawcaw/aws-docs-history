# TagPropagationConfiguration

Specifies configuration for propagating resource tags from source log groups to centralized
destination log groups. The service uses a customer-managed IAM role in the destination
account to add, update, and remove tags on destination log groups.

## Contents

**DestinationRoleArn**

The ARN of a customer-managed IAM role in the destination account. The service assumes
this role to propagate tags to destination log groups. You must have
`iam:PassRole` permission on this role.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws[a-zA-Z-]*:iam::\d{12}:role/[\w+=,.@/-]+`

Required: Yes

**TagConflictResolutionStrategy**

The strategy for resolving conflicts when a tag key exists on both the source and
destination log groups. If not specified, defaults to `UPDATE_SYNC`.

- `ADD_ONLY` – Only adds new tags from the source without
  modifying existing destination tags.
- `UPDATE_SYNC` – Adds new tags and updates existing tags from
  the source. Does not remove destination tags that are absent from the
  source.
- `IN_SYNC` – Keeps destination tags fully synchronized with
  source tags, including removing destination tags that do not exist on the
  source.

Type: String

Valid Values: `IN_SYNC | ADD_ONLY | UPDATE_SYNC`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TagPropagationConfiguration.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/TagPropagationConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TagPropagationConfiguration.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/TagPropagationConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TagPropagationConfiguration.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/TagPropagationConfiguration.md")
