

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Step D: Deploy the VM and Install AWS Elemental Server
<a name="install-vm-p-cf-ig-install-vm-w"></a>

After you've installed the AWS Elemental Conductor File nodes, perform these steps on each individual blade that you're adding to the cluster in order to deploy a VM and install the AWS Elemental Server worker software.

1. Start the VMware vSphere client and choose the option that lets you run the OVF Deploy wizard.



<table>
<thead>
  <tr><th>Screen and Field</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td><b>Select source</b></td><td>Do one of these:<ul><li> Choose <b>URL</b> and enter the network share where you placed the OVA. </li><li> Choose <b>Local file</b> and browse to the download directory on your workstation, then select the OVA. </li></ul></td></tr>
  <tr><td><b>Review details</b></td><td>Make sure the value for <b>Size on disk</b> is as expected.</td></tr>
  <tr><td><b>Accept EULAs</b></td><td>Accept the EULA.</td></tr>
  <tr><td><b>Destination &gt; Select name and folder</b></td><td><ul><li>Assign a name to the guest (the VM that you are building on the physical blade).</li><li>Select a folder: Select the physical blade where the guest will be created.</li></ul></td></tr>
  <tr><td><b>Destination &gt; Select storage</b></td><td>Complete this screen as desired.</td></tr>
  <tr><td><b>Destination &gt; Setup networks</b></td><td>Complete this screen as desired.</td></tr>
  <tr><td><b>Destination &gt; Customize template &gt; General</b></td><td>Do the following:<ul><li> <b>Hostname</b>: Create a hostname for this guest. For example, “conductor-file01” or “conductor-file-chicago-01”. The hostname must be unique among all of your AWS Elemental products. </li><li> <b>Shut down VM after installation</b>: Make sure you set this to your preference. </li></ul></td></tr>
  <tr><td><b>Destination &gt; Customize template &gt; Installer</b></td><td> <ul><li> Location field: enter the path and filename of the AWS Elemental Server installer (.run) file. The path is to the network share where you placed the installer after downloading it. </li><li> Installer options: enter this string <pre>-s -e 2790@{{<IP address of primary Conductor File node>}}:2790@{{<IP address of secondary Conductor File node>}}</pre> <br />For example, <b>-s -e 2790@10.24.34.2:2790@10.24.34.0</b> <br />Where: <ul><li> The <code>-s</code> option instructs the installer to start the service (elemental_se) automatically. </li><li> The <code>-e</code> option (and its parameters) configures the worker node with the IP address and port of each Conductor File node. This address is used to obtain a pooled license when required. </li></ul> </li><li> License file: leave empty. </li></ul> </td></tr>
  <tr><td><b>Destination &gt; Customize template &gt; Networking</b></td><td> <ul><li> DNS servers field: Leave blank; you will configure DNS servers in the next phase of configuration. </li><li> eth0 field: Complete if you are using static IP addresses. Leave blank if you are using DHCP. </li><li> eth1 and eth2 fields: Leave blank; you will configure more Ethernet devices in the next phase of configuration. </li></ul> </td></tr>
  <tr><td><b>Ready to complete</b></td><td><b>Power on after deployment</b>: Select this field.</td></tr>
</tbody>
</table>


1. Choose **Finish**. The OVA is installed, the guest is created, and AWS Elemental Conductor File is installed on that guest with the eth0 configured as specified.

1. Before proceeding, take a snapshot of the VM, as described in the VMware vSphere help text.

1. When you've finished installing, enter the hostname of the worker node into a web browser and make sure that the web interface appears.

1. Repeat these steps for each worker node.