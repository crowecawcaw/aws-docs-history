

# Validate templates with `cfn-lint`
<a name="cfn-lint"></a>

The CloudFormation Linter (`cfn-lint`) checks JSON and YAML templates against the [CloudFormation resource provider schemas](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/resource-type-schemas.html) and additional rules. It can find invalid resource properties, unsupported values, and common problems before you send a template to CloudFormation.

Source code, release notes, settings, and the complete rule list are available in the [cfn-lint repository on GitHub](https://github.com/aws-cloudformation/cfn-lint).

**Topics**
+ [Install `cfn-lint`](#cfn-lint-install)
+ [Run `cfn-lint`](#cfn-lint-run)
+ [Configure checks](#cfn-lint-configure)
+ [Add `cfn-lint` to your workflow](#cfn-lint-integrate)

## Install `cfn-lint`
<a name="cfn-lint-install"></a>

Install `cfn-lint` from Python Package Index (PyPI):

```
python3 -m pip install cfn-lint
```

On macOS, you can instead install it with Homebrew:

```
brew install cfn-lint
```

For supported Python versions and other installation methods, see the [installation instructions](https://github.com/aws-cloudformation/cfn-lint#install) on GitHub.

## Run `cfn-lint`
<a name="cfn-lint-run"></a>

Pass one or more template paths to the command:

```
cfn-lint template.yaml
cfn-lint template-one.yaml template-two.json
```

To check templates for more than one AWS Region, use the `--regions` option:

```
cfn-lint --regions us-east-1 us-west-2 -- template.yaml
```

The command returns a nonzero exit code when it finds issues. You can use this behavior to stop an automated build when a template doesn't pass your selected checks.

## Configure checks
<a name="cfn-lint-configure"></a>

Use a `.cfnlintrc`, `.cfnlintrc.yaml`, or `.cfnlintrc.yml` file to keep project settings with your templates. You can use this file to select templates, include or ignore checks, choose AWS Regions, and configure rule behavior. For all settings, see [Config file](https://github.com/aws-cloudformation/cfn-lint#config-file) in the project documentation on GitHub.

## Add `cfn-lint` to your workflow
<a name="cfn-lint-integrate"></a>

You can run `cfn-lint` from supported editors, automatically before a Git commit, or as part of an automated build. The CloudFormation Language Server also uses `cfn-lint` to show problems while you type. For Language Server setup, see [CloudFormation Language Server](ide-extension.md).

For editor plugins, GitHub Actions, pre-commit configuration, custom rules, and more examples, see the [cfn-lint project documentation](https://github.com/aws-cloudformation/cfn-lint) on GitHub.