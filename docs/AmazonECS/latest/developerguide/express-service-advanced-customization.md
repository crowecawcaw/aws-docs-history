# Updating Resources Outside of Express Mode

Express Mode simplifies deployment by automatically provisioning and managing AWS resources on your behalf, but it's important to understand
the responsibility model. While Express Mode creates and configures resources like Amazon ECS services, load balancers, and auto scaling policies, all
resources remain in your AWS account and are fully accessible for direct management. You can modify these resources outside of Express Mode
using the AWS Console, AWS CLI, or APIs, but doing so may affect Express Mode's ability to manage your service. This section explains which resources
Express Mode manages, how to safely make changes outside of Express Mode, and what happens when you do.

## Understanding the shared responsibility model

The responsibility boundary in Express Mode is defined by API usage. Express Mode APIs manage resources on your behalf with coordinated
updates across multiple AWS services. Standard AWS service APIs give you direct control over individual resources. This allows you to go beyond
the set of parameters that Express Mode provides for configuration, and gives you control over every parameter of every resource. Both sets of APIs operate
on the same underlying infrastructure in your account, and both will execute the operations you request. AWS has the responsibility of performing the operation
you request. Express Mode does not validate whether resource modifications using direct APIs will conflict with Express Mode configuration, nor does it
prevent changes that might disrupt service functionality. This also means that you have the ability to make changes, and those changes will persist. Express Mode
will not overwrite changes unless requested as part of an Express Mode update. You're responsible for understanding how modifications using direct APIs
interact with Express Mode's configuration and for resolving any resulting conflicts or service issues.

For more details on the defaults that Express Mode sets and the resources that it orchestrates, see
[Resources created by Amazon ECS Express Mode services](AmazonECS/latest/developerguide/express-service-work.md "AmazonECS/latest/developerguide/express-service-work.md").

## Do I need to do anything before I can take advantage of Amazon ECS features in my Express Mode service?

No, there is no graduation path or break glass for Express Mode. The entire Amazon ECS feature set is always available for your Express Mode service.
If you'd like to make sure no further Express Mode updates can occur on your service, there are several options. By removing the Managed Tag on your
resources, Amazon ECS will no longer be able to identify and operate on it as an Express Mode service. Alternatively, you can also use IAM to
restrict user permissions to the Express Mode APIs.

## Example Updates Outside of Express Mode

### Adding a sidecar to an Express Mode service

You can add any sidecar container to your service. This example shows how to add a Fluent Bit logging sidecar.

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**.
3. Select the cluster where your Express Mode service is located, and in the **Services** panel, select it.
4. Go to the **Resources** tab and select the task definition.
5. Select the **JSON** tab, and then select the down arrow in the top button labeled **Create New Revision**.
   Here you'll find an action called **Create New Revision with JSON**.
6. Add the sidecar container before or after your primary container definition. For more information, see [Example Amazon ECS task definition: Route logs to FireLens](firelens-taskdef.md "firelens-taskdef.md").
7. If you have a logging sidecar, like in this example, you'll want to change the `logDriver` in the primary container:

```

"logConfiguration": {
    "logDriver": "awsfirelens"
}

```

8. Assuming the default settings for an Express Mode service, set the primary container memoryReservation to 1998 and the Fluent Bit
   container memoryReservation to 50. This ensures the total memory reservation across the two containers does not exceed the amount you have running
   on your Fargate task (2048 for a default Express Mode service).
9. Create your new revision.
10. Click the drop down that says **Deploy** and select **Update Service**.
11. Select the **Cluster** and **Service** that you're updating, and then select **Force new
    deployment**. The task definition revision you just created should be auto-selected. Select **Update**.
12. Watch your deployment take place. Tasks in this service will now have two containers. Additional updates through the Express Mode
    Console or APIs will not overwrite the changes to the task definition, unless they are in direct conflict - for example in this case,
    if you gave Express Mode a new Log Group and Log Stream name, the logDriver would be updated back to `awslogs`.

### Adding a custom domain to your service

**Prerequisites:** This guide assumes your domain is a hosted zone managed by Route 53 with an ACM certificate.
If your domain is hosted elsewhere, you will need a CNAME to point to the Application Load Balancer DNS record.

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**.
3. Select the cluster where your Express Mode service is located, and in the **Services** panel, select it.
4. Go to the **Resources** tab and select the listener rule.
5. Select **Action** and **Edit Rule**.
6. Copy the current Host header value (your Application URL), then **Remove** the rule since there can only be one of each type.
7. Add a condition of type **Host header**, paste your Application URL back in as the Host header condition value.
8. Click **Add OR condition value**.
9. Enter your custom domain here.
10. Click **Next** and **Save Changes**.
11. Now select the **Certificates** tab of the Application Load Balancer listener.
12. Click **Add certificate**. Here you can import the certificate to the listener.
13. In your Route 53 hosted zone, click **Create record** to create a routing record to your service.
14. Select a simple routing record.
15. Add a record name.
16. Select a record type.
17. Route traffic to an **Alias to Application and Classic Load Balancer**.
18. Select your Region.
19. Select the load balancer your Express Mode service uses.

After a few minutes for propagation, your service will begin to receive traffic on the custom domain. If you are adding many certificates
to your Application Load Balancer or servicing many Express Mode services from your Application Load Balancer, you may want to consider raising the service limit for certificates on the Application Load Balancer.
