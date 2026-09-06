

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# AWS Operational Best Practices
<a name="OBP"></a>





AWS Audit Manager provides a prebuilt AWS Operational Best Practices (OBP) framework to assist you with your audit preparation. 

This framework offers a subset of controls from the AWS Foundational Security Best Practices standard. These controls serve as baseline checks to detect when your deployed accounts and resources deviate from security best practices.

**Topics**
+ [What is the AWS Foundational Security Best Practices standard?](#what-is-OBP)
+ [Using this framework](#framework-OBP)
+ [Next steps](#next-steps-OBP)
+ [Additional resources](#resources-operational-best-practices)

## What is the AWS Foundational Security Best Practices standard?
<a name="what-is-OBP"></a>

You can use the *AWS Foundational Security Best Practices* standard to evaluate your accounts and workloads and quickly identify areas of deviation from best practices. The standard provides actionable and prescriptive guidance on how to improve and maintain your organization’s security posture.

The controls include best practices from across multiple AWS services. Each control is assigned a category that reflects the security function that it applies to. For more information, see [Control categories](https://docs.aws.amazon.com/securityhub/latest/userguide/control-categories.html) in the *AWS Security Hub CSPM User Guide*.

## Using this framework
<a name="framework-OBP"></a>

You can use the *AWS Operational Best Practices* framework to help you prepare for audits. This framework includes a prebuilt collection of controls with descriptions and testing procedures. These controls are grouped into control sets according to AWS Operational Best Practices requirements. You can also customize this framework and its controls to support internal audits with specific requirements. 

The AWS Operational Best Practices framework details are as follows:


| Framework name in AWS Audit Manager | Number of automated controls | Number of manual controls | Number of control sets | 
| --- | --- | --- | --- | 
| AWS Operational Best Practices | 0 | 51 | 20 | 

**Important**  
To ensure that this framework collects the intended evidence from AWS Security Hub CSPM, make sure that you enabled all standards in Security Hub CSPM.

The controls in this framework aren't intended to verify if your systems are compliant with AWS Operational Best Practices. Moreover, they can't guarantee that you'll pass an AWS Operational Best Practices audit. 

This framework contains only manual controls. These manual controls don't collect evidence automatically. AWS Audit Manager doesn't automatically check procedural controls that require manual evidence collection.

## Next steps
<a name="next-steps-OBP"></a>

For instructions on how to view detailed information about this framework, including the list of standard controls that it contains, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md). 

For instructions on how to create an assessment using this framework, see [Creating an assessment in AWS Audit Manager](create-assessments.md). 

For instructions on how to customize this framework to support your specific requirements, see [Making an editable copy of an existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md). 

## Additional resources
<a name="resources-operational-best-practices"></a>
+ [AWS Foundational Security Best Practices standard](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp.html) in the *AWS Security Hub CSPM User Guide*
+ [Control categories](https://docs.aws.amazon.com/securityhub/latest/userguide/control-categories.html) in the *AWS Security Hub CSPM User Guide*