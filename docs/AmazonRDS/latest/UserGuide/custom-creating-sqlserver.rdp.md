

# Connecting to your RDS Custom DB instance using RDP
<a name="custom-creating-sqlserver.rdp"></a>

After you create your RDS Custom DB instance, you can connect to this instance using an RDP client. The procedure is the same as for connecting to an Amazon EC2 instance. For more information, see [Connect to your Windows instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.html).

To connect to the DB instance, you need the key pair associated with the instance. RDS Custom creates the key pair for you. The pair name uses the prefix `do-not-delete-rds-custom-{{DBInstanceIdentifier}}`. AWS Secrets Manager stores your private key as a secret.

Complete the task in the following steps:

1. [Configure your DB instance to allow RDP connections](#custom-creating-sqlserver.rdp.port).

1. [Retrieve your secret key](#custom-creating-sqlserver.rdp.key).

1. [Connect to your EC2 instance using the RDP utility](#custom-creating-sqlserver.rdp.connect).

## Configure your DB instance to allow RDP connections
<a name="custom-creating-sqlserver.rdp.port"></a>

To allow RDP connections, configure your VPC security group and set a firewall rule on the host.

### Configure your VPC security group
<a name="custom-creating-sqlserver.rdp.port.vpc"></a>

Make sure that the VPC security group associated with your DB instance permits inbound connections on port 3389 for Transmission Control Protocol (TCP). To learn how to configure your VPC security group, see [Configure your VPC security group](custom-setup-sqlserver.md#custom-setup-sqlserver.vpc.sg).

### Set the firewall rule on the host
<a name="custom-creating-sqlserver.rdp.port.firewall"></a>

To permit inbound connections on port 3389 for TCP, set a firewall rule on the host. The following examples show how to do this.

We recommend that you use the specific `-Profile` value: `Public`, `Private`, or `Domain`. Using `Any` refers to all three values. You can also specify a combination of values separated by a comma. For more information about setting firewall rules, see [Set-NetFirewallRule](https://docs.microsoft.com/en-us/powershell/module/netsecurity/set-netfirewallrule?view=windowsserver2019-ps) in the Microsoft documentation.

**To use Systems Manager Session Manager to set a firewall rule**

1. Connect to Session Manager as shown in [Connecting to your RDS Custom DB instance using AWS Systems Manager](custom-creating-sqlserver.ssm.md).

1. Run the following command.

   ```
   Set-NetFirewallRule -DisplayName "Remote Desktop - User Mode (TCP-In)" -Direction Inbound -LocalAddress Any -Profile {{Any}}
   ```

**To use Systems Manager CLI commands to set a firewall rule**

1. Use the following command to open RDP on the host.

   ```
   OPEN_RDP_COMMAND_ID=$(aws ssm send-command --region $AWS_REGION \
       --instance-ids $RDS_CUSTOM_INSTANCE_EC2_ID \
       --document-name "AWS-RunPowerShellScript" \
       --parameters '{"commands":["Set-NetFirewallRule -DisplayName \"Remote Desktop - User Mode (TCP-In)\" -Direction Inbound -LocalAddress Any -Profile {{Any}}"]}' \
       --comment "Open RDP port" | jq -r ".Command.CommandId")
   ```

1. Use the command ID returned in the output to get the status of the previous command. To use the following query to return the command ID, make sure that you have the jq plug-in installed.

   ```
   aws ssm list-commands \
       --region $AWS_REGION \
       --command-id $OPEN_RDP_COMMAND_ID
   ```

## Retrieve your secret key
<a name="custom-creating-sqlserver.rdp.key"></a>

Retrieve your secret key using either AWS Management Console or the AWS CLI.

### Console
<a name="custom-creating-sqlserver.rdp.key.CON"></a>

**To retrieve the secret key**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the RDS Custom DB instance to which you want to connect.

1. Choose the **Configuration** tab.

1. Note the **DB instance ID** for your DB instance, for example, `{{my-custom-instance}}`.

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Look for the name of your EC2 instance, and then choose the instance ID associated with it.

   In this example, the instance ID is `i-abcdefghijklm01234`.

1. In **Details**, find **Key pair name**. The pair name includes the DB identifier. In this example, the pair name is `do-not-delete-rds-custom-{{my-custom-instance}}-{{0d726c}}`.

1. In the instance summary, find **Public IPv4 DNS**. For the example, the public DNS might be `ec2-12-345-678-901.us-east-2.compute.amazonaws.com`.

1. Open the AWS Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose the secret that has the same name as your key pair.

1. Choose **Retrieve secret value**.

### AWS CLI
<a name="custom-creating-sqlserver.rdp.key.CLI"></a>

**To retrieve the private key**

1. Get the list of your RDS Custom DB instances by calling the `aws rds describe-db-instances` command.

   ```
   aws rds describe-db-instances \
       --query 'DBInstances[*].[DBInstanceIdentifier,DbiResourceId]' \
       --output text
   ```

1. Choose the DB instance identifier from the sample output, for example `do-not-delete-rds-custom-{{my-custom-instance}}`.

1. Find the EC2 instance ID of your DB instance by calling the `aws ec2 describe-instances` command. The following example uses the EC2 instance name to describe the DB instance.

   ```
   aws ec2 describe-instances \
       --filters "Name=tag:Name,Values=do-not-delete-rds-custom-{{my-custom-instance}}" \
       --output text \
       --query 'Reservations[*].Instances[*].InstanceId'
   ```

   The following sample output shows the EC2 instance ID.

   ```
   i-abcdefghijklm01234
   ```

1. Find the key name by specifying the EC2 instance ID, as shown in the following example.

   ```
   aws ec2 describe-instances \
       --instance-ids {{i-abcdefghijklm01234}} \
       --output text \
       --query 'Reservations[*].Instances[*].KeyName'
   ```

   The following sample output shows the key name, which uses the prefix `do-not-delete-rds-custom-{{DBInstanceIdentifier}}`.

   ```
   do-not-delete-rds-custom-{{my-custom-instance}}-{{0d726c}}
   ```

## Connect to your EC2 instance using the RDP utility
<a name="custom-creating-sqlserver.rdp.connect"></a>

Follow the procedure in [Connect to your Windows instance using RDP](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.html#connect-rdp) in the *Amazon EC2 User Guide*. This procedure assumes that you created a .pem file that contains your private key.