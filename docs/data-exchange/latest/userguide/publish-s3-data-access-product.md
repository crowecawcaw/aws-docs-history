# Publishing a product in AWS Data Exchange

containing Amazon S3 data access

With AWS Data Exchange for Amazon S3, providers can share direct access to Amazon S3 buckets or specific
prefixes and Amazon S3 objects. Providers also use AWS Data Exchange to automatically manage
subscriptions, entitlements, billing, and payments.

As a data provider, you can share direct access to an entire Amazon S3 bucket or specific
prefixes and Amazon S3 objects without creating or managing copies. These shared
Amazon S3 objects can be server-side encrypted with customer managed keys stored in
AWS Key Management Service (AWS KMS) or with AWS managed keys (SSE-S3). For more information about
monitoring your KMS keys and understanding encryption contexts, see [Key management for Amazon S3 data access](key-management.md "key-management.md"). When a customer subscribes to your data products, AWS Data Exchange
automatically provisions an Amazon S3 access point and updates its resource policies on your
behalf to grant subscribers read-only access. Subscribers can use the Amazon S3 access point
aliases in places where they use Amazon S3 bucket names to access data in Amazon S3.

When the subscription ends, the subscriber’s permissions are revoked. If you choose to
end an agreement with a subscriber early, contact [AWS Support](https://console.aws.amazon.com/support/home#/case/create%3FissueType=customer-service "https://console.aws.amazon.com/support/home#/case/create%3FissueType=customer-service"). You can add terms of subscriptions in the Data Subscription
Agreement (DSA).

Before you can publish a product containing Amazon S3 data access, you must meet the
following prerequisites:

###### Prerequisites

- Confirm that the Amazon S3 buckets hosting the data are configured with the Amazon S3
  bucket owner enforced setting turned on **ACLs Disabled**. For
  more information, see [Controlling
  ownership of objects and disabling ACLs for your bucket](../../../AmazonS3/latest/userguide/about-object-ownership.md "../../../AmazonS3/latest/userguide/about-object-ownership.md") in the
  _Amazon Simple Storage Service User Guide_.
- Your shared objects must be in the Amazon S3 Standard Storage class, or be managed
  using S3 Intelligent Tiering, for subscribers to access them successfully. If
  they’re in other storage classes, or if you have enabled Intelligent Tiering
  with Deep Archive, your subscribers will receive errors because they won’t have
  permission to
  `RestoreObject`.
- Confirm that the Amazon S3 buckets hosting the data has encryption disabled or
  encrypted with Amazon S3 managed keys (SSE-S3) or customer managed keys stored in AWS Key Management Service
  (AWS KMS).
- If you're using customer managed keys, you must have the following:

      1. IAM permissions to `kms:CreateGrant` on the KMS keys.
       You can access these permissions through the key policy, IAM
       credentials, or through an AWS KMS grant on the KMS key. For more
       information about key management and understanding how AWS Data Exchange uses AWS
       KMS grants, see [Creating AWS KMS grants](key-management.md#create-kms-grants "key-management.md#create-kms-grants").


      To provide access, add permissions to your users, groups, or roles:




      	+ Users and groups in AWS IAM Identity Center:


      	Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the *AWS IAM Identity Center User Guide*.
      	+ Users managed in IAM through an identity provider:


      	Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
      	 in the *IAM User Guide*.
      	+ IAM users:




      		- Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the *IAM User Guide*.
      		- (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the *IAM User Guide*.
      Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.


      To grant users programmatic access, choose one of the following options.




      | Which user needs programmatic access? | To | By |
      | --- | --- | --- |
      | IAM | (Recommended) Use console credentials as temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br>+ For the AWS CLI, see [Login for AWS local development](../../../cli/latest/userguide/cli-configure-sign-in.md "../../../cli/latest/userguide/cli-configure-sign-in.md") in<br>the *AWS Command Line Interface User Guide*.<br>+ For AWS SDKs, see [Login for AWS local development](../../../sdkref/latest/guide/access-login.md "../../../sdkref/latest/guide/access-login.md") in the<br>*AWS SDKs and Tools Reference Guide*. |
      | Workforce identity<br>(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs. | Following the instructions for the interface that you want to use.<br>+ For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the<br>*AWS Command Line Interface User Guide*.<br>+ For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center<br>authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the *AWS SDKs and Tools Reference Guide*. |
      | IAM | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs. | Following the instructions in [Using temporary<br>credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the *IAM User Guide*. |
      | IAM | (Not recommended)Use long-term credentials to sign programmatic requests<br>to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br>+ For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in<br>the *AWS Command Line Interface User Guide*.<br>+ For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the<br>*AWS SDKs and Tools Reference Guide*.<br>+ For AWS APIs, see [Managing access keys for<br>IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the *IAM User Guide*. |


      Following is an example JSON policy that shows how you could add to
       the key policy of the KMS key.



      ```

      {
            "Sid": "AllowCreateGrantPermission",
            "Effect": "Allow",
            "Principal": {
      "AWS": "<IAM identity who will call Dataexchange API>"
            },
            "Action": "kms:CreateGrant",
            "Resource": "*"
      }

      ```

      The following policy shows an example policy addition for the IAM
       identity that is used.



      JSON





      ```
      `{
       "Version":"2012-10-17",
       "Statement": [
       {
       "Effect": "Allow",
       "Sid": "AllowCreateGrantPermission",
       "Action": [
       "kms:CreateGrant"
       ],
       "Resource": [
       "arn:aws:kms:`us-east-1`:`111122223333`:key/`KeyId`"
       ]
       }
       ]
      }`

      ```





      ###### Note

      Cross account KMS keys are also permitted if the
       `kms:CreateGrant` permission on the KMS keys are
       obtained through the earlier step. If another account owns the key,
       you must have permissions on the key policy and your IAM
       credentials as detailed in the above examples.
      2. Make sure to use KMS keys to encrypt existing and new objects in the
       Amazon S3 bucket using the Amazon S3 bucket key feature.
       For more details, see [Configuring S3 Bucket Keys](../../../AmazonS3/latest/userguide/bucket-key.md#configure-bucket-key "../../../AmazonS3/latest/userguide/bucket-key.md#configure-bucket-key") in the *Amazon Simple Storage Service User Guide*.




      	+ For new objects added to your Amazon S3 bucket, you
      	 can set up Amazon S3 bucket key encryption by default.
      	 If existing objects have been encrypted without using the
      	 Amazon S3bucket key feature, these objects must be
      	 migrated to use the Amazon S3 bucket key for encryption.


      	To enable the Amazon S3 bucket key for existing
      	 objects, use the `copy` operation. For more
      	 information, see [Configuring an Amazon S3 bucket key at the object
      	 level using batch operations](../../../AmazonS3/latest/userguide/configuring-bucket-key-object.md "../../../AmazonS3/latest/userguide/configuring-bucket-key-object.md").
      	+ AWS managed KMS keys or AWS owned keys aren't supported.
      	 You can migrate from an unsupported encryption scheme to the
      	 ones currently supported. For more information, see [Changing your Amazon S3 encryption](https://aws.amazon.com/blogs/storage/changing-your-amazon-s3-encryption-from-s3-managed-encryption-sse-s3-to-aws-key-management-service-sse-kms/ "https://aws.amazon.com/blogs/storage/changing-your-amazon-s3-encryption-from-s3-managed-encryption-sse-s3-to-aws-key-management-service-sse-kms/") at the AWS Storage
      	 Blog.
      3. Set the Amazon S3 buckets hosting the data to trust AWS Data Exchange owned access
       points. You must update these Amazon S3 bucket policies to give AWS Data Exchange
       permissions to create Amazon S3 access points and grant or remove
       subscribers' access on your behalf. If the policy statement is missing,
       you must edit the bucket policy to add the Amazon S3 locations
       to your data set.


      An example policy is shown below. Replace `<Bucket ARN>`
       with the appropriate value.



      JSON





      ```
      `{
       "Version":"2012-10-17",
       "Statement": [
       {
       "Effect": "Allow",
       "Principal": {
       "AWS": "*"
       },
       "Action": [
       "s3:GetObject",
       "s3:ListBucket"
       ],
       "Resource": [
       "arn:aws:s3:::`BucketName`",
       "arn:aws:s3:::/*"
       ],
       "Condition": {
       "StringEquals": {
       "s3:DataAccessPointAccount": [
       "337040091392",
       "504002150500",
       "366362662752",
       "330489627928",
       "291973504423",
       "461002523379",
       "036905324694",
       "540564263739",
       "675969394711",
       "108584782536",
       "844053218156"
       ]
       }
       }
       }
       ]
      }`

      ```

  You can delegate data sharing through AWS Data Exchange to an entire Amazon S3 bucket. However, you
  can scope delegation to the specific prefixes and objects of the bucket that you want to
  share in the data set. Following is an example of a scoped policy. Replace
  `<Bucket ARN>` and `"mybucket/folder1/*"` with your own
  information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DelegateToAdxGetObjectsInFolder1",
 "Effect": "Allow",
 "Principal": {
 "AWS": "*"
 },
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::mybucket/folder1/*"
 ],
 "Condition": {
 "StringEquals": {
 "s3:DataAccessPointAccount": [
 "337040091392",
 "504002150500",
 "366362662752",
 "330489627928",
 "291973504423",
 "461002523379",
 "036905324694",
 "540564263739",
 "675969394711",
 "108584782536",
 "844053218156"
 ]
 }
 }
 },
 {
 "Sid": "DelegateToAdxListObjectsInFolder1",
 "Effect": "Allow",
 "Principal": {
 "AWS": "*"
 },
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:::mybucket",
 "Condition": {
 "StringLike": {
 "s3:prefix": [
 "folder1/*"
 ]
 },
 "StringEquals": {
 "s3:DataAccessPointAccount": [
 "337040091392",
 "504002150500",
 "366362662752",
 "330489627928",
 "291973504423",
 "461002523379",
 "036905324694",
 "540564263739",
 "675969394711",
 "108584782536",
 "844053218156"
 ]
 }
 }
 }
 ]
}`

```

Similarly, to scope access to only a single file, a provider can use the following
policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DelegateToAdxGetMyFile",
 "Effect": "Allow",
 "Principal": {
 "AWS": "*"
 },
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::mybucket/folder1/myfile"
 ],
 "Condition": {
 "StringEquals": {
 "s3:DataAccessPointAccount": [
 "337040091392",
 "504002150500",
 "366362662752",
 "330489627928",
 "291973504423",
 "461002523379",
 "036905324694",
 "540564263739",
 "675969394711",
 "108584782536",
 "844053218156"
 ]
 }
 }
 }
 ]
}`

```

The following topics describe the process of creating an Amazon S3 data set and publishing
a new product with Amazon S3 data sets using the AWS Data Exchange console. The process has the following
steps:

###### Steps

- [Step 1: Create an Amazon S3 data set](#create-S3-data-set "#create-S3-data-set")
- [Step 2: Configure Amazon S3 data
  access](#configure-s3-data-access-product "#configure-s3-data-access-product")
- [Step 3: Review and finalize
  the data set](#review-finalize-s3-data-set-product "#review-finalize-s3-data-set-product")
- [Step 4: Add an Amazon S3 data set
  to an AWS Data Exchange product](#add-s3-data-set-to-existing-product "#add-s3-data-set-to-existing-product")
- [Step 5: Publish a new product containing access
  to Amazon S3](#publish-s3-product "#publish-s3-product")
- [Step 6: (Optional) Copy a product](#copy-s3-product "#copy-s3-product")

## Step 1: Create an Amazon S3 data set

###### To create an Amazon S3 data set

1. On the left side navigation pane, under **Publish
   data**, choose **Owned data sets**.
2. On the left side navigation pane, under **Publish
   data**, choose **Owned data sets**.
3. In **Owned data sets**, choose **Create data
   set** to open the **Data set creation steps**
   wizard.
4. In **Select data set type**, choose **Amazon S3 data
   access**.
5. In **Define data set**, enter a **Name**
   and **Description** for your data set. For more
   information, see [Data set best practices](data-sets.md#data-set-best-practices "data-sets.md#data-set-best-practices").
6. (Optional) Under **Add tags – optional**, add
   tags.
7. Choose **Create data set** and continue.

## Step 2: Configure Amazon S3 data

access

Choose the Amazon S3 buckets or Amazon S3 bucket locations that you want to make available
to subscribers. You can select an entire Amazon S3 bucket, or specify up to five prefixes
or objects within an Amazon S3 bucket. To add more Amazon S3 buckets, you must create another
Amazon S3 data share.

###### To configure shared Amazon S3 data access

1. On the **Configure Amazon S3 data access** page, select
   **Choose Amazon S3 locations**.
2. In **Choose Amazon S3 locations**, enter your Amazon S3 bucket
   name in the search bar or select your Amazon S3 bucket, prefixes, or Amazon S3 files
   and choose **Add selected**. Then, choose **Add
   locations**.

###### Note

We recommend choosing a top-level folder where a majority of objects
and prefixes are stored so providers don't need to reconfigure which
prefixes or objects to share. 3. In **Configuration details**, choose your
**Requester Pays** configuration. There are two
options:

    * **Enable Requester Pays**
    *(recommended)* – Requesters
     will pay for all requests and transfers in the Amazon S3 bucket. We
     recommend this option because it helps protect against unintended
     costs from subscriber requests and transfers.
    * **Disable Requester Pays** – You pay for
     subscriber requests and transfers in the Amazon S3 bucket.


    For more information about **Requester Pays**,
     see [Objects in Requester Pays Buckets](../../../AmazonS3/latest/userguide/ObjectsinRequesterPaysBuckets.md "../../../AmazonS3/latest/userguide/ObjectsinRequesterPaysBuckets.md") in the *Amazon Simple Storage Service User Guide*.

4. Select the **Bucket Policy** that best suits your needs.
   Choose **General** to use one bucket policy for your entire
   Amazon S3 bucket. This is a one-time configuration and additional configuration
   isn't needed to share prefixes or objects in the future. Choose
   **Specific** to use a bucket policy that is specific to
   the selected Amazon S3 locations. Your shared Amazon S3 bucket needs a bucket policy
   in place to create an Amazon S3 data access data set successfully and can’t have
   ACLs enabled.
   1. To disable ACLs, navigate to your bucket permissions and set
      **Object Ownership** to **Bucket owner
      enforced**.
   2. To add a bucket policy, copy the bucket statement to your
      clipboard. In the Amazon S3 console, from the **Amazon S3
      permissions** tab, choose **Edit** in
      the **bucket policy** section, paste the bucket
      policy into the statement, and **Save
      changes**.

5. If the Amazon S3 bucket contains objects encrypted using AWS KMS customer managed keys, you
   must share all such KMS keys with AWS Data Exchange. For information about required
   prerequisites when using KMS keys to encrypt objects in your
   Amazon S3 bucket, see [Publishing a product in AWS Data Exchange
   containing Amazon S3 data access](publish-s3-data-access-product.md "publish-s3-data-access-product.md"). To share these KMS keys with AWS Data Exchange, do the following:
   1. From the **Configure Amazon S3 data access** page, in
      **Customer managed KMS keys**, select
      **Choose from your AWS KMS keys** or
      **Enter AWS KMS key ARN** and select all
      **AWS KMS keys** currently being used to
      encrypt the Amazon S3 shared locations. AWS Data Exchange uses these KMS keys to
      create grants for subscribers to access your shared locations. For
      more information, see [Grants in
      AWS KMS](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md").###### Note

AWS KMS has a limit of 50,000 grants per KMS key including
pre-existing grants. 6. Review your Amazon S3 locations, selected KMS keys, and configuration
details, and choose **Save and continue**.

## Step 3: Review and finalize

the data set

Review and finalize your newly created data set. If you wish to create and add
another Amazon S3 data access to share access to additional Amazon S3 buckets, prefixes,
objects, choose **Add another Amazon S3 data access**.

###### Note

We recommend this when needing to share access to data hosted in a different
Amazon S3 bucket than the one previously picked in the initial Amazon S3 data
access.

If you would like to make changes prior to publishing, you can save the data set
as a draft by choosing **Save draft**. Then, choose
**Finalize data set** to add it to your product.

## Step 4: Add an Amazon S3 data set

to an AWS Data Exchange product

In the following procedure, you add your data set to a new or existing AWS Data Exchange
product.

###### To add a data set to a new or existing AWS Data Exchange product

1. On the **Owned data sets** page, under **Data set
   overview**, you can **Edit name**,
   **Delete**, or **Create product from data
   set**.
2. Complete the product creation specifying product description, use cases,
   metadata, pricing, and terms and conditions.
3. **Review and publish** the product when finished.

###### Note

When a customer subscribes to your product, the customer receives
access permission to read and use your data using the Amazon S3 access point
created on your behalf.

## Step 5: Publish a new product containing access

to Amazon S3

After you create at least one data set and finalize a revision with assets, you
can publish a product with Amazon S3 data access. For more information, see [Product best practices in AWS Data Exchange](product-details.md "product-details.md"). Make sure that you
have all required details about your product and offer.

###### Note

You don't need to create a new revision when updating the shared Amazon S3 objects
unless the Amazon S3 locations have been altered and these objects aren't accessible
to subscribers.

###### To publish a new product containing access to Amazon S3

1. From the left navigation pane of the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange"), under **Publish
   data**, choose **Products**.
2. From **Products**, choose **Publish new
   product** to open the **Publish new product**
   wizard.
3. In the **Product visibility** section, choose your
   product's **Product visibility options** and
   **Sensitive information** configuration, and then
   choose **Next**. For more information, see [Product visibility in AWS Data Exchange](product-visibility.md "product-visibility.md") and
   [Sensitive categories of information in AWS Data Exchange](sensitive-information.md "sensitive-information.md").
4. In the **Add data** section, under **Owned data
   sets**, select the check boxes next to the data sets that you
   want to add, and then choose **Add selected**.

###### Note

The data sets you choose must have a finalized revision. Data sets
without finalized revisions aren't added.

    1. Go to **Selected data sets** to review your
     selections.


    You can review the **Name** of the data set, the
     **Type** of data set, and the timestamp of when
     the data set was **Last updated**.
    2. Go to **Select revision access rules**, choose
     the revision access rules that you want to set for data sets
     included in this product, and then choose **Next**.


    For more details, see [Revision access rules in AWS Data Exchange](best-practices-revisions.md "best-practices-revisions.md").

5. In the **Define product** section, under
   **Product overview**, enter information about your
   product, including the **Product name**, **Product
   logo**, **Support contact** information, and
   **Product categories**.

For more information, see [Product best practices in AWS Data Exchange](product-details.md "product-details.md"). 6. (Optional) In the **Define product** section, under
**Data dictionaries and samples – optional**, choose a
data set by selecting the option button next to the data set name and then
choose **Edit**.

For more information, see [Data dictionaries in AWS Data Exchange](data-dictionaries-pro.md "data-dictionaries-pro.md") and [Sample data in AWS Data Exchange](samples-pro.md "samples-pro.md").

    1. In the **Edit** dialog box, under
     **Upload data dictionary**, choose
     **Add file** to upload a new data dictionary.


    You can choose one data dictionary, in .csv format, with a maximum
     size of 1 MB.
    2. Choose a saved data dictionary from your computer and then choose
     **Open**.


    The data dictionary .csv file appears on the
     **Edit** dialog box.


    ###### Note

    Your data dictionary must conform to the AWS Data Exchange data dictionary
     template. If you don’t have a saved data dictionary to upload,
     you can choose either the **blank data dictionary
     template** link or the **example data
     dictionary** link in the AWS Data Exchange console.
    3. Choose **Data dictionary preview** to preview the
     data dictionary.
    4. Under **Samples - optional**, choose
     **Upload samples**, choose a sample from your
     computer, and then choose **Open**.


     The samples appear on the **Edit** dialog
     box.


    ###### Note

    You can upload up to 10 samples with a maximum size of 50 MB.
     Samples in .csv format can be previewed.
    5. Enter a description for each sample that will be visible on the
     product detail page.
    6. Choose **Save**.

7. Under **Product definition**, enter a **Short
   description** and a **Long description** of
   your product.

If you want to use a template for your long description, select
**Apply template**, choose your template type, and then
provide your specific product details in the template. 8. Choose **Next**. 9. Configure your offer.

    * If you're creating a public offer, in the **Add public
     offer** section, configure your offer. All AWS Data Exchange
     products with visibility set to **Public** require a public offer.




    	1. Choose your **Pricing and access
    	 duration** options for the subscription.
    	2. Choose your US sales tax settings, data subscription
    	 agreement (DSA), and refund policy.
    	3. (Optional) Set **Subscription
    	 verification** to control who can subscribe to
    	 this product. For more information, see [Subscription verification for providers in
    	 AWS Data Exchange](subscription-verification-pro.md "subscription-verification-pro.md").
    	4. Choose your **Oﬀer auto-renewal** option.
    	 For more information, see [Creating an offer for AWS Data Exchange products](prepare-offers.md "prepare-offers.md").
    	5. Choose **Next**.


    * If you're creating a private offer, configure the offer details in
     the **Add custom offer** section.




    	1. In the **Subscriber account information**
    	 section, add at least one subscriber account to which you
    	 want to extend the offer.
    	2. Choose your **Pricing and access
    	 duration** options for the subscription.
    	3. Choose the **Offer expiration date** by
    	 which the subscriber must accept the offer.
    	4. Choose your US sales tax settings, data subscription
    	 agreement (DSA), and refund policy.
    	5. Choose your **Oﬀer auto-renewal** option.
    	 For more information, see [Creating an offer for AWS Data Exchange products](prepare-offers.md "prepare-offers.md").
    	6. Choose **Next**.

10. In the **Review & publish** section, review your
    product information and then expand the **Product page
    preview** to see how it will look after it’s published.
11. If you're sure that you want to make the product and public offer visible
    and available to everyone, choose **Publish**.

You've now completed the manual portion of publishing a data product with a public
offer. AWS Data Exchange prepares and publishes your product. On the **Product
overview** page, the status of your product is **Awaiting
approval**. The status changes to **Published** after
the product is published.

## Step 6: (Optional) Copy a product

After you have created your first product, you can copy its details and public
offers to create a new product.

###### Note

You can copy a public, private, published, or unpublished product. Custom
oﬀers associated with the product can't be copied, but public oﬀers can be
copied.

###### To copy a product

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. From the left navigation pane, under **Publish data**,
   choose **Products**.
3. From **Products**, choose the option next to the product
   that you want to copy.
4. Select the **Actions** dropdown list, and then choose
   **Create copy**.
5. Continue through the **Publish a product** workflow, with
   details already filled in, based on the product you chose in Step 3. For
   more information, see [Step 5: Publish a new product](publish-data-product.md#publish-products "publish-data-product.md#publish-products").
