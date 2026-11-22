

# Delete a connector

Delete a connector when you no longer need it. You can delete a connector with the Amazon Elastic VMware Service console or the AWS CLI.

**Important**  
The management connector of your environment is the SDDC Manager connector for VMware Cloud Foundation (VCF) 5.2.x or the VCF Operations connector for VCF 9.x. If you delete the management connector, Amazon EVS reports impaired environment health through AWS Health notifications. If you delete the SDDC Manager connector (VCF 5.2.x), Amazon EVS also can’t validate host counts and license key coverage.

## Before you begin
<a name="_before_you_begin"></a>

Before you delete a connector, check the following requirements.
+ The connector must be in the `ACTIVE`, `CREATE_FAILED`, or `UPDATE_FAILED` state.
+ You must delete all entitlements that are associated with a vCenter connector before you can delete the connector. For the steps, see [Delete Windows Server entitlements](delete-entitlements.md).

## Delete the connector
<a name="evs-env-delete-connector-procedure"></a>

To delete the connector in the Amazon EVS console or with the AWS CLI, use the following steps.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment that contains the connector.

1. Choose the **Connectors** tab.

1. Select the connector that you want to delete.

1. Choose **Delete Connector**.

1. Confirm the deletion.

1. To verify, check that the connector no longer appears in the list.

1. Run the `delete-environment-connector` command.

   ```bash
   aws evs delete-environment-connector \
       --environment-id env-abcde12345 \
       --connector-id cnctr-abcde12345
   ```

1. To verify, run the `list-environment-connectors` command, and check that the connector is no longer listed.

   ```bash
   aws evs list-environment-connectors \
       --environment-id env-abcde12345
   ```

You have deleted the connector when it no longer appears in the list.

To create a connector again, see [Create a connector](evs-env-create-connector.md).