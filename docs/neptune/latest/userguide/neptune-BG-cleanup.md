# Cleaning up after the Neptune Blue/Green solution has completed

After you have promoted the staging (green) cluster to production, clean up the
resources created by the Neptune Blue/Green solution:

- Delete the Amazon EC2 instance that was created to run the solution.
- Delete the AWS CloudFormation templates for the [Neptune
  streams-based replication](streams-consumer-setup.md "streams-consumer-setup.md") that kept the green cluster in sync with the
  blue cluster. The main one has the stack name that you provided earlier, and one
  is composed of the deployment ID followd by "-replication": that is,
  ``(DeploymentID)`-replication`.
  Deleting AWS CloudFormation templates doesn't delete the clusters themselves. Once you have
  verified that the green cluster is working as expected, you can optionally take
  a snapshot before manually deleting the blue cluster.
