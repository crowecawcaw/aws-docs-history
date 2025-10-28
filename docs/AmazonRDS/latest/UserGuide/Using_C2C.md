# Use Console-to-Code to generate code for your Amazon RDS console actions

The console provides a guided path for creating resources and testing prototypes. If
you want to create the same resources at scale, you'll need automation code. Console-to-Code is a
feature of Amazon Q Developer that can help you get started with your automation code. Console-to-Code
records your console actions, including default values and parameters values that you
provide. It then uses generative AI to suggest code in your preferred language and
format for the actions that you choose. Because the console workflow makes sure the
parameter values that you specify are valid together, the code that you generate by
using Console-to-Code has compatible parameter values. You can use the code as a starting point,
and then customize it to make it production-ready for your specific use case.

For example, with Console-to-Code, you can record creating an RDS
DB instance and choose
to generate code in AWS CloudFormation JSON format. Then, you can copy that code and customize it
for use in your AWS CloudFormation template.

Console-to-Code can currently generate infrastructure-as-code (IaC) in the following languages and formats:

- CDK Java
- CDK Python
- CDK TypeScript
- CloudFormation JSON
- CloudFormation YAML
  For more information and instructions on how to use Console-to-Code, see [Automating AWS services with Amazon Q Developer Console-to-Code](../../../amazonq/latest/qdeveloper-ug/console-to-code.md "../../../amazonq/latest/qdeveloper-ug/console-to-code.md") in the
  _Amazon Q Developer User Guide_.
