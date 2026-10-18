

# Private workflows in HealthOmics
<a name="private-workflows"></a>

Use *Private workflows* when you want to create your own workflow definition. The workflow definition specifies information about the workflow and defines the workflow tasks. A *run* is a single invocation of a workflow, and a *task* is a single process within the run.

HealthOmics supports workflow definitions that you create in Nextflow, Workflow Description Language (WDL), or Common Workflow Language (CWL).

Working with HealthOmics private workflows involves four stages. Choose a tab for details.

------
#### [ Setting up ]

You can create a workflow and an optional configuration for internet access.
+ **[Creating workflows](workflows-setup.md)** and **[workflow versions](workflow-versions.md)** – A workflow is your pipeline definition. It defines its tasks, outputs, and configuration. You can also create versions of a private workflow to update the pipeline definition. Workflow versioning provides the ability for users to choose when to start using updated functionality. Workflow versions are immutable and provide the same level of data provenance as workflows.
+ **[Configuration](workflows-vpc-networking.md#vpc-configuration-apis)** – This is an optional setting that you create when a workflow needs internet access.
+ **[IAM permissions](omics-permissions.md)** – Before you run a workflow, configure the IAM permissions that workflows require. HealthOmics uses IAM service roles to access other services (such as Amazon S3, Amazon ECR, and CloudWatch) on your behalf to complete the processes defined in your workflow.

------
#### [ Execution ]

After you create a private workflow, you can start a single run or start multiple runs together.
+ **[Start a run](running-workflows.md)** – You can start a single run of a private workflow that you created with your input dataset. HealthOmics executes your private workflow definition with each task as a single process within that run.
+ **[Start a batch run](workflows-batch.md)** – A batch run executes many runs (for example, more than four runs at the same time) of the same workflow together in a single submission. Instead of launching runs one at a time, you submit a batch run and HealthOmics orchestrates them.
+ **[Monitoring runs](monitoring-overview.md)** – HealthOmics emits real-time logs and metrics for you to monitor your runs using CloudWatch and EventBridge. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take actions when a specified metric reaches a threshold that you specify.

------
#### [ Optimization and governance ]

You can control compute usage, prioritize runs, or reuse previous run results for one or more of your runs.
+ **[Run groups](creating-run-groups.md)** – You can add private workflows to a run group to control compute usage. A run group is a collection of workflow runs that share a set of resource limits, such as maximum concurrent runs and maximum run duration. You set these limits to control the compute resources that the run group consumes.
+ **[Call caching](workflows-call-caching.md)** – You can use a call cache to save and reuse task outputs, which results in shorter run durations and compute cost savings.
+ **[Run optimization](workflows-run-optimize.md)** – You can optimize runs for total cost, total run time, or a combination of both. HealthOmics provides data and tools to help you with run optimization decisions.

------
#### [ Collaboration ]

You can collaborate with other AWS accounts by sharing your private workflows.
+ **[Sharing workflows](sharing-workflows.md)** – You can share your private workflows with other AWS accounts in the same Region. A subscriber account can then start runs of a workflow it does not own. Setup, execution, and optimization all happen inside one account, whereas sharing crosses the account boundary.

------

For full examples of how to use HealthOmics private workflows, see the [aws-healthomics-tutorials repository](https://github.com/aws-samples/aws-healthomics-tutorials) on GitHub or the [AWS HealthOmics end-to-end workshop](https://catalog.workshops.aws/amazon-omics-end-to-end) in the AWS Builder Center workshop catalog.

**Topics**
+ [Creating private workflows in HealthOmics](workflows-setup.md)
+ [Workflow versioning in HealthOmics](workflow-versions.md)
+ [Using HealthOmics runs](running-workflows.md)
+ [Batch runs in HealthOmics](workflows-batch.md)
+ [Using HealthOmics run groups](creating-run-groups.md)
+ [Call caching for HealthOmics runs](workflows-call-caching.md)
+ [Sharing HealthOmics workflows](sharing-workflows.md)
+ [Connecting HealthOmics workflows to a VPC](workflows-vpc-networking.md)
+ [Internet access for VPC-connected workflows](workflows-vpc-internet.md)