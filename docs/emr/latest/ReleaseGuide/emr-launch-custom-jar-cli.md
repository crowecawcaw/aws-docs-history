# Submit a custom JAR step

A custom JAR runs a compiled Java program that you can upload to Amazon S3. You should
compile the program against the version of Hadoop you want to launch, and submit a
`CUSTOM_JAR` step to your Amazon EMR cluster. For more information about how
to compile a JAR file, see [Build binaries using Amazon EMR](emr-build-binaries.md "emr-build-binaries.md").

For more information about building a Hadoop MapReduce application, see the [MapReduce Tutorial](http://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html "http://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html") in the Apache Hadoop documentation.

This section covers the basics of submitting a custom JAR step in Amazon EMR. Submitting a
custom JAR step enables you to write a script to process your data with the Java
programming language.

## Submit a custom JAR step with the

console

This example describes how to use the Amazon EMR console to submit a custom JAR step to
a running cluster.

###### To submit a custom JAR step with the console

1. Open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr/ "https://console.aws.amazon.com/emr/").
2. In the **Cluster List**, select the name of your
   cluster.
3. Scroll to the **Steps** section and expand it, then
   choose **Add step**.
4. In the **Add Step** dialog:
   - For **Step type**, choose **Custom
     JAR**.
   - For **Name**, accept the default name (Custom
     JAR) or type a new name.
   - For **JAR S3 location**, type or browse to the
     location of your JAR file. JAR location maybe a path into S3 or a
     fully qualified java class in the classpath..
   - For **Arguments**, type any required arguments as
     space-separated strings or leave the field blank.
   - For **Action on failure**, accept the default
     option (**Continue**).

5. Choose **Add**. The step appears in the console with a
   status of Pending.
6. The status of the step changes from Pending to Running to Completed as the
   step runs. To update the status, choose the **Refresh**
   icon above the Actions column.

## Launching a cluster and submitting a custom

JAR step with the AWS CLI

###### To launch a cluster and submit a custom JAR step with the AWS CLI

To launch a cluster and submit a custom JAR step with the AWS CLI, type the
`create-cluster` subcommand with the `--steps`
parameter.

- To launch a cluster and submit a custom JAR step, type the following
  command, replace `myKey` with the name of your EC2
  key pair, and replace `amzn-s3-demo-bucket` with your bucket
  name.

```
aws emr create-cluster --name "`Test cluster`" --release-label `emr-7.12.0` \
--applications Name=`Hue` Name=`Hive` Name=`Pig` --use-default-roles \
--ec2-attributes KeyName=`myKey` --instance-type `m5.xlarge` --instance-count `3` \
--steps Type=`CUSTOM_JAR`,Name="`Custom JAR Step`",ActionOnFailure=`CONTINUE`,Jar=`pathtojarfile`,Args=["`pathtoinputdata`","`pathtooutputbucket`","`arg1`","`arg2`"]
```

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

When you specify the instance count without the
`--instance-groups` parameter, a single primary node
launches, and the remaining instances launch as core nodes. All nodes use
the instance type that you specify in the command.

###### Note

If you have not previously created the default Amazon EMR service role and
EC2 instance profile, type `aws emr create-default-roles` to
create them before typing the `create-cluster`
subcommand.

For more information on using Amazon EMR commands in the AWS CLI, see [https://docs.aws.amazon.com/cli/latest/reference/emr](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").

## Third-party dependencies

Sometimes it may be necessary to include in the MapReduce classpath JARs for use
with your program. You have two options for doing this:

- Include the `--libjars
s3://`URI_to_JAR`` in the step options
  for the procedure in [Launching a cluster and submitting a custom
  JAR step with the AWS CLI](#emr-dev-create-jar-cli "#emr-dev-create-jar-cli").
- Launch the cluster with a modified
  `mapreduce.application.classpath` setting in
  `mapred-site.xml`. Use the
  `mapred-site` configuration classification. To create
  the cluster with the step using AWS CLI, this would look like the
  following:

```
aws emr create-cluster --release-label `emr-7.12.0` \
--applications Name=`Hue` Name=`Hive` Name=`Pig` --use-default-roles \
--instance-type m5.xlarge --instance-count 2  --ec2-attributes KeyName=`myKey` \
--steps Type=`CUSTOM_JAR`,Name="`Custom JAR Step`",ActionOnFailure=`CONTINUE`,Jar=`pathtojarfile`,Args=["`pathtoinputdata`","`pathtooutputbucket`","`arg1`","`arg2`"] \
--configurations https://s3.amazonaws.com/amzn-s3-demo-bucket/myfolder/myConfig.json
```

`myConfig.json`:

```
[
    {
      "Classification": "mapred-site",
      "Properties": {
        "mapreduce.application.classpath": "`path1`,`path2`"
      }
    }
  ]

```

The comma-separated list of paths should be appended to the JVM classpath for
each task.
