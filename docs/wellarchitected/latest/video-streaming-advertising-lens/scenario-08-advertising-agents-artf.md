

# Scenario 8: Implementation of advertising agents with IAB Tech Labs Agentic RTB Framework (ARTF)
<a name="scenario-08-advertising-agents-artf"></a>

 The Agentic Real-Time Bidding Framework (ARTF), published by IAB Tech Lab, defines a containerized execution model for real-time bidding. Third-party agent services run as OCI-compliant containers within the host provider's infrastructure, communicating through gRPC with Protocol Buffers. Agents propose mutations to the bidstream through OpenRTB Patch responses tagged with declared intents. The host controls which mutations to apply. This model targets approximately 80% latency reduction compared to traditional server-to-server integrations. 

## Characteristics
<a name="s08-characteristics"></a>
+  Third-party agents need to participate directly in the RTB bidstream within the host provider's infrastructure boundary. 
+  Agents must operate within sub-millisecond to single-digit millisecond response budgets to meet auction deadlines. 
+  The host controls which agent mutations are applied. Agents propose, hosts decide, and this separation provides security isolation. 
+  No external network access is permitted. Agents operate entirely within the host's VPC boundary. 
+  Agents declare intents (ACTIVATE\_DEALS, BID\_SHADE, ADD\_METRICS, and ADJUST\_DEAL\_FLOOR) describing proposed mutations. 
+  Both ECS/EKS container deployments and Amazon Bedrock AgentCore as a managed alternative are supported. 

## Reference architecture
<a name="s08-reference-architecture"></a><a name="scenario-08-fig1"></a>

![ARTF agent deployment architecture on AWS showing the layered architecture within the host provider's VPC, with the auction engine, agent orchestration, ARTF agent fleet, data/ML layer, observability, and security layers, plus Amazon Bedrock AgentCore as a managed alternative](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-08-artf-agent-deployment.jpg)


 The architecture consists of the following components: 

1.  **Auction Engine**: Receives bid requests through ALB/NLB. Forwards context to the Agent Orchestrator through gRPC/protobuf. Returns the final bid with applied mutations after the Mutation Policy Engine validates and resolves agent proposals. 

1.  **Agent Orchestrator**: Determines applicable agents from the intent registry. Invokes relevant agents in parallel. Collects OpenRTB Patch responses with declared intents and confidence scores. Manages per-agent gRPC connection pools. 

1.  **ARTF Agent Fleet (Amazon ECS/EKS)**: OCI-compliant agent containers deployed on Amazon ECS on Fargate (moderate volume) or EKS (Kubernetes management, high volume). Each agent type in its own ECS service or EKS deployment with independent Auto Scaling policies. Agents have no external network access. All connectivity is within the VPC. 

1.  **Mutation Policy Engine**: Validates agent intents, resolves conflicts between competing agent proposals, enforces per-agent limits (for example, maximum bid shade percentage). Applies approved mutations to the bidstream before returning to the Auction Engine. 

1.  **Data and ML Layer**: Amazon ElastiCache (same Availability Zone as agents) for sub-millisecond cache reads. Amazon SageMaker AI for embedded model inference through a sidecar pattern. DynamoDB for agent configuration and intent registry. 

1.  **Observability Layer**: Amazon CloudWatch for per-agent metrics (invocation counts, mutation acceptance rate, model inference latency). AWS X-Ray for distributed tracing across the full bid cycle. Amazon OpenSearch Service for structured log analysis. 

1.  **Security Layer**: Amazon GuardDuty for threat detection. AWS Security Hub for centralized security findings. AWS WAF for bid request validation. Mutual TLS between orchestrator and agents using AWS Certificate Manager. 

1.  **Amazon Bedrock AgentCore (managed alternative)**: Provides serverless runtime, memory persistence, Cedar policy enforcement, MCP gateway, observability, and agent-to-agent communication as a managed layer. Reduces the operational complexity of managing the Agent Orchestration and ARTF Agent Fleet layers. Suitable for teams preferring managed infrastructure over self-managed containers. 

## Configuration notes
<a name="s08-configuration-notes"></a>

### Container optimization
<a name="container-optimization"></a>

 Build minimal container images from distroless or scratch base images. Production images contain only the compiled binary and model artifacts. Pre-allocate memory pools at startup for protobuf message buffers, inference tensors, and intermediate data structures. Load ML model weights at container startup and run warm-up inference passes before the gRPC server accepts traffic. Compile ML models to ONNX Runtime format for microsecond-to-low-millisecond inference. 

### gRPC performance
<a name="grpc-performance"></a>

 Configure the Agent Orchestrator to maintain persistent HTTP/2 connection pools to agent containers (2–4 connections per container per high-volume agent type). This avoids per-request TLS handshake overhead. Set per-adapter timeout budgets at 80% of the overall auction timeout, leaving 20% for orchestration and response assembly. Configure gRPC deadline propagation so agents return no-bid immediately when remaining time is insufficient. 

### Hybrid deployment
<a name="hybrid-deployment"></a>

 Start with 1–5% of bid traffic routed through ARTF agents using feature flags. Monitor bid response latency, agent mutation acceptance rate, and revenue impact against the control group. Increase ARTF traffic share as validation confirms latency and revenue targets are met. Use AWS CodeDeploy or feature flag services for gradual rollout. 

### Agent security
<a name="agent-security"></a>

 Implement mutual TLS between the Agent Orchestrator and all agent containers using certificates from AWS Certificate Manager. Configure VPC security groups to deny all outbound internet access from agent subnets. Agents communicate only with services inside the VPC. Use IAM task roles (ECS) or IRSA (EKS) for least-privilege access to AWS services. Validate ads.txt and sellers.json authorization in the Agent Identity Service. 

### AgentCore deployment path
<a name="agentcore-deployment-path"></a>

 For teams preferring managed infrastructure, deploy ARTF agents using Amazon Bedrock AgentCore Runtime. AgentCore handles session routing, scaling, and lifecycle management. AgentCore Policy (Cedar) maps directly to the ARTF mutation policy model. AgentCore's separation of capability (agent logic) from enforcement (policy/gateway) mirrors the ARTF architecture, making it a natural fit for ARTF agent deployments. 