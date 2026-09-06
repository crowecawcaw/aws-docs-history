

# Input sources
<a name="next-gen-api-input-sources-actions"></a>


| Action | Method | Description | 
| --- | --- | --- | 
| CreateInputSource | POST | Configure a resource discovery source (resource tags, CloudFormation stack, Terraform state file, EKS cluster, or design file). For a single tag-based input source with multiple tags, the service discovers only resources that match all specified tags. For multiple tag-based input sources, the service discovers resources that match any of them. | 
| ListInputSources | GET | List input sources for a service. | 
| DeleteInputSource | POST | Delete an input source. | 