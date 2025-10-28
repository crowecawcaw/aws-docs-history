# Transitioning objects

using Amazon S3 Lifecycle

You can add transition actions to an S3 Lifecycle configuration to tell Amazon S3 to move
objects to another Amazon S3 storage class. For more information about storage classes, see
[Understanding and managing Amazon S3 storage classes](storage-class-intro.md "storage-class-intro.md"). Some
examples of when you might use S3 Lifecycle configurations in this way include the
following:

- When you know that objects are infrequently accessed, you might transition
  them to the S3 Standard-IA storage class.
- You might want to archive objects that you don't need to access in real time
  to the S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage
  classes.

###### Note

Encrypted objects remain encrypted throughout the storage class transition
process.

## Supported

transitions

In an S3 Lifecycle configuration, you can define rules to transition objects from
one storage class to another to save on storage costs. When you don't know the
access patterns of your objects, or if your access patterns are changing over time,
you can transition the objects to the S3 Intelligent-Tiering storage class for
automatic cost savings. For information about storage classes, see [Understanding and managing Amazon S3 storage classes](storage-class-intro.md "storage-class-intro.md").

Amazon S3 supports a waterfall model for transitioning between storage classes, as
shown in the following diagram.

![Amazon S3 storage class waterfall graphic.](images/lifecycle-transitions-v4.png)

### Supported lifecycle

transitions

Amazon S3 supports the following lifecycle transitions between storage classes
using an S3 Lifecycle configuration.

- The S3 Standard storage class to the S3 Standard-IA, S3 Intelligent-Tiering, S3 One Zone-IA, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, or S3 Glacier Deep Archive storage classes.
- The S3 Standard-IA storage class to the S3 Intelligent-Tiering, S3 One Zone-IA, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, or S3 Glacier Deep Archive storage classes.
- The S3 Intelligent-Tiering storage class can transition to different storage classes depending on the S3 Intelligent-Tiering access tier. The following transitions are possible for each access tier.
  - Frequent Access tier or Infrequent Access tier to S3 One Zone-IA, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, or S3 Glacier Deep Archive storage classes.
  - Archive Instant Access tier to S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, or S3 Glacier Deep Archive storage classes.
  - Archive Access tier to S3 Glacier Flexible Retrieval, or S3 Glacier Deep Archive storage classes.
  - Deep Archive Access tier to S3 Glacier Deep Archive storage classes.

- The S3 One Zone-IA storage class to the S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage classes.
- The S3 Glacier Instant Retrieval storage class to the S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage classes.
- The S3 Glacier Flexible Retrieval storage class to the S3 Glacier Deep Archive storage class.

###### Note

For versioning enabled or versioning suspended buckets, you can't transition objects with a `Pending` replication status.

## Constraints and considerations

for transitions

Lifecycle storage class transitions have the following constraints:

###### Objects smaller than 128 KB will not transition by default to any storage

class

