

# Update an Amazon EVS environment connector
<a name="evs-env-update-connector"></a>

You can update an existing connector to change the appliance FQDN or point to a different Secrets Manager secret for authentication. For example, you may need to update the FQDN if the appliance endpoint changes, or switch to a different secret. You can also update the values of the existing Secrets Manager secret directly when rotating vCenter credentials, so that no connector update is required.

More info on connectors can be found under [Concepts and components of Amazon EVS](concepts.md#concepts-connector).

**Note**  
Only one property of a connector can be updated at a time.

**Note**  
The connector must be in an Active or Update Failed state to be updated.

**Note**  
If updating the FQDN, the new FQDN must be valid, match the domain name used when creating your EVS environment, and be unique across all connectors in the environment.

 **To update an Amazon EVS environment connector** 

Follow these steps to update an Amazon EVS connector.

**Example**  

1. Go to the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment containing the connector.

1. Select the **Connectors** tab.

1. Select the connector you want to update.

1. Choose **Actions**, and then in the dropdown, select **Update Secret** or **Update FQDN**.

1. For **Update Secret**:

   1. In the secret dropdown, select the secret with the appliance credentials and choose **Update**.

1. For **Update FQDN**:

   1. Enter the new FQDN and choose **Update**.

1. To verify completion, check that the **connector state** has returned to Active from Updating.

1. Open a new terminal session.

1. Update the connector secret or FQDN. See example commands below for reference.

   To update the secret:

   ```
   aws evs update-environment-connector \
       --environment-id env-abcde12345 \
       --connector-id cnctr-szgj87q6gi \
       --secret-identifier arn:aws:secretsmanager:us-east-2:123456789012:secret:vcenter-creds-AbCdEf
   ```

   To update the FQDN:

   ```
   aws evs update-environment-connector \
       --environment-id env-abcde12345 \
       --connector-id cnctr-szgj87q6gi \
       --appliance-fqdn vcf.evs.dev
   ```

1. To verify completion, use the **list-environment-connectors** command and check that the connector state is Active.

   ```
   aws evs list-environment-connectors \
       --environment-id env-abcde12345
   ```