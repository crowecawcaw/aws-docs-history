# Comparing DB parameter groups

You can use the AWS Management Console to view the differences between two DB parameter groups.

The specified parameter groups must both be DB parameter groups, or they both must be DB cluster parameter groups. This is
true even when the DB engine and version are the same. For example, you can't compare an `aurora-mysql8.0`
(Aurora MySQL version 3) DB parameter group and an `aurora-mysql8.0` DB cluster parameter group.

You can compare Aurora MySQL and RDS for MySQL DB parameter groups, even for different versions, but you can't compare
Aurora PostgreSQL and RDS for PostgreSQL DB parameter groups.

###### To compare two DB parameter groups

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter
   groups**.
3. In the list, choose the two parameter groups that you want to compare.

###### Note

To compare a default parameter group to a custom parameter group, first choose the default parameter group on the
**Default** tab, then choose the custom parameter group on the **Custom**
tab. 4. From **Actions**, choose **Compare**.
