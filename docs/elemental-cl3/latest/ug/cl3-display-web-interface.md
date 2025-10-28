# Displaying the Conductor Live web

interface

You create ECL3; encoding workflow by creating profiles and channels. When you are
ready, you then start the channel. When your Elemental Live nodes are in a cluster, you should use
AWS Elemental Conductor Live to create the Elemental Live encoding workflow.

## Displaying the web

interface

1. Obtain the following information from the person who configured the
   Conductor Live cluster:
   - IP address of the Conductor Live node. The correct address depends on
     your high-availability redundancy setup:
     - If the cluster is set up with Conductor Live high-availability
       redundancy, the address is the address of the VIP. This VIP is set up
       when you configured for high-availability redundancy, as described in
       the [AWS Elemental Conductor Live Configuration Guide](../configguide.md "../configguide.md").
     - If your Conductor Live cluster is _not_ set up with Conductor Live redundancy, use the IP
       address of the Conductor Live to set it up.

   - Your user credentials, if the cluster is set up for user
     login.

   - Whether the cluster is set up for worker redundancy.

2. On a web browser, enter the IP address that you obtained.

###### Warning

In a high-availability deployment, you must always access the web
interface from the VIP. It is possible to access it from the primary
Conductor Live, but, when a failover occurs, problems occur. 3. If the **Login** dialog appears, enter your user
credentials.

The Conductor Live web interface appears. The Conductor Live main menu contains these
menu items:

- **Channels**: Lets you create and work with channels
  that are on an Elemental Live node in the cluster.
- **Profiles**: Lets you create and work with profiles
  that are on an Elemental Live node in the cluster.
- **MPTS**: Lets you create and work with MPTSes (MPTS outputs)
  that are on an Elemental Statmux node in the cluster.
- **Status**: Lets you monitor activity on all the
  nodes in the cluster.
- **Cluster**: Lets you set up the cluster and set up
  redundancy groups in the cluster.
- **Settings**: Lets you configure hardware components
  (such as network cards) on the Conductor Live node, and configure the Conductor Live
  software.

## Viewing Conductor Live

configuration information

On the Conductor Live web interface, choose the **Globe** icon
at the top right of the page. A drop-down menu appears showing system
information:

- If redundancy is enabled on the cluster, the information includes the
  following:
  - The term **High Availability Enabled**.
  - The hostname beside the **Globe** icon shows the
    hostname of the Conductor Live that is currently the primary
    Conductor Live.
  - The **VIP** field shows the IP address of the VIP.
    This address does not match either the primary or the backup
    Conductor Live node.

- If redundancy is not enabled, the information appears as:

The hostname beside the **Globe** icon shows the
hostname of the Conductor Live.

The **IP** field shows the IP address of the
Conductor Live node.

For more information about Conductor Live redundancy, see [Conductor Live node redundancy](redundancy-cl3.md "redundancy-cl3.md").
