# Data types

The following table lists the key data types used by the next generation of Resilience Hub API.

| Type                        | Description                                                                                                                                                      |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SystemEntity`              | System with ARN, name, description, and creation time.                                                                                                           |
| `UserJourneyEntity`         | User journey with name, description, service list, and policy.                                                                                                   |
| `ServiceEntity`             | Service with ARN, name, system association, permission model, and input<br>sources.                                                                              |
| `ResiliencePolicyEntity`    | Policy with name and components (DR, availability, performance).                                                                                                 |
| `AssessmentEntity`          | Assessment with ID, status, timestamps, and failure mode findings count.                                                                                         |
| `FindingEntity`             | Failure mode finding with ID, name, description, severity, and<br>recommendations.                                                                               |
| `RecommendationEntity`      | Recommendation with name, description, cost, and complexity.                                                                                                     |
| `DependencyDiscoveryConfig` | Dependency discovery configuration with status, eligible resource count, message,<br>and last-updated timestamp. Returned by `GetService` and<br>`ListServices`. |
| `DependencyEntity`          | Dependency with name, location, criticality, and allowed status.                                                                                                 |
| `TopologyEntity`            | Topology with ID, timestamp, resource count, and edges.                                                                                                          |
