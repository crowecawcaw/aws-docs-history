

# Supported Region Posture
<a name="plan-region-posture"></a>

## Single-region, co-located deployment
<a name="plan-region-single-region"></a>

AVX is a **single-region guidance**. All components — the AVX CDK stacks, AgentCore runtimes, the CMS operational foundation, and the Amazon Connect instance — are co-located in the same AWS region. The Automotive Data Platform (ADP) that AVX reads from is deployed to its own region and reached over cross-account, cross-region Athena and Amazon Bedrock Knowledge Base grants; see the security chapter for the trust and encryption boundaries.

The guidance deploys **staging in US West (Oregon) (`us-west-2`)**. This is the region in which the guidance’s automated deploy, seed, and evaluation pipeline runs; it is where Amazon Nova 2 Sonic voice is invoked natively without cross-region routing. For a second environment, the same constraints apply — voice needs a region where Nova 2 Sonic is available, and the AgentCore runtime execution role must be named per the Bedrock allow-list convention `AmazonBedrockAgentCoreSDKRuntime-{region}-vsa-{stage}`.

**Note**  
For staging or evaluation deployments in other regions, AVX supports a cross-region Nova 2 Sonic configuration: the AgentCore runtime can be deployed outside a Nova-native region and route bidi voice calls to a Nova-native region via an IAM cross-region grant. This adds latency and introduces a cross-region data-transfer cost, and is why staging runs in `us-west-2` natively rather than routing across regions. See the deployment guide for configuration details.

## Voice model regional fallback
<a name="plan-region-voice-fallback"></a>

If Amazon Nova 2 Sonic is unavailable in your target region (or during a regional service event), AVX’s voice path falls back to Amazon Polly (text-to-speech) and Amazon Transcribe (speech-to-text). This fallback preserves voice connectivity at the cost of the turn-by-turn conversational experience that Nova 2 Sonic’s speech-to-speech architecture provides; latency increases and the natural conversational pacing is reduced.

The fallback is configured per deployment in the AgentCore runtime environment variables. The recommended posture is to deploy in a region where Nova 2 Sonic is natively available and treat Polly/Transcribe as the emergency fallback only.

## Multi-region considerations
<a name="plan-region-multi-region-roadmap"></a>

Multi-region active/active deployment of AVX — with regional Connect instances, regional AgentCore runtimes, and data replication — is not implemented in this guidance. The guidance deploys a single-region topology. To extend to active/active multi-region, replicate the CDK stacks per region, co-locate Connect instances with AgentCore runtimes in each region, and add cross-region data replication for DynamoDB and the tenant configuration cache. The same AgentCore execution role naming convention (`AmazonBedrockAgentCoreSDKRuntime-{region}-vsa-{stage}`) must be applied in each target region.