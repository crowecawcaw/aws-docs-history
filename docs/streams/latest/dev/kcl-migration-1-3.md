# Migrating from KCL 1.x to KCL

3.x

This topic explains the instructions to migrate your consumer from KCL 1.x to
KCL 3.x. KCL 1.x uses different classes and interfaces compared to
KCL 2.x and KCL 3.x. You must migrate the record processor, record
processor factory, and worker classes to the KCL 2.x/3.x compatible format
first, and follow the migration steps for KCL 2.x to KCL 3.x
migration. You can directly upgrade from KCL 1.x to KCL 3.x.

- **Step 1: Migrate the record processor**

Follow the [Migrate the record processor](kcl-migration.md#recrod-processor-migration "kcl-migration.md#recrod-processor-migration") section in the [Migrate consumers from KCL 1.x to KCL 2.x](kcl-migration.md#recrod-processor-migration "kcl-migration.md#recrod-processor-migration") page.

- **Step 2: Migrate the record processor
  factory**

Follow the [Migrate the record processor factory](kcl-migration.md#recrod-processor-factory-migration "kcl-migration.md#recrod-processor-factory-migration") section in the [Migrate consumers from KCL 1.x to KCL 2.x](kcl-migration.md#recrod-processor-migration "kcl-migration.md#recrod-processor-migration") page.

- **Step 3: Migrate the worker**

Follow the [Migrate the worker](kcl-migration.md#worker-migration "kcl-migration.md#worker-migration") section in the [Migrate consumers from KCL 1.x to KCL 2.x](kcl-migration.md#recrod-processor-migration "kcl-migration.md#recrod-processor-migration") page.

- **Step 4: Migrate KCL 1.x configuration**

Follow the [Configure the Amazon Kinesis client](kcl-migration.md#client-configuration "kcl-migration.md#client-configuration") section in the [Migrate consumers from KCL 1.x to KCL 2.x](kcl-migration.md#recrod-processor-migration "kcl-migration.md#recrod-processor-migration") page.

- **Step 5: Check idle time removal and client configuration
  removals**

Follow the [Idle time removal](kcl-migration.md#idle-time-removal "kcl-migration.md#idle-time-removal") and [Client configuration removals](kcl-migration.md#client-configuration-removals "kcl-migration.md#client-configuration-removals") sections in the [Migrate consumers from KCL 1.x to KCL 2.x](kcl-migration.md#recrod-processor-migration "kcl-migration.md#recrod-processor-migration") page.

- **Step 6: Follow the step-by-step instructions in the
  KCL 2.x to KCL 3.x migration guide**

Follow instructions on the [Migrate from KCL 2.x to KCL
3.x](kcl-migration-from-2-3.md "kcl-migration-from-2-3.md") page to complete the migration. If
you need to roll back to the previous KCL version or roll forward to KCL 3.x
after a rollback, refer to [Roll back to the previous KCL
version](kcl-migration-rollback.md "kcl-migration-rollback.md") and [Roll forward to KCL 3.x after a
rollback](kcl-migration-rollforward.md "kcl-migration-rollforward.md").

###### Important

Do not use AWS SDK for Java version 2.27.19 to 2.27.23 with KCL 3.x. These
versions include an issue that causes an exception error related to KCL's
DynamoDB usage. We recommend that you use the AWS SDK for Java version 2.28.0 or later to
avoid this issue.
