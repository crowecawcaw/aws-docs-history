# Best practice 15.7 – Efficiently manage your analytics infrastructure to reduce

underutilized resources

Ensuring your organization has the correct amount of resource provisioned for your workload is a diﬃcult and challenging task. The common approach for ensuring your organization has the suﬃcient number of resources available for unpredicted peaks is to overprovision your resources. However, this approach generally leads to underutilization, and energy waste.

When designing your analytics workloads, consider using managed and serverless services. Managed services shift responsibility for maintaining high average utilization, and sustainability optimization of the deployed hardware, to AWS. Use managed services to distribute the sustainability impact of the service across all tenants of the service, reducing your individual contribution.

For a wider understanding of optimizing infrastructure for sustainability, refer to the
following information:

- Well-Architected Sustainability: [Optimizing your AWS Infrastructure for Sustainability, Part I: Compute](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute/ "https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute/")
- Well-Architected Sustainability: [Optimizing your AWS Infrastructure for Sustainability, Part II: Storage](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/ "https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/")

**How does your organization ensure efficient infrastructure
usage?**

## Suggestion 15.7.1– Use managed and serverless services

Serverless is ideal when it is diﬃcult to predict compute needs, such as with variable workloads, periodic workloads with idle time, and steady-state workloads with spikes. These kinds of workloads are common in analytics applications. Data processing pipelines, running reports, and as-necessary queries are some examples.

Use serverless services AWS Glue ETL and Amazon EMR Serverless to run your data processing jobs and let AWS manage and optimize the underlying resources efficiently. Similarly, using Amazon Athena and Amazon Redshift Serverless for data lakes and data warehousing ensures that you only use compute resources when needed, and allow these services to optimize resource utilization behind the scenes.

For more details, refer to the following information:

- [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/")
- [AWS Glue](https://aws.amazon.com/glue/engines/ "https://aws.amazon.com/glue/engines/")
- [Amazon Redshift Serverless](https://aws.amazon.com/redshift/redshift-serverless/ "https://aws.amazon.com/redshift/redshift-serverless/")
- [Amazon EMR Serverless](https://aws.amazon.com/emr/serverless/ "https://aws.amazon.com/emr/serverless/")

## Suggestion 15.7.2– Pause your data warehouse and compute clusters when not in use

Compute resources should only be allocated when needed. If your workload cannot leverage serverless technologies, you should implement a process of stopping your compute clusters if there are periods when they will not be used (for example, during nights and weekends).

If your data warehouse uses Amazon Redshift, you can use the pause and resume feature. This retains the underlying data structures so that you can resume the cluster when needed. You can pause and resume clusters using the console, or the API, or even create a schedule that automatically pauses and resumes the cluster at set times.

Pausing data warehouse and compute clusters when not in use ensures there are fewer underutilized resources and reduces the environmental impact of your analytics workload.

For more details, refer to the following information:

- [Amazon Redshift pause and resume: Lower your costs with the new pause and resume actions on Amazon Redshift](https://aws.amazon.com/blogs/big-data/lower-your-costs-with-the-new-pause-and-resume-actions-on-amazon-redshift/ "https://aws.amazon.com/blogs/big-data/lower-your-costs-with-the-new-pause-and-resume-actions-on-amazon-redshift/")
- [Amazon Redshift pause and resume: Pausing and resuming clusters](../../../redshift/latest/mgmt/managing-cluster-operations.md#rs-mgmt-pause-resume-cluster "../../../redshift/latest/mgmt/managing-cluster-operations.md#rs-mgmt-pause-resume-cluster")
- [AWS Well-Architected Framework Data Analytics: Decouple storage from compute](best-practice-11.1---decouple-storage-from-compute..md "best-practice-11.1---decouple-storage-from-compute..md")

## Suggestion 15.7.3 – Scale your data warehouses and compute clusters to match demand

Only the necessary amount of compute resources should be allocated at any time. Scaling your data warehouse and compute clusters to match demand helps you maximize resource utilization, and reduce the environmental impact of your analytics workload.

For more details, refer to the following information:

- [AWS Well-Architected Framework: SUS05-BP01 Use the minimum amount of hardware to meet your needs](../sustainability-pillar/sus_sus_hardware_a2.md "../sustainability-pillar/sus_sus_hardware_a2.md")
- AWS Well-Architected Framework Data Analytics: Best practice 11.4 – Use auto scaling where appropriate
- [Scale Amazon Redshift to meet high throughput query requirements](https://aws.amazon.com/blogs/big-data/scale-amazon-redshift-to-meet-high-throughput-query-requirements/ "https://aws.amazon.com/blogs/big-data/scale-amazon-redshift-to-meet-high-throughput-query-requirements/")
- [Amazon Redshift: Elastic resize](../../../redshift/latest/mgmt/managing-cluster-operations.md#elastic-resize "../../../redshift/latest/mgmt/managing-cluster-operations.md#elastic-resize")
- [Amazon Redshift: Working with concurrency scaling](../../../redshift/latest/dg/concurrency-scaling.md "../../../redshift/latest/dg/concurrency-scaling.md")

## Suggestion 15.7.4 – Run your analytics workloads on spare capacity in your Amazon EKS environment for optimal application infrastructure usage

If you use Amazon EKS to run your applications, you can use Amazon EMR on Amazon EKS to also run your analytics workloads, such as Apache Spark jobs, on the same infrastructure. This can make it possible to increase the utilization of your existing compute resources.

For more details, refer to the following information:

- [Amazon EMR on Amazon EKS](https://aws.amazon.com/emr/features/eks/ "https://aws.amazon.com/emr/features/eks/")
