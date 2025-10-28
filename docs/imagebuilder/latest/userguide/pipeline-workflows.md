# Configure image pipeline workflows in Image Builder

With image workflows, you can customize the workflows that your pipeline runs to build
and test images according to your needs. The workflows that you define run within the
context of the Image Builder workflow framework. For more information about the stages that
make up the workflow framework, see [Manage build and test workflows for Image Builder images](manage-image-workflows.md "manage-image-workflows.md").

Build workflow

Build workflows run during the `Build` stage of the
workflow framework. You can specify only one build workflow for
your pipeline. Or you can skip the build entirely to configure a
test-only pipeline.

Test workflow

Test workflows run during the `Test` stage of the
workflow framework. You can specify up to ten test workflows for
your pipeline. You can also skip tests entirely if you only want
your pipeline to build.

## Define test groups for test workflows

Test workflows are defined within test groups. You can run up to ten test workflows for your
pipeline. You decide whether to run the test workflows in a specific order or to run as many
as possible at the same time. How they run depends on how you define your test groups. The
following scenarios demonstrate several ways that you can define your test workflows.

###### Note

If you use the console to create workflows, we recommend that you take time to plan how
you want to run your test workflows before you define your test groups. In the console, you
can add or remove test workflows and groups, but you can’t reorder them.

###### Scenario 1: Run one test workflow at a time

To run all of your test workflows one at a time, you can configure up to ten test groups,
each with a single test workflow in it. Test groups run one at a time, in the order that you
add them to your pipeline. This is one way to ensure that your test workflows run one at
a time in a specific order.

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

## Set workflow parameters in an Image Builder

pipeline from the console

Workflow parameters function the same way for build workflows and test workflows.
When you create or update a pipeline, you select build and test workflows that you want
to include. If you defined parameters in the workflow document for a workflow that you
selected, Image Builder displays them in the **Parameters** panel. The panel is
hidden for workflows that don't have parameters defined.

Each parameter displays the following attributes that your workflow document defined:

- **Name** (_not editable_) –
  The name of the parameter.
- **Type** (_not editable_) –
  The data type for the parameter value.
- **Value** – The value for the parameter. You
  can edit the parameter value to set it for your pipeline.

## Specify the IAM service role that Image Builder uses to run workflow actions

To run image workflows, Image Builder needs permission to perform
workflow actions. You can specify the [AWSServiceRoleForImageBuilder](security-iam-awsmanpol.md#sec-iam-manpol-AWSServiceRoleForImageBuilder "security-iam-awsmanpol.md#sec-iam-manpol-AWSServiceRoleForImageBuilder") service-linked role, or
you can specify your own custom role for service access, as follows.

- **Console** – In the pipeline wizard
  **Step 3 Define image creation process**, select the
  service-linked role or your own custom role from the **IAM role**
  list in the **Service access** panel.
- **Image Builder API** – In the [CreateImage](../APIReference/API_CreateImage.md "../APIReference/API_CreateImage.md") action request,
  specify the service-linked role or your own custom role as the value for the
  `executionRole` parameter.

To learn more about how to create a service role, see
[Creating a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_AWS Identity and Access Management User Guide_.
