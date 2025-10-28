Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Joining database groups when connecting to a

cluster

Database groups are collections of database users. Database privileges can be
granted to groups. An administrator can configure an IAM role such that these
database groups are taken into account when your SQL runs with the Data API.
For more information about database groups, see [Groups](../dg/r_Groups.md "../dg/r_Groups.md") in the
_Amazon Redshift Database Developer Guide_.

You can configure a Data API caller's IAM role so that the database user
specified in the call joins database groups when the Data API connects to a
cluster. This capability is only supported when connecting to provisioned clusters.
It's not supported when connecting to Redshift Serverless workgroups. The IAM role of the caller
of the Data API must also allow the `redshift:JoinGroup`
action.

Configure this by adding tags to IAM roles. The administrator of the caller's
IAM role adds tags with the key `RedshiftDbGroups` and a key value of a
list of database groups. The value is a list of colon (:) separated names of
database groups up to a total length of 256 characters. The database groups must be
previously defined in the connected database. If any specified group is not found in
the database, it's ignored. For example, for database groups `accounting`
and `retail`, the key-value is `accounting:retail`. The tag
key-value pair `{"Key":"RedshiftDbGroups","Value":"accounting:retail"}`
is used by the Data API to determine which database groups are associated with
the provided database user in the call to the Data API.

###### To join database groups

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the console, choose **Roles**
   and then choose the name of the role that you want to edit.
3. Choose the **Tags** tab, then choose **Manage
   tags**.
4. Choose **Add tag**, then add the key
   **RedshiftDbGroups** and a value which is a list of
   `database-groups-colon-separated`.
5. Choose **Save changes**.

Now when an IAM principal (with this IAM role attached) calls the
Data API, the specified database user joins the database groups
specified in the IAM role.
For more information on how to attach a tag to a principal, including IAM roles
and IAM users, see [Tagging IAM resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the
_IAM User Guide_.
