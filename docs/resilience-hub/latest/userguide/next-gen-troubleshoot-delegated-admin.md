

# Delegated administrator setup errors
<a name="next-gen-troubleshoot-delegated-admin"></a>


| Error | Cause | Resolution | 
| --- | --- | --- | 
| `AWSOrganizationsNotInUseException` | Organizations not enabled | Enable AWS Organizations with all features. | 
| `AccountNotRegisteredException` | Account is not a member of the organization | Verify account membership. | 
| `ConstraintViolationException` | Service trust not enabled | Run enable-aws-service-access first. | 