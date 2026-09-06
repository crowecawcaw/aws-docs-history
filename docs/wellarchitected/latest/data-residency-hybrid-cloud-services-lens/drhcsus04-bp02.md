

# DRHCSUS04-BP02 Use elasticity and automation to optimize storage volumes usage in AWS Local Zones
<a name="drhcsus04-bp02"></a>

 EBS volumes attached to EC2 instances in AWS Local Zones should be provisioned as small as possible to meet workload requirements and then grown as needed when more capacity is required. 

 **Desired outcome:** EBS volumes will be sized to meet workload requirements and minimize energy consumption, while growing dynamically via automation when needed. 

 **Benefits of establishing this best practice:** Your workloads will be provisioned to use the minimum required EBS storage, decreasing energy consumption, while retaining the ability to grow storage via automation when needed. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance-59"></a>

 Create and use Amazon EBS volumes in Local Zones with size, throughput, and latency characteristics appropriate for your data residency workloads. Provision the smallest suitable EBS volumes, and use [elasticity and automation](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a5.html) to expand volumes as data grows. This improves sustainability by preventing over-provisioning of workload storage. Use [Amazon CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/metrics-collected-by-CloudWatch-agent.html) to collect and monitor guest disk utilization, and set thresholds to initiate EBS volume expansion when thresholds are reached. 