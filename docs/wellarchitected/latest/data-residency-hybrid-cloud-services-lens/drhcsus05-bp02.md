

# DRHCSUS05-BP02 Consider Amazon S3 for Outposts, or deploy a self-managed shared-file sharing solution
<a name="drhcsus05-bp02"></a>

 Amazon S3 for Outposts or EBS-backed shared storage solutions which are self-managed or procured from the AWS Marketplace can be used to reduce data duplication and overall storage consumption. 

 **Desired outcome:** Duplication of data will be minimized using local S3, managed, or self-managed shared storage services on Outposts 

 **Benefits of establishing this best practice:** Data duplication can be minimized, reducing overall storage requirements and energy consumption for on-premises data-residency workloads. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance-61"></a>

 AWS Outposts supports [Amazon S3 for AWS Outposts](https://aws.amazon.com/s3/outposts/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc), which can be used for on-premises shared object storage. The use of shared data provides data consistency and prevents the inefficient use of per-user or per-application data duplication. Where Amazon S3 for AWS Outposts is not deployed or is unsuitable for workload requirements, consider using self-managed or [AWS Marketplace](https://aws.amazon.com/marketplace/search/results?searchTerms=shared+storage) shared storage solutions that are compatible with [Amazon Elastic Block Store (EBS)](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) on Outposts volume-types as their backing storage. 