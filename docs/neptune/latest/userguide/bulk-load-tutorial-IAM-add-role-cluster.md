

# Adding the IAM Role to an Amazon Neptune Cluster
<a name="bulk-load-tutorial-IAM-add-role-cluster"></a>

Use the console to add the IAM role to an Amazon Neptune cluster. This allows any Neptune DB instance in the cluster to assume the role and load from Amazon S3.

**Note**  
The Amazon Neptune console requires the user to have the following IAM permissions to attach the role to the Neptune cluster:  

```
iam:GetAccountSummary on resource: *
iam:ListAccountAliases on resource: *
iam:PassRole on resource: * with iam:PassedToService restricted to rds.amazonaws.com
```

**To add an IAM role to an Amazon Neptune cluster**

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home).

1. In the navigation pane, choose **Databases**.

1. Choose the cluster identifier for the cluster that you want to modify.

1. Choose the **Connectivity & Security** tab.

1. In the IAM Roles section, choose the role you created in the previous section.

1. Choose **Add role**.

1. Wait until the IAM role becomes accessible to the cluster before you use it.