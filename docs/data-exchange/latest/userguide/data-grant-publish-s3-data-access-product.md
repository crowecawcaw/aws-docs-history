# Creating a data grant on AWS Data Exchange

containing Amazon S3 data access

With AWS Data Exchange for Amazon S3, data owners can share direct access to Amazon S3 buckets or specific
prefixes and Amazon S3 objects. Data owners also use AWS Data Exchange to automatically manage entitlements
through data grants.

As a data owner, you can share direct access to an entire Amazon S3 bucket or specific prefixes
and Amazon S3 objects without creating or managing copies. These shared
Amazon S3 objects can be server-side encrypted with customer managed keys stored in AWS Key Management Service
(AWS KMS) or with AWS managed keys (SSE-S3). For more information about monitoring your
KMS keys and understanding encryption contexts, see [Key management for Amazon S3 data access](key-management.md "key-management.md"). When a
receiver gains access to your data products, AWS Data Exchange automatically provisions an Amazon S3 access
point and updates its resource policies on your behalf to grant recipients read-only access.
Recipients can use the Amazon S3 access point aliases in places where they use Amazon S3 bucket names to
access data in Amazon S3.

When the subscription ends, the receiver’s permissions are revoked.

Before you can create a data grant containing Amazon S3 data access, you must meet the
following prerequisites:

###### Prerequisites

- Confirm that the Amazon S3 buckets hosting the data are configured with the Amazon S3 bucket
  owner enforced setting turned on **ACLs Disabled**. For more information,
  see [Controlling ownership of
  objects and disabling ACLs for your bucket](../../../AmazonS3/latest/userguide/about-object-ownership.md "../../../AmazonS3/latest/userguide/about-object-ownership.md") in the _Amazon Simple Storage Service User Guide_.
- Your shared objects must be in the Amazon S3 Standard Storage class, or be managed using Amazon S3 Intelligent
  Tiering, for recievers to access them successfully. If they’re in other storage classes,
  or if you have enabled Intelligent Tiering with Deep Archive, your receivers will get
  errors because they won’t have permission to `RestoreObject`.
- Confirm that the Amazon S3 buckets hosting the data has encryption disabled or encrypted
  with Amazon S3 managed keys (SSE-S3) or customer managed keys stored in AWS Key Management Service (AWS KMS).
