# Configuring synchronization of AWS Config

data using an Aggregator in ServiceNow CMDB

**Prerequisite**: You need to opt-in and
configure the AWS account that contains the aggregated AWS Config resources details
prior to performing the steps below. For more information, see [Configuring AWS Accounts to Synchronize in the Connector.](sn-configure-accounts.md "sn-configure-accounts.md")

###### To configure the Connector to use an Aggregator to synchronize AWS Config data

1. In the AWS Service Management scoped app, choose the **Setup** module.
2. Choose **Aggregators for AWS Config**.
3. Choose **New**.
4. Enter the name of the new Config Aggregator.
5. Choose the Region where you created the new Config Aggregator.
6. Choose the AWS account that should use the new
   Aggregator. Only AWS accounts opted into the Connector
   for ServiceNow that have **Integrate with AWS Config** are viewable.
7. Choose **Submit**.

If you define an Aggregator for an AWS account and
Region, the Aggregator integration becomes the only AWS Config to
ServiceNow CMDB synchronization mechanism for that AWS
account.
The Connector can now synchronize Config data from multiple accounts and Regions
using an Aggregator. You must configure the Config Aggregator in AWS
before using this feature. For more information, see [Setting up an Aggregator](../../../config/latest/developerguide/setup-aggregator-console.md "../../../config/latest/developerguide/setup-aggregator-console.md") in the console.

###### Note

The Config Aggregator view in AWS displays only current config
item resources in AWS Config. Thus, terminated resources are not
available in the Config Aggregator view.

To minimize stale config item records from rendering in the ServiceNow CMDB
from the AWS Config Aggregator, we recommend you remove Config rules
associated to terminated resources. For more information, see [Evaluating Resources with AWS Config Rules](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md")
