Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Example: An 'Approval' gate

The following example shows how to add an **Approval** gate called
`Approval_01` between two actions called `Staging`, and
`Production`. The `Staging` action runs first, the
`Approval_01` gate second, and the `Production` action last.
The `Production` action only runs if the `Approval_01` gate is
unlocked. The `DependsOn` property ensures that the `Staging`,
`Approval_01`, and `Production` phases run in sequential
order.

For more information about the **Approval** gate, see [Requiring approvals on workflow runs](workflows-approval.md "workflows-approval.md").

```
Actions:
  Staging: # Deploy to a staging server
    Identifier: aws/ecs-deploy@v1
    Configuration:
    ...
  Approval_01:
    Identifier: aws/approval@v1
    DependsOn:
      - Staging
    Configuration:
      ApprovalsRequired: 2
  Production: # Deploy to a production server
    Identifier: aws/ecs-deploy@v1
    DependsOn:
      - Approval_01
    Configuration:
    ...
```
