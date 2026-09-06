

# Common permission error codes and resolution
<a name="next-gen-troubleshoot-error-codes"></a>

The following table lists common permission error codes and their recommended resolution.


| Error | Cause | Resolution | 
| --- | --- | --- | 
| `AccessDeniedException: Unable to assume role` | Invoker role trust policy doesn't include resiliencehub.amazonaws.com | Update the role's trust policy. | 
| `AccessDeniedException: Cross-account role` | Cross-account role trust policy doesn't allow assumption from the invoker role | Verify the trust policy and ExternalId. | 
| `AccessDeniedException: sts:AssumeRole` | Invoker role lacks sts:AssumeRole permission for cross-account roles | Add sts:AssumeRole permission to the invoker role. | 
| `InvalidParameterException: Role does not exist` | Role name in permissionModel doesn't match an existing IAM role | Verify the role name and account. | 