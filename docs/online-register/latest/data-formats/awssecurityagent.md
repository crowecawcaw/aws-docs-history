

# Data retrieval APIs for AWS Security Agent
<a name="awssecurityagent"></a>

AWS Security Agent provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="securityagent-BatchGetAgentSpaces"></a>[BatchGetAgentSpaces](https://docs.aws.amazon.com/securityagent/API_BatchGetAgentSpaces.html) | Retrieve multiple agent spaces in a single request | Read | 
| <a name="securityagent-BatchGetArtifactMetadata"></a>[BatchGetArtifactMetadata](https://docs.aws.amazon.com/securityagent/API_BatchGetArtifactMetadata.html) | Retrieve one or more Artifact Metadata records for the given Agent Space | Read | 
| <a name="securityagent-BatchGetCodeReviewJobTasks"></a>[BatchGetCodeReviewJobTasks](https://docs.aws.amazon.com/securityagent/API_BatchGetCodeReviewJobTasks.html) | Retrieve multiple code review job tasks in a single request | Read | 
| <a name="securityagent-BatchGetCodeReviewJobs"></a>[BatchGetCodeReviewJobs](https://docs.aws.amazon.com/securityagent/API_BatchGetCodeReviewJobs.html) | Retrieve multiple code review jobs in a single request | Read | 
| <a name="securityagent-BatchGetCodeReviews"></a>[BatchGetCodeReviews](https://docs.aws.amazon.com/securityagent/API_BatchGetCodeReviews.html) | Retrieve multiple code reviews in a single request | Read | 
| <a name="securityagent-BatchGetFindings"></a>[BatchGetFindings](https://docs.aws.amazon.com/securityagent/API_BatchGetFindings.html) | Retrieve multiple security testing findings in a single request | Read | 
| <a name="securityagent-BatchGetPentestJobContentMetadata"></a>[BatchGetPentestJobContentMetadata](https://docs.aws.amazon.com/securityagent/API_BatchGetPentestJobContentMetadata.html) | Retrieve multiple pentest job contents metadata in a single request | Read | 
| <a name="securityagent-BatchGetPentestJobTasks"></a>[BatchGetPentestJobTasks](https://docs.aws.amazon.com/securityagent/API_BatchGetPentestJobTasks.html) | Retrieve multiple pentest job tasks in a single request | Read | 
| <a name="securityagent-BatchGetPentestJobs"></a>[BatchGetPentestJobs](https://docs.aws.amazon.com/securityagent/API_BatchGetPentestJobs.html) | Retrieve multiple security testing jobs in a single request | Read | 
| <a name="securityagent-BatchGetPentests"></a>[BatchGetPentests](https://docs.aws.amazon.com/securityagent/API_BatchGetPentests.html) | Retrieve multiple penetration tests in a single request | Read | 
| <a name="securityagent-BatchGetSecurityRequirements"></a>[BatchGetSecurityRequirements](https://docs.aws.amazon.com/securityagent/API_BatchGetSecurityRequirements.html) | Retrieve multiple security requirements in a single request | Read | 
| <a name="securityagent-BatchGetTargetDomains"></a>[BatchGetTargetDomains](https://docs.aws.amazon.com/securityagent/API_BatchGetTargetDomains.html) | Retrieve multiple target domains in a single request | Read | 
| <a name="securityagent-BatchGetThreatModelJobTasks"></a>[BatchGetThreatModelJobTasks](https://docs.aws.amazon.com/securityagent/API_BatchGetThreatModelJobTasks.html) | Retrieve multiple tasks for a threat model job in a single request | Read | 
| <a name="securityagent-BatchGetThreatModelJobs"></a>[BatchGetThreatModelJobs](https://docs.aws.amazon.com/securityagent/API_BatchGetThreatModelJobs.html) | Retrieve details for one or more threat model jobs | Read | 
| <a name="securityagent-BatchGetThreatModels"></a>[BatchGetThreatModels](https://docs.aws.amazon.com/securityagent/API_BatchGetThreatModels.html) | Retrieve multiple threat models in a single request | Read | 
| <a name="securityagent-BatchGetThreats"></a>[BatchGetThreats](https://docs.aws.amazon.com/securityagent/API_BatchGetThreats.html) | Retrieve details for one or more threats | Read | 
| <a name="securityagent-DescribePrivateConnection"></a>[DescribePrivateConnection](https://docs.aws.amazon.com/securityagent/API_DescribePrivateConnection.html) | Describe a private connection | Read | 
| <a name="securityagent-GetApplication"></a>[GetApplication](https://docs.aws.amazon.com/securityagent/API_GetApplication.html) | Get application details by application ID | Read | 
| <a name="securityagent-GetArtifact"></a>[GetArtifact](https://docs.aws.amazon.com/securityagent/API_GetArtifact.html) | Retrieve an Artifact for the given Agent Space | Read | 
| <a name="securityagent-GetDesignReview"></a>[GetDesignReview](https://docs.aws.amazon.com/securityagent/API_GetDesignReview.html) | Get the status of the associated agent space design review | Read | 
| <a name="securityagent-GetDesignReviewArtifact"></a>[GetDesignReviewArtifact](https://docs.aws.amazon.com/securityagent/API_GetDesignReviewArtifact.html) | Get design review artifact for a specific document | Read | 
| <a name="securityagent-GetDesignReviewFeedback"></a>[GetDesignReviewFeedback](https://docs.aws.amazon.com/securityagent/API_GetDesignReviewFeedback.html) | Get feedback for a design review comment | Read | 
| <a name="securityagent-GetIntegration"></a>[GetIntegration](https://docs.aws.amazon.com/securityagent/API_GetIntegration.html) | Get the integration metadata by ID | Read | 
| <a name="securityagent-GetProviderRegistrationManifest"></a>[GetProviderRegistrationManifest](https://docs.aws.amazon.com/securityagent/API_GetProviderRegistrationManifest.html) | Retrieve the provider registration manifest used for browser-based integration registration | Read | 
| <a name="securityagent-GetSecurityRequirement"></a>[GetSecurityRequirement](https://docs.aws.amazon.com/securityagent/API_GetSecurityRequirement.html) | Retrieve a Security Requirement | Read | 
| <a name="securityagent-GetSecurityRequirementPack"></a>[GetSecurityRequirementPack](https://docs.aws.amazon.com/securityagent/API_GetSecurityRequirementPack.html) | Retrieve a security requirement pack | Read | 
| <a name="securityagent-ListAgentSpaces"></a>[ListAgentSpaces](https://docs.aws.amazon.com/securityagent/API_ListAgentSpaces.html) | List agent spaces | List | 
| <a name="securityagent-ListApplications"></a>[ListApplications](https://docs.aws.amazon.com/securityagent/API_ListApplications.html) | List all applications in the account | List | 
| <a name="securityagent-ListArtifacts"></a>[ListArtifacts](https://docs.aws.amazon.com/securityagent/API_ListArtifacts.html) | List all artifacts for the given agent space | List | 
| <a name="securityagent-ListCodeReviewJobTasks"></a>[ListCodeReviewJobTasks](https://docs.aws.amazon.com/securityagent/API_ListCodeReviewJobTasks.html) | List tasks associated with a code review job | List | 
| <a name="securityagent-ListCodeReviewJobsForCodeReview"></a>[ListCodeReviewJobsForCodeReview](https://docs.aws.amazon.com/securityagent/API_ListCodeReviewJobsForCodeReview.html) | List code review jobs associated with a code review | List | 
| <a name="securityagent-ListCodeReviews"></a>[ListCodeReviews](https://docs.aws.amazon.com/securityagent/API_ListCodeReviews.html) | List code reviews with optional filtering by status | List | 
| <a name="securityagent-ListDesignReviewComments"></a>[ListDesignReviewComments](https://docs.aws.amazon.com/securityagent/API_ListDesignReviewComments.html) | List design review comments | List | 
| <a name="securityagent-ListDesignReviews"></a>[ListDesignReviews](https://docs.aws.amazon.com/securityagent/API_ListDesignReviews.html) | List all design reviews for the given agent space | List | 
| <a name="securityagent-ListDiscoveredEndpoints"></a>[ListDiscoveredEndpoints](https://docs.aws.amazon.com/securityagent/API_ListDiscoveredEndpoints.html) | List discovered endpoints associated with a pentest job with optional URI prefix filtering | List | 
| <a name="securityagent-ListFindings"></a>[ListFindings](https://docs.aws.amazon.com/securityagent/API_ListFindings.html) | List findings with filtering and pagination support | List | 
| <a name="securityagent-ListIntegratedResources"></a>[ListIntegratedResources](https://docs.aws.amazon.com/securityagent/API_ListIntegratedResources.html) | List integrated resources for an agent space | List | 
| <a name="securityagent-ListIntegrations"></a>[ListIntegrations](https://docs.aws.amazon.com/securityagent/API_ListIntegrations.html) | Get the integrations owned by the caller's AWS account | List | 
| <a name="securityagent-ListMemberships"></a>[ListMemberships](https://docs.aws.amazon.com/securityagent/API_ListMemberships.html) | List all members associated to an agent space with pagination support | List | 
| <a name="securityagent-ListPentestJobTasks"></a>[ListPentestJobTasks](https://docs.aws.amazon.com/securityagent/API_ListPentestJobTasks.html) | List pentest job tasks associated with a pentest job | List | 
| <a name="securityagent-ListPentestJobsForPentest"></a>[ListPentestJobsForPentest](https://docs.aws.amazon.com/securityagent/API_ListPentestJobsForPentest.html) | List penetration test jobs associated with a penetration test | List | 
| <a name="securityagent-ListPentests"></a>[ListPentests](https://docs.aws.amazon.com/securityagent/API_ListPentests.html) | List penetration tests with optional filtering by status | List | 
| <a name="securityagent-ListPrivateConnections"></a>[ListPrivateConnections](https://docs.aws.amazon.com/securityagent/API_ListPrivateConnections.html) | List private connections in the account | List | 
| <a name="securityagent-ListResourcesFromIntegration"></a>[ListResourcesFromIntegration](https://docs.aws.amazon.com/securityagent/API_ListResourcesFromIntegration.html) | List resources from Integration | List | 
| <a name="securityagent-ListSecurityRequirementPacks"></a>[ListSecurityRequirementPacks](https://docs.aws.amazon.com/securityagent/API_ListSecurityRequirementPacks.html) | List all security requirement packs in the account | List | 
| <a name="securityagent-ListSecurityRequirements"></a>[ListSecurityRequirements](https://docs.aws.amazon.com/securityagent/API_ListSecurityRequirements.html) | List all Security Requirements | List | 
| <a name="securityagent-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/securityagent/API_ListTagsForResource.html) | List the tags for a resource | Read | 
| <a name="securityagent-ListTargetDomains"></a>[ListTargetDomains](https://docs.aws.amazon.com/securityagent/API_ListTargetDomains.html) | List target domains | List | 
| <a name="securityagent-ListThreatModelJobTasks"></a>[ListThreatModelJobTasks](https://docs.aws.amazon.com/securityagent/API_ListThreatModelJobTasks.html) | List tasks associated with a specific threat model job | List | 
| <a name="securityagent-ListThreatModelJobs"></a>[ListThreatModelJobs](https://docs.aws.amazon.com/securityagent/API_ListThreatModelJobs.html) | List threat model jobs for a threat model | List | 
| <a name="securityagent-ListThreatModels"></a>[ListThreatModels](https://docs.aws.amazon.com/securityagent/API_ListThreatModels.html) | List threat models for an agent space | List | 
| <a name="securityagent-ListThreats"></a>[ListThreats](https://docs.aws.amazon.com/securityagent/API_ListThreats.html) | List threats for a threat model job with filtering and pagination support | List | 