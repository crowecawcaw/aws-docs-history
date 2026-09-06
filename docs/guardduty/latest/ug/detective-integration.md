

# Integrating with Amazon Detective
<a name="detective-integration"></a>

[Amazon Detective](https://docs.aws.amazon.com/detective/latest/userguide/what-is-detective.html) helps you quickly analyze and investigate security events across one or more AWS accounts by generating data visualizations that represent the ways your resources behave and interact over time. Detective creates visualizations of GuardDuty findings.

Detective ingests finding details for all finding types, and provides access to the entity profiles to investigate different entities that are involved with the finding. An entity can be an AWS account, an AWS resource within an account, or an external IP Address that has interacted with your resources. The GuardDuty console supports pivoting to Amazon Detective from the following entities, depending on finding type: AWS account, IAM role, user, or role session, user agent, federated user, Amazon EC2 instance, or IP address. 

**Contents**
+ [Enabling the integration](#detective-integration-enable)
+ [Pivoting to Amazon Detective from a GuardDuty finding](#pivot-to-detective)
+ [Using the integration with a GuardDuty multi-account environment](#detective-integration-multiaccount)

## Enabling the integration
<a name="detective-integration-enable"></a>

To use Amazon Detective with GuardDuty you must first enable Amazon Detective. For information on how to enable Detective, see [Geting started with Amazon Detective](https://docs.aws.amazon.com/detective/latest/userguide/detective-setup.html) in the *Amazon Detective User Guide*.

When you enable both GuardDuty and Detective, the integration is enabled automatically. Once enabled, Detective will immediately ingest your GuardDuty findings data.

**Note**  
GuardDuty sends findings to Detective based on the GuardDuty findings export frequency. By default, the export frequency for updates to existing findings is 6 hours. To ensure Detective receives the most recent updates to your findings it is recommended that you change the export frequency to 15 minutes in each region in which you use Detective with GuardDuty. For more information see [Step 5 – Setting frequency to export updated active findings](guardduty_exportfindings.md#guardduty_exportfindings-frequency).

## Pivoting to Amazon Detective from a GuardDuty finding
<a name="pivot-to-detective"></a>

1. Log into the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console.

1. Choose a single finding from your findings table.

1. Choose **Investigate with Detective** from the finding details pane.

1. Choose an aspect of the finding to investigate with Amazon Detective. This opens the Detective console for that finding or entity.

If the pivot does not behave as expected, see [Troubleshooting the pivot](https://docs.aws.amazon.com/detective/latest/userguide/profile-pivot-from-service.html#profile-pivot-troubleshooting) in the *Amazon Detective User Guide*.

**Note**  
If you archive a GuardDuty finding in the Detective console, that finding gets archived in the GuardDuty console as well.

## Using the integration with a GuardDuty multi-account environment
<a name="detective-integration-multiaccount"></a>

If you are managing a multi-account environment in GuardDuty, you must add your member accounts to Amazon Detective to view Detective data visualizations for findings and entities in those accounts.

It is recommended that you use the same GuardDuty Administrator account as the administrator account for Detective. For more information on adding member accounts in Detective, see [Managing accounts](https://docs.aws.amazon.com/detective/latest/userguide/accounts.html) in the *Amazon Detective User Guide*.

**Note**  
Detective is a regional service, meaning you must enable Detective and add your member accounts in each region in which you want to use the integration.