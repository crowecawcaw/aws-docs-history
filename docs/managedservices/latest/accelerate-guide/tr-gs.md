# Get started with Trusted Remediator in AMS

Trusted Remediator is available in AMS at no additional charge. Trusted Remediator supports single account and multi-account configurations.

## Onboard to Trusted Remediator

To onboard your AMS accounts to Trusted Remediator, email your Cloud Architects or Cloud Service Delivery Managers (CSDMs). In the email, include the following
information:

- **AWS accounts:** The twelve-digit account identification number. All accounts that you want to onboard to Trusted Remediator must belong
  to the same Accelerate customer.
  - **Delegated administrator account:** The account that is used for Trusted Advisor and Compute Optimizer check configuration for single or multiple accounts.
  - **Member accounts:** These are the accounts linked to the delegated administrator account. These accounts inherit the configurations from the
    delegated administrator account. You can have one member account or multiple member accounts.

  ###### Note

  Member accounts inherit the configurations from the delegated administrator account. If you need different configurations for specific accounts, then onboard
  multiple delegated administrator accounts with your preferred configurations. Plan the account structure and the configurations with your Cloud Architects before you
  onboard.

- **AWS Regions:** The AWS Regions where your resources are located. For a list of AWS Regions, see
  [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").
- **Remediation schedule and time:** Your preferred remediation schedule (daily or weekly). Trusted Remediator gathers Trusted Advisor checks and initiates
  remediation at the scheduled time. For example, you can set the remediation schedule for 1:00 AM Sunday every week, Australian Eastern Standard Time.
- **Notification email:** Trusted Remediator uses the notification email to notify you daily if there are remediations.
  The notification email subject is "Trusted Remediator remediation summary" and the contents provide information on Trusted Remediator remediations run in the
  last 24 hours.

###### Note

Review your applications and resources after every scheduled remediation. For additional support, contact AMS.

After you submit your onboard request with the required details to your CA or CSDM, AMS onboards your accounts to Trusted Remediator. Trusted Remediator uses AWS AppConfig,
a capability of AWS Systems Manager, to define the configuration for the Trusted Advisor checks. These configurations are a set of attributes that are stored in AWS AppConfig. To prevent
unauthorized charges to your resources, all supported Trusted Advisor checks are set to **Inactive** when accounts are onboarded to Trusted Remediator. After you're
onboarded, you can use the AWS AppConfig console or API to manage the configurations. These configurations help you to automatically remediate specific Trusted Advisor checks, or
to assess and manually remediate the remaining checks. The configurations are highly customizable, allowing you to apply configurations for each Trusted Advisor check.
For more information, see [Configure Trusted Advisor check remediation in Trusted Remediator](tr-configure-remediations.md "tr-configure-remediations.md").

## Choose the checks and recommendations to remediate

By default, remediation execution mode is **Inactive** for all Trusted Advisor checks and Compute Optimizer recommendations in your configuration. This prevents
unauthorized remediation and protects resources. AMS provides curated SSM automation documents for Trusted Advisor check remediation.

To select the checks that you want to remediate with Trusted Remediator, complete the following steps:

1. Review the list of supported [Trusted Advisor and Compute Optimizer recommendations or
   and the name of the associated SSM automation documents](tr-supported-checks.md "tr-supported-checks.md") to decide which checks and recommendations you want to remediate with Trusted Remediator.
2. Update your configuration to turn on remediation for your selected Trusted Advisor checks. For instructions on how to select checks, see
   [Configure Trusted Advisor check remediation in Trusted Remediator](tr-configure-remediations.md "tr-configure-remediations.md").

## Track your remediations in Trusted Remediator

After you update your account-level configuration, Trusted Remediator creates OpsItems for each remediation. Trusted Remediator runs the SSM document for automated remediation of
OpsItems according to
your remediation schedule. For instructions on how to view all remediation OpsItems from the Systems Manager OpsCenter console, see
[Track remediations in Trusted Remediator](tr-remediation.md#tr-remediation-track "tr-remediation.md#tr-remediation-track").

## Run manual remediations in Trusted Remediator

You can manually remediate Trusted Advisor checks. When you initiate a manual remediation, Trusted Remediator creates a manual execution OpsItem. You must review and
initiate the SSM automation document to remediate the OpsItems. For more information, see [Run manual remediations in Trusted Remediator](tr-remediation.md#tr-remediation-run "tr-remediation.md#tr-remediation-run").
