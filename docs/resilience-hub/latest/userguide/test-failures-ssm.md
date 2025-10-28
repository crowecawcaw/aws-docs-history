# Analyzing AWS FIS experiment execution using AWS

Systems Manager

After running an AWS FIS experiment, you can view the execution details in the AWS
Systems Manager.

1. Go to **CloudTrail** > **Event
   History**.
2. Filter events by **User name** using the
   experiment ID.
3. View the StartAutomationExecution entry. **Request
   ID** is the SSM automation ID.
4. Go to **AWS Systems Manager** > **Automation**.
5. Filter by **Execution ID** using SSM
   automation ID and view the automation details.

You can analyze the execution with any Systems Manager automation. For more
information, see the [AWS Systems Manager Automation](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md") user guide. The execution input
parameters appear in the **Input parameters**
section of the **Execution Detail** and include
optional parameters not appearing in the AWS FIS experiment.

You can find information on step status and other step details by drilling
down to specific steps within the Execution steps.
**Common failures**

The following are common failures encountered while executing an assessment
report:

- Alarm template was not deployed before the Test/SOP experiment was
  executed. This causes an error message during the automation step.
  - **Failure message:**
    `The following parameters were not found:
 [/ResilienceHub/Alarm/3dee49a1-9877-452a-bb0c-a958479a8ef2/nat-gw-alarm-bytes-out-to-source-2020-09-21_nat-02ad9bc4fbd4e6135].
 Make sure all the SSM parameters in automation document are
 created in SSM Parameter Store.`
  - **Remediation:** Ensure to render the
    relevant alarm and deploy the resulting template before rerunning
    the fault injection experiment.

- Missing permissions in the execution role. This error message occurs if
  the provided execution role is missing a permission and appears within the
  step details.
  - **Failure message:**
    `An error occurred (Unauthorized Operation) when calling the
 DescribeInstanceStatus operation: You are not authorized to
 perform this operation. Please Refer to Automation Service
 Troubleshooting Guide for more diagnosis details`.
  - **Remediation**: Verify you provided
    the correct execution role. If this was done, add the required
    permission and rerun the assessment.

- Execution succeeded but did not have the expected result. This is the
  result of incorrect parameters or an internal automation issue.
  - **Failure message:** The execution
    succeeded, so no error message is shown.
  - **Remediation:** Check the input
    parameters and look at the executed steps as explained in the
    Analyze AWS FIS experiment execution before examining the individual
    steps for expected inputs and outputs.
