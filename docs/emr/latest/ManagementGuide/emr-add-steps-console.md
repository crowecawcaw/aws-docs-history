

# Adding steps to a cluster with the Amazon EMR Management Console
<a name="emr-add-steps-console"></a>

Use the following procedures to add steps to a cluster with the AWS Management Console. For detailed information about how to submit steps for specific big data applications, see the following sections of the *[Amazon EMR Release Guide](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-components.html)*:
+ [Submit a custom JAR step ](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-launch-custom-jar-cli.html) 
+ [Submit a Hadoop streaming step ](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/CLI_CreateStreaming.html) 
+ [Submit a Spark step ](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-submit-step.html) 
+ [Submit a Pig step](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-pig-launch.html#ConsoleCreatingaPigJob) 
+ [Run a command or script as a step ](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-launch-custom-jar-cli.html) 
+ [Pass values into steps to run Hive scripts](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hive-differences.html#emr-hive-additional-features) 

## Add steps during cluster creation
<a name="emr-add-steps-console-cluster-creation"></a>

From the AWS Management Console, you can add steps when you create a cluster.

------
#### [ Console ]

**To add steps when you create a cluster with the console**

1. Sign in to the AWS Management Console, and open the Amazon EMR console at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr).

1. Under **EMR on EC2** in the left navigation pane, choose **Clusters**, and then choose **Create cluster**.

1. Under **Steps**, choose **Add step**. Enter appropriate values in the fields in the **Add step** dialog. For information on formatting your step arguments, see [Add step arguments](#emr-add-steps-console-arguments). Options differ depending on the step type. To add your step and exit the dialog, select **Add step**.

1. Choose any other options that apply to your cluster. 

1. To launch your cluster, choose **Create cluster**.

------

## Add steps to a running cluster
<a name="emr-add-steps-console-running-cluster"></a>

With the AWS Management Console, you can add steps to a cluster with the auto-terminate option disabled. 

------
#### [ Console ]

**To add steps to a running cluster with the console**

1. Sign in to the AWS Management Console, and open the Amazon EMR console at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr).

1. Under **EMR on EC2** in the left navigation pane, choose **Clusters**, and select the cluster that you want to update.

1. On the **Steps** tab on the cluster details page, select **Add step**. To clone an existing step, choose the **Actions** dropdown menu and select **Clone step**.

1. Enter appropriate values in the fields in the **Add step** dialog. Options differ depending on the step type. To add your step and exit the dialog, choose **Add step**.

------

## Modify the step concurrency level in a running cluster
<a name="emr-add-steps-console-modify-concurrency"></a>

With the AWS Management Console, you can modify the step concurrency level in a running cluster. 

**Note**  
You can only run multiple steps in parallel with Amazon EMR version 5.28.0 and later. 

------
#### [ Console ]

**To modify step concurrency in a running cluster with the console**

1. Sign in to the AWS Management Console, and open the Amazon EMR console at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr).

1. Under **EMR on EC2** in the left navigation pane, choose **Clusters**, and select the cluster that you want to update. The cluster must be running to change its concurrency attribute.

1. On the **Steps** tab on the cluster details page, find the **Attributes** section. Select **Edit** to change the concurrency. Enter a value between 1 and 256.

------

## Add step arguments
<a name="emr-add-steps-console-arguments"></a>

When you use the AWS Management Console to add a step to your cluster, you can specify arguments for that step in the **Arguments** field. You must separate arguments with whitespace and surround string arguments that consist of characters *and* whitespace with quotation marks.

**Example : Correct arguments**  
The following example arguments are formatted correctly for the AWS Management Console, with quotation marks around the final string argument.  

```
bash -c "aws s3 cp s3://amzn-s3-demo-bucket/my-script.sh ."
```
You can also put each argument on a separate line for readability as shown in the following example.  

```
bash 
-c 
"aws s3 cp s3://amzn-s3-demo-bucket/my-script.sh ."
```

**Example : Incorrect arguments**  
The following example arguments are improperly formatted for the AWS Management Console. Notice that the final string argument, `aws s3 cp s3://amzn-s3-demo-bucket/my-script.sh .`, contains whitespace and is not surrounded by quotation marks.  

```
bash -c aws s3 cp s3://amzn-s3-demo-bucket/my-script.sh .
```