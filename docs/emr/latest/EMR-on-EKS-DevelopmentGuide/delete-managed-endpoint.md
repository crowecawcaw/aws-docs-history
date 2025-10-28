# Delete an interactive endpoint

To delete an interactive endpoint associated with an Amazon EMR on EKS virtual cluster, use the
`delete-managed-endpoint` AWS CLI command. When you delete an interactive
endpoint, Amazon EMR on EKS removes the default security groups that were created for that
endpoint.

Specify values for the following parameters to the command:

- **‐‐id:** The identifier of the interactive
  endpoint that you want to delete.
- **‐‐virtual-cluster-id** – The identifier of
  the virtual cluster associated with the interactive endpoint that you want to delete.
  This is the same virtual cluster ID that was specified when the interactive endpoint was
  created.

```
aws emr-containers delete-managed-endpoint ‐‐id `managed-endpoint-id` ‐‐virtual-cluster-id `virtual-cluster-id`
```

The command returns output similar to the following to confirm that you deleted the
interactive endpoint:

```
{
    "id":"8gai4l4exxxxx",
    "virtualClusterId":"0b0qvauoy3ch1nqodxxxxxxxx"
}
```
