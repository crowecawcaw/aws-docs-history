# Configure Amazon EMR scale-down

behavior

###### Note

The terminate at instance hour scale-down behavior option is no longer
supported for Amazon EMR release 5.10.0 and higher. The following scale-down behavior
options only appear in the Amazon EMR console for releases 5.1.0 through
5.9.1.

You can use the AWS Management Console, the AWS CLI, or the Amazon EMR API to configure scale-down
behavior when you create a cluster.

Console

###### To configure scale-down behavior with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation
   pane, choose **Clusters**, and then choose
   **Create cluster**.
3. In the **Cluster scaling and provisioning
   option** section, choose **Use custom automatic scaling** . Under **Custom automatic scaling policies**,
   choose the **plus action button** to add **Scale in**
   policies. We recommend that you add both **Scale in** and
   **Scale out** policies. Adding in only one set
   of policies means Amazon EMR will only perform one-way scaling,
   and you have to manually perform the other actions.
4. Choose any other options that apply to your cluster.
5. To launch your cluster, choose **Create
   cluster**.

AWS CLI

###### To configure scale-down behavior with the AWS CLI

- Use the `--scale-down-behavior` option to specify
  either `TERMINATE_AT_INSTANCE_HOUR` or
  `TERMINATE_AT_TASK_COMPLETION`.
