# Preparing to send findings to AWS Security Hub CSPM

As an APN Partner, you cannot send information to Security Hub CSPM for your customers until the Security Hub CSPM
team enables you as a finding provider. To be enabled as a finding provider, you must complete
the following onboarding steps. Doing so ensures a positive experience Security Hub CSPM for you and your
customers.

As you complete the onboarding steps, be sure to follow the guidelines in [Tenets for creating and updating findings](tenets-update-create-findings.md "tenets-update-create-findings.md"), [Guidelines for mapping findings into the AWS Security
Finding Format (ASFF)](guidelines-asff-mapping.md "guidelines-asff-mapping.md"), and [Guidelines for using the
BatchImportFindings API](guidelines-batchimportfindings.md "guidelines-batchimportfindings.md").

1. Map your security findings to the AWS Security Finding Format (ASFF).
2. Build your integration architecture to push findings to the correct Regional Security Hub CSPM
   endpoint. To do this, you define whether you will send findings from your own AWS account or
   from within your customer's accounts.
3. Have your customers subscribe the product to their account. To do this, they can use the
   console or the [`EnableImportFindingsForProduct`](../../1.0/APIReference/API_EnableImportFindingsForProduct.md "../../1.0/APIReference/API_EnableImportFindingsForProduct.md") API operation. See [Managing product integrations](../userguide/securityhub-integrations-managing.md "../userguide/securityhub-integrations-managing.md") in the _AWS Security Hub CSPM User Guide_.

You can also subscribe the product for them. To do this, you use a cross-account role to
access the [`EnableImportFindingsForProduct`](../../1.0/APIReference/API_EnableImportFindingsForProduct.md "../../1.0/APIReference/API_EnableImportFindingsForProduct.md") API operation on behalf of the
customer.

This step establishes the resource policies that are needed to accept findings from that
product for that account.
The following blog posts discuss some of the existing partner integrations with
Security Hub CSPM.

- [Announcing Cloud
  Custodian Integration with AWS Security Hub CSPM](https://aws.amazon.com/blogs/opensource/announcing-cloud-custodian-integration-aws-security-hub/ "https://aws.amazon.com/blogs/opensource/announcing-cloud-custodian-integration-aws-security-hub/")
- [Use AWS Fargate and Prowler to send security configuration findings about AWS services to
  Security Hub CSPM](https://aws.amazon.com/blogs/security/use-aws-fargate-prowler-send-security-configuration-findings-about-aws-services-security-hub/ "https://aws.amazon.com/blogs/security/use-aws-fargate-prowler-send-security-configuration-findings-about-aws-services-security-hub/")
- [How to import
  AWS Config rules evaluations as findings in Security Hub CSPM](https://aws.amazon.com/blogs/security/how-to-import-aws-config-rules-evaluations-findings-security-hub/ "https://aws.amazon.com/blogs/security/how-to-import-aws-config-rules-evaluations-findings-security-hub/")
