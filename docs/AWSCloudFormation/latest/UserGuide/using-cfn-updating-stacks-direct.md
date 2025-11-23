# Update stacks directly

When you want to quickly deploy updates to your stack, perform a direct update. With a
direct update, you submit a template or input parameters that specify updates to the resources
in the stack, and CloudFormation immediately deploys them. If you want to use a template to make
your updates, you can modify the current template and store it locally or in an Amazon S3
bucket.

For resource properties that don't support updates, you must keep the current values. To
preview the changes that CloudFormation will make to your stack before you update it, use change
sets. For more information, see [Update CloudFormation stacks using change
sets](using-cfn-updating-stacks-changesets.md "using-cfn-updating-stacks-changesets.md").

When updating a stack, CloudFormation might interrupt resources or replace updated resources,
depending on which properties you update. For more information about resource update behaviors,
see [Understand update behaviors of stack
resources](using-cfn-updating-stacks-update-behaviors.md "using-cfn-updating-stacks-update-behaviors.md").

###### To update a stack

(console)

1. Sign in to the AWS Management Console and open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose your AWS Region.
3. On the **Stacks** page, select the running stack that you want to
   update.
4. In the stack details pane, choose **Update**.
5. If you _haven't_ modified the stack template, select **Use
   existing template**, and then choose **Next**.

If you have modified the template, select **Replace existing template**
and specify the location of the updated template in the **Specify
template** section:

    * For a template stored locally on your computer, select **Upload a template
     file**. Choose **Choose file** to navigate to the file and
     select it, and then choose **Next**.


    ###### Note

    If you upload a local template file, CloudFormation uploads it to an Amazon Simple Storage Service (Amazon S3)
     bucket in your AWS account. If you don't already have an S3 bucket that was created
     by CloudFormation, it creates a unique bucket for each Region in which you upload a
     template file. If you already have an S3 bucket that was created by CloudFormation in your
     AWS account, CloudFormation adds the template to that bucket.

    Considerations to keep in mind about S3 buckets created by CloudFormation



    	+ The buckets are accessible to anyone with Amazon S3 permissions in your
    	 AWS account.
    	+ CloudFormation creates the buckets with server-side encryption enabled by default,
    	 thereby encrypting all objects stored in the bucket.


    	You can directly manage encryption options for buckets that CloudFormation has
    	 created; for example, using the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/"), or the AWS CLI. For
    	 more information, see [Setting
    	 default server-side encryption behavior for Amazon S3 buckets](../../../AmazonS3/latest/userguide/bucket-encryption.md "../../../AmazonS3/latest/userguide/bucket-encryption.md") in the
    	 *Amazon Simple Storage Service User Guide*.
    	+ You can use your own bucket and manage its permissions by manually uploading
    	 templates to Amazon S3. When you create or update a stack, specify the Amazon S3 URL of a
    	 template file.
    * For a template stored in an Amazon S3 bucket, choose **Amazon S3 URL**. Enter
     or paste the URL for the template, and then choose **Next**.


    If you have a template in a versioning-enabled bucket, you can specify a specific
     version of the template by appending
     `?versionId=`version-id`` to the URL. For more
     information, see [Working
     with objects in a versioning-enabled bucket](../../../AmazonS3/latest/userguide/manage-objects-versioned-bucket.md "../../../AmazonS3/latest/userguide/manage-objects-versioned-bucket.md") in the
     *Amazon Simple Storage Service User Guide*.

If any syntax issues are detected, the console provides error messages that help you
correct the template. 6. If your template contains parameters, on the **Specify stack details**
page you can enter or modify the parameter values, and then choose
**Next**.

CloudFormation populates each parameter with the value that's currently set in the stack
with the exception of parameters declared with the `NoEcho` attribute; however,
you can still use current values by checking **Use existing value**.

For more information about using `NoEcho` to mask sensitive information, in
addition to using dynamic parameters to manage secrets, see the [Do not embed credentials in your templates](security-best-practices.md#creds "security-best-practices.md#creds") best practice. 7. On the **Configure stack options** page, you can update the tags and
permissions applied to the stack, and modify advanced options such as stack policy, rollback
configuration, or update the Amazon SNS notification topic. For more information about these
options, see [Configure stack options](cfn-console-create-stack.md#configure-stack-options "cfn-console-create-stack.md#configure-stack-options"). 8. If your template contains IAM resources, for **Capabilities**, choose
**I acknowledge that this template may create IAM resources** to
specify that you want to use IAM resources in the template. For more information, see
[Acknowledging IAM resources in CloudFormation
templates](control-access-with-iam.md#using-iam-capabilities "control-access-with-iam.md#using-iam-capabilities"). 9. Choose **Next** to continue. 10. Review the stack information and the changes that you submitted.

Check that you submitted the correct information, such as the correct parameter values
or template URL.

In the **Change set preview** section, check that CloudFormation will make
all the changes that you expect. For example, you can check that CloudFormation adds, removes,
and modifies the resources that you intended to add, remove, or modify. CloudFormation generates
this preview by creating a change set for the stack. For more information, see [Update CloudFormation stacks using change
sets](using-cfn-updating-stacks-changesets.md "using-cfn-updating-stacks-changesets.md"). 11. When you are satisfied with your changes, choose **Update
stack**.

###### Note

At this point, you also have the option to view the change set to review your proposed
updates more thoroughly. To do so, choose **View change set** instead of
**Update stack**. CloudFormation displays the change set generated based on
your updates. When you are ready to perform the stack update, choose
**Execute**.

CloudFormation displays the stack details page for your stack, with the
**Events** pane selected. Your stack now has a status of
`UPDATE_IN_PROGRESS`. After CloudFormation has successfully finished updating the
stack, it sets the stack status to `UPDATE_COMPLETE`.

If the stack update fails, CloudFormation; automatically rolls back changes, and sets the
stack status to `UPDATE_ROLLBACK_COMPLETE`.

###### Note

You can cancel an update while it's in the `UPDATE_IN_PROGRESS` state. For
more information, see [Cancel a stack update](using-cfn-stack-update-cancel.md "using-cfn-stack-update-cancel.md").

###### To update a stack using the command line

You can use one of the following commands:

- [update-stack](../../../cli/latest/reference/cloudformation/update-stack.md "../../../cli/latest/reference/cloudformation/update-stack.md") (AWS CLI)
- [Update-CFNStack](../../../powershell/latest/reference/items/Update-CFNStack.md "../../../powershell/latest/reference/items/Update-CFNStack.md") (AWS Tools for Windows PowerShell)
  For examples of using the command line to update a stack, see [Examples of CloudFormation stack operation commands for
  the AWS CLI and PowerShell](service_code_examples.md "service_code_examples.md").
