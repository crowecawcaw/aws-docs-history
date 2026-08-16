# Request Foundational Technical Review for your solutions

You can submit a Foundational Technical Review (FTR) validation request for your active software
solutions listed in AWS Marketplace. The streamlined FTR process accepts industry-standard compliance
certifications aligned to the same security, reliability, and operational standards that AWS validates,
and returns approval or actionable feedback within minutes.

## Accepted validation documents

You can submit either of the following reports to satisfy FTR requirements:

- **SOC 2 Type II report** — A third-party audit report from an
  accredited auditor that covers the trust services criteria for your AWS-hosted workload.
- **[AWS Well-Architected Framework Review](../../../wellarchitected/latest/userguide/waf.md "../../../wellarchitected/latest/userguide/waf.md") (WAFR) report** — A
  completed review that assesses your workload against the six pillars of the AWS Well-Architected
  Framework: operational excellence, security, reliability, performance efficiency, cost optimization,
  and sustainability. The review must cover your solution's primary AWS-hosted workload.

## Prerequisites

Your solution must meet the following requirements before you can submit for FTR validation. In
AWS Partner Central, the **Validation** tab displays these as a prerequisite
checklist. Checks run in sequence — later checks remain blocked until earlier ones pass.

| Prerequisite                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Solution is linked to an AWS Marketplace product                     | Your solution must have an AWS Marketplace product linked through the AWS Marketplace<br>tab. To complete this, ensure you have completed<br>[Partner Central AWS account linking](../getting-started/account-linking.md "../getting-started/account-linking.md")<br>or access Partner Central on the AWS Console.                                                                                                                                                                                                                    |
| Solution is linked to only one AWS Marketplace product               | FTR validation supports one product per solution. If your solution has multiple products<br>linked, remove extras or create a separate solution for each product.                                                                                                                                                                                                                                                                                                                                                                     |
| Solution does not contain non-AWS Marketplace products               | All products in the solution must be AWS Marketplace listings. Remove any<br>non-Marketplace products.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Solution is linked to a software product                             | The linked product must be a software type (SaaS, AMI, Container, or Machine Learning).<br>Professional services and other non-software types are not eligible for this validation<br>path.                                                                                                                                                                                                                                                                                                                                           |
| AWS Marketplace product is deployed on AWS                           | Your product must have an approved AWS hosted architecture. Upload an architecture<br>diagram in the AWS Marketplace Management Portal showing your solution running on AWS<br>infrastructure.                                                                                                                                                                                                                                                                                                                                        |
| AWS Marketplace product is Partner Revenue Measurement (PRM) enabled | [Partner Revenue Measurement](../../../PRM/latest/aws-prm-onboarding-guide/what-is-service.md "../../../PRM/latest/aws-prm-onboarding-guide/what-is-service.md")<br>must be enabled for the product. After you enable PRM, it can take up to 7 days for<br>measurement data to appear. This check is complete when the product appears in your<br>[Attributed revenue dashboard](../getting-started/partner-analytics-attributed-revenue.md "../getting-started/partner-analytics-attributed-revenue.md")<br>as an onboarded product. |

After you make changes to resolve a prerequisite, choose **Refresh** on the
Validation tab to update the status.

## Request FTR validation

After all prerequisites show as complete, you can submit a validation document.

1. Sign in to [AWS Partner Central](https://partnercentral.awspartner.com "https://partnercentral.awspartner.com").
2. From the navigation, choose **Build**, then **Solutions**.
3. Choose the solution you want to validate.
4. Navigate to the **Validation** tab. Confirm that all prerequisites show a
   status of **Complete**.
5. Choose **Request validation**.
6. For **Report type**, select either **SOC 2 report** or
   **WAFR report**.
7. Upload your validation document. Maximum file size is 3 MB. Accepted format: PDF.
8. Choose **Request FTR**.

Your submission is reviewed automatically. You receive approval or feedback within minutes.

## Review results

After you submit, the FTR status on your solution updates to reflect the outcome:

- **Approved** — Your solution passed FTR validation. The
  Validation tab displays the FTR expiration date and your solution is eligible for program benefits
  including badging, Partner Solutions Finder listing, and APN program eligibility.
- **Action required** — Your submission did not pass one or more
  validation checks. The Validation tab displays specific feedback identifying which checks
  failed and what to address. Review the feedback, work with your auditor or team to resolve the
  issues, then choose **Resubmit** to upload an updated report.

## Validation checks

The automated review evaluates your submitted report against the following checks. For the full
list of FTR requirements, see the
[Software FTR guide](https://partnercentral.awspartner.com/partnercentral2/s/article?category=Introductory_resources&article=AWS-Foundational-Technical-Review "https://partnercentral.awspartner.com/partnercentral2/s/article?category=Introductory_resources&article=AWS-Foundational-Technical-Review").

**SOC 2 Type II reports:**

- Report issue date is within 1 year
- Unqualified auditor opinion
- AWS infrastructure is in scope (system description references your AWS-hosted components)
- The specific partner solution is in scope
- Security and Availability trust services criteria are included

**WAFR reports:**

- Report is less than 1 year old
- Zero high-risk issues (HRIs) identified in the Security, Operational Excellence, and Reliability pillars
- The specific partner solution is referenced in either the workload name or workload description
- The reviewer's full name and email address are referenced in the reviewer owner field
- The WAFR is conducted using the AWS Well-Architected Tool (the review can be performed by the partner as a self-service exercise, or with the assistance of an AWS employee, a Well-Architected Program Partner (WAPP), or ISV tools)

## Resubmit after feedback

If your report does not pass validation:

1. On the **Validation** tab, review the feedback in the
   **Validation feedback** section.
2. Address the identified issues with your auditor or team.
3. Choose **Resubmit**.
4. Upload the corrected report and submit.

You can resubmit as many times as needed. Each submission is reviewed automatically and returns
results within minutes.

## Related resources

- [AWS Well-Architected Framework](../../../wellarchitected/latest/userguide/waf.md "../../../wellarchitected/latest/userguide/waf.md")
- [Partner Revenue Measurement onboarding guide](../../../PRM/latest/aws-prm-onboarding-guide/what-is-service.md "../../../PRM/latest/aws-prm-onboarding-guide/what-is-service.md")
- [Attributed revenue dashboard](../getting-started/partner-analytics-attributed-revenue.md "../getting-started/partner-analytics-attributed-revenue.md")
