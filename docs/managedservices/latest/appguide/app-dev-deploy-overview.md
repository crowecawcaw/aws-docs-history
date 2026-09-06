

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Application development
<a name="app-dev-deploy-overview"></a>

Application development processes and practices that enable effective design and deployment of applications into an AWS Managed Services (AMS) environment. AMS guides you through the following high level process:

1. Envision and architect an application to be developed or integrated to your AMS-managed environment. Some considerations:

   1. How will you deploy your application? With automation using a deployment tool such Ansible, or manually by directly uploading needed files?

   1. How will you update your application? With a mutable approach updating each instance separately, or with an immutable approach updating each instance with a single, updated, AMI in an Auto Scaling group?

1. Plan and architect the infrastructure that will be used to host the application using AWS architecture libraries, AWS "Well-Architected" guidance, and AMS and other cloud architecture subject matter experts. The following sections of this guide provide information that can help with this.

1. Select an infrastructure deployment approach:

   1. Full Stack: All infrastructure components are deployed at once, together.

   1. Tier and Tie: Infrastructure deployments are deployed separately and, after, tied together with security group modifications. This type of deployment is also achieved by a serial configuration of stack components that builds upon each other; for example, specifying the load balancer that you previously created when you create an Auto Scaling group.

   1. What environments, such as Dev, Staging, and Prod, will you employ?

1. Choose AMS change types (CTs) that will provision the necessary stacks, or tiers, and prepare the necessary requests for change (RFCs).

1. Submit the RFCs to trigger the deployment of the infrastructure to the appropriate environment.

1. Deploy the application using the application deployment approach selected.

1. Re-work infrastructure and applications as needed.

1. Deploy infrastructure and applications to appropriate follow-on environments, assuming your first deployment is to a non-production environment.

1. Ongoing maintenance is handled by AMS operating the underlying infrastructure, and your operations teams operating the application(s) infrastructures.

1. To decommission an application, terminate the AMS infrastructure for it.