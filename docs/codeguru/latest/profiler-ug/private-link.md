# Using CodeGuru Profiler with VPC Endpoints

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a private
connection between your VPC and Amazon CodeGuru Profiler. You can use this connection to access and submit
profiles to your profiling group without crossing the public internet.

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual network that
you define. With a VPC, you have control over your network settings, such the IP address
range, subnets, route tables, and network gateways. With VPC endpoints, the AWS network
handles the routing between the VPC and AWS services.

To connect your VPC to CodeGuru Profiler, you define an interface VPC endpoint for CodeGuru Profiler. An
interface endpoint is an elastic network interface with a private IP address that serves as
an entry point for traffic destined to a supported AWS service. The endpoint provides
reliable, scalable connectivity to CodeGuru Profiler —and it doesn't require an internet
gateway, a network address translation (NAT) instance, or a VPN connection. For more
information, see [What Is Amazon VPC](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") in the
_Amazon VPC User Guide_.

Interface VPC endpoints are enabled by AWS PrivateLink. This AWS technology enables
private communication between AWS services by using an elastic network interface with
private IP addresses.

## Creating Amazon VPC Endpoints for CodeGuru Profiler

You can create a VPC endpoint to use with CodeGuru Profiler to submit profiles to your profiling
group.

To start using CodeGuru Profiler with your VPC, use the Amazon VPC console to create an interface VPC
endpoint for CodeGuru Profiler. For instructions, see the procedure "To create an interface
endpoint to an AWS service using the console" in [Creating an Interface Endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint"). Note the following procedure steps:

- Step 3 –For **Service category**, choose _AWS
  services_.
- Step 4 – For **Service Name**, choose
  _com.amazonaws.region.codeguru-profiler_ – Creates
  a VPC endpoint for CodeGuru Profiler operations.

For more information, see [Getting
Started](../../../vpc/latest/userguide/GetStarted.md "../../../vpc/latest/userguide/GetStarted.md") in the _Amazon VPC User Guide_.

###### Note

CodeGuru Profiler does not support Amazon VPC endpoint policies at this
time.
