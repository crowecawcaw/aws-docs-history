# FrameworkControl

Contains detailed information about all of the controls of a framework. Each framework
must contain at least one control.

## Contents

**ControlName**

The name of a control. This name is between 1 and 256 characters.

Type: String

Required: Yes

**ControlInputParameters**

The name/value pairs.

Type: Array of [ControlInputParameter](API_ControlInputParameter.md "API_ControlInputParameter.md") objects

Required: No

**ControlScope**

The scope of a control. The control scope defines what the control will evaluate. Three
examples of control scopes are: a specific backup plan, all backup plans with a specific
tag, or all backup plans.

For more information, see [`ControlScope`.](API_ControlScope.md "API_ControlScope.md")

Type: [ControlScope](API_ControlScope.md "API_ControlScope.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/FrameworkControl.md "../../../goto/SdkForCpp/backup-2018-11-15/FrameworkControl.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/FrameworkControl.md "../../../goto/SdkForJavaV2/backup-2018-11-15/FrameworkControl.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/FrameworkControl.md "../../../goto/SdkForRubyV3/backup-2018-11-15/FrameworkControl.md")
