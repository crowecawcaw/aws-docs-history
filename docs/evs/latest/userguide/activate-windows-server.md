

# Activate Windows Server on entitled VMs

Amazon Elastic VMware Service provides Windows Server activation for VMs that have Windows Server entitlements. You create an Amazon EVS Windows Server activation VPC endpoint in the VPC of your environment, and then configure each entitled VM to activate against it.

## Before you begin
<a name="activate-windows-server-prereqs"></a>
+ You have an active Amazon EVS environment. You can create the VPC endpoint only when the environment is active.
+ You have created Windows Server entitlements for the VMs. For instructions, see [Create Windows Server entitlements](create-entitlements.md).
+ You can connect to each Windows Server VM and open PowerShell.

## Step 1. Create the activation VPC endpoint
<a name="activate-windows-server-endpoint"></a>

1. Identify the VPC where the Amazon EVS environment is deployed.

1. In the same VPC, create a VPC endpoint with the following settings:

   1. For **Type**, choose ** AWS services**.

   1. For **Service name**, search for and select `com.amazonaws.<region-code>.evs-windows-server-activation`. Replace `<region-code>` with the Region where you created the environment.

   1. For **VPC**, choose the VPC of your Amazon EVS environment.

   1. For **Subnets**, choose the subnets from which your Windows VMs make outbound connections.

   1. For **Security groups**, choose a security group that allows inbound TCP port `1688` from the security group or CIDR of your Windows VMs.

1. Note the private DNS name of the VPC endpoint.

## Step 2. Check that the VM has a GVLK
<a name="activate-windows-server-gvlk"></a>

The Amazon EVS activation endpoint uses Microsoft Key Management Service (KMS) activation. This KMS is a Windows licensing service and is separate from AWS Key Management Service (AWS KMS). Each VM must have a Generic Volume License Key (GVLK) installed.

1. Connect to the Windows Server VM and open **PowerShell**.

1. Run the following command.

   ```powershell
   cscript C:\Windows\System32\slmgr.vbs /dlv | findstr /C:"Product Key Channel"
   ```

1. If the output does not show `Volume:GVLK`, find the GVLK for your version and edition of Windows Server in [KMS client activation keys](https://learn.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys?tabs=windows1110ltsc%2Cwindows81%2Cserver2025%2Cversion1803#windows-server-ltsc) on the Microsoft website. Then install it. In the following command, replace `<gvlk>` with the GVLK.

   ```powershell
   cscript C:\Windows\System32\slmgr.vbs /ipk <gvlk>
   ```

## Step 3. Activate Windows Server
<a name="activate-windows-server-activate"></a>

1. On the VM, in **PowerShell**, set the activation server to the VPC endpoint. In the following command, replace `<vpc-endpoint-private-dns-name>` with the private DNS name of the VPC endpoint.

   ```powershell
   cscript C:\Windows\System32\slmgr.vbs /skms <vpc-endpoint-private-dns-name>:1688
   ```

   The output confirms that the activation server was set.

1. Activate Windows Server.

   ```powershell
   cscript C:\Windows\System32\slmgr.vbs /ato
   ```

   The output includes `Product activated successfully.` 

1. Verify the activation.

   ```powershell
   cscript C:\Windows\System32\slmgr.vbs /dli
   ```

   The output includes these values:
   +  `Volume activation expiration: 259200 minute(s) (180 day(s))` or a value close to it
   +  `Registered KMS machine name: <vpc-endpoint-private-dns-name>:1688` 

1. Repeat these steps on each entitled VM.

You have activated Windows Server on your entitled VMs.

## Next steps
<a name="activate-windows-server-next"></a>

The following pages cover tasks that you might do after activation.
+ To fix entitlement status issues, see [Troubleshoot Windows Server entitlements](troubleshoot-entitlements.md).
+ To stop using Windows Server licensing from AWS for a VM, see [Delete Windows Server entitlements](delete-entitlements.md).

## If the activation command returns an error
<a name="activate-windows-server-errors"></a>

If `cscript C:\Windows\System32\slmgr.vbs /ato` returns an error, first make sure that the VM has a GVLK ([Step 2](#activate-windows-server-gvlk)). Then check that the VM can reach the VPC endpoint on port 1688.

In the following command, replace `<vpc-endpoint-private-dns-name>` with the private DNS name of the VPC endpoint.

```powershell
Test-NetConnection -ComputerName <vpc-endpoint-private-dns-name> -Port 1688
```

The output shows `TcpTestSucceeded : True` when the connection works. The following is example output.

```text
ComputerName     : <vpc-endpoint-private-dns-name>
RemoteAddress    : <vpc-endpoint-ip-address>
RemotePort       : 1688
InterfaceAlias   : Ethernet 2
SourceAddress    : 10.0.110.93
TcpTestSucceeded : True
```

If `TcpTestSucceeded` is `False`, make sure that the security group of the VPC endpoint allows inbound TCP port 1688 from the security group or CIDR of the VM. For entitlement status issues, see [Troubleshoot Windows Server entitlements](troubleshoot-entitlements.md).