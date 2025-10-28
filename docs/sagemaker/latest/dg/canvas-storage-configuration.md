# Configure your Amazon S3 storage

When you set up your SageMaker Canvas application, the default storage location for model
artifacts, datasets, and other application data is an Amazon S3 bucket that Canvas creates.
This default Amazon S3 bucket follows the naming pattern
`s3://sagemaker-`{Region}`-`{your-account-id}``
and exists in the same Region as your Canvas application. However, you can
customize the storage location and specify your own Amazon S3 bucket for
storing Canvas application data. You might want to use your own Amazon S3 bucket for storing
application data for any of the following reasons:

- Your organization has internal naming conventions for Amazon S3
  buckets.
- You want to enable cross-account access to model artifacts or other Canvas
  data.
- You want to be compliant with internal security guidelines, such as
  restricting users to specific Amazon S3 buckets or model artifacts.
- You want enhanced visibility and access to logs produced by Canvas,
  independent of the AWS console or SageMaker Studio Classic.
  By specifying your own Amazon S3 bucket, you can have increased control over your own
  storage and be compliant with your organization.

To get started, you can either create a new SageMaker AI domain or user profile, or you can
update an existing domain or user profile. Note that the user profile settings override the
domain-level settings. For example, you can use the default bucket configuration at the
domain level, but you can specify a custom Amazon S3 bucket for an individual user. After
specifying your own Amazon S3 bucket for the domain or user profile, Canvas creates a
subfolder called `Canvas/<UserProfileName>`
under the input Amazon S3 URI and saves all artifacts generated in the Canvas application under
this subfolder.

###### Important

If you update an existing domain or user profile,
you no
longer have access to your Canvas artifacts from the previous location. Your files
are still in the old Amazon S3 location, but you can no longer view them from Canvas. The
new configuration takes effect the next time you log into the application.

