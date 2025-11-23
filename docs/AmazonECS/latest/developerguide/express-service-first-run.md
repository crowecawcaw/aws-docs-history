# Create your first Amazon ECS Express Mode service in the

console

The console experience for Express Mode service provides a streamlined way to deploy your containerized application with minimal configuration required.
Read more about prerequisies in [Amazon ECS Express Mode](express-service-overview.md "express-service-overview.md").
To learn more about what Express Mode creates and how it works, see [Resources created by Amazon ECS Express Mode services](express-service-work.md "express-service-work.md").

## Procedure

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Express mode**.
3. Under **Let's set up your app**:
   1. Specify the image to use for your application. For **Image URI**, enter the URI for your image. To browse your Amazon ECR images, choose **Browse ECR images**, and then do the following:
      1. For **Private repository**, choose the Amazon ECR private repository.
      2. For **Image**, choose your image.
      3. Choose how to identify the image. For **Select image by**, choose one of the following options:
         - AWS recommends that you choose **Image digest**.
         - To use the tag, choose **Image tag**. The for **Tag**, choose the tag.

   2. If using a private registry, select **Private registry**. Then for **Secrets Manager ARN or name**,
      enter the Secrets Manager ARN you created in the prerequisites.
   3. For **Task execution role**, and **Infrastructure role**, choose the roles. If you've never created these roles
      in Amazon ECS before, you will see the option to **Create new role** in the drop down. When you select this option, the role will be created for you automatically once you click
      **Create**. For the **Task execution role**, the Permission details will display the link for additional details on the
      [AmazonECSTaskExecutionRolePolicy](../../../aws-managed-policy/latest/reference/AmazonECSTaskExecutionRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonECSTaskExecutionRolePolicy.md") in the AWS Managed Policy Reference Guide. For the
      **Infrastructure role**, the Permission details will display the link for additional details on the
      [AmazonECSInfrastructureRoleforExpressGatewayServices](../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRoleforExpressGatewayServices.md "../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRoleforExpressGatewayServices.md") Managed Policy in the AWS Managed Policy Reference Guide.

   If you prefer to customize these roles, the **Create new role** button directs you to the IAM console where you can create the role,
   view, and edit the permissions attached to role. When you return to the Amazon ECS Express Mode console, refresh to view the role you created.

   ###### Note

   The first time you create a service in the Amazon ECS Console, some users may see an `Invalid Parameter Exception: Unable to assume the service linked role.` If this occurs, wait a few seconds and try again.

4. Choose **Create**. You've just created your first Amazon ECS Express Mode service!

## Next steps

After creating your first Express Mode service:

- Access your application using the provided Application URL once the deployment is complete.
- Monitor deployment progress in the Resources tab of the console. When the deployment is complete, your service is ready to receive traffic. For more
  information, see [Viewing the details of an
  Amazon ECS Express Mode service](express-service-view-service.md "express-service-view-service.md").
- To navigate back to your service, select from the navigation **Clusters**, then select the `default` Cluster if you did not specify one during the create.
  Amazon ECS Organizes services into logical groupings called clusters. This is an easy way to organize applications in your account.
- If you encounter any issues during deployment, see [Troubleshooting Amazon ECS Express Mode services](express-service-troubleshooting.md "express-service-troubleshooting.md").

## Customize

Optionally, you can also customize the configuration of your Express Mode service. Open the section titled **Additional configurations -
_optional_**.

1. Select a **Cluster** from the drop down if there is a specific Amazon ECS Cluster where you want to deploy your service. If no cluster is
   specified, Express Mode will use the `Default` cluster. If you leave the Express Mode console to create a cluster, use the refresh button to populate
   the drop down.
2. Enter a **Name** for the service. If no name is specified, Express Mode will generate one from the container image name. This service name
   will be used across several resources, including the Application URL, Amazon ECS Service, Amazon ECS Task Definition, certificate, scaling target, and scaling policy.
3. Optionally specify details about your **Container**:
   1. For **Container port**, enter the port your application listens on (default is 80).
   2. For **Health check path**, enter the path for health checks (for example, `"/health"`). The default is `"/".`
   3. Under **Environment variables**, add key-value pairs for environment variables your application needs. For **Key**,
      enter the environment variable name. For **Value type**, choose **Environment variable** or **Secret**.
      For **Value or value from**, enter the value or reference. Choose **Add environment variable** to add more variables as needed.
      No defaults are provided.
   4. For **Command**, optionally enter a custom command to override the Docker `CMD` instruction. No default is provided.
   5. For **Task role**, choose an IAM role that grants permissions to your application. No default is provided.

4. Optionally specify details about your **Compute** and **Auto scaling**:
   1. For **CPU**, choose the vCPU allocation for your tasks (the default is 1 vCPU).
   2. For **Memory**, choose the Memory allocation for your tasks (the default is 2 GB).
   3. For **ECS service metric**, choose the metric to scale on (the default is **Average CPU Utilization**).
   4. For **Target value**, choose the target percentage for scaling (the default is **60**.)
   5. For **Minimum number of tasks** and **Maximum number of tasks**, set the scaling limits. (The defaults are **1**
      and **20**)

5. Check the box to **Customize networking configurations**. If you do not customize these configurations, Express Mode will use the Default VPC.
   1. Select a **VPC** to help quickly navigate to the **Subnets** where your services will run. Optionally, leave the Amazon ECS
      Console to create a new VPC, and come back to refresh and find that VPC in the drop down.
   2. For **Security groups**, choose or create security groups to allow additional inbound network access to your service.

6. Under **Logs**:
   1. For **Amazon CloudWatch log group**, enter the preferred log group name for your application logs. The default log group is named according to your cluster and service names.
   2. For **Amazon CloudWatch log stream prefix**, enter a preferred prefix for log streams. The default stream prefix is `ecs/Main/.`

7. Under **Tags**, add key-value pairs to tag your resources. For **Key**, enter the tag key. For **Value**, enter the tag value. Choose
   **Add new item** to add more tags as needed. Tags can only be added on create.
