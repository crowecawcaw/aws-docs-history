

# Private optimization APIs for Connect Customer forecasting, capacity planning, and scheduling
<a name="optimization-apis"></a>

Connect Customer forecasting, capacity planning, and scheduling uses the following private API resources as actions in its IAM policy:
+ `connect:BatchAssociateAnalyticsDataSet`. Grants access permissions and associates the specified datasets for the specified Connect Customer instance with the specified AWS account.
+ `connect:BatchDisassociateAnalyticsDataSet`. Revokes access permissions and disassociates the specified datasets for the specified Connect Customer instance with the specified AWS account.

If you remove these actions from the preview role policy, the forecasting, capacity planning, and scheduling features won't work.