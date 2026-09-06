

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Run the Configuration Script for AWS Elemental Conductor File
<a name="config-cond-cf-cg-script"></a>

Perform this procedure if one of these applies:
+ You have two Conductor File nodes.
+ You want to require users to enter login credentials when working with the cluster (user authentication).

**Getting Ready**  
If you have a redundant Conductor File configuration, designate one of the nodes as the primary Conductor File node and the other as the secondary Conductor File node.

**Configuring AWS Elemental Conductor File**  
If you have a redundant Conductor File configuration, perform this procedure on both nodes: first the primary, and then the secondary. If you have a non-redundant configuration, perform this procedure on the one Conductor File node.

1. From a Linux prompt, log in with the *elemental* user credentials. Once you're logged in, the initial directory is `/home/elemental`.

1. Change to the directory where the configuration script is located:

   ```
   [elemental@hostname ~]$ cd /opt/elemental_se
   ```

1. Run the configuration script as follows:

   ```
   [elemental@hostname elemental_se]$ sudo ./configure
   ```

1. The following prompts appear. Complete each prompt as follows.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-script.html)

**Configuring the Conductor File Nodes**  
Take the appropriate action:
+ If you have a redundant configuration and the node that you are configuring is the primary Conductor File node, type **No**.
+ If you have a redundant configuration and the node that you are configuring is the secondary Conductor File node, type **Yes**. At the next prompt, enter the IP address or hostname of the primary node.
+ If you have a non-redundant configuration (only one Conductor File node), type **No**.