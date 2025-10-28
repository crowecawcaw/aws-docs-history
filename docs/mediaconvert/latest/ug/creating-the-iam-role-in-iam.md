# Creating a role with the IAM

console

Working directly with AWS Identity and Access Management (IAM), you
can do actions that aren't available in the MediaConvert
console. You can
either
do this when you create your role in IAM, or you can create
your role in MediaConvert and then use IAM to refine it later.

The following procedure explains how to create a role with the IAM console. For
information about accessing IAM
programmatically, see the appropriate document in the [IAM documentation set](../../../iam.md "../../../iam.md").

###### To create the service role for MediaConvert (IAM console)

1.  Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2.  In the navigation pane of the IAM console, choose **Roles**, and
    then choose **Create role**.
3.  For **Trusted entity type**, choose **AWS service**.
4.  For **Service or use case**, choose **MediaConvert**, and then choose the **MediaConvert** use case.
5.  Choose **Next**.
6.  Select the box next to the MediaConvert policy that you created in the previous procedure.
7.  (Optional) Set a [permissions
    boundary](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md"). This is an advanced feature that is available for service roles, but
    not service-linked roles.

        1. Open the **Set permissions boundary** section, and then choose
        **Use a permissions boundary to control the maximum role permissions**.


        IAM includes a list of the AWS managed and customer-managed policies in your account.
        2. Select the policy to use for the permissions boundary.

8.  Choose **Next**.
9.  Enter a role name or a role name suffix to help you identify the purpose of the role.

###### Important

When you name a role, note the following:

    * Role names must be unique within your AWS account, and can't be made unique by case.


    For example, don't create roles named both `PRODROLE` and
     `prodrole`. When a role name is used in a policy or as part of an ARN, the role name is case sensitive, however when a role name appears to customers in the console, such as during the sign-in process, the role name is case insensitive.
    * You can't edit the name of the role after it's created because other entities might reference the role.

10. (Optional) For **Description**, enter a description for the role.
11. (Optional) To edit
    the use cases and permissions for the role, in the **Step 1: Select trusted
    entities** or **Step 2: Add permissions** sections, choose **Edit**.
12. (Optional) To help identify, organize, or search for the role, add tags as key-value pairs. For more
    information about using tags in IAM, see [Tags for AWS Identity and Access Management resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_.
13. Review the role, and then choose **Create role**.

###### Note

For **New role name**, we suggest that you enter `MediaConvert_Default_Role`. When you do,
MediaConvert uses this role by default for your future jobs.
