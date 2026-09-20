

# Creating a vCenter connector
<a name="create-vcenter-connector"></a>

To set up Windows Server entitlements for your virtual machines (VMs), you first create a vCenter connector. With this connector, Amazon EVS can communicate with vCenter Server in your environment. It uses the fully qualified domain name (FQDN) and credentials that you store in an AWS Secrets Manager secret to authenticate with the appliance.

Before you create a connector, make sure that you meet the requirements in [Prerequisites for Windows Server entitlements](entitlements-prerequisites.md).

Note the following connector constraints:
+ Each connector maps to a single appliance FQDN, and only one vCenter connector is allowed per environment. The FQDN must match the domain name that you used when you created your Amazon EVS environment, and it must be unique across all connectors in the environment.
+ Connector creation does not validate appliance reachability or credentials. After the connector shows as Active, EVS runs a reachability check every 10 minutes and updates the connector’s status to Passed, Failed, or Unknown.

 **To create an Amazon EVS environment connector** 

**Example**  

1. Go to the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment where you want to create the connector.

1. Select the **Connectors** tab.

1. Choose **Create connector**.

1. For **Appliance FQDN**, enter the fully qualified domain name of the appliance.

1. For the Secret Manager dropdown, select the **Secret** containing the appliance credentials.

1. Choose **Create connector**.

1. To verify completion, check that the connector state is Active and the reachability check result is Passed.

1. Open a new terminal session.

1. Create a new connector. See example command below for reference.
   + secret-identifier can be the secret name or ARN

     ```
     aws evs create-environment-connector \
         --environment-id env-abcde12345 \
         --type VCENTER \
         --appliance-fqdn vcenter.example.com \
         --secret-identifier arn:aws:secretsmanager:us-east-2:123456789012:secret:vcenter-creds-AbCdEf
     ```

1. To verify completion, use the **list-environment-connectors** command and check that the connector state is Active and the reachability check result is Passed.

   ```
   aws evs list-environment-connectors \
       --environment-id env-abcde12345
   ```

After the connector is Active and the reachability check has Passed, you can create entitlements for your Windows VMs. See [Creating Windows Server entitlements for your VMs](create-entitlements.md).