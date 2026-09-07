

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html) or [AWS Wickr User Guide](https://docs.aws.amazon.com/wickr/latest/userguide/what-is-wickr.html).

# Multi-Node installation
<a name="multi-node-installation"></a>

Wickr Enterprise Embedded Cluster Multi-Node installations provide an option for Embedded Cluster users to separate the Wickr Calling and Wickr Messaging workloads on to different physical machines. To do this, Wickr Enterprise leverages the Replicated Embedded Cluster Multi-Node tooling.

## Port requirements
<a name="multi-node-port-requirements"></a>

The following ports must be open on all members of the cluster for the Multi-Node functionality to work correctly. These only need to be open between the nodes themselves, and not open to the wider internet.
+ 53 TCP/UDP
+ 2380/TCP
+ 4789/UDP
+ 6443/TCP
+ 8080/TCP
+ 9091/TCP
+ 9443/TCP
+ 10249/TCP
+ 10250/TCP
+ 10256/TCP
+ 30000/TCP
+ 50000/TCP

## License requirements
<a name="multi-node-license-requirements"></a>

The Wickr Embedded Cluster Multi-Node configuration options require additional license privileges. Contact Support to make sure your license supports this feature.

## Creating an additional node during initial setup
<a name="multi-node-initial-setup"></a>

When you initially configure the Wickr Enterprise Embedded Cluster, you can create an additional calling node during the setup process. Start by following the procedure described in [Installation of Wickr Enterprise embedded cluster (standard)](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/standard-installation.html) When you navigate to the KOTS admin panel, you will be prompted to create additional nodes.

**Note**  
Currently, Embedded Cluster Multi-Node supports only 1 calling node and 1 messaging/controller node.

To begin, deselect the **Controller** role option and select the **Calling** role option. This populates additional instruction sets for configuring the new node. Run these instructions on the new node to configure it to join the cluster as a calling node.

Run instructions similar to the following examples on the new node:

1. Download the binary on the new node:

   ```
   curl -k https://172.31.42.64:30000/api/v1/embedded-cluster/binary -o wickr-enterprise-ha.tgz
   ```

1. Extract the binary:

   ```
   tar -xvf wickr-enterprise-ha.tgz
   ```

1. Join the node to the cluster:

   ```
   sudo ./wickr-enterprise-ha join 172.31.42.64:30000 AAAAAbbbbbbbbCCCCCCCzzzzz
   ```

After the join command completes successfully, the new node appears on the **Configure cluster** page with the **Calling** role assigned. Choose **Continue** to proceed to the Wickr Enterprise configuration page. Follow directions for embedded node configuration options outlined in [KOTS admin console configuration](kots-admin-console-config.md).

## Adding an additional node to an existing embedded cluster installation
<a name="multi-node-add-existing-setup"></a>

To add a calling node to an existing Wickr Enterprise Embedded Cluster installation, navigate to the KOTS Admin Console. To do this, log in to the node through ssh or other mechanism and navigate to the installation directory that contains the `wickr-enterprise-ha` binary used for installation. Run `./wickr-enterprise-ha admin-console` to start the KOTS Admin Console. If this command does not return any output, the KOTS Admin Console is already running and can be accessed by navigating to port 30000 on the IP of the node in a web browser, for example: `https://127.0.0.1:30000/`.

Enter the KOTS Admin password when requested, then perform the following procedure to create an additional node:

1. Once logged in, navigate to the **Cluster Management** page on the top left of the KOTS Admin Console.

1. Choose **Add node**.

1. Deselect **Controller** under `Roles`.

1. Select **Calling** under `Roles`

1. Follow the instructions provided to run the commands on the new node you want to add.

1. When finished, choose **Close**

1. Your new node appears in the **Nodes** list with the **Calling** role.

1. Navigate to the **Application** page at the top-left of the KOTS Admin Console

1. Choose **Config** from the navigation bar at the top of the page.

1. Navigate to the **Calling** section in the left navigation panel.

1. Select **Require Calling Nodes** to allow use of the Calling node.

1. Scroll to the bottom of the page and choose **Save config**.

1. A popup appears, indicating the Config has been updated. Choose **Go to updated version**.

1. On the updated version page, the currently installed version is displayed. A new line item is listed under installed versions with the designation **Config Change**. Choose **Deploy** to deploy this new version and enable the new calling node.