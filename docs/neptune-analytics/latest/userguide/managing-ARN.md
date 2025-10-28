# Working with ARNs in Neptune Analytics graph

You can get the ARN of a Neptune Analytics graph resource by using the AWS Management Console or the AWS CLI.

**Console:**

1. For Graphs: Go to your graph page in the Neptune console and look for the “Resource ARN” field.
2. For graph snapshots: Go to your graph page in the Neptune console and look for the "Snapshot ARN" field.
   **AWS CLI**

To get an ARN from the AWS CLI for a particular Neptune Analytics graph resource, you use the `get` command for that
resource. The following table shows each AWS CLI command, and the ARN property used with the command to get an ARN.

| Resource      | AWS CLI command                                                                                                                                             | ARN property |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Graph         | [get-graph](../../../cli/latest/reference/neptune-graph/get-graph.md "../../../cli/latest/reference/neptune-graph/get-graph.md")                            | arn          |
| GraphSnapshot | [get-graph-snapshot](../../../cli/latest/reference/neptune-graph/get-graph-snapshot.md "../../../cli/latest/reference/neptune-graph/get-graph-snapshot.md") | arn          | As an example, running the following command: `aws neptune-graph get-graph --graph-id g-vgebxfyat7 --query "arn"` would return `"arn:aws:neptune-graph:us-east-1:123456789012:graph/g-vgebxfyat7"`. |
