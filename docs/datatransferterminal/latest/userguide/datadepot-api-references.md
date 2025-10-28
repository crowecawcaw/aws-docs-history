# Data Transfer Terminal API references: Actions and resources

When creating AWS Identity and Access Management (IAM) policies, this page can help you understand the relationship between AWS Data Transfer Terminal API operations, the corresponding actions that you can grant permissions to perform, and the AWS resources for which you can grant the permissions.

In general, here’s how you add Data Transfer Terminal permissions to your policy:

- Specify an action in the `Action` element. The value includes a `datatransferterminal:` prefix and the API operation name. For example, `datatransferterminal:CreateTask`.
- Specify an AWS resource related to the action in the `Resource` element.
  You can also use AWS condition keys in your Data Transfer Terminal policies. For a complete list of AWS keys, see [Available keys](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the _IAM User Guide_.

Data Transfer Terminal API operations and corresponding actions

CreateTransferTeam

- **Action:**
  `datatransferterminal:CreateTransferTeam`

**Resource:**
`None`

GetTransferTeam

- **Action:**
  `datatransferterminal:GetTransferTeam`

**Resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId````

UpdateTransferTeam

- **Action:**
  `datatransferterminal:UpdateTransferTeam`

**Resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId````

DeleteTransferTeam

- **Action:**
  `datatransferterminal:DeleteTransferTeam`

**Resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId````

ListTransferTeams

- **Action:**
  `datatransferterminal:ListTransferTeams`

**Resource:**
`None`

RegisterPerson

- **Action:**
  `datatransferterminal:RegisterPerson`

**Resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId````

GetPerson

- **Action:**
  `datatransferterminal:GetPerson`

**Resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId`/person/$[replaceable]`PersonId````

**Dependent action:**
`datatransferterminal:GetTransferTeam`

**Dependent resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId````

DeregisterPerson

- **Action:**
  `datatransferterminal:DeregisterPerson`

**Resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId`/person/$[replaceable]`PersonId````

**Dependent action:**
`datatransferterminal:GetTransferTeam`

**Dependent resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId````

ListPersons

- **Action:**
  `datatransferterminal:ListPersons`

**Resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId````

CreateReservation

- **Action:**
  `datatransferterminal:CreateReservation`

**Resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId````

**Dependent action:**
`datatransferterminal:GetTransferTeam`

**Dependent resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId````

**Dependent action:**
`datatransferterminal:GetPerson`

**Dependent resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId`/person/$[replaceable]`PersonId````

**Dependent action:**
`datatransferterminal:GetFacility`

**Dependent resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:::facility/$[replaceable]`FacilityId````

GetReservation

- **Action:**
  `datatransferterminal:GetReservation`

**Resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId`/reservation/$[replaceable]`ReservationId````

**Dependent action:**
`datatransferterminal:GetTransferTeam`

**Dependent resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId````

UpdateReservation

- **Action:**
  `datatransferterminal:UpdateReservation`

**Resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId`/reservation/$[replaceable]`ReservationId````

**Dependent action:**
`datatransferterminal:GetTransferTeam`

**Dependent resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId````

**Dependent action:**
`datatransferterminal:GetPerson`

**Dependent resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId`/person/$[replaceable]`PersonId````

DeleteReservation

- **Action:**
  `datatransferterminal:DeleteReservation`

**Resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId`/person/$[replaceable]`PersonId````

**Dependent action:**
`datatransferterminal:GetTransferTeam`

**Dependent resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId````

ListReservations

- **Action:**
  `datatransferterminal:ListReservations`

**Resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:$[replaceable]`Region`:$[replaceable]`Account`:transfer-team/$[replaceable]`TransferTeamId````

ListFacilities

- **Action:**
  `datatransferterminal:ListFacilities`

**Resource:**
`None`

GetFacility

- **Action:**
  `datatransferterminal:GetFacility`

**Resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:::facility/$[replaceable]`FacilityId````

GetFacilityAvailability

- **Action:**
  `datatransferterminal:GetFacilityAvailability`

**Resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:::facility/$[replaceable]`FacilityId`/availability`

**Dependent action:**
`datatransferterminal:GetFacility`

**Dependent resource:**
`arn:aws::$[replaceable]`Partition`:datatransferterminal:::facility/$[replaceable]`FacilityId`/availability`
