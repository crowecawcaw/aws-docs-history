

# Integration with AWS Security Hub CSPM
<a name="securityhub-integration"></a>

**Integration type:** Source

[AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) provides you with a comprehensive view of your security state in AWS and helps your environment against security industry standards and best practices. Security Hub CSPM collects security data from across AWS accounts, services, and supported third-party partner products and helps you to analyze your security trends and identify the highest priority security issues.

When you enable Security Hub CSPM and add Security Hub CSPM findings as a source in Security Lake, Security Hub CSPM starts sending new findings and updates to existing findings to Security Lake.

## How Security Lake receives Security Hub CSPM findings
<a name="securityhub-integration-sending-findings"></a>

In Security Hub CSPM, security issues are tracked as findings. Some findings come from issues that are detected by other AWS services or by third-party partners. Security Hub CSPM also generates its own findings by running automated and continuous security checks against rules. The rules are represented by security controls.

All findings in Security Hub CSPM use a standard JSON format called the [AWS Security Finding Format (ASFF)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html).

Security Lake receives Security Hub CSPM findings and transforms them into the [Open Cybersecurity Schema Framework (OCSF) in Security Lake](open-cybersecurity-schema-framework.md).

## Send your Security Hub CSPM findings to Security Lake
<a name="send-securityhub-findings"></a>

To send Security Hub CSPM findings to Security Lake, you must enable both services and add Security Hub CSPM findings as a source in Security Lake. For instructions on adding an AWS source, see [Adding an AWS service as a source](internal-sources.md#add-internal-sources).

If you want Security Hub CSPM to generate [control findings ](https://docs.aws.amazon.com/securityhub/latest/userguide/controls-findings-create-update.html) and send them to Security Lake, you must enable the relevant security standards and turn on resource recording on a Regional basis in AWS Config. For more information, see [Enabling and configuring AWS Config](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-prereq-config.html) in the *AWS Security Hub User Guide*.

## Stop receiving Security Hub CSPM findings in Security Lake
<a name="securityhub-integration-disable"></a>

To stop receiving Security Hub CSPM findings, you can use the Security Hub CSPM console, Security Hub CSPM API, or AWS CLI in the following topics in the *AWS Security Hub User Guide*:
+ [Disabling and enabling the flow of findings from an integration (console)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-integrations-managing.html#securityhub-integration-findings-flow-console)
+ [Disabling the flow of findings from an integration (Security Hub API, AWS CLI)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-integrations-managing.html#securityhub-integration-findings-flow-disable-api)