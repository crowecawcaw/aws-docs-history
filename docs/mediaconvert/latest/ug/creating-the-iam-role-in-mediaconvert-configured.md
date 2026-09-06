

# Creating the IAM role within MediaConvert
<a name="creating-the-iam-role-in-mediaconvert-configured"></a>

When you create the AWS Identity and Access Management (IAM) role in MediaConvert with configured permissions, you can restrict MediaConvert access to only specific Amazon S3 buckets. You can also specify whether to grant invoke access to your Amazon API Gateway endpoints.

**To set up the IAM role in MediaConvert with configured permissions**

1. Open the [Jobs](https://console.aws.amazon.com/mediaconvert/home#/jobs/list) page in the MediaConvert console.

1. Choose **Create job**.

1. Under **Job settings**, choose **AWS integration**.

1. In the **Service access** section, for **Service role control**, choose **Create a new service role, configure permissions**.

1. For **New role name**, we suggest that you keep the default value **MediaConvert\_Default\_Role**. When you do, MediaConvert uses this role by default for your future jobs.

1. For **Input S3 locations** and **Output S3 locations**, choose **Add location**. Select the Amazon S3 buckets that you will use for input or output locations.

1. (Optional) For **API Gateway endpoint invocation**, if you use features that require it, choose allow.

   MediaConvert requires this access for the following features:
   + Digital rights management with SPEKE
   + Nielsen non-linear watermarking

   To allow MediaConvert invoke access to a specific endpoint only, modify these permissions in the role policy after you create it by using the AWS Identity and Access Management (IAM) service. For more information, see [Editing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html) in the *AWS Identity and Access Management User Guide*.