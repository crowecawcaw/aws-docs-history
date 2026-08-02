# Resilience testing

| Action                               | Method | Description                                                                       |
| ------------------------------------ | ------ | --------------------------------------------------------------------------------- |
| `ListTestTemplates`                  | GET    | List the available test templates.                                                |
| `GetTestTemplate`                    | GET    | Retrieve a test template, including its actions and parameters.                   |
| `CreateTest`                         | POST   | Create a test for a service from a test template.                                 |
| `GetTest`                            | GET    | Retrieve a test configuration including parameters, stop conditions, and<br>role. |
| `UpdateTest`                         | POST   | Update a test configuration including parameters, stop conditions, and<br>role.   |
| `ListTests`                          | GET    | Lists tests for a service.                                                        |
| `DeleteTest`                         | POST   | Delete a test.                                                                    |
| `StartTestRun`                       | POST   | Start a test run for a service.                                                   |
| `StopTestRun`                        | POST   | Stop a test run.                                                                  |
| `ListTestRuns`                       | GET    | List test runs for a service.                                                     |
| `GetTestRun`                         | GET    | Retrieve a test run including status, parameters, and timestamp.                  |
| `ListTestRunEvents`                  | GET    | List the events in a test run's timeline.                                         |
| `PutTestSources`                     | POST   | Add or update success criteria alarms or observability alarms for a<br>test.      |
| `DeleteTestSources`                  | POST   | Remove success criteria alarms or observability alarms from a<br>test.            |
| `ListTestSources`                    | GET    | List success criteria alarms or observability alarms for a test.                  |
| `ListTestRunSources`                 | GET    | List success criteria alarms or observability alarms for a test<br>run.           |
| `ListResolvedTestRunTargetResources` | GET    | List the resources that were resolved as targets for a test run.                  |
