# Submit Pig work

This section demonstrates submitting Pig work to an Amazon EMR cluster. The examples that
follow generate a report containing the total bytes transferred, a list of the top 50 IP
addresses, a list of the top 50 external referrers, and the top 50 search terms using
Bing and Google. The Pig script is located in the Amazon S3 bucket
`s3://elasticmapreduce/samples/pig-apache/do-reports2.pig`. Input data is
located in the Amazon S3 bucket `s3://elasticmapreduce/samples/pig-apache/input`.
The output is saved to an Amazon S3 bucket.

## Submit Pig work using the Amazon EMR console

This example describes how to use the Amazon EMR console to add a Pig step to a
cluster.

###### To submit a Pig step

1. Open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr/ "https://console.aws.amazon.com/emr/").
2. Choose **Create cluster** to create a cluster with Pig installed. For steps on how to create a cluster,
   see [Plan and configure an Amazon EMR cluster](../ManagementGuide/emr-gs.md#emr-getting-started-plan-and-configure "../ManagementGuide/emr-gs.md#emr-getting-started-plan-and-configure").
3. Open a terminal and SSH into the master node of your cluster following the
   steps outlined in [Connect to the master node using SSH](../ManagementGuide/emr-connect-master-node-ssh.md "../ManagementGuide/emr-connect-master-node-ssh.md"). Once you've done that,
   run the following steps.

```
sudo mkdir -p /home/hadoop/lib/pig/
sudo aws s3 cp s3://elasticmapreduce/libs/pig/0.3/piggybank-0.3-amzn.jar /home/hadoop/lib/pig/piggybank.jar
```

4. In the console, click **Cluster List** and select the
   name of the cluster you created.
5. Scroll to the **Steps** section and expand it, then
   choose **Add step**.
6. In the **Add Step** dialog:
   - For **Step type**, choose **Pig
     program**.
   - For **Name**, accept the default name (Pig
     program) or type a new name.
   - For **Script S3 location**, type the location of
     the Pig script. For example:
     `s3://elasticmapreduce/samples/pig-apache/do-reports2.pig`.
   - For **Input S3 location**, type the location of
     the input data. For example:
     `s3://elasticmapreduce/samples/pig-apache/input`.
   - For **Output S3 location**, type or browse to the
     name of your Amazon S3 output bucket.
   - For **Arguments**, leave the field blank.
   - For **Action on failure**, accept the default
     option (**Continue**).

7. Choose **Add**. The step appears in the console with a
   status of Pending.
8. The status of the step changes from Pending to Running to Completed as the
   step runs. To update the status, choose the **Refresh**
   icon above the **Actions** column. When your step is
   complete, check your Amazon S3 bucket to confirm your Pig step's output files are
   there.

## Submit Pig work using the AWS CLI

###### To submit a Pig step using the AWS CLI

When you launch a cluster using the AWS CLI, use the `--applications`
parameter to install Pig. To submit a Pig step, use the `--steps`
parameter.

1. To launch a cluster with Pig installed, type the following command,
   replacing `myKey` and `amzn-s3-demo-bucket/` with the name of your EC2 key
   pair and Amazon S3 bucket.

```
aws emr create-cluster \
--name "`Test cluster`" \
--log-uri s3://`amzn-s3-demo-bucket/` \
--release-label `emr-5.36.2` \
--applications Name=Pig \
--use-default-roles \
--ec2-attributes KeyName=`myKey` \
--instance-type `m5.xlarge` \
--instance-count `3`
```

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

When you specify the instance count without using the
`--instance-groups` parameter, a single master node is
launched, and the remaining instances are launched as core nodes. All nodes
use the instance type specified in the command.

###### Note

If you have not previously created the default EMR service role
and EC2 instance profile, type `aws emr
 create-default-roles` to create them before typing the
`create-cluster` subcommand. 2. To submit a Pig step, enter the following command, replacing
`myClusterId` and
`amzn-s3-demo-bucket` with your cluster ID and
name of your Amazon S3 bucket.

```
aws emr add-steps \
--cluster-id `myClusterId` \
--steps Type=PIG,Name="Pig Program",ActionOnFailure=CONTINUE,Args=[-f,s3://elasticmapreduce/samples/pig-apache/do-reports2.pig,-p,INPUT=s3://elasticmapreduce/samples/pig-apache/input,-p,OUTPUT=s3://`amzn-s3-demo-bucket`/pig-apache/output]
```

This command will return a step ID, which you can use to check the `State` of your step. 3. Query the status of your step with the `describe-step` command.

```
aws emr describe-step --cluster-id `myClusterId` --step-id `s-1XXXXXXXXXXA`
```

The `State` of the step changes from `PENDING` to
`RUNNING` to `COMPLETED` as the step runs. When
your step is complete, check your Amazon S3 bucket to confirm your Pig step's
output files are there.

For more information about using Amazon EMR commands in the AWS CLI, see the
[AWS CLI Command Reference](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").
