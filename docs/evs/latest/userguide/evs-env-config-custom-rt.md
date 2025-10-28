# Configure a custom route table for Amazon EVS subnets

Amazon EVS supports the use of a custom route table only after the Amazon EVS environment is created.
To enable successful environment creation, you must configure the main route table to allow traffic to dependent services such as DNS and on-premises systems.
This is because Amazon EVS VLAN subnets are implicitly associated to our VPC’s main route table during environment deployment.

After your environment deploys, you must explicitly associate each of the Amazon EVS VLAN subnets with a route table in your VPC.
NSX connectivity fails if your VLAN subnets are not explicitly associated with a VPC route table.
We strongly recommend that you explicitly associate your subnets with a custom route table.
A custom route table provides more granular control over network traffic routing within your VPC, allowing for tailored routing rules for specific subnets or gateways.
For more information about creating a custom route table, see [Create a route table for your VPC](../../../pc/latest/userguide/create-vpc-route-table.md "../../../pc/latest/userguide/create-vpc-route-table.md") in the _Amazon VPC User Guide_.
