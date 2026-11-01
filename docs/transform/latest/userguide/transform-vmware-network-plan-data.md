

# Use migration plan data as network input
<a name="transform-vmware-network-plan-data"></a>

Skip collecting a separate network file. If your migration plan includes observed network connections, AWS Transform can generate your network directly from that plan, so the network reflects the servers and applications you already organized for migration.

Migration plan data is available as an input when your job includes the [Build migration plan](transform-vmware-review-groupings-and-waves.md) step before Migrate network. The option depends on the data you gave to Build migration plan. It appears when that data includes connections between your servers, such as discovery tool data collected at the OS level. It doesn't appear when you built your plan from an RVTools file alone. After Build migration plan reads your data, its summary lists the number of network connections it found.

When the option is available and you choose [Map source network to new VPCs](transform-vmware-migrate-network-new-vpcs.md) or [Apply security posture to existing VPCs](transform-vmware-apply-security-posture.md), AWS Transform asks whether to use your migration plan data or to upload a network file. Choose **Use my migration plan data** to use the plan. Choose **Upload a network file** to work from a discovery or configuration export instead.

AWS Transform uses the following data from your plan:
+ Your server inventory.
+ Your application inventory.
+ The network connections observed during discovery and migration planning.

From this data, AWS Transform generates the VPCs and subnets, followed by security groups organized around your applications. If your VPCs already exist, AWS Transform generates only the security groups and associates them with your existing VPCs.

Migration plan data also affects the review step:
+ The observed connections in your plan serve as the traffic data for stale security group rule removal. You don't submit separate traffic data.
+ The application and environment data in your plan supports the application alignment recommendation.