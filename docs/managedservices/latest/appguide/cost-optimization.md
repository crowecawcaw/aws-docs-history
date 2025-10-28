# Cost optimization in AWS Managed Services

AWS Managed Services provides a detailed cost utilization and savings reports every month to you during your monthly business reviews (MBRs).

AMS follows a standard set of processes and mechanisms to identify cost saving avenues in your managed accounts and assist you
to plan and roll-out the changes to optimize your AWS spend.

###### Note

AMS is developing a video to help with cost optimization. The first step is providing you with a PDF and an Excel spreadsheet of
cost optimization best practices. To access these resources, open the
[Quick guide to cost optimization](samples/Resources_Quick_Guide_to_Cost_Optimization.md "samples/Resources_Quick_Guide_to_Cost_Optimization.md") ZIP file.

## Cost optimization framework

AMS follows a three-staged approach with you to optimize your AWS costs:

1. Identify cost optimization avenues in your managed environment
2. Present a cost optimization plan to you
3. Assist in achieving cost optimization in a measurable way

### Identify cost optimization avenues in the managed environment

AMS utilizes AWS native tools like Cost explorer, and Trusted Advisor while leveraging over 20 cost savings patterns across
architecture optimization, EC2 instance, and AWS account-focused optimizations to build tailored cost savings recommendations for you.

Some of the optimization recommendations include the following.

**Architectural optimization recommendations:**

- **Optimal S3 storage class use**: Amazon S3 offers a range of storage classes to meet various workload
  requirements based on data access, resiliency, and cost. S3 Intelligent-Tiering and S3 storage class analysis based on the workload
  needs allow you to manage the S3 costs efficiently.
- **Using caching architectures**: Leveraging cache instances, where applicable, can help you replace
  some database instances, while simultaneously meeting your IOPS requirements.
- **EBS upgrade savings**: Migrating your EBS volumes from gp2 to gp3 provides a cost savings of up to 20% and
  you can take advantage of predictable 3,000 IOPS baseline performance and 125 MiB/s, regardless of volume size.
- **Using elasticity**: The auto-scaling capabilities that AWS provides allow effective resource utilization
  and avenues for cost optimization. Reviewing and updating the instance scaling policies regularly based on need, further provides cost savings.

**EC2 instance-focused recommendations**

- **Instance rightsizing**: Recommendations focused on sizing the instances and optimal configurations based
  on the usage. Recommendations also include utilizing Amazon EC2 Auto Scaling feature and replacing EC2 instances where applicable with
  AWS Lambda or static web content on Amazon S3, etc.
- **Instance scheduling**: Using AMS Resource Scheduler to automatically start and stop instances based on a
  time schedule helps contain costs, especially for non-production instances that are not utilized during non-business hours.
- **Subscribing to Savings plans**: Savings plan is the easiest way to save on AWS usage. The
  EC2 Instance Savings Plans offer up to 72% savings compared to On-Demand pricing on your Amazon EC2 instances usage. The Amazon SageMaker AI Savings Plans
  offer up to 64% savings on your Amazon SageMaker AI services usage. AMS provides appropriate recommendations on Savings plans based on your AWS resource usage.
- **Reserved instance (RI) usage and consumption guidance**: Amazon EC2 Reserved Instances (RI) provide a
  significant discount (up to 75%) compared to On-Demand pricing and provide a capacity reservation when used in a specific availability zone.
- **Spot instance usage**: Fault tolerant workloads can utilize Spot instances and reduce prices up to 90%.
- **Idle instance termination**: Identifying and reporting instances that are idle or have low utilization
  that can be terminated.

**Account-focused recommendations**

- **Account cleanup**: At an account level, AMS also identifies un-utilized EBS volumes, duplicate CloudTrail trails,
  empty accounts with unused resources, and so forth, and provides recommendations for clean-up.
- **SLA recommendations**: Further, AMS regularly reviews your Plus and Premium accounts and recommends
  choosing the right SLA level for the accounts.
- **AMS automation optimization**: AMS continuously optmizes AMS automation and infrastructure used to
  provide AMS services.

### Present to customers and assist in planning

AMS conducts monthly business reviews (MBRs) with the key customer stakeholders and present the cost saving avenues, mechanisms and
recommendations identified along with potential cost savings. We further work with you to plan the changes needed.

### Assist in recommendation implementation and measure the cost impact

AMS assists in achieving and measuring cost impacts and optimization changes.

You assess the application impact, risk and success criteria of the recommended changes, and raise the appropriate requests for
change (RFCs) through the AMS console. AMS collaborates with you and implements the changes related to cost optimization in your managed accounts.
AMS measures the cost impact and include the savings realised in the monthly business reviews (MBRs).

## Cost optimization responsibility matrix

Responsibilities in AMS cost optimization.

| Cost optimization RACI                                           | Activity | Customer | AMS |
| ---------------------------------------------------------------- | -------- | -------- | --- |
| Compiling cost saving recommendations and preparing the report   | I        | R        |
| Presenting cost savings report                                   | C        | R        |
| Planning changes associated with cost savings                    | R        | C        |
| Assessing the change impact and risk                             | R        | C        |
| Raising RFCs for implementing the changes                        | R        | C        |
| Reviewing the RFCs and implementing the changes                  | C        | R        |
| Testing the application and validating the change implementation | R        | C        |
| Measuring the cost impact post change and presenting to customer | I        | R        |
