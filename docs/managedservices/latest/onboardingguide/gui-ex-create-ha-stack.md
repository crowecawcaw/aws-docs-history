

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Console Tutorial: High Availability Two Tier Stack (Linux/RHEL)
<a name="gui-ex-create-ha-stack"></a>

This section describes how to deploy a high availability (HA) WordPress site into an AMS environment using the AMS console.

**Note**  
This deployment walkthrough has been tested in AMZN Linux and RHEL environments.

Summary of tasks and required RFCs:

1. Create infrastructure (HA two-tier stack)

1. Create an S3 bucket for CodeDeploy applications

1. Create the WordPress application bundle and upload it to the S3 bucket

1. Deploy the application with CodeDeploy

1. Access the WordPress site and log in to validate the deployment

1. Tear down the deployment

Descriptions for all CT options, including ChangeTypeId, can be found in [AMS Change Type Reference](https://docs.aws.amazon.com/managedservices/latest/ctref/index.html).