# Creating a general purpose bucket

To upload your data to Amazon S3, you must first create an Amazon S3 general purpose bucket in one of the AWS Regions. The
AWS account that creates the bucket owns it. When you create a bucket, you must choose a bucket name and
Region. During the creation process, you can optionally choose other storage management options for the
bucket.

###### Important

After you create a bucket, you can't change the bucket name, the bucket owner, or the Region. For
more information about bucket naming, see [General purpose bucket naming rules](bucketnamingrules.md "bucketnamingrules.md").

By default, you can create up to 10,000 general purpose buckets
per AWS account. To request a quota increase for general purpose buckets,
visit the [Service Quotas
console](https://console.aws.amazon.com/servicequotas/home/services/s3/quotas/ "https://console.aws.amazon.com/servicequotas/home/services/s3/quotas/").

You can store any number of objects in a bucket. For a list of restriction and limitations related
to Amazon S3 general purpose buckets, see [General purpose bucket quotas, limitations, and restrictions](BucketRestrictions.md "BucketRestrictions.md").

## General purpose bucket settings

When you're creating a general purpose bucket, you can use the following settings to control various aspects of your
bucket's behavior:

- **S3 Object Ownership** – S3 Object Ownership is an Amazon S3
  bucket-level setting that you can use both to control ownership of objects that are uploaded to your
  bucket and to disable or enable access control lists (ACLs). By default, Object Ownership is set to
  the Bucket owner enforced setting, and all ACLs are disabled. With ACLs disabled, the bucket owner
  owns every object in the bucket and manages access to data exclusively by using policies. For more
  information, see [Controlling ownership of objects and disabling ACLs
  for your bucket](about-object-ownership.md "about-object-ownership.md").
- **S3 Object Lock** – S3 Object Lock can help prevent
  Amazon S3 objects from being deleted or overwritten for a fixed amount of time or indefinitely.
  Object Lock uses a _write-once-read-many_ (WORM) model to store
  objects. You can use Object Lock to help meet regulatory requirements that require WORM storage, or
  to add another layer of protection against object changes or deletion. For more information, see
  [Locking objects with Object Lock](object-lock.md "object-lock.md").

After you create a general purpose bucket, or when you're creating a general purpose bucket by using the Amazon S3 console, you can also
use the following settings to control other aspects of your bucket's behavior:

- **S3 Block Public Access** – The S3 Block Public Access
  feature provides settings for access points, buckets, and accounts to help you manage public access to
  Amazon S3 resources. By default, new buckets, access points, and objects don't allow public access.
  However, users can modify bucket policies, access point policies, or object permissions to allow
  public access. S3 Block Public Access settings override these policies and permissions so that you can
  limit public access to these resources. For more information, see [Blocking public access to your Amazon S3
  storage](access-control-block-public-access.md "access-control-block-public-access.md").
- **S3 Versioning** – Versioning is a means of keeping multiple
  variants of an object in the same bucket. You can use versioning to preserve, retrieve, and restore
  every version of every object stored in your bucket. With versioning, you can easily recover from both
  unintended user actions and application failures. By default, versioning is disabled for buckets. For
  more information, see [Retaining multiple versions of objects with S3 Versioning](Versioning.md "Versioning.md").
- **Default encryption** – You can set the default encryption type for all
  objects in your bucket. Server-side encryption with Amazon S3 managed keys (SSE-S3) is the base level of
  encryption configuration for every bucket in Amazon S3. All new objects uploaded to an S3 bucket are
  automatically encrypted with SSE-S3 as the base level of encryption. If you want to use a different
  type of default encryption, you can specify server-side encryption with AWS Key Management Service (AWS KMS) keys
  (SSE-KMS), dual-layer server-side encryption with AWS KMS keys (DSSE-KMS), or server-side encryption
  with customer-provided keys (SSE-C) to encrypt your data. For more information, see [Setting default server-side encryption behavior for Amazon S3
  buckets](bucket-encryption.md "bucket-encryption.md").
  You can use the Amazon S3 console, Amazon S3 REST API, AWS Command Line Interface (AWS CLI), or AWS SDKs to create a general purpose bucket.
  For more information about the permissions required to create a general purpose bucket, see [CreateBucket](../API/API_CreateBucket.md "../API/API_CreateBucket.md") in the
  _Amazon Simple Storage Service API Reference_.

If you're having trouble creating an Amazon S3 bucket, see [How do I troubleshoot errors when
creating an Amazon S3 bucket?](https://repost.aws/knowledge-center/s3-create-bucket-errors "https://repost.aws/knowledge-center/s3-create-bucket-errors") on AWS re:Post.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the currently displayed AWS Region. Next, choose the Region in which you want to create a bucket.

###### Note

    * After you create a bucket, you can't change its Region.
    * To minimize latency and costs and address regulatory requirements, choose a Region close to
     you. Objects stored in a Region never leave that Region unless you explicitly transfer them to
     another Region. For a list of Amazon S3 AWS Regions, see [AWS service endpoints](../../../general/latest/gr/rande.md#s3_region "../../../general/latest/gr/rande.md#s3_region") in the *Amazon Web Services General Reference*.

3. In the left navigation pane, choose **General purpose buckets**.
4. Choose **Create bucket**. The **Create bucket** page opens.
5. For **Bucket name**, enter a name for your bucket.

The bucket name must:

    * Be unique within a partition. A partition is a grouping of Regions. AWS currently has
     three partitions: `aws` (commercial Regions), `aws-cn` (China Regions), and
     `aws-us-gov` (AWS GovCloud (US) Regions).
    * Be between 3 and 63 characters long.
    * Consist only of lowercase letters, numbers, periods (`.`), and hyphens
     (`-`). For best compatibility, we recommend that you avoid using periods
     (`.`) in bucket names, except for buckets that are used only for static website
     hosting.
    * Begin and end with a letter or number.
    * For a complete list of bucket-naming rules, see [General purpose bucket naming rules](bucketnamingrules.md "bucketnamingrules.md").

###### Important

    * After you create the bucket, you can't change its name.
    * Don't include sensitive information in the bucket name. The bucket name is visible in the URLs
     that point to the objects in the bucket.

6. (Optional) Under **General configuration**, you can choose to copy an existing
   bucket's settings to your new bucket. If you don't want to copy the settings of an existing bucket, skip
   to the next step.

###### Note

This option:

    * Isn't available in the AWS CLI and is only available in the Amazon S3 console
    * Doesn't copy the bucket policy from the existing bucket to the new bucket

To copy an existing bucket's settings, under **Copy settings from existing
bucket**, select **Choose bucket**. The **Choose bucket**
window opens. Find the bucket with the settings that you want to copy, and select **Choose
bucket**. The **Choose bucket** window closes, and the **Create
bucket** window reopens.

Under **Copy settings from existing bucket**, you now see the name of the
bucket that you selected. The settings of your new bucket now match the settings of the bucket that you
selected. If you want to remove the copied settings, choose **Restore defaults**.
Review the remaining bucket settings on the **Create bucket** page. If you don't want
to make any changes, you can skip to the final step. 7. Under **Object Ownership**, to disable or enable ACLs and control
ownership of objects uploaded in your bucket, choose one of the following
settings:

###### ACLs disabled

    * **Bucket owner enforced (default)** –
     ACLs are disabled, and the bucket owner automatically owns and has full control over every object in the general purpose bucket. ACLs
     no longer affect access permissions to data in the S3 general purpose bucket. The bucket uses policies exclusively to define access control.


    By default, ACLs are disabled. A majority of modern use cases in Amazon S3 no
     longer require the use of ACLs. We recommend that you keep ACLs disabled, except
     in circumstances where you must control access for each object
     individually. For more information, see [Controlling ownership of objects and disabling ACLs
     for your bucket](about-object-ownership.md "about-object-ownership.md").

###### ACLs enabled

    * **Bucket owner preferred** – The bucket owner owns and
     has full control over new objects that other accounts write to the bucket with
     the `bucket-owner-full-control` canned ACL.


    If you apply the **Bucket owner preferred** setting, to
     require all Amazon S3 uploads to include the `bucket-owner-full-control`
     canned ACL, you can [add a
     bucket policy](ensure-object-ownership.md#ensure-object-ownership-bucket-policy "ensure-object-ownership.md#ensure-object-ownership-bucket-policy") that allows only object uploads that use this
     ACL.
    * **Object writer** – The AWS account that uploads an
     object owns the object, has full control over it, and can grant other users
     access to it through ACLs.

###### Note

The default setting is **Bucket owner enforced**. To apply the
default setting and keep ACLs disabled, only the `s3:CreateBucket`
permission is needed. To enable ACLs, you must have the
`s3:PutBucketOwnershipControls` permission. 8. Under **Block Public Access settings for this bucket**, choose the
Block Public Access settings that you want to apply to the bucket.

By default, all four Block Public Access settings are enabled. We recommend that you
keep all settings enabled, unless you know that you need to turn off one or more of them
for your specific use case. For more information about blocking public access, see [Blocking public access to your Amazon S3
storage](access-control-block-public-access.md "access-control-block-public-access.md").

###### Note

To enable all Block Public Access settings, only the `s3:CreateBucket` permission
is required. To turn off any Block Public Access settings, you must have the
`s3:PutBucketPublicAccessBlock` permission. 9. (Optional) By default, **Bucket Versioning** is disabled. Versioning is a means
of keeping multiple variants of an object in the same bucket. You can use versioning to preserve,
retrieve, and restore every version of every object stored in your bucket. With versioning, you can
recover more easily from both unintended user actions and application failures. For more information
about versioning, see [Retaining multiple versions of objects with S3 Versioning](Versioning.md "Versioning.md").

To enable versioning on your bucket, choose **Enable**. 10. (Optional) Under **Tags**, you can choose to add tags to your bucket. With
AWS cost allocation, you can use bucket tags to annotate billing for your use of a bucket. A tag is a
key-value pair that represents a label that you assign to a bucket. For more information, see [Using cost allocation S3 bucket tags](CostAllocTagging.md "CostAllocTagging.md").

To add a bucket tag, enter a **Key** and optionally a
**Value** and choose **Add Tag**. 11. To configure **Default encryption**, under **Encryption type**,
choose one of the following:

    * **Server-side encryption with Amazon S3 managed keys (SSE-S3)**
    * **Server-side encryption with AWS Key Management Service keys (SSE-KMS)**
    * **Dual-layer server-side encryption with AWS Key Management Service (AWS KMS) keys
     (DSSE-KMS)**


    ###### Important

    If you use the SSE-KMS or DSSE-KMS option for your default encryption configuration, you are
     subject to the requests per second (RPS) quota of AWS KMS. For more information about AWS KMS quotas
     and how to request a quota increase, see [Quotas](../../../kms/latest/developerguide/limits.md "../../../kms/latest/developerguide/limits.md") in
     the *AWS Key Management Service Developer Guide*.

Buckets and new objects are encrypted by using server-side encryption with Amazon S3 managed keys
(SSE-S3) as the base level of encryption configuration. For more information about default encryption,
see [Setting default server-side encryption behavior for Amazon S3
buckets](bucket-encryption.md "bucket-encryption.md"). For more information about
SSE-S3, see [Using server-side encryption with Amazon S3 managed keys
(SSE-S3)](UsingServerSideEncryption.md "UsingServerSideEncryption.md").

For more information about using server-side encryption to encrypt your data, see [Protecting data with encryption](UsingEncryption.md "UsingEncryption.md"). 12. If you chose **Server-side encryption with AWS Key Management Service keys (SSE-KMS)** or
**Dual-layer server-side encryption with AWS Key Management Service (AWS KMS) keys (DSSE-KMS)**, do the
following:

    1. Under **AWS KMS key**, specify your KMS key in one of the following ways:




    	* To choose from a list of available KMS keys, choose **Choose from
    	 your AWS KMS keys**, and choose your
    	 **KMS key** from the list of available keys.


    	Both the AWS managed key (`aws/s3`) and your customer managed keys appear in this
    	 list. For more information about customer managed keys, see [Customer keys and
    	 AWS keys](../../../kms/latest/developerguide/concepts.md#key-mgmt "../../../kms/latest/developerguide/concepts.md#key-mgmt") in the *AWS Key Management Service Developer Guide*.
    	* To enter the KMS key ARN, choose **Enter AWS KMS key
    	 ARN**, and enter your KMS key ARN in the field that appears.
    	* To create a new customer managed key in the AWS KMS console, choose **Create a
    	 KMS key**.


    	For more information about creating an AWS KMS key, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the *AWS Key Management Service Developer Guide*.
    ###### Important

    You can use only KMS keys that are available in the same AWS Region as the bucket. The
     Amazon S3 console lists only the first 100 KMS keys in the same Region as the bucket. To use a
     KMS key that isn't listed, you must enter your KMS key ARN. If you want to use a KMS key
     that's owned by a different account, you must first have permission to use the key, and then you
     must enter the KMS key ARN. For more information about cross account permissions for KMS keys,
     see [Creating KMS keys that other accounts can use](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md#cross-account-console "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md#cross-account-console") in the
     *AWS Key Management Service Developer Guide*. For more information about SSE-KMS, see [Specifying server-side encryption with AWS KMS
     (SSE-KMS)](specifying-kms-encryption.md "specifying-kms-encryption.md"). For more
     information about DSSE-KMS, see [Using dual-layer server-side encryption with AWS KMS keys
     (DSSE-KMS)](UsingDSSEncryption.md "UsingDSSEncryption.md").

    When you use an AWS KMS key for server-side encryption in Amazon S3, you must
     choose a symmetric encryption KMS key. Amazon S3 supports only symmetric encryption KMS keys and not
     asymmetric KMS keys. For more information, see [Identifying symmetric and
     asymmetric KMS keys](../../../kms/latest/developerguide/find-symm-asymm.md "../../../kms/latest/developerguide/find-symm-asymm.md") in the *AWS Key Management Service Developer Guide*.
    2. When you configure your bucket to use default encryption with SSE-KMS, you can also use S3 Bucket Keys.
     S3 Bucket Keys lower the cost of encryption by decreasing request traffic from Amazon S3 to AWS KMS. For more
     information, see [Reducing the cost of SSE-KMS with Amazon S3 Bucket Keys](bucket-key.md "bucket-key.md"). S3 Bucket Keys aren't
     supported for DSSE-KMS.


    By default, S3 Bucket Keys are enabled in the Amazon S3 console. We recommend leaving S3 Bucket Keys enabled to
     lower your costs. To disable S3 Bucket Keys for your bucket, under **Bucket Key**, choose
     **Disable**.

13. (Optional) S3 Object Lock helps protect new objects from being deleted or overwritten. For
    more information, see [Locking objects with Object Lock](object-lock.md "object-lock.md"). If you want to enable
    S3 Object Lock, do the following:
    1.  Choose **Advanced settings**.

    ###### Important

    Enabling Object Lock automatically enables versioning for the bucket. After you've
    enabled and successfully created the bucket, you must also configure the Object Lock default
    retention and legal hold settings on the bucket's **Properties** tab. 2. If you want to enable Object Lock, choose
    **Enable**, read the warning that appears, and acknowledge it.###### Note

To create an Object Lock enabled bucket, you must have the following permissions:
`s3:CreateBucket`, `s3:PutBucketVersioning`, and
`s3:PutBucketObjectLockConfiguration`. 14. Choose **Create bucket**.
When you use the AWS SDKs to create a general purpose bucket, you must create a client and then use the
client to send a request to create a bucket. As a best practice, you should create your client and
bucket in the same AWS Region. If you don't specify a Region when you create a client or a bucket,
Amazon S3 uses the default Region, US East (N. Virginia). If you want to constrain the bucket creation to a
specific AWS Region, use the [LocationConstraint](../API/API_CreateBucketConfiguration.md "../API/API_CreateBucketConfiguration.md") condition key.

To create a client to access a dual-stack endpoint, you must specify an AWS Region. For
more information, see [Using Amazon S3
dual-stack endpoints](../API/dual-stack-endpoints.md#dual-stack-endpoints-description "../API/dual-stack-endpoints.md#dual-stack-endpoints-description") in the _Amazon S3 API Reference_. For a list of
available AWS Regions, see [Amazon Simple Storage Service
endpoints and quotas](../../../general/latest/gr/s3.md "../../../general/latest/gr/s3.md") in the _AWS General Reference_.

When you create a client, the Region maps to the Region-specific endpoint. The
client uses this endpoint to communicate with Amazon S3:
`s3.`region`.amazonaws.com`. If your
Region launched after March 20, 2019, your client and bucket must be in the same
Region. However, you can use a client in the US East (N. Virginia) Region to create a bucket in
any Region that launched before March 20, 2019. For more information, see [Legacy endpoints](VirtualHosting.md#s3-legacy-endpoints "VirtualHosting.md#s3-legacy-endpoints").

These AWS SDK code examples perform the following tasks:

- **Create a client by explicitly specifying an
  AWS Region** – In the example, the client uses the
  `s3.us-west-2.amazonaws.com` endpoint to communicate with
  Amazon S3. You can specify any AWS Region. For a list of AWS Regions, see
  [Regions and
  endpoints](../../../general/latest/gr/s3.md "../../../general/latest/gr/s3.md") in the _AWS General Reference_.
- **Send a create bucket request by specifying only a
  bucket name** – The client sends a request to Amazon S3 to
  create the bucket in the Region where you created a client.
- **Retrieve information about the location of the
  bucket** – Amazon S3 stores bucket location information in the
  _location_ subresource that's associated with the bucket.
  For additional AWS SDK examples and examples in other languages, see [Use
  CreateBucket with an AWS SDK or CLI](../API/s3_example_s3_CreateBucket_section.md "../API/s3_example_s3_CreateBucket_section.md") in the _Amazon Simple Storage Service API Reference_.

Java
For examples of how to create a bucket with the AWS SDK for Java, see [Create a bucket](../API/s3_example_s3_CreateBucket_section.md "../API/s3_example_s3_CreateBucket_section.md") in the _Amazon S3 API Reference_.

When using the AWS SDK for Java v2, you can create a general purpose bucket with a globally unique identifier (GUID) appended to the bucket name to ensure uniqueness. Use `UUID.randomUUID().toString().replace("-", "")` to generate a GUID and concatenate it with your base bucket name. This approach helps avoid bucket naming conflicts across all AWS accounts.

.NET
For information about how to create and test a working sample, see the [AWS SDK for .NET Version 3 API
Reference](../../../sdkfornet/v3/apidocs/Index.md "../../../sdkfornet/v3/apidocs/Index.md").

```
using Amazon;
using Amazon.S3;
using Amazon.S3.Model;
using Amazon.S3.Util;
using System;
using System.Threading.Tasks;

namespace Amazon.DocSamples.S3
{
    class CreateBucketTest
    {
        private const string bucketName = "*** bucket name ***";
        // Specify your bucket region (an example region is shown).
        private static readonly RegionEndpoint bucketRegion = RegionEndpoint.USWest2;
        private static IAmazonS3 s3Client;
        public static void Main()
        {
            s3Client = new AmazonS3Client(bucketRegion);
            CreateBucketAsync().Wait();
        }

        static async Task CreateBucketAsync()
        {
            try
            {
                if (!(await AmazonS3Util.DoesS3BucketExistAsync(s3Client, bucketName)))
                {
                    var putBucketRequest = new PutBucketRequest
                    {
                        BucketName = bucketName,
                        UseClientRegion = true
                    };

                    PutBucketResponse putBucketResponse = await s3Client.PutBucketAsync(putBucketRequest);
                }
                // Retrieve the bucket location.
                string bucketLocation = await FindBucketLocationAsync(s3Client);
            }
            catch (AmazonS3Exception e)
            {
                Console.WriteLine("Error encountered on server. Message:'{0}' when writing an object", e.Message);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unknown encountered on server. Message:'{0}' when writing an object", e.Message);
            }
        }
        static async Task<string> FindBucketLocationAsync(IAmazonS3 client)
        {
            string bucketLocation;
            var request = new GetBucketLocationRequest()
            {
                BucketName = bucketName
            };
            GetBucketLocationResponse response = await client.GetBucketLocationAsync(request);
            bucketLocation = response.Location.ToString();
            return bucketLocation;
        }
    }
}

```

Ruby
For information about how to create and test a working sample, see the [AWS SDK for Ruby - Version 3](../../../sdk-for-ruby/v3/api.md "../../../sdk-for-ruby/v3/api.md").

```
require 'aws-sdk-s3'

# Wraps Amazon S3 bucket actions.
class BucketCreateWrapper
  attr_reader :bucket

  # @param bucket [Aws::S3::Bucket] An Amazon S3 bucket initialized with a name. This is a client-side object until
  #                                 create is called.
  def initialize(bucket)
    @bucket = bucket
  end

  # Creates an Amazon S3 bucket in the specified AWS Region.
  #
  # @param region [String] The Region where the bucket is created.
  # @return [Boolean] True when the bucket is created; otherwise, false.
  def create?(region)
    @bucket.create(create_bucket_configuration: { location_constraint: region })
    true
  rescue Aws::Errors::ServiceError => e
    puts "Couldn't create bucket. Here's why: #{e.message}"
    false
  end

  # Gets the Region where the bucket is located.
  #
  # @return [String] The location of the bucket.
  def location
    if @bucket.nil?
      'None. You must create a bucket before you can get its location!'
    else
      @bucket.client.get_bucket_location(bucket: @bucket.name).location_constraint
    end
  rescue Aws::Errors::ServiceError => e
    "Couldn't get the location of #{@bucket.name}. Here's why: #{e.message}"
  end
end

# Example usage:
def run_demo
  region = "us-west-2"
  wrapper = BucketCreateWrapper.new(Aws::S3::Bucket.new("amzn-s3-demo-bucket-#{Random.uuid}"))
  return unless wrapper.create?(region)

  puts "Created bucket #{wrapper.bucket.name}."
  puts "Your bucket's region is: #{wrapper.location}"
end

run_demo if $PROGRAM_NAME == __FILE__

```

The following AWS CLI example creates a general purpose bucket in the US West (N. California) Region
(`us-west-1`) Region with an example bucket name that uses a globally
unique identifier (GUID). To use this example command, replace the `user input placeholders`
with your own information.

```
aws s3api create-bucket \
    --bucket `amzn-s3-demo-bucket1`$(uuidgen | tr -d - | tr '[:upper:]' '[:lower:]' ) \
    --region `us-west-1` \
    --create-bucket-configuration LocationConstraint=`us-west-1`
```

For more information and additional examples, see [create-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html") in the _AWS CLI Command Reference_.
