

# DRHCSUS04-BP01 Consider sustainable object storage options for Local Zones
<a name="drhcsus04-bp01"></a>

 Amazon S3 Object storage in AWS Regions used by workloads deployed in AWS Local Zones can be optimized to use the most energy-efficient and sustainable service tiers, based on data access and resiliency requirements. 

 **Desired outcome:** Data and objects are stored in the lowest cost and most sustainable Amazon S3 service tier based on access profiles. 

 **Benefits of establishing this best practice:** The energy and cost efficiency of Amazon S3 object storage will be aligned to the data resiliency and access requirements. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance-58"></a>

 Although Amazon S3 is not available natively in Local Zones, you can still use S3 buckets located in AWS Regions to store data that is not, or is no longer, subject to data residency policies. When doing so, review the [Amazon S3 Storage Classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html), and implement [Amazon S3 storage lifecycle policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to migrate infrequently accessed data into more sustainable storage Classes such as [Amazon Glacier](https://docs.aws.amazon.com/AmazonS3/latest/userguide/glacier-storage-classes.html). 

 This practice not only optimizes storage costs and improves data management but also reduces energy consumption and environmental impact through the use of the most energy-efficient storage technologies. 