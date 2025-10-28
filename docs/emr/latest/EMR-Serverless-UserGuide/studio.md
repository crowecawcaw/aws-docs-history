# Creating an EMR Serverless application from the EMR Studio

console

From the EMR Studio console, create, access, and manage EMR Serverless
applications. To navigate to the EMR Studio console, follow the instructions in [Getting started
from the console](getting-started.md#gs-console "getting-started.md#gs-console").

## Create an application

With the **Create application** page, create an EMR Serverless
application by following these steps.

1. In the **Name** field, enter the name you want to call your
   application.
2. In the **Type** field, choose Spark or Hive as the type of the
   application.
3. In the **Release version** field, choose the EMR release
   number.
4. In the **Architecture** options, choose the instruction set
   architecture to use. For more information, refer to [Amazon EMR Serverless architecture options](architecture.md "architecture.md").
   - **arm64** — 64-bit ARM architecture; to use
     Graviton processors
   - **x86_64** — 64-bit x86 architecture; to use
     x86-based processors

5. There are two application setup options for the remaining fields: default settings
   and custom settings. These fields are optional.

**Default settings** — Default settings allow you to create
an application quickly with pre-initialized capacity. This includes one driver and one
executor for Spark, and one driver and one Tez Task for Hive. The default settings don't
enable network connectivity to your VPCs. The application is configured to stop if idle
for 15 minutes, and auto-starts on job submission.

**Custom settings** — Custom settings allow you to modify
the following properties.

    * **Pre-initialized capacity** — The number of drivers and
     executors or Hive Tez Task workers, and the size of each worker.
    * **Application limits** — The maximum capacity of an
     application.
    * **Application behavior** — The application's auto-start
     and auto-stop behavior.
    * **Network connections** — Network connectivity to VPC
     resources.
    * **Tags** — Custom tags that assign to the
     application.

For more information about pre-initialized capacity, application limits, and
application behavior, refer to [Configuring an application when working with EMR Serverless](application-capacity.md "application-capacity.md"). For more information about network
connectivity, refer to [Configuring VPC access for EMR Serverless applications to connect to data](vpc-access.md "vpc-access.md"). 6. To create the application, choose **Create application** .
