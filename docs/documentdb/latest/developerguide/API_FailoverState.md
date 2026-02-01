# FailoverState

Contains the state of scheduled or in-process operations on an Amazon DocumentDB global cluster.
This data type is empty unless a switchover or failover operation is scheduled or is in progress on the global cluster.

## Contents

###### Note

In the following list, the required parameters are described first.

**FromDbClusterArn**

The Amazon Resource Name (ARN) of the Amazon DocumentDB cluster that is currently being demoted, and which is associated with this state.

Type: String

Required: No

**IsDataLossAllowed**

Indicates whether the operation is a global switchover or a global failover.
If data loss is allowed, then the operation is a global failover. Otherwise, it's a switchover.

Type: Boolean

Required: No

**Status**

The current status of the global cluster. Possible values are as follows:

- **pending** – The service received a request to switch over or fail over the global cluster.
  The global cluster's primary cluster and the specified secondary cluster are being verified before the operation starts.
- **failing-over** – The chosen secondary cluster is being promoted to become the new primary cluster to fail over the global cluster.
- **cancelling** – The request to switch over or fail over the global cluster was cancelled and the primary cluster and the selected secondary cluster are returning to their previous states.

Type: String

Valid Values: `pending | failing-over | cancelling`

Required: No

**ToDbClusterArn**

The Amazon Resource Name (ARN) of the Amazon DocumentDB cluster that is currently being promoted, and which is associated with this state.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/FailoverState.md "../../../goto/SdkForCpp/docdb-2014-10-31/FailoverState.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/FailoverState.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/FailoverState.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/FailoverState.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/FailoverState.md")
