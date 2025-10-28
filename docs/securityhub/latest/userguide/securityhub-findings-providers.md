# Understanding integrations in Security Hub CSPM

AWS Security Hub CSPM can ingest security findings from several AWS services and supported
third-party AWS Partner Network security solutions. These integrations can help you get a
comprehensive view of security and compliance across your AWS environment. Security Hub CSPM ingests
findings from integrated solutions and converts them to the AWS Security Finding Format (ASFF).

###### Important

For supported AWS and third-party product integrations, Security Hub CSPM receives and
consolidates findings that are generated only after you enable Security Hub CSPM for your
AWS accounts. The service doesn't retroactively receive and consolidate security
findings that were generated before you enabled Security Hub CSPM.

The **Integrations** page of the Security Hub CSPM console provides access to
available AWS and third-party product integrations. The Security Hub CSPM API also has operations for
managing integrations.

An integration might not be available in all AWS Regions. If an integration isn't
supported in the Region that you are currently signed in to on the Security Hub CSPM console, it doesn't
appear on the **Integrations** page of the console. For a list of
integrations that are available in the China Regions and AWS GovCloud (US) Regions, see [Availability of integrations
by Region](securityhub-regions.md#securityhub-regions-integration-support "securityhub-regions.md#securityhub-regions-integration-support").

In addition to AWS service and built-in third-party integrations, you can integrate
custom security products with Security Hub CSPM. You can then send findings from these products to Security Hub CSPM
by using the Security Hub CSPM API. You can also use the API to update existing findings that Security Hub CSPM
received from a custom security product.

###### Topics

- [Reviewing a list of Security Hub CSPM
  integrations](securityhub-integrations-view-filter.md "securityhub-integrations-view-filter.md")
- [Enabling the flow of findings from a
  Security Hub CSPM integration](securityhub-integration-enable.md "securityhub-integration-enable.md")
- [Disabling the flow of findings from a
  Security Hub CSPM integration](securityhub-integration-disable.md "securityhub-integration-disable.md")
- [Viewing findings from a Security Hub CSPM
  integration](securityhub-integration-view-findings.md "securityhub-integration-view-findings.md")
- [AWS service integrations with
  Security Hub CSPM](securityhub-internal-providers.md "securityhub-internal-providers.md")
- [Third-party product integrations with
  Security Hub CSPM](securityhub-partner-providers.md "securityhub-partner-providers.md")
- [Integrating Security Hub CSPM with custom products](securityhub-custom-providers.md "securityhub-custom-providers.md")
