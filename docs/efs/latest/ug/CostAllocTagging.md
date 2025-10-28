# Using cost allocation EFS file system tags

To track the storage cost or other criteria for individual projects or groups of projects,
label your EFS file systems using cost allocation tags. A _cost allocation
tag_ is a key-value pair that you associate with a file system. After you
activate cost allocation tags, AWS uses the tags to organize your resource costs on your
cost allocation report.

The _cost allocation report_ lists the AWS usage for your account by
product category and linked account user. The report contains the same line items as the
detailed billing report (see [Understanding billing and
usage reports for Amazon EFS](billing-usage-reports-understand.md "billing-usage-reports-understand.md")) and additional columns for your tag
keys.

AWS provides two types of cost allocation tags, _AWS-generated tags_ and _user-defined
tags_. AWS defines, creates, and applies the AWS-generated `aws:createdBy` tag key for
you after an Amazon EFS CreateFileSystem event. You define, create, and apply
_user-defined_ tags to your file systems.

You must activate both types of tags separately in the Billing and Cost Management console before they can appear
in your billing reports. For more information about AWS-generated tags, see [Organizing and tracking costs using AWS cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the
_AWS Billing User Guide_.

- For more information about creating user-defined tags for EFS resources, see [Tagging EFS resources](manage-fs-tags.md "manage-fs-tags.md").
- For more information about activating user-defined tags in the Billing and Cost Management console, see [Activating user-defined cost allocation tags](../../../awsaccountbilling/latest/aboutv2/activating-tags.md "../../../awsaccountbilling/latest/aboutv2/activating-tags.md") in the
  _AWS Billing User Guide_.
- For more information about activating AWS-generated tags in the Billing and Cost Management console, see [Activating
  AWS-generated cost allocation tags](../../../awsaccountbilling/latest/aboutv2/activate-built-in-tags.md "../../../awsaccountbilling/latest/aboutv2/activate-built-in-tags.md") in the
  _AWS Billing User Guide_.

## User-defined cost allocation tags

A user-defined cost allocation tag has the following components:

- The tag key. The tag key is the name of the tag. For example, in the tag
  project/Trinity, project is the key. The tag key is a case-sensitive string that
  can contain 1 to 128 Unicode characters.

- The tag value. The tag value is a required string. For example, in the tag
  project/Trinity, Trinity is the value. The tag value is a case-sensitive string
  that can contain from 0 to 256 Unicode characters.

For more
information about user-defined tags, see [Using user-defined cost
allocation tags](../../../awsaccountbilling/latest/aboutv2/custom-tags.md "../../../awsaccountbilling/latest/aboutv2/custom-tags.md") in the _AWS Billing User Guide_.
