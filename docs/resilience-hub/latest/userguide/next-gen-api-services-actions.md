# Services

| Action          | Method | Description                                                                                                                                    |
| --------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `CreateService` | POST   | Create a service with regions, permission model, report configuration, and dependency<br>discovery settings.                                   |
| `UpdateService` | POST   | Update service configuration including permission model and dependency<br>discovery.                                                           |
| `GetService`    | GET    | Retrieve full service details including effective policy values and resilience<br>score.                                                       |
| `ListServices`  | GET    | List services, filterable by `systemId`,<br>`userJourneyId`, `organizationId`,<br>`ouId`, `accountId`,<br>`assessmentStatus`, and `policyArn`. |
| `DeleteService` | POST   | Delete a service.                                                                                                                              |
