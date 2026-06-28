# Create an Amazon EVS environment connector

You can create a connector to enable Amazon EVS to communicate with a VCF management appliance, such as vCenter Server, in your environment.
A connector uses the fully qualified domain name (FQDN) for the appliance and credentials you store in an AWS Secrets Manager secret to authenticate with the appliance.

More info on connectors can be found under [Concepts and components of Amazon EVS](concepts.md#concepts-connector "concepts.md#concepts-connector").

###### Warning

Before creating a connector, we recommend you create a dedicated vCenter user with a ReadOnly role. Avoid using credentials with elevated or administrative permission.

###### Note

Before creating a connector, you must create a secret in AWS Secrets Manager with your appliance credentials.
The secret must contain two keys `username` and `password`.
The values must be the login credentials for the dedicated user you created for the appliance specified in the connector.

###### Important

You must add the tag `EvsAccess=true` to your Secrets Manager secret.
If you encrypted the secret with your own AWS KMS key, then add the `EvsAccess=true` tag to the AWS KMS key as well.

###### Note

Each connector maps to a single appliance FQDN.

###### Note

Only one connector of type vCenter is allowed per environment.

###### Note

The FQDN must be valid, match the domain name used when creating your EVS environment, and be unique across all connectors in the environment.

###### Note

Connector creation does not validate appliance reachability or credentials.
After the connector state is Active, the reachability check status will update from Unknown to Passed or Failed asynchronously within 10 minutes.

**To create an Amazon EVS environment connector**

Follow these steps to create an Amazon EVS connector.

###### Example

Amazon EVS console

1. Go to the [Amazon EVS console](https://console.aws.amazon.com/evs "https://console.aws.amazon.com/evs").
2. In the navigation pane, choose **Environments**.
3. Select the environment where you want to create the connector.
4. Select the **Connectors** tab.
5. Choose **Create connector**.
6. For **Appliance FQDN**, enter the fully qualified domain name of the appliance.
7. For the Secrets Manager dropdown, select the **Secret** containing the appliance credentials.
8. Choose **Create connector**.
9. To verify completion, check that the connector state is Active and the reachability check result is Passed.

AWS CLI

1. Open a new terminal session.
2. Create a new connector.
   See example command below for reference.

   - secret-identifier can be the secret name or ARN

   ```
   aws evs create-environment-connector \
       --environment-id env-abcde12345 \
       --type VCENTER \
       --appliance-fqdn vcenter.example.com \
       --secret-identifier arn:aws:secretsmanager:us-east-2:123456789012:secret:vcenter-creds-AbCdEf
   ```

3. To verify completion, use the **list-environment-connectors** command and check that the connector state is Active and the reachability check result is Passed.

```
aws evs list-environment-connectors \
    --environment-id env-abcde12345
```
