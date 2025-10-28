# Logging in to your Amazon EC2 gateway

local console

You log in to the gateway local console on an Amazon EC2 instance by using a Secure Shell
(SSH) client. For detailed information, see [Connect to your instance](../../../AWSEC2/latest/UserGuide/AccessingInstances.md "../../../AWSEC2/latest/UserGuide/AccessingInstances.md") in the
_Amazon EC2 User Guide_. To connect this way, you need the SSH key
pair that you specified when you launched your instance. For information about Amazon EC2 key
pairs, see [Amazon EC2 key pairs](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md") in the
_Amazon EC2 User Guide._

###### To log in to the gateway local

console

1. Connect to the Amazon EC2 instance using SSH and log in as the
   _admin_ user.
2. After you log in, you see the **AWS Appliance Activation -
   Configuration** main menu, from which you can perform various
   tasks.

| To Learn About This Task                    | See This Topic                                                                                                                                                 |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Configure an HTTP proxy for your gateway    | [Routing your gateway deployed on Amazon EC2 through an HTTP proxy](EC2_MaintenanceRoutingProxy-fgw.md "EC2_MaintenanceRoutingProxy-fgw.md")                   |
| Configure network settings for your gateway | [Configuring your Amazon EC2 gateway network settings](EC2-MaintenanceConfiguringStaticIP-fgw.md "EC2-MaintenanceConfiguringStaticIP-fgw.md")                  |
| Test network connectivity                   | [Testing your gateway's network connectivity](EC2_MaintenanceTestGatewayConnectivity-fgw.md "EC2_MaintenanceTestGatewayConnectivity-fgw.md")                   |
| View a system resource check                | [Viewing your gateway system resource status](EC2_system-resource-check-fgw.md "EC2_system-resource-check-fgw.md").                                            |
| Run Storage Gateway console commands        | [Running Storage Gateway commands on the local console for an Amazon EC2 gateway](EC2_MaintenanceGatewayConsole-fgw.md "EC2_MaintenanceGatewayConsole-fgw.md") | To shut down the gateway, enter `0`. To exit the configuration session, enter `X`. |
