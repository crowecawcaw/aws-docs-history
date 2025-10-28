# Turn off auto scaling for a table in Amazon Keyspaces

This section provides examples of how to turn off auto scaling for a multi-Region table in provisioned capacity mode. You can
do this on the Amazon Keyspaces console, using CQL or the AWS CLI.

###### Important

We recommend using auto scaling for multi-Region tables that use provisioned
capacity mode. For more information, see [Estimate and provision capacity for a multi-Region table in Amazon Keyspaces](tables-multi-region-capacity.md "tables-multi-region-capacity.md").

###### Note

To delete the service-linked role that Application Auto Scaling uses, you must disable
automatic scaling on all tables in the account across all
AWS Regions.

Console

###### Turn off Amazon Keyspaces automatic scaling for an existing multi-Region table on the console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. Choose the table that you want to work with and choose the
   **Capacity** tab.
3. In the **Capacity settings** section, choose **Edit**.
4. To disable Amazon Keyspaces automatic scaling, clear the **Scale automatically** check
   box. Disabling automatic scaling deregisters the table as a scalable target with
   Application Auto Scaling. To delete the service-linked role that Application Auto Scaling uses to access your
   Amazon Keyspaces table, follow the steps in [Deleting a service-linked role for
   Amazon Keyspaces](using-service-linked-roles-app-auto-scaling.md#delete-service-linked-role-app-auto-scaling "using-service-linked-roles-app-auto-scaling.md#delete-service-linked-role-app-auto-scaling").
5. When the automatic scaling settings are defined, choose
   **Save**.

Cassandra Query Language (CQL)

###### Turn off auto scaling for a

multi-Region table using CQL

- You can use `ALTER TABLE` to turn off auto scaling for an existing table.
  Note that you can't turn off auto scaling for an individual table replica.

In the following example, auto scaling is turned off for the table's read capacity.

```
ALTER TABLE mykeyspace.mytable
WITH AUTOSCALING_SETTINGS = {
    'provisioned_read_capacity_autoscaling_update': {
        'autoscaling_disabled': true
    }
};
```

CLI

###### Turn off auto scaling for a

multi-Region table using the AWS CLI

- You can use the AWS CLI `update-table` command to turn off auto scaling for
  an existing table. Note that you can't turn off auto scaling for an individual table
  replica.

In the following example, auto scaling is turned off for the table's read
capacity.

```
aws keyspaces update-table --keyspace-name mykeyspace --table-name mytable
           \ --auto-scaling-specification readCapacityAutoScaling={autoScalingDisabled=true}
```
