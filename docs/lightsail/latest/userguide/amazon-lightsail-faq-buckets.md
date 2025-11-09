# Object storage and buckets

## What can I do with Lightsail object

storage?

You can store your static content, such as images, videos, and HTML files in a bucket in
the Lightsail object storage service. You can use the objects stored in your bucket with
your websites and applications. Lightsail object storage can be associated to your
Lightsail CDN distribution with a few simple clicks, making it quick and easy to
accelerate the delivery of your content to a global audience. It can also be used as a low
cost, secure backup solution. For more information, see [Object storage](buckets-in-amazon-lightsail.md "buckets-in-amazon-lightsail.md").

## What does Lightsail object storage cost?

Lightsail object storage has three different fixed-priced bundles in all AWS Regions
where Lightsail is available. The first bundle is $1/month and is free for the first 12
months. This bundle includes 5 GB storage capacity and 25 GB of data transfer. The second
bundle is $3 per month and includes 100 GB storage capacity and 250 GB of data transfer.
Lastly, the third bundle is $5 per month and includes 250 GB of storage capacity and 500 GB
data transfer. Lightsail object storage includes unlimited data transfer into your bucket,
as the bundled data transfer allowance is used only for data transfer out from your
bucket.

## Can I change the plan associated with my Lightsail

bucket?

Yes, you can change the storage plan of an individual Lightsail bucket one time within
your monthly AWS billing cycle.

## Can I copy objects from Lightsail object

storage to Amazon S3?

Yes, copying from Lightsail object storage to Amazon S3 is supported. For more information,
see [How
can I copy all objects from one Amazon S3 bucket to another bucket?](https://aws.amazon.com/premiumsupport/knowledge-center/move-objects-s3-bucket/ "https://aws.amazon.com/premiumsupport/knowledge-center/move-objects-s3-bucket/") in the
_AWS Premium Support Knowledge Center_.

## How do I get started with Lightsail object

storage?

To use Lightsail object storage, you must first create a bucket that is used to store
your data. For more information, see [Create a bucket](amazon-lightsail-creating-buckets.md "amazon-lightsail-creating-buckets.md"). After your bucket is up and running, you can start adding objects
to your bucket by uploading files using the Lightsail console or by configuring your
application to put content like logs or other application data in the bucket. Alternatively,
you can also get started with Lightsail object storage through the use of AWS Command Line Interface
(AWS CLI).

## How do I upload objects to my

bucket?

To upload object(s) to your bucket, like images or other static files, choose “Upload”
from the “Objects” top navigation tab and select the correct filed or directory from your
computer. Alternately, drag and drop files and directories from your desktop into the marked
area in the Lightsail object storage console.

## Can I block public access to my bucket?

Lightsail buckets and objects are set to private by default, meaning that only users
with appropriate permissions have access to the bucket and objects. A user can change this
default setting and either make individual objects public and read only in a private bucket
or opt to make the entire bucket public and read only. When a user makes a bucket or object
public, anyone in the world can read its content. For more information, see [Bucket
permissions](amazon-lightsail-understanding-bucket-permissions.md "amazon-lightsail-understanding-bucket-permissions.md").

## How do I provide programmatic access to my

bucket?

You can use either access keys or roles for programmatic access to your bucket. First,
select the bucket you want to programmatically connect to in the Lightsail console.
Second, under the **Permissions** tab, create an access key or assign a
role to your Lightsail instance and then configure your website or application code to use
your bucket. This behavior may vary depending on how you plan to use object storage with
your website or application. For more information, see [Bucket
permissions](amazon-lightsail-understanding-bucket-permissions.md "amazon-lightsail-understanding-bucket-permissions.md").

## How do I share a bucket with other AWS

accounts?

Lightsail makes cross-account sharing easy by allowing you to share access to your
bucket with the AWS account ID that you specify in the Cross-account access section of the
bucket management page. After you specify an AWS account ID, that account will have
read-only access to the bucket. For more information, see [Bucket
permissions](amazon-lightsail-understanding-bucket-permissions.md "amazon-lightsail-understanding-bucket-permissions.md").

## What is versioning?

Versioning allows you to preserve, retrieve, and restore every version of every object
storage in your bucket, providing an additional level of protection from accidental
overwrites and deletes.. For more information, see [Enable and suspend bucket
object versioning](amazon-lightsail-managing-bucket-object-versioning.md "amazon-lightsail-managing-bucket-object-versioning.md").

## How do I associate my Lightsail bucket to my

Lightsail CDN distribution?

Lightsail object storage can be associated to Lightsail CDN distributions with a few
simple clicks, making it quick and easy to accelerate the delivery of your content to a
global audience. To do so, create a Lightsail CDN distribution and simply select the
Lightsail bucket as the origin of your Lightsail CDN distribution. For more information,
see [Using an Amazon
Lightsail bucket with a Lightsail content delivery network distribution](amazon-lightsail-using-distributions-with-buckets.md "amazon-lightsail-using-distributions-with-buckets.md").

## What limits are there for the Lightsail

object storage service?

You can create up to 20 buckets in the Lightsail object storage service per account.
There is no limit to the number of objects that you can store in a bucket. You can store all
of your objects in a single bucket, or you can organize them across several buckets.

## Does Lightsail object storage support

monitoring and alerting?

With Lightsail object storage, customers can easily view metrics on the total used
space within a bucket and number of objects within the bucket. Alerting based on these
metrics is also supported. For more information, see [Viewing metrics for your bucket in
Amazon Lightsail](amazon-lightsail-viewing-bucket-metrics.md "amazon-lightsail-viewing-bucket-metrics.md") and [Create bucket metric alarms](amazon-lightsail-adding-bucket-metric-alarms.md "amazon-lightsail-adding-bucket-metric-alarms.md").
