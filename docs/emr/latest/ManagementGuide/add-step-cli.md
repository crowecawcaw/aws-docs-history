# Adding steps to an Amazon EMR cluster with the AWS CLI

The following procedures demonstrate how to add steps to a newly created cluster and
to a running cluster with the AWS CLI. Both examples use the `--steps`
subcommand to add steps to the cluster.

###### To add steps during cluster creation

- Type the following command to create a cluster and add an Apache Pig step.
  Make sure to replace `myKey` with the name
  of your Amazon EC2 key pair.

```
aws emr create-cluster --name "`Test cluster`" \
--applications Name=`Spark` \
--use-default-roles \
--ec2-attributes KeyName=`myKey` \
--instance-groups InstanceGroupType=`PRIMARY`,InstanceCount=`1`,InstanceType=`m5.xlarge` InstanceGroupType=`CORE`,InstanceCount=`2`,InstanceType=`m5.xlarge` \
--steps '[{"Args":["spark-submit","--deploy-mode","cluster","--class","org.apache.spark.examples.SparkPi","/usr/lib/spark/examples/jars/spark-examples.jar","5"],"Type":"CUSTOM_JAR","ActionOnFailure":"CONTINUE","Jar":"command-runner.jar","Properties":"","Name":"Spark application"}]'
```

###### Note

The list of arguments changes depending on the type of step.

By default, the step concurrency level is `1`. You can set the step
concurrency level with the `StepConcurrencyLevel` parameter when you
create a cluster.

The output is a cluster identifier similar to the following.

```
{
    "ClusterId": "j-2AXXXXXXGAPLF"
}
```

###### To add a step to a running cluster

- Type the following command to add a step to a running cluster. Replace
  `j-2AXXXXXXGAPLF` with your own
  cluster ID.

```
aws emr add-steps --cluster-id `j-2AXXXXXXGAPLF` \
--steps '[{"Args":["spark-submit","--deploy-mode","cluster","--class","org.apache.spark.examples.SparkPi","/usr/lib/spark/examples/jars/spark-examples.jar","5"],"Type":"CUSTOM_JAR","ActionOnFailure":"CONTINUE","Jar":"command-runner.jar","Properties":"","Name":"Spark application"}]'
```

The output is a step identifier similar to the following.

```
{
    "StepIds": [
	"s-Y9XXXXXXAPMD"
    ]
}
```

###### To modify the StepConcurrencyLevel in a running cluster

1. In a running cluster, you can modify the `StepConcurrencyLevel`
   with the `ModifyCluster` API. For example, type the following command
   to increase the `StepConcurrencyLevel` to `10`. Replace
   `j-2AXXXXXXGAPLF` with your
   cluster ID.

```
aws emr modify-cluster --cluster-id `j-2AXXXXXXGAPLF` --step-concurrency-level 10
```

2. The output is similar to the following.

```
{
"StepConcurrencyLevel": 10
}
```

For more information on using Amazon EMR commands in the AWS CLI, see the [AWS CLI Command
Reference](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").
