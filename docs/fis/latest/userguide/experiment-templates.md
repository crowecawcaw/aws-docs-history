# AWS FIS experiment template components

You use the following components to construct experiment templates:

**Actions**

The [AWS FIS actions](fis-actions-reference.md "fis-actions-reference.md") that you want to run.
Actions can be run in a set order that you specify, or they can be run
simultaneously. For more information, see [Actions](action-sequence.md "action-sequence.md").

**Targets**

The AWS resources on which a specific action is carried out.
For more information, see [Targets](targets.md "targets.md").

**Stop conditions**

The CloudWatch alarms that define a threshold at which your application
performance is not acceptable. If a stop condition is triggered while
an experiment is running, AWS FIS stops the experiment. For more
information, see [Stop conditions](stop-conditions.md "stop-conditions.md").

**Experiment role**

An IAM role that grants AWS FIS the permissions required so that
it can run experiments on your behalf. For more information, see
[Experiment role](getting-started-iam-service-role.md "getting-started-iam-service-role.md").

**Experiment report configuration**

The configuration to enable experiment reports. For more information, see [Experiment report configurations for AWS FIS](experiment-report-configuration.md "experiment-report-configuration.md").

**Experiment options**

Options for the experiment template. For more
information, see [Experiment options for AWS FIS](experiment-options.md "experiment-options.md").

Your account has quotas related to AWS FIS. For example, there is a quota on the
number of actions per experiment template. For more information, see [Quotas and limitations](fis-quotas.md "fis-quotas.md").

## Template syntax

The following is the syntax for an experiment template.

```
{
            "description": "`string`",
            "targets": {},
            "actions": {},
            "stopConditions": [],
            "roleArn": "arn:aws:iam::`123456789012`:role/`AllowFISActions`",
            "experimentReportConfiguration":{},
            "experimentOptions":{},
            "tags": {}
        }
```

For examples, see [Example templates](experiment-template-example.md "experiment-template-example.md").

## Get started

To create an experiment template using the AWS Management Console, see [Create an experiment template](create-template.md "create-template.md").

To create an experiment template using the AWS CLI, see [Example AWS FIS experiment templates](experiment-template-example.md "experiment-template-example.md").
