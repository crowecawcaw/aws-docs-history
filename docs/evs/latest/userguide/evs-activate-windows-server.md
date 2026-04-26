# Configure Windows Server Activation

Amazon EVS provides Windows Server activation for VMs that have Windows Server entitlements. You must create an EVS Windows Server activation VPC endpoint within the VPC you used for your Amazon EVS environment. Each entitled VM must then be configured to connect to this activation endpoint. VPC endpoints can only be created if you have an active Amazon EVS environment.

1. Identify the VPC where the Amazon EVS environment is deployed.
2. In the same VPC, create a VPC Endpoint using the following service name:

`com.amazonaws.*<region>*.evs-windows-server-activation`

For example, create a VPC Endpoint with the following configuration:

    * **Type**: AWS services
    * **Service name**: search for and select `com.amazonaws.*<region>*.evs-windows-server-activation`
    * **VPC**: Select the VPC your Amazon EVS environment resides in
    * **Subnets**: Select the subnet(s) from which your Windows VMs establish outbound connections
    * **Security groups**: Select or create one that allows inbound TCP port `1688` from your Windows instance’s security group/CIDR

3. Note down the private DNS name of the VPC Endpoint you created.
4. Connect to the Windows Server VM and open **PowerShell**.
5. Configure the activation server to use the VPC Endpoint by using the command:

```
slmgr /skms <VPC Endpoint Private DNS Name>:1688
```

You will get a dialog confirming the activation server was set. 6. Activate Windows Server by using the command:

```
slmgr /ato
```

You should get a dialog saying "**Product activated successfully.**" 7. Verify that activation completed successfully using the command:

```
slmgr /dli
```

Look for License Status: **Licensed**.
