# Creating a cluster with Flink

You can launch a cluster with the AWS Management Console, AWS CLI, or an AWS SDK.

###### To launch a cluster with Flink installed from

the console

1. Open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr/ "https://console.aws.amazon.com/emr/").
2. Choose **Create cluster**, **Go to
   advanced options**.
3. For **Software Configuration**, choose **EMR Release emr-5.1.0** or later.
4. Choose **Flink** as an application, along with any others to
   install.
5. Select other options as necessary and choose **Create
   cluster**.

###### To launch a cluster with Flink from the AWS CLI

- Create the cluster with the following command:

```
aws emr create-cluster --release-label `emr-7.10.0` \
--applications Name=Flink \
--region `us-east-1` \
--log-uri `s3://myLogUri` \
--instance-type `m5.xlarge` \
--instance-count `2` \
--service-role EMR_DefaultRole_V2 \
--ec2-attributes KeyName=`MyKeyName`,InstanceProfile=EMR_EC2_DefaultRole \
--steps Type=CUSTOM_JAR,Jar=command-runner.jar,Name=`Flink_Long_Running_Session`,\
Args=`flink-yarn-session,-d`
```

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).
