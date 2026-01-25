# Turn off Amazon Keyspaces auto scaling for a table

You can turn off Amazon Keyspaces auto scaling for your table at any time. If you no longer
need to scale your table's read or write capacity, you should consider turning off auto
scaling so that Amazon Keyspaces doesn't continue modifying your table’s read or write capacity
settings. You can update the table using the console, CQL, or the AWS CLI.

Turning off auto scaling also deletes the CloudWatch alarms that were created on your behalf.

To delete the service-linked role used by Application Auto Scaling to access your Amazon Keyspaces table,
follow the steps in [Deleting a service-linked role for
Amazon Keyspaces](using-service-linked-roles-app-auto-scaling.md#delete-service-linked-role-app-auto-scaling "using-service-linked-roles-app-auto-scaling.md#delete-service-linked-role-app-auto-scaling").

###### Note

To delete the service-linked role that Application Auto Scaling uses, you must disable automatic
scaling on all tables in the account across all AWS Regions.

Console
**Turn off Amazon Keyspaces automatic scaling for your table using the console**

###### Using the Amazon Keyspaces console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. Choose the table you want to update and go to the
   **Capacity** tab.
3. In the **Capacity
   settings** section, choose **Edit**.
4. To disable Amazon Keyspaces automatic scaling, clear the **Scale automatically**
   check box. Disabling automatic scaling deregisters the table as a scalable target with
   Application Auto Scaling.

Cassandra Query Language (CQL)
**Turn off Amazon Keyspaces automatic scaling for your table using CQL**

The following statement turns off auto scaling for write capacity of the table _mytable_.

```
ALTER TABLE mykeyspace.mytable
WITH AUTOSCALING_SETTINGS = {
    'provisioned_write_capacity_autoscaling_update': {
        'autoscaling_disabled': true
    }
};
```

CLI
**Turn off Amazon Keyspaces automatic scaling for your table using the AWS CLI**

The following command turns off auto scaling for the table's read capacity. It
also deletes the CloudWatch alarms that were created on your behalf.

```
aws keyspaces update-table --keyspace-name mykeyspace --table-name mytable
            \ --auto-scaling-specification readCapacityAutoScaling={autoScalingDisabled=true}
```
