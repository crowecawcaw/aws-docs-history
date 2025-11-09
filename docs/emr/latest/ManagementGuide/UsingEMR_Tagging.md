# View cluster instances in Amazon EC2

To help you manage your resources, Amazon EC2 allows you to assign metadata to resources in
the form of tags. Each Amazon EC2 tag consists of a key and a value. Tags allow you to categorize
your Amazon EC2 resources in different ways: for example, by purpose, owner, or environment.

You can search and filter resources based on the tags. The tags that you assign to
resources through your AWS account are available only to you. Other accounts that share
the same resource can't view your tags.

Amazon EMR automatically tags each EC2 instance that it launches with key-value pairs. The keys
identify the cluster and the instance group to which the instance belongs. This makes it
easy to filter your EC2 instances to show, for example, only those instances that belong to
a particular cluster, or to show all of the currently running instances in the instance
group for the task. This is especially useful if you run several clusters concurrently or
manage large numbers of EC2 instances.

These are the predefined key-value pairs that Amazon EMR assigns:

| Key                                      | Value                 | Value definition                                                                                                                                |
| ---------------------------------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| aws:elasticmapreduce:job-flow-id         | `job-flow-identifier` | The ID of the cluster that the instance is provisioned for. It appears in the<br>format `j-XXXXXXXXXXXXX` and can be up to 256 characters long. |
| aws:elasticmapreduce:instance-group-role | `group-role`          | The type of instance group, entered as one of the following values:<br>`master`, `core`, or `task`.                                             |

You can view and filter on the tags that Amazon EMR adds. For more information, see [Using tags](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md") in the
_Amazon EC2 User Guide_. Because the tags set by Amazon EMR are system tags and
cannot be edited or deleted, the sections on displaying and filtering tags are the most
relevant.

###### Note

Amazon EMR adds tags to the EC2 instance when its status updates to **Running**. If latency occurs between the time that the EC2 instance is
provisioned and the time that its status is set to **Running**, the tags that Amazon EMR sets will appear once the instance starts.
If you don't see the tags, wait for a few minutes and refresh the view.
