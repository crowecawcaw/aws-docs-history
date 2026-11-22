

# Update a connector

Update a connector to change the appliance fully qualified domain name (FQDN) or to point the connector to a different AWS Secrets Manager secret. For example, you update the FQDN when the appliance endpoint changes. You can update a connector of any type with the Amazon Elastic VMware Service console or the AWS CLI.

If you only changed the credentials in the existing secret, you don’t need to update the connector, because the connector already points to that secret. For credential rotation, see [Rotate vCenter connector credentials](rotate-vcenter-credentials.md).

## Update rules
<a name="evs-env-update-connector-rules"></a>

The following rules apply when you update a connector.
+ You can update only one property of a connector at a time.
+ The connector must be in the `ACTIVE` or `UPDATE_FAILED` state. If the connector is in the `CREATING` or `UPDATING` state, wait for it to reach the `ACTIVE` state before you update it.
+ A new FQDN must be valid and must match the domain name that you used when you created the Amazon EVS environment. It must also be unique across all connectors in the environment.
+ A new secret must contain the keys for the connector type and carry the `EvsAccess=true` tag. For the keys, see [Connector types and secret keys](evs-env-create-connector.md#evs-env-create-connector-types).

## Update the connector
<a name="evs-env-update-connector-procedure"></a>

To update the connector in the Amazon EVS console or with the AWS CLI, use the following steps.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment that contains the connector.

1. Choose the **Connectors** tab.

1. Select the connector that you want to update.

1. Choose **Actions**, and then choose **Update Secret** or **Update FQDN**.

1. Do one of the following:

   1. For **Update Secret**, select the secret with the appliance credentials, and choose **Update**.

   1. For **Update FQDN**, enter the new FQDN, and choose **Update**.

1. To verify, check that the connector state has returned to **Active** from **Updating**.

1. Run the `update-environment-connector` command with either `--secret-identifier` or `--appliance-fqdn`.

   The example ARN uses the `aws` partition. In other partitions, replace `aws` with your partition. Replace `<region-code>` with the Region where you created the environment.

   To update the secret:

   ```bash
   aws evs update-environment-connector \
       --environment-id env-abcde12345 \
       --connector-id cnctr-abcde12345 \
       --secret-identifier arn:aws:secretsmanager:<region-code>:111122223333:secret:vcenter-creds-AbCdEf
   ```

   To update the FQDN:

   ```bash
   aws evs update-environment-connector \
       --environment-id env-abcde12345 \
       --connector-id cnctr-abcde12345 \
       --appliance-fqdn vcenter.example.com
   ```

1. To verify, run the `list-environment-connectors` command, and check that the connector state is `ACTIVE`.

   ```bash
   aws evs list-environment-connectors \
       --environment-id env-abcde12345
   ```

You have updated the connector when its state is `ACTIVE` again. After the update, check that the reachability check result is `PASSED`. If the update fails or the reachability check stays `FAILED`, see [Troubleshoot environment status checks](troubleshoot-status-checks.md).