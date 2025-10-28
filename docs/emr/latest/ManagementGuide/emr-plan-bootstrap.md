# Create bootstrap actions to install additional

software with an Amazon EMR cluster

You can use a _bootstrap action_ to install
additional software or customize the configuration of cluster instances. Bootstrap actions are scripts that run on cluster after Amazon EMR launches the instance using the Amazon Linux Amazon Machine Image (AMI). Bootstrap actions run before Amazon EMR installs the applications that you specify when you create the cluster and before cluster nodes begin processing data. If you add nodes to a running cluster,
bootstrap actions also run on those nodes in the same way. You can create custom bootstrap actions and
specify them when you create your cluster.

Most predefined bootstrap actions for Amazon EMR AMI versions 2.x and 3.x are not
supported in Amazon EMR releases 4.x. For example, `configure-Hadoop` and
`configure-daemons` are not supported in Amazon EMR release 4.x.
Instead, Amazon EMR release 4.x natively provides this functionality. For more
information about how to migrate bootstrap actions from Amazon EMR AMI versions 2.x
and 3.x to Amazon EMR release 4.x, go to [Customizing cluster and application configuration with earlier AMI versions of Amazon EMR](../ReleaseGuide/emr-3x-customizeappconfig.md "../ReleaseGuide/emr-3x-customizeappconfig.md") in the Amazon EMR Release Guide.

## Bootstrap action basics

Bootstrap actions execute as the Hadoop user by default. You can execute a bootstrap
action with root privileges by using `sudo`.

All Amazon EMR management interfaces support bootstrap actions. You can specify up to 16
bootstrap actions per cluster by providing multiple `bootstrap-actions`
parameters from the console, AWS CLI, or API.

From the Amazon EMR console, you can optionally specify a bootstrap action while creating a
cluster.

When you use the CLI, you can pass references to bootstrap action scripts to Amazon EMR by adding
the `--bootstrap-actions` parameter when you create the cluster using the
`create-cluster` command.

```
--bootstrap-actions Path="s3://`amzn-s3-demo-bucket`/`filename`",Args=[`arg1`,`arg2`]
```

If the bootstrap action returns a nonzero error code, Amazon EMR treats it as a failure and
terminates the instance. If too many instances fail their bootstrap actions, then Amazon EMR
terminates the cluster. If just a few instances fail, Amazon EMR attempts to reallocate the
failed instances and continue. Use the cluster `lastStateChangeReason` error
code to identify failures caused by a bootstrap action.

## Conditionally run a bootstrap action

In order to only run a bootstrap actions on the master node, you can use a custom bootstrap
action with some logic to determine if the node is master.

```
#!/bin/bash
if grep isMaster /mnt/var/lib/info/instance.json | grep false;
then
    echo "This is not master node, do nothing,exiting"
    exit 0
fi
echo "This is master, continuing to execute script"
# continue with code logic for master node below
```

The following output will print from a core node.

```
This is not master node, do nothing, exiting
```

The following output will print from master node.

```
This is master, continuing to execute script
```

To use this logic, upload your bootstrap action, including the above code, to your Amazon S3
bucket. On the AWS CLI, add the `--bootstrap-actions` parameter to the `aws emr
 create-cluster` API call and specify your bootstrap script location as the
value of `Path`.

## Shutdown actions

A bootstrap action script can create one or more shutdown actions by writing
scripts to the
`/mnt/var/lib/instance-controller/public/shutdown-actions/`
directory. When a cluster is terminated, all the scripts in this directory are
executed in parallel. Each script must run and complete within 60 seconds.

Shutdown action scripts are not guaranteed to run if the node terminates with an
error.

###### Note

When using Amazon EMR versions 4.0 and later, you must manually create the `/mnt/var/lib/instance-controller/public/shutdown-actions/` directory on the master node. It doesn't exist by default; however, after being created, scripts in this directory nevertheless run before shutdown. For more information about connecting to the Master node to create directories, see [Connect to the Amazon EMR cluster primary node using
SSH](emr-connect-master-node-ssh.md "emr-connect-master-node-ssh.md").