For more information about granting cross-account access to your Amazon S3 bucket, see
[Granting cross-account object permissions](../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example4.md#access-policies-walkthrough-example4-overview "../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example4.md#access-policies-walkthrough-example4-overview") in the _Amazon S3 User Guide_.

The following sections describe how to specify a custom Amazon S3 bucket for your Canvas
storage configuration. If you’re setting up a new SageMaker AI domain (or a new user in a
domain), then use the [New domain setup method](#canvas-storage-configuration-new-domain "#canvas-storage-configuration-new-domain") or the [New user profile setup method](#canvas-storage-configuration-new-user "#canvas-storage-configuration-new-user"). If you have an existing
Canvas user profile and would like to update the profile's
storage configuration, use the [Existing user method](#canvas-storage-configuration-existing-user "#canvas-storage-configuration-existing-user").

## Before you begin

If you’re specifying an Amazon S3 URI from a different AWS account, or if you’re using a
bucket that is encrypted with AWS KMS, then you must configure permissions before
proceeding. You must grant AWS IAM permissions to ensure that Canvas can
download and upload objects to and from your bucket. For detailed information on how to
grant the required permissions, see [Grant permissions for cross-account Amazon S3 storage](canvas-permissions-cross-account.md "canvas-permissions-cross-account.md").

Additionally, the final Amazon S3 URI for the training folder in your Canvas storage
location must be 128 characters or less. The final Amazon S3 URI consists of your bucket path
`s3://<your-bucket-name>/<folder-name>/`
plus the path that Canvas adds to your bucket:
`Canvas/<user-profile-name>/Training`.
For example, an acceptable path that is less than 128 characters is
`s3://<amzn-s3-demo-bucket>/<machine-learning>/Canvas/<user-1>/Training`.

## New domain setup method

If you’re setting up a new domain and Canvas application, use this section to
configure the storage location at the domain level. This configuration applies to all
new users you create in the domain, unless you specify a different storage location for
individual user profiles.

When doing a **Standard setup** for your domain, on the
**Step 3: Configure Applications - Optional** page, use the
following procedure for the **Canvas** section:

1. For the **Canvas storage configuration**, do
   the following:
   1. Select **System managed** if you want to
      set the location to the default SageMaker AI bucket that follows
      the pattern `s3://sagemaker-`{Region}`-`{your-account-id}``.
   2. Select **Custom S3** to specify your own
      Amazon S3 bucket as the storage location. Then, enter the Amazon S3
      URI.
   3. (Optional) For **Encryption key**,
      specify a KMS key for encrypting Canvas artifacts stored at the
      specified location.

2. Finish setting up the domain and choose **Submit**.

Your domain is now configured to use the Amazon S3 location you specified for
SageMaker Canvas application storage.

## New user profile setup method

If you’re setting up a new user profile in your domain, use this section to
configure the storage location for the user. This configuration overrides the domain-level configuration.

When adding a user profile to your domain, for **Step 2: Configure
Applications**, use the following procedure for the
**Canvas** section:

1. For the **Canvas storage configuration**, do
   the following:
   1. Select **System managed** if you want to
      set the location to the default SageMaker AI created bucket that follows
      the pattern `s3://sagemaker-`{Region}`-`{your-account-id}``.
   2. Select **Custom S3** to specify your own
      Amazon S3 bucket as the storage location. Then, enter the Amazon S3
      URI.
   3. (Optional) For **Encryption key**,
      specify a KMS key for encrypting Canvas artifacts stored at the
      specified location.

2. Finish setting up the user profile and choose **Submit**.

Your user profile is now configured to use the Amazon S3 location you specified for SageMaker Canvas application storage.

## Existing user method

If you have an existing Canvas user profile and would like to update the Amazon S3
storage location, you can edit the SageMaker AI domain or user profile settings. The change
takes effect the next time you log into the Canvas application.

###### Note

When you change the storage location for an
existing Canvas application, you lose access to your Canvas artifacts from the
previous storage location. The artifacts are still stored in the old Amazon S3 location, but you can no longer
view them from Canvas.

Remember that the user profile settings override the general domain settings, so
you can update the Amazon S3 storage location for specific user profiles without changing it
for all of the users. You can update the storage configuration for an existing
domain or user by using the following procedures.

Update an existing domain
Use the following procedure to update the storage configuration for a domain.

1. Open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose
   **Domains**.
4. From the list of domains, choose your domain.
5. On the **Domain details** page, choose the **App
   Configurations** tab.
6. Scroll down to the **Canvas** section and choose **Edit**.
7. The **Edit Canvas settings** page opens.
   For the **Canvas storage configuration** section, do
   the following:
   1. Select **System managed** if you want to
      set the location to the default SageMaker AI created bucket that follows
      the pattern `s3://sagemaker-`{Region}`-`{your-account-id}``.
   2. Select **Custom S3** to specify your own
      Amazon S3 bucket as the storage location. Then, enter the Amazon S3
      URI.
   3. (Optional) For **Encryption key**,
      specify a KMS key for encrypting Canvas artifacts stored at the
      specified location.

8. Finish any other modifications you want to make to the domain, and then choose **Submit** to save your changes.

Update an existing user profile
Use the following procedure to update the storage configuration for a user
profile.

1. Open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. From the list of **domains**, choose your domain.
5. From the list of users in the domain, choose the user whose configuration you want to edit.
6. On the **User Details** page, choose **Edit**.
7. In the navigation pane, choose **Canvas settings**.
8. For the **Canvas storage configuration**, do
   the following:
   1. Select **System managed** if you want to
      set the location to the default SageMaker AI bucket that follows
      the pattern `s3://sagemaker-`{Region}`-`{your-account-id}``.
   2. Select **Custom S3** to specify your own
      Amazon S3 bucket as the storage location. Then, enter the Amazon S3
      URI.
   3. (Optional) For **Encryption key**,
      specify a KMS key for encrypting Canvas artifacts stored at the
      specified location.

9. Finish any other modifications you want to make to the user profile, and then choose **Submit** to save your changes.

The storage location for your Canvas user profile should now be updated. The next
time you log into the Canvas application, you
receive a notification that the storage location has been updated. You lose access to
any previous artifacts that you created in Canvas. You can still access the files in
Amazon S3, but you can no longer view them in Canvas.
