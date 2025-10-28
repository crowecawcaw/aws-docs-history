# Logging In to Your Amazon EC2 Gateway

Local Console

You can connect to your Amazon EC2 instance by using a Secure Shell (SSH) client. For
detailed information, see [Connect to
Your Instance](../../../AWSEC2/latest/UserGuide/AccessingInstances.md "../../../AWSEC2/latest/UserGuide/AccessingInstances.md") in the _Amazon EC2 User Guide_. To connect this
way, you will need the SSH key pair you specified when you launched the instance. For
information about Amazon EC2 key pairs, see [Amazon EC2 Key Pairs](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md") in the _Amazon EC2 User Guide._

###### To log in to the gateway local

console

1. Log in to your local console. If you are connecting to your EC2 instance from
   a Windows computer, log in as _admin_.
2. After you log in, you see the **AWS Storage Gateway -
   Configuration** main menu, from which you can perform various
   tasks.

| To Learn About This Task                 | See This Topic                                                                                                                              |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Configure a SOCKS proxy for your gateway | [Routing your gateway deployed on EC2 through an HTTP proxy](EC2_MaintenanceRoutingProxy-common.md "EC2_MaintenanceRoutingProxy-common.md") |
| Test network connectivity                | [Testing gateway network connectivity](EC2_MaintenanceTestGatewayConnectivity-common.md "EC2_MaintenanceTestGatewayConnectivity-common.md") |
| Run Storage Gateway console commands     | [Running Storage Gateway commands on the local console](EC2_MaintenanceGatewayConsole-common.md "EC2_MaintenanceGatewayConsole-common.md")  |
| View a system resource check             | [Viewing your gateway system resource status](EC2_system-resource-check-common.md "EC2_system-resource-check-common.md").                   | To shut down the gateway, enter `0`. To exit the configuration session, enter `X`. |
