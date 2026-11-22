

# Step 6: Create connectors

A connector is an Amazon Elastic VMware Service sub-resource that represents a persistent connection from Amazon EVS to a specific VMware Cloud Foundation (VCF) management appliance. Amazon EVS uses connectors to monitor your deployment. Create them after VCF is installed and its management appliances are reachable over your VCF management network. You can create connectors with the Amazon EVS console or the AWS CLI. For more information, see [Manage connectors and credentials](connectors-overview.md).

## Why the Operations Manager connector matters
<a name="self-deployed-connector-why"></a>

VCF 9.x requires an Operations Manager (`OPERATIONS_MANAGER`) connector. Amazon EVS uses this connector to connect to and stay in sync with your VMware deployment, and to monitor vSAN capacity. If the required connector isn’t created or becomes unreachable, Amazon EVS reports impaired environment health through AWS Health notifications.

You can also create a vCenter (`VCENTER`) connector. Amazon EVS uses it to monitor VM lifecycle events for entitled VMs. For the connector types and their required secret keys, see [Create a connector](evs-env-create-connector.md).

## Store the appliance credentials
<a name="self-deployed-connector-secret"></a>

**Important**  
Before you create a connector, store the credentials for the target VCF management appliance in AWS Secrets Manager. Tag the secret with `EvsAccess=true`. If you encrypted the secret with your own AWS KMS key, also tag the key with `EvsAccess=true`. Without this tag, Amazon EVS can’t access the secret and connector creation fails.

To store the credentials, do the following.

1. In the VCF management appliance, create a dedicated read-only user for Amazon EVS. For Operations Manager and vCenter, use credentials with the minimum permissions that the appliance type requires. Don’t use credentials with elevated or administrative permissions.

1. In AWS Secrets Manager, create a secret with the keys `username` and `password` that contain the credentials of that user. Each connector maps to a single appliance FQDN, so create a separate secret for each appliance.

1. Add the tag `EvsAccess=true` to the secret, and to the AWS KMS key if you use your own key.

## Create the Operations Manager connector
<a name="self-deployed-connector-create"></a>

To create the connector in the Amazon EVS console or with the AWS CLI, use the following steps.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select your environment.

1. Select the **Connectors** tab.

1. Choose **Create connector**.

1. For **Appliance FQDN**, enter the fully qualified domain name of the VCF Operations appliance.

1. For the Secrets Manager dropdown, select the **Secret** that contains the appliance credentials.

1. Choose **Create connector**.

1. Run the `aws evs create-environment-connector` command. The secret identifier can be the secret name or ARN. Replace `<environment-id>` with the ID of your environment. Replace the example FQDN and secret name with your own values.

   ```bash
   aws evs create-environment-connector \
       --environment-id <environment-id> \
       --type OPERATIONS_MANAGER \
       --appliance-fqdn vcfops.evs.example.com \
       --secret-identifier vcfops-credentials
   ```

1. List the connectors of the environment.

   ```bash
   aws evs list-environment-connectors \
       --environment-id <environment-id>
   ```

Connector creation is asynchronous and doesn’t validate appliance reachability or credentials. After the connector state reaches `ACTIVE`, the reachability check status changes from `UNKNOWN` to `PASSED` or `FAILED` within 10 minutes. You have created the connector when its state is `ACTIVE` and its reachability check is `PASSED`.

To create a vCenter connector, repeat these steps with the vCenter Server FQDN, its secret, and the `VCENTER` type.

If connector creation fails or the reachability check stays `FAILED`, see [Troubleshoot Self-deployed deployments](troubleshoot-self-deployed.md).

Next step: [Step 7: Verify the environment](self-deployed-verify.md).