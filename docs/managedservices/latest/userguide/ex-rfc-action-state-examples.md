# Review RFC action states use case examples

**Use Case: Visibility on Manual RFC Process**

- Once you submit a manual RFC, the RFC action state automatically
  changes to `AwsActionPending` to indicate that an operator needs
  to review and approve the RFC. When an operator begins actively reviewing your RFC,
  the RFC action state changes to `AwsOperatorAssigned`.
- Consider a manual RFC that has been approved and scheduled and is
  ready to begin running. Once the RFC status changes to `InProgress`,
  the RFC action state automatically changes to `AwsActionPending`. It
  changes again to `AwsOperatorAssigned` once an operator starts actively
  running the RFC.
- When a manual RFC is completed (closed as "Success" or "Failure"), the
  RFC Action state changes to `NoActionPending` to indicate that no further
  actions are necessary from either the customer or operator.
  **Use case: RFC correspondence**

- When a manual RFC is `Pending Approval`, an AMS
  Operator might need further information from you. Operators will
  post a correspondence to the RFC and change the RFC action state to
  `CustomerActionPending`. When you respond by adding a
  new RFC correspondence, the RFC action state automatically changes
  to `AwsActionPending`.
- When an automated or manual RFC has failed, you can add a
  correspondence to the RFC details, asking the AMS Operator why the
  RFC failed. When your correspondence is added, the RFC action state
  is automatically set to `AwsActionPending`. When the
  AMS operator picks up the RFC to view your correspondence, the RFC
  action state changes to `AwsOperatorAssigned`. When the
  operator responds by adding a new RFC correspondence, the RFC action
  state may be set to `CustomerActionPending`, indicating
  that there is another response from the customer expected, or to
  `NoActionPending`, indicating that no response from
  the customer is needed or expected.
