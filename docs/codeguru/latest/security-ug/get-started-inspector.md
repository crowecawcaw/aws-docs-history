On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Integrate with Amazon Inspector

Amazon CodeGuru Security is available through Amazon Inspector Lambda code scanning. For more information, see
[Scanning AWS Lambda
functions with Amazon Inspector](../../../inspector/latest/user/scanning-lambda.md "../../../inspector/latest/user/scanning-lambda.md").

###### Note

CodeGuru Security only reports critical and high severity vulnerabilities in Lambda code scans with
Amazon Inspector. Medium, low, and informational code quality findings are not returned.

The following steps show how to activate AWS Lambda code scanning with Amazon Inspector. After you
activate code scanning, code scans are automated and you can view findings in the **All
findings** section in the Amazon Inspector console.

You can also complete these steps on the **Integrations** page in the [CodeGuru Security console](https://console.aws.amazon.com/codeguru/security/integrations "https://console.aws.amazon.com/codeguru/security/integrations"). Choose
**Integrate with Amazon Inspector** to get started.

###### Activate code scanning for Lambda

1. Open the
   [Amazon Inspector console](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. In the navigation bar, choose **Account management**.
3. Select the accounts that you want to activate Lambda code scanning in.
4. Choose **Activate**, then choose
   **AWS Lambda code scanning**.
