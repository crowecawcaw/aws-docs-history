# Configure image pipeline workflows in Image Builder

With image workflows, you can customize the workflows that your pipeline runs to build,
test, and distribute images according to your needs. The workflows that you define run within the
context of the Image Builder workflow framework. For more information about the stages that
make up the workflow framework, see [Manage build, test, and distribution workflows for Image Builder images](manage-image-workflows.md "manage-image-workflows.md").

Build workflow

Build workflows run during the `Build` stage of the
workflow framework. You can specify only one build workflow for
your pipeline. Or you can skip the build entirely to configure a
test-only pipeline.

Test workflow

Test workflows run during the `Test` stage of the
workflow framework. You can add one or more test workflows to
your pipeline, up to the limit of ten workflows total, which also
counts your build and distribution workflows. Test workflows can run in
parallel or one at a time, depending on how you define your test groups. You
can also skip tests entirely if you only want your pipeline to build.

Distribution workflow

Distribution workflows run during the `Distribution` stage of the
workflow framework. A distribution workflow is optional. If you do not specify one,
Image Builder still distributes your AMI by running the distribution configuration that you
attach to the pipeline or image. Specify a distribution workflow when you want to
override that distribution configuration with different distribution settings, or to
gain more visibility into the distribution process. You can specify one distribution
workflow for your pipeline. If you build container images and do not specify a
distribution workflow, Image Builder adds the Amazon managed container-distribution workflow
for you.

## Define test groups for test workflows

You define test workflows within test groups. You can run multiple test workflows for your
pipeline. The combined limit is ten workflows total, which includes your build and distribution
workflows. You decide whether to run the test workflows in a specific order or to run as many as
possible at the same time. How they run depends on how you define your test groups. The
following scenarios demonstrate several ways that you can define your test workflows.

###### Note

The `parallelGroup` and `onFailure` settings apply only to test
workflows. Image Builder rejects them on a build or distribution workflow with an
`InvalidParameterCombinationException`.

###### How test groups run

Image Builder runs your test workflows in test groups. It runs the groups one at a time. The
test workflows within a single group run at the same time (in parallel). Image Builder runs up to
five test workflows at the same time; if a group has more than five, Image Builder starts the next
test workflow as each one finishes. A test workflow that isn't part of a group runs on its
own.

How you define test groups depends on whether you use the console or the AWS CLI and API.
Select the tab that matches the method you use.

AWS Management Console
When you create or edit a pipeline in the console, you define your test workflows in
the **Test workflow** section of the image creation process. To run
tests, choose the option to select test workflows. To build images without testing,
choose the option to skip test workflows.

The console organizes test workflows into test groups. A new pipeline starts with one
test group. To build your test configuration, do the following:

- **Add a test workflow to a group** – Add a
  test workflow to a group and select the workflow from your own workflows
  (**Owned by me**) or the AWS managed workflows
  (**Managed by Amazon**). If the workflow defines parameters, the
  console shows them so that you can enter values. A group can hold up to five test
  workflows, which run at the same time.
- **Add a test group** – Add another test
  group to run a different set of tests. You can add up to ten test groups. To
  rename a group, choose **Edit name**. A group name can have up to
  128 characters, and can include letters, numbers, hyphens (`-`), and
  underscores (`_`).

Image Builder runs the test groups one at a time, in the order that they appear in the wizard.
The test workflows within a group run at the same time. A group can contain up to five
test workflows. To run your tests one at a time, put each test workflow in its own
group.

###### Note

You can add or remove test workflows and groups, but you cannot reorder them. Plan
the order of your test groups before you create them.

AWS CLI
When you use the AWS CLI or the Image Builder API, you don't define test groups directly.
Instead, you set the `parallelGroup` attribute on each test workflow in the
`workflows` list. Test workflows that have the same
`parallelGroup` value form one group and run at the same time. A test
workflow that has no `parallelGroup` value runs on its own. If you don't set
a `parallelGroup` value on any of your test workflows, Image Builder runs them one at
a time.

