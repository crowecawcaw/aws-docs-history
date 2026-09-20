

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# Step B: Install (Kickstart) the Operating System Software
<a name="clean-install-sm-upg-install"></a>

You must install a configured operating system from an `.iso` file onto each physical machine that will be running AWS Elemental software. Doing so is referred to as “kickstarting the system”.

Make sure that you install the right version of the operating system with each piece of software. The correct `.iso` file is always provided with the `.run` file under **Activations** at [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations).

**Create a Boot USB Drive or DVD**  
Do this from your workstation.

Use a third-party utility (such as PowerISO or ISO2USB) to create a bootable DVD or USB drive from your `.iso` file. Instructions for using these utilities can be found in the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter) knowledge base.

**Install the Operating System at Each Node**  
Do this from each Elemental node.

1. Insert the DVD or USB thumb drive into the hardware unit.

1. Boot up or reboot the system. The installer automatically starta.  
![](https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/images/install-installer-shared-png.png)

1. Use the arrow keys to select each option and do the following:



<table>
<thead>
  <tr><th>Menu Option</th><th>Instructions</th></tr>
</thead>
<tbody>
  <tr><td><code>Set Hostname</code></td><td>Change the hostname to a useful name such as <b>statmux-01</b> or <b>statmux-chicago-01</b>.<br />Do not use localhost as the hostname!<br />Do not use periods or underscores in the hostname</td></tr>
  <tr><td><code>Disk layout: Auto-detect</code></td><td>Leave this set at Auto-detect.</td></tr>
  <tr><td><code>Set Key</code></td><td>Press the down arrow to skip this option.</td></tr>
  <tr><td><code>Upgrade</code></td><td>Choose <b>No</b>. Choosing <b>No</b> deletes all data from the hardware unit. Never choose <b>Yes</b> when doing a new install.</td></tr>
  <tr><td><code>Install and configure base operating system</code></td><td>Press <b>Enter</b> to begin the OS installation.</td></tr>
</tbody>
</table>


   The operating system is installed. From now on, the system runs this customized version of your Linux operating system.

1. Repeat the above steps on each system, using the `.iso` file that goes with the AWS Elementalsoftware you are installing on each system.