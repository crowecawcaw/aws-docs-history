

# Storage assessments
<a name="transform-app-assessments-storage"></a>

AWS Transform models your storage footprint and recommends AWS storage services and configurations based on your current storage usage and performance requirements. Storage attached to servers is right-sized alongside the compute recommendation, and AWS Transform also models detached storage across block, object, and file storage services.

## Amazon EBS
<a name="transform-app-assessments-storage-ebs"></a>

AWS Transform recommends Amazon Elastic Block Store (Amazon EBS) volume types and configurations for the block storage attached to your migrated servers, based on your current capacity, IOPS, and throughput requirements. AWS Transform accounts for storage capacity, provisioned IOPS, and provisioned throughput when estimating cost, so you can compare volume types such as gp3 and io2.

## Amazon S3
<a name="transform-app-assessments-storage-s3"></a>

AWS Transform models object storage on Amazon Simple Storage Service (Amazon S3). Use Amazon S3 modeling for unstructured data, backups, and archives that do not need to remain on block storage.

## Amazon FSx for NetApp ONTAP
<a name="transform-app-assessments-storage-fsx-ontap"></a>

AWS Transform models file storage on Amazon FSx for NetApp ONTAP, including storage capacity, provisioned IOPS, and provisioned throughput. This is the target for detached and shared file storage, including the storage attached to VMware workloads.

## Example prompts
<a name="transform-app-assessments-storage-prompts"></a>
+ "Estimate storage costs for my file servers on Amazon FSx for NetApp ONTAP"
+ "What is the impact of moving from gp3 to io2 volumes?"
+ "Model my backup and archive data on Amazon S3"