# Default subnets

By default, a default subnet is a public subnet, because the main route table sends the
subnet's traffic that is destined for the internet to the internet gateway. You can
make a default subnet into a private subnet by removing the route from the
destination 0.0.0.0/0 to the internet gateway. However, if you do this, no EC2
instance running in that subnet can access the internet.

Instances that you launch into a default subnet receive both a public IPv4 address and a
private IPv4 address, and both public and private DNS hostnames. Instances that you
launch into a nondefault subnet in a default VPC don't receive a public IPv4 address
or a DNS hostname. You can change your subnet's default public IP addressing
behavior. For more information, see [Modify the IP addressing attributes of your subnet](subnet-public-ip.md "subnet-public-ip.md").

From time to time, AWS may add a new Availability Zone to a Region. In most cases, we
automatically create a new default subnet in this Availability Zone for your default
VPC within a few days. However, if you made any modifications to your default VPC,
we do not add a new default subnet. If you want a default subnet for the new
Availability Zone, you can create one yourself. For more information, see [Create a default subnet](work-with-default-vpc.md#create-default-subnet "work-with-default-vpc.md#create-default-subnet").
