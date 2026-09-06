

# Semiconductor and Electronics on AWS
<a name="semiconductor-electronics-on-aws"></a>

Publication date: **February 21, 2020 ([Diagram history](#semi-history))**

With this architecture, you can run semiconductor design workflows on AWS. The solution provides an overview of AWS services and data movement options for design compute, storage, remote access, and security. You can also collaborate with fabrication partners and third-party IP providers.

## Semiconductor and electronics on AWS diagram
<a name="semi-diagram"></a>

![Reference architecture diagram showing AWS services and data movement for semiconductor design workflows including Amazon EC2, Amazon S3, Amazon EFS, and FSx for Lustre.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/semiconductor-electronics-on-aws/images/semiconductor-electronics-on-aws.png)


The following steps describe the data flow and key configuration points for this architecture:

1. Determine what data you need for your proof of concept or test.

1. Transfer data into AWS by using [AWS Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/), AWS Direct Connect, or other AWS services.

1. Store transferred data in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) buckets. Access data stored in Amazon S3 from an [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) instance or nearly any AWS service.

1. Access your environment through a remote desktop session or command line (SSH).

1. Use all of the infrastructure needed for semiconductor design workflows on AWS.

1. Use AWS flexible and robust compute to run semiconductor design workflows.

1. Store tools and job data on [Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/), [FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/), and local disk. (Optional) Move long-term data to Amazon S3.

1. Use other AWS services such as data lakes, artificial intelligence and machine learning (AI/ML), and analytics after your data is in AWS.

1. Isolate environments to enhance security and limit third parties to only the data they need.

1. Enable encryption everywhere by using [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/) with your keys.

## Further reading
<a name="semi-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="semi-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#semi-history) | Reference architecture diagram first published. | February 21, 2020 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.