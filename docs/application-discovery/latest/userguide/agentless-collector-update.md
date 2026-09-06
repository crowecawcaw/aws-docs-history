

AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

# Manually updating Application Discovery Service Agentless Collector
<a name="agentless-collector-update"></a>

When you configure Application Discovery Service Agentless Collector (Agentless Collector), you can choose to enable automatic updates as described in [Configuring Agentless Collector](agentless-collector-gs-configure.md). If you do not enable automatic updates, you'll need to manually update Agentless Collector.

The following procedure describes how to manually update Agentless Collector.

**To manually update Agentless Collector**

1. Obtain the latest Agentless Collector Open Virtualization Archive (OVA) file.

1. (Optional) We recommend that you delete the previous Agentless Collector OVA file, before you deploy the latest one.

1. Follow steps in [Deploy Agentless Collector](agentless-collector-deploying.md#agentless-collector-gs-deploy).

**The previous procedure only updates the Agentless Collector. It is your responsibility to keep the OS up to date.**

**To update your Amazon EC2 instance**

1.  Get the IP address of the Agentless Collector from VMware vCenter. 

1. Open the collector’s VM console and sign in as **ec2-user** using the password **collector** as shown in the following example.

   ```
   username: ec2-user
   password: collector
   ```

1. Follow the instructions in [Update instance software on your AL2 instance](https://docs.aws.amazon.com/linux/al2/ug/install-updates.html) in the Amazon Linux 2 User Guide.

**Kernel Live Patching**

------
#### [ Agentless Collector version 2 ]

The Agentless Collector version 2 virtual machine uses Amazon Linux 2023 as described in [Deploy Agentless Collector](agentless-collector-deploying.md#agentless-collector-gs-deploy). 

To enable and use Live Patching for Amazon Linux 2023, see [Kernel Live Patching on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/live-patching.html) in the *Amazon EC2 User Guide*.

------
#### [ Agentless Collector version 1 ]

The Agentless Collector version 1 virtual machine uses Amazon Linux 2 as described in [Deploy Agentless Collector](agentless-collector-deploying.md#agentless-collector-gs-deploy). 

To enable and use Live Patching for Amazon Linux 2, see [Kernel Live Patching on AL2](https://docs.aws.amazon.com/linux/al2/ug/al2-live-patching.html) in the *Amazon EC2 User Guide*.

------

**To upgrade from Agentless Collector version 1 to version 2**

1. Install a new Agentless Collector OVA by using the latest image.

1. Set up credentials.

1. Delete the old virtual appliance.