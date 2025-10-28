# Setting up IAM permissions

To run transcoding jobs with AWS Elemental MediaConvert, you need an IAM service role to
allow MediaConvert access to your resources. Resources include things like your input
files and the locations where your output files are stored.

Regardless of how you initially create your IAM service role, you can refine this
role at any time using IAM. For more information, see [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console") in the _IAM User Guide_.

You can create your IAM service role in one of the following ways:

- In the MediaConvert console, with some restrictions on the permissions that
  you grant. For instructions, see [Creating the IAM role within MediaConvert](creating-the-iam-role-in-mediaconvert-configured.md "creating-the-iam-role-in-mediaconvert-configured.md").

From the MediaConvert console, by configuring your role to allow
MediaConvert access to only some of your Amazon S3 buckets. You can also choose
whether to grant invoke access to your API Gateway endpoints.

- In the IAM console. For instructions, see [Creating a role in
  IAM](creating-the-iam-role-in-iam.md "creating-the-iam-role-in-iam.md").

You can exercise fine control over exactly what access you grant to
MediaConvert when you set up your IAM role in the IAM console. You can also
use IAM through the AWS Command Line Interface (AWS CLI), or an API or SDK.

###### Note

If you enable Amazon S3 default encryption on your Amazon S3 buckets, and you and specify
your own key managed by AWS Key Management Service, you must grant additional permissions. For more
information, see [Granting permissions for MediaConvert to access encrypted Amazon S3 buckets](granting-permissions-for-mediaconvert-to-access-encrypted-s3-buckets.md "granting-permissions-for-mediaconvert-to-access-encrypted-s3-buckets.md").

## Using the default MediaConvert role

If you use the name `MediaConvert_Default_Role`, then the MediaConvert
console uses it by default when you create jobs in the future. This happens
regardless of how you create the IAM service role for MediaConvert to use.
