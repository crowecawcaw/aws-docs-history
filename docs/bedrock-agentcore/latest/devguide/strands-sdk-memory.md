# Strands Agents SDK

Use the [Strands Agents](https://strandsagents.com/latest/ "https://strandsagents.com/latest/") SDK for
seamless integration with agent frameworks, providing automatic memory management
and retrieval within conversational agents.

**Install dependencies**

```
pip install bedrock-agentcore
pip install strands-agents
```

**Add short-term memory**

```
from datetime import datetime
from strands import Agent
from bedrock_agentcore.memory import MemoryClient
from bedrock_agentcore.memory.integrations.strands.config import AgentCoreMemoryConfig, RetrievalConfig
from bedrock_agentcore.memory.integrations.strands.session_manager import AgentCoreMemorySessionManager

client = MemoryClient(region_name="us-east-1")
basic_memory = client.create_memory(
    name="BasicTestMemory",
    description="Basic memory for testing short-term functionality"
)

MEM_ID = basic_memory.get('id')
ACTOR_ID = "actor_id_test_%s" % datetime.now().strftime("%Y%m%d%H%M%S")
SESSION_ID = "testing_session_id_%s" % datetime.now().strftime("%Y%m%d%H%M%S")

# Configure memory
agentcore_memory_config = AgentCoreMemoryConfig(
    memory_id=MEM_ID,
    session_id=SESSION_ID,
    actor_id=ACTOR_ID
)

# Create session manager
session_manager = AgentCoreMemorySessionManager(
    agentcore_memory_config=agentcore_memory_config,
    region_name="us-east-1"
)

# Create agent
agent = Agent(
    system_prompt="You are a helpful assistant. Use all you know about the user to provide helpful responses.",
    session_manager=session_manager,
)

agent("I like sushi with tuna")
# Agent remembers this preference

agent("I like pizza")
# Agent acknowledges both preferences

agent("What should I buy for lunch today?")
# Agent suggests options based on remembered preferences
```

**Add long-term memory with strategies**

```
from bedrock_agentcore.memory import MemoryClient
from strands import Agent
from bedrock_agentcore.memory.integrations.strands.config import AgentCoreMemoryConfig, RetrievalConfig
from bedrock_agentcore.memory.integrations.strands.session_manager import AgentCoreMemorySessionManager
from datetime import datetime

# Create comprehensive memory with all built-in strategies
client = MemoryClient(region_name="us-east-1")
comprehensive_memory = client.create_memory_and_wait(
    name="ComprehensiveAgentMemory",
    description="Full-featured memory with all built-in strategies",
    strategies=[
        {
            "summaryMemoryStrategy": {
                "name": "SessionSummarizer",
                "namespaces": ["/summaries/{actorId}/{sessionId}"]
            }
        },
        {
            "userPreferenceMemoryStrategy": {
                "name": "PreferenceLearner",
                "namespaces": ["/preferences/{actorId}"]
            }
        },
        {
            "semanticMemoryStrategy": {
                "name": "FactExtractor",
                "namespaces": ["/facts/{actorId}"]
            }
        }
    ]
)

MEM_ID = comprehensive_memory.get('id')
ACTOR_ID = "actor_id_test_%s" % datetime.now().strftime("%Y%m%d%H%M%S")
SESSION_ID = "testing_session_id_%s" % datetime.now().strftime("%Y%m%d%H%M%S")

# Configure memory
agentcore_memory_config = AgentCoreMemoryConfig(
    memory_id=MEM_ID,
    session_id=SESSION_ID,
    actor_id=ACTOR_ID
)

# Create session manager
session_manager = AgentCoreMemorySessionManager(
    agentcore_memory_config=agentcore_memory_config,
    region_name="us-east-1"
)

# Create agent
agent = Agent(
    system_prompt="You are a helpful assistant. Use all you know about the user to provide helpful responses.",
    session_manager=session_manager,
)

agent("I like sushi with tuna")
# Agent remembers this preference

agent("I like pizza")
# Agent acknowledges both preferences

agent("What should I buy for lunch today?")
# Agent suggests options based on remembered preferences
```

More examples are available on GitHub: [https://github.com/aws/bedrock-agentcore-sdk-python/tree/main/src/bedrock_agentcore/memory/integrations/strands](https://github.com/aws/bedrock-agentcore-sdk-python/tree/main/src/bedrock_agentcore/memory/integrations/strands "https://github.com/aws/bedrock-agentcore-sdk-python/tree/main/src/bedrock_agentcore/memory/integrations/strands")