Amazon S3 applies a default behavior to S3 Lifecycle configurations that prevents
objects smaller than 128 KB from being transitioned to any storage class. We
don't recommend transitioning objects less than 128 KB because you are charged a
transition request for each object. This means, for smaller objects, the
transition costs can outweigh the storage savings. For more information about
transition request costs, see **Requests & data
retrievals** on the **Storage &
requests** tab of the [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/") page.

To allow smaller objects to transition, you can add an [object size filter](intro-lifecycle-rules.md#intro-lifecycle-rules-filter "intro-lifecycle-rules.md#intro-lifecycle-rules-filter") to your
Lifecycle transition rules that specifies a custom minimum size
(`ObjectSizeGreaterThan`) or maximum size
(`ObjectSizeLessThan`). For more information, see [Example: Allowing objects smaller than 128 KB to be transitioned](lifecycle-configuration-examples.md#lc-small-objects "lifecycle-configuration-examples.md#lc-small-objects").

###### Note

In September 2024 Amazon S3 updated the default transition behavior for small
objects, as follows:

- **Updated default transition behavior**
  — Starting September 2024, the default behavior prevents objects
  smaller than 128 KB from being transitioned to any storage class.
- **Previous default transition behavior**
  — Before September 2024, the default behavior allowed objects
  smaller than 128 KB to be transitioned only to the S3 Glacier Flexible Retrieval and
  S3 Glacier Deep Archive storage classes.
  Configurations created before September 2024 retain the previous transition
  behavior unless you modify them. That is, if you create, edit, or delete rules,
  the default transition behavior for your configuration changes to the updated
  behavior. If your use case requires, you can change the default transition
  behavior so that objects smaller than 128KB will transition to S3 Glacier Flexible Retrieval and
  S3 Glacier Deep Archive. To do this, use the optional
  `x-amz-transition-default-minimum-object-size` header in a [PutBucketLifecycleConfiguration](../API/API_PutBucketLifecycleConfiguration.md "../API/API_PutBucketLifecycleConfiguration.md") request.

###### Objects must be stored for at least 30 days before transitioning to

S3 Standard-IA or S3 One Zone-IA

Before you transition objects to S3 Standard-IA or S3 One Zone-IA, you must store
them for at least 30 days in Amazon S3. For example, you cannot create a Lifecycle
rule to transition objects to the S3 Standard-IA storage class one day after you
create them. Amazon S3 doesn't support this transition within the first 30 days
because newer objects are often accessed more frequently or deleted sooner than
is suitable for S3 Standard-IA or S3 One Zone-IA storage.

Similarly, if you are transitioning noncurrent objects (in versioned buckets), you
can transition only objects that are at least 30 days noncurrent to S3 Standard-IA or
S3 One Zone-IA storage. For a list of minimum storage duration for all storage class,
see [Comparing the Amazon S3 storage classes](storage-class-intro.md#sc-compare "storage-class-intro.md#sc-compare").

###### You are charged for transitioning objects before their minimum storage

duration

Certain storage classes have a minimum object storage duration. If you
transition objects out of these storage classes before the minimum duration, you
are charged for the remainder of that duration. For more information on which
storage classes have minimum storage durations, see [Comparing the Amazon S3 storage classes](storage-class-intro.md#sc-compare "storage-class-intro.md#sc-compare").

You can't create a single Lifecycle rule that transitions objects from one storage
class to another before the minimum storage duration period has passed.

For example, S3 Glacier Instant Retrieval has a minimum storage duration of 90
days. You can’t specify a lifecycle rule that transitions objects to
S3 Glacier Instant Retrieval after 4 days, and then transitions objects to
S3 Glacier Deep Archive after 20 days. In this case the S3 Glacier Deep Archive transition must occur
after at least 94 days.

You can specify two rules to accomplish this, but you pay the minimum duration
storage charges. For more information about cost considerations, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

For more information about creating a S3 Lifecycle, see [Setting an S3 Lifecycle configuration on a
bucket](how-to-set-lifecycle-configuration-intro.md "how-to-set-lifecycle-configuration-intro.md").

## Transitioning to the

S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive storage classes
(object archival)

By using an S3 Lifecycle configuration, you can transition objects to the
S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage classes for
archiving.

Before you archive objects, review the following sections for relevant
considerations.

### General

considerations

The following are the general considerations for you to consider before you
archive objects:

- Encrypted objects remain encrypted throughout the storage class
  transition process.
- Objects that are stored in the S3 Glacier Flexible Retrieval or
  S3 Glacier Deep Archive storage classes are not available in
  real time.

Archived objects are Amazon S3 objects, but before you can access an
archived object, you must first restore a temporary copy of it. The
restored object copy is available only for the duration that you specify
in the restore request. After that, Amazon S3 deletes the temporary copy, and
the object remains archived in S3 Glacier Flexible Retrieval.

You can restore an object by using the Amazon S3 console or
programmatically by using the AWS SDK wrapper libraries or the Amazon S3
REST API in your code. For more information, see [Restoring an archived object](restoring-objects.md "restoring-objects.md").

- Objects that are stored in the S3 Glacier Flexible Retrieval storage
  class can only be transitioned to the S3 Glacier Deep Archive
  storage class.

You can use an S3 Lifecycle configuration rule to convert the storage
class of an object from S3 Glacier Flexible Retrieval to the
S3 Glacier Deep Archive storage class only. If you want to
change the storage class of an object that is stored in
S3 Glacier Flexible Retrieval to a storage class other than
S3 Glacier Deep Archive, you must use the restore operation to
make a temporary copy of the object first. Then use the copy operation
to overwrite the object specifying S3 Standard, S3 Intelligent-Tiering,
S3 Standard-IA, S3 One Zone-IA, or Reduced Redundancy as the storage
class.

- The transition of objects to the S3 Glacier Deep Archive
  storage class can go only one way.

You cannot use an S3 Lifecycle configuration rule to convert the
storage class of an object from S3 Glacier Deep Archive to any
other storage class. If you want to change the storage class of an
archived object to another storage class, you must use the restore
operation to make a temporary copy of the object first. Then use the
copy operation to overwrite the object specifying S3 Standard,
S3 Intelligent-Tiering, S3 Standard-IA, S3 One Zone-IA, S3 Glacier Instant Retrieval,
S3 Glacier Flexible Retrieval, or Reduced Redundancy Storage as the storage
class.

###### Note

The Copy operation for restored objects isn't supported in the
Amazon S3 console for objects in the S3 Glacier Flexible Retrieval or
S3 Glacier Deep Archive storage classes. For this type of
Copy operation, use the AWS Command Line Interface (AWS CLI), the AWS SDKs, or the
REST API.

The objects that are stored in the S3 Glacier Flexible Retrieval and
S3 Glacier Deep Archive storage classes are visible and
available only through Amazon S3. They are not available through the separate
Amazon Glacier service.

These are Amazon S3 objects, and you can access them only by using the Amazon S3
console or the Amazon S3 API. You cannot access the archived objects through
the separate Amazon Glacier console or the Amazon Glacier API.

### Cost considerations

If you are planning to archive infrequently accessed data for a period of
months or years, the S3 Glacier Flexible Retrieval and
S3 Glacier Deep Archive storage classes can reduce your storage costs.
However, to ensure that the S3 Glacier Flexible Retrieval or
S3 Glacier Deep Archive storage class is appropriate for you, consider
the following:

- Storage overhead charges – When
  you transition objects to the S3 Glacier Flexible Retrieval or
  S3 Glacier Deep Archive storage class, a fixed amount of storage
  is added to each object to accommodate metadata for managing the
  object.

      + For each object archived to S3 Glacier Flexible Retrieval or
       S3 Glacier Deep Archive, Amazon S3 uses 8 KB of storage for
       the name of the object and other metadata. Amazon S3 stores this
       metadata so that you can get a real-time list of your archived
       objects by using the Amazon S3 API. For more information, see [Get Bucket (List
       Objects)](../API/RESTBucketGET.md "../API/RESTBucketGET.md"). You are charged S3 Standard rates for this
       additional storage.
      + For each object that is archived to
       S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive,
       Amazon S3 adds 32 KB of storage for index and related metadata. This
       extra data is necessary to identify and restore your object. You
       are charged S3 Glacier Flexible Retrieval or
       S3 Glacier Deep Archive rates for this additional
       storage.

  If you are archiving small objects, consider these storage charges.
  Also consider aggregating many small objects into a smaller number of
  large objects to reduce overhead costs.

- Number of days you plan to keep objects
  archived – S3 Glacier Flexible Retrieval and
  S3 Glacier Deep Archive are long-term archival solutions. The
  minimal storage duration period is 90 days for the
  S3 Glacier Flexible Retrieval storage class and 180 days for
  S3 Glacier Deep Archive. Deleting data that is archived to
  Amazon Glacier doesn't incur charges if the objects you delete are archived
  for more than the minimal storage duration period. If you delete or
  overwrite an archived object within the minimal duration period, Amazon S3
  charges a prorated early deletion fee. For information about the early
  deletion fee, see the "How am I charged for deleting objects from
  Amazon Glacier that are less than 90 days old?" question on the [Amazon S3 FAQ](https://aws.amazon.com/s3/faqs/#Amazon_S3_Glacier "https://aws.amazon.com/s3/faqs/#Amazon_S3_Glacier").
- S3 Glacier Flexible Retrieval and
  S3 Glacier Deep Archive transition request charges
  – Each object that you transition to the
  S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage
  class constitutes one transition request. There is a cost for each such
  request. If you plan to transition a large number of objects, consider
  the request costs. If you are archiving a mix of objects that includes
  small objects, especially those under 128KB, we recommend using the
  lifecycle object size filter to filter out small objects from your
  transition to reduce request costs.
- S3 Glacier Flexible Retrieval and
  S3 Glacier Deep Archive data restore charges
  – S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive
  are designed for long-term archival of data that you access
  infrequently. For information about data restoration charges, see the
  "How much does it cost to retrieve data from Amazon Glacier?" question on the
  [Amazon S3
  FAQ](https://aws.amazon.com/s3/faqs/#Amazon_S3_Glacier "https://aws.amazon.com/s3/faqs/#Amazon_S3_Glacier"). For information about how to restore data from
  Amazon Glacier, see [Restoring an archived object](restoring-objects.md "restoring-objects.md").

###### Note

S3 Lifecycle transitions objects to S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive asynchronously. There might be a delay between the transition date in the S3 Lifecycle configuration rule and the date of the physical transition. In this case you are charged the default rate of the storage class you transitioned from based on the transition date specified in the rule.

The Amazon S3 product detail page provides pricing information and example
calculations for archiving Amazon S3 objects. For more information, see the following
topics:

- "How is my storage charge calculated for Amazon S3 objects archived to
  Amazon Glacier?" on the [Amazon S3 FAQ](https://aws.amazon.com/s3/faqs/#Amazon_S3_Glacier "https://aws.amazon.com/s3/faqs/#Amazon_S3_Glacier").
- "How am I charged for deleting objects from Amazon Glacier that are less
  than 90 days old?" on the [Amazon S3 FAQ](https://aws.amazon.com/s3/faqs/#Amazon_S3_Glacier "https://aws.amazon.com/s3/faqs/#Amazon_S3_Glacier").
- "How much does it cost to retrieve data from Amazon Glacier?" on the [Amazon S3 FAQ](https://aws.amazon.com/s3/faqs/#Amazon_S3_Glacier "https://aws.amazon.com/s3/faqs/#Amazon_S3_Glacier").
- [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/") for
  storage costs for the different storage classes.

### Restoring archived

objects

Archived objects aren't accessible in real time. You must first initiate a
restore request and then wait until a temporary copy of the object is available
for the duration that you specify in the request. After you receive a temporary
copy of the restored object, the object's storage class remains
S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive. (A [HeadObject](../API/RESTObjectHEAD.md "../API/RESTObjectHEAD.md") or
[GetObject](../API/RESTObjectGET.md "../API/RESTObjectGET.md")
API operation request will return S3 Glacier Flexible Retrieval or
S3 Glacier Deep Archive as the storage class.)

###### Note

When you restore an archive, you are paying for both the archive
(S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive rate) and a
copy that you restored temporarily (S3 Standard storage rate). For
information about pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

You can restore an object copy programmatically or by using the Amazon S3 console.
Amazon S3 processes only one restore request at a time per object. For more
information, see [Restoring an archived object](restoring-objects.md "restoring-objects.md").
