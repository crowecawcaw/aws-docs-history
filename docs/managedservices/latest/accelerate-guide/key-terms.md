

# AMS key terms
<a name="key-terms"></a>
+ *AMS Advanced*: The services described in the "Service Description" section of the AMS Advanced Documentation. See [Service Description](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-sd.html).
+ *AMS Advanced Accounts*: AWS accounts that at all times meet all requirements in the AMS Advanced Onboarding Requirements. For information on AMS Advanced benefits, case studies, and to contact a sales person, see [AWS Managed Services](https://aws.amazon.com/managed-services/).
+ *AMS Accelerate Accounts*: AWS accounts that at all times meet all requirements in the AMS Accelerate Onboarding Requirements. See [Getting Started with AMS Accelerate](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/getting-started-acc.html).
+ *AWS Managed Services*: AMS and or AMS Accelerate.
+ *AWS Managed Services accounts*: The AMS accounts and or AMS Accelerate accounts.
+ <a name="CritRec"></a>*Critical Recommendation*: A recommendation issued by AWS through a service request informing you that your action is required to protect against potential risks or disruptions to your resources or the AWS services. If you decide not to follow a Critical Recommendation by the specified date, you are solely responsible for any harm resulting from your decision.
+ *Customer-Requested Configuration*: Any software, services or other configurations that are not identified in:
  + Accelerate: [Supported Configurations](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sd.html#supported-configs) or [AMS Accelerate; Service Description](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sd.html).
  + AMS Advanced: [Supported Configurations](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-sd.html#supported-configs) or [AMS Advanced; Service Description](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-sd.html).
+ *Incident communication*: AMS communicates an Incident to you or you request an Incident with AMS via an Incident created in Support Center for AMS Accelerate and in the AMS Console for AMS. The AMS Accelerate Console provides a summary of Incidents and Service Requests on the Dashboard and links to Support Center for details.
+ *Managed Environment*: The AMS Advanced accounts and or the AMS Accelerate accounts operated by AMS.

  For AMS Advanced, these include multi-account landing zone (MALZ) and single-account landing zone (SALZ) accounts.
+ *Billing start date*: The next business day after AWS receives the your information requested in the AWS Managed Services Onboarding Email. The AWS Managed Services Onboarding Email refers to the email sent by AWS to the you to collect the information needed to activate AWS Managed Services on the your accounts. 

   For accounts subsequently enrolled by you, the billing start date is the next day after AWS Managed Services sends an AWS Managed Services Activation Notification for the enrolled account. An AWS Managed Services Activation Notification occurs when:

  1. You grants access to a compatible AWS account and hand it over to AWS Managed Services.

  1. AWS Managed Services designs and builds the AWS Managed Services Account.
+ *Service Termination*: You can terminate the AWS Managed Services for all AWS Managed Services accounts, or for a specified AWS Managed Services account for any reason by providing AWS at least 30 days notice through a service request. On the Service Termination Date, either: 

  1. AWS hands over the controls of all AWS Managed Services accounts or the specified AWS Managed Services accounts as applicable, to you, or 

  1. The parties remove the AWS Identity and Access Management roles that give AWS access from all AWS Managed Services accounts or the specified AWS Managed Services accounts, as applicable. 
+ *Service termination date*: The service termination date is the last day of the calendar month following the end of the 30 days requisite termination notice period. If the end of the requisite termination notice period falls after the 20th day of the calendar month, then the service termination date is the last day of the following calendar month. The following are example scenarios for termination dates. 
  + If the termination notice is provided on April 12, then the 30 days notice ends on May 12. The service termination date is May 31.
  + If a termination notice is provided on April 29, then the 30 days notice ends on May 29. The service termination date is June 30.
+ *Provision of AWS Managed Services*: AWS makes available to you and you can access and use AWS Managed Services for each AWS Managed Services account from the service commencement date.
+ *Termination for specified AWS Managed Services accounts*: You can terminate the AWS Managed Services for a specified AWS Managed Services account for any reason by providing AWS notice through a service request ("AMS Account Termination Request").

**Incident management terms**:
+ *Event*: A change in your AMS environment.
+ *Alert*: Whenever an event from a supported AWS service exceeds a threshold and triggers an alarm, an alert is created and notice is sent to your contacts list. Additionally, an incident is created in your Incident list.
+ *Incident*: An unplanned interruption or performance degradation of your AMS environment or AWS Managed Services that results in an impact as reported by AWS Managed Services or you.
+ *Problem*: A shared underlying root cause of one or more incidents.
+ *Incident Resolution* or *Resolve an Incident*: 
  + AMS has restored all unavailable AMS services or resources pertaining to that incident to an available state, or
  + AMS has determined that unavailable stacks or resources cannot be restored to an available state, or 
  + AMS has initiated an infrastructure restore authorized by you.
+ *Incident Response Time*: The difference in time between when you create an incident, and when AMS provides an initial response by way of the console, email, service center, or telephone.
+ *Incident Resolution Time*: The difference in time between when either AMS or you creates an incident, and when the incident is resolved.
+ *Incident Priority*: How incidents are prioritized by AMS, or by you, as either Low, Medium, or High.
  + *Low*: A non-critical problem with your AMS service.
  + *Medium*: An AWS service within your managed environment is available but is not performing as intended (per the applicable service description).
  + *High*: Either (1) the AMS Console, or one or more AMS APIs within your managed environment are unavailable; or (2) one or more AMS stacks or resources within your managed environment are unavailable and the unavailability prevents your application from performing its function.

  AMS may re-categorize incidents in accordance with the above guidelines.
+ *Infrastructure Restore*: Re-deploying existing stacks, based on templates of impacted stacks, and initiating a data restore based on the last known restore point, unless otherwise specified by you, when incident resolution is not possible.

**Infrastructure terms**:
+ *Managed production environment*: A customer account where the customer’s production applications reside.
+ *Managed non-production environment*: A customer account that only contains non-production applications, such as applications for development and testing.
+ *AMS stack*: A group of one or more AWS resources that are managed by AMS as a single unit.
+ *Immutable infrastructure*: An infrastructure maintenance model typical for Amazon EC2 Auto Scaling groups (ASGs) where updated infrastructure components, (in AWS, the AMI) are replaced for every deployment, rather than being updated in-place. The advantages to immutable infrastructure is that all components stay in a synchronous state since they are always generated from the same base. Immutability is independent of any tool or workflow for building the AMI.
+ *Mutable infrastructure*: An infrastructure maintenance model typical for stacks that are not Amazon EC2 Auto Scaling groups and contain a single instance or just a few instances. This model most closely represents traditional, hardware-based, system deployment where a system is deployed at the beginning of its life cycle and then updates are layered onto that system over time. Any updates to the system are applied to the instances individually, and may incur system downtime (depending on the stack configuration) due to application or system restarts.
+ *Security groups*: Virtual firewalls for your instance to control inbound and outbound traffic. Security groups act at the instance level, not the subnet level. Therefore, each instance in a subnet in your VPC could have a different set of security groups assigned to it.
+ *Service Level Agreements (SLAs)*: Part of AMS contracts with you that define the level of expected service.
+ SLA *Unavailable* and *Unavailability*:
  + An API request submitted by you that results in an error.
  + A Console request submitted by you that results in a 5xx HTTP response (the server is incapable of performing the request).
  + Any of the AWS service offerings that constitute stacks or resources in your AMS-managed infrastructure are in a state of "Service Disruption" as shown in the [Service Health Dashboard](https://status.aws.amazon.com/).
  + Unavailability resulting directly or indirectly from an AMS exclusion is not considered in determining eligibility for service credits. Services are considered available unless they meet the criteria for being unavailable.
+ *Service Level Objectives (SLOs)*: Part of AMS contracts with you that define specific service goals for AMS services.

**Patching terms**:
+ *Mandatory patches*: Critical security updates to address issues that could compromise the security state of your environment or account. A "Critical Security update" is a security update rated as "Critical" by the vendor of an AMS-supported operating system. 
+ *Patches announced versus released*: Patches are generally announced and released on a schedule. Emergent patches are announced when the need for the patch has been discovered and, usually soon after, the patch is released.
+ *Patch add-on*: Tag-based patching for AMS instances that leverages AWS Systems Manager (SSM) functionality so you can tag instances and have those instances patched using a baseline and a window that you configure.
+ *Patch methods*:
  + *In-place patching*: Patching that is done by changing existing instances.
  + *AMI replacement patching*: Patching that is done by changing the AMI reference parameter of an existing EC2 Auto Scaling group launch configuration.
+ *Patch provider* (OS vendors, third party): Patches are provided by the vendor or governing body of the application.
+ *Patch Types*:
  + *Critical Security Update (CSU)*: A security update rated as "Critical" by the vendor of a supported operating system.
  + *Important Update (IU)*: A security update rated as "Important" or a non-security update rated as "Critical" by the vendor of a supported operating system.
  + *Other Update (OU)*: An update by the vendor of a supported operating system that is not a CSU or an IU.
+ *Supported patches*: AMS supports operating system level patches. Upgrades are released by the vendor to fix security vulnerabilities or other bugs or to improve performance. For a list of currently supported OSs, see [Support Configurations](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sd.html#supported-configs).

**Security terms**:
+ *Detective Controls*: A library of AMS-created or enabled monitors that provide ongoing oversight of customer managed environments and workloads for configurations that do not align with security, operational, or customer controls, and take action by notifying owners, proactively modifying, or terminating resources.

**Service Request terms**:
+ *Service request*: A request by you for an action that you want AMS to take on your behalf.
+ *Alert notification*: A notice posted by AMS to your **Service requests** list page when an AMS alert is triggered. The contact configured for your account is also notified by the configured method (for example, email). If you have contact tags on your instances/resources, and have provided consent to your cloud service delivery manager (CSDM) for tag-based notifications, the contact information (key value) in the tag is also notified for automated AMS alerts.
+ *Service notification*: A notice from AMS that is posted to your **Service request** list page.

<a name="misc-terms"></a>**Miscellaneous terms**:
+ *AWS Managed Services Interface*: For AMS: The AWS Managed Services Advanced Console, AMS CM API, and Support API. For AMS Accelerate: The Support Console and Support API.
+ *Customer satisfaction (CSAT)*: AMS CSAT is informed with deep analytics including Case Correspondence Ratings on every case or correspondence when given, quarterly surveys, and so forth.
+ *DevOps*: DevOps is a development methodology that strongly advocates automation and monitoring at all steps. DevOps aims at shorter development cycles, increased deployment frequency, and more dependable releases by bringing together the traditionally-separate functions of development and operations over a foundation of automation. When developers can manage operations, and operations informs development, issues and problems are more quickly discovered and solved, and business objectives are more readily achieved.
+ *ITIL*: Information Technology Infrastructure Library (called ITIL) is an ITSM framework designed to standardize the lifecycle of IT services. ITIL is arranged in five stages that cover the IT service lifecycle: service strategy, service design, service transition, service operation, and service improvement.
+ *IT service management (ITSM)*: A set of practices that align IT services with the needs of your business.
+ *Managed Monitoring Services (MMS)*: AMS operates its own monitoring system, Managed Monitoring Service (MMS), that consumes AWS Health events and aggregates Amazon CloudWatch data, and data from other AWS services, notifying AMS operators (online 24x7) of any alarms created through an Amazon Simple Notification Service (Amazon SNS) topic.
+ *Namespace*: When you create IAM policies or work with Amazon Resource Names (ARNs), you identify an AWS service by using a namespace. You use namespaces when identifying actions and resources. 