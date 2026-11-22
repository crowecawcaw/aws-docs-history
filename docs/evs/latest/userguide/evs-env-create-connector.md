

# Create a connector

Create a connector so that Amazon Elastic VMware Service can communicate with a VMware Cloud Foundation (VCF) management appliance, such as VCF Operations, SDDC Manager, or vCenter Server. You can create a connector with the Amazon EVS console or the AWS CLI. The procedure is the same for every connector type. Only the type, the appliance, and the secret keys differ.

For what each connector type does, see [Manage connectors and credentials](connectors-overview.md).

**Important**  
Use credentials with the minimum permissions that the appliance type requires.

For vCenter Server and VCF Operations, create a dedicated read-only user. For SDDC Manager, scope the API key to the read-only access that Amazon EVS requires. Avoid credentials with elevated or administrative permissions.

## Connector types and secret keys
<a name="evs-env-create-connector-types"></a>

Choose the connector type for your appliance and deployment mode. The secret that you create must contain the keys in the **Required secret keys** column.


| Connector type | VCF version | Required secret keys | Appliance | 
| --- | --- | --- | --- | 
|  `OPERATIONS_MANAGER`  | VCF 9.0 and 9.1 (Self-deployed) |  `username` and `password`  | VCF Operations. This is the required management connector for VCF 9.x. Amazon EVS also uses it to monitor vSAN capacity. | 
|  `SDDC_MANAGER`  | VCF 5.2.x (EVS-deployed) |  `apiKey`  | SDDC Manager. This is the required management connector for VCF 5.2.x. Amazon EVS also uses it to monitor vSAN capacity. | 
|  `VCENTER`  | VCF 5.2.x, 9.0, and 9.1 (both modes) |  `username` and `password`  | vCenter Server. Needed for Windows Server entitlements. | 

## Connector rules
<a name="evs-env-create-connector-rules"></a>

The following rules apply when you create a connector.
+ Each connector maps to a single appliance FQDN. The FQDN must match the domain name that you used when you created the Amazon EVS environment, and it must be unique across all connectors in the environment.
+ You can create only one vCenter connector for each environment.
+ Connector creation is asynchronous and doesn’t validate appliance reachability or credentials. After the connector state reaches `ACTIVE`, the reachability check status changes from `UNKNOWN` to `PASSED` or `FAILED` within 10 minutes.

## Before you begin
<a name="evs-env-create-connector-before"></a>
+ Your VCF management appliance is installed and reachable over your VCF management network.
+ In the appliance, you have created a dedicated user, or for SDDC Manager an API key, with read-only access for Amazon EVS.
+ In AWS Secrets Manager, you have created a secret that contains the keys for your connector type, with the credentials of that user. Create a separate secret for each appliance.
+ You have added the tag `EvsAccess=true` to the secret. If you encrypted the secret with your own AWS KMS key, you have also added the `EvsAccess=true` tag to the AWS KMS key. Without this tag, Amazon EVS can’t access the secret and connector creation fails.
+ For a vCenter connector, you meet the requirements in [Windows Server entitlements](entitlements.md).

## Create the connector
<a name="evs-env-create-connector-procedure"></a>

To create the connector in the Amazon EVS console or with the AWS CLI, use the following steps.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment where you want to create the connector.

1. Choose the **Connectors** tab.

1. Choose **Create connector**.

1. For **Appliance FQDN**, enter the fully qualified domain name of the appliance.

1. For **Secret**, choose the secret that contains the appliance credentials.

1. Choose **Create connector**.

1. To verify, check that the connector state is **Active** and the reachability check result is **Passed**.

1. Run the `create-environment-connector` command. For `--type`, use `OPERATIONS_MANAGER`, `SDDC_MANAGER`, or `VCENTER`. For `--secret-identifier`, use the secret name or ARN.

   The following example creates a vCenter connector. The example ARN uses the `aws` partition. In other partitions, replace `aws` with your partition. Replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws evs create-environment-connector \
       --environment-id env-abcde12345 \
       --type VCENTER \
       --appliance-fqdn vcenter.example.com \
       --secret-identifier arn:aws:secretsmanager:<region-code>:111122223333:secret:vcenter-creds-AbCdEf
   ```

1. To verify, run the `list-environment-connectors` command, and check that the connector state is `ACTIVE` and the reachability check result is `PASSED`.

   ```bash
   aws evs list-environment-connectors \
       --environment-id env-abcde12345
   ```

You have created the connector when its state is `ACTIVE` and its reachability check is `PASSED`. If the required management connector isn’t created or becomes unreachable, Amazon EVS reports impaired environment health through AWS Health notifications.

If connector creation fails or the reachability check stays `FAILED`, see [Troubleshoot environment status checks](troubleshoot-status-checks.md).

## Next steps for a vCenter connector
<a name="create-vcenter-connector"></a>

After the vCenter connector is `ACTIVE` and its reachability check is `PASSED`, you can create Windows Server entitlements for your VMs. For the steps, see [Create Windows Server entitlements](create-entitlements.md).