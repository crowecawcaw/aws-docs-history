

# Resilience in Deadline Cloud
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures. 

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

AWS Deadline Cloud does not back up data stored in your job attachments S3 bucket. You can enable backups of your job attachments data using any standard Amazon S3 backup mechanism, such as [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) or [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html).

The following list describes what each part of a farm relies on, so that you can plan backups for the parts that you own:
+ **Farm, queue, fleet, and job data** – Deadline Cloud stores this data in the AWS Region where you create the farm and doesn't replicate it to other AWS Regions. To run in a second Region, create a farm there.
+ **Job attachments** – Your Amazon S3 bucket stores these files with the durability of the storage class that you choose. Enable S3 Versioning or AWS Backup to recover from an accidental overwrite or delete.
+ **Job and worker logs** – Your CloudWatch Logs log groups store these logs. Export the logs that you need to keep for longer than the log group's retention period, if you configured one.
+ **Customer-managed fleet hosts and images** – You manage these hosts and images. Keep the infrastructure as code and the image build for a fleet in source control so that you can rebuild the fleet.