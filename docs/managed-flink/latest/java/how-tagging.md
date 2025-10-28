Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Add tags to Managed Service for Apache Flink applications

This section describes how to add key-value metadata tags to Managed Service for Apache Flink applications. These tags can be used for the following purposes:

- Determining billing for individual Managed Service for Apache Flink applications. For more information, see
  [Using Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md")
  in the _Billing and Cost Management Guide_.
- Controlling access to application resources based on tags. For more information, see
  [Controlling Access Using Tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md")
  in the _AWS Identity and Access Management User Guide_.
- User-defined purposes. You can define application functionality based on the presence of user tags.
  Note the following information about tagging:

- The maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.
- If an action includes a tag list that has duplicate `Key` values, the service throws an `InvalidArgumentException`.

###### This topic contains the following sections:

- [Add tags when an application is created](how-tagging-create.md "how-tagging-create.md")
- [Add or update tags for an existing application](how-tagging-add.md "how-tagging-add.md")
- [List tags for an application](how-tagging-list.md "how-tagging-list.md")
- [Remove tags from an application](how-tagging-remove.md "how-tagging-remove.md")
