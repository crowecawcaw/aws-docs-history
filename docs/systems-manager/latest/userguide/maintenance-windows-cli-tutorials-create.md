AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Tutorial: Create and

configure a maintenance window using the AWS CLI

This tutorial demonstrates how to use the AWS Command Line Interface (AWS CLI) to create and
configure a maintenance window, its targets, and its tasks. The main path
through the tutorial consists of simple steps. You create a single maintenance
window, identify a single target, and set up a simple task for the maintenance
window to run. Along the way, we provide information you can use to try more
complicated scenarios.

As you follow the steps in this tutorial, replace the values in italicized
`red` text with your own options and IDs. For example, replace
the maintenance window ID `mw-0c50858d01EXAMPLE` and the instance ID
`i-02573cafcfEXAMPLE` with IDs of resources you create.

###### Contents

- [Step 1: Create the maintenance
  window using the AWS CLI](mw-cli-tutorial-create-mw.md "mw-cli-tutorial-create-mw.md")
- [Step 2: Register a target node
  with the maintenance window using the AWS CLI](mw-cli-tutorial-targets.md "mw-cli-tutorial-targets.md")
- [Step 3: Register a task with the
  maintenance window using the AWS CLI](mw-cli-tutorial-tasks.md "mw-cli-tutorial-tasks.md")
