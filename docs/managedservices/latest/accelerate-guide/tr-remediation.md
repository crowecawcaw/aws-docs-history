# Work with remediations in Trusted Remediator

## Track remediations in Trusted Remediator

To track OpsItems remediations, complete the following steps:

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Choose **Operations Management**, **OpsCenter**.
3. (Optional) Filter the list by **Source=Trusted Remediator** to include only Trusted Remediator OpsItems in the list.

The following is an example of the OpsCenter screen filtered by **Source=Trusted Remediator**:

![An example of the Attributes section.](images/tr-opsitems-console.png)

###### Note

In addition to viewing OpsItems from the OpsCenter, you can view remediation logs in the AMS S3 bucket. For more information, see
[Remediation logs in Trusted Remediator](tr-logging.md "tr-logging.md").

## Run manual remediations in Trusted Remediator

Trusted Remediator creates OpsItems for checks configured for manual remediation. You must review these checks and begin the remediation process manually.

To manually remediate the OpsItem, complete the following steps:

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Choose **Operations Management**, **OpsCenter**.
3. (Optional) Filter the list by **Source=Trusted Remediator** to include only Trusted Remediator OpsItems in the list.
4. Choose the OpsItem that you want to review.
5. Review the operational data of the OpsItem. The operational data includes the following items:
   - **trustedAdvisorCheckCategory:** The category of the Trusted Advisor check ID. For example, Fault tolerance
   - **trustedAdvisorCheckId:** The unique Trusted Advisor check ID.
   - **trustedAdvisorCheckMetadata:** The resource metadata, including the resource ID.
   - **trustedAdvisorCheckName:** The name of the Trusted Advisor check.
   - **trustedAdvisorCheckStatus:** The status of the Trusted Advisor check detected for the resource.

6. To manually remediate the OpsItem, complete the following steps:
   1. From **Runbooks**, choose one of associated runbooks (SSM documents).
   2. Choose **Execute**.
   3. For **AutomationAssumeRole** , choose `arn:aws:iam::`AWS accountID`:role/ams_ssm_automation_role`.
      Replace AWS accountID with the account ID where the remediation runs. For other parameter values, see the **Operation data**.

   To manually remediate resources, the role or user used to authenticate to the AWS account must have the `iam:PassRole` permissions for the IAM role
   `ams-ssm-automation-role`. For more information, see [Granting a user permissions to
   pass a role to an AWS service](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") or contact your Cloud Architect. 4. Choose **Execute**. 5. Monitor the SSM document execution's progress in the **Latest status and results** column. 6. After the document completes, choose **Set Status**, **Resolved** to manually resolve the OpsItem. If the document failed, then review the
   details and re-run the SSMdocument. For additional troubleshooting support, create a service request.To resolve an OpsItem without remediation, select **Set Status** to **Resolved**.

7. Repeat steps 3 and 4 for all remaining manual remediation OpsItems.

## Troubleshoot remediations in Trusted Remediator

For assistance with manual remediations and remediation failures, contact AMS.

To view remediation status and results, complete the following steps:

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Choose **Operations Management**, **OpsCenter**.
3. (Optional) Filter the list by **Source=Trusted Remediator** to include only Trusted Remediator OpsItems in the list.
4. Choose the OpsItem that you want to review.
5. In the **Automation Executions** section review the **Document Name** and **Status and results**.
6. Review the following common automation failures. If your issues isn't listed here, then contact your CSDM for assistance.

**Common remediation errors**

No executions associated with the OpsItem might indicate that the execution failed to start due to incorrect parameter values.

###### Troubleshooting steps

1. In the **Operational data**, review the `trustedAdvisorCheckAutoRemediation` property value.
2. Verify that the **DocumentName** and **Parameters** values are correct. For the correct values, review
   [Configure Trusted Advisor check remediation in Trusted Remediator](tr-configure-remediations.md "tr-configure-remediations.md") for details on how to configure SSM parameters. To review supported
   check parameters, see [Trusted Advisor checks supported by Trusted Remediator](tr-supported-checks.md "tr-supported-checks.md")
3. Verify that values in the SSM document match allowed patterns. To view parameters details in the document content, select the document name in the
   **Runbooks** section.
4. After you review and correct the parameters, [manually run the SSM document again](tr-remediation.md "tr-remediation.md").
5. To prevent this error from reoccurring, make sure that you configure the remediation with the correct **parameter** values in your
   configuration. For more information, see [Configure Trusted Advisor check remediation in Trusted Remediator](tr-configure-remediations.md "tr-configure-remediations.md")
   Remediation documents contain multiple steps that interact with AWS services performing various actions through APIs. To identify a specific cause for the
   failure, complete the following steps:

###### Troubleshooting steps

1. To view the individual execution steps, choose the **Execution ID**, link in the **Automation Executions** section.
   The following is an example of the Systems Manager console showing the **Exection steps** for a selected automation:

![An example of the Systems Manager console showing a selected automation.](images/tr-troubleshooting.png) 2. Choose the step with the **Failed** status. The following are example error messages:

    * `NoSuchBucket - An error occurred (NoSuchBucket) when calling the GetPublicAccessBlock operation: The specified bucket does not exist`


    This error indicates that the incorrect bucket name was specified in the remediation configuration's preconfigured-parameters.


    To resolve this error, [manually run the automation](tr-remediation.md "tr-remediation.md") using the correct bucket name. To prevent this issue from reoccurring,
     [update the remediation configuration](tr-configure-remediations.md "tr-configure-remediations.md") with the correct bucket name.
    * `DB instance my-db-instance-1 is not in available status for modification.`


    This error indicates that the automation couldn't make the expected changes because the DB instance was in an invalid state.


    To resolve this error, [manually run the automation](tr-remediation.md "tr-remediation.md").
