# Tagging a private repository in Amazon ECR

To help you manage your Amazon ECR repositories, you can assign your own metadata to new or
existing Amazon ECR repositories by using AWS resource _tags_. For example,
you could define a set of tags for your account's Amazon ECR repositories that helps you track
the owner of each repository.

## Tag basics

Tags don't have any semantic meaning to Amazon ECR and are interpreted strictly as a string of
characters. Tags are not automatically assigned to your resources. You can edit tag keys
and values, and you can remove tags from a resource at any time. You can set the value
of a tag to an empty string, but you can't set the value of a tag to null. If you add a
tag that has the same key as an existing tag on that resource, the new value overwrites
the old value. If you delete a resource, any tags for the resource are also
deleted.

You can work with tags using the Amazon ECR console, the AWS CLI, and the Amazon ECR API.

Using AWS Identity and Access Management (IAM), you can control which users in your AWS account have permission
to create, edit, or delete tags. For information about tags in IAM policies, see [Using Tag-Based Access Control](ecr-supported-iam-actions-tagging.md "ecr-supported-iam-actions-tagging.md").

## Tagging your resources for billing

The tags you add to your Amazon ECR repositories are helpful when reviewing cost allocation
after enabling them in your Cost & Usage Report. For more information, see [Amazon ECR usage reports](usage-reports.md "usage-reports.md").

To see the cost of your combined resources, you can organize your billing information
based on resources that have the same tag key values. For example, you can tag several
resources with a specific application name, and then organize your billing information
to see the total cost of that application across several services. For more information
about setting up a cost allocation report with tags, see [The Monthly Cost Allocation
Report](../../../awsaccountbilling/latest/aboutv2/configurecostallocreport.md "../../../awsaccountbilling/latest/aboutv2/configurecostallocreport.md") in the _AWS Billing User Guide_.

###### Note

If you've just enabled reporting, data for the current month is available for
viewing after 24 hours.
