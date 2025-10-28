# Real world use cases for AMS modes

Examine these to help determine how to use AMS modes.

- **Use Case 1, business imperative to lower costs with a time-sensitive data center exit**:
  An enterprise with a compelling business event, like a data center exit, is interested
  in re-hosting their on-prem applications on the cloud. Most of the on-prem inventory consists
  of Windows and Linux servers with a mix of operating system versions. In doing so, the
  customer also wants to take advantage of cost savings that moving to the cloud offers and
  improving the technical and security posture of their applications. The customer wants to
  move fast but does not have the in-house cloud operations expertise built out yet. The customer
  has to find a balance of refactoring, too much refactoring can be risky against a tight timeline.
  However, with some refactoring, like updating OS versions and optimizing databases, applications
  can achieve the next level of performance. In this example, the customer can select AMS-managed
  RFC mode to re-host most of their applications. AMS provides infrastructure operations,
  while also guiding the customer operations teams on best practices on securely operating in the cloud.

AMS-managed AWS Service Catalog and AMS-managed Direct Change mode gives the customer an extra flexibility while achieving
the same business outcomes and objectives. In addition, the customer can use the AMS Operations On Demand (OOD) offering to have
dedicated AMS operations engineers to prioritize the execution of requests for change (RFCs).

While offloading the undifferentiated infrastructure operational tasks (patching, backups,
account management, etc) to AMS, the customer can continue to focus on optimizing their application and
ramp-up their internal teams on cloud operations. AMS provides monthly reports to the customer
on cost savings, and makes recommendations on resource optimizations. In this use case, if there were
end-of-life applications hosted on legacy OS versions like Windows 2003 and 2008, that the customer
decided not to re-factor, those can also be migrated to AMS and hosted in an account that leverages
Customer Managed mode.

- **Use Case 2, building a data lake with Lambda, Glue, Athena within the secure AMS boundary**:
  An enterprise is looking to set up a Data Lake to meet the reporting needs
  for multiple applications in AMS. The customer wants to use S3 buckets for the storage of
  datasets and AWS Athena to query against the dataset for each report. S3 and AWS Athena
  will be deployed in separate AMS Managed accounts. The account with S3 also has other
  services like Glue, Lambda, and Step Functions to build a data ingestion pipeline. Glue,
  Lambda, Athena, and Step Functions are considered Self-Service Provisioning (SSP) services in this case.
  The customer also deployed an EC2 instance in the account that acts as an ad hoc tooling/scripting server.
  The customer starts by requesting AMS to enable the SSP services in their AMS Managed account.
  AMS provisions an IAM role for each service that the customer can assume, once the role is
  onboarded to the customer's federation solution. For ease of management, the customer can also combine the
  policies for the separate IAM roles into one custom role, alleviating the need to switch
  roles when working between the AWS services. Once the role is enabled in the account, the customer
  is able to configure the services as per their requirements. However, the customer must
  work with the AMS change management system to request additional permissions, depending on their use case.

For example, for access to Glue Crawlers, additional permissions are needed by Glue. Additional
permissions will also be needed to create event sources for Lambda. The customer will work with
AMS to update IAM roles to allow cross-account access for Athena to query S3 buckets. Updates to
service roles or service-linked roles will also be needed through AMS change management for Lambda to
call the Step Functions service, and Glue to read and write to all S3 buckets. AMS works with customers
to ensure that the least-privilege access model is followed and the IAM changes requested are
not overly permissive and opening up the environment to unnecessary risk. The customer’s data lake team
spends time planning for all IAM permissions needed for the services specific to the customer’s architecture
and requests AMS to enable them. This is because all IAM changes are processed manually and undergo review
from the AMS Security team. Time to process these requests should be accounted for in the application
deployment schedule.

