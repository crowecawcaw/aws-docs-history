

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Step D: Deploy the VM and Install AWS Elemental Server
<a name="install-vm-p-cf-ig-install-vm-w"></a>

After you've installed the AWS Elemental Conductor File nodes, perform these steps on each individual blade that you're adding to the cluster in order to deploy a VM and install the AWS Elemental Server worker software.

1. Start the VMware vSphere client and choose the option that lets you run the OVF Deploy wizard.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-vm-p-cf-ig-install-vm-w.html)

1. Choose **Finish**. The OVA is installed, the guest is created, and AWS Elemental Conductor File is installed on that guest with the eth0 configured as specified.

1. Before proceeding, take a snapshot of the VM, as described in the VMware vSphere help text.

1. When you've finished installing, enter the hostname of the worker node into a web browser and make sure that the web interface appears.

1. Repeat these steps for each worker node.