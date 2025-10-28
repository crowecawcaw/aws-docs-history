# AWS Marketplace Vendor Insights

AWS Marketplace Vendor Insights is a feature that simplifies software risk assessments performed by organizations to
safeguard procuring software they trust and meets their standards. With AWS Marketplace Vendor Insights, buyers can
monitor the security profile of a product in near real-time from a single console. AWS Marketplace Vendor Insights can
ease the procurement process for buyers and potentially increase sales for sellers. It reduces a
buyer's assessment effort by providing a dashboard of the software product’s security and
compliance information.

All security and compliance information in the AWS Marketplace Vendor Insights dashboard is based on evidence
gathered from the following sources:

- Seller's self-attestation, including the AWS Marketplace Vendor Insights security self-assessment and Consensus
  Assessment Initiative Questionnaire (CAIQ)
- Industry standard audit reports (for example, International Organization for
  Standardization ISO 27001)
- AWS Audit Manager, which automates evidence collection from the seller's production
  environment
  AWS Marketplace Vendor Insights gathers compliance artifacts and security control information about the product and
  presents it in a dashboard. The dashboard takes data from the seller's self-assessment, evidence
  from audit reports, and live evidence from AWS accounts. This data feeds into the security
  controls and then to the dashboard for buyers to review. Live evidence is the method of
  consistently updating data from multiple sources to present the most current information.
  AWS Config is enabled in the seller's environment. Data about configurations, backups enabled, and
  other information is updated automatically. For example, assume that the **Access Control** for a product is **Compliant** and an Amazon Simple Storage Service
  (Amazon S3) bucket becomes public. The dashboard would display that the control's status changed from
  **Compliant** to **Undetermined**.

You must set up the baseline resources and infrastructure in your AWS accounts before
using AWS Marketplace Vendor Insights. After setup is completed, AWS Marketplace Vendor Insights can gather information and generate security
profiles for your software as a service (SaaS) products in AWS Marketplace.

###### Contents

- [Understanding AWS Marketplace Vendor Insights](vendor-insights-understanding.md "vendor-insights-understanding.md")
- [Setting up AWS Marketplace Vendor Insights](vendor-insights-setting-up.md "vendor-insights-setting-up.md")
- [Viewing your AWS Marketplace Vendor Insights profile](vendor-insights-profile.md "vendor-insights-profile.md")
- [Managing snapshots in AWS Marketplace Vendor Insights](vendor-insights-snapshot.md "vendor-insights-snapshot.md")
- [Controlling access in
  AWS Marketplace Vendor Insights](vendor-insights-seller-controlling-access.md "vendor-insights-seller-controlling-access.md")
