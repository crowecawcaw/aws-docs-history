# Sending Rule

Evaluations to Security Hub

After adding an AWS Config rule, you can also send rule evaluations to AWS Security Hub. The
integration between AWS Config and Security Hub allows you to triage and remediate rule evaluations
alongside other misconfigurations and security issues.

## Send Rule Evaluations to Security Hub

To send rule evaluations to Security Hub, you must first set up AWS Security Hub and AWS Config, and
then add at least one AWS Config managed or custom rule. After this, AWS Config immediately
starts sending rule evaluations to Security Hub. Security Hub enriches the rule evaluations and
transforms them into Security Hub findings.

For more information about this integration, see [Available AWS Service Integrations](../../../securityhub/latest/userguide/securityhub-internal-providers.md#integration-config "../../../securityhub/latest/userguide/securityhub-internal-providers.md#integration-config") in the AWS Security Hub User
Guide.
