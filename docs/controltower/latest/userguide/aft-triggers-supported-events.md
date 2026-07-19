# Supported event paths

The `account_move` trigger fires when AFT receives an
`UpdateManagedAccount` AWS Control Tower lifecycle event. This event is emitted
when:

- An account's OU is changed through the AFT account request file (Terraform
  `ManagedOrganizationalUnit` parameter update).
- An account is updated through the AWS Control Tower console.
- An account is moved using the Register OU or Account Factory operations (console
  or Service Catalog API).

###### Important

Accounts updated through the Auto Enroll feature in AWS Control Tower landing zone do not emit
the `UpdateManagedAccount` lifecycle event. The customization trigger
does not fire for those operations.

For more information about AWS Control Tower lifecycle events, see
[Lifecycle events](lifecycle-events.md "lifecycle-events.md")
in the _AWS Control Tower User Guide_.
