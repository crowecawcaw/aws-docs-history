

# Configure and use Deadline Cloud service-managed fleets
<a name="smf"></a>

A service-managed fleet (SMF) is a collection of workers managed by Deadline Cloud. An SMF eliminates the need to manage fleet scaling for processing demands or reduce fleet size after task completion. For more information about choosing a fleet type, see [Choose between service-managed and customer-managed fleets](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/fleet-types.html) in the *Deadline Cloud User Guide*.

When an SMF is associated with a queue using the default conda queue environment, Deadline Cloud configures the workers in the fleet with the appropriate software package. For supported partner applications, see [Default conda queue environment](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/create-queue-environment.html) in the *AWS Deadline Cloud User Guide*.

In most cases, you don't need to change an SMF to process your workloads. However, some situations may require you make changes to your fleets.

**Note**  
To install custom software on workers using host configuration scripts, see [Run host configuration scripts with administrator privileges](smf-admin.md).

**Topics**
+ [Connect VPC resources to your SMF with VPC resource endpoints](smf-vpc.md)
+ [Use job attachments with service-managed fleets](smf-job-attachments.md)
+ [Persistent storage for service-managed fleets](smf-persistent-storage-dev.md)