As the SSP services are operational in the account, the customer can request support and report
issues through AMS incident management and service requests. However, AMS will not actively
monitor performance and concurrency metrics for Lambda, or job metrics for Glue. It is the customer’s
responsibility to ensure appropriate logging and monitoring is enabled for SSP services. The EC2
instance and S3 bucket in the account are fully managed by AMS.

- **Use Case 3, quick and flexible set up of a CICD deployment pipeline in AMS**:
  A customer is looking to set up a Jenkins-based CICD pipeline to deploy code pipeline
  to all application accounts in AMS. The customer may find it most suitable to host this CICD pipeline
  in the AMS-managed Direct Change mode (DCM) or AMS-managed Developer mode because it gives them flexibility to set up the
  Jenkins server with required custom configuration on EC2, with the desired IAM permissions to access CloudFormation
  and S3 buckets that host the artifact repository. While this can also be done in the AMS-managed RFC
  mode, the customer team would need to create multiple manual RFCs for IAM roles to iterate on the least
  permissive set of approved permissions, which are manually reviewed by AMS.
  DCM allows the customers to achieve their operational goals on AWS while avoiding the need to create multiple manual RFCs for IAM
  roles, when using AMS-managed RFC mode, to iterate on the least permissive set of approved permissions, which are manually
  reviewed by AMS. This would take time as well as education on the customer’s part to ramp up AMS processes and tools. Working with Developer mode,
  the customer can start with a "developer role" to provision infrastructure using native AWS APIs. The
  quickest and most flexible way to set up this pipeline would be to use AMS Managed-Developer mode.
  Developer mode gives the quickest and easiest way, while compromising on operational integration, while DCM is less flexible but
  does provide the same level of operational support as RFC mode.
- **Use Case 4, bespoke operating model within the AMS foundation**:
  A customer is looking at a deadline-driven data center exit and one of their enterprise
  applications is fully managed by a third party MSP, including application operations and infrastructure operations.
  Assuming that the customer does not have time in the schedule to re-factor this application so that it can
  be operated by AMS, Customer Managed mode is a suitable option. The customer can
  take advantage of the automated and quick set up of AMS managed Landing Zone. They can leverage the
  centralized account management that controls account vending and connectivity through the centralized
  networking account. It also simplifies their billing by consolidating charges for all customer managed
  accounts through the AMS Payer account. The customer has flexibility to set up their bespoke access
  management model with the MSP separate from standard access management used for AMS Managed accounts.
  This way, using Customer Managed mode, they can set up an AMS managed environment while meeting their
  business requirement of vacating their on-prem environment. In this case, if the customer also has
  Windows-based applications that they are migrating to the cloud, and choose to move them to a Customer
  Managed account, the customer is responsible for creating a cloud operating model. This can be complex,
  expensive, and time consuming depending on the customer's ability to transform traditional IT processes and
  train people. The customer can save time and cost by "lift and shift" of such workloads to an AMS Managed
  account and offload infrastructure operations to AMS.

###### Note

Customers may sometimes feel the need to move application accounts between the
governance framework of RFC or SSP mode and Developer mode. For example, customers
may host an application in AMS-managed mode as part of initial lift and shift migration,
but overtime want to re-write the application to optimize it for cloud-native AWS services.
They could change the mode of the pre-prod account from AMS-managed RFC to
AMS-managed Developer mode, giving them the flexibility and agility for provisioning infrastructure.
However, once infrastructure provisioning changes have been made using the "developer role", the
same infrastructure cannot be moved back to AMS-managed RFC mode. This is because
AMS cannot guarantee operations of infrastructure that was provisioned outside of the AMS change
management system. Customers may need to create a new application account that offers
AMS-managed RFC mode and then re-deploy the "optimized" infrastructure configuration
through CloudFormation templates or custom AMIs ingested into an AMS-managed account. This is
a clean way to deploy a production ready configuration. Once deployed, the application will
be under prescriptive AMS governance and operations. The same applies to switching modes
between Customer Managed mode and AMS-managed.