- If you're using customer managed keys, you must have the following:

      1. IAM permissions to `kms:CreateGrant` on the KMS keys. You can
       access these permissions through the key policy, IAM credentials, or through an
       AWS KMS grant on the KMS key. For more information about key management and
       understanding how AWS Data Exchange uses AWS KMS grants, see [Creating AWS KMS grants](key-management.md#create-kms-grants "key-management.md#create-kms-grants").


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
      | Workforce identity<br>(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs. | Following the instructions for the interface that you want to use.<br>+ For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the<br>*AWS Command Line Interface User Guide*.<br>+ For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center<br>authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the *AWS SDKs and Tools Reference Guide*. |
      | IAM | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs. | Following the instructions in [Using temporary<br>credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the *IAM User Guide*. |
      | IAM | (Not recommended)Use long-term credentials to sign programmatic requests<br>to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br>+ For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in<br>the *AWS Command Line Interface User Guide*.<br>+ For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the<br>*AWS SDKs and Tools Reference Guide*.<br>+ For AWS APIs, see [Managing access keys for<br>IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the *IAM User Guide*. |


      Following is an example JSON policy that shows how you could add to the key policy
       of the KMS key.



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

      The following policy shows an example policy addition for the IAM identity that
       is used.



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

      Cross account KMS keys are also permitted if the `kms:CreateGrant`
       permission on the KMS keys are obtained through the earlier step. If another
       account owns the key, you must have permissions on the key policy and your IAM
       credentials as detailed in the above examples.
      2. Make sure to use KMS keys to encrypt existing and new objects in the
       Amazon S3 bucket using the Amazon S3 bucket key feature. For more
       details, see [Configuring S3
       Bucket Keys](../../../AmazonS3/latest/userguide/bucket-key.md#configure-bucket-key "../../../AmazonS3/latest/userguide/bucket-key.md#configure-bucket-key") in the *Amazon Simple Storage Service User Guide*.




      	+ For new objects added to your Amazon S3 bucket, you can set up
      	 Amazon S3 bucket key encryption by default. If existing objects have been
      	 encrypted without using the Amazon S3bucket key feature, these objects
      	 must be migrated to use the Amazon S3 bucket key for encryption.


      	To enable the Amazon S3 bucket key for existing objects, use the
      	 `copy` operation. For more information, see [Configuring
      	 an Amazon S3 bucket key at the object level using batch
      	 operations](../../../AmazonS3/latest/userguide/configuring-bucket-key-object.md "../../../AmazonS3/latest/userguide/configuring-bucket-key-object.md").
      	+ AWS managed KMS keys or AWS owned keys aren't supported. You can migrate
      	 from an unsupported encryption scheme to the ones currently supported. For more
      	 information, see [Changing your Amazon S3 encryption](https://aws.amazon.com/blogs/storage/changing-your-amazon-s3-encryption-from-s3-managed-encryption-sse-s3-to-aws-key-management-service-sse-kms/ "https://aws.amazon.com/blogs/storage/changing-your-amazon-s3-encryption-from-s3-managed-encryption-sse-s3-to-aws-key-management-service-sse-kms/") at the AWS Storage Blog.
      3. Set the Amazon S3 buckets hosting the data to trust AWS Data Exchange owned access points. You must
       update these Amazon S3 bucket policies to give AWS Data Exchange permissions to create Amazon S3 access
       points and grant or remove subscribers' access on your behalf. If the policy statement
       is missing, you must edit the bucket policy to add the Amazon S3 locations to
       your data set.


      An example policy is shown below. Replace `<Bucket ARN>` with the
       appropriate value.



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

  You can delegate data sharing through AWS Data Exchange to an entire Amazon S3 bucket. However, you can
  scope delegation to the specific prefixes and objects of the bucket that you want to share in
  the data set. Following is an example of a scoped policy. Replace `<Bucket ARN>`
  and `"mybucket/folder1/*"` with your own information.

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

Similarly, to scope access to only a single file, a data owner can use the following
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

The following topics describe the process of creating an Amazon S3 data set and a data grant
with Amazon S3 data sets using the AWS Data Exchange console. The process has the following steps:

###### Steps

- [Step 1: Create an Amazon S3 data set](#data-grant-create-S3-data-set "#data-grant-create-S3-data-set")
- [Step 2: Configure Amazon S3 data
  access](#data-grant-configure-s3-data-access-product "#data-grant-configure-s3-data-access-product")
- [Step 3: Review and finalize
  the data set](#data-grant-review-finalize-s3-data-set-product "#data-grant-review-finalize-s3-data-set-product")
- [Step 4: Create a new data
  grant](#data-grant-add-s3-data-set-to-existing-product "#data-grant-add-s3-data-set-to-existing-product")

## Step 1: Create an Amazon S3 data set

###### To create an Amazon S3 data set

1. On the left side navigation pane, under **My data**, choose
   **Owned data sets**.
2. In **Owned data sets**, choose **Create data set**
   to open the **Data set creation steps** wizard.
3. In **Select data set type**, choose **Amazon S3 data
   access**.
4. In **Define data set**, enter a **Name** and
   **Description** for your data set. For more information, see [Data set best practices](data-sets.md#data-set-best-practices "data-sets.md#data-set-best-practices").
5. (Optional) Under **Add tags – optional**, add tags.
6. Choose **Create data set** and continue.

## Step 2: Configure Amazon S3 data

access

Choose the Amazon S3 buckets or Amazon S3 bucket locations that you want to make available to
recipients. You can select an entire Amazon S3 bucket, or specify up to five prefixes or objects
within an Amazon S3 bucket. To add more Amazon S3 buckets, you must create another Amazon S3 data
share.

###### To configure shared Amazon S3 data access

1. On the **Configure Amazon S3 data access** page, select **Choose
   Amazon S3 locations**.
2. In **Choose Amazon S3 locations**, enter your Amazon S3 bucket name in
   the search bar or select your Amazon S3 bucket, prefixes, or Amazon S3 files and choose
   **Add selected**. Then, choose **Add
   locations**.

###### Note

We recommend choosing a top-level folder where a majority of objects and prefixes
are stored so data owners don't need to reconfigure which prefixes or objects to
share. 3. In **Configuration details**, choose your **Requester
Pays** configuration. There are two options:

    * **Enable Requester Pays**
    *(recommended)* – Requesters will pay for
     all requests and transfers in the Amazon S3 bucket. We recommend this option because it
     helps protect against unintended costs from receiver requests and transfers.
    * **Disable Requester Pays** – You pay for receiver
     requests and transfers in the Amazon S3 bucket.


    For more information about **Requester Pays**, see [Objects in
     Requester Pays Buckets](../../../AmazonS3/latest/userguide/ObjectsinRequesterPaysBuckets.md "../../../AmazonS3/latest/userguide/ObjectsinRequesterPaysBuckets.md") in the *Amazon Simple Storage Service User Guide*.

4. Select the **Bucket Policy** that best suits your needs. Choose
   **General** to use one bucket policy for your entire Amazon S3 bucket.
   This is a one-time configuration and additional configuration isn't needed to share
   prefixes or objects in the future. Choose **Specific** to use a bucket
   policy that is specific to the selected Amazon S3 locations. Your shared Amazon S3 bucket needs a
   bucket policy in place to create an Amazon S3 data access data set successfully and can’t
   have ACLs enabled.
   1. To disable ACLs, navigate to your bucket permissions and set **Object
      Ownership** to **Bucket owner enforced**.
   2. To add a bucket policy, copy the bucket statement to your clipboard. In the Amazon S3
      console, from the **Amazon S3 permissions** tab, choose
      **Edit** in the **bucket policy** section, paste
      the bucket policy into the statement, and **Save changes**.

5. If the Amazon S3 bucket contains objects encrypted using AWS KMS customer managed keys, you must
   share all such KMS keys with AWS Data Exchange. For information about required prerequisites when
   using KMS keys to encrypt objects in your Amazon S3 bucket, see [Publishing a product in AWS Data Exchange
   containing Amazon S3 data access](publish-s3-data-access-product.md "publish-s3-data-access-product.md"). To share these KMS keys with AWS Data Exchange, do
   the following:
   1. From the **Configure Amazon S3 data access** page, in
      **Customer managed KMS keys**, select **Choose from your
      AWS KMS keys** or **Enter AWS KMS key ARN** and
      select all **AWS KMS keys** currently being used to encrypt the
      Amazon S3 shared locations. AWS Data Exchange uses these KMS keys to create grants for recipients
      to access your shared locations. For more information, see [Grants in
      AWS KMS](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md").###### Note

AWS KMS has a limit of 50,000 grants per KMS key including pre-existing
grants. 6. Review your Amazon S3 locations, selected KMS keys, and configuration details, and
choose **Save and continue**.

## Step 3: Review and finalize

the data set

Review and finalize your newly created data set. If you wish to create and add another
Amazon S3 data access to share access to additional Amazon S3 buckets, prefixes, objects, choose
**Add another Amazon S3 data access**.

###### Note

We recommend this when needing to share access to data hosted in a different Amazon S3
bucket than the one previously picked in the initial Amazon S3 data access.

If you would like to make changes prior to publishing, you can save the data set as a
draft by choosing **Save draft**. Then, choose **Finalize data
set** to add it to your data grant.

## Step 4: Create a new data

grant

After you've created at least one data set and finalized a revision with assets, you're
ready to use that data set as a part of a data grant.

###### To create a new data grant

1. In the left navigation pane of the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange"), under **Exchanged data grants**, choose
   **Sent data grants**.
2. From **Sent data grants**, choose **Create data
   grant** to open the **Define data grant** wizard.
3. In the **Select owned data set** section, select the check box next
   to the data set you want to add.

###### Note

The data set you choose must have a finalized revision. Data sets without finalized
revisions can't be added to data grants.

Unlike with data sets included in data products which are shared on AWS Marketplace, data
sets added to data grants have no revision access rules, meaning a recipient of a data
grant, once the data grant is approved, will have access to all finalized revisions of
a given data set (including historical revisions finalized prior to the data grant
creation). 4. In the **Grant overview** section, enter information the recipient
will see about your data grant, including the **Data grant name** and
**Data grant description**. 5. Choose **Next**.

For more information, see [Product best practices in AWS Data Exchange](product-details.md "product-details.md"). 6. In the **Recipient access information** section, under
**AWS account ID**, enter the AWS account ID of the recipient
account who should receive the data grant. . 7. Under **Access end date**, select a specific end date for when the
data grant should expire or, if the grant should exist in perpetuity, select
**No end date**. 8. Choose **Next**. 9. In the **Review and send** section, review your data grant
information. 10. If you're sure that you want to create the data grant and send it to the chosen
recipient, choose **Create and send data grant**.

You've now completed the manual portion of creating a data grant. The data grant will show on the **Sent data
grants** tab on the **Sent data grants** page showing its status
as **Pending acceptance** until the recipient account accepts it.
