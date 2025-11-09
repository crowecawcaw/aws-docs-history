Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Specifying the version of a gate

By default, when you add a gate to a workflow, CodeCatalyst adds the full version to the
workflow definition file using the format:

`v`major`.`minor`.`patch``

For example:

```
My-Gate:
  Identifier: aws/approval@v1
```

You can lengthen the version so that the workflow uses a specific major or minor
version of the gate. For instructions, see [Specifying the action version to use](workflows-action-versions.md "workflows-action-versions.md"). The referenced topic refers to workflow
actions but applies equally to gates.

For more information about gates in CodeCatalyst, see [Gating a workflow run](workflows-gates.md "workflows-gates.md").
