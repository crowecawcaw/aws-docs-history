

# Multi-Region: isolation
<a name="next-gen-resilience-testing-multi-region-isolation"></a>

The **Multi-Region: isolation** test blocks connectivity between two Regions, including network traffic, cross-Region data replication, and selected dependencies. It can help you validate that your service operates independently when resources in another Region are not accessible, and surface cross-Region dependencies that could impact availability.
+ Focuses on Region isolation (loss of cross-Region connectivity) rather than recovery to another Region.
+ Blocks network traffic, pauses cross-Region replication (Amazon S3, DynamoDB, MemoryDB), and optionally blocks dependencies between the two Regions.
+ Validates that the Region can function on its own.
+ This is a sustained test. The test passes if all success alarms remain in `OK` state until the test actions end.
+ Choose success alarms that measure the isolated Region's health – validate it continues serving traffic independently.
+ This test applies to both active/active and active/passive architectures.
+ A key use case: validate your recovery Region can operate standalone. For example, if your primary is `us-east-1` and secondary is `us-west-2`, use this to validate `us-west-2` operates independently when isolated from `us-east-1`.
+ This test is also a good precursor to **Multi-Region: recovery** – validate independence before testing full failover. The test can help discover cross-Region dependencies that are critical.
+ Ensure your dependencies are actively used during the test (traffic is flowing to them) – this validates the block is having an effect. Consider adding alarms or metrics that track dependency usage (for example, request count or connection errors) to verify that the dependency is being exercised during the test.
+ Dependencies must be resolvable DNS endpoints.
+ Blocking dependencies that trigger health check failures may cause compute (for example, Amazon ECS tasks) to be replaced. The packet loss action does not re-apply to replacement tasks and may report as failed.
+ **Isolated Region** – The Region you are testing for independent operation.
+ **Destination Region** – The Region being blocked (connectivity cut to this Region).
+ **Duration** – The length of time the test actions run. It takes a few additional minutes afterward to collect final results before the test ends. Default is 3 hours when you first create the test.
+ **Dependencies to block** (optional) – If dependency discovery is enabled, the list shows dependencies from the isolated Region to the destination Region. You can select from this list or add manually by DNS domain name. No dependencies are selected by default. Other actions in this test (network connectivity, replication pausing) run regardless. Additional dependencies added here are only used for this test and will not be saved to the service's dependency discovery. These defaults apply in the console; when using the API, you provide the dependencies explicitly.

This test runs the following AWS FIS actions to drop traffic to the dependencies that you select. Actions inject 100% packet loss on Amazon EC2 instances, Amazon ECS tasks (Amazon EC2 and Fargate), and Amazon EKS pods (Amazon EC2). If your service has no resources matching an action's target type, that action is skipped.

**Note**  
The actions used to block dependencies require additional setup: SSM Agent installed on Amazon EC2 instances, an SSM Agent container in your Amazon ECS task definition, or a Kubernetes service account for Amazon EKS pods.


| Action | Description | 
| --- | --- | 
| aws:network:transit-gateway-disrupt-cross-region-connectivity | Blocks cross-Region traffic via Transit Gateway peering to the destination Region. | 
| aws:network:route-table-disrupt-cross-region-connectivity | Blocks cross-Region traffic from subnets to the destination Region. | 
| aws:network:disrupt-vpc-endpoint | Blocks traffic to cross-Region VPC endpoints to the destination Region. | 
| aws:s3:bucket-pause-replication | Pauses Amazon S3 cross-Region replication to the destination Region. | 
| aws:dynamodb:global-table-pause-replication | Pauses DynamoDB global table replication. | 
| aws:memorydb:multi-region-cluster-pause-replication | Pauses MemoryDB multi-Region cluster replication. | 
| aws:ssm:send-command | Drops traffic from Amazon EC2 instances to the selected dependencies. | 
| aws:ecs:task-network-packet-loss | Drops traffic from Amazon ECS tasks to the selected dependencies. | 
| aws:eks:pod-network-packet-loss | Drops traffic from Amazon EKS pods to the selected dependencies. | 

To see this test's parameters and their default values, use `get-test-template`.