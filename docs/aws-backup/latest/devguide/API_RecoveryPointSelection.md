# RecoveryPointSelection

This specifies criteria to assign
a set of resources, such as resource types or backup vaults.

## Contents

**DateRange**

This is a resource filter containing FromDate: DateTime
and ToDate: DateTime. Both values are required. Future DateTime
values are not permitted.

The date and time are in Unix format and Coordinated
Universal Time (UTC), and it is accurate to milliseconds
((milliseconds are optional).
For example, the value 1516925490.087 represents Friday, January
26, 2018 12:11:30.087 AM.

Type: [DateRange](API_DateRange.md "API_DateRange.md") object

Required: No

**ResourceIdentifiers**

These are the resources included in the resource selection
(including type of resources and vaults).

Type: Array of strings

Required: No

**VaultNames**

These are the names of the vaults in which the selected
recovery points are contained.

Type: Array of strings

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/RecoveryPointSelection.md "../../../goto/SdkForCpp/backup-2018-11-15/RecoveryPointSelection.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/RecoveryPointSelection.md "../../../goto/SdkForJavaV2/backup-2018-11-15/RecoveryPointSelection.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/RecoveryPointSelection.md "../../../goto/SdkForRubyV3/backup-2018-11-15/RecoveryPointSelection.md")
