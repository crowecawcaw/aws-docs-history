

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# FedRAMP Security Baseline Controls r4
<a name="fedramp-moderate"></a>





AWS Audit Manager provides a prebuilt standard framework that supports the Federal Risk And Authorization Management Program (FedRAMP) Security Baseline Controls r4.

**Topics**
+ [What is FedRAMP?](#what-is-fedramp-moderate)
+ [Using this framework](#framework-fedramp-moderate)
+ [Next steps](#next-steps-fedramp-moderate)
+ [Additional resources](#resources-fedramp-moderate)

## What is FedRAMP?
<a name="what-is-fedramp-moderate"></a>

FedRAMP was established in 2011. It provides a cost-effective, risk-based approach for the adoption and use of cloud services by the U.S. federal government. FedRAMP empowers federal agencies to use modern cloud technologies, with an emphasis on the security and protection of federal information.

For more information about the FedRAMP moderate baseline controls, see the [FedRAMP Moderate Security Test Case Procedures Template](https://www.fedramp.gov/assets/resources/templates/SAP-Appendix-A-FedRAMP-Moderate-Security-Test-Case-Procedures-Template.xlsx). 

## Using this framework
<a name="framework-fedramp-moderate"></a>

You can use the FedRAMP r4 framework to help you prepare for audits. This framework includes a prebuilt collection of controls with descriptions and testing procedures. These controls are grouped into control sets according to FedRAMP r4 requirements. You can also customize this framework and its controls to support internal audits with specific requirements. 

Using the framework as a starting point, you can create an Audit Manager assessment and start collecting evidence that’s relevant for your audit. After you create an assessment, Audit Manager starts to assess your AWS resources. It does this based on the controls that are defined in the framework. When it's time for an audit, you—or a delegate of your choice—can review the evidence that Audit Manager collected. Either, you can browse the evidence folders in your assessment and choose which evidence you want to include in your assessment report. Or, if you enabled evidence finder, you can search for specific evidence and export it in CSV format, or create an assessment report from your search results. Either way, you can use this assessment report to show that your controls are working as intended. 

The FedRAMP Moderate Baseline framework details are as follows:


| Framework name in AWS Audit Manager | Number of automated controls | Number of manual controls | Number of control sets | 
| --- | --- | --- | --- | 
| Federal Risk And Authorization Management Program (FedRAMP) Security Baseline Controls r4, Moderate | 36 | 289 | 17 | 

**Important**  
To ensure that this framework collects the intended evidence from AWS Security Hub CSPM, make sure that you enabled all standards in Security Hub CSPM.  
To ensure that this framework collects the intended evidence from AWS Config, make sure that you enable the necessary AWS Config rules. To review the AWS Config rules that are used as data source mappings in this standard framework, download the [AuditManager\_ConfigDataSourceMappings\_FedRAMP-Security-Baseline-Controls-r4-Moderate.zip](samples/AuditManager_ConfigDataSourceMappings_FedRAMP-Security-Baseline-Controls-r4-Moderate.zip) file.

The controls in this framework aren't intended to verify if your systems are compliant with FedRAMP r4. Moreover, they can't guarantee that you'll pass a FedRAMP audit. AWS Audit Manager doesn't automatically check procedural controls that require manual evidence collection.

## Next steps
<a name="next-steps-fedramp-moderate"></a>

For instructions on how to view detailed information about this framework, including the list of standard controls that it contains, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md). 

For instructions on how to create an assessment using this framework, see [Creating an assessment in AWS Audit Manager](create-assessments.md). 

For instructions on how to customize this framework to support your specific requirements, see [Making an editable copy of an existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md). 

## Additional resources
<a name="resources-fedramp-moderate"></a>
+ [AWS Compliance page for FedRAMP](https://aws.amazon.com/compliance/fedramp)
+ [AWS FedRAMP blog posts](https://aws.amazon.com/blogs/security/tag/fedramp)