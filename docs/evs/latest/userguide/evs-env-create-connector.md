# Create an Amazon EVS environment connector

You can create a connector to enable Amazon EVS to communicate with a VCF management appliance, such as vCenter Server, in your environment.
A connector uses the fully qualified domain name (FQDN) for the appliance and credentials you store in an AWS Secrets Manager secret to authenticate with the appliance.

More info on connectors can be found under [Concepts and components of Amazon EVS](concepts.md#concepts-connector "concepts.md#concepts-connector").

###### Warning

Use credentials with the minimum permissions required for the appliance type. For **vCenter** and **Operations Manager**, create a dedicated read-only user. For **SDDC Manager**, scope the API key to the read-only access that Amazon EVS requires. Avoid using credentials with elevated or administrative permissions.

## Prerequisites

Before you create a connector, store the appliance credentials in AWS Secrets Manager and tag the secret so that Amazon EVS can access it. Each connector maps to a single appliance FQDN, so create a separate secret for each appliance.

1. In AWS Secrets Manager, create a secret that contains the keys for your connector type:

| Connector type       | VCF version         | Required secret keys      | Description                                                                                                                                                               |
| -------------------- | ------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `VCENTER`            | 5.2.x, 9.0.x, 9.1.x | `username` and `password` | Monitors VM lifecycle events for entitled VMs.                                                                                                                            |
| `OPERATIONS_MANAGER` | 9.0.x, 9.1.x        | `username` and `password` | VCF 9.0.x and 9.1.x appliance that Amazon EVS uses to connect to and stay in sync with your VMware deployment. Replaces the license-management functions of SDDC Manager. |
| `SDDC_MANAGER`       | 5.2.x               | `apiKey`                  | VCF 5.2.x appliance that Amazon EVS uses to validate host counts and license-key coverage.                                                                                |

The values must be the login credentials for the dedicated user you created for the appliance specified in the connector. 2. Add the tag `EvsAccess=true` to the Secrets Manager secret. If you encrypted the secret with your own AWS KMS key, also add the `EvsAccess=true` tag to the AWS KMS key.

###### Note

If the required connector is not created or becomes unreachable, Amazon EVS reports impaired environment health through AWS Health notifications.

###### Note

Connector creation is asynchronous and does not validate appliance reachability or credentials. After the connector state reaches `ACTIVE`, the reachability check status updates from `UNKNOWN` to `PASSED` or `FAILED` within 10 minutes.

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
