

# Create a development or test instance for your Connect Customer contact center
<a name="create-connect-instance"></a>

You might want to create multiple contact center instances, for example, one as a Sandbox for development, another for QA, and a third for Production. 

Each instance functions only within the AWS Region in which you create it.

**Important**  
Most entities in Connect Customer can be (re)created and replicated among instances using the Connect Customer API. While doing that keep the following limitations in mind:  
Service quotas are specific to each instance.
Some supporting services, such as User Directory, can be linked to only one Connect Customer instance at a time.
Any additional external and Region-specific limitations.
For more information, see [Can I migrate my Amazon Connect instance from a test environment to a production environment?](https://aws.amazon.com/premiumsupport/knowledge-center/connect-migrate-instance-resources/)

**To create another instance**

1. In the AWS Management Console, choose **Connect Customer**.

1. Choose **Add an instance**.

1. Complete the steps on the Connect Customer resource configuration page. For instructions see [Create a Connect Customer instance](amazon-connect-instances.md).