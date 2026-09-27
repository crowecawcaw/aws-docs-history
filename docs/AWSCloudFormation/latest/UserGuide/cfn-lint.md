

# Validate templates with `cfn-lint`
<a name="cfn-lint"></a>

AWS CloudFormation Linter (`cfn-lint`) checks JSON and YAML templates against the [CloudFormation resource provider schemas](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/resource-type-schemas.html) and additional rules. It can find invalid resource properties, unsupported property values, broken references, and common best-practice problems. Use it to catch these problems before you send a template to CloudFormation. If a template uses the AWS Serverless Application Model (AWS SAM) transform, `cfn-lint` applies the transform before it checks the template.

For release notes, the complete rule list, and all command options, see [`cfn-lint`](https://github.com/aws-cloudformation/cfn-lint) on GitHub.

For the limitations of local validation and steps to take before deployment, see [Understand validation scope](template-guide.md#template-validation-scope).

**Topics**
+ [Install `cfn-lint`](#cfn-lint-install)
+ [Run `cfn-lint`](#cfn-lint-run)
+ [Understand the results](#cfn-lint-results)
+ [Configure checks](#cfn-lint-configure)
+ [Add custom rules](#cfn-lint-custom-rules)
+ [Add `cfn-lint` to your workflow](#cfn-lint-integrate)

## Install `cfn-lint`
<a name="cfn-lint-install"></a>

Install `cfn-lint` from the Python Package Index (PyPI):

```
python3 -m pip install cfn-lint
```

On macOS, you can instead install it with Homebrew:

```
brew install cfn-lint
```

To confirm the installation, print the installed version:

```
cfn-lint --version
```

For a Docker image and other installation methods, see the [installation instructions](https://github.com/aws-cloudformation/cfn-lint#install) on GitHub.

## Run `cfn-lint`
<a name="cfn-lint-run"></a>

Pass one or more template paths to the command:

```
cfn-lint template.yaml
cfn-lint template-one.yaml template-two.json
```

You can also use wildcards to check every template in a directory. Use `**` to include subdirectories:

```
cfn-lint templates/*.yaml
cfn-lint templates/**/*.yaml
```

**Note**  
In `bash`, run `shopt -s globstar` before you use `**` so that it matches subdirectories. In `zsh`, `**` matches subdirectories by default.

To read a template from standard input, pass `-` as the template path:

```
cat template.yaml | cfn-lint -
```

By default, `cfn-lint` checks templates against the schemas for `us-east-1`. To check templates for other AWS Regions, use the `--regions` option. Because this option accepts multiple values, add `--` before the template path or use `-t` to identify the template:

```
cfn-lint --regions us-east-1 us-west-2 -- template.yaml
cfn-lint --regions us-east-1 us-west-2 -t template.yaml
```

Some checks depend on parameter values. To check a template with specific values, pass them with `--parameters` or provide a parameter file with `--parameter-files`:

```
cfn-lint --parameters InstanceType=t3.micro Environment=prod -- template.yaml
cfn-lint --parameter-files params.json -- template.yaml
```

To list every rule that `cfn-lint` can apply, run the following command:

```
cfn-lint --list-rules
```

## Understand the results
<a name="cfn-lint-results"></a>

For each finding, `cfn-lint` prints the rule ID, a message, and the file, line, and column of the problem. For the complete list of rules and what each one checks, see [cfn-lint rules](https://github.com/aws-cloudformation/cfn-lint/blob/main/docs/rules.md) on GitHub.

To change the output format, use `--format` with `quiet`, `parseable`, `json`, `junit`, `pretty`, or `sarif`:

```
cfn-lint --format json template.yaml
```

`cfn-lint` returns exit code `0` when it finds no issues and a nonzero exit code otherwise. To control which findings cause a nonzero exit code, use `--non-zero-exit-code`. You can use the exit code to stop an automated build when a template doesn't pass your selected checks.

## Configure checks
<a name="cfn-lint-configure"></a>

You can configure `cfn-lint` with command-line options, a configuration file, or metadata in the template. When the same setting appears in more than one place, command-line options override template metadata, and template metadata overrides the configuration file.

### Select and configure rules
<a name="cfn-lint-configure-rules"></a>

To skip rules, use `--ignore-checks` with one or more rule IDs or rule ID prefixes. To run rules that are off by default, use `--include-checks`. To run a rule even when it matches an ignore setting, use `--mandatory-checks`.

```
cfn-lint --ignore-checks {{RULE_ID}} -- template.yaml
```

Some rules accept settings. Use `--configure-rule` with the format `{{RULE_ID}}:{{key}}={{value}}`:

```
cfn-lint --configure-rule {{RULE_ID}}:{{key}}={{value}} -- template.yaml
```

### Use a configuration file
<a name="cfn-lint-configure-file"></a>

To keep settings with your templates, create a `.cfnlintrc`, `.cfnlintrc.yaml`, or `.cfnlintrc.yml` file in the directory where you run `cfn-lint`. You can also create a `~/.cfnlintrc` file in your home directory for settings that apply everywhere. The following example selects the templates to check, skips one template, sets the Regions, and skips a rule:

```
templates:
  - templates/**/*.yaml
ignore_templates:
  - templates/legacy.yaml
regions:
  - us-east-1
  - us-west-2
ignore_checks:
  - {{RULE_ID}}
```

When the configuration file selects templates, you can run `cfn-lint` without arguments to check all of them. For all settings, see [Config file](https://github.com/aws-cloudformation/cfn-lint#config-file) on GitHub.

### Configure checks in the template
<a name="cfn-lint-configure-metadata"></a>

To configure `cfn-lint` for one template, add a `cfn-lint` key to the top-level `Metadata` section:

```
Metadata:
  cfn-lint:
    config:
      regions:
        - us-east-1
        - us-east-2
      ignore_checks:
        - {{RULE_ID}}
```

To skip a rule for a single resource, add the same key to that resource's `Metadata` attribute. The following example skips a rule for one instance only:

```
Resources:
  MyInstance:
    Type: AWS::EC2::Instance
    Metadata:
      cfn-lint:
        config:
          ignore_checks:
            - {{RULE_ID}}
    Properties:
      InstanceType: t3.micro
      ImageId: ami-abc1234
```

## Add custom rules
<a name="cfn-lint-custom-rules"></a>

You can add your own checks without writing Python. A custom rules file contains one rule per line in the following format:

```
{{ResourceType}} {{Property}} {{Operator}} {{Value}} [{{ErrorLevel}}] [{{Message}}]
```

For example, the following rule in `custom_rules.txt` reports a warning when a template uses an expensive instance type:

```
AWS::EC2::Instance InstanceType NOT_EQUALS "m4.16xlarge" WARN "This is an expensive instance type, don't use it"
```

Pass the file with `--custom-rules` (or `-z`), or add a `custom_rules` setting to your configuration file:

```
cfn-lint --custom-rules custom_rules.txt -- template.yaml
```

For the supported operators, see [Custom rules](https://github.com/aws-cloudformation/cfn-lint/blob/main/docs/custom_rules.md) on GitHub. For more complex checks, you can write rules in Python and load them with `--append-rules`. To change what `cfn-lint` considers valid, such as requiring specific tags, you can provide a specification override file with `--override-spec`. For more information, see [Getting started with rules](https://github.com/aws-cloudformation/cfn-lint/blob/main/docs/getting_started/rules.md) and [Customize specifications](https://github.com/aws-cloudformation/cfn-lint/blob/main/docs/customize_specifications.md) on GitHub.

## Add `cfn-lint` to your workflow
<a name="cfn-lint-integrate"></a>

You can run `cfn-lint` in the following places:
+ **In your editor** – The CloudFormation Language Server uses `cfn-lint` to show problems while you type. For setup, see [CloudFormation Language Server](ide-extension.md). Plugins are also available for other editors, including Vim, Emacs, and Sublime Text.
+ **Before a Git commit** – Add `cfn-lint` to your `.pre-commit-config.yaml` file so that it runs on changed templates before each commit. Replace the `rev` value with the version that you want to use.

  ```
  repos:
    - repo: https://github.com/aws-cloudformation/cfn-lint
      rev: v1.56.0
      hooks:
        - id: cfn-lint
          files: templates/.*\.(json|yml|yaml)$
  ```
+ **In an automated build** – Run `cfn-lint` as a build step and use the exit code to fail the build. A GitHub Action for `cfn-lint` is also available.
+ **In your own Python code** – Import `cfnlint.api` and call `lint` or `lint_all` to check a template string and process the results in your application.

  ```
  from cfnlint.api import lint, ManualArgs
  
  with open("template.yaml") as f:
      template = f.read()
  
  matches = lint(template, config=ManualArgs(regions=["us-east-1"]))
  for match in matches:
      print(match)
  ```

For editor plugins, the GitHub Action, and more integration examples, see [`cfn-lint`](https://github.com/aws-cloudformation/cfn-lint) on GitHub.