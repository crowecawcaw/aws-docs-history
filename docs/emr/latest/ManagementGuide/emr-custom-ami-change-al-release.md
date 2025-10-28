# Change the Amazon Linux release when you

create an EMR cluster

When you launch a cluster using Amazon EMR 6.6.0 or higher, it automatically uses the
latest Amazon Linux 2 release that has been validated for the default Amazon EMR AMI. You can specify
a different Amazon Linux release for your cluster with the Amazon EMR console or the AWS CLI.

Amazon EMR console

###### To change the Amazon Linux release when you create a cluster from the

console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation pane,
   choose **Clusters**, and then choose
   **Create cluster**.
3. For **EMR version**, choose
   **emr-6.6.0** or higher.
4. Under **Operating system options**, choose **Amazon Linux release**, uncheck
   the **Automatically apply latest Amazon Linux updates** check box, and choose a desired **Amazon Linux release**.
5. Choose any other options that apply to your cluster.
6. To launch your cluster, choose **Create
   cluster**.

AWS CLI

###### To change the Amazon Linux release when you create a cluster with the

AWS CLI

- Use the `--os-release-label` parameter to specify the
  **Amazon Linux Release** when you run the `aws
 emr`
  [create-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/create-cluster.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/create-cluster.html") command.

```
aws emr create-cluster --name "Cluster with Different Amazon Linux Release" \
--os-release-label 2.0.20210312.1 \
--release-label emr-6.6.0 --use-default-roles \
--instance-count 2 --instance-type m5.xlarge
```
