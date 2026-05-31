# Supported Next generation Resilience Hub events

All Next generation Resilience Hub API actions are logged in CloudTrail, including the following.

| Category    | Example events                                                                            |
| ----------- | ----------------------------------------------------------------------------------------- |
| Systems     | `CreateSystem`, `DeleteSystem`,<br>`GetSystem`, `ListSystems`                             |
| Services    | `CreateService`, `UpdateService`,<br>`DeleteService`, `ListServices`                      |
| Policies    | `CreateResiliencePolicy`,<br>`UpdateResiliencePolicy`,<br>`DeleteResiliencePolicy`        |
| Assessments | `StartFailureModeAssessment`,<br>`GetFailureModeAssessment`,<br>`ListFailureModeFindings` |
| Discovery   | `StartServiceTopologyDiscovery`,<br>`ListDependencies`,<br>`ClassifyDependency`           |
