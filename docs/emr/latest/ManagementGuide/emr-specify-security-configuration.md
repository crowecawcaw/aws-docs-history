# Specify a security configuration

for an Amazon EMR cluster

You can specify encryption settings when you create a cluster by specifying the
security configuration. You can use the AWS Management Console or the AWS CLI.

Console

###### To specify a security configuration with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation pane,
   choose **Clusters**, and then choose
   **Create cluster**.
3. Under **Security configuration and permissions**,
   find the **Security configuration** field. Select
   the dropdown menu or choose **Browse** to select
   the name of a security configuration that you created previously.
   Alternatively, choose **Create security
   configuration** to create a configuration that you can
   use for your cluster.
4. Choose any other options that apply to your cluster.
5. To launch your cluster, choose **Create
   cluster**.

CLI

###### To specify a security configuration with the AWS CLI

- Use `aws emr create-cluster` to optionally apply a
  security configuration with `--security-configuration
`MySecConfig`, where
`MySecConfig``is the
name of the security configuration, as shown in the following
example. The`--release-label`you specify must be 4.8.0
or later and the`--instance-type` can be any
  available.

```
aws emr create-cluster --instance-type `m5.xlarge` --release-label emr-5.0.0 --security-configuration `mySecConfig`
```
