Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Referencing GitHub output

parameters

Use the following instructions to reference a GitHub output parameter.

###### To reference a GitHub output parameter

1. Complete the steps in [Exporting GitHub output parameters](integrations-github-action-export.md "integrations-github-action-export.md").

The GitHub output parameter is now available for use in other actions. 2. Note the output parameter's `Variables` value. It includes an underscore
(\_). 3. Refer to the output parameter using the following syntax:

```
${`action-name`.`output-name`}
```

Replace:

    * `action-name` with the name of the CodeCatalyst
     **GitHub Action** that produces the output parameter (do not use
     the GitHub action's `name` or `id`).
    * `output-name` with the output parameter's
     `Variables` value you noted earlier.

**Example**

```

BuildActionB:
  Identifier: aws/build@v1
  Configuration:
    Steps:
      - Run: echo **${MyGitHubAction.random-color-generator\_SELECTEDCOLOR}**
```

###### Example with context

The following example shows you how to set a `SELECTEDCOLOR` variable in
`GitHubActionA`, output it, and then refer to it in
`BuildActionB`.

```
Actions:
  GitHubActionA:
    Identifier: aws/github-actions-runner@v1
    Configuration:
      Steps:
        - name: Set selected color
          run: echo "SELECTEDCOLOR=green" >> $GITHUB_OUTPUT
          id: random-color-generator
    Outputs:
      Variables:
      - 'random-color-generator_SELECTEDCOLOR'

   BuildActionB:
    Identifier: aws/build@v1
    Configuration:
      Steps:
        - Run: echo **${GitHubActionA.random-color-generator\_SELECTEDCOLOR}**

```
