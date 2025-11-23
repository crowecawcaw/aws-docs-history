# Create templates visually with Infrastructure Composer

AWS Infrastructure Composer (formerly known as **Application Composer**) helps you visually
compose and configure modern applications on AWS. Instead of writing code, you can drag and
drop different resources to build your application visually.

_Infrastructure Composer in CloudFormation console mode_ is the recommended tool
to work with CloudFormation templates visually. This version of Infrastructure Composer that you can access from the
CloudFormation console is an improvement from an older tool called CloudFormation Designer.

With Infrastructure Composer in CloudFormation console mode, you can drag, drop, configure, and connect a variety
of resources, called _cards_, onto a visual canvas. This visual approach
makes it easy to design and edit your application architecture without having to work with
templates directly. To access this mode from the [CloudFormation console](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/"), select
**Infrastructure Composer** from the left-side navigation menu.

For more information, see [How to compose in
AWS Infrastructure Composer](../../../infrastructure-composer/latest/dg/using-composer-basics.md "../../../infrastructure-composer/latest/dg/using-composer-basics.md") in the _AWS Infrastructure Composer Developer Guide_.

## Why use Infrastructure Composer in CloudFormation console

mode?

Visualizing your templates in Infrastructure Composer helps you identify gaps and areas of improvement in
your CloudFormation templates and application architecture. Infrastructure Composer improves your development
experience with the ease and efficiency of visually building and modifying CloudFormation stacks.
You can start with an initial draft, create deployable code, and incorporate your developer
workflows with the visual designer in Infrastructure Composer.

## How is this mode different than

the Infrastructure Composer console?

While the CloudFormation console version of Infrastructure Composer has similar features to the standard Infrastructure Composer
console, there are a few differences. Lambda-related cards (**Lambda
Function** and **Lambda Layer**) require code builds and packaging
solutions that are not available in Infrastructure Composer in CloudFormation console mode. Local sync is also not
available in this mode.

However, you can use these Lambda-related cards and the local sync feature in the [Infrastructure Composer console](https://console.aws.amazon.com/composer/home "https://console.aws.amazon.com/composer/home") or the AWS Toolkit for Visual Studio Code. For more
information, see the [AWS Infrastructure Composer Developer Guide](../../../infrastructure-composer/latest/dg/what-is-composer.md "../../../infrastructure-composer/latest/dg/what-is-composer.md")
and [Infrastructure Composer](../../../toolkit-for-vscode/latest/userguide/appcomposer.md "../../../toolkit-for-vscode/latest/userguide/appcomposer.md") in the _AWS Toolkit for Visual Studio Code User Guide_.
