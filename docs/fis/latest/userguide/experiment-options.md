# Experiment options for AWS FIS

Experiment options are optional settings for an experiment. You can define certain experiment options on the experiment template. Additional experiment options are set when you begin the experiment.

The following is the syntax for experiment options that you define on the experiment template.

```
{
        "experimentOptions": {
        "accountTargeting": "single-account | multi-account",
            "emptyTargetResolutionMode": "fail | skip"
    }
}
```

If you do not specify any experiment options when you create the experiment template, the default for each option is used.

The following is the syntax for experiment options that you set when you begin the experiment.

```
{
        "experimentOptions": {
            "actionsMode": "run-all | skip-all"
     }
}
```

If you do not specify any experiment options when you begin the experiment, the default `run-all` is used.

###### Contents

- [Account targeting](#account-targeting "#account-targeting")
- [Empty target resolution mode](#empty-target-resolution-mode "#empty-target-resolution-mode")
- [Actions mode](#actions-mode "#actions-mode")

## Account targeting

If you have multiple AWS accounts with resources that you want to target in an experiment, you can define
a multi-account experiment using the account targeting experiment option. You run multi-account experiments from
an orchestrator account that impacts resources in multiple target accounts. The orchestrator account owns the AWS FIS experiment
template and experiment. A target account is an individual AWS account with resources that can be affected by an AWS FIS experiment.
For more information, see [Working with multi-account experiments for AWS FIS](multi-account.md "multi-account.md").

You use account targeting to indicate the location of your target resources. You can provide two values for account targeting:

- single-account – Default. The experiment will only target resources in the AWS account where AWS FIS experiment runs.
- multi-account – The experiment can target resources in multiple AWS accounts.

### Target account configurations

To run a multi-account experiment, you must define one or more target account configurations.
A target account configuration specifies the accountId, roleArn, and description for each account with resources targeted in the experiment. The account IDs of the target account configurations for an experiment template must be unique.

When you create a multi-account experiment template, the experiment template will return a read-only field, `targetAccountConfigurationsCount`, that is a count of all the target account configurations for the experiment template.

The following is the syntax for a target account configuration.

```
{
    accountId: "123456789012",
    roleArn: "arn:aws:iam::123456789012:role/AllowFISActions",
    description: "fis-ec2-test"
}
```

When you create a target account configuration, you provide the following:

**accountId**

12-digit AWS account ID of the target account.

**roleArn**

An IAM Role granting AWS FIS permissions to take actions in target account.

**description**

An optional description.

To learn more about how to work with target account configurations, see [Working with multi-account experiments for AWS FIS](multi-account.md "multi-account.md").

## Empty target resolution mode

This mode gives you the option to allow experiments to complete even when a target resource is not
resolved.

- fail – Default. If no resources are resolved for the target, the experiment is terminated immediately with a status of `failed`.
- skip – If no resources are resolved for the target, the experiment will continue and any actions with no resolved targets are skipped.
  Actions with targets that are defined using unique identifiers, such as ARNs, cannot be skipped. If a target defined using a unique identifier is not found the experiment is terminated immediately with a status of `failed`

##

Actions mode

Actions mode is an optional parameter that you can specify when you start an experiment. You can set actions mode to `skip-all` to generate a target preview
before injecting faults into your target resources. The target preview allows you to verify the following:

- That you have configured your experiment template to target the resources you expect. The actual resources that are targeted when you start this experiment may be different from the preview because resources may be removed, updated, or sampled randomly.
- That your logging configurations are set up correctly.
- That for multi-account experiments you have correctly set up an IAM role for each of your target account configurations.

###### Note

The `skip-all` mode does not allow you to verify that you have the necessary permissions to run the AWS FIS experiment and take actions on your resources.

The actions mode parameter accepts the following values:

- `run-all` - (Default) The experiment will take actions on target resources.
- `skip-all` - The experiment will skip all actions on target resources.

To learn more about how to set the actions mode parameter when you start an experiment, see [Generate a target preview from an experiment template](generate-target-preview.md "generate-target-preview.md").
