

# Shared responsibility
<a name="shared-responsibility"></a>

Security and Compliance is a shared responsibility between AWS and the customer. This shared model can help relieve the customer’s operational burden as AWS operates, manages, and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates. The customer assumes responsibility and management of the guest operating system (including updates and security patches), and other associated application software in addition to the configuration of the AWS provided security group firewall. Customers should carefully consider the services they choose as their responsibilities vary depending on the services used, the integration of those services into their IT environment, and applicable laws and regulations. The nature of this shared responsibility also provides the flexibility and customer control that permits the deployment. As shown in the following chart, this differentiation of responsibility is commonly referred to as Security “of” the Cloud versus Security “in” the Cloud. 

**AWS responsibility “Security of the Cloud”** – AWS is responsible for protecting the infrastructure that runs all of the services offered in the AWS Cloud. This infrastructure is composed of the hardware, software, networking, and facilities that run AWS Cloud services. 

**Customer responsibility “Security in the Cloud”** – Customer responsibility will be determined by the AWS Cloud services that a customer selects. This determines the amount of configuration work the customer must perform as part of their security responsibilities. For example, a service such as Amazon Elastic Compute Cloud (Amazon EC2) is categorized as Infrastructure as a Service (IaaS) and, as such, requires the customer to perform all of the necessary security configuration and management tasks. Customers that deploy an Amazon EC2 instance are responsible for management of the guest operating system (including updates and security patches), any application software or utilities installed by the customer on the instances, and the configuration of the AWS-provided firewall (called a security group) on each instance. For abstracted services, such as Amazon S3 and Amazon DynamoDB, AWS operates the infrastructure layer, the operating system, and platforms, and customers access the endpoints to store and retrieve data. Customers are responsible for managing their data (including encryption options), classifying their assets, and using IAM tools to apply the appropriate permissions.

![Shared responsibility model showing customer responsibilities above AWS infrastructure layers.](http://docs.aws.amazon.com/wellarchitected/latest/security-pillar/images/aws-shared-responsibility.png)


*Figure 1: AWS Shared Responsibility Model.*

This customer/AWS shared responsibility model also extends to IT controls. Just as the responsibility to operate the IT environment is shared between AWS and its customers, so is the management, operation, and verification of IT controls shared. AWS can help relieve customer burden of operating controls by managing those controls associated with the physical infrastructure deployed in the AWS environment that may previously have been managed by the customer. As every customer is deployed differently in AWS, customers can take advantage of shifting management of certain IT controls to AWS, which results in a (new) distributed control environment. Customers can then use the AWS control and compliance documentation available to them to perform their control evaluation and verification procedures as required. The following are examples of controls that are managed by AWS, AWS customers, or both.

**Inherited controls:** Controls that a customer fully inherits from AWS.
+ Physical and environmental controls

**Shared controls:** Controls that apply to both the infrastructure layer and customer layers, but in separate contexts or perspectives. In a shared control, AWS provides the requirements for the infrastructure and the customer must provide their own control implementation within their use of AWS services. Examples include:
+ **Patch management:** AWS is responsible for patching and fixing flaws within the infrastructure, but customers are responsible for patching their guest operating system and applications.
  +  For AWS managed services operating on single-tenant architectures (such as Amazon ElastiCache, Amazon RDS, and Amazon OpenSearch Service), patch management responsibility is shared as follows: 
    +  **AWS responsibility:** Identify vulnerabilities, develop and validate patches, release patches within the service's patching SLA, and notify customers of available updates through the service's documented notification mechanism. 
    +  **Customer responsibility:** Review available updates and facilitate patching by selecting maintenance windows, applying service updates, or scheduling required restarts within the timeframes communicated by AWS. 
  +  For AWS managed services operating on multi-tenant architectures (such as Amazon ElastiCache Serverless, Amazon DynamoDB, and Amazon S3), patch management responsibility is shared as follows: 
    +  **AWS responsibility:** Apply patches without requiring customer action. 
    +  **Customer responsibility:** Consult patching and maintenance documentation for each AWS managed service they use to understand specific notification mechanisms, maintenance window options, and update application processes available to them. 
+ **Configuration management:** AWS maintains the configuration of its infrastructure devices, but customers are responsible for configuring their own guest operating systems, databases, and applications.
+ **Awareness and training:** AWS trains AWS employees, but customers must train their own employees.

**Customer specific:** Controls that are solely the responsibility of the customer based on the application they are deploying within AWS services. Examples include: 
+ Service and Communications Protection or Zone Security, which might require a customer to route or zone data within specific security environments.