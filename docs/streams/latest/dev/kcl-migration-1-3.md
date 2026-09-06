

# Migrating from KCL 1.x to KCL 3.x
<a name="kcl-migration-1-3"></a>

This topic explains the instructions to migrate your consumer from KCL 1.x to KCL 3.x. KCL 1.x uses different classes and interfaces compared to KCL 2.x and KCL 3.x. You must migrate the record processor, record processor factory, and worker classes to the KCL 2.x/3.x compatible format first, and follow the migration steps for KCL 2.x to KCL 3.x migration. You can directly upgrade from KCL 1.x to KCL 3.x.

**Important**  
We recommend that you migrate to KCL 3.5 or later, which uses single table format by default for new migrations. First, migrate your record processor, factory, and worker classes to the KCL 2.x/3.x compatible format using the steps on this page. Then, follow the migration path from KCL 2.x to KCL 3.5. Single table format is automatically enabled for new migrations from 2.x. For more information, see [Single table format for KCL](kcl-single-table-format.md).
+ **Step 1: Migrate the record processor**

  Follow the [Migrate the record processor](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration.html#recrod-processor-migration) section in the [Migrate consumers from KCL 1.x to KCL 2.x](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration.html#recrod-processor-migration) page.
+ **Step 2: Migrate the record processor factory**

  Follow the [Migrate the record processor factory](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration.html#recrod-processor-factory-migration) section in the [Migrate consumers from KCL 1.x to KCL 2.x](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration.html#recrod-processor-migration) page.
+ **Step 3: Migrate the worker**

  Follow the [Migrate the worker](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration.html#worker-migration) section in the [Migrate consumers from KCL 1.x to KCL 2.x](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration.html#recrod-processor-migration) page.
+ **Step 4: Migrate KCL 1.x configuration **

  Follow the [Configure the Amazon Kinesis client](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration.html#client-configuration) section in the [Migrate consumers from KCL 1.x to KCL 2.x](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration.html#recrod-processor-migration) page.
+ **Step 5: Check idle time removal and client configuration removals**

  Follow the [Idle time removal ](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration.html#idle-time-removal)and [Client configuration removals](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration.html#client-configuration-removals) sections in the [Migrate consumers from KCL 1.x to KCL 2.x](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration.html#recrod-processor-migration) page.
+ **Step 6: Follow the step-by-step instructions in the KCL 2.x to KCL 3.x migration guide**

  Follow instructions on the [Migrate from KCL 2.x to KCL 3.x](kcl-migration-from-2-3.md) page to complete the migration. If you need to roll back to the previous KCL version or roll forward to KCL 3.x after a rollback, refer to [Roll back to the previous KCL version](kcl-migration-rollback.md) and [Roll forward to KCL 3.5.x after a rollback from KCL 3.5.x](kcl-migration-rollforward.md).

**Important**  
Do not use AWS SDK for Java version 2.27.19 to 2.27.23 with KCL 3.x. These versions include an issue that causes an exception error related to KCL's DynamoDB usage. We recommend that you use the AWS SDK for Java version 2.28.0 or later to avoid this issue. 