The AWS CLI and API don't limit the number of test workflows in a group. The only
limit is the total number of workflows, which can't exceed ten (including your build
and distribution workflows). The console limits a group to five test workflows.

Image Builder always runs build workflows first, then test workflows, then the distribution
workflow. This order applies regardless of how you list them.

Within the test stage, Image Builder orders your test workflows as follows:

- It orders the groups by the position where each group first appears in your
  `workflows` list. It does not order them by the
  `parallelGroup` value.
- It keeps each workflow that has no group in its listed position.
- It runs the workflows in a group together, at the position where that group
  first appears.

**Example**

Suppose you list five test workflows in this order, and set the
`parallelGroup` value on some of them:

- Test workflow A – no group
- Test workflow B – `parallelGroup`: `tests-1`
- Test workflow C – no group
- Test workflow D – `parallelGroup`: `tests-1`
- Test workflow E – `parallelGroup`: `tests-2`

Image Builder runs them in the following order:

1. Test workflow A, on its own.
2. Test workflow B and test workflow D, at the same time. They share the
   `tests-1` group, which first appears at test workflow B.
3. Test workflow C, on its own.
4. Test workflow E, on its own, in the `tests-2` group.

Test workflow D runs together with test workflow B because they share a group,
even though you listed test workflow C between them. The group named
`tests-1` runs before `tests-2` because `tests-1`
appears first in the list – the group order follows the order in the list, not
the `parallelGroup` value.

###### Scenario 1: Run one test workflow at a time

To run all of your test workflows one at a time, configure a separate test group for each
test workflow, up to the combined limit of ten workflows total (which includes your build
and distribution workflows). Image Builder runs the test groups one at a time. This is one way to
ensure that your test workflows run one at a time in a specific order.

###### Scenario 2: Run multiple test workflows at the same time

If the order doesn't matter, and you want to run as many test workflows as possible
at the same time, you can configure a single test group and put the maximum number of
test workflows in it. Image Builder starts up to five test workflows at the same time, and starts
additional test workflows as others complete. If your goal is to run your test workflows
as fast as possible, this is one way to do it.

###### Scenario 3: Mix and match

If you have a mixed scenario, with some test workflows that can run at the same time
and some that should run one at a time, you can configure your test groups to accomplish
this goal. The only limit to how you configure your test groups is the maximum number of
test workflows that can run for your pipeline

## Set workflow parameters in an Image Builder pipeline from the console

Workflow parameters function the same way for build, test, and distribution workflows.
When you create or update a pipeline, you select the build, test, and distribution workflows
that you want to include. If you defined parameters in the workflow document for a workflow
that you selected, Image Builder displays them in the **Parameters** panel. The panel
is hidden for workflows that do not have parameters defined.

Each parameter displays the following attributes that your workflow document defined:

- **Name** (_not editable_) –
  The name of the parameter.
- **Type** (_not editable_) –
  The data type for the parameter value.
- **Value** – The value for the parameter. You
  can edit the parameter value to set it for your pipeline.

## Specify the IAM service role that Image Builder uses to run workflow actions

When you attach custom image workflows to your pipeline, or when you set a logging
configuration, you must also specify an execution role. This is the IAM role that Image Builder
assumes to run your workflow actions. The role must trust the Image Builder service principal. For
the required permissions, see the workflow service access information that follows.

To run image workflows, Image Builder needs permission to perform
workflow actions. You grant this permission with an execution role that Image Builder assumes on your
behalf. You assign the execution role as follows.

###### Important

