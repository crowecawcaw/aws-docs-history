

# Validate templates with `cloudformation-validate`
<a name="cloudformation-validate"></a>

The open-source [`cloudformation-validate` project](https://github.com/aws-cloudformation/cloudformation-validate) checks JSON and YAML CloudFormation templates locally and is available on GitHub. It can find invalid template structure, broken references, security issues, and best-practice problems. Each finding includes the problem, its severity, and its location in the template.

The tool includes the rules and CloudFormation resource definitions that it needs, so it runs without network access or AWS credentials after installation.

**Topics**
+ [Choose a validation method](#cloudformation-validate-ways-to-use)
+ [Install the command-line tool](#cloudformation-validate-install)
+ [Run validation](#cloudformation-validate-run)
+ [Add custom rules](#cloudformation-validate-custom-rules)
+ [Embed the validation library](#cloudformation-validate-library)
+ [Use with AWS CDK](#cloudformation-validate-cdk)
+ [Understand validation scope](#cloudformation-validate-scope)

## Choose a validation method
<a name="cloudformation-validate-ways-to-use"></a>
+ **Command line** – Run `cfn-validate` to check one template or every template in a directory from a terminal or an automated build.
+ **Library** – Add the validator to a Rust, Node.js, Python, Go, or JVM application and process the results in your code.
+ **AWS CDK** – Validate templates automatically after CDK synthesizes them.
+ **Custom rules** – Add checks written in CEL, Rego, or the Guard rule language. For supported rule formats and examples, see the [Custom Rules Reference](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/src/CUSTOM_RULES.md) on GitHub. For Guard rule syntax, see [Validate templates with Guard](cloudformation-guard.md) in this guide.

## Install the command-line tool
<a name="cloudformation-validate-install"></a>

Open the [latest `cfn-validate` release](https://github.com/aws-cloudformation/cloudformation-validate/releases/latest) on GitHub and download the `cfn-validate` file for your operating system and processor. Follow the [installation guide](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/INSTALLATION.md) on GitHub to rename the file to `cfn-validate`, add it to your `PATH`, and verify the downloaded file.

## Run validation
<a name="cloudformation-validate-run"></a>

The command uses the following syntax:

```
cfn-validate {{TEMPLATE_OR_DIRECTORY}} [OPTIONS]
```

Check one template:

```
cfn-validate template.yaml
```

Pass a directory to recursively check every `.yaml`, `.yml`, and `.json` file:

```
cfn-validate ./templates/
```

The command writes a structured JSON validation report to standard output. Use `--format standard` for compact output or `--format detailed` for the default detailed report.

The command returns `0` when it finds no error or fatal diagnostics, `1` when it finds error or fatal diagnostics, and `2` for a usage or initialization error, such as an invalid option or a file that doesn't exist.

For all engines, filters, output formats, and parameters, see the [`cfn-validate` CLI reference](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/src/cfn-validate/README.md) on GitHub.

## Add custom rules
<a name="cloudformation-validate-custom-rules"></a>

Use `--rule-source` to load a custom Rego or CEL rule file. Use `--guard-rule-source` to load a Guard rule file or directory. You can repeat either option to load multiple rule sources:

```
cfn-validate template.yaml --rule-source ./rules/my-rule.rego
cfn-validate template.yaml --guard-rule-source ./guard-rules/
```

For rule formats and examples, see [Custom Rules Reference](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/src/CUSTOM_RULES.md) on GitHub.

## Embed the validation library
<a name="cloudformation-validate-library"></a>

Install the published package for your programming language to run the same offline checks from your application. Create a validation engine once, reuse it for multiple templates, and process the structured diagnostics returned for each template. You can also configure custom CEL, Rego, or Guard rules through the library API.


| Language | Published package | API and examples | 
| --- | --- | --- | 
| Rust | [`cloudformation-validate` on crates.io](https://crates.io/crates/cloudformation-validate) | [Rust API and examples](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/src/bindings-rust/README.md) | 
| Node.js | [`@aws/cloudformation-validate` on npm](https://www.npmjs.com/package/@aws/cloudformation-validate) | [Node.js API and examples](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/src/bindings-wasm/README.md) | 
| Python | [`cloudformation-validate` on PyPI](https://pypi.org/project/cloudformation-validate/) | [Python API and examples](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/src/bindings-python/README.md) | 
| Go | [CloudFormation Validate Go module](https://pkg.go.dev/github.com/aws-cloudformation/cloudformation-validate/src/bindings-go/go) | [Go API and examples](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/src/bindings-go/README.md) | 
| JVM (Java or Kotlin) | [`software.amazon.cloudformation:cloudformation-validate` on Maven Central](https://central.sonatype.com/artifact/software.amazon.cloudformation/cloudformation-validate) | [JVM API and examples](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/src/bindings-jvm/README.md) | 

For installation instructions and supported platforms, see the [language binding installation guide](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/INSTALLATION.md#language-bindings).

For complete examples in every language and links to each API guide, see [Embedding as a library](https://github.com/aws-cloudformation/cloudformation-validate#embedding-as-a-library) in the project documentation on GitHub.

## Use with AWS CDK
<a name="cloudformation-validate-cdk"></a>

If you use AWS CDK, you don't need to install the validator separately. The AWS CDK construct library includes a default `CloudFormationValidatePlugin` that runs the same checks automatically after synthesizing your CloudFormation templates.

```
cdk synth
```

CDK reports possible deployment failures and best-practice findings with its validation results. You can explicitly configure `CloudFormationValidatePlugin` when you want to add custom Rego or Guard rules.

For plugin configuration, acknowledgments, and validation reporting, see [Template and Policy Validation](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib-readme.html#template-and-policy-validation) in the *AWS CDK API Reference*.

## Understand validation scope
<a name="cloudformation-validate-scope"></a>

For the limitations of local validation and steps to take before deployment, see [Understand validation scope](template-guide.md#template-validation-scope).