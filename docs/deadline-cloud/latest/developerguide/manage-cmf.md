

# Create and use Deadline Cloud customer-managed fleets
<a name="manage-cmf"></a>

When you create a customer-managed fleet (CMF), you have full control over your processing pipeline. You define the network and software environment for each worker. Deadline Cloud acts as the repository and scheduler for your jobs. For more information about choosing a fleet type, see [Choose between service-managed and customer-managed fleets](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/fleet-types.html) in the *Deadline Cloud User Guide*.

A worker may be an Amazon Elastic Compute Cloud (Amazon EC2) instance, a worker in a co-location facility, or an on-premises worker. Each worker must run the Deadline Cloud worker agent. All workers must have access to [ the Deadline Cloud service endpoint](https://docs.aws.amazon.com/general/latest/gr/deadlinecloud.html#deadlinecloud_region).

The following topics show you how to create a basic CMF using Amazon EC2 instances.

**Topics**
+ [Create a customer-managed fleet](create-a-cmf.md)
+ [Worker host setup and configuration](worker-host.md)
+ [Manage access to Windows job user secrets](manage-access-windows-secrets.md)
+ [Install and configure software required for jobs](install-software.md)
+ [Configuring AWS credentials](aws-credentials.md)
+ [Worker host data flow for customer-managed fleets](cmf-network.md)
+ [Test the configuration of your worker host](test-software.md)
+ [Create an Amazon Machine Image](create-ami.md)
+ [Create fleet infrastructure with an Amazon EC2 Auto Scaling group](create-auto-scaling.md)