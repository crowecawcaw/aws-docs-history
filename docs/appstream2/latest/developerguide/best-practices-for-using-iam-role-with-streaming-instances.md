# Best Practices for Using IAM Roles With WorkSpaces Applications Streaming Instances

When you use IAM roles with WorkSpaces Applications streaming instances, we recommend that you follow these practices:

- Limit the permissions that you grant to AWS API actions and resources.

Follow least privilege principles when you create and attach IAM policies to the IAM roles associated with WorkSpaces Applications streaming instances. When you use an application or script that requires access to AWS API actions or resources, determine the specific actions and resources that are required. Then, create policies that allow the application or script to perform only those actions. For more information, see [Grant Least Privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") in the _IAM User Guide_.

- Create an IAM role for each WorkSpaces Applications resource.

Creating a unique IAM role for each WorkSpaces Applications resource is a practice that follows least privilege principles. Doing so also lets you modify permissions for a resource without affecting other resources.

- Limit where the credentials can be used.

IAM policies let you define the conditions under which your IAM role can be used to access a resource. For example, you can include conditions to specify a range of IP addresses that requests can come from. Doing so prevents the credentials from being used outside of your environment. For more information, see [Use Policy Conditions for Extra Security](../../../IAM/latest/UserGuide/best-practices.md#use-policy-conditions "../../../IAM/latest/UserGuide/best-practices.md#use-policy-conditions") in the _IAM User Guide_.
