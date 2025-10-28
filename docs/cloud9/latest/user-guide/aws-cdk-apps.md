AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Working with AWS CDK applications

Use the **AWS CDK Explorer** in the AWS Cloud9 integrated development environment (IDE) to visualize
and work with AWS CDK applications.

## Prerequisites

Install the AWS CDK command line interface. For instructions, see [Getting Started with the AWS CDK](../../../cdk/latest/guide/getting_started.md "../../../cdk/latest/guide/getting_started.md") in
the _AWS Cloud Development Kit (AWS CDK) Developer Guide_.

###### Important

The AWS CDK version that you install must be 1.17.0 or later. You can check
which version you're running using **`cdk
 --version`** command.

## Visualize an AWS CDK application

Using the AWS Cloud9 IDE AWS CDK Explorer, you can manage the [stacks](../../../cdk/latest/guide/stacks.md "../../../cdk/latest/guide/stacks.md") and [resources](../../../cdk/latest/guide/resources.md "../../../cdk/latest/guide/resources.md") that are stored in the CDK
constructs of your apps. The AWS CDK Explorer displays your resources in a tree view using
the information that's defined in the `tree.json` file. This file is
created when you run the **`cdk synth`**
command. By default, the `tree.json` file is located in an app's
`cdk.out` directory.

To get started using the Toolkit AWS CDK Explorer, create a CDK application.

1. Complete the first several steps of the [Hello World
   Tutorial](../../../cdk/latest/guide/getting_started.md#hello_world_tutorial "../../../cdk/latest/guide/getting_started.md#hello_world_tutorial") lin the [AWS CDK Developer
   Guide](../../../cdk/v2/guide/getting_started.md "../../../cdk/v2/guide/getting_started.md").

###### Important

When you reach the **Deploying the Stack** step, stop and return
to this guide.

###### Note

You can run the commands that are provided in the tutorial, such as **`mkdir`** and **`cdk
 init`**, on an operating system command line
interface or in a **Terminal** window inside the VS Code
editor. 2. After you complete the required steps of the CDK tutorial, open the CDK content that you created in the AWS Cloud9 IDE editor. 3. In the AWS navigation pane, expand the **CDK** heading. Your CDK
applications and their associated resources are now displayed in the CDK
Explorer tree view. You can also run the following commands in a terminal within
AWS Cloud9 to confirm that the CDK feature is working:

```
mkdir mycdkapp
cd mycdkapp
cdk init app --language=typescript
cdk synth
cdk bootstrap
```

### Important notes

- When you load CDK apps into the AWS Cloud9 editor, you can load multiple
  folders at once. Each folder can contain multiple CDK apps, as shown
  in the preceding image. The AWS CDK Explorer finds apps in the project root
  directory and its direct subdirectories.

- When you perform the first several steps of the tutorial, you might notice
  that the last command that you ran is **`cdk
synth`**. This command synthesizes the CloudFormation
  template by translating your AWS CDK app to CFN. As a by-product, it also
  generates the `tree.json` file. If you make changes to a
  CDK app, run the **`cdk
synth`** command again to see the changes reflected in
  the tree view. One example change is adding more resource to the app.

## Perform other operations on an AWS CDK app

You can use the AWS Cloud9 editor to perform other operations on a CDK app in the
same way that you use a command line interface. For example, you can update the code
files in the editor and deploy the app by using an AWS Cloud9 **Terminal**
window.

To try out these types of actions, use the AWS Cloud9 editor to continue the [Hello World
Tutorial](../../../cdk/latest/guide/getting_started.md#hello_world_tutorial "../../../cdk/latest/guide/getting_started.md#hello_world_tutorial") in the _AWS CDK Developer Guide_. Make sure that
you perform the last step, **Destroying the App's
Resources**. Otherwise, you might incur unexpected costs to your
AWS account.
