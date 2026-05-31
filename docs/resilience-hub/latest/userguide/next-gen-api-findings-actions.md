# Failure mode findings

| Action                     | Method | Description                                                                               |
| -------------------------- | ------ | ----------------------------------------------------------------------------------------- |
| `GetFailureModeFinding`    | GET    | Retrieve failure mode finding details including AI-generated<br>recommendations.          |
| `UpdateFailureModeFinding` | POST   | Update failure mode finding status (resolved, irrelevant) and add comments.               |
| `ListFailureModeFindings`  | GET    | List failure mode findings, filterable by `severity`,<br>`failureCategory`, and `status`. |
