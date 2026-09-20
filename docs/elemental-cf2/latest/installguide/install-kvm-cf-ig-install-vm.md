

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Step B: Deploy the KVM
<a name="install-kvm-cf-ig-install-vm"></a>

Perform these steps from your workstation.

1. Place the OVA file in a convenient location accessible to the VM host.

1. Start the Virtual Machine Manager client and choose **File** > **Create New Virtual Machine**. 

1. In the **New VM** dialog, choose **Import existing disk image** and select **Forward**.

1. Complete the fields as described in the following table and then select **Forward**.



<table>
<thead>
  <tr><th>Screen and Field</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td><b>Provide the existing storage path</b></td><td>Select the location where the OVA image file is located.</td></tr>
  <tr><td><b>OS type</b></td><td>Select <b>Linux</b>.</td></tr>
  <tr><td><b>Version</b></td><td>Select <b>CentOS 6.5</b>.</td></tr>
</tbody>
</table>


1. Complete the memory and CPU fields as described in the following table and then select **Forward**.



<table>
<thead>
  <tr><th>Screen and Field</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td><b>Memory (RAM)</b></td><td>Choose a minimum of 15259 MiB (16GB). If your physical system has additional RAM available, choose more for improved performance. If you oversubscribe your memory for your virtual machine and there isn't enough for the host, then you might see performance degradation in the AWS Elemental Conductor File software. </td></tr>
  <tr><td><b>CPUs</b></td><td>Choose <b>24</b>. Ensure that the number of cores you select matches your AWS Elemental licensing. To check the cores available with your license, see the <b>Activations</b> information at <a href="https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations">AWS Elemental Support Center Activations</a>. </td></tr>
</tbody>
</table>


1. Complete the installation fields as described in the following table and choose **Finish**.



<table>
<thead>
  <tr><th>Screen and Field</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td><b>Name</b></td><td>Type a descriptive name for the VM. This will be the hostname that you use to access AWS Elemental Conductor File.</td></tr>
  <tr><td><b>Network selection</b></td><td>Use this section to configure your system according to your network setup.</td></tr>
</tbody>
</table>


   The OVA is installed and the VM is created.

1. Before proceeding, take a snapshot of the VM, as described in the CentOS 7 online help.

1. Repeat these steps to install the OVA on all of the VM instances.