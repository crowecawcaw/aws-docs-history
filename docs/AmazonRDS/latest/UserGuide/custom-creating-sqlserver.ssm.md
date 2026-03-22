# Connecting to your RDS Custom DB instance using AWS Systems Manager

After you create your RDS Custom DB instance, you can connect to it using AWS Systems Manager
Session Manager. Session Manager is a Systems Manager capability that you can use to manage Amazon EC2
instances through a browser-based shell or through the AWS CLI. For more information, see
[AWS Systems Manager Session Manager](../../../systems-manager/latest/userguide/session-manager.md "../../../systems-manager/latest/userguide/session-manager.md").

###### To connect to your DB instance using Session Manager

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the RDS Custom DB instance to which
   you want to connect.
3. Choose **Configuration**.
4. Note the **Resource ID** value for your DB instance.
   For example, the resource ID might be
   `db-ABCDEFGHIJKLMNOPQRS0123456`.
5. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
6. In the navigation pane, choose **Instances**.
7. Look for the name of your EC2 instance, and then choose the instance ID associated with it. For example, the
   instance ID might be `i-abcdefghijklm01234`.
8. Choose **Connect**.
9. Choose **Session Manager**.
10. Choose **Connect**.

A window opens for your session.
You can connect to your RDS Custom DB instance using the AWS CLI. This technique requires the Session Manager plugin for the
AWS CLI. To learn how to install the plugin, see [Install the Session Manager plugin for the AWS CLI](../../../systems-manager/latest/userguide/session-manager-working-with-install-plugin.md "../../../systems-manager/latest/userguide/session-manager-working-with-install-plugin.md").

To find the DB resource ID of your RDS Custom DB instance, use `describe-db-instances`.

```
aws rds describe-db-instances \
    --query 'DBInstances[*].[DBInstanceIdentifier,DbiResourceId]' \
    --output text
```

The following sample output shows the resource ID for your RDS Custom instance. The prefix is `db-`.

```
db-ABCDEFGHIJKLMNOPQRS0123456
```

To find the EC2 instance ID of your DB instance, use `aws ec2 describe-instances`. The following example
uses `db-ABCDEFGHIJKLMNOPQRS0123456` for the resource ID.

```
aws ec2 describe-instances \
    --filters "Name=tag:Name,Values=`db-ABCDEFGHIJKLMNOPQRS0123456`" \
    --output text \
    --query 'Reservations[*].Instances[*].InstanceId'
```

The following sample output shows the EC2 instance ID.

```
i-abcdefghijklm01234
```

Use the `aws ssm start-session` command, supplying the EC2 instance ID in the `--target`
parameter.

```
aws ssm start-session --target "i-abcdefghijklm01234"
```

A successful connection looks like the following.

```
Starting session with SessionId: yourid-abcdefghijklm1234
[ssm-user@ip-123-45-67-89 bin]$
```
