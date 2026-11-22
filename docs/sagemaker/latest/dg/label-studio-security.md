

# Security in Label Studio labeling spaces

Security is a shared responsibility between AWS and you. You control what you put in a labeling space: who joins it, the IAM permissions you grant, and the bucket you export annotations to. For more information about how the responsibilities divide, see [Shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) on the AWS website.

Your annotation data stays in your account. The labeling space holds it, and you export it to an Amazon Simple Storage Service (Amazon S3) bucket that you own. This topic describes which parts of the shared responsibility model are yours when you label data with Label Studio.

## The shared space is the access boundary
<a name="label-studio-security-boundary"></a>

**Important**  
Every member of the shared space can see every labeling project in that space, including projects assigned to other annotators. Label Studio Community Edition does not provide role-based access control, so it does not restrict what a member can do. Any member can view, create, edit, and delete projects, tasks, and annotations, including work that belongs to someone else. Nothing at the project level keeps one annotator out of another annotator's work.

You decide which annotator works on which project, and permissions do not enforce that decision. Each annotator receives their own project and a direct link to it, but any space member can open any project in the space. Plan access on that basis:
+ Add only the people you intend to have access to all the data in the space.
+ To separate groups of annotators from one another, give each group its own shared space, or its own SageMaker AI domain.
+ Everyone in a shared space can reach the same data, so treat the space, and not the project, as the unit you grant access to.
+ Plan how many annotators share a space against the limit of about 8 annotators saving at the same time, described in [Operating limits that affect planning](#label-studio-security-limits).

Annotators sign in to AWS as themselves and open Studio as their own user profile. Studio signs each annotator in to Label Studio automatically as that profile, so you do not need to distribute a separate Label Studio password or API token. You reach Label Studio only through the Studio proxy. The proxy authenticates every request, and the space exposes no public endpoint.

## AWS Identity and Access Management for labeling spaces
<a name="label-studio-security-iam"></a>

A labeling job involves four identities. Each one needs different permissions. Grant each one only the permissions described here. The following table describes the four identities, what to restrict for each one, and the permissions each one needs.

**Important**  
Do not attach `AmazonSageMakerFullAccess` to an annotator. That policy lets an annotator create a sign-in session for any user profile in the domain, which defeats the annotator restriction in the following table.


| Identity | Key restriction | Permissions it needs | 
| --- | --- | --- | 
| Project creator | Scope the project creator to their own user profile. Add an annotator's profile only if the project creator creates that annotator's sign-in link. | The project creator sets up the labeling job. They need read access to discover domains and user profiles, and access to the labeling space and its application. They also need `sagemaker:CreatePresignedDomainUrl` on their own user profile. Add an annotator's profile ARN to that permission only if the project creator creates that annotator's sign-in link; otherwise each annotator creates their own. Name each profile explicitly instead of granting the permission on every profile in the domain. | 
| Annotator | IAM enforces the restriction, not the labeling application. The restriction holds no matter how the annotator reaches Studio. | The annotator labels the data in their own project. Each annotator needs one permission: `sagemaker:CreatePresignedDomainUrl` for their own user profile and no other. Create one policy for each annotator. | 
| An annotator's execution role | Do not attach `AmazonSageMakerFullAccess`. If you attach it, an annotator can open any user profile in the domain. | Studio assumes this role when an annotator opens the application. It is a different identity from the annotator who signs in. It needs read access to the domain, user profile, space, and application. It does not need to list the other user profiles in the domain. If you omit permission to list user profiles, one annotator cannot enumerate the others. For more information, see [Give your users access to spaces](studio-updated-jl-admin-guide-permissions.md). | 
| Space execution role | This role does not need permission to create presigned sign-in sessions, and you must not grant it. | The shared space runs with the space execution role, but Label Studio itself makes no AWS calls. The space starts the application without credentials, and your own credentials upload the annotations that you export. Grant this role no permissions on behalf of Label Studio. | 

**Important**  
Two identities can create an annotator's sign-in link, and your choice decides this permission. We recommend that each annotator creates their own link with the policy that follows, so that the project creator needs `sagemaker:CreatePresignedDomainUrl` on no profile but their own. Create links on an annotator's behalf only when that annotator has no AWS access of their own, and then add only that annotator's profile ARN. A presigned URL signs its holder in as that user profile, so grant reach over another person's profile only to people you intend to have it.

Use the following policy to limit an annotator to their own user profile. In the policy, replace each placeholder value as follows:

{{region}}  
The AWS Region of your domain, such as `us-west-2`.

{{111122223333}}  
Your AWS account ID.

{{domain-id}}  
The ID of your SageMaker AI domain, such as `d-xxxxxxxxxxxx`.

{{annotator-profile-name}}  
The name of the annotator's user profile. Give each annotator a policy that names only their own profile.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "OpenOwnProfileOnly",
            "Effect": "Allow",
            "Action": "sagemaker:CreatePresignedDomainUrl",
            "Resource": "arn:aws:sagemaker:{{region}}:{{111122223333}}:user-profile/{{domain-id}}/{{annotator-profile-name}}"
        }
    ]
}
```

You cannot scope some of a project creator's read permissions to a specific resource, because the corresponding SageMaker AI API operations do not support resource-level permissions. Those operations return the names and execution role ARNs of other user profiles in the domain, so grant them only to project creators.

## Data protection
<a name="label-studio-security-data"></a>

Labeling produces two kinds of data: the records you are labeling, and the labels your annotators create. Both belong to you and both stay in your account.

**Important**  
Label Studio's cloud storage connections are turned off in a labeling space. To save annotations to Amazon S3, ask the skill to export them: it exports the annotations and uploads the file to the Amazon S3 location you give it, using your own credentials. Do not enter AWS credentials in Label Studio's **Cloud Storage** settings. The form is still visible, but a connection added there fails.

**Note**  
Deleting annotations in Label Studio does not reduce the size of its database file. Size the space's volume for the largest amount of annotation data you expect to hold at one time, not the amount you have labeled so far.

### Encryption at rest
<a name="label-studio-security-encryption-rest"></a>

Your annotation data rests in two places inside your AWS account, each with its own storage and its own encryption, and both of them support an AWS Key Management Service (AWS KMS) key that you own and manage. The following table describes where each kind of data rests and how AWS encrypts it. The skill also keeps local copies of your annotation data on the machine that runs it, and AWS does not encrypt those copies.


| Location | What rests there | How AWS encrypts it | 
| --- | --- | --- | 
| The labeling space | Label Studio keeps projects, tasks, and annotations in a database on the space's Amazon Elastic Block Store (Amazon EBS) volume, and keeps any media it serves on the same volume. | The volume uses the encryption that you configure for your domain, including an AWS KMS key that you own and manage if you set one. For more information, see [Studio notebooks](encryption-at-rest-studio.md). You set the volume size when you create the space, and that size limits how much annotation data the space holds. | 
| Your Amazon S3 bucket | The annotations that you export rest in a bucket that you own. | The destination is an existing bucket in your account. Amazon S3 encrypts the exported objects with that bucket's default encryption. Check that bucket's encryption setting, its public-access settings and its object ownership before you export to it. | 

### Encryption in transit
<a name="label-studio-security-encryption-transit"></a>

Annotators reach a labeling space over HTTPS. A project creator gives each annotator a presigned Studio domain URL, and that URL is the sign-in path to Label Studio. Requests to AWS APIs and to the Studio proxy use HTTPS, and the proxy authenticates every request.

Inside the space, Label Studio listens on the loopback interface only, so its own traffic never leaves the instance, and the space exposes no public endpoint.

### Key management
<a name="label-studio-security-key-management"></a>

Label Studio adds no key management of its own. It introduces no service-owned data store and makes no AWS KMS calls. In the two places your annotation data rests inside your AWS account, it inherits the encryption already configured there, so you manage keys where you manage those resources. A third copy rests on the machine that runs the skill, where AWS manages no encryption and you have no key to manage.
+ **The labeling space.** The database and any exports that you write to the space rest on the Amazon EBS volume of the space. That volume uses the key configured for your domain, so an AWS KMS key that you own and manage, set on the domain, also protects your annotation data, as described earlier in this topic.
+ **Your Amazon S3 bucket.** Annotations that you export rest in a bucket that you own, under the encryption of that bucket. To protect them with an AWS KMS key that you own and manage, configure server-side encryption with AWS KMS keys (SSE-KMS) on the destination bucket. For more information, see [Using server-side encryption with AWS KMS keys (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html).

  Exporting to a bucket that uses SSE-KMS also needs permissions on that bucket's key. The identity that runs the export needs the following permissions:
  + Grant `kms:GenerateDataKey` on the bucket's key, so that Amazon S3 can encrypt the exported file.
  + Grant `kms:Decrypt` on the same key, because Amazon S3 uploads an export larger than 8 MB in parts.
  + Grant `kms:Decrypt` on the key of the input dataset when the records that your annotators label come from an Amazon S3 object that uses SSE-KMS.
+ **Your machine.** The skill keeps local copies, in JSON Lines format, of the records that it imports and of every export, in the `data/hil` folder of your project. It keeps the export copy even when you also export to Amazon S3. AWS does not encrypt these files, and no AWS KMS key protects them. If the records come from a dataset that an AWS KMS key encrypts, that key does not extend to the local copy. Encrypt the disk of the machine that runs the skill, and delete these files when you no longer need them.

## Resilience and retention
<a name="label-studio-security-resilience"></a>

**Important**  
AWS does not back up annotation data in a labeling space on your behalf. Export your annotations when a labeling job finishes, and do not treat the space as durable storage.

Stopping the space's application does not delete its volume, and annotations remain available when the application restarts. Deleting the space deletes the volume and everything on it, including any annotations that you never exported. If you export to Amazon S3, you can use Amazon S3 versioning and lifecycle rules on the destination bucket to manage retention of the exported files.

**Important**  
You incur charges while a labeling space and its application run. Stop the application when annotators are not labeling, and delete the space when you no longer need it.

## Configuration and software updates
<a name="label-studio-security-updates"></a>

AWS maintains and patches the labeling application image. You do not manage an operating system and you do not apply patches yourself.

**Important**  
A running application continues to use the image it started with. To pick up an updated image, stop the application and start it again. Restart labeling spaces periodically, and whenever AWS notifies you that an update is available.

## Security best practices for labeling spaces
<a name="label-studio-security-best-practices"></a>

The following practices are general guidelines and do not represent a complete security solution. Because they might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions.

### Preventative practices for labeling spaces
<a name="label-studio-security-best-practices-preventative"></a>

The following practices limit who can reach annotation data before a job starts:
+ Grant the scoped-down policies described in [AWS Identity and Access Management for labeling spaces](#label-studio-security-iam) instead of `AmazonSageMakerFullAccess`.
+ Give each annotator a policy that names only their own user profile.
+ Add only intended members to a labeling space, because space membership is the access boundary. See [The shared space is the access boundary](#label-studio-security-boundary).
+ Review the export destination before you approve it, and keep the annotations in a bucket you control.

### Lifecycle practices for labeling spaces
<a name="label-studio-security-best-practices-lifecycle"></a>

The following practice limits how long annotation data stays reachable after a job ends:
+ Delete labeling spaces and their projects after you finish a job and export its annotations.

### Detective practices for labeling spaces
<a name="label-studio-security-best-practices-detective"></a>

The following practices show you who reached annotation data and when:
+ Use AWS CloudTrail (CloudTrail) to review who created a sign-in session and for which user profile. CloudTrail records the calling identity and the target user profile for each **CreatePresignedDomainUrl** call.
+ Monitor for labeling spaces and applications that someone creates outside your intended workflow.
+ Enable Amazon S3 server access logging or CloudTrail data events on the export bucket if your annotation data is sensitive.

**CloudTrail does not record activity inside Label Studio**  
CloudTrail records that you created a presigned URL, not that someone redeemed it. It does not record who opened the URL, or what that person did inside Label Studio afterward. Treat these records as an audit trail of who you granted a session to, not of annotator activity.

## Operating limits that affect planning
<a name="label-studio-security-limits"></a>

Up to about 8 annotators can save annotations at the same time. Label Studio Community Edition stores its data in a database that accepts one writer at a time, and the space processes simultaneous saves in sequence. Beyond roughly 8 simultaneous saves, each save takes longer, and the space completes less work overall, not more.

Any number of annotators can sign in and review data at the same time. The limit applies only to saving. A larger instance type for the space does not raise this limit, because the application's storage design sets the limit, not the compute available to the space.