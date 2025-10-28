# Connecting to the Hue web user interface

Connecting to the Hue web user interface is the same as connecting to any HTTP
interface hosted on the master node of a cluster. The following procedure describes how
to access the Hue user interface. For more information, see [View web interfaces hosted on EMR
clusters](../ManagementGuide/emr-web-interfaces.md "../ManagementGuide/emr-web-interfaces.md") in the _Amazon EMR Management Guide_.

###### To view the Hue web user interface

1. Follow these instructions to [Set up an SSH tunnel to the master node using dynamic port
   forwarding](../ManagementGuide/emr-ssh-tunnel.md "../ManagementGuide/emr-ssh-tunnel.md") in the _Amazon EMR Management Guide_.
2. Type the following address in your browser to open the
   **Hue** web interface: `http://`master
   public DNS`:8888` where `master public
dns` is the public DNS name of your cluster master node, for
   example `ec2-11-22-333-44.compute-1.amazonaws.com`.
3. At the Hue login screen, if you are the administrator logging in for the
   first time, enter a user name and password to create your Hue superaccount
   and then select **Create account**. Otherwise, type your
   username and password and select **Create account** or enter
   the credentials provided by your administrator.
