

# AI Inventory in Security Hub
<a name="securityhub-v2-ai-inventory"></a>

 The AI inventory in AWS Security Hub provides a unified view of your artificial intelligence (AI) and machine learning (ML) resources across your AWS environment. Use the AI inventory to identify unsanctioned AI workloads, understand where AI is running and how it was discovered, and prioritize the resources that require closer security review. Security Hub organizes AI resources into two discovery types: 
+  **Managed** – AI resources that AWS provides as a managed service. Security Hub discovers these resources from AWS Config configuration items. Managed resource types include a supported subset of Amazon Bedrock, Amazon Bedrock AgentCore, and Amazon SageMaker. 
+  **Self-hosted** – AI resources that aren't provided as a managed service. Examples include open source models, agents, and inference servers that run on your own compute. Security Hub detects these resources from contributing signals on Amazon Elastic Compute Cloud (Amazon EC2) instances and Amazon Elastic Container Registry (Amazon ECR) images. The signals include Amazon Inspector software bill of materials (SBOM) findings and Amazon GuardDuty DNS activity. 

 Administrator accounts can view AI resources from all enabled accounts in their organization. Member accounts can view only the AI resources within their own account. 

## Prerequisites for self-hosted AI discovery
<a name="securityhub-v2-ai-inventory-prerequisites"></a>

 Discovery of managed AI resources requires no additional configuration beyond enabling Security Hub. To discover self-hosted AI resources, you must also enable the AWS services that provide the contributing signals: 
+  **Amazon Inspector** – Enable Amazon Inspector (with Security Hub essentials) to generate SBOMs. Security Hub uses these SBOMs to detect self-hosted models, inference endpoints, and agents. For Amazon EC2 instances, enable agent-based scanning with enhanced scanning mode, agentless scanning, or hybrid scanning. Agent-based scanning without enhanced scanning mode doesn't produce the deep software inventory that AI resource detection requires. For Amazon ECR images, Amazon Inspector provides SBOMs through container image scanning. 
+  **Amazon GuardDuty** – Enable GuardDuty so that Security Hub can use DNS activity to detect external AI endpoints that your Amazon EC2 instances call. 

## Supported AI resource types
<a name="securityhub-v2-ai-inventory-supported-resources"></a>

 At general availability, Security Hub supports the following self-hosted AI resource types. Security Hub uses a confidence-based detection system for self-hosted AI resources. Each detection is anchored to a primary signal, such as an SBOM component. Security Hub then correlates additional signals to establish confidence before a resource appears in your inventory. Security Hub shows only the resources that meet the confidence threshold, which helps minimize false positives. Each resource uses a `ResourceType` with the `SelfHosted::AI::` prefix. 
+  **Models** (`SelfHosted::AI::Model`) – Hugging Face and Ollama models. Security Hub detects models only in the default model-cache directories (such as the Hugging Face and Ollama caches) and in custom paths that you configure for Amazon Inspector scanning. 
+  **Inference endpoints** (`SelfHosted::AI::InferenceEndpoint`) – Supported model-serving software, such as vLLM, Ollama, TorchServe, Triton, Text Generation Inference (TGI), SGLang, llama.cpp, LocalAI, BentoML, Xinference, Ray Serve, and GPT4All. 
+  **Agents** (`SelfHosted::AI::Agent`) – OpenClaw agents. 
+  **External endpoints** (`SelfHosted::AI::ExternalEndpoint`) – External AI service domains that your Amazon EC2 instances call. Security Hub maintains an allow list of known AI service domains, such as OpenAI, Anthropic, Cohere, Mistral, and other major AI providers, and detects when your instances make DNS requests to them. External endpoints are detected from GuardDuty DNS activity on Amazon EC2 only. 

 Managed AI resources are a supported subset of Amazon Bedrock, Amazon Bedrock AgentCore, and Amazon SageMaker configuration item types, each with the `AI/ML` resource category. 

## Finding AI resources from the Resources page
<a name="securityhub-v2-ai-inventory-resources-page"></a>

 The **Resources** page lists all of the resources in your environment. For AI resources, you can use the following capabilities to identify AI workloads and the hosts that run them: 
+  Managed AI/ML resources display an AI icon next to the resource. Choose the icon to view a description. 
+  Host resources that run self-hosted AI resources, such as Amazon EC2 instances, display a self-hosted AI count badge. Hosts with no self-hosted AI resources don't display a badge. 
+  Use the quick filter toggle to show only the hosts that contain self-hosted AI resources. 
+  To drill down into a host, choose the host to open its detail panel, choose the **AI assets** tab, and then choose **View all** to see the self-hosted AI resources detected on that host. 

## Using the AI inventory page
<a name="securityhub-v2-ai-inventory-page"></a>

 The AI inventory page focuses on the AI resources in your organization. Every resource on this page belongs to the `AI/ML` resource category. This page shows managed AWS AI resources and self-hosted AI resources in your environment. The following sections describe the main components of the page. 

### Summary bar
<a name="securityhub-v2-ai-inventory-page-summary-bar"></a>

 The summary bar displays the total number of AI assets and a breakdown by discovery type, either self-hosted or managed. It also displays a breakdown by sub-category, such as model or agent. Choose the value for a statistic to display the supporting details in the table. 

### Grouping, filtering, and searching
<a name="securityhub-v2-ai-inventory-page-grouping"></a>

 The AI inventory table groups resources by resource type by default. You can modify the grouping or remove it for a flat view of all resources. Available grouping fields include canonical ID, host resource type, discovery type, account ID, and resource type. 

 The canonical ID identifies what a resource is, independent of where it runs. For example, two Amazon EC2 instances that run the same Hugging Face model share the same canonical ID, so that you can find all deployments of a specific model across your organization. 

**Note**  
 The canonical ID and host resource type groupings apply only to self-hosted resources. When you group by these fields, managed AI resources don't appear in the results because they don't have these attributes. Use the discovery type or resource type groupings to see both managed and self-hosted resources together. 

 **Quick filters** enable filtering by resource sub-category or discovery type. **Property filters** support additional fields, including host resource type and canonical ID for self-hosted resources. 

### Resource detail and contributing signals
<a name="securityhub-v2-ai-inventory-page-detail"></a>

 Choose a resource row to open the detail panel. For managed resources, the panel displays the resource configuration as JSON. For self-hosted resources, the panel displays the contributing signals that Security Hub used to detect the resource. These signals include the detection source and individual signal details, such as the SBOM components and supporting inference software for a model, or the DNS domain for an external endpoint. 

### Rolling up to the host resource
<a name="securityhub-v2-ai-inventory-page-rollup"></a>

 For a self-hosted AI resource, the detail panel displays the host resource where Security Hub detected the resource. To see all of the self-hosted AI resources on the same host, filter the table by the host resource. With this view, you can drill up from an individual self-hosted resource to its host and review the adjacent AI resources on that host. 

## Considerations
<a name="securityhub-v2-ai-inventory-limitations"></a>

 The AI inventory has the following limitations at general availability: 
+  Self-hosted AI resources don't have findings in this release. Security Hub shows finding counts for managed AI resources only. 
+  Self-hosted AI detection is supported on Amazon EC2 instances and Amazon ECR images only. AWS Lambda functions and other compute types aren't supported. 
+  Security Hub doesn't attribute Amazon ECR images to a parent host in this release, so the host AI counts don't include them. 
+  Security Hub detects external endpoints from GuardDuty DNS activity on Amazon EC2 only. In this release, Security Hub doesn't attribute calls from AWS Fargate, AWS Lambda, Amazon SageMaker, Amazon EKS, or other service-managed compute. 

## Accessing the AI inventory with the API
<a name="securityhub-v2-ai-inventory-api"></a>

 You can retrieve AI inventory data programmatically with the [GetResourcesV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetResourcesV2.html) and [GetResourcesStatisticsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetResourcesStatisticsV2.html) operations. 

 For AI/ML resources, the `GetResourcesV2` response includes the `ResourceSubCategory` and `DiscoveryType` fields. The `DiscoveryType` field indicates whether a resource is `Managed` or `SelfHosted`. For self-hosted AI resources and their host resources, the response also includes `ResourceInfo` with an `AIDetails` structure. 

 Self-hosted AI resources use a `ResourceType` with the `SelfHosted::AI::` prefix. Supported types include the following: 
+ `SelfHosted::AI::Model`
+ `SelfHosted::AI::Agent`
+ `SelfHosted::AI::InferenceEndpoint`
+ `SelfHosted::AI::ExternalEndpoint`

 The `AIDetails` structure links a self-hosted AI resource to its host with the `HostResourceGuid` and `HostResourceType` fields. The `CanonicalId` field identifies what a resource is, independent of where it's deployed, so that you can aggregate identical resources across multiple hosts. The canonical ID uses a `type/identifier` format: 
+  For ML models: `model/<purl>` (for example, `model/pkg:huggingface/meta-llama/llama-3-8b`) 
+  For inference endpoints and agents: a `type/asset-identifier-name` format 
+  For external endpoints: the normalized domain (for example, `api.*.openai.com`) 

 On a host resource, such as an Amazon EC2 instance, the `SelfHostedAI*ResourceCount` fields and the `SelfHostedTotalAIResourceCount` field contain the counts of the self-hosted AI resources detected on the host. 

**Note**  
 When you use `GetResourcesV2` and filter by `ResourceSubCategory`, you must also include a `ResourceCategory` filter. Set the comparison to `EQUALS` and the value to `AI/ML`. This requirement also applies when you group by `ResourceSubCategory`, `ResourceInfo.AIDetails.HostResourceType`, or `ResourceInfo.AIDetails.CanonicalId` in `GetResourcesStatisticsV2`. Otherwise, the operation returns a `ValidationException`.   
 The following example shows a valid filter combination:   

```
{
    "Filters": {
        "CompositeFilters": [
            {
                "Operator": "AND",
                "StringFilters": [
                    {
                        "FieldName": "ResourceCategory",
                        "Filter": {
                            "Comparison": "EQUALS",
                            "Value": "AI/ML"
                        }
                    },
                    {
                        "FieldName": "ResourceSubCategory",
                        "Filter": {
                            "Comparison": "EQUALS",
                            "Value": "Model"
                        }
                    }
                ]
            }
        ]
    }
}
```