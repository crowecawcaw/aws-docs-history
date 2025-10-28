# parse-tree

Generates a parse tree for the AWS CloudFormation Guard rules defined in a rules file.

## Syntax

```
cfn-guard parse-tree
--output <value>
--rules <value>
```

## Parameters

`-h`, `--help`

Prints help information.

`-p`, `--print-json`

Prints the output in JSON format.

`-y`, `--print-yaml`

Prints the output in YAML format.

`-V`, `--version`

Prints version information.

## Options

`-o`, `--output`

Writes the generated tree to an output file.

`-r`, `--rules`

Provides a rules file.

## Examples

```
cfn-guard parse-tree --output `output.json` --rules `rules.guard`
```
