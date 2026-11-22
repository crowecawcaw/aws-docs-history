

# Shared responsibility

 Building and operating workloads in the cloud is a shared responsibility between AWS and you. This shared model can help relieve your operational burden, as AWS operates, manages, and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the services run. You assume responsibility and management of the guest operating system (including updates and security patches), other associated application software, and the configuration of the AWS-provided resources you use. You should carefully consider the services you choose, because your responsibilities vary depending on the services used, the integration of those services into your IT environment, and applicable laws and regulations. This differentiation of responsibility is commonly referred to as responsibility *of* the cloud versus *in* the cloud. 

 Some pillars of the Well-Architected Framework describe how the shared responsibility model applies to that pillar's specific concerns. 
+  [The shared responsibility model for security](sec-shared-responsibility.md) 
+  [The shared responsibility model for resilience](rel-shared-responsibility.md) 
+  [The shared responsibility model for sustainability](sus-shared-responsibility.md) 

## AWS responsibility of the cloud
<a name="shared-responsibility-of-the-cloud"></a>

 AWS is responsible for protecting and operating the infrastructure that runs all of the services offered in the AWS Cloud. This infrastructure is composed of the hardware, software, networking, and facilities that run AWS Cloud services. AWS uses commercially reasonable efforts to make these services available, verifying that service availability meets or exceeds [AWS Service Level Agreements (SLAs)](https://aws.amazon.com/legal/service-level-agreements/). 

 The [AWS Global Cloud Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) is designed to allow you to build highly available and resilient workload architectures. Each AWS Region is fully isolated and consists of multiple [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/#Availability_Zones), which are physically isolated partitions of infrastructure. Availability Zones isolate faults that could impact workload resilience, preventing them from impacting other zones in the Region. At the same time, all zones in an AWS Region are interconnected with high-bandwidth, low-latency networking over fully redundant, dedicated metro fiber, and all traffic between zones is encrypted. 

## Customer responsibility in the cloud
<a name="shared-responsibility-in-the-cloud"></a>

 Your responsibility is determined by the AWS Cloud services that you select. This determines the amount of configuration work you must perform as part of your responsibilities. For example, a service such as Amazon Elastic Compute Cloud (Amazon EC2) is categorized as Infrastructure as a Service (IaaS) and requires you to perform all of the necessary configuration and management tasks. Customers that deploy an Amazon EC2 instance are responsible for management of the guest operating system (including updates and security patches), any application software or utilities installed on the instances, and the configuration of the AWS-provided firewall (called a security group) on each instance. 

 For abstracted and managed services, such as Amazon S3 and Amazon DynamoDB, AWS operates the infrastructure layer, the operating system, and platforms, and you access the endpoints to store and retrieve data. You are responsible for managing your data (including classification, encryption options, backup, versioning, and replication strategies) and for using IAM tools to apply the appropriate permissions. 