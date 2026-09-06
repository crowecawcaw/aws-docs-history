

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Full stack app deployments in AMS
<a name="full-stack-aog"></a>

A Full Stack deployment is where you submit an RFC with a CT that creates and configures everything you need at once. For example, to deploy the high availability website just described (EC2 instances, load balancer, and database) you would use a CT that, all together, created and configured an Auto Scaling group, a load balancer, a database, and the security group settings required for all instances to function as a stack. Examples of two AMS CTs that do this are described next.
+ High Availability Two-Tier Stack (ct-06mjngx5flwto): This change type allows you to create a stack and configure an Auto Scaling Group, RDS-backed database, Load Balancer, and CodeDeploy application and configuration. Note that the load balancer isn't considered a tier as it is shared across multiple applications as a network appliance and the CodeDeploy functions are also considered an appliance. Additionally, it creates a CodeDeploy deployment group (with the name you give the CodeDeploy application) that can be used to deploy your applications. Security group settings to allow the resources to function together are automatically created.
+ High Availability One-Tier Stack (ct-09t6q7j9v5hrn): This change type allows you to create a stack and configure an Auto Scaling Group, and an Application Load Balancer. Security group settings that allow the resources to function together are automatically created.