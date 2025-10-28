# Configure provisioning timeouts

for cluster launch in Amazon EMR

You can define a timeout period to provision Spot Instances for each fleet in your
cluster. If Amazon EMR can't provision Spot capacity, you can choose either to terminate
the cluster or to provision On-Demand capacity instead. If the timeout period ends
during the cluster resizing process, Amazon EMR cancels unprovisioned Spot requests.
Unprovisioned Spot instances aren't transferred to On-Demand capacity.

Perform the following steps to customize a provisioning timeout period for cluster
launch with the Amazon EMR console.

Console

###### To configure the provisioning timeout when you create a cluster

with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation
   pane, choose **Clusters**, and then choose
   **Create cluster**.
3. On the **Create Cluster** page, navigate to
   **Cluster configuration** and select
   **Instance Fleets**.
4. Under **Cluster scaling and provisioning
   option**, specify the Spot size for your core and
   task fleets.
5. Under **Spot timeout configuration**, select
   either **Terminate cluster after Spot timeout**
   or **Switch to On-Demand after Spot timeout**.
   Then, specify the timeout period for provisioning Spot
   Instances. The default value is 1 hour.
6. Choose any other options that apply for your cluster.
7. To launch your cluster with the configured timeout, choose
   **Create cluster**.

AWS CLI
**To specify a provisioning timeout with the
`create-cluster` command**

```
aws emr create-cluster \
--release-label emr-5.35.0 \
--service-role EMR_DefaultRole \
--ec2-attributes '{"InstanceProfile":"EMR_EC2_DefaultRole","SubnetIds":["subnet-XXXXX"]}' \
--instance-fleets '[{"InstanceFleetType":"MASTER","TargetOnDemandCapacity":1,"TargetSpotCapacity":0,"LaunchSpecifications":{"OnDemandSpecification":{"AllocationStrategy":"lowest-price"}},"InstanceTypeConfigs":[{"WeightedCapacity":1,"EbsConfiguration":{"EbsBlockDeviceConfigs":[{"VolumeSpecification":{"SizeInGB":32,"VolumeType":"gp2"},"VolumesPerInstance":2}]},"BidPriceAsPercentageOfOnDemandPrice":100,"InstanceType":"m5.xlarge"}],"Name":"Master - 1"},{"InstanceFleetType":"CORE","TargetOnDemandCapacity":1,"TargetSpotCapacity":1,"LaunchSpecifications":{"SpotSpecification":{"TimeoutDurationMinutes":120,"TimeoutAction":"SWITCH_TO_ON_DEMAND"},"OnDemandSpecification":{"AllocationStrategy":"lowest-price"}},"InstanceTypeConfigs":[{"WeightedCapacity":1,"EbsConfiguration":{"EbsBlockDeviceConfigs":[{"VolumeSpecification":{"SizeInGB":32,"VolumeType":"gp2"},"VolumesPerInstance":2}]},"BidPriceAsPercentageOfOnDemandPrice":1,"InstanceType":"m5.xlarge"}],"Name":"Core - 2"}]'

```
