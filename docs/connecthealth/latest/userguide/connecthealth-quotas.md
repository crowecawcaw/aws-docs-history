# Quotas for Amazon Connect Health

Amazon Connect Health enforces service quotas that govern how AI agents operate within your deployment. These include limits for agent invocation rates, the number of conversation turns per session, and the number of tokens processed per turn. These quotas are designed to ensure service stability and consistent performance across all customers.

If your operational scale requires higher limits — for example, health systems with high concurrent call volumes — you can submit limit increase requests through AWS Support.

In addition to Amazon Connect Health quotas, you are also subject to the default [service quotas of Amazon Connect](../../../connect/latest/adminguide/amazon-connect-service-limits.md "../../../connect/latest/adminguide/amazon-connect-service-limits.md"). If you are deploying at scale, review and request increases for Amazon Connect service quotas as needed.

## Service quotas

The following quotas apply to Amazon Connect Health resources.

| Quota name                      | Default | Adjustable | Description                                                                            |
| ------------------------------- | ------- | ---------- | -------------------------------------------------------------------------------------- |
| Concurrent streaming sessions   | 10      | Yes        | The maximum number of concurrent streaming sessions for Ambient Streaming per account. |
| Concurrent Patient Insight jobs | 25      | Yes        | The maximum number of concurrent Patient Insight jobs per domain.                      |
| Domains per account             | 10      | No         | The maximum number of domains per account.                                             |

## API throttling quotas

The following table lists the default API throttling quotas for Amazon Connect Health, measured in transactions per second (TPS) per account and AWS Region.

| Quota name                           | Default | Adjustable | Description                                                                     |
| ------------------------------------ | ------- | ---------- | ------------------------------------------------------------------------------- |
| `StartMedicalScribeListeningSession` | 2       | Yes        | The maximum number of `StartMedicalScribeListeningSession` requests per second. |
| `GetMedicalScribeListeningSession`   | 10      | Yes        | The maximum number of `GetMedicalScribeListeningSession` requests per second.   |
| `StartPatientInsightsJob`            | 5       | Yes        | The maximum number of `StartPatientInsightsJob` requests per second.            |
| `GetPatientInsightsJob`              | 10      | Yes        | The maximum number of `GetPatientInsightsJob` requests per second.              |
| `ListDomain`                         | 5       | Yes        | The maximum number of `ListDomain` requests per second.                         |
| `GetDomain`                          | 5       | Yes        | The maximum number of `GetDomain` requests per second.                          |
| `CreateDomain`                       | 1       | Yes        | The maximum number of `CreateDomain` requests per second.                       |
| `DeleteDomain`                       | 1       | Yes        | The maximum number of `DeleteDomain` requests per second.                       |
| `CreateSubscription`                 | 1       | Yes        | The maximum number of `CreateSubscription` requests per second.                 |
| `GetSubscription`                    | 5       | Yes        | The maximum number of `GetSubscription` requests per second.                    |
| `ListSubscriptions`                  | 5       | Yes        | The maximum number of `ListSubscriptions` requests per second.                  |
| `ActivateSubscription`               | 1       | Yes        | The maximum number of `ActivateSubscription` requests per second.               |
| `DeactivateSubscription`             | 1       | Yes        | The maximum number of `DeactivateSubscription` requests per second.             |
