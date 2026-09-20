

# Integration with AWS Security Hub CSPM
<a name="securityhub-integration"></a>

[AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) provides you with a comprehensive view of your security state in AWS and helps you to check your environment against security industry standards and best practices. Security Hub CSPM collects security data from across AWS accounts, services, and supported third-party partner products and helps you to analyze your security trends and identify the highest priority security issues.

The Amazon Connect Talent integration with Security Hub CSPM enables you to send findings from Amazon Connect Talent to Security Hub CSPM. Security Hub CSPM can then include those findings in its analysis of your security posture.

**Contents**
+ [How Amazon Connect Talent sends findings to Security Hub CSPM](#securityhub-integration-sending-findings)
  + [Types of findings that Amazon Connect Talent sends](#securityhub-integration-finding-types)
  + [Latency for sending findings](#securityhub-integration-finding-latency)
  + [Typical finding from Amazon Connect Talent](#securityhub-integration-finding-example)
+ [Enabling and configuring the integration with AWS Security Hub CSPM](#securityhub-integration-enable)
+ [How to stop sending findings to AWS Security Hub CSPM](#securityhub-integration-disable)

## How Amazon Connect Talent sends findings to Security Hub CSPM
<a name="securityhub-integration-sending-findings"></a>

In Security Hub CSPM, security issues are tracked as findings. Some findings come from issues that are detected by other AWS services or by third-party partners. Security Hub CSPM also has a set of rules that it uses to detect security issues and generate findings.

Security Hub CSPM provides tools to manage findings from across all of these sources. You can view and filter lists of findings and view details for a finding. See [Viewing findings](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-viewing.html) in the *AWS Security Hub User Guide*. You can also track the status of an investigation into a finding. See [Taking action on findings](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-taking-action.html) in the *AWS Security Hub User Guide*.

All findings in Security Hub CSPM use a standard JSON format called the AWS Security Finding Format (ASFF). The ASFF includes details about the source of the issue, the affected resources, and the current status of the finding. See [AWS Security Finding Format (ASFF)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html) in the *AWS Security Hub User Guide*.

Amazon Connect Talent is one of the AWS services that sends findings to Security Hub CSPM.

### Types of findings that Amazon Connect Talent sends
<a name="securityhub-integration-finding-types"></a>

Amazon Connect Talent sends the findings to Security Hub CSPM using the [AWS Security Finding Format (ASFF)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html). In ASFF, the `Types` field provides the finding type.

### Latency for sending findings
<a name="securityhub-integration-finding-latency"></a>

When Amazon Connect Talent creates a new finding, it sends the finding to Security Hub CSPM in near real time.

### Typical finding from Amazon Connect Talent
<a name="securityhub-integration-finding-example"></a>

Amazon Connect Talent sends findings to Security Hub CSPM using the [AWS Security Finding Format (ASFF)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html).

## Enabling and configuring the integration with AWS Security Hub CSPM
<a name="securityhub-integration-enable"></a>

To use the integration with AWS Security Hub CSPM, you must enable Security Hub CSPM. For information on how to enable Security Hub CSPM, see [Setting up Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html) in the *AWS Security Hub User Guide*.

## How to stop sending findings to AWS Security Hub CSPM
<a name="securityhub-integration-disable"></a>

To stop sending findings to Security Hub CSPM, you can use either the Security Hub CSPM console or the API.

See [Disabling and enabling the flow of findings from an integration (console)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-integrations-managing.html#securityhub-integration-findings-flow-console) or [Disabling the flow of findings from an integration (Security Hub API, AWS CLI)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-integrations-managing.html#securityhub-integration-findings-flow-disable-api) in the *AWS Security Hub User Guide*.