# HumanLoopActivationOutput

Shows the results of the human in the loop evaluation. If there is no HumanLoopArn, the
input did not trigger human review.

## Contents

**HumanLoopActivationConditionsEvaluationResults**

Shows the result of condition evaluations, including those conditions which activated a
human review.

Type: String

Length Constraints: Maximum length of 10240.

Required: No

**HumanLoopActivationReasons**

Shows if and why human review was needed.

Type: Array of strings

Array Members: Minimum number of 1 item.

Required: No

**HumanLoopArn**

The Amazon Resource Name (ARN) of the HumanLoop created.

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/HumanLoopActivationOutput.md "../../../goto/SdkForCpp/textract-2018-06-27/HumanLoopActivationOutput.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/HumanLoopActivationOutput.md "../../../goto/SdkForJavaV2/textract-2018-06-27/HumanLoopActivationOutput.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/HumanLoopActivationOutput.md "../../../goto/SdkForRubyV3/textract-2018-06-27/HumanLoopActivationOutput.md")
