# Create a cluster with

Hudi installed

With Amazon EMR release version 5.28.0 and later, Amazon EMR installs Hudi components by
default when Spark, Hive, or Presto is installed. To use Hudi on Amazon EMR, create a
cluster with one or more of the following applications installed:

- Hadoop
- Hive
- Spark
- Presto
- Flink
  You can create a cluster using the AWS Management Console, the AWS CLI, or the Amazon EMR API.

1. Navigate to the new Amazon EMR console and select **Switch to the old console** from the side navigation. For more information on what to expect when you switch to the old console, see [Using the old console](../ManagementGuide/whats-new-in-console.md#console-opt-in "../ManagementGuide/whats-new-in-console.md#console-opt-in").
2. Choose **Create cluster**, **Go to advanced options**.
3. Under Software Configuration, choose **emr-5.28.0**
   or later for **Release** and select
   **Hadoop**, **Hive**,
   **Spark**, **Presto**, and
   **Tez** along with other applications that your
   cluster requires.
4. Configure other options as required for your application, and then
   choose **Next**.
5. Configure options for **Hardware** and
   **General cluster settings** as desired.
6. For **Security Options**, we recommend that you
   select an **EC2 key pair** that you can use to connect
   to the master node command line using SSH. This allows you to run the
   Spark shell commands, Hive CLI commands, and Hudi CLI commands
   described in this guide.
7. Choose other security options as desired, and then choose
   **Create cluster**.
