# Security Hub controls for AWS Service Catalog

This AWS Security Hub control evaluates the AWS Service Catalog service and resources. The control might not
be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [ServiceCatalog.1] Service Catalog portfolios should be shared within an AWS organization only

**Related requirements:** NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-6,
NIST.800-53.r5 CM-8, NIST.800-53.r5 SC-7

**Category:** Protect > Secure access management

**Severity:** Medium

**Resource type:**
`AWS::ServiceCatalog::Portfolio`

**AWS Config rule:**
[service-catalog-shared-within-organization](../../../config/latest/developerguide/service-catalog-shared-within-organization.md "../../../config/latest/developerguide/service-catalog-shared-within-organization.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether AWS Service Catalog shares portfolios within an organization when the integration with AWS Organizations
is enabled. The control fails if portfolios aren't shared within an organization.

Portfolio sharing only within Organizations helps ensure that a portfolio isn't shared with incorrect AWS accounts. To share
a Service Catalog portfolio with an account in an organization, Security Hub recommends using `ORGANIZATION_MEMBER_ACCOUNT` instead of
`ACCOUNT`. This simplifies administration by governing the access granted to the account across the organization. If you
have a business need to share Service Catalog portfolios with an external account, you can [automatically suppress the findings](automation-rules.md "automation-rules.md") from this
control or [disable it](disable-controls-overview.md "disable-controls-overview.md").

### Remediation

To enable portfolio sharing with AWS Organizations, see [Sharing with AWS Organizations](../../../servicecatalog/latest/adminguide/catalogs_portfolios_sharing_how-to-share.md#portfolio-sharing-organizations "../../../servicecatalog/latest/adminguide/catalogs_portfolios_sharing_how-to-share.md#portfolio-sharing-organizations") in the _AWS Service Catalog Administrator
Guide_.
