# test

Validates an AWS CloudFormation Guard rules file against a Guard unit testing file in JSON
or YAML format to determine the success of individual rules.

## Syntax

```
cfn-guard test
--rules-file <value>
--test-data <value>
```

## Parameters

`-a`, `--alphabetical`

Sort alphabetically inside a directory.

`-h`, `--help`

Prints help information.

`-m`, `--last-modified`

Sorts by last-modified times within a directory

`-V`, `--version`

Prints version information.

`-v`, `--verbose`

Increases the output verbosity. Can be specified multiple times.

The verbose output follows the structure of the Guard rules file. Every block in
the rules file is a block in the verbose output. The top-most block is each rule. If there are
`when` conditions against the rule, they appear as a sibling condition block.

## Options

`-d`, `--dir`

Provide the root directory for rules.

`-o`, `--output-format`

Specify the format in which the output should be displayed.

_Default_: `single-line-summary`

_Allowed values_: `json` | `yaml` |
`single-line-summary` | `junit`

`-r`, `--rules-file`

Provides the name of a rules file.

`-t`, `--test-data`

Provides the name of a file or directory for data files in either JSON or YAML
format.

## Examples

```
cfn-guard test --rules-file `rules.guard` --test-data `example.json`
```

## Output

```
`PASS|FAIL` Expected Rule = `rule_name`, Status = `SKIP|FAIL|PASS`, Got Status = `SKIP|FAIL|PASS`
```

## See also

[Testing Guard rules](testing-rules.md "testing-rules.md")
