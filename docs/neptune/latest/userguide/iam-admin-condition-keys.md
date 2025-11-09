# IAM condition keys for administering Amazon Neptune

[Using condition keys](security-iam-access-manage.md#iam-using-condition-keys "security-iam-access-manage.md#iam-using-condition-keys"), you can
specify conditions in an IAM policy statement so that the statement takes effect
only when the conditions are true. The condition keys that you can use in Neptune
administrative policy statements fall into the following categories:

- [Global condition keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md")   –  
  These are defined by AWS for general use with AWS services. Most can be used
  in Neptune administrative policy statements.
- [Administrative resource property condition keys](#iam-rds-property-condition-keys "#iam-rds-property-condition-keys")   –  
  These keys, listed [below](#iam-rds-property-condition-keys "#iam-rds-property-condition-keys"), are
  based on properties of administrative resources.
- [Tag-based access condition keys](#iam-rds-tag-based-condition-keys "#iam-rds-tag-based-condition-keys")   –  
  These keys, listed [below](#iam-rds-tag-based-condition-keys "#iam-rds-tag-based-condition-keys"), are
  based on [AWS tags](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") attached to
  administrative resources.

## Neptune administrative resource property condition keys

| Condition keys       | Description                                                                                                                                                                                            | Type    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| `rds:DatabaseClass`  | Filters access by the type of DB instance class.                                                                                                                                                       | String  |
| `rds:DatabaseEngine` | Filters access by the database engine. For possible values refer to the engine parameter in CreateDBInstance API                                                                                       | String  |
| `rds:DatabaseName`   | Filters access by the user-defined name of the database on the DB instance                                                                                                                             | String  |
| `rds:EndpointType`   | Filters access by the type of the endpoint. One of: READER, WRITER, CUSTOM                                                                                                                             | String  |
| `rds:Vpc`            | Filters access by the value that specifies whether the DB instance<br>runs in an Amazon Virtual Private Cloud (Amazon VPC). To indicate that the<br>DB instance runs in an Amazon VPC, specify `true`. | Boolean |

## Administrative tag-based condition keys

Amazon Neptune supports specifying conditions in an IAM policy using custom tags,
to control access to Neptune through the [Management API reference](api.md "api.md").

For example, if you add a tag named `environment` to your DB instances, with values
such as `beta`, `staging`, and `production`, you can then create
a policy that restricts access to the instances based on the value of that tag.

###### Important

If you manage access to your Neptune resources using tagging, be sure to secure
access to the tags. You can restrict access to the tags by creating policies for the
`AddTagsToResource` and `RemoveTagsFromResource` actions.

For example, you could use the following policy to deny users the ability to
add or remove tags for all resources. Then, you could create policies to allow
specific users to add or remove tags.

JSON

```
`{ "Version":"2012-10-17",
 "Statement":[
 { "Sid": "DenyTagUpdates",
 "Effect": "Deny",
 "Action": [
 "rds:AddTagsToResource",
 "rds:RemoveTagsFromResource"
 ],
 "Resource":"*"
 }
 ]
}`

```

The following tag-based condition keys only work with administrative resources
in administrative policy statements.

| Tag-based administrative condition keys                                                                                                                                                                                      | Condition keys                                                                       | Description | Type |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ----------- | ---- |
| [`aws:RequestTag/${TagKey}`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag")    | Filters access based on the presence of tag key-value pairs in the request.          | String      |
| [`aws:ResourceTag/${TagKey}`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag") | Filters access based on tag key-value pairs attached to the resource.                | String      |
| [`aws:TagKeys`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keyss "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keyss")                                     | Filters access based on the presence of tag keys in the request.                     | String      |
| `rds:cluster-pg-tag/${TagKey}`                                                                                                                                                                                               | Filters access by the tag attached to a DB cluster parameter group.                  | String      |
| `rds:cluster-snapshot-tag/${TagKey}`                                                                                                                                                                                         | Filters access by the tag attached to a DB cluster snapshot.                         | String      |
| `rds:cluster-tag/${TagKey}`                                                                                                                                                                                                  | Filters access by the tag attached to a DB cluster.                                  | String      |
| `rds:db-tag/${TagKey}`                                                                                                                                                                                                       | Filters access by the tag attached to a DB instance.                                 | String      |
| `rds:es-tag/${TagKey}`                                                                                                                                                                                                       | Filters access by the tag attached to an event subscription.                         | String      |
| `rds:pg-tag/${TagKey}`                                                                                                                                                                                                       | Filters access by the tag attached to a DB parameter group.                          | String      |
| `rds:req-tag/${TagKey}`                                                                                                                                                                                                      | Filters access by the set of tag keys and values that can be used to tag a resource. | String      |
| `rds:secgrp-tag/${TagKey}`                                                                                                                                                                                                   | Filters access by the tag attached to a DB security group.                           | String      |
| `rds:snapshot-tag/${TagKey}`                                                                                                                                                                                                 | Filters access by the tag attached to a DB snapshot.                                 | String      |
| `rds:subgrp-tag/${TagKey}`                                                                                                                                                                                                   | Filters access by the tag attached to a DB subnet group                              | String      |
