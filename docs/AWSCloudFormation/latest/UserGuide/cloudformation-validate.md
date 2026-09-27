

# Validate templates with `cloudformation-validate`
<a name="cloudformation-validate"></a>

AWS CloudFormation Validate (`cloudformation-validate`) helps you find template problems before deployment. It checks JSON and YAML templates locally for invalid template structure, broken references, security issues, and best-practice problems. Each finding includes a stable rule ID, a severity, the line and column in the template, the affected resource, and, when available, a suggested fix.

The tool includes the rules and CloudFormation resource schemas that it needs. As a result, it runs without network access or AWS credentials after installation. Validation of a typical template completes in less than a second. You can run it from the command line or embed it in a Rust, Node.js, Python, Go, or JVM application. You can also let AWS CDK run it after synthesis. All of these methods produce the same results.

For release notes and the complete list of built-in rules, see [`cloudformation-validate`](https://github.com/aws-cloudformation/cloudformation-validate) on GitHub.

For the limitations of local validation and steps to take before deployment, see [Understand validation scope](template-guide.md#template-validation-scope).

**Topics**
+ [How validation works](#cloudformation-validate-how-it-works)
+ [Choose a validation method](#cloudformation-validate-ways-to-use)
+ [Install the command-line tool](#cloudformation-validate-install)
+ [Run validation](#cloudformation-validate-run)
+ [Understand the results](#cloudformation-validate-results)
+ [Filter the results](#cloudformation-validate-filter)
+ [Add custom rules](#cloudformation-validate-custom-rules)
+ [Validate new resource types and properties](#cloudformation-validate-additional-schemas)
+ [Embed the validation library](#cloudformation-validate-library)
+ [Use with AWS CDK](#cloudformation-validate-cdk)

## How validation works
<a name="cloudformation-validate-how-it-works"></a>

When you validate a template, `cloudformation-validate` resolves intrinsic functions such as `Ref`, `Fn::GetAtt`, `Fn::Sub`, and `Fn::If`, and then runs the following checks:
+ **Schema checks** – Compares each resource with the [CloudFormation resource provider schemas](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/resource-type-schemas.html) and reports type mismatches, missing required properties, invalid enumeration values, and pattern or constraint failures.
+ **Rules** – Runs the built-in rules and any custom rules that you provide. These rules find semantic errors, broken cross-resource references, security risks, and best-practice problems.
+ **State machine checks** – Validates the definitions of `AWS::StepFunctions::StateMachine` resources, including state types, `StartAt` and `Next` references, and required fields.

## Choose a validation method
<a name="cloudformation-validate-ways-to-use"></a>
+ **Command line** – Run `cfn-validate` to check one template or every template in a directory from a terminal or an automated build. See [Install the command-line tool](#cloudformation-validate-install).
+ **Library** – Add the validator to a Rust, Node.js, Python, Go, or JVM application and process the results in your code. See [Embed the validation library](#cloudformation-validate-library).
+ **AWS CDK** – Validate templates automatically after AWS CDK synthesizes them. See [Use with AWS CDK](#cloudformation-validate-cdk).

With any method, you can add custom rules written in Common Expression Language (CEL), Rego, or the Guard rule language. See [Add custom rules](#cloudformation-validate-custom-rules).

## Install the command-line tool
<a name="cloudformation-validate-install"></a>

The `cfn-validate` command is a single file with no dependencies. Open the [latest release](https://github.com/aws-cloudformation/cloudformation-validate/releases/latest) on GitHub and download the file for your operating system and processor. Files are available for Linux (x86-64 and ARM64), macOS (Apple silicon and Intel), and Windows (x86-64 and ARM64).

On Linux or macOS, make the file executable, rename it to `cfn-validate`, and move it to a directory on your `PATH`. The following example uses the Linux x86-64 file. Replace {{VERSION}} with the version that you downloaded.

```
chmod +x cfn-validate-{{VERSION}}-linux-x64
sudo mv cfn-validate-{{VERSION}}-linux-x64 /usr/local/bin/cfn-validate
```

On Windows, rename the file to `cfn-validate.exe` and move it to a directory on your `PATH`.

Each release also includes a signature file for every download and the public key used to sign it. To verify a download before you use it, see [Verify a downloaded release asset](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/INSTALLATION.md#verify-a-downloaded-release-asset) on GitHub.

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

Some checks depend on the AWS Region or on parameter values. Use `--region` to set the `AWS::Region` pseudo parameter, `--parameter` to set a template parameter, and `--pseudo-parameter` to set other pseudo parameters such as `AWS::AccountId` or `AWS::Partition`. You can repeat `--parameter` and `--pseudo-parameter`:

```
cfn-validate template.yaml --region us-west-2 --parameter Environment=prod --parameter InstanceType=t3.micro
```

To treat warnings as errors, for example in an automated build, add `--strict`. To list every built-in rule, run `cfn-validate --list-rules`.

## Understand the results
<a name="cloudformation-validate-results"></a>

The command writes a JSON report to standard output. Each finding in the report includes the rule ID, severity, message, source location (line and column), the resource or other template entity, and a suggested fix when one is available. The default `--format detailed` report also includes the rule description and related context. Use `--format standard` for a compact report that omits those fields.

To limit the report to more serious findings, use `--level` with the minimum severity to include:

```
cfn-validate template.yaml --level error
```

The command returns exit code `0` when it finds no errors, `1` when it finds errors, and `2` for a usage or initialization error, such as an invalid option or a file that doesn't exist. With `--strict`, warnings also cause exit code `1`.

## Filter the results
<a name="cloudformation-validate-filter"></a>

You can include or exclude findings by rule ID, rule ID range, category, resource type, service prefix, or the logical ID of a template entity. Each filter has an `--include-` and an `--exclude-` form. The following examples show common filters:

```
# Suppress specific rules everywhere
cfn-validate template.yaml --exclude-ids {{RULE_ID}},{{RULE_ID}}

# Report only security findings
cfn-validate template.yaml --include-categories Security

# Suppress one rule for one resource only
cfn-validate template.yaml --exclude-logical-id MyBucket={{RULE_ID}}

# Suppress every rule for a resource type
cfn-validate template.yaml --exclude-resource-type AWS::EC2::Instance

# Suppress every rule for a service
cfn-validate template.yaml --exclude-service AWS::AutoScaling
```

Filters that target a resource type, service, or logical ID accept an optional `={{RULE_ID}}` suffix to limit the filter to one rule. Without the suffix, the filter applies to every rule for that target. For all filter options, see the [`cfn-validate` CLI reference](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/src/cfn-validate/README.md) on GitHub.

## Add custom rules
<a name="cloudformation-validate-custom-rules"></a>

You can add your own checks in any of the following formats. Each format assumes basic familiarity with its rule language. By default, custom rules run in addition to the built-in rules. To run only your custom rules, add `--disable-builtin-rules`.
+ **CEL** (`.json`) – Property and data-driven checks written as [CEL](https://cel.dev/) expressions in a JSON file. Load with `--rule-source`.
+ **Rego** (`.rego`) – Complex cross-resource logic written in the [Rego](https://www.openpolicyagent.org/docs/policy-language) policy language. Load with `--rule-source`.
+ **Guard** (`.guard`) – Declarative compliance rules in the Guard rule language. Load a file or directory with `--guard-rule-source`. The validator supports a subset of the Guard language. If a rule uses an unsupported construct, the validator rejects the rule when it loads instead of ignoring the construct. For the rule syntax, see [Validate templates with Guard](cloudformation-guard.md).

You can repeat either option to load multiple rule sources:

```
cfn-validate template.yaml --rule-source ./rules/checks.json --rule-source ./rules/network.rego
cfn-validate template.yaml --guard-rule-source ./guard-rules/
```

The following CEL example in `checks.json` reports a finding for each Amazon S3 bucket without encryption. The `resource_type` field makes the rule run once for each resource of that type, and `{name}` in the message is replaced with the resource's logical ID.

```
{
  "rules": [
    {
      "rule_id": "CUSTOM001",
      "severity": "ERROR",
      "resource_type": "AWS::S3::Bucket",
      "expression": "!has(properties.BucketEncryption)",
      "message": "S3 bucket {name} must have encryption configured",
      "prop_path": "Properties.BucketEncryption",
      "suggested_fix": "Add BucketEncryption with SSEAlgorithm: aws:kms"
    }
  ]
}
```

For more information about the data available to rules, the supported CEL functions, and writing Rego rules, see the [Custom Rules Reference](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/src/CUSTOM_RULES.md) on GitHub.

## Validate new resource types and properties
<a name="cloudformation-validate-additional-schemas"></a>

The bundled schemas match the CloudFormation registry at the time of the release. If a template uses a resource type, property, or allowed value that CloudFormation published after that release, or a private resource type from your own registry, pass the resource provider schema with `--additional-schema`. The validator uses it to extend the bundled schema for an existing type or to validate a new type. You can pass a `.json` file or a directory of schema files, and repeat the option:

```
cfn-validate template.yaml --additional-schema ./schemas/
```

An additional schema never removes a constraint from the bundled schema. If a schema can't be read or applied, the command exits with code `2` instead of ignoring it.

## Embed the validation library
<a name="cloudformation-validate-library"></a>

Install the package for your programming language to run the same offline checks from your application. Create a validation engine once, reuse it for multiple templates, and process the structured diagnostics returned for each template. You can also configure custom CEL, Rego, or Guard rules and additional schemas through the library API.


| Language | Package | Install | Documentation | 
| --- | --- | --- | --- | 
| Rust | [`cloudformation-validate`](https://crates.io/crates/cloudformation-validate) on crates.io | cargo add cloudformation-validate | [API and examples](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/src/bindings-rust/README.md) | 
| Node.js | [`@aws/cloudformation-validate`](https://www.npmjs.com/package/@aws/cloudformation-validate) on npm | npm install @aws/cloudformation-validate | [API and examples](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/src/bindings-wasm/README.md) | 
| Python | [`cloudformation-validate`](https://pypi.org/project/cloudformation-validate/) on PyPI | python3 -m pip install cloudformation-validate | [API and examples](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/src/bindings-python/README.md) | 
| Go | [`cloudformation-validate/src/bindings-go/go`](https://pkg.go.dev/github.com/aws-cloudformation/cloudformation-validate/src/bindings-go/go) on pkg.go.dev | go get github.com/aws-cloudformation/cloudformation-validate/src/bindings-go/go@latest | [API and examples](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/src/bindings-go/README.md) | 
| JVM (Java or Kotlin) | [`software.amazon.cloudformation:cloudformation-validate`](https://central.sonatype.com/artifact/software.amazon.cloudformation/cloudformation-validate) on Maven Central | implementation("software.amazon.cloudformation:cloudformation-validate:{{VERSION}}") (Gradle) or the equivalent Maven dependency | [API and examples](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/src/bindings-jvm/README.md) | 

Every library exposes one method that validates a template and returns a report with the same diagnostics as the command-line tool. The following examples use `CompositeEngine`, the default engine, which runs the built-in rules and any custom CEL, Rego, or Guard rules that you configure. Each example validates one template and prints each finding.

Python:

```
from cloudformation_validate import CompositeEngine

engine = CompositeEngine()
report = engine.validate_template("template.yaml")
for d in report.diagnostics:
    print(f"[{d.severity.name}] {d.rule_id}: {d.message}")
```

Kotlin:

```
import software.amazon.cloudformation.validate.CompositeEngine
import java.io.File

fun main() {
    val engine = CompositeEngine()
    val report = engine.validateTemplate(File("template.yaml"))
    for (d in report.diagnostics) {
        println("[${d.severity}] ${d.ruleId}: ${d.message}")
    }
}
```

For supported language runtimes, version pinning, prerelease channels, and Maven and Gradle syntax, see the [language binding installation guide](https://github.com/aws-cloudformation/cloudformation-validate/blob/main/INSTALLATION.md#language-bindings) on GitHub. For the API reference and complete examples in each language, see [Embedding as a library](https://github.com/aws-cloudformation/cloudformation-validate#embedding-as-a-library) on GitHub.

## Use with AWS CDK
<a name="cloudformation-validate-cdk"></a>

If you use AWS CDK, you don't need to install the validator separately. The AWS CDK construct library includes a default `CloudFormationValidatePlugin` that runs the same checks automatically after synthesizing your CloudFormation templates.

```
cdk synth
```

AWS CDK reports possible deployment failures and best-practice findings with its validation results. You can explicitly configure `CloudFormationValidatePlugin` when you want to add custom Rego or Guard rules.

For plugin configuration, acknowledgments, and validation reporting, see [Template and Policy Validation](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib-readme.html#template-and-policy-validation) in the *AWS CDK API Reference*.