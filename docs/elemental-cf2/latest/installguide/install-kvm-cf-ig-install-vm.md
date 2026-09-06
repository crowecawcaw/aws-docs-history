

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Step B: Deploy the KVM
<a name="install-kvm-cf-ig-install-vm"></a>

Perform these steps from your workstation.

1. Place the OVA file in a convenient location accessible to the VM host.

1. Start the Virtual Machine Manager client and choose **File** > **Create New Virtual Machine**. 

1. In the **New VM** dialog, choose **Import existing disk image** and select **Forward**.

1. Complete the fields as described in the following table and then select **Forward**.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-kvm-cf-ig-install-vm.html)

1. Complete the memory and CPU fields as described in the following table and then select **Forward**.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-kvm-cf-ig-install-vm.html)

1. Complete the installation fields as described in the following table and choose **Finish**.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-kvm-cf-ig-install-vm.html)

   The OVA is installed and the VM is created.

1. Before proceeding, take a snapshot of the VM, as described in the CentOS 7 online help.

1. Repeat these steps to install the OVA on all of the VM instances.