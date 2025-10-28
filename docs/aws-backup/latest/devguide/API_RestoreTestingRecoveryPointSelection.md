# RestoreTestingRecoveryPointSelection

`RecoveryPointSelection` has five parameters (three required and two
optional). The values you specify determine which recovery point is included in the restore
test. You must indicate with `Algorithm` if you want the latest recovery point
within your `SelectionWindowDays` or if you want a random recovery point, and
you must indicate through `IncludeVaults` from which vaults the recovery points
can be chosen.

`Algorithm` (_required_) Valid values:
"`LATEST_WITHIN_WINDOW`" or "`RANDOM_WITHIN_WINDOW`".

`Recovery point types` (_required_) Valid values:
"`SNAPSHOT`" and/or "`CONTINUOUS`". Include `SNAPSHOT`
to restore only snapshot recovery points; include `CONTINUOUS` to restore
continuous recovery points (point in time restore / PITR); use both to restore either a
snapshot or a continuous recovery point. The recovery point will be determined by the value
for `Algorithm`.

`IncludeVaults` (_required_). You must include one or more
backup vaults. Use the wildcard ["\*"] or specific ARNs.

`SelectionWindowDays` (_optional_) Value must be an
integer (in days) from 1 to 365. If not included, the value defaults to
`30`.

`ExcludeVaults` (_optional_). You can choose to input one
or more specific backup vault ARNs to exclude those vaults' contents from restore
eligibility. Or, you can include a list of selectors. If this parameter and its value are
not included, it defaults to empty list.

## Contents

**Algorithm**

Acceptable values include "LATEST_WITHIN_WINDOW" or
"RANDOM_WITHIN_WINDOW"

Type: String

Valid Values: `LATEST_WITHIN_WINDOW | RANDOM_WITHIN_WINDOW`

Required: No

**ExcludeVaults**

Accepted values include specific ARNs or list of selectors.
Defaults to empty list if not listed.

Type: Array of strings

Required: No

**IncludeVaults**

Accepted values include wildcard ["\*"] or by specific ARNs or
ARN wilcard replacement
["arn:aws:backup:us-west-2:123456789012:backup-vault:asdf", ...]
["arn:aws:backup:\*:\*:backup-vault:asdf-\*", ...]

Type: Array of strings

Required: No

**RecoveryPointTypes**

These are the types of recovery points.

Include `SNAPSHOT`
to restore only snapshot recovery points; include `CONTINUOUS` to restore
continuous recovery points (point in time restore / PITR); use both to restore either a
snapshot or a continuous recovery point. The recovery point will be determined by the value
for `Algorithm`.

Type: Array of strings

Valid Values: `CONTINUOUS | SNAPSHOT`

Required: No

**SelectionWindowDays**

Accepted values are integers from 1 to 365.

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/RestoreTestingRecoveryPointSelection.md "../../../goto/SdkForCpp/backup-2018-11-15/RestoreTestingRecoveryPointSelection.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingRecoveryPointSelection.md "../../../goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingRecoveryPointSelection.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingRecoveryPointSelection.md "../../../goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingRecoveryPointSelection.md")
