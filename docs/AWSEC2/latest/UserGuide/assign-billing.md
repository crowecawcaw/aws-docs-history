# Billing assignment for shared Amazon EC2 Capacity Reservations

By default, when a Capacity Reservation is shared, the owner is billed for the instances they run
in the Capacity Reservation and for any available capacity, also called _unused
capacity_, in the Capacity Reservation; while consumers are billed only for the
instances they run in the shared Capacity Reservation.

If needed, the Capacity Reservation owner can assign the billing of any available capacity in the
Capacity Reservation to any one of the accounts with which the Capacity Reservation is shared. After billing is
assigned to another account, that account becomes the _billing
owner_ of any available capacity in the Capacity Reservation. Any charges for
available capacity in the Capacity Reservation, from that point onward, are billed to the assigned
account instead of the owner's account. The Capacity Reservation owner and the accounts with which
the Capacity Reservation is shared continue to be billed for the instances they run in the
Capacity Reservation.

###### Important

The Capacity Reservation owner remains the resource owner and they remain responsible for
managing the Capacity Reservation. The account to which billing is assigned does not get any
additional privileges; they can't cancel, modify, or share the Capacity Reservation in any
way.

###### Topics

- [How it works](#how-billing-ownership-works "#how-billing-ownership-works")
- [Considerations](#billing-ownership-considerations "#billing-ownership-considerations")
- [Assign billing](request-billing-transfer.md "request-billing-transfer.md")
- [View billing assignment requests](view-billing-transfers.md "view-billing-transfers.md")
- [Accept or reject billing](accept-decline-billing-transfer.md "accept-decline-billing-transfer.md")
- [Cancel or revoke requests](cancel-billing-transfer.md "cancel-billing-transfer.md")
- [Monitor
  requests](billing-ownership-events.md "billing-ownership-events.md")

## How it works

Only the Capacity Reservation owner can assign billing of a shared Capacity Reservation to another account.
Billing can be assigned only to an account with which the Capacity Reservation is shared and
that is consolidated under the same AWS Organizations payer account as the Capacity Reservation
owner.

To assign billing of the available capacity of a Capacity Reservation to another account, the
Capacity Reservation owner must initiate a request to the required account. The specified
account receives the request and they must either accept or reject it within 12
hours.

- If they **accept**, they become the
  _billing owner_ of any available capacity, also
  called _unused capacity_, in the Capacity Reservation. From that
  point onward, charges for any available capacity in the Capacity Reservation are billed
  to their account instead of the owner's account. After it is accepted, only the
  Capacity Reservation owner can revoke billing from the assigned account.
- If they **reject**, the Capacity Reservation owner
  remains the billing owner of the available capacity in the Capacity Reservation. Charges
  for any available capacity in the Capacity Reservation continue to be billed to the
  owner's account.
- If they **do not accept or reject** the
  request within 12 hours, it expires and charges for any available
  capacity in the Capacity Reservation continue to be billed to owner's account.

For the period that billing is assigned to another account, the
`Reservation` and `UnusedBox` line items appear in the
assigned account's Cost and Usage Report (CUR) instead of the owner's
CUR.

The following table shows which line items appear in the CUR for the Capacity Reservation
owner and consumer accounts **before** billing is
assigned to another account.

| Account                                                         | CUR line items before billing is assigned           |
| --------------------------------------------------------------- | --------------------------------------------------- |
| Capacity Reservation owner                                      | • `Reservation`<br>• `BoxUsage` \*<br>• `UnusedBox` |
| Consumer accounts with which the Capacity Reservation is shared | • `BoxUsage` \*                                     |

The following table shows which line items appear in the CUR for the Capacity Reservation
owner and consumer accounts **after** billing is
assigned to another account.

| Account                                                               | CUR line items after billing is assigned            |
| --------------------------------------------------------------------- | --------------------------------------------------- |
| Capacity Reservation owner                                            | • `BoxUsage` \*                                     |
| Consumer account to which billing is assigned                         | • `Reservation`<br>• `BoxUsage` \*<br>• `UnusedBox` |
| Other consumer accounts with which the Capacity Reservation is shared | • `BoxUsage` \*                                     |

###### Note

- \* The `BoxUsage` line item appears in an account's CUR
  only if they have running instances in the Capacity Reservation. For more
  information about the CUR line items, see [Monitoring Capacity Reservations](../../../cur/latest/userguide/monitor-ondemand-reservations.md "../../../cur/latest/userguide/monitor-ondemand-reservations.md").
- Use the Capacity Reservation ARN in the CUR to determine who owns the Capacity Reservation. If the
  ARN includes your AWS account ID, you are the Capacity Reservation owner.
  Otherwise, the Capacity Reservation is owned by a different account but billing is
  assigned to you.
- Cost allocation tags assigned to Capacity Reservation by the owner will not appear
  in the consumer account's CUR. Cost allocation tags appear in the
  Capacity Reservation owner's CUR only.

## Considerations

Keep the following in mind when assigning billing of a shared Capacity Reservation:

- You can't do partial or split billing assignments. Billing of all
  available capacity of a Capacity Reservation can be assigned to one account at a
  time.
- The available capacity of a Capacity Reservation can change over time. This will
  impact billing for the assigned account. For example, available capacity
  can increase if the Capacity Reservation owner increases the size of the Capacity Reservation, or if
  other consumer accounts stop or terminate their instances running in the
  Capacity Reservation.
- Billing can be assigned only to a consumer account that is
  consolidated under the same AWS Organizations payer account. Billing is
  automatically revoked from the consumer account if they leave the
  organization, or if the Capacity Reservation is no longer shared with them.
- Only the Capacity Reservation owner can cancel a pending billing assignment request
  and revoke billing from an assigned account after the request has been
  accepted.
