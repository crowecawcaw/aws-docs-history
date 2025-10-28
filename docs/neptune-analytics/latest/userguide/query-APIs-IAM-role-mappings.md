# IAM role mappings

When you're calling Neptune Analytics API methods on a cluster, you require an IAM policy attached to the user or role making
the calls that provides permissions for the actions you want to make. You set those permissions in the policy using
corresponding IAM actions. You can also restrict the actions that can be taken using [IAM condition keys](../../../neptune/latest/userguide/iam-data-condition-keys.md "../../../neptune/latest/userguide/iam-data-condition-keys.md").

Most IAM actions have the same name as the API methods that they correspond to, but some methods in the data API
have different names, because some are shared by more than one method. The table below lists data methods and their
corresponding IAM actions.

| Data API operation name | IAM correspondences                                                           |
| ----------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ListQueries             | Action: ListQueries                                                           |
| GetQuery                | Action: GetQueryStatus                                                        |
| Cancel Query            | Action: CancelQuery                                                           |
| GetGraphSummary         | Action: GetGraphSummary                                                       |
| ExecuteQuery            | Action: ReadDataViaQuery Action: WriteDataViaQuery Action: DeleteDataViaQuery | For more information, see [Actions, resources and condition keys for Neptune Analytics](../../../service-authorization/latest/reference/list_amazonneptuneanalytics.md "../../../service-authorization/latest/reference/list_amazonneptuneanalytics.md"). |
