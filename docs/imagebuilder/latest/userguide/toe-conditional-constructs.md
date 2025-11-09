# Use conditional constructs in

AWSTOE

Conditional constructs perform different actions in your component document based
on whether the specified conditional expression evaluates to `true` or
`false`. You can use the `if` construct to control the flow
of execution in your component document.

## if Construct

You can use the `if` construct to evaluate whether a step should run
or not. By default, when the `if` conditional expression evaluates to
`true`, AWSTOE runs the step, and when the condition evaluates to `false`,
AWSTOE skips the step. If a step is skipped, it's treated as a successful step when AWSTOE
evaluates whether the phase and document ran successfully.

###### Note

An `if` statement is only evaluated one time, even if the step triggers
a restart. If a step restarts, it recognizes that the `if` statement has
already been evaluated, and continues where it left off.

### Syntax

```
if:
  - <conditional expression>:
      [then: <step action>]
      [else: <step action>]
```

| Key name               | Required    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| conditional expression | Yes         | The conditional expression can contain exactly one of the<br>following types of operators at the top level.<br>• **Comparison operator** –<br>For a list of comparison operators, and information about how<br>they work in AWSTOE component documents, see<br>[Comparison<br>operators](toe-comparison-operators.md "toe-comparison-operators.md").<br>• **Logical operator** –<br>Logical operators include `and`, `or`, and<br>`not`, and operate on one or more comparison operators.<br>For more information about how logical operators work in AWSTOE<br>component documents, see [Logical<br>operators](toe-logical-operators.md "toe-logical-operators.md").<br>If your expression must satisfy multiple conditions, use a<br>logical operator to specify your conditions. |
| then                   | No          | Defines the action to take if the conditional expression<br>evaluates to `true`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| else                   | No          | Defines the action to take if the conditional expression<br>evaluates to `false`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| step action            | Conditional | When you use `then` or `else`,<br>you must specify one of the following step actions:<br>• **Abort** – AWSTOE<br>marks the step as failed.<br>• **Execute** – AWSTOE<br>runs the step.<br>• **Skip** – AWSTOE<br>skips the step.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

###### Example 1: Install package

The following example steps from an AWSTOE component document use logical operators
to test a parameter value and run the appropriate package manager commands to install
an application if the package is unzipped.

```

    - name: InstallUnzipAptGet
      action: ExecuteBash
      if:
        and:
            - binaryExists: 'apt-get'
            - not:
                binaryExists: 'unzip'
      inputs:
        commands:
            - sudo apt-get update
            - sudo apt-get install -y unzip

    - name: InstallUnzipYum
      action: ExecuteBash
      if:
        and:
            - binaryExists: 'yum'
            - not:
                binaryExists: 'unzip'
      inputs:
        commands:
            - sudo yum install -y unzip

    - name: InstallUnzipZypper
      action: ExecuteBash
      if:
        and:
            - binaryExists: 'zypper'
            - not:
                binaryExists: 'unzip'
      inputs:
        commands:
            - sudo zypper refresh
            - sudo zypper install -y unzip
```

###### Example 2: Skip a step

The following example shows two ways to skip a step. One uses a logical operator,
and one uses a comparison operator with the `Skip` step action.

```
# Creates a file if it does not exist using not
- name: CreateMyConfigFile-1
  action: ExecuteBash
  if:
    not:
      fileExists: '/etc/my_config'
  inputs:
    commands:
      - echo "Hello world" > '/etc/my_config'

# Creates a file if it does not exist using then and else
- name: CreateMyConfigFile-2
  action: ExecuteBash
  if:
    fileExists: '/etc/my_config'
    then: Skip
    else: Execute
  inputs:
    commands:
      - echo "Hello world" > '/etc/my_config'
```
