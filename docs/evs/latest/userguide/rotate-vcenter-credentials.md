

# Rotating vCenter connector credentials
<a name="rotate-vcenter-credentials"></a>

When you create a vCenter connector, Amazon EVS authenticates with your vCenter Server by using the vCenter user credentials that you store in an AWS Secrets Manager secret. If you rotate the credentials for that vCenter user in VCF, you must make the new credentials available to the connector so that it can continue to authenticate with the appliance.

You have two options to provide the rotated credentials:
+ Update the values in the existing Secrets Manager secret with the new credentials. Because the connector already points to this secret, no connector update is required.
+ Update the connector to point to a different Secrets Manager secret that contains the new credentials.

Note the following constraints:
+ Only one property of a connector can be updated at a time.
+ The connector must be in an Active or Update Failed state to be updated. If the connector is in a Creating or Updating state, wait until it reaches an Active or Update Failed state before you attempt the update.

If you chose to store the rotated credentials in a different secret, follow these steps to update the connector to point to that secret.

**Example**  

1. Go to the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment containing the connector.

1. Select the **Connectors** tab.

1. Select the connector you want to update.

1. Choose **Actions**, and then in the dropdown, select **Update Secret**.

1. In the secret dropdown, select the secret with the appliance credentials and choose **Update**.

1. To verify completion, check that the **connector state** has returned to Active from Updating.

1. Open a new terminal session.

1. Update the connector secret. See example command below for reference.

   ```
   aws evs update-environment-connector \
       --environment-id env-abcde12345 \
       --connector-id cnctr-szgj87q6gi \
       --secret-identifier arn:aws:secretsmanager:us-east-2:123456789012:secret:vcenter-creds-AbCdEf
   ```

1. To verify completion, use the **list-environment-connectors** command and check that the connector state is Active.

   ```
   aws evs list-environment-connectors \
       --environment-id env-abcde12345
   ```