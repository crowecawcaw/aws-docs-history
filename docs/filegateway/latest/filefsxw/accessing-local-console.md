Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Accessing the gateway local console

How you access your VM's local console depends on the type of the Hypervisor you deployed
your gateway VM on. In this section, you can find information on how to access the VM local
console using Linux Kernel-based Virtual Machine (KVM), VMware ESXi, and Microsoft Hyper-V
Manager.

###### Topics

- [Accessing the Gateway Local Console
  with Linux KVM](#MaintenanceConsoleWindowKVM-common "#MaintenanceConsoleWindowKVM-common")
- [Accessing the Gateway Local
  Console with VMware ESXi](#MaintenanceConsoleWindowVMware-common "#MaintenanceConsoleWindowVMware-common")
- [Access the Gateway Local Console
  with Microsoft Hyper-V](#MaintenanceConsoleWindowHyperV-common "#MaintenanceConsoleWindowHyperV-common")

## Accessing the Gateway Local Console

with Linux KVM

There are different ways to configure virtual machines running on KVM, depending on
the Linux distribution being used. Instructions for accessing KVM configuration options
from the command line follow. Instructions might differ depending on your KVM
implementation.

###### To access your gateway's local console with KVM

1. Use the following command to list the VMs that are currently available in KVM.

```
# virsh list
```

The command returns a list of VMs with **Id**,
**Name**, and **State** information for
each. Note the `Id` of the VM for which you want to launch the
gateway local console. 2. Use the following command to access the local console.

```
# virsh console `Id`
```

Replace `Id` with the **Id** of the
VM you noted in the previous step.

The AWS Appliance gateway local console prompts you to login to change your
network configuration and other settings. 3. Enter your username and password to log into the gateway local console. For
more information, see [Logging in to the File Gateway local console](manage-on-premises-fgw.md#LocalConsole-login-fgw "manage-on-premises-fgw.md#LocalConsole-login-fgw") .

After you log in, the **AWS Appliance Activation -
Configuration** menu appears. You can select from the menu options
to perform gateway configuration tasks. For more information, see [Performing
tasks on the virtual machine local console](manage-on-premises-fgw.md "manage-on-premises-fgw.md") .

## Accessing the Gateway Local

Console with VMware ESXi

###### To access your gateway's local console with VMware ESXi

1. In the VMware vSphere client, select your gateway VM.
2. Make sure that the gateway VM is turned on.

###### Note

If your gateway VM is turned on, a green arrow icon appears with the VM
icon in the VM browser panel on the left side of the application window. If
your gateway VM is not turned on, you can turn it on by choosing the green
**Power On** icon on the **Toolbar**
at the top of the application window. 3. Choose the **Console** tab in the main information panel on
the right side of the application window.

After a few moments, the AWS Appliance gateway local console prompts you to
login to change your network configuration and other settings.

###### Note

To release the cursor from the console window, press
**Ctrl+Alt**. 4. Enter your username and password to log into the gateway local console. For
more information, see [Logging in to the File Gateway local console](manage-on-premises-fgw.md#LocalConsole-login-fgw "manage-on-premises-fgw.md#LocalConsole-login-fgw") .

After you log in, the **AWS Appliance Activation -
Configuration** menu appears. You can select from the menu options
to perform gateway configuration tasks. For more information, see [Performing
tasks on the virtual machine local console](manage-on-premises-fgw.md "manage-on-premises-fgw.md") .

## Access the Gateway Local Console

with Microsoft Hyper-V

###### To access your gateway's local console (Microsoft Hyper-V)

1. Select your gateway appliance VM from the **Virtual
   Machines** panel on the left side of the Microsoft Hyper-V Manager
   application window.
2. Make sure that the gateway is turned on.

###### Note

If your gateway VM is turned on, `Running` is displayed in the
**State** column for the VM in the **Virtual
Machines** panel on the left side of the application window. If
your gateway VM is not turned on, you can turn it on by choosing
**Start** in the **Actions** panel on
the right side of the application window. 3. Choose **Connect** from the **Actions**
panel.

The **Virtual Machine Connection** window appears. If an
authentication window appears, type the sign-in credentials provided to you by
the hypervisor administrator.

After a few moments, the AWS Appliance gateway local console prompts you to
login to change your network configuration and other settings. 4. Enter your username and password to log into the gateway local console. For
more information, see [Logging in to the File Gateway local console](manage-on-premises-fgw.md#LocalConsole-login-fgw "manage-on-premises-fgw.md#LocalConsole-login-fgw") .

After you log in, the **AWS Appliance Activation -
Configuration** menu appears. You can select from the menu options
to perform gateway configuration tasks. For more information, see [Performing
tasks on the virtual machine local console](manage-on-premises-fgw.md "manage-on-premises-fgw.md") .
