# Reviewing and executing suggested runbook remediations for CloudWatch investigations

When you add a hypothesis to the **Feed** area of an active
investigation, CloudWatch investigations might display **Show suggested actions**. One
suggested action might be to view documentation with information to help you remediate a
problem manually.

Another suggestion might be to use an _Automation
runbook_ to attempt to automatically resolve the issue. Automation is a
capability in Systems Manager, another AWS service. Automation runbooks define a series of
steps, or actions, to be run on the resources that you select. Each runbook is designed
to address a specific issue. Runbooks can address a variety of operational needs:
Creating, repairing, reconfiguring, installing, troubleshooting, remediating,
duplicating, and more. For more information about Automation, see [Integration with AWS Systems Manager Automation](Investigations-Integrations.md#Investigations-Integrations-SSM "Investigations-Integrations.md#Investigations-Integrations-SSM").

###### Before you begin

Before working with Automation runbooks in an investigation, be aware of the
following important considerations:

- Choosing to execute a runbook incurs charges. For information, see [AWS Systems Manager
  pricing](https://aws.amazon.com/systems-manager/pricing/#Automation "https://aws.amazon.com/systems-manager/pricing/#Automation").
- Root causes and runbook suggestions are powered by automated reasoning and
  generative artificial intelligence services.

###### Important

You are responsible for actions that result from executing runbook steps
and the choice of parameter values entered during runbook execution. You
might need to edit the suggested runbook to make sure the runbook performs
as expected. For more information, see [**AWS responsible
AI policy**](https://aws.amazon.com/ai/responsible-ai/policy/ "https://aws.amazon.com/ai/responsible-ai/policy/").

- Depending on the runbook, you might need to enter values for the runbook's
  **Input parameters** before the execution can run.
- The runbook executes using the IAM permissions assigned to the operator. If
  necessary, sign in with different IAM permissions to execute the runbook. In
  addition to permissions for the actions being taken, you'll need additional
  Systems Manager permissions to execute runbook steps. For more information, see [Setting up
  Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md") in the _AWS Systems Manager User Guide_.

###### To review and execute suggested runbook actions for CloudWatch investigations

1. To view information about a suggested runbook, choose
   **Review** for information about how to execute the runbook
   steps.

On the investigation details page, choose **Suggestions**. 2. In the **Suggestions** pane, review the list of hypotheses
based on the system's analysis of the issue under investigation.

For each hypothesis, you can choose from the following options:

    * **Show reasoning** – View more information
     about why the system has generated the hypothesis.
    * **View actions** – View the suggested actions
     for the issue. Not all hypotheses will include suggested actions.
    * **Accept** – Accept the hypothesis and add it
     to the investigation's **Feed** section.


    ###### Note

    Accepting the hypothesis doesn't automatically run the associated
     runbook solution. You can view suggested runbooks before accepting a
     hypothesis, but you must accept the hypothesis to execute a
     runbook.
    * **Discard** – Reject the hypothesis and don't
     engage with it any further.

3.  After you choose **View action**, in the **Suggested
    actions** pane, review the list of suggested actions you can take
    to address the issue. Suggested actions can include one or more of the
    following:
    - **AWS knowledge articles** – Provides
      information about steps you can take to manually address the issue, plus
      a link to more information.
    - **AWS documentation** – Provides
      links to user documentation topics related to the issue.
    - **AWS-owned runbooks** – Lists one or more
      Automation runbooks that are managed by AWS that you can run to
      attempt issue resolution.
    - **Runbooks owned by you** – Lists one or more
      custom Automation runbooks created by you or someone else in your
      account or organization, which you can run to attempt issue resolution.

    ###### Note

    The system automatically generates this list of runbooks by
    evaluating keywords in your custom runbooks and then comparing them
    to terms related to the issue being investigated.

    More keyword matches mean a particular custom runbook appears
    higher in the **Runbooks owned by you**
    list.

4.  After reviewing the hypothesis, you can examine a specific suggested action
    further and read related documentation by choosing **Learn
    more**. You can also choose **Review details** to
    inspect suggested runbooks owned by AWS and you.
5.  When choosing **Review details** for runbooks, do the
    following:
    1. For **Runbook description**, review the content,
       which provides an overview of the actions the runbook can take to
       remediate the issue being investigated. Choose **View
       steps** to visualize the runbook's workflow and drill into
       the details of individual steps.
    2. For **Input parameters**, specify values for any
       parameters required by the runbook. These parameters vary from runbook
       to runbook.
    3. For **Execution preview**, carefully review the
       information. This information explains what the scope and impact would
       be if you choose to execute the runbook.

    The **Execution preview** content provides the
    following information:

        * How many accounts and Regions the runbook operation would
         occur in.
        * The types of actions that would be taken, and how many of each
         type.


        Action types include the following:




        	+ `Mutating`: A runbook step would make
        	 changes to the targets through actions that create,
        	 modify, or delete resources.
        	+ `Non-Mutating`: A runbook step would
        	 retrieve data about resources but not make changes to
        	 them. This category generally includes
        	 `Describe`, `List`,
        	 `Get`, and similar read-only API
        	 actions.
        	+ `Undetermined`: An undetermined step
        	 invokes executions performed by another orchestration
        	 service like AWS Lambda, AWS Step Functions, or Run Command, a
        	 capability of AWS Systems Manager. An undetermined step might also
        	 call a third-party API or run a Python or PowerShell
        	 script. Systems Manager Automation can't detect what the outcome
        	 would be of the orchestration processes or third-party
        	 API executions, and therefore can't evaluate them. The
        	 results of those steps would have to be manually
        	 reviewed to determine their impact.
        For information about supported actions and their impact
         types, see [Remediation impact types of runbook actions](../../../systems-manager/latest/userguide/remediation-impact-type.md "../../../systems-manager/latest/userguide/remediation-impact-type.md") in the
         *AWS Systems Manager User Guide*.

    4. Review the preview information carefully before deciding whether to
       proceed.

    At this point, you can choose one of the following actions:

        * Stop and do not execute the runbook.
        * Change the input parameters before executing the
         runbook.
        * Execute the runbook with the options you have already
         selected.###### Important

Choosing to execute the runbook incurs charges. For information, see
[AWS Systems Manager pricing](https://aws.amazon.com/systems-manager/pricing/#Automation "https://aws.amazon.com/systems-manager/pricing/#Automation"). 6. If you want to execute the runbook, choose
**Execute**.

If you already accepted the hypothesis, the execution runs.

If you have not already accepted the hypothesis, a dialog box prompts you to
accept it before the execution runs.
After you choose **Execute** for a runbook, that action is added to
the **Feed** pane of the investigation. From the investigation, you can
monitor new data in the metrics in the findings to see if the runbook actions are
correcting the issue.
