

# SEC08-BP04 Enforce access control

 Encryption protects data at rest, and access control decides who can reach that data. Apply least privilege, isolate data by sensitivity, block public access, and preserve prior versions to limit unauthorized access and damage from accidental or unauthorized changes. 

 **Desired outcome:** 
+  You allow only authorized users and services to reach data, and only for the tasks that require it. 
+  You scope access to decryption keys as tightly as access to the data itself. 
+  You isolate data of different sensitivity levels, so exposure of one level does not expose others. 
+  Your versioning and object retention protect critical data against modification and deletion. 
+  You block public access to storage unless a specific, reviewed requirement allows it. 

 **Common anti-patterns:** 
+  Teams store data of different sensitivity or classification together. 
+  Administrators grant overly permissive permissions on decryption keys. 
+  Teams classify data incorrectly, so the controls do not match its sensitivity. 
+  Teams keep no detailed backups of important data. 
+  Teams provide persistent access to production data instead of time-bound access. 
+  Teams do not audit data access or review permissions on a regular cadence. 

 **Benefits of establishing this best practice:** 
+  An identity under unauthorized control reaches only the data its narrow permissions allow, which limits blast radius. 
+  Isolating classifications keeps a single exposure from cascading across your data estate. 
+  Versioning and object locking give you a recovery path after accidental or unauthorized changes. 
+  Regular access review removes standing permissions before they become an attack path. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Access control for data at rest is layered. Identity permissions govern who can call operations, resource policies govern what a bucket, volume, or key allows, and account boundaries govern which workloads can see the resource. These layers overlap, so a mistake in one layer does not expose data by itself. Isolate data by classification into distinct accounts through [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) to keep a permission error contained. 

 Access to encryption keys is access to data. For example, a principal that can decrypt is able to read whatever the key protects. Apply the same least privilege scrutiny to [AWS KMS key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) that you apply to data permissions. Review who can decrypt, and use conditions to constrain when and from where decryption is allowed. 

 Public exposure of storage is usually caused by a single permissive policy. Set a default of no public access, and use detective controls such as [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) managed rules to detect resources that become publicly reachable. Serve content through a distribution layer to keep the origin private. Apply the same review to other data sources that authorize access through identity policies. 

 Protect integrity and recoverability alongside confidentiality. Versioning preserves earlier copies, so you can reverse an accidental overwrite or deletion. Object locking and vault locking make protected copies immutable for a retention period, and even a highly privileged operator cannot delete them before the lock expires. Audit resource sharing regularly. Snapshots, images, and resources shared for a past need often stay shared long after, so revoke access that is no longer justified. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Apply least privilege to data and keys:** Review the permissions granted to users and services, and remove any that exceed what a task requires. Review access to encryption keys through your [AWS KMS key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html), and confirm that appropriate conditions apply. 

1.  **Isolate data by classification with separate accounts:** Place each data classification level in a distinct AWS account, and manage those accounts centrally with [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html). This isolation reduces the risk that access to one level exposes another. 

1.  **Review and restrict storage access:** Regularly review [Amazon S3 bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html), avoid publicly readable or writable buckets, and use [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) to detect resources that allow public access. Serve content through [Amazon CloudFront](https://aws.amazon.com/cloudfront/) to keep the origin private, and apply the same review to databases and other sources that use IAM authentication. 

1.  **Analyze external and public access:** Configure [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) to generate findings when a policy grants access to an entity outside your defined boundary. Review the findings and correct any unintended access. 

1.  **Preserve and lock critical data:** Enable [Amazon S3 versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) to recover from overwrites and deletions, and use [Amazon S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) to make objects immutable for a retention period, including archived objects in the Amazon Glacier storage classes. 

1.  **Audit encryption and replication status:** Use [Amazon S3 Inventory](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory.html) to report on the encryption and replication status of your objects, and act on any gaps it reveals. 

1.  **Review resource sharing regularly:** Check your [Amazon EBS snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-modifying-snapshot-permissions.html) and [AMI sharing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharing-amis.html) permissions to confirm that images and volumes are not shared with external accounts. Audit [AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) shares and stop sharing resources that no longer need it. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC08-BP01 Implement secure key management](sec08-bp01.md) 
+  [SEC08-BP02 Enforce encryption at rest](sec08-bp02.md) 
+  [SEC03-BP01 Grant least privilege access in workload components](sec03-bp01.md) 
+  [SEC03-BP03 Analyze public and cross-account access](sec03-bp03.md) 
+  [SEC07-BP01 Understand your data classification scheme](sec07-bp01.md) 

 **Related documents:** 
+  [AWS Key Management Service cryptographic details](https://docs.aws.amazon.com/kms/latest/cryptographic-details/intro.html) 
+  [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) 
+  [Building a data perimeter on AWS](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html) 

 **Related videos:** 
+  [AWS Encryption and Authorization for Security](https://aws.amazon.com/video/watch/22b31d63959/) 

 **Related examples:** 
+  [Restrict access to an Amazon S3 origin with Origin Access Control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) 