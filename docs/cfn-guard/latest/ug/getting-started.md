# Prerequisites and overview for using Guard rules

This section demonstrates how you can complete the core Guard tasks of writing,
testing, and validating rules against JSON- or YAML-formatted data. In addition, it
contains detailed walkthroughs that demonstrate writing rules that respond to specific use
cases.

###### Topics

- [Prerequisites](#getting-started-prerequisites "#getting-started-prerequisites")
- [Overview of using Guard rules](#getting-started-overview "#getting-started-overview")
- [Writing AWS CloudFormation Guard rules](writing-rules.md "writing-rules.md")
- [Testing AWS CloudFormation Guard rules](testing-rules.md "testing-rules.md")
- [Using input parameters with AWS CloudFormation Guard
  rules](using-input-parameters.md "using-input-parameters.md")
- [Validating input data against AWS CloudFormation Guard rules](validating-rules.md "validating-rules.md")

## Prerequisites

Before you can write policy rules using the Guard domain-specific language (DSL),
you must install the Guard command line interface (CLI). For more information, see [Setting up Guard](setting-up.md "setting-up.md").

## Overview of using Guard rules

When using Guard, you typically perform the following steps:

1. Write JSON- or YAML-formatted data to validate.
2. Write Guard policy rules. For more information, see [Writing Guard rules](writing-rules.md "writing-rules.md").
3. Verify that your rules work as intended by using the Guard `test`
   command. For more information about unit testing, see [Testing Guard rules](testing-rules.md "testing-rules.md").
4. Use the Guard `validate` command to validate your JSON- or YAML-formatted
   data against your rules. For more information, see [Validating input data against Guard rules](validating-rules.md "validating-rules.md").