## Use custom bootstrap actions

You can create a custom script to perform a customized bootstrap action. Any of the
Amazon EMR interfaces can reference a custom bootstrap action.

###### Note

For the best performance, we recommend that you store custom bootstrap actions, scripts, and other files that you want to use with Amazon EMR in an Amazon S3 bucket that is in the same AWS Region as your cluster.

###### Contents

- [Add custom bootstrap actions](#custom-bootstrap "#custom-bootstrap")
- [Use a custom bootstrap action to copy an
  object from Amazon S3 to each node](#CustomBootstrapCopyS3Object "#CustomBootstrapCopyS3Object")

### Add custom bootstrap actions

Console

###### To create a cluster with a bootstrap action with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation pane, choose
   **Clusters**, and then choose
   **Create cluster**.
3. Under **Bootstrap actions**, choose **Add** to
   specify a name, script location, and optional arguments for your
   action. Select **Add bootstrap action**.
4. Optionally, add more bootstrap actions.
5. Choose any other options that apply to your cluster.
6. To launch your cluster, choose **Create
   cluster**.

CLI

###### To create a cluster with a custom bootstrap action with the AWS CLI

When using the AWS CLI to include a bootstrap action, specify the `Path` and
`Args` as a comma-separated list. The following example doesn't
use an arguments list.

- To launch a cluster with a custom bootstrap action, type the following command, replacing
  `myKey` with the name of your EC2 key pair.
  Include `--bootstrap-actions` as a parameter and specify your
  bootstrap script location as the value of `Path`.

      + Linux, UNIX, and Mac OS X users:



      ```
      aws emr create-cluster --name `"Test cluster"` --release-label `emr-4.0.0` \
      --use-default-roles --ec2-attributes KeyName=`myKey` \
      --applications Name=`Hive` Name=`Pig` \
      --instance-count `3` --instance-type `m5.xlarge` \
      --bootstrap-actions Path=`"s3://elasticmapreduce/bootstrap-actions/download.sh"`
      ```
      + Windows users:



      ```
      aws emr create-cluster --name `"Test cluster"` --release-label `emr-4.2.0` --use-default-roles --ec2-attributes KeyName=`myKey` --applications Name=`Hive` Name=`Pig` --instance-count `3` --instance-type `m5.xlarge` --bootstrap-actions Path=`"s3://elasticmapreduce/bootstrap-actions/download.sh"`
      ```

  When you specify the instance count without using the `--instance-groups`
  parameter, a single primary node is launched, and the remaining instances
  are launched as core nodes. All nodes will use the instance type specified
  in the command.

###### Note

If you have not previously created the default Amazon EMR service role and
EC2 instance profile, type `aws emr create-default-roles` to
create them before typing the `create-cluster`
subcommand.

For more information on using Amazon EMR commands in the AWS CLI, see [https://docs.aws.amazon.com/cli/latest/reference/emr](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").

### Use a custom bootstrap action to copy an

object from Amazon S3 to each node

You can use a bootstrap action to copy objects from Amazon S3 to each node in
a cluster before your applications are installed. The AWS CLI
is installed on each node of a cluster, so your bootstrap action
can call AWS CLI commands.

The following example demonstrates a simple bootstrap action script that copies a file, `myfile.jar`, from Amazon S3 to a local folder, `/mnt1/myfolder`, on each cluster node. The script is saved to Amazon S3 with the file name `copymyfile.sh` with the following contents.

```
#!/bin/bash
aws s3 cp s3://amzn-s3-demo-bucket/myfilefolder/myfile.jar /mnt1/myfolder
```

When you launch the cluster, you specify the script. The following AWS CLI example demonstrates this:

```
aws emr create-cluster --name "Test cluster" --release-label `emr-7.10.0` \
--use-default-roles --ec2-attributes KeyName=myKey \
--applications Name=Hive Name=Pig \
--instance-count 3 --instance-type m5.xlarge \
--bootstrap-actions Path="s3://amzn-s3-demo-bucket/myscriptfolder/copymyfile.sh"
```
