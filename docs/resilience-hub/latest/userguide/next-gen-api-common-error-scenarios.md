

# Common error scenarios
<a name="next-gen-api-common-error-scenarios"></a>


| Scenario | Error | Resolution | 
| --- | --- | --- | 
| Starting assessment without topology | ConflictException | Run StartServiceTopologyDiscovery first. | 
| Starting assessment while one is running | ConflictException | Wait for the current assessment to complete. | 
| Deleting system with services | ConflictException | Remove all service associations first. | 
| Cross-account access without role | AccessDeniedException | Configure cross-account roles or enable Organizations. | 
| Exceeding 5 cross-account roles | ServiceQuotaExceededException | Use AWS Organizations for larger deployments. | 