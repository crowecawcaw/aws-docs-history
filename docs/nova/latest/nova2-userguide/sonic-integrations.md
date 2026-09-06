

# Integrations
<a name="sonic-integrations"></a>

Amazon Nova 2 Sonic can be integrated with various frameworks and platforms to build conversational AI applications. These integrations provide pre-built components and simplified APIs for common use cases.

## Strands Agents
<a name="sonic-strands-agents"></a>

Strands Agents is a simple yet powerful SDK that takes a model-driven approach to building and running AI agents. From simple conversational assistants to complex autonomous workflows, from local development to production deployment, Strands Agents scales with your needs.

For comprehensive documentation on the Strands framework, visit the [official Strands documentation](https://strandsagents.com/latest/documentation/docs/user-guide/quickstart/).

The Strands BidiAgent provides real-time audio and text interaction through persistent streaming connections. Unlike traditional request-response patterns, this agent maintains long-running conversations with support for interruptions, concurrent processing and continuous audio responses.

**Prerequisites:**
+ Python 3.8 or later installed
+ Credentials for AWS configured with access to Amazon Bedrock
+ Basic familiarity with Python async/await syntax

**Code example:**

### Code example
<a name="w2aac25c15b5c15b1"></a>

**Installation:**

 Install the required packages:

```
pip install strands-agents strands-agents-tools
```

Run this example:

```
import asyncio
from strands.experimental.bidi.agent import BidiAgent
from strands.experimental.bidi.io.audio import BidiAudioIO
from strands.experimental.bidi.io.text import BidiTextIO
from strands.experimental.bidi.models.novasonic import BidiNovaSonicModel
from strands_tools import calculator

async def main():
    """Test the BidirectionalAgent API."""
    # Audio and Text input/output utility
    audio_io = BidiAudioIO(audio_config={})
    text_io = BidiTextIO()
    
    # Nova Sonic model
    model = BidiNovaSonicModel(region="us-east-1")
    
    async with BidiAgent(model=model, tools=[calculator]) as agent:
        print("New BidiAgent Experience")
        print("Try asking: 'What is 25 times 8?' or 'Calculate the square root of 144'")
        
        await agent.run(
            inputs=[audio_io.input()],
            outputs=[audio_io.output(), text_io.output()]
        )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nConversation ended by user")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
```

### 1. Import: Required Models
<a name="w2aac25c15b5c15b3"></a>

```
from strands.experimental.bidi.agent import BidiAgent 
from strands.experimental.bidi.io.audio import BidiAudioIO 
from strands.experimental.bidi.io.text import BidiTextIO 
from strands.experimental.bidi.models.novasonic import BidiNovaSonicModel 
from strands_tools import calculator
```
+ BidiAgent: The main agent class that orchestrates bidirectional conversations
+ BidiAudioIO: Handles audio input and output for speech interactions
+ BidiTextIO: Provides text output for transcriptions and responses
+ BidiNovaSonicModel The Nova 2 Sonic model wrapper
+ Calculator: A pre-built tool for mathematical operations

### 2. Configure Audio and Text I/O
<a name="w2aac25c15b5c15b5"></a>

```
audio_io = BidiAudioIO(audio_config={}) 
text_io = BidiTextIO()
```

The BidiAudioIO manages microphone input and speaker output, while BidiTextIO displays text transcriptions and responses in the console.

### 3. Initialize the Model
<a name="w2aac25c15b5c15b7"></a>

```
model = BidiNovaSonicModel(region="us-east-1")
```

Create a Nova Sonic model instance. The region parameter specifies the AWS region where the model is deployed.

### 4. Create and Run the Agent
<a name="w2aac25c15b5c15b9"></a>

```
async with BidiAgent(model=model, tools=[calculator]) as agent: 
    await agent.run( 
        inputs=[audio_io.input()],  
        outputs=[audio_io.output(), text_io.output()] 
    )
```

The agent is created with:
+ Model: The Nova 2 Sonic model to use
+ Tools: List of tools the agent can call (like calculator)
+ Inputs: Audio input from the microphone
+ Outputs: Audio output to speakers and text output to console

## Framework integrations
<a name="sonic-framework-integrations"></a>

Amazon Nova 2 Sonic can be integrated with various frameworks and platforms to build sophisticated voice applications. The following examples demonstrate integration patterns with popular frameworks.

### Amazon Bedrock AgentCore
<a name="sonic-agentcore"></a>

Amazon Bedrock AgentCore provides a managed runtime environment for deploying Nova 2 Sonic applictions with enterprise-grade security and scalability. AgentCore simplifies the deployment of real-time voice AI applications by handling infrastructure, authentication, and WebSocket connectivity.

![AgentCore architecture showing client apps connecting via WebSocket to runtime container with Nova Sonic.](http://docs.aws.amazon.com/nova/latest/nova2-userguide/images/Agentcore-Architecture-Overview_11.png)


**Key features:**
+ Bidirectional streaming - Native support for Nova Sonic's full-duplex streaming interface with real-time event processing and low-latency communication.
+ WebSocket infrastructure - Production-ready WebSocket servers with automatic scaling, connection management, and error recovery.
+ Container deployment - Deploy Nova Sonic applications as containers to managed infrastructure with horizontal scaling and independent versioning.
+ Enterprise security - Fine-grained authentication via IAM and SigV4, VPC isolation, and comprehensive audit logging.

The architecture shows how client applications connect to AgentCore Runtime via WebSocket with SigV4 authentication. The containerized environment includes your WebSocket server, application logic, and Nova Sonic client, all communicating with Nova Sonic through the bidirectional streaming API.

**Benefits:**
+ Simplified operations: Focus on application logic while AgentCore manages infrastructure, scaling, and reliability.
+ Enterprise security: Built-in authentication, authorization, and compliance features for production deployments.
+ Cost efficienty: Pay only for what you use with automatic scaling and resource optimization.
+ Developer productivity: Reduce time to production with managed WebSocket infrastructure and container deployment.

**Use cases**
+ Customer service voice assistants with secure authentication
+ Enterprise voice applications requiring IAM integration
+ Multi-tenant voice platforms with isolated deployments
+ Voice-enabled applications requiring compliance and audit trails

For detailed documentation on deploying Nova Sonic with AgentCore, visit the [Amazon Bedrock AgentCore Documentation.](https://aws.amazon.com/bedrock/agentcore/)

### LiveKit
<a name="sonic-livekit"></a>

LiveKit is an open-source platform for building real-time audio and video applications. Integration with Amazon Nova 2 Sonic enables developers to build conversational voice interfaces without managing complex audio pipelines or signaling protocols.

 For detailed implementation examples and code examples, visit the [LiveKit AWS Integration Documentation.](https://docs.livekit.io/agents/integrations/aws/)

![Architecture diagram showing LiveKit integration with Amazon Bedrock using WebRTC and Nova Sonic.](http://docs.aws.amazon.com/nova/latest/nova2-userguide/images/LiveKit-Architecture-Overview_9.png)


**How it works:**
+ Client layer: Web, mobile, or desktop applications connect using LiveKit's client SDKs, which handle audio capture, WebRTC streaming, and playback.
+ LiveKit Server: Acts as the real-time communication hub, managing WebRTC connections, routing audio streams, and handling session state with low-latency optimization.
+ LiveKit Agent: Python-based agent that receives audio from the server, processes it through the Nova Sonic plugin, and streams responses back. Includes built-in features like voice activity detection and turn management.
+ Amazon Nova 2 Sonic: Processes the audio stream through bidirectional streaming API, performing speech recognition, natural language understanding, and generating conversational responses with synthesized speech.

### Pipecat
<a name="sonic-pipecat"></a>

Pipecat is a framework for building voice and multimodal conversational AI applications. It provides a modular, pipeline-based architecture that orchestrates multiple components to create intelligent voice applications with Amazon Nova Sonic and other AWS services.

For detailed implementation examples and code samples, visit the [PipeCat AWS Integration Documentation.](https://docs.pipecat.ai/server/services/s2s/aws)

**Key features:**
+ Pipeline architecture: Modular Python-based framework for composing voice AI components including ASR, NLU, TTS, and more.
+ Pipecat flows: State management framework for building complex conversational logic and tool execution.
+ WebRTC Support: Built-in integration with Daily and other WebRTC providers for real-time audio streaming.
+ AWS Integration: Native support for Amazon Bedrock, Amazon Transcribe, and Amazon Polly.

![Architecture diagram showing voice input flow through VAD, Amazon Transcribe, Pipecat Flows, Amazon Bedrock, and Amazon Polly to voice output via WebRTC.](http://docs.aws.amazon.com/nova/latest/nova2-userguide/images/Pipecat-Architecture-Overview_10.png)


The architecture includes:
+ WebRTC Transport: Real-time audio streaming between client devices and application server.
+ Voice activity detection (VAD): Silero VAD with configurable speech detection and noise suppression.
+ Speech recognition: Amazon Transcribe for accurate, real-time speech-to-text conversion.
+ Natural language understanding: Amazon Nova Pro on Bedrock with latency-optimized inference.
+ Tool execution: Pipecat Flows for API integration and backend service calls.
+ Response generation: Amazon Nova Pro for coherent, context-aware responses.
+ Text-to-speech: Amazon Polly with generative voices for lifelike speech output.

### Deploy on AWS
<a name="sonic-deploy-aws"></a>

Deploy your Nova Sonic applications to AWS using infrastructure as code with AWS CDK (Cloud Development Kit). This approach provides repeatable, version-controlled deployments with best practices built in.

Deployment options
+ Amazon ECS (Elastic Container Service): Fully managed container orchestration with Application Load Balancer integration, auto-scaling, and serverless Fargate execution.
+ Amazon EKS (Elastic Kubernetes Services): Managed Kubernetes for complex orchestration, advanced networking, multi-region deployments, and extensive tooling ecosystem.
+ AWS CDK: AWS CDK allows you to define cloud infrastructure using familiar programming languages.

For a complete, production-ready example of deploying Nova Sonic with AWS CDK, see the [Speech-to-Speech CDK Sample](https://github.com/aws-samples/generative-ai-cdk-constructs-samples/tree/main/samples/speech-to-speech) on GitHub. This sample demonstrates:

![Architecture diagram showing users connecting via HTTPS and WebSocket to static website and speech-to-speech service components, with Amazon Bedrock integration for Nova Sonic.](http://docs.aws.amazon.com/nova/latest/nova2-userguide/images/cdk-12.png)

+ Complete CDK infrastructure setup with TypeScript
+ WebSocket server implementation for real-time communication
+ Container deployment with ECS and Fargate
+ Application Load Balancer configuration for WebSocket support
+ VPC networking and security group setup
+ CloudWatch monitoring and logging
+ Best practices for production deployments

### Multi-agentic systems
<a name="sonic-multi-agent"></a>

Multi-agent architecture is a widely used pattern for designing AI assistants that handle complex tasks. In a voice assistant powered by Nova 2 Sonic, this architecture coordinates multiple specialized agents, where each agent operates independently to enable parallel processing, modular design, and scalable solutions.

Nova Sonic serves as the orchestrator in a multi-agent system, performing two key functions:

Conversation flow management: Ensures all necessary information is collected before proceeding to the next step in the conversation.

Intent classification: Analyzes user inquiries and routes them to the appropriate specialized sub-agent.

![Architecture diagram showing call flow from user through greeting to three agents handling authentication, banking, and mortgage services.](http://docs.aws.amazon.com/nova/latest/nova2-userguide/images/Banking-Assistant_13.png)


The diagram above shows a banking voice assistant that uses a multi-agent architecture. The conversation flow begins with a greeting and collecting the user's name, then handles inquiries related to banking or mortgages through specialized sub-agents.

Conversation flow example:

1. User connects to voice assistant.

1. Nova 2 Sonic: "Hello\! What's your name?"

1. User: "My name is John"

1. Nova 2 Sonic: "Hi John, how can I help you today?"

1. User: "I want to check my account balance"

1. Nova 2 Sonic: [Routes to Authentication Agent]

1. Authentication Agent: "Please provide your account ID"

1. User: "12345"

1. Authentication Agent: [Verifies identity]

1. Nova 2 Sonic: [Routes to Banking Agent]

1. Banking Agent: "Your current balance is $5,431,10"

While this example demonstrates sub-agents using the Strands Agents framework deployed on Amazon Bedrock AgentCore, the architecture is flexible. You can choose:
+ Your preferred agent framework
+ Any LLM provider
+ Custom hosting options
+ Different orchestration patterns

**Benefits:**
+ Modularity: Each agent focuses on a specific domain, making the system easier to maintain and update.
+ Scalability: Add new agents without modifying existing ones, allowing your system to grow with your needs.
+ Parallel processing: Multiple agents can work simultaneously, improving response times for complex queries.
+ Specialization: Each agent can be optimized for its specific task, using the most appropriate tools and knowledge bases.
+ Fault isolation: If one agent fails, others continue to function, improving overall system reliability.

Refer to [this blog](https://aws.amazon.com/blogs/machine-learning/building-a-multi-agent-voice-assistant-with-amazon-nova-sonic-and-amazon-bedrock-agentcore/) for more details and code examples.

See the [Nova Sonic Workshop Multi-Agent Lab](https://catalog.workshops.aws/amazon-nova-sonic-s2s/en-US/02-repeatable-pattern/05-multi-agent-agentcore) for hands-on samples.

### Telephony integration
<a name="sonic-telephony"></a>

Amazon Nova 2 Sonic integrates with telephony providers to enable AI-powered voice applications accessible via phone calls. This guide covers integration with Twilio, Vonage, and other SIP-based systems for building contact center solutions and voice agents.

**Twilio**: Cloud communications platform with programmable voice and media streaming capabilities.

**Vonage**: Global communications APIs with voice, WebSocket audio streaming, and SIP connectivity.

AWS provides a comprehensive sample implementation demonstrating Nova Sonic in a contact center environment with real-time analytics and telephony integration.

Repository: [ Sample Sonic Contact Center with Telephony](https://github.com/aws-samples/sample-sonic-contact-center-with-telephony)