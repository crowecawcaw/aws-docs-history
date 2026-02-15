# Quotas for routing control

Routing control in Amazon Application Recovery Controller (ARC) is subject to the following quotas (formerly referred to as limits).

| Entity                                                                                                                                                                                                                                      | Quota |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| Number of clusters per account                                                                                                                                                                                                              | 2     |
| Number of control panels per cluster                                                                                                                                                                                                        | 50    |
| Number of routing controls per control panel                                                                                                                                                                                                | 100   |
| Total number of routing controls (in all control panels) per cluster                                                                                                                                                                        | 300   |
| Number of safety rules per control panel                                                                                                                                                                                                    | 20    |
| Number of routing controls per [UpdateRoutingControlStates](../../../routing-control/latest/APIReference/API_UpdateRoutingControlStates.md "../../../routing-control/latest/APIReference/API_UpdateRoutingControlStates.md") operation call | 10    |
| Number of mutating API calls to a cluster endpoint, per second                                                                                                                                                                              | 3     |
