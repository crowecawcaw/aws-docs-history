

# Create an Amazon EVS environment connector
<a name="evs-env-create-connector"></a>

You can create a connector to enable Amazon EVS to communicate with a VCF management appliance, such as vCenter Server, in your environment. A connector uses the fully qualified domain name (FQDN) for the appliance and credentials you store in an AWS Secrets Manager secret to authenticate with the appliance.

More info on connectors can be found under [Concepts and components of Amazon EVS](concepts.md#concepts-connector).

**Warning**  
Use credentials with the minimum permissions required for the appliance type. For **vCenter** and **Operations Manager**, create a dedicated read-only user. For **SDDC Manager**, scope the API key to the read-only access that Amazon EVS requires. Avoid using credentials with elevated or administrative permissions.

## Prerequisites
<a name="_prerequisites"></a>

Before you create a connector, store the appliance credentials in AWS Secrets Manager and tag the secret so that Amazon EVS can access it. Each connector maps to a single appliance FQDN, so create a separate secret for each appliance.

1. In AWS Secrets Manager, create a secret that contains the keys for your connector type:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/evs/latest/userguide/evs-env-create-connector.html)

   The values must be the login credentials for the dedicated user you created for the appliance specified in the connector.

1. Add the tag `EvsAccess=true` to the Secrets Manager secret. If you encrypted the secret with your own AWS KMS key, also add the `EvsAccess=true` tag to the AWS KMS key.

**Note**  
If the required connector is not created or becomes unreachable, Amazon EVS reports impaired environment health through AWS Health notifications.

**Note**  
Connector creation is asynchronous and does not validate appliance reachability or credentials. After the connector state reaches `ACTIVE`, the reachability check status updates from `UNKNOWN` to `PASSED` or `FAILED` within 10 minutes.

 **To create an Amazon EVS environment connector** 

Follow these steps to create an Amazon EVS connector.

**Example**  

1. Go to the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment where you want to create the connector.

1. Select the **Connectors** tab.

1. Choose **Create connector**.

1. For **Appliance FQDN**, enter the fully qualified domain name of the appliance.

1. For the Secrets Manager dropdown, select the **Secret** containing the appliance credentials.

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