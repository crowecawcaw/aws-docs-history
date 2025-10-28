# Using Infrastructure Composer in CloudFormation console mode

Infrastructure Composer in CloudFormation console mode is the recommended tool to visualize your AWS CloudFormation templates.
You can also use this tool to create and edit AWS CloudFormation templates.

## How is this mode different than the Infrastructure Composer console?

Infrastructure Composer in CloudFormation console mode generally has the same functionality as the [default Infrastructure Composer console](using-composer-console.md "using-composer-console.md"), but there are a few differences to note.

- This mode is integrated with the stack workflow in the AWS CloudFormation console. This allows you to use Infrastructure Composer directly in AWS CloudFormation.
- [Locally sync and save your
  project in the Infrastructure Composer console](using-composer-project-local-sync.md "using-composer-project-local-sync.md"), a feature that automatically syncs and saves data to your local machine, is not supported.
- Lambda-related cards (**Lambda Function** and **Lambda Layer**) require code builds and packaging solutions that are not available in this mode.

###### Note

These cards and local sync can be used in the [Infrastructure Composer Console](https://aws.amazon.com/application-composer/ "https://aws.amazon.com/application-composer/") or the AWS Toolkit for Visual Studio Code.

When you open Infrastructure Composer from the AWS CloudFormation console, Infrastructure Composer opens in CloudFormation console mode. In this mode, you can use Infrastructure Composer to visualize, create, and update your templates.
