# Managing data migrations

After using the **Migrate data from EC2 database** action from the RDS console,
RDS starts the migration automatically.

If you used the AWS DMS console to create the migration resources, you can start the migration process.

## Starting the data migration

Follow these steps to start data migration:

###### Starting a data migration

1. Choose the target database on the **Databases** page in the RDS console.
2. In the database details page, choose the **Data migrations** tab.
3. Under the **Data migrations** tab, the
   **Associated data migrations** lists the available data migrations.

Migrations set up using the RDS
console start automatically once the required resources are set up.

Migrations set up using the DMS console are set to **Ready**.

To begin these migrations, select the **Actions**
drop down and select **Start**. 4. This begins the data migration for your EC2 database.

## Stopping the data migration

For data migrations whose replication type is full load, stopping the migration
causes the process to stop and can't be resumed. Once stopped, you must restart the
migration.

For migrations with replication type set to change data capture (CDC) or full load and CDC,
you can stop the continuous replication process, and resume the process later.

###### Stopping a data migration

1. Choose the target database on the **Databases** page in the RDS console.
2. In the database details page, choose the **Data migrations** tab.
3. Under the **Data migrations** tab, the
   **Associated data migrations** lists the ongoing data migrations.

To stop a migration, select a data migration and select **Stop**
in the **Actions** drop down. 4. This stops the data migration for your EC2 database.

## Resuming the data migration

For data migrations whose replication type is full load and change data capture (CDC)
or change data capture (CDC) migration, you can resume the CDC process from the last stop point.

###### Resuming a data migration

1. Choose the target database on the **Databases** page in the RDS console.
2. In the database details page, choose the **Data migrations** tab.
3. Under the **Data migrations** tab, the
   **Associated data migrations** lists the stopped data migrations.

To resume a migration, select a data migration and select **Resume processing**
in the **Actions** drop down. 4. This resume the data migration for your EC2 database.

## Deleting the data migration

To delete an associated data migration, use the following instructions

###### Deleting a data migration

1. Choose the target database on the **Databases** page in the RDS console.
2. In the database details page, choose the **Data migrations** tab.
3. To delete a migration, select a data migration and select **Delete**
   in the **Actions** drop down.
4. This deletes the data migration.

Deleting a data migration that was in progress doesn't impact
any data that has already been loaded to the target database.

## Restarting the data migration

To restart an associated data migration from a CDC start point, use the following instructions

###### Restarting a data migration

1. Choose the target database on the **Databases** page in the RDS console.
2. In the database details page, choose the **Data migrations** tab.
3. To restart a migration, select a data migration and select **Restart**
   in the **Actions** drop down.
4. This restarts the data migration from a CDC start point.

Restarting a data migration that was in progress doesn't impact
any data that has already been loaded to the target database.
