# Configuring NTP and PTP servers

You must configure a clock server for the nodes to use. You can configure any of these types
of clock servers:

- An NTP clock.

- A PTP clock
  If you plan to set up at least one channel with a SMPTE 2110 output, you
  must set up the clocks as follows:

- Configure the AWS Elemental Conductor Live nodes and any AWS Elemental Statmux nodes to use NTP.

- Configure all the AWS Elemental Live nodes that include SMPTE 2110 outputs with PTP. For other
  Elemental Live nodes, you can configure to use PTP or NTP.
  If you don't plan to set up with SMPTE 2110 outputs, you can set up all
  the nodes to use NTP.

## Configuring NTP

servers

**Where to perform the configuration for
NTP**

Make sure you perform the configuration on the correct nodes.

| Node                          | Work on this node? |
| ----------------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Primary Conductor Live node   | Yes                |
| Secondary Conductor Live node | Yes                |
| Each worker node              | Yes                | **Recommendation** We recommend that you set up each worker node to specify the URL of the primary Conductor Live node. In this way, the worker nodes synchronize their internal clocks with Conductor Live. Setting up in this way reduces the risk that one worker clock will drift from the other clocks and cause encoding problems. ###### To configure NTP on Conductor Live 1. Perform this step in the remote terminal session on the primary Conductor Live node. <br>• On the Conductor Live node, edit the file `/etc/chrony.conf` <br>• Uncomment the following line, and modify the IP addresses to specify the subnet that Conductor Live and the workers are configured with. `#allow 192.168.0.0/16` <br>• Uncomment the following line. `#local stratum 10` When you uncomment this line, the worker nodes will be able to sync with the Conductor Live node even if the Conductor Live loses communication with the NTP server. All the nodes must stay in synch all the time, in order for Conductor Live to control the worker nodes. <br>• Save the file. <br>• On the Conductor Live enter this command to restart chronyd: `sudo systemctl restart chronyd` 2. On the Conductor Live web interface, go to the **Settings** page and choose **Network**. 3. On the **Network Time Protocol Servers** tab, enter the IP address for the server you want to use. ###### To configure NTP on Elemental Live or Elemental Statmux 1. On the Elemental Live web interface, choose **Settings** from the main menu. 2. Choose the **Network** tab, then choose **Hostname, DNS, & Timing Server**. 3. In the **NTP Servers** section, set up one line, with the IP address of the primary Conductor Live node. Choose **Save**. ## Configuring PTP PTP applies only to Elemental Live, and only starting with version 2.21.3, which is when support for SMPTE 2110 was introduced. ###### To configure PTP on Elemental Live 1. On the Elemental Live web interface, go to the **Settings** page and choose **Network**. 2. On the **Host, DNS & Timing Server** tab, select the Enable PTP check box and choose Save. When you save, PTP is enabled on the Elemental Live node. If NTP was previously enabled, it is automatically disabled on the Elemental Live node. But the Conductor Live nodes and the Elemental Statmux nodes in the cluster will continue to use NTP. |
