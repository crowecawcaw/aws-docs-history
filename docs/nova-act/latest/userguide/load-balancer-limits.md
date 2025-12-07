# Quotas for Nova Act

Your AWS account has default quotas, formerly referred to as limits, for each AWS service. You can request increases for some quotas, while other quotas cannot be increased. To request a quota increase, contact AWS support.

To maintain the performance of the service and to ensure appropriate usage of Nova Act, the default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota increase request.

To view service quotas for Nova Act, do one of the following:

- Follow the steps at [Viewing service quotas](../../../servicequotas/latest/userguide/gs-request-quota.md "../../../servicequotas/latest/userguide/gs-request-quota.md") and select **Amazon Nova Act** as the service.
- Refer to **Amazon Nova Act service quotas** in the [AWS General Reference](../../../general/latest/gr/Welcome.md "../../../general/latest/gr/Welcome.md").

## Adjustable Quotas

### Control Plane API Quotas

The following table describes the Control Plane API quotas for Nova Act:

| API                      | Default Limit | Scope   | Adjustable |
| ------------------------ | ------------- | ------- | ---------- |
| CreateWorkflowDefinition | 100 TPS       | Account | Yes        |
| DeleteWorkflowDefinition | 100 TPS       | Account | Yes        |
| DeleteWorkflowRun        | 100 TPS       | Account | Yes        |
| GetWorkflowDefinition    | 100 TPS       | Account | Yes        |
| ListWorkflowDefinitions  | 100 TPS       | Account | Yes        |
| GetWorkflowRun           | 100 TPS       | Account | Yes        |
| ListWorkflowRuns         | 100 TPS       | Account | Yes        |
| ListActs                 | 100 TPS       | Account | Yes        |
| ListModels               | 100 TPS       | Account | Yes        |
| ListSessions             | 100 TPS       | Account | Yes        |

### Data Plane API Quotas

The following table describes the Data Plane API quotas for Nova Act:

| API               | Default Limit | Scope   | Adjustable |
| ----------------- | ------------- | ------- | ---------- |
| CreateWorkflowRun | 100 TPS       | Account | Yes        |
| CreateSession     | 100 TPS       | Account | Yes        |
| CreateAct         | 100 TPS       | Account | Yes        |
| InvokeActStep     | 5 TPS         | Account | Yes        |
| UpdateAct         | 100 TPS       | Account | Yes        |
| UpdateWorkflowRun | 100 TPS       | Account | Yes        |

### Resource Count Quotas

The following table describes the Resource Count quotas for Nova Act:

| Resource             | Default Limit | Scope   | Adjustable |
| -------------------- | ------------- | ------- | ---------- |
| Workflow Definitions | 100K          | Account | Yes        |

## Non-Adjustable Quotas

The following table describes the non-adjustable quotas for Nova Act:

| Limit                      | Limit    | Scope   | Adjustable |
| -------------------------- | -------- | ------- | ---------- |
| Steps per Act              | 200      | Session | No         |
| InvokeActStep Payload Size | 5 mb     | Account | No         |
| Workflow Run Timeout       | 1 Week   | Account | No         |
| Act Timeout                | 24 hours | Account | No         |
| Tool Spec Payload Size     | 350 kb   | Account | No         |
| Tools per Act              | 100      | Account | No         |
