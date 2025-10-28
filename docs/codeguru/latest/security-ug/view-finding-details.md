On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# View finding details

To view finding details in the console, open the **Findings**
page in the [CodeGuru Security
console](https://console.aws.amazon.com/codeguru/security/Findings "https://console.aws.amazon.com/codeguru/security/Findings"), and choose the finding you want to view details about. You can also view
finding details with the AWS CLI and AWS SDKs.

###### Topics

- [Finding details](#finding-details "#finding-details")
- [View finding details with the AWS CLI and AWS SDKs](#view-finding-details-cli-sdk "#view-finding-details-cli-sdk")

## Finding details

The finding details page gives overview information about the finding and the suggested
remediation to close the finding. The name of the vulnerability is displayed at the top of the
page with a brief description.

- **Overview** - The Overview panel includes the following key
  information about the finding, in addition to other details like the finding ID, the name of
  the scan that generated the finding, the file path, and the rule ID. For additional
  information on these concepts, see [Terminology and metrics](terms-and-metrics.md "terms-and-metrics.md").
  - **Vulnerability name** - The name of the detected
    vulnerability. You can learn more about how the vulnerability was detected by choosing the
    vulnerability name that links to the corresponding detector in the [Amazon CodeGuru Detector
    Library](../../detector-library.md "../../detector-library.md").
  - **Status** - Finding status can be Open or Closed.
  - **Relevant CWEs** - One or more Common Weakness
    Enumeration types that apply to the detector that identified the security vulnerability.
    Choose the link to the CWE to learn more.
  - **Severity** - The severity of the finding can be
    critical, high, medium, low, or informational. For information about how the severity is
    calculated, see [How severity is calculated](finding-severity.md#severity-calculation "finding-severity.md#severity-calculation").
  - **Vulnerability tags** - Categorizations for this type of
    vulnerability. You can learn more about similar types of vulnerabilities by choosing the
    vulnerability tag that redirects you to that tag’s page in the [Amazon CodeGuru Detector
    Library](../../detector-library.md "../../detector-library.md").

- **Suggested remediation** - The suggested remediation for a
  finding describes the vulnerability detected in your code, why it may pose a security risk,
  and how to remediate it.
- **Suggested code change** - Some findings include inline
  code updates to replace your vulnerable code. The suggested code change indicates the portion
  of code where the vulnerability was detected and provides the inline code update to remediate
  it. Several code changes may be offered for you to select from depending on what solution
  applies to your use case.

For more information on updating your code with suggested changes, see [Add suggested code changes with the console](address-findings.md#suggested-code-changes "address-findings.md#suggested-code-changes").

- **Code snippet** - If there is no suggested code change, the
  code snippet section displays the portion of your code where the vulnerability was detected,
  and highlights the vulnerable lines of code that need to be updated based on the suggested
  remediation.

## View finding details with the AWS CLI and AWS SDKs

To view finding details with the AWS CLI or AWS SDKs, use the [`GetFindings`](../security-api/API_GetFindings.md "../security-api/API_GetFindings.md") or
[`BatchGetFindings`](../security-api/API_BatchGetFindings.md "../security-api/API_BatchGetFindings.md") operations. For more information, see the
[Amazon CodeGuru Security API Reference](../security-api.md "../security-api.md").
