

# Configure Windows Server Activation
<a name="evs-activate-windows-server"></a>

Amazon EVS provides Windows Server activation for VMs that have Windows Server entitlements. You must create an EVS Windows Server activation VPC endpoint within the VPC you used for your Amazon EVS environment. Each entitled VM must then be configured to connect to this activation endpoint. VPC endpoints can only be created if you have an active Amazon EVS environment.

1. Identify the VPC where the Amazon EVS environment is deployed.

1. In the same VPC, create a VPC Endpoint using the following service name:

    `com.amazonaws.{{region}}.evs-windows-server-activation` 

   For example, create a VPC Endpoint with the following configuration:
   +  **Type**: AWS services
   +  **Service name**: search for and select `com.amazonaws.{{region}}.evs-windows-server-activation` 
   +  **VPC**: Select the VPC your Amazon EVS environment resides in
   +  **Subnets**: Select the subnet(s) from which your Windows VMs establish outbound connections
   +  **Security groups**: Select or create one that allows inbound TCP port `1688` from your Windows instance’s security group or CIDR

1. Note down the private DNS name of the VPC Endpoint you created.

1. Connect to the Windows Server VM and open **PowerShell**.

1. Configure the activation server to use the VPC Endpoint by running the following command:

   ```
   cscript C:\Windows\System32\slmgr.vbs /skms {{VPC_Endpoint_Private_DNS_Name}}:1688
   ```

   The output confirms that the activation server was set successfully.

1. Activate Windows Server by running the following command:

   ```
   cscript C:\Windows\System32\slmgr.vbs /ato
   ```

   The output should include `Product activated successfully.` 

1. Verify that activation completed successfully by running the following command:

   ```
   cscript C:\Windows\System32\slmgr.vbs /dli
   ```

   The output should include:
   +  `Volume activation expiration: 259200 minute(s) (180 day(s))` — or close to it
   +  `Registered KMS machine name: {{VPC_Endpoint_Private_DNS_Name}}:1688` 

## Troubleshooting
<a name="_troubleshooting"></a>

### Activation fails because the VM does not have a GVLK
<a name="_activation_fails_because_the_vm_does_not_have_a_gvlk"></a>

The EVS activation endpoint requires VMs to have a Generic Volume License Key (GVLK) installed to use KMS-based activation. To check whether a GVLK is installed, run the following command:

```
cscript C:\Windows\System32\slmgr.vbs /dlv | findstr /C:"Product Key Channel"
```

If the output does not show `Volume:GVLK`, find the corresponding product key (GVLK) for your version and edition of Windows from [KMS client activation keys](https://learn.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys?tabs=windows1110ltsc%2Cwindows81%2Cserver2025%2Cversion1803#windows-server-ltsc) on the Microsoft website. Install it by running the following command:

```
cscript C:\Windows\System32\slmgr.vbs /ipk {{GVLK}}
```

After installing the GVLK, retry the activation steps starting from the `/ato` command in step 6.

### Activation command returns an error
<a name="_activation_command_returns_an_error"></a>

If `cscript C:\Windows\System32\slmgr.vbs /ato` returns an error, verify that the VM can reach the VPC Endpoint on port 1688:

```
Test-NetConnection -ComputerName {{VPC_Endpoint_Private_DNS_Name}} -Port 1688
```

The output should show `TcpTestSucceeded : True`. For example:

```
ComputerName     : <VPC_Endpoint_Private_DNS_Name>
RemoteAddress    : <VPC_Endpoint_IP_address>
RemotePort       : 1688
InterfaceAlias   : Ethernet 2
SourceAddress    : 10.0.110.93
TcpTestSucceeded : True
```

If `TcpTestSucceeded` is `False`, verify that the VPC Endpoint security group allows inbound TCP port 1688 from the VM’s security group or CIDR.