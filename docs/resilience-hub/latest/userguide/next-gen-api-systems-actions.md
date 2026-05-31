# Systems

| Action         | Method | Description                                                                  |
| -------------- | ------ | ---------------------------------------------------------------------------- |
| `CreateSystem` | POST   | Create a system with optional dependency discovery enablement.               |
| `UpdateSystem` | POST   | Update system description, dependency discovery, and KMS key.                |
| `GetSystem`    | GET    | Retrieve system details.                                                     |
| `ListSystems`  | GET    | List systems, filterable by<br>`organizationId`, `ouId`, and<br>`accountId`. |
| `DeleteSystem` | POST   | Delete a system (must have no associated services).                          |
