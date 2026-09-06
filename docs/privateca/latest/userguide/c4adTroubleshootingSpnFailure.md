

# Troubleshoot Connector for AD SPN creation failure
<a name="c4adTroubleshootingSpnFailure"></a>

Service principal name (SPN) creation can fail for various reasons. When SPN creation fails you'll receive the failure reason in the API response. If you're using the console, then the failure reason is displayed in the Connector details page under the **Additional status details** field within the **Service principal name (SPN)** container. The following table describes failure reasons and recommended steps for resolution.


| Failure status | Description | Remediation | 
| --- | --- | --- | 
| DIRECTORY\_ACCESS\_DENIED | Connector for AD can't access your directory. | Grant Connector for AD access to your directory. For an example IAM policy that includes permissions that grant directory access, see [Step 4: Create IAM Policy](connector-for-ad-getting-started-prerequisites.md#prereq-iam). | 
| DIRECTORY\_NOT\_REACHABLE | Connector for AD can't access your directory. | Check the network between AWS and your directory, and try creating an SPN again. | 
| DIRECTORY\_RESOURCE\_NOT\_FOUND | Connector for AD can't find the specified directory. | Make sure you specify the correct directory ID, then delete the failed connector and create a new one using your intended directory ID. | 
| INTERNAL\_FAILURE | Connector for AD experienced an internal failure. | Try again later. | 
| SPN\_EXISTS\_ON\_DIFFERENT\_AD\_OBJECT | The service principal name (SPN) exists on a different Active Directory object. | Delete the SPN from the Active Directory object, and try creating the SPN again. | 
| SPN\_LIMIT\_EXCEEDED | Connector for AD can't create the SPN because you've reached the limit of SPNs per directory. The maximum number of SPNs per directory is 10. | Delete one or more SPNs from your account, and try creating the SPN again. | 