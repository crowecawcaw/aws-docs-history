

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# EU GMP Annex 11, v1
<a name="GxP-EU-Annex-11"></a>





AWS Audit Manager provides a prebuilt framework that supports the EudraLex - The Rules Governing Medicinal Products in the European Union (EU) - Volume 4: Good Manufacturing Practice (GMP) Medicinal Products for Human and Veterinary Use - Annex 11.

**Topics**
+ [What is the EU GMP Annex 11?](#what-is-GxP-EU-Annex-11)
+ [Using this framework](#framework-GxP-EU-Annex-11)
+ [Next steps](#next-steps-GxP-EU-Annex-11)

## What is the EU GMP Annex 11?
<a name="what-is-GxP-EU-Annex-11"></a>

The EU GMP Annex 11 framework is the European equivalent to the Title 21 CFR part 11 framework in the United States. This annex applies to all forms of computerized systems that are used as part of Good Manufacturing Practices (GMP) regulated activities. A computerized system is a set of software and hardware components that together fulfill certain functionalities. The application should be validated and IT infrastructure should be qualified. Where a computerized system replaces a manual operation, there should be no resultant decrease in product quality, process control, or quality assurance. There should be no increase in the overall risk of the process.

Annex 11 is part of the European GMP guidelines and defines the terms of reference for computerized systems that are used by organizations in the pharmaceutical industry. Annex 11 functions as a checklist that enables the European regulatory agencies to establish the requirements for computerized systems that relate to pharmaceutical products and medical devices. The guidelines set by the Commission of the European Committees aren't that much distant from the FDA (Title 21 CFR Part 11). Annex 11 defines the criteria for how electronic records and electronic signatures are considered to be managed. 

## Using this framework
<a name="framework-GxP-EU-Annex-11"></a>

You can use the EU GMP Annex 11 framework to help you prepare for audits. This framework includes a prebuilt collection of controls with descriptions and testing procedures. These controls are grouped into control sets according to EU GMP requirements. You can also customize this framework and its controls to support internal audits with specific requirements. 

Using the framework as a starting point, you can create an Audit Manager assessment and start collecting evidence that’s relevant for your audit. After you create an assessment, Audit Manager starts to assess your AWS resources. It does this based on the controls that are defined in the EU GMP Annex 11 framework. When it's time for an audit, you—or a delegate of your choice—can review the evidence that Audit Manager collected. Either, you can browse the evidence folders in your assessment and choose which evidence you want to include in your assessment report. Or, if you enabled evidence finder, you can search for specific evidence and export it in CSV format, or create an assessment report from your search results. Either way, you can use this assessment report to show that your controls are working as intended. 

The framework details are as follows:


| Framework name in AWS Audit Manager | Number of automated controls | Number of manual controls | Number of control sets | 
| --- | --- | --- | --- | 
| EudraLex - The Rules Governing Medicinal Products in the European Union (EU) - Volume 4: Good Manufacturing Practice (GMP) Medicinal Products for Human and Veterinary Use - Annex 11 | 0 | 32 | 3 | 

**Important**  
To ensure that this framework collects the intended evidence from AWS Config, make sure that you enable the necessary AWS Config rules. To review the AWS Config rules that are used as data source mappings in this standard framework, download the [AuditManager\_ConfigDataSourceMappings\_EudraLex-GMP-Volume-4-Annex-11.zip](samples/AuditManager_ConfigDataSourceMappings_EudraLex-GMP-Volume-4-Annex-11.zip) file.

The controls in this framework aren't intended to verify if your systems are compliant with the EU GMP Annex 11 requirements. Moreover, they can't guarantee that you'll pass a EU GMP audit. AWS Audit Manager doesn't automatically check procedural controls that require manual evidence collection. 

## Next steps
<a name="next-steps-GxP-EU-Annex-11"></a>

For instructions on how to view detailed information about this framework, including the list of standard controls that it contains, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md). 

For instructions on how to create an assessment using this framework, see [Creating an assessment in AWS Audit Manager](create-assessments.md). 

For instructions on how to customize this framework to support your specific requirements, see [Making an editable copy of an existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md). 