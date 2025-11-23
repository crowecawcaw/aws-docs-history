# Disable Amazon EC2 High Availability for SQL Server

You can disable Amazon EC2 High Availability for SQL Server (SQL HA). Note only instances enabled by SQL HA can receive
the SQL Server license savings. Use one of the following methods to disable SQL HA for your
instances:

Console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation panel, choose **Instances**.
3. Select the instances in the High Availability deployment to enable SQL HA standby
   detection monitoring, choose **Actions**, **Instance
   settings**, **Modify SQL High Availability settings**.
4. In the **Review prerequisites** step, choose
   **Next**. The prerequisites only apply for enabling the
   monitoring, and it is not necessary to review them for disabling SQL HA
   standby detection monitoring.
5. In the **Manage SQL High Availability license savings** step, for each
   instance to disable, for **SQL High Availability license savings**, select
   **None**.
6. Choose **Next**.
7. In the **Review and apply changes** step, review the
   configuration and then choose **Apply changes**.

AWS CLI
Use the [disable-instance-sql-ha-standby-detections](../../../cli/latest/reference/ec2/disable-instance-sql-ha-standby-detections.md "../../../cli/latest/reference/ec2/disable-instance-sql-ha-standby-detections.md") command. For
`instance-ids`, specify the IDs of the instances to disable.

```
aws ec2 disable-instance-sql-ha-standby-detections \
--instance-ids `instance_ids`
```
