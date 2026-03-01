# Creating an Amazon ECS cluster for External instance workloads

You create a cluster to define the infrastructure your tasks and services run on.

Before you begin, be sure that you've completed the steps in [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md") and
assign the appropriate IAM permission. For more information, see [Amazon ECS cluster examples](security_iam_id-based-policy-examples.md#IAM_cluster_policies "security_iam_id-based-policy-examples.md#IAM_cluster_policies"). The Amazon ECS console provides a simple way to create the
resources that are needed by an Amazon ECS cluster by creating a CloudFormation stack.

To make the cluster creation process as easy as possible, the console has default
selections for many choices which we describe below. There are also help panels available
for most of the sections in the console which provide further context.

You can modify the following options:

- Add a namespace to the cluster.

A namespace allows services that you create in the cluster can connect to the
other services in the namespace without additional configuration. For more information, see [Interconnect Amazon ECS services](interconnecting-services.md "interconnecting-services.md").

- Configure the cluster for external instances
- Assign a AWS KMS key for your managed storage. For information about how to create a
  key, see [Create a KMS
  key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service User
  Guide_.
- Add tags to help you identify your cluster.

###### To create a new cluster (Amazon ECS console)

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. From the navigation bar, select the Region to use.
3. In the navigation pane, choose **Clusters**.
4. On the **Clusters** page, choose **Create
   cluster**.
5. Under **Cluster configuration**, configure the following:
   - For **Cluster name**, enter a unique name.

   The name can contain up to 255 letters (uppercase and lowercase), numbers,
   and hyphens.
   - (Optional) To have the namespace used for Service Connect be different
     from the cluster name, for **Namespace**, enter a unique
     name.

6. (Optional) Use Container Insights, expand **Monitoring**, and then choose one
   of the following options:
   - To use the recommended Container Insights with enhanced observability, choose
     **Container Insights with enhanced observability**.
   - To use Container Insights, choose **Container Insights**.

7. (Optional) To use ECS Exec to debug tasks in the cluster, expand **Troubleshooting configuration**, and then configure the following:
   - Select **Turn on ECS Exec**.
   - (Optional) For **AWS KMS key for ECS Exec**, enter the ARN of the AWS KMS key you want to use to encrypt the ECS Exec session data.
   - (Optional) For **ECS Exec logging**, choose the log destination:
     - To send logs to CloudWatch Logs, choose **Amazon CloudWatch**.
     - To send logs to Amazon S3, choose **Amazon S3**.
     - To disable logging, choose **None**.

8. (Optional) Encrypt the data on managed storage. Under **Encryption**, for **Managed
   storage**, enter the ARN of the AWS KMS key you want to use to encrypt
   the managed storage data.
9. (Optional) To help identify your cluster, expand **Tags**, and
   then configure your tags.

[Add a tag] Choose **Add tag** and do the following:

    * For **Key**, enter the key name.
    * For **Value**, enter the key value.

10. Choose **Create**.

## Next steps

You must register the instances with the cluster. For more information,
see [Registering an external instance to an Amazon ECS cluster](ecs-anywhere-registration.md "ecs-anywhere-registration.md").

Create a task definition for the external launch type. For more information, see [Creating an Amazon ECS task definition using the console](create-task-definition.md "create-task-definition.md")

Run your applications as standalone tasks, or as part of a service. For more
information, see the following:

- [Running an application as an Amazon ECS task](standalone-task-create.md "standalone-task-create.md")
- [Creating an Amazon ECS rolling update deployment](create-service-console-v2.md "create-service-console-v2.md")
