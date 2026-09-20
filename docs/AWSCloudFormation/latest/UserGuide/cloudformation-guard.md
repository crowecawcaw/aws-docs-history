

# Validate templates with Guard
<a name="cloudformation-guard"></a>

AWS CloudFormation Guard (`cfn-guard`) is a policy-as-code tool. You write rules that describe required or prohibited configurations, and then check JSON or YAML data against those rules. For example, you can require every Amazon S3 bucket in a template to use encryption.

For the limitations of local validation and steps to take before deployment, see [Understand validation scope](template-guide.md#template-validation-scope).

**Topics**
+ [Install Guard](#cloudformation-guard-install)
+ [Write a rule](#cloudformation-guard-write-rule)
+ [Validate a template](#cloudformation-guard-validate)
+ [Add Guard to your workflow](#cloudformation-guard-integrate)
+ [Learn more](#cloudformation-guard-learn-more)

## Install Guard
<a name="cloudformation-guard-install"></a>

On macOS, install Guard with Homebrew:

```
brew install cloudformation-guard
```

For Linux, Windows, other macOS installation methods, and release verification, see [Setting up AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/setting-up.html).

## Write a rule
<a name="cloudformation-guard-write-rule"></a>

Save rules in a file with the `.guard` extension. The following example requires every Amazon S3 bucket in a template to specify bucket encryption:

```
let s3_buckets = Resources.*[ Type == 'AWS::S3::Bucket' ]

rule S3_BUCKET_ENCRYPTED when %s3_buckets !empty {
  %s3_buckets {
    Properties.BucketEncryption exists
  }
}
```

For rule syntax and more examples, see [Writing AWS CloudFormation Guard rules](https://docs.aws.amazon.com/cfn-guard/latest/ug/writing-rules.html).

## Validate a template
<a name="cloudformation-guard-validate"></a>

Pass the rule file to `--rules` and the template to `--data`:

```
cfn-guard validate --rules rules.guard --data template.yaml
```

The command returns exit status `0` when the template passes. If a rule fails, the output identifies the failed rule. You can also pass directories to `--rules` and `--data` to check multiple files.

Before using a rule in an automated workflow, test it with the built-in unit testing support. For instructions, see [Testing AWS CloudFormation Guard rules](https://docs.aws.amazon.com/cfn-guard/latest/ug/testing-rules.html).

## Add Guard to your workflow
<a name="cloudformation-guard-integrate"></a>

You can run Guard locally, in an automated build, or before a Git commit. The CloudFormation Language Server can also run Guard rule packs while you edit a template. For setup, see [CloudFormation Language Server](ide-extension.md).

To enforce rules during CloudFormation and Cloud Control API operations, use Guard Hooks. For more information, see [Guard Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks.html).

## Learn more
<a name="cloudformation-guard-learn-more"></a>

For the complete language and command reference, see the [AWS CloudFormation Guard User Guide](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html). Source code and release information are available in the [AWS CloudFormation Guard repository on GitHub](https://github.com/aws-cloudformation/cloudformation-guard).