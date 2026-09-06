

# Step B: Deploy the VM
<a name="install-vm-cl3-ig-install-vm"></a>

Perform these steps from your workstation.

1. Place the OVA image in a location convenient and accessible to the VM host.

1. Start the VMware vSphere client and choose the option that lets you run the OVF Deploy wizard.

1. Complete the fields in the wizard. Pay special attention to the following settings:
   + For the *source*, enter the location where you saved the OVA file.
   + Ensure that the *hostname* that you assign to the VM guest is unique across all of your AWS Elemental products.
   + For *network settings*, such as DNS servers and eth configuration, leave the fields blank. You will configure these settings later in the Conductor Live installation and configuration process.

   When you finish and save your inputs, the OVA is installed, the guest is created, and the eth0 is configured as specified.

1. Before you proceed, take a snapshot of the VM as described in the VMware vSphere help text.

1. Repeat these steps to install the OVA on all VM instances.