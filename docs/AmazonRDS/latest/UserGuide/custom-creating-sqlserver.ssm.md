

# Connecting to your RDS Custom DB instance using AWS Systems Manager
<a name="custom-creating-sqlserver.ssm"></a>

After you create your RDS Custom DB instance, you can connect to it using AWS Systems Manager Session Manager. Session Manager is a Systems Manager capability that you can use to manage Amazon EC2 instances through a browser-based shell or through the AWS CLI. For more information, see [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html).

## Console
<a name="custom-creating-sqlserver.ssm.CON"></a>

**To connect to your DB instance using Session Manager**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the RDS Custom DB instance to which you want to connect.

1. Choose **Configuration**.

1. Note the **Resource ID** value for your DB instance. For example, the resource ID might be `db-ABCDEFGHIJKLMNOPQRS0123456`.

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Look for the name of your EC2 instance, and then choose the instance ID associated with it. For example, the instance ID might be `i-abcdefghijklm01234`.

1. Choose **Connect**.

1. Choose **Session Manager**.

1. Choose **Connect**.

   A window opens for your session.

## AWS CLI
<a name="custom-creating-sqlserver.ssm.CLI"></a>

You can connect to your RDS Custom DB instance using the AWS CLI. This technique requires the Session Manager plugin for the AWS CLI. To learn how to install the plugin, see [Install the Session Manager plugin for the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html).

To find the DB resource ID of your RDS Custom DB instance, use `[describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html)`.

```
aws rds describe-db-instances \
    --query 'DBInstances[*].[DBInstanceIdentifier,DbiResourceId]' \
    --output text
```

The following sample output shows the resource ID for your RDS Custom instance. The prefix is `db-`.

```
db-ABCDEFGHIJKLMNOPQRS0123456
```

To find the EC2 instance ID of your DB instance, use `aws ec2 describe-instances`. The following example uses `db-ABCDEFGHIJKLMNOPQRS0123456` for the resource ID.

```
aws ec2 describe-instances \
    --filters "Name=tag:Name,Values={{db-ABCDEFGHIJKLMNOPQRS0123456}}" \
    --output text \
    --query 'Reservations[*].Instances[*].InstanceId'
```

The following sample output shows the EC2 instance ID.

```
i-abcdefghijklm01234
```

Use the `aws ssm start-session` command, supplying the EC2 instance ID in the `--target` parameter.

```
aws ssm start-session --target "i-abcdefghijklm01234"
```

A successful connection looks like the following.

```
Starting session with SessionId: yourid-abcdefghijklm1234
[ssm-user@ip-123-45-67-89 bin]$
```