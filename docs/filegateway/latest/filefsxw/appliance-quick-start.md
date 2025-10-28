Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Setting up your AWS Storage Gateway Hardware Appliance

###### Note

End of availability notice: As of May 12, 2025, the AWS Storage Gateway Hardware Appliance
will no longer be offered. Existing customers with the AWS Storage Gateway Hardware
Appliance can continue to use and receive support until May 2028. As an alternative,
you can use the AWS Storage Gateway service to give your applications on-premises and
in-cloud access to virtually unlimited cloud storage.

After you receive your Storage Gateway Hardware Appliance, you use the hardware appliance local
console to configure networking to provide an always-on connection to AWS and activate
your appliance. Activation associates your appliance with the AWS account that is used
during the activation process. After the appliance is activated, you can launch an
S3 File Gateway, FSx File Gateway, Tape Gateway, or Volume Gateway from the Storage Gateway
console.

###### To install and configure your hardware appliance

1. Rack-mount the appliance, and plug in power and network connections. For more
   information, see [Physically installing your hardware appliance](appliance-rack-mount.md "appliance-rack-mount.md").
2. Set the Internet Protocol version 4 (IPv4) addresses for the hardware
   appliance (the host). For more information, see [Configuring hardware appliance network
   parameters](appliance-configure-network.md "appliance-configure-network.md").
3. Activate the hardware appliance on the console **Hardware appliance
   overview** page in the AWS Region of your choice. For more
   information, see [Activating your AWS Storage Gateway Hardware Appliance](appliance-activation.md "appliance-activation.md").
4. Create a gateway on your hardware appliance. For more information, see [Creating your gateway](create-file-gateway.md "create-file-gateway.md").

You set up gateways on your hardware appliance the same way that you set up gateways
on VMware ESXi, Microsoft Hyper-V, Linux Kernel-based Virtual Machine (KVM), or
Amazon EC2.

###### Increasing the usable cache storage

You can increase the usable storage on the hardware appliance from 5 TB to 12 TB. Doing
this provides a larger cache for low latency access to data in AWS. If you ordered
the 5 TB model, you can increase the usable storage to 12 TB by buying five 1.92 TB
SSDs (solid state drives).

You can then add them to the hardware appliance before you activate it. If you have already
activated the hardware appliance and want to increase the usable storage on the appliance to
12 TB, do the following:

1. Reset the hardware appliance to its factory settings. Contact AWS Support for
   instructions on how to do this.
2. Add five 1.92 TB SSDs to the appliance.

###### Network interface card options

Depending on the model of appliance you ordered, it may come with a 10G-Base-T
RJ45 copper, or a 10G DA/SFP+ network card.

- 10G-Base-T NIC configuration:
  - Use CAT6 cables for 10G or CAT5(e) for 1G

- 10G DA/SFP+ NIC configuration:
  - Use Twinax copper Direct Attach Cables up to 5 meters
  - Dell/Intel compatible SFP+ optical modules (SR or LR)
  - SFP/SFP+ copper transceiver for 1G-Base-T or 10G-Base-T