We recommend that you don't pass the
[AWSServiceRoleForImageBuilder](security-iam-awsmanpol.md#sec-iam-manpol-AWSServiceRoleForImageBuilder "security-iam-awsmanpol.md#sec-iam-manpol-AWSServiceRoleForImageBuilder") service-linked
role as your execution role. Instead, create a custom IAM role and
attach the [EC2ImageBuilderExecutionPolicy](security-iam-awsmanpol.md#sec-iam-manpol-EC2ImageBuilderExecutionPolicy "security-iam-awsmanpol.md#sec-iam-manpol-EC2ImageBuilderExecutionPolicy") AWS managed
policy. This policy grants the same permissions that Image Builder needs to call
AWS services on your behalf. Using a custom role gives you full control
over the permissions that Image Builder uses. It also keeps your service control
policies (SCPs) and resource control policies (RCPs) in effect for
operations that Image Builder performs on your behalf.

- **Console** – In the pipeline wizard
  **Step 3 Define image creation process**, select your custom role
  from the **IAM role** list in the **Service access**
  panel.
- **Image Builder API** – In the [CreateImage](../APIReference/API_CreateImage.md "../APIReference/API_CreateImage.md") action request,
  specify your custom role as the value for the
  `executionRole` parameter.

To create a custom execution role, see
[Creating a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_AWS Identity and Access Management User Guide_.

## Associate workflows with a pipeline

To associate custom build, test, and distribution image workflows with your pipeline, select the
tab that matches the method you want to use.

AWS Management Console
When you create or update a pipeline in the AWS Management Console, the
**Create image pipeline** wizard includes a
**Workflows** step where you select the workflows that your pipeline
runs. To associate custom image workflows, do the following in that step:

1. For **Build workflow**, select the build workflow that you
   want your pipeline to run.
2. For **Test workflows**, add one or more test workflows and
   organize them into test groups to control the order in which they run. For more
   information, see [Define test groups for test workflows](#pipeline-workflows-test-groups "#pipeline-workflows-test-groups").
3. For **Distribution workflow**, select a distribution workflow
   if you want to override the attached distribution configuration or gain more
   visibility into the distribution process. This is optional.
4. For **Execution role**, select the IAM role that Image Builder
   assumes to run your workflow actions. An execution role is required when you
   associate custom image workflows. For more information, see
   [Specify the IAM service role that Image Builder uses to run workflow actions](#pipeline-workflow-service-role "#pipeline-workflow-service-role").
5. If a workflow that you selected defines parameters, set their values in the
   **Parameters** panel. For more information, see
   [Set workflow parameters in an Image Builder pipeline from the console](#pipeline-workflow-set-params "#pipeline-workflow-set-params").

For a step-by-step walkthrough of the full
**Create image pipeline** wizard, see
[Create and update AMI image pipelines](ami-image-pipelines.md "ami-image-pipelines.md").

AWS CLI
To associate custom image workflows when you create a pipeline, use the
**[create-image-pipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image-pipeline.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image-pipeline.html")** command. Specify your execution role with
the `--execution-role` parameter, and list your build, test, and
distribution workflows with the `--workflows` parameter. The following
example creates a pipeline with one build workflow, one test workflow, and one
distribution workflow.

```
`aws imagebuilder create-image-pipeline \
 --name `example-pipeline` \
 --image-recipe-arn arn:aws:imagebuilder:`us-west-2`:`111122223333`:image-recipe/`example`/`1.0.0` \
 --infrastructure-configuration-arn arn:aws:imagebuilder:`us-west-2`:`111122223333`:infrastructure-configuration/`example` \
 --execution-role arn:aws:iam::`111122223333`:role/`ImageBuilderWorkflowExecutionRole` \
 --workflows '[
 {"workflowArn":"arn:aws:imagebuilder:`us-west-2`:`111122223333`:workflow/build/`example-build`/`1.0.0`"},
 {"workflowArn":"arn:aws:imagebuilder:`us-west-2`:`111122223333`:workflow/test/`example-test`/`1.0.0`","parallelGroup":"`group-1`","onFailure":"CONTINUE"},
 {"workflowArn":"arn:aws:imagebuilder:`us-west-2`:`111122223333`:workflow/distribution/`example-distribute`/`1.0.0`"}
 ]'`
```
