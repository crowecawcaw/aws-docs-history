# Integrating with Amazon Detective

[Amazon Detective](../../../detective/latest/userguide/what-is-detective.md "../../../detective/latest/userguide/what-is-detective.md") helps you quickly analyze and investigate security events across one
or more AWS accounts by generating data visualizations that represent the ways your
resources behave and interact over time. Detective creates visualizations of GuardDuty
findings.

Detective ingests finding details for all finding types, and provides access to the entity
profiles to investigate different entities that are involved with the finding. An entity can
be an AWS account, an AWS resource within an account, or an external IP Address that has
interacted with your resources. The GuardDuty console supports pivoting to Amazon Detective from the
following entities, depending on finding type: AWS account, IAM role, user, or role
session, user agent, federated user, Amazon EC2 instance, or IP address.

###### Contents

- [Enabling the integration](detective-integration.md#detective-integration-enable "detective-integration.md#detective-integration-enable")
- [Pivoting to Amazon Detective from a GuardDuty finding](detective-integration.md#pivot-to-detective "detective-integration.md#pivot-to-detective")
- [Using the integration with a GuardDuty
  multi-account environment](detective-integration.md#detective-integration-multiaccount "detective-integration.md#detective-integration-multiaccount")

## Enabling the integration

To use Amazon Detective with GuardDuty you must first enable Amazon Detective. For information on how to
enable Detective, see [Geting started with Amazon Detective](../../../detective/latest/userguide/detective-setup.md "../../../detective/latest/userguide/detective-setup.md")
in the _Amazon Detective User Guide_.

When you enable both GuardDuty and Detective, the integration is enabled automatically. Once
enabled, Detective will immediately ingest your GuardDuty findings data.

###### Note

GuardDuty sends findings to Detective based on the GuardDuty findings export frequency. By
default, the export frequency for updates to existing findings is 6 hours. To ensure
Detective receives the most recent updates to your findings it is recommended that you
change the export frequency to 15 minutes in each region in which you use Detective with
GuardDuty. For more information see [Step 5 – Setting frequency
to export updated active findings](guardduty_exportfindings.md#guardduty_exportfindings-frequency "guardduty_exportfindings.md#guardduty_exportfindings-frequency").

## Pivoting to Amazon Detective from a GuardDuty finding

1. Log into the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console.
2. Choose a single finding from your findings table.
3. Choose **Investigate with Detective** from the finding
   details pane.
4. Choose an aspect of the finding to investigate with Amazon Detective. This opens the
   Detective console for that finding or entity.

If the pivot does not behave as expected, see [Troubleshooting the pivot](../../../detective/latest/userguide/profile-pivot-from-service.md#profile-pivot-troubleshooting "../../../detective/latest/userguide/profile-pivot-from-service.md#profile-pivot-troubleshooting") in the _Amazon Detective User
Guide_.

###### Note

If you archive a GuardDuty finding in the Detective console, that finding gets archived in
the GuardDuty console as well.

## Using the integration with a GuardDuty

multi-account environment

If you are managing a multi-account environment in GuardDuty, you must add your member
accounts to Amazon Detective to view Detective data visualizations for findings and
entities in those accounts.

It is recommended that you use the same GuardDuty Administrator account as the
administrator account for Detective. For more information on adding member accounts in Detective,
see [Managing accounts](../../../detective/latest/userguide/accounts.md "../../../detective/latest/userguide/accounts.md") in the
_Amazon Detective User Guide_.

###### Note

Detective is a regional service, meaning you must enable Detective and add your member
accounts in each region in which you want to use the integration.
