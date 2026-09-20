

# Logging In to Your Amazon EC2 Gateway Local Console
<a name="EC2_MaintenanceConsoleWindow-common"></a>

You can connect to your Amazon EC2 instance by using a Secure Shell (SSH) client. For detailed information, see [Connect to Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html) in the *Amazon EC2 User Guide*. To connect this way, you will need the SSH key pair you specified when you launched the instance. For information about Amazon EC2 key pairs, see [Amazon EC2 Key Pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in the *Amazon EC2 User Guide.*<a name="EC2_MaintenanceConsoleWindowMenu-common"></a>

**To log in to the gateway local console**

1. Log in to your local console. If you are connecting to your EC2 instance from a Windows computer, log in as *admin*.

1. After you log in, you see the **AWS Storage Gateway - Configuration** main menu, from which you can perform various tasks.


<table>
<thead>
  <tr><th>To Learn About This Task</th><th>See This Topic</th></tr>
</thead>
<tbody>
  <tr><td>Configure a SOCKS proxy for your gateway</td><td><a href="EC2_MaintenanceRoutingProxy-common.md">Routing your gateway deployed on EC2 through an HTTP proxy</a> </td></tr>
  <tr><td>Test network connectivity</td><td> <a href="EC2_MaintenanceTestGatewayConnectivity-common.md">Testing gateway network connectivity</a> </td></tr>
  <tr><td>Run Storage Gateway console commands</td><td> <a href="EC2_MaintenanceGatewayConsole-common.md">Running Storage Gateway commands on the local console</a> </td></tr>
  <tr><td>View a system resource check</td><td> <a href="EC2_system-resource-check-common.md">Viewing your gateway system resource status</a>.</td></tr>
</tbody>
</table>


To shut down the gateway, enter **0**.

To exit the configuration session, enter **X**. 