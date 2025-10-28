# ControlInputParameter

The parameters for a control. A control can have zero, one, or more than one
parameter. An example of a control with two parameters is: "backup plan frequency is at
least `daily` and the retention period is at least `1 year`". The
first parameter is `daily`. The second parameter is `1 year`.

## Contents

**ParameterName**

The name of a parameter, for example, `BackupPlanFrequency`.

Type: String

Required: No

**ParameterValue**

The value of parameter, for example, `hourly`.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ControlInputParameter.md "../../../goto/SdkForCpp/backup-2018-11-15/ControlInputParameter.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ControlInputParameter.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ControlInputParameter.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ControlInputParameter.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ControlInputParameter.md")
