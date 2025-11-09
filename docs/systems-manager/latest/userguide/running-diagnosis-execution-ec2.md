AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Running a diagnosis and optional

remediation for unmanaged EC2 instances

Use the following procedure to diagnose the network-related and VPC-related issues
that might be preventing Systems Manager from managing your EC2 instances.

The diagnosis operation can detect and group together issues of the following
types:

- **Network configurations issues** – Types of
  networking issues that might be preventing EC2 instances from communicating
  with the Systems Manager service in the cloud. Remediation operations might be
  available for these issues. For more information about the network
  configuration issues, see [Categories of diagnosable unmanaged
  EC2 instance issues](diagnosing-ec2-category-types.md "diagnosing-ec2-category-types.md").
- **Unidentified issues** – A list of findings for
  cases where the diagnostic operation was unable to determine why EC2
  instances are not able to communicate with the Systems Manager service in the
  cloud.

###### To run a diagnosis and remediation for unmanaged EC2 instances

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Diagnose and
   remediate**.
3. Choose the **Unmanaged EC2 instances issue** tab.
4. In the **Issue summary** section, choose **Run
   new diagnosis**.

-or-

If this is your first time to diagnose unmanaged EC2 issues, in the
**Diagnose unmanaged EC2 instances** section, choose
**Execute**.

###### Tip

While the diagnosis is running, choose **View
progress** or **View executions** to
monitor the current state of the execution. For more information, see
[Viewing execution progress
and history for remediations in Systems Manager](diagnose-and-remediate-execution-history.md "diagnose-and-remediate-execution-history.md"). 5. After the diagnosis completes, do the following:

    * For any issues reported in the **Unidentified
     issues** section, choose the **Learn
     more** link for information about resolving the
     problem.
    * For issues reported in the **Network configurations
     issues** section, continue with the next step.

6.  In the list of finding types, in the **Recommendations**
    column, for a particular issue, choose the link, such as **2
    recommendations**.
7.  In the **Recommendations** pane that opens, choose from
    the available mitigations:
    - **Learn more** – Open a topic with
      information about how to resolve an issue manually.
    - **View runbook** – Open a pane with
      information about the Automation runbook you can execute to resolve
      the issue with your EC2 instances, as well as options for generating
      a _preview_ of the actions that runbook would
      take. Continue with the next step.

8.  In the runbook pane, do the following:
    1. For **Document description**, review the content,
       which provides an overview of the actions the runbook can take to
       remediate your unmanaged EC2 instance issues. Choose **View
       steps** to preview the individual actions the runbook
       would take.
    2. For **Targets**, do the following:
       - If you are managing remediations for an organization, for
         **Accounts**, specify whether this
         runbook would target all accounts, or only a subset of
         accounts you choose.
       - For **Regions**, specify whether this
         runbook would target all AWS Regions in your account or
         organization, or only a subset of Regions you choose.

    3. For **Runbook preview**, carefully review the
       information. This information explains what the scope and impact
       would be if you choose to execute the runbook.

    ###### Note

    Choosing to execute the runbook would incur charges. Review
    the preview information carefully before deciding whether to
    proceed.

    The **Runbook preview** content provides the
    following information:

        * How many Regions the runbook operation would occur
         in.
        * (Organizations only) How many organizational units (OUs)
         the operation would run in.
        * The types of actions that would be taken, and how many of
         each.


        Action types include the following:




        	+ **Mutating**: The
        	 runbook step would make changes to the targets
        	 through actions that create, modify, or delete
        	 resources.
        	+ **Non-mutating**: The
        	 runbook step would retrieve data about resources but
        	 not make changes to them. This category generally
        	 includes `Describe*`, `List*`,
        	 `Get*`, and similar read-only API
        	 actions.
        	+ **Undetermined**: An
        	 undetermined step invokes executions performed by
        	 another orchestration service like AWS Lambda,
        	 AWS Step Functions, or AWS Systems Manager Run Command. An undetermined
        	 step might also call a third-party API. Systems Manager
        	 Automation doesn’t know the outcome of the
        	 orchestration processes or third-party API
        	 executions, so the results of the steps are
        	 undetermined.

    4.  At this point, you can choose one of the following actions:

            * Stop and do not execute the runbook.
            * Choose **Execute** to run the runbook
             with the options you have already selected.If you choose to run the operation, choose **View

        progress** or **View executions\*\* to monitor
        the current state of the execution. For more information, see [Viewing execution progress
        and history for remediations in Systems Manager](diagnose-and-remediate-execution-history.md "diagnose-and-remediate-execution-history.md").
