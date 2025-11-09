Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding secrets components to a blueprint

Secrets can be used in CodeCatalyst to store sensitive data that can be referenced in workflows. You can add a
secret to your custom blueprint and reference it in your workflow. For more information, see
[Masking data using secrets](workflows-secrets.md "workflows-secrets.md").

**To import Amazon CodeCatalyst blueprints region type**

In your `blueprint.ts` file, add the following:

```
import { Secret, SecretDefinition } from '@amazon-codecatalyst/blueprint-component.secrets'
```

###### Topics

- [Creating a secret](#comp-create-secrets-bp "#comp-create-secrets-bp")
- [Referencing a secret in a workflow](#comp-reference-secrets-bp "#comp-reference-secrets-bp")

## Creating a secret

The following example creates a UI component that prompts the user to enter a secret value and optional description:

```
export interface Options extends ParentOptions {
    ...
    mySecret: SecretDefinition;
}


export class Blueprint extends ParentBlueprint {
  constructor(options_: Options) {
    new Secret(this, options.secret);
}
```

The secret component requires a `name`. The following code is the minimum
required default shape:

```
{
    ...
    "secret": {
        "name": "secretName"
    },

}
```

## Referencing a secret in a workflow

The following example blueprint creates a secret and a workflow that references the secret value. For
more information, see [Referencing a secret in a
workflow](workflows-secrets.md#workflows-using-secrets.using-identifier "workflows-secrets.md#workflows-using-secrets.using-identifier").

```
export interface Options extends ParentOptions {
    ...
/**
*
* @validationRegex /^\w+$/
*/
  username: string;


  password: SecretDefinition;
}


export class Blueprint extends ParentBlueprint {
  constructor(options_: Options) {
    const password = new Secret(this, options_.password);

    const workflowBuilder = new WorkflowBuilder(this, {
      Name: 'my_workflow',
    });


    workflowBuilder.addBuildAction({
      actionName: 'download_files',
      input: {
        Sources: ['WorkflowSource'],
      },
      output: {
        Artifacts: [{ Name: 'download', Files: ['file1'] }],
      },
      steps: [
        `curl -u ${options_.username}:${password.reference} https://example.com`,
      ],
    });

    new Workflow(
      this,
      repo,
      workflowBuilder.getDefinition(),
    );

}
```

To learn more about using secrets in CodeCatalyst, see [Masking data using secrets](workflows-secrets.md "workflows-secrets.md").
