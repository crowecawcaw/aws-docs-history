# Creating a cluster with Tez

To install Tez, choose Apache Tez as an application when you create your
cluster.

###### To create a cluster with Tez installed using the

console

1. Navigate to the new Amazon EMR console and select **Switch to the old console** from the side navigation. For more information on what to expect when you switch to the old console, see [Using the old console](../ManagementGuide/whats-new-in-console.md#console-opt-in "../ManagementGuide/whats-new-in-console.md#console-opt-in").
2. Choose **Create cluster**, **Go to advanced options**.
3. Under **Software Configuration**, select a
   **Release** of **emr-4.7.0** or
   higher.
4. Select **Tez** along with other applications you want Amazon EMR
   to install.
5. Select other options as necessary and then choose **Create
   cluster**.

###### To create a cluster with Tez using the AWS CLI

- Use the `create-cluster` command along with the `--
applications` option to specify **Tez**. The
  following example creates a cluster with Tez installed.

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

```
aws emr create-cluster --name "`Cluster with Tez`" --release-label `emr-7.10.0` \
--applications Name=Tez --ec2-attributes KeyName=`myKey` \
--instance-type `m5.xlarge` --instance-count `3` --use-default-roles
```
