# ExpenseField

Breakdown of detected information, seperated into
the catagories Type, LabelDetection, and ValueDetection

## Contents

**Currency**

Shows the kind of currency, both the code and confidence associated with any monatary value
detected.

Type: [ExpenseCurrency](API_ExpenseCurrency.md "API_ExpenseCurrency.md") object

Required: No

**GroupProperties**

Shows which group a response object belongs to, such as whether an address line
belongs to the vendor's address or the recipent's address.

Type: Array of [ExpenseGroupProperty](API_ExpenseGroupProperty.md "API_ExpenseGroupProperty.md") objects

Required: No

**LabelDetection**

The explicitly stated label of a detected element.

Type: [ExpenseDetection](API_ExpenseDetection.md "API_ExpenseDetection.md") object

Required: No

**PageNumber**

The page number the value was detected on.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**Type**

The implied label of a detected element. Present alongside LabelDetection for explicit elements.

Type: [ExpenseType](API_ExpenseType.md "API_ExpenseType.md") object

Required: No

**ValueDetection**

The value of a detected element. Present in explicit and implicit elements.

Type: [ExpenseDetection](API_ExpenseDetection.md "API_ExpenseDetection.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/ExpenseField.md "../../../goto/SdkForCpp/textract-2018-06-27/ExpenseField.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/ExpenseField.md "../../../goto/SdkForJavaV2/textract-2018-06-27/ExpenseField.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/ExpenseField.md "../../../goto/SdkForRubyV3/textract-2018-06-27/ExpenseField.md")
