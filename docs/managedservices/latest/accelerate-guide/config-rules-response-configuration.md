# AMS Config Rules Response Configuration report

The AMS Config Rules Response Configuration report provides an in-depth look at how you currently have Accelerate configured to respond to non-compliant AMS config rules. For more information on how to change the response for AMS config rules, see [AMS Accelerate Customized findings responses](custom-findings-responses.md "custom-findings-responses.md").

This report only shows the configurations that you have changed, and excludes the AMS default configurations that are listed in the [AMS Config Rules Library](acc-sec-compliance.md "acc-sec-compliance.md"). The report provides data on resource and AMS config rule response configuration of AMS accounts, including the following:

- The list of AWS accounts for which you changed the default response for AMS config rules.
- The list of tags for which you have associated a response for AMS config rules.
- The list of response configurations for each rule, account, and tag.
- The list of resources for which you have changed the default response for AMS config rules.

## Latest Response Configurations Report

| **Field**                  | **Description**                                                                 |
| -------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Date                       | Date in which the report was generated                                          |
| Customer name              | Customer name                                                                   |
| AWS account ID             | The AWS account ID associated with the configuration                            |
| Account Name               | AWS account name of account level resource group                                |
| Finding Type               | Type of finding identified. In this case, AWS Config                            |
| Source Identifier          | AWS Config Rule Unique Source Identifier                                        |
| Resource Group ID          | The Resource Group ID associated with the response configuration                |
| Response Action Configured | Action type triggered by AMS                                                    |
| SSM Runbook Associated     | The Remediation Runbook that will be run, if any                                |
| Resource Group Type        | This can be Account or Tag                                                      | ## Resources with Custom Default Response of Config Rules |
| **Field Name**             | **Definition**                                                                  |
| ---                        | ---                                                                             |
| Customer Name              | Customer name                                                                   |
| Date                       | Date in which the report was generated                                          |
| AWS Account Name           | AWS account name                                                                |
| Account ID                 | Associated AWS account ID                                                       |
| AMS Config Rule            | AMS config rule that's targeting the resource and applying with a configuration |
| Resource ID                | The resource ID in the customer account targeted by the AMS config rule         |
| Resource Region            | The AWS Region that the configuration is applied in                             |
| Resource Type              | AWS resource type                                                               |
| Resource Group ID          | The Resource group ID associated with the response configuration                |
| Resource AMS Flag          | If the AWS resource is deployed by AMS, then this field is set to `True`        |
| Trigger Type               | The type of response configured for the resource                                |
| Compliance Flag            | AMS config rule compliance state                                                |
