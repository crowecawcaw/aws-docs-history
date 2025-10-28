# AWS Config sample with CodeBuild

AWS Config provides an inventory of your AWS resources and a history of configuration changes
to these resources. AWS Config now supports AWS CodeBuild as an AWS resource, which means the
service can track your CodeBuild projects. For more information about AWS Config, see [What is AWS Config?](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md") in the _AWS Config
Developer Guide_.

You can see the following information about CodeBuild resources on the **Resource
Inventory** page in the AWS Config console:

- A timeline of your CodeBuild configuration changes.
- Configuration details for each CodeBuild project.
- Relationships with other AWS resources.
- A list of changes to your CodeBuild projects.

###### Topics

- [Use CodeBuild with AWS Config](#how-to-integrate-config-run "#how-to-integrate-config-run")
- [Step 3: View AWS CodeBuild data in the AWS Config console](#viewing-config-details "#viewing-config-details")

## Use CodeBuild with AWS Config

The procedures in this topic show you how to set up AWS Config and look up CodeBuild
projects.

###### Topics

- [Prerequisites](#how-to-create-a-build-project "#how-to-create-a-build-project")
- [Step 1: Set up AWS Config](#setup-config "#setup-config")
- [Step 2: Look up AWS CodeBuild projects](#lookup-projects "#lookup-projects")

### Prerequisites

Create your AWS CodeBuild project. For instructions, see [Create a build project](create-project.md "create-project.md").

### Step 1: Set up AWS Config

- [Setting up AWS Config
  (console)](../../../config/latest/developerguide/gs-console.md "../../../config/latest/developerguide/gs-console.md")
- [Setting up AWS Config
  (AWS CLI)](../../../config/latest/developerguide/gs-cli.md "../../../config/latest/developerguide/gs-cli.md")

###### Note

After you complete setup, it might take up to 10 minutes before you can see
AWS CodeBuild projects in the AWS Config console.

### Step 2: Look up AWS CodeBuild projects

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config](https://console.aws.amazon.com/config "https://console.aws.amazon.com/config").
2. On the **Resource inventory** page, select
   **AWS CodeBuild Project** under **Resource
   type**. Scroll down and select the **CodeBuild
   project** check box.
3. Choose **Look up**.
4. After the list of CodeBuild projects is added, choose the CodeBuild project name
   link in the **Config timeline** column.

## Step 3: View AWS CodeBuild data in the AWS Config console

When you look up resources on the **Resource inventory** page,
you can choose the AWS Config timeline to view details about your CodeBuild project. The
details page for a resource provides information about the configuration,
relationships, and number of changes made to that resource.

The blocks at the top of the page are collectively called the timeline. The
timeline shows the date and time that the recording was made.

For more information, see [Viewing configuration
details in the AWS Config console](../../../config/latest/developerguide/view-manage-resource-console.md "../../../config/latest/developerguide/view-manage-resource-console.md") in the _AWS Config Developer
Guide_.
