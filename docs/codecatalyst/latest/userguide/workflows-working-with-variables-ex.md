Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Examples of

variables

The following examples show how to define and reference variables in
the workflow definition file.

For more information about variables, see [Using variables in workflows](workflows-working-with-variables.md "workflows-working-with-variables.md").

###### Examples

- [Example:
  Defining a variable using the Inputs property](#workflows-working-with-variables-ex-define-inputs "#workflows-working-with-variables-ex-define-inputs")
- [Example:
  Defining a variable using the Steps property](#workflows-working-with-variables-ex-define-steps "#workflows-working-with-variables-ex-define-steps")
- [Example:
  Exporting a variable using the Outputs property](#workflows-working-with-variables-ex-export-outputs "#workflows-working-with-variables-ex-export-outputs")
- [Example:
  Referencing a variable defined in the same action](#workflows-working-with-variables-ex-refer-current "#workflows-working-with-variables-ex-refer-current")
- [Example:
  Referencing a variable defined in another action](#workflows-working-with-variables-ex-refer-other "#workflows-working-with-variables-ex-refer-other")
- [Example:
  Referencing a secret](#workflows-working-with-variables-ex-refer-secret "#workflows-working-with-variables-ex-refer-secret")

## Example:

Defining a variable using the Inputs property

The following example shows you how to define two variables, `VAR1`
and `VAR2`, in an `Inputs` section.

```
Actions:
  Build:
    Identifier: aws/build@v1
    Inputs:
      Variables:
      - Name: VAR1
        Value: "My variable 1"
      - Name: VAR2
        Value: "My variable 2"
```

## Example:

Defining a variable using the Steps property

The following example shows you how to define a `DATE` variable in
the `Steps` section explicitly.

```
Actions:
  Build:
    Identifier: aws/build@v1
    Configuration:
      Steps:
        - Run: DATE=$(date +%m-%d-%y)
```

## Example:

Exporting a variable using the Outputs property

The following example shows you how to define two variables,
`REPOSITORY-URI` and `TIMESTAMP`, and export them
using the `Outputs` section.

```
Actions:
  Build:
    Identifier: aws/build@v1
    Inputs:
      Variables:
        - Name: REPOSITORY-URI
          Value: 111122223333.dkr.ecr.us-east-2.amazonaws.com/codecatalyst-ecs-image-repo
    Configuration:
      Steps:
        - Run: TIMESTAMP=$(date +%m-%d-%y-%H-%m-%s)
    Outputs:
      Variables:
        - REPOSITORY-URI
        - TIMESTAMP
```

## Example:

Referencing a variable defined in the same action

The following example shows you how to specify a `VAR1` variable in
`MyBuildAction`, and then reference it in the same action using
`$VAR1`.

```
Actions:
  MyBuildAction:
    Identifier: aws/build@v1
    Inputs:
      Variables:
        - Name: VAR1
          Value: my-value
    Configuration:
      Steps:
        - Run: $VAR1

```

## Example:

Referencing a variable defined in another action

The following example shows you how to specify a `TIMESTAMP`
variable in `BuildActionA`, export it using the `Outputs`
property, and then reference it in `BuildActionB` using
`${BuildActionA.TIMESTAMP}`.

```
Actions:
  BuildActionA:
    Identifier: aws/build@v1
    Configuration:
      Steps:
        - Run: TIMESTAMP=$(date +%m-%d-%y-%H-%m-%s)
    Outputs:
      Variables:
        - TIMESTAMP
  BuildActionB:
    Identifier: aws/build@v1
    Configuration:
      Steps:
        - Run: docker build -t my-ecr-repo/image-repo:latest .
        - Run: docker tag my-ecr-repo/image-repo:**${BuildActionA.TIMESTAMP}**

        # Specifying just '$TIMESTAMP' here will not work
        # because TIMESTAMP is not a variable
        # in the BuildActionB action.

```

## Example:

Referencing a secret

The following example shows you how to reference a `my-password`
secret. The `my-password` is the secret's key. This secret's key and
corresponding password value must be specified on the
**Secrets** page of the CodeCatalyst console prior to being used
in the workflow definition file. For more information, see [Masking data using secrets](workflows-secrets.md "workflows-secrets.md").

```
Actions:
  BuildActionA:
    Identifier: aws/build@v1
    Configuration:
      Steps:
        - Run: curl -u LiJuan:**${Secrets.my-password}** https://example.com
```
