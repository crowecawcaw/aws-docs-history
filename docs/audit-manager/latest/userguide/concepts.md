

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Understanding AWS Audit Manager concepts and terminology
<a name="concepts"></a>



To help you get started, this page defines terms and explains some of the key concepts of AWS Audit Manager.

## A
<a name="auditmanager-concepts-A"></a>

 [A](#auditmanager-concepts-A) \| B \| [C](#auditmanager-concepts-C) \| [D](#auditmanager-concepts-D) \| [E](#auditmanager-concepts-E) \| [F](#auditmanager-concepts-F) \| G \| H \| [I](#auditmanager-concepts-I) \| J \| K \| L \| M \| N \| O \| P \| Q \| [R](#auditmanager-concepts-R) \| [S](#auditmanager-concepts-S) \| T \| U \| V \| W \| X \| Y \| Z 

**Assessment**  
You can use an Audit Manager assessment to automatically collect evidence that’s relevant for an audit.  
An assessment is based on a framework, which is a grouping of controls that are related to your audit. You can create an assessment from a standard framework or a custom framework. Standard frameworks contain prebuilt control sets that support a specific compliance standard or regulation. In contrast, custom frameworks contain controls that you can customize and group according to your specific audit requirements. Using a framework as a starting point, you can create an assessment that specifies the AWS accounts that you want to include in the scope of your audit.  
When you create an assessment, Audit Manager automatically starts to assess resources in your AWS accounts based on the controls that are defined in the framework. Next, it collects the relevant evidence and converts it into an auditor-friendly format. After doing this, it then attaches the evidence to the controls in your assessment. When it's time for an audit, you—or a delegate of your choice—can review the collected evidence and then add it to an assessment report. This assessment report helps you to demonstrate that your controls are working as intended.   
Evidence collection is an ongoing process that starts when you create your assessment. You can stop evidence collection by changing the assessment status to *inactive*. Alternatively, you can stop evidence collection at the control level. You can do this by changing the status of a specific control within your assessment to *inactive*.  
For instructions on how to create and manage assessments, see [Managing assessments in AWS Audit Manager](assessments.md).

**Assessment report**  
An assessment report is a finalized document that's generated from an Audit Manager assessment. These reports summarize the relevant evidence that's collected for your audit. They link to the relevant evidence folders. The folders are named and organized according to the controls that are specified in your assessment. For each assessment, you can review the evidence that Audit Manager collects, and decide which evidence you want to include in the assessment report.   
To learn more about assessment reports, see [Assessment reports](assessment-reports.md). To learn how to generate an assessment report, see [Preparing an assessment report in AWS Audit Manager](generate-assessment-report.md).

**Assessment report destination**  
An assessment report destination is the default S3 bucket where Audit Manager saves your assessment reports. To learn more, see [Configuring your default assessment report destination](settings-destination.md).

**Audit**  
An audit is an independent examination of the assets, operations, or business integrity of your organization. An information technology (IT) audit specifically examines the controls within the information systems of your organization. The goal of an IT audit is to determine if information systems safeguard assets, operate effectively, and maintain data integrity. All of these are important to meeting the regulatory requirements that are mandated by a compliance standard or regulation. 

**Audit owner**  
The term *audit owner* has two different meanings depending on the context.  
In the context of Audit Manager, an audit owner is a user or role that manages an assessment and its related resources. The responsibilities of this Audit Manager persona include creating assessments, reviewing evidence, and generating assessment reports. Audit Manager is a collaborative service, and audit owners benefit when other stakeholders participate in their assessments. For example, you can add other audit owners to your assessment to share management tasks. Or, if you’re an audit owner and you need help interpreting the evidence that was collected for a control, you can [delegate that control set](https://docs.aws.amazon.com/audit-manager/latest/userguide/delegate.html) to a stakeholder who has subject matter expertise in that area. Such a person is known as a *delegate* persona.  
In business terms, an audit owner is someone who coordinates and oversees the audit readiness efforts of their company, and presents evidence to an auditor. Typically, this is a governance, risk, and compliance (GRC) professional, such as a Compliance Officer or a GDPR Data Protection Officer. GRC professionals have the expertise and authority to manage audit preparation. More specifically, they understand compliance requirements, and can analyze, interpret, and prepare reporting data. However, other business roles can also assume the Audit Manager persona of an audit owner—not only GRC professionals take on this role. For example, you might choose to have your Audit Manager assessments set up and managed by a technical expert from one of the following teams:  
+ SecOps
+ IT/DevOps 
+ Security Operations Center/Incident Response
+ Similar teams that own, develop, remediate, and deploy cloud assets, and understand the cloud infrastructure of your organization
Who you choose to assign as an audit owner in your Audit Manager assessment depends greatly on your organization. It also depends on how you structure your security operations and the specifics of the audit. In Audit Manager, the same individual can assume the audit owner persona in one assessment, and the delegate persona in another.   
No matter how you choose to use Audit Manager, you can manage the separation of duties across your organization using the audit owner/delegate persona and granting specific IAM policies to each user. Through this two-step approach, Audit Manager ensures that you have full control over all of the specifics of an individual assessment. For more information, see [Recommended policies for user personas in AWS Audit Manager](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-personas).

** AWS managed source**  
An AWS managed source is an evidence source that AWS maintains for you.   
Each AWS managed source is a predefined grouping of data sources that maps to a specific common control or core control. When you use a common control as an evidence source, you automatically collect evidence for all the core controls that support that common control. You can also use individual core controls as an evidence source.  
Whenever an AWS managed source is updated, the same updates are automatically applied to all custom controls that use that AWS managed source. This means that your custom controls collect evidence against the latest definitions of that evidence source. This helps you to ensure continuous compliance as the cloud compliance environment changes.  
See also: [](#customer-managed-source), [](#evidence-source).

## C
<a name="auditmanager-concepts-C"></a>

 [A](#auditmanager-concepts-A) \| B \| [C](#auditmanager-concepts-C) \| [D](#auditmanager-concepts-D) \| [E](#auditmanager-concepts-E) \| [F](#auditmanager-concepts-F) \| G \| H \| [I](#auditmanager-concepts-I) \| J \| K \| L \| M \| N \| O \| P \| Q \| [R](#auditmanager-concepts-R) \| [S](#auditmanager-concepts-S) \| T \| U \| V \| W \| X \| Y \| Z 

**Changelog**  
For each control in an assessment, Audit Manager tracks user activity for that control. You can then review an audit trail of activities that are related to a specific control. For more information about which user activities are captured in the changelog, see [Changelog tab](review-controls.md#review-changelog). 

**Cloud compliance**  
Cloud compliance is the general principle that cloud-delivered systems must be compliant with the standards that are faced by cloud customers.

**Common control**  
See [](#control).

**Compliance regulation**  
A compliance regulation is a law, rule, or other order that's prescribed by an authority, typically to regulate conduct. One example is GDPR.

**Compliance standard**  
A compliance standard is a structured set of guidelines that detail the processes of an organization for maintaining accordance with established regulations, specifications, or legislation. Examples include PCI DSS and HIPAA. 

**Control**  
A control is a safeguard or countermeasure that’s prescribed for an information system or an organization. Controls are designed to protect the confidentiality, integrity, and availability of your information, and to meet a set of defined requirements. They provide an assurance that your resources are operating as intended, your data is reliable, and your organization is compliant with applicable laws and regulations.  
In Audit Manager, a control can also represent a question in a vendor risk assessment questionnaire. In this case, a control is a specific question that asks information about an organization’s security and compliance posture.  
Controls collect evidence continually when they’re active in your Audit Manager assessments. You can also manually add evidence to any control. Each piece of evidence is a record that helps you to demonstrate compliance with the control’s requirements.  
Audit Manager provides the following types of controls:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/concepts.html)

**Control domain**  
You can think of a control domain as a category of controls that’s not specific to any compliance standard. An example of a control domain is *Data protection*.   
Controls are often grouped by domain for simple organizational purposes. Each domain has multiple objectives.  
Control domain groupings are one of the most powerful features of the [Audit Manager dashboard](https://docs.aws.amazon.com/audit-manager/latest/userguide/dashboard.html). Audit Manager highlights the controls in your assessments that have non-compliant evidence, and groups them by control domain. This enables you to focus your remediation efforts on specific subject domains as you prepare for an audit. 

**Control objective**  
A control objective describes the goal of the common controls that fall underneath it. Each objective can have multiple common controls. If these common controls are implemented successfully, they’ll help you to fulfill the objective.  
Each control objective falls under a control domain. For example, the *Data protection* control domain might have a control objective named *Data classification and handling.* To support this control objective, you could use a common control called *Access controls* to monitor and detect unauthorized access to your resources.

** Core control**  
See [](#control).

** Custom control**  
See [](#control).

** Customer managed source**  
A customer managed source is an evidence source that you define.   
When you create a custom control in Audit Manager, you can use this option to create your own individual data sources. This gives you the flexibility to collect automated evidence from a business-specific resource, such as a custom AWS Config rule. You can also use this option if you want to add manual evidence to your custom control.  
When you use customer managed sources, you are responsible for maintaining all of the data sources that you create.  
See also: [](#aws-managed-source), [](#evidence-source).

## D
<a name="auditmanager-concepts-D"></a>

 [A](#auditmanager-concepts-A) \| B \| [C](#auditmanager-concepts-C) \| [D](#auditmanager-concepts-D) \| [E](#auditmanager-concepts-E) \| [F](#auditmanager-concepts-F) \| G \| H \| [I](#auditmanager-concepts-I) \| J \| K \| L \| M \| N \| O \| P \| Q \| [R](#auditmanager-concepts-R) \| [S](#auditmanager-concepts-S) \| T \| U \| V \| W \| X \| Y \| Z 

**Data source**  
Audit Manager uses *data sources* to collect evidence for a control. A data source has the following properties:  
+ A **data source type** defines which type of data source Audit Manager collects evidence from. 
  + For automated evidence, the type can be *AWS Security Hub CSPM*, *AWS Config, AWS CloudTrail*, or *AWS API calls.* 
  + If you upload your own evidence, the type is *Manual*. 
  + The Audit Manager API refers to a data source type as a [sourceType](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ControlMappingSource.html#auditmanager-Type-ControlMappingSource-sourceType).
+ A **data source mapping** is a keyword that pinpoints where evidence is collected from for a given data source type. 
  + For example, this might be the name of a CloudTrail event or the name of an AWS Config rule. 
  + The Audit Manager API refers to a data source mapping as a [sourceKeyword](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_SourceKeyword.html). 
+ A **data source name** labels the pairing of a data source type and mapping. 
  + For standard controls, Audit Manager provides a default name. 
  + For custom controls, you can provide your own name. 
  + The Audit Manager API refers to a data source name as a [sourceName](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ControlMappingSource.html#auditmanager-Type-ControlMappingSource-sourceName).
A single control can have multiple data source types and multiple mappings. For example, one control might collect evidence from a mixture of data source types (such as AWS Config and Security Hub CSPM). Another control might have AWS Config as its only data source type, with multiple AWS Config rules as mappings.  
The following table lists the automated data source types and shows examples of some corresponding mappings.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/concepts.html)

**Delegate**  
A delegate is an AWS Audit Manager user with limited permissions. Delegates typically have specialized business or technical expertise. For example, these expertise might be in data retention policies, training plans, network infrastructure, or identity management. Delegates help audit owners review collected evidence for controls that are in their area of expertise. Delegates can review control sets and their related evidence, add comments, upload additional evidence, and update the status of each of the controls that you assign to them for review.   
Audit owners assign specific control sets to delegates, not entire assessments. As a result, delegates have limited access to assessments. For instructions on how to delegate a control set, see [Delegations in AWS Audit Manager](delegate.md). 

## E
<a name="auditmanager-concepts-E"></a>

 [A](#auditmanager-concepts-A) \| B \| [C](#auditmanager-concepts-C) \| [D](#auditmanager-concepts-D) \| [E](#auditmanager-concepts-E) \| [F](#auditmanager-concepts-F) \| G \| H \| [I](#auditmanager-concepts-I) \| J \| K \| L \| M \| N \| O \| P \| Q \| [R](#auditmanager-concepts-R) \| [S](#auditmanager-concepts-S) \| T \| U \| V \| W \| X \| Y \| Z 

**Evidence**  
Evidence is a record that contains the information that's needed to demonstrate compliance with a control's requirements. Examples of evidence include a change activity invoked by a user, and a system configuration snapshot.   
There are two main types of evidence in Audit Manager: *automated evidence* and *manual evidence*.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/concepts.html)
Automated evidence collection starts when you create an assessment. This is an ongoing process, and Audit Manager collects evidence at different frequencies depending on the evidence type and the underlying data source. For more information, see [Understanding how AWS Audit Manager collects evidence](how-evidence-is-collected.md).   
For instructions on how to review evidence in an assessment, see [Reviewing evidence in AWS Audit Manager](review-evidence.md).

**Evidence source**  
An evidence source defines where a control collects evidence from. It can be an individual data source, or a predefined grouping of data sources that maps to a common control or a core control.   
When you create a custom control, you can collect evidence from AWS managed sources, customer managed sources, or both.   
We recommend that you use AWS managed sources. Whenever an AWS managed source is updated, the same updates are automatically applied to all custom controls that use these sources. This means that your custom controls always collect evidence against the latest definitions of that evidence source. This helps you to ensure continuous compliance as the cloud compliance environment changes.
See also: [](#aws-managed-source), [](#customer-managed-source).

**Evidence collection method**  
There are two ways that a control can collect evidence.       
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/concepts.html)
You can attach manual evidence to any automated control. In many cases, a combination of automated and manual evidence is needed to demonstrate full compliance with a control. Although Audit Manager can provide automated evidence that’s helpful and relevant, some automated evidence might only demonstrate partial compliance. In this case, you can supplement the automated evidence that Audit Manager provides with your own evidence.  
For example:  
+ The [AWS Generative AI Best Practices Framework v2](aws-generative-ai-best-practices.md) contains a control called `Error analysis`. This control requires you to identify when inaccuracies are detected in your model usage. It also requires you to conduct a thorough error analysis to understand the root causes and take corrective action.
+ To support this control, Audit Manager collects automated evidence that shows if CloudWatch alarms are enabled for the AWS account where your assessment is running. You can use this evidence to demonstrate partial compliance with the control by proving that your alarms and checks are configured correctly.
+ To demonstrate full compliance, you can supplement the automated evidence with manual evidence. For example, you can upload a policy or a procedure that shows your error analysis process, your thresholds for escalations and reporting, and the results of your root cause analysis. You can use this manual evidence to demonstrate that established policies are in place, and that corrective action was taken when prompted.
For a more detailed example, see [Controls with mixed data sources](https://docs.aws.amazon.com/audit-manager/latest/userguide/examples-of-controls.html#mixed).

**Export destination**  
An export destination is the default S3 bucket where Audit Manager saves the files that you export from evidence finder. For more information, see [Configuring your default export destination for evidence finder](settings-export-destination.md).

## F
<a name="auditmanager-concepts-F"></a>

 [A](#auditmanager-concepts-A) \| B \| [C](#auditmanager-concepts-C) \| [D](#auditmanager-concepts-D) \| [E](#auditmanager-concepts-E) \| [F](#auditmanager-concepts-F) \| G \| H \| [I](#auditmanager-concepts-I) \| J \| K \| L \| M \| N \| O \| P \| Q \| [R](#auditmanager-concepts-R) \| [S](#auditmanager-concepts-S) \| T \| U \| V \| W \| X \| Y \| Z 

**Framework**  
An Audit Manager framework structures and automate assessments for a specific standard or risk governance principle. These frameworks include a collection of prebuilt or customer defined controls, and they help you to map your AWS resources to the requirements of these controls.   
There are two types of framework in Audit Manager.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/concepts.html)
For instructions on how to create and manage frameworks, see [Using the framework library to manage frameworks in AWS Audit Manager](framework-library.md).   
AWS Audit Manager assists in collecting evidence that's relevant for verifying compliance with specific compliance standards and regulations. However, it doesn't assess your compliance itself. The evidence that's collected through AWS Audit Manager therefore might not include all the information about your AWS usage that's needed for audits. AWS Audit Manager isn't a substitute for legal counsel or compliance experts.

**Framework sharing**  
You can use the [Sharing a custom framework in AWS Audit Manager](share-custom-framework.md) feature to quickly share your custom frameworks across AWS accounts and Regions. To share a custom framework, you create a *share request.* The recipient then has 120 days to accept or decline the request. When they accept, Audit Manager replicates the shared custom framework into their framework library. In addition to replicating the custom framework, Audit Manager also replicates any custom control sets and controls that are contained within that framework. These custom controls are added to the recipient’s control library. Audit Manager doesn’t replicate standard frameworks or controls. This is because these resources are already available by default in each account and Region.

## I
<a name="auditmanager-concepts-I"></a>

 [A](#auditmanager-concepts-A) \| B \| [C](#auditmanager-concepts-C) \| [D](#auditmanager-concepts-D) \| [E](#auditmanager-concepts-E) \| [F](#auditmanager-concepts-F) \| G \| H \| [I](#auditmanager-concepts-I) \| J \| K \| L \| M \| N \| O \| P \| Q \| [R](#auditmanager-concepts-R) \| [S](#auditmanager-concepts-S) \| T \| U \| V \| W \| X \| Y \| Z 

**Inconclusive Evidence**  
AWS Audit Manager marks evidence as inconclusive when automated compliance evaluation isn't possible. This occurs in the following situations:  
+ You haven't enabled AWS Config or AWS Security Hub CSPM, which are key data sources.
+ Evidence is collected directly from AWS services via API calls, AWS CloudTrail logs, or manual uploads.
When there's no mechanism for automatic evaluation of this evidence, AWS Audit Manager can't provide evaluation details. As a result, it marks the evidence as *inconclusive*.  
Inconclusive evidence doesn't indicate failure. Instead, it signals that you need to manually evaluate the evidence for compliance.

## R
<a name="auditmanager-concepts-R"></a>

 [A](#auditmanager-concepts-A) \| B \| [C](#auditmanager-concepts-C) \| [D](#auditmanager-concepts-D) \| [E](#auditmanager-concepts-E) \| [F](#auditmanager-concepts-F) \| G \| H \| [I](#auditmanager-concepts-I) \| J \| K \| L \| M \| N \| O \| P \| Q \| [R](#auditmanager-concepts-R) \| [S](#auditmanager-concepts-S) \| T \| U \| V \| W \| X \| Y \| Z 

**Resource**  
A resource is a physical or information asset that's assessed in an audit. Examples of AWS resources include Amazon EC2 instances, Amazon RDS instances, Amazon S3 buckets, and Amazon VPC subnets.

**Resource assessment**  
A resource assessment is the process of assessing an individual resource. This assessment is based on the requirement of a control. While an assessment is active, Audit Manager runs resource assessments for each individual resource in the scope of the assessment. A resource assessment runs the following set of tasks:  

1. Collects evidence including resource configurations, event logs, and findings

1. Translates and maps evidence to controls

1. Stores and tracks the lineage of evidence to enable integrity

**Resource compliance**  
Resource compliance refers to the evaluation status of a resource that was assessed when collecting compliance check evidence.  
Audit Manager collects compliance check evidence for controls that use AWS Config and Security Hub CSPM as a data source type. Multiple resources might be assessed during this evidence collection. As a result, a single piece of compliance check evidence can include one or more resources.   
You can use the **Resource compliance** filter in evidence finder to explore compliance status at the resource level. After your search is complete, you can then preview the resources that matched your search query.  
In evidence finder, there are three possible values for resource compliance:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/concepts.html)

## S
<a name="auditmanager-concepts-S"></a>

 [A](#auditmanager-concepts-A) \| B \| [C](#auditmanager-concepts-C) \| [D](#auditmanager-concepts-D) \| [E](#auditmanager-concepts-E) \| [F](#auditmanager-concepts-F) \| G \| H \| [I](#auditmanager-concepts-I) \| J \| K \| L \| M \| N \| O \| P \| Q \| [R](#auditmanager-concepts-R) \| [S](#auditmanager-concepts-S) \| T \| U \| V \| W \| X \| Y \| Z 

**Service in scope**  
Audit Manager manages which AWS services are in scope for your assessments. If you have an older assessment, it’s possible that you manually specified the services in scope in the past. After June 04, 2024, you can’t manually specify or edit services in scope.  
A *service in scope* is an AWS service that your assessment collects evidence about. When a service is included in the scope of your assessment, Audit Manager assesses that service's resources. Some example resources include the following:   
+ An Amazon EC2 instance
+ An S3 bucket
+ An IAM user or role
+ A DynamoDB table
+ A network component such as an Amazon Virtual Private Cloud (VPC), security group, or network access control list (ACL) table
For example, if Amazon S3 is a service in scope, Audit Manager can collect evidence about your S3 buckets. The exact evidence that's collected is determined by a control's [](#control-data-source). For instance, if the data source type is AWS Config, and the data source mapping is an AWS Config rule (such as `s3-bucket-public-write-prohibited`), Audit Manager collects the result of that rule evaluation as evidence.  
Keep in mind that a service in scope is different to a *data source type*, which can also be an AWS service or something else. For more information, see [What's the difference between a service in scope and a data source type?](evidence-collection-issues.md#data-source-vs-service-in-scope) in the *Troubleshooting* section of this guide.

** Standard control**  
See [](#control).