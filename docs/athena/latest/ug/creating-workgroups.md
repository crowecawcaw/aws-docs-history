

# Create a workgroup
<a name="creating-workgroups"></a>

Creating a workgroup requires permissions to `CreateWorkgroup` API actions. See [Configure access to workgroups and tags](workgroups-access.md) and [Use IAM policies to control workgroup access](workgroups-iam-policy.md). If you are adding tags, you also need to add permissions to `TagResource`. See [Tag policy examples for workgroups](tags-access-control.md#tag-policy-examples-workgroups).

The following procedure shows how to use the Athena console to create a workgroup. To create a workgroup using the Athena API, see [CreateWorkGroup](https://docs.aws.amazon.com/athena/latest/APIReference/API_CreateWorkGroup.html).

**To create a workgroup in the Athena console**

1.  Decide which workgroups to create. A few factors to consider include:
   + Who can run queries in each workgroup, and who owns workgroup configuration. Use IAM policies to enforce workgroup permissions. For more information, see [Use IAM policies to control workgroup access](workgroups-iam-policy.md).
   + The location in Amazon S3 to use for the query results for the workgroup. All users of the workgroup must have access to this location.
   + Whether the workgroup query results must be encrypted. Because encryption is per-workgroup (not per query), you should create separate workgroups for encrypted and non-encrypted query results. For more information, see [Encrypt Athena query results stored in Amazon S3](encrypting-query-results-stored-in-s3.md).

1. If the console navigation pane is not visible, choose the expansion menu on the left.  
![Choose the expansion menu.](http://docs.aws.amazon.com/athena/latest/ug/images/nav-pane-expansion.png)

1. In the Athena console navigation pane, choose **Workgroups**.

1. On the **Workgroups** page, choose **Create workgroup**. 

1. On the **Create workgroup** page, fill in the fields as follows:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/athena/latest/ug/creating-workgroups.html)

1. Choose **Create workgroup**. The workgroup appears in the list on the **Workgroups** page.

   In the query editor, Athena displays the current workgroup in the **Workgroup** option on the upper right of the console. You can use this option to switch workgroups. When you run queries, they run in the current workgroup.

1. Create IAM policies for your users, groups, or roles to enable their access to workgroups. The policies establish the workgroup membership and access to actions on a `workgroup` resource. For more information, see [Use IAM policies to control workgroup access](workgroups-iam-policy.md). For example JSON policies, see [Configure access to workgroups and tags](workgroups-access.md).

1. (Optional) Configure a minimal level of encryption in Amazon S3 for all query results from the workgroup when workgroup-wide encryption is not enforced by the override client-side settings option. You can use this feature to ensure that query results are never stored in an Amazon S3 bucket in an unencrypted state. For more information, see [Configure minimum encryption for a workgroup](workgroups-minimum-encryption.md).

1. (Optional) Use Amazon CloudWatch and Amazon EventBridge to monitor your workgroup's queries and control costs. For more information, see [Use CloudWatch and EventBridge to monitor queries and control costs](workgroups-control-limits.md).

1. (Optional) Use the Billing and Cost Management console to tag the workgroup with cost allocation tags. For more information, see [Using user-defined cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/custom-tags.html) in the *AWS Billing User Guide*.

1. (Optional) To get dedicated processing capacity for the queries in the workgroup, add the workgroup to a capacity reservation. You can assign one or more workgroups to a reservation. For more information, see [Manage query processing capacity](capacity-management.md).