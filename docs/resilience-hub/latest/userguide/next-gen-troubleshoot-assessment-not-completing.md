# Assessment not completing

**Symptom:** Assessment stays in
`IN_PROGRESS` status for more than 30 minutes.

The following table lists possible causes and solutions.

| Cause                          | Solution                                                                                                    |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| Large service (many resources) | Assessments for services with 1,000 or more resources may take longer. Wait up to 60<br>minutes.            |
| Invoker role permissions issue | Verify the invoker role has `ReadOnlyAccess` and<br>`AWSResilienceHubV2AssessmentExecutionPolicy` attached. |
| Topology not completed         | Ensure `StartServiceTopologyDiscovery` completed successfully before<br>starting an assessment.             |
| Service error                  | If the assessment fails, check the error message in the<br>`GetFailureModeAssessment` response.             |
