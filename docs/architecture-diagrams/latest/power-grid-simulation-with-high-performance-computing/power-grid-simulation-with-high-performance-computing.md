# Power Grid Simulation with High Performance Computing on AWS

Publication date: **August 10, 2023 ([Diagram history](#diagram-history "#diagram-history"))**

This reference architecture shows power utilities how to run large-scale grid simulations with high performance
computing (HPC) on AWS and use cloud-native, fully-managed services to perform advanced analytics on the study
results. Find insights from output using serverless data integration, interactive query, and machine learning
(ML) methods to help with grid planning and operations.

## Power Grid Simulation with High Performance Computing on AWS Diagram

![Reference architecture diagram showing how to run large-scale grid simulations with high performance computing (HPC) on AWS and use cloud-native, fully-managed services to perform advanced analytics on the study results.](images/power-grid-simulation-with-high-performance-computing.png)

1. Provision a secondary head node if you need high availability (HA) for the cluster. Use an **Elastic Load Balancing**
   load balancer to distribute traffic to the head nodes and **Amazon Route 53** to create an alias record that points to your load balancer.
2. Install HPC Pack on the head node and compute node to form a Windows-based cluster. Use target tracking
   scaling policies with the right metrics—for example, number of queued jobs and online nodes—to
   dynamically scale the **Amazon EC2 Auto Scaling** group for compute nodes. The launched instances
   should be protected from being terminated before they process a certain number of jobs to reduce
   average waiting time due to initialization. Compute-optimized instances are recommended for the
   compute node (for example, c6id).
3. Use **AWS Glue** to perform the Extract, Transform, Load (ETL) task
   on data saved in **Amazon Simple Storage Service** (Amazon S3). Analyze the data with
   **Amazon Athena** through interactive Structured Query Language
   (SQL) queries. Connect the results with **Amazon Quick Suite** for Business
   Intelligence (BI) reporting and actionable insights delivery. Use **Amazon SageMaker AI**
   to identify power grid operation patterns and detect anomalies.
4. Use **AWS Directory Service** to run Microsoft Active Directory (AD) for
   the cluster and allow access to the head node. Use **AWS Secrets Manager**
   to store sensitive information such as AD credentials for the provisioned directory.
5. Use **AWS Storage Gateway** to allow engineers to directly
   store and retrieve data in **Amazon S3** through an
   on-premises file server. Use **Amazon FSx for Windows File Server** to
   store intermediate results during job processing.
6. Power utility customers can set up private network connectivity between their
   corporate data center and AWS with services such as **AWS Site-to-Site VPN**
   and **AWS Direct Connect** to meet their security, compliance and network bandwidth objectives.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/power-grid-simulation-with-high-performance-computing.md "samples/power-grid-simulation-with-high-performance-computing.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Contributors

Contributors to this reference architecture diagram include:

- Song Zhang, Senior Solutions Architect, Amazon Web Services

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date            |
| ------------------- | ----------------------------------------------- | --------------- |
| Initial publication | Reference architecture diagram first published. | August 10, 2023 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
