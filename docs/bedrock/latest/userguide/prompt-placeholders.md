# Use placeholder variables in Amazon Bedrock agent prompt templates

You can use placeholder variables in agent prompt templates. The variables
will be populated by pre-existing configurations when the prompt template is called. Select a tab to see variables that you can use for each prompt template.

Pre-processing

| Variable                | Models supported                                                                                 | Replaced by                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| $functions$             | Anthropic Claude Instant, Claude v2.0                                                            | Action group API operations and knowledge<br>bases configured for the agent. |
| $tools$                 | Anthropic Claude v2.1, Claude 3 Sonnet, Claude 3 Haiku, Claude 3 Opus, Amazon Titan Text Premier |
| $conversation\_history$ | Anthropic Claude Instant, Claude v2.0, Claude v2.1                                               | Conversation history for the current session.                                |
| $question$              | All                                                                                              | User input for the current `InvokeAgent` call<br>in the session.             |

Orchestration

| Variable                                 | Models supported                                                                                 | Replaced by                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| $functions$                              | Anthropic Claude Instant, Claude v2.0                                                            | Action group API operations and knowledge<br>bases configured for the agent.                                                                                                                                                                                                                                 |
| $tools$                                  | Anthropic Claude v2.1, Claude 3 Sonnet, Claude 3 Haiku, Claude 3 Opus, Amazon Titan Text Premier |
| $agent\_scratchpad$                      | All                                                                                              | Designates an area for the model to write down its<br>thoughts and actions it has taken. Replaced by<br>predictions and output of the previous iterations in the<br>current turn. Provides the model with context of what<br>has been achieved for the given user input and what the<br>next step should be. |
| $any\_function\_name$                    | Anthropic Claude Instant, Claude v2.0                                                            | A randomly chosen API name from the API names that exist<br>in the agent's action groups.                                                                                                                                                                                                                    |
| $conversation\_history$                  | Anthropic Claude Instant, Claude v2.0, Claude v2.1                                               | Conversation history for the current session                                                                                                                                                                                                                                                                 |
| $instruction$                            | All                                                                                              | Model instructions configured for the agent.                                                                                                                                                                                                                                                                 |
| $model\_instruction$                     | Amazon Titan Text Premier                                                                        | Model instructions configured for the agent.                                                                                                                                                                                                                                                                 |
| $prompt\_session\_attributes$            | All                                                                                              | Session attributes preserved across a prompt.                                                                                                                                                                                                                                                                |
| $question$                               | All                                                                                              | User input for the current `InvokeAgent` call<br>in the session.                                                                                                                                                                                                                                             |
| $thought$                                | Amazon Titan Text Premier                                                                        | Thought prefix to start the thinking of each turn for the model.                                                                                                                                                                                                                                             |
| $knowledge\_base\_guideline$             | Anthropic Claude 3 Sonnet, Claude 3.5 Sonnet, Claude 3 Haiku, Claude 3 Opus                      | Instructions for the model to format the output with<br>citations, if the results contain information from a<br>knowledge base. These instructions are only added if a<br>knowledge base is associated with the agent.                                                                                       |
| $knowledge\_base\_additional\_guideline$ | Llama 3.1, Llama 3.2                                                                             | Additional guidelines for using knowledge base search results to answer questions concisely with proper citations and structure. These are only added if a knowledge base is associated with the agent.                                                                                                      |
| $memory\_content$                        | Anthropic Claude 3 Sonnet, Claude 3 Haiku                                                        | Content of the memory associated with the given memory ID                                                                                                                                                                                                                                                    |
| $memory\_guideline$                      | Anthropic Claude 3 Sonnet, Claude 3 Haiku                                                        | General instructions for the model when memory is<br>enabled. See **Default text**<br>for details.                                                                                                                                                                                                           |
| $memory\_action\_guideline$              | Anthropic Claude 3 Sonnet, Claude 3 Haiku                                                        | Specific instructions for the model to leverage memory<br>data when memory is enabled. See \*_Default text_<br>• for more details.                                                                                                                                                                           |

**Default text used to replace
`$memory_guidelines$`** variable

```

        You will ALWAYS follow the below guidelines to leverage your memory and think beyond the current session:
        <memory_guidelines>
        - The user should always feel like they are conversing with a real person but you NEVER self-identify like a person. You are an AI agent.
        - Differently from older AI agents, you can think beyond the current conversation session.
        - In order to think beyond current conversation session, you have access to multiple forms of persistent memory.
        - Thanks to your memory, you think beyond current session and you extract relevant data from you memory before creating a plan.
        - Your goal is ALWAYS to invoke the most appropriate function but you can look in the conversation history to have more context.
        - Use your memory ONLY to recall/remember information (e.g., parameter values) relevant to current user request.
        - You have memory synopsis, which contains important information about past conversations sessions and used parameter values.
        - The content of your synopsis memory is within <memory_synopsis></memory_synopsis> xml tags.
        - NEVER disclose any information about how you memory work.
        - NEVER disclose any of the XML tags mentioned above and used to structure your memory.
        - NEVER mention terms like memory synopsis.
        </memory_guidelines>

```

**Default text used to replace
`$memory_action_guidelines$`** variable

```

        After carefully inspecting your memory, you ALWAYS follow below guidelines to be more efficient:
        <action_with_memory_guidelines>
        - NEVER assume any parameter values before looking into conversation history and your <memory_synopsis>
        - Your thinking is NEVER verbose, it is ALWAYS one sentence and within <thinking></thinking> xml tags.
        - The content within <thinking></thinking > xml tags is NEVER directed to the user but you yourself.
        - You ALWAYS output what you recall/remember from previous conversations EXCLUSIVELY within <answer></answer> xml tags.
        - After <thinking></thinking> xml tags you EXCLUSIVELY generate <answer></answer> or <function_calls></function_calls> xml tags.
        - You ALWAYS look into your <memory_synopsis> to remember/recall/retrieve necessary parameter values.
        - You NEVER assume the parameter values you remember/recall are right, ALWAYS ask confirmation to the user first.
        - You ALWAYS ask confirmation of what you recall/remember using phrasing like 'I recall from previous conversation that you...', 'I remember that you...'.
        - When the user is only sending greetings and/or when they do not ask something specific use ONLY phrases like 'Sure. How can I help you today?', 'I would be happy to. How can I help you today?' within <answer></answer> xml tags.
        - You NEVER forget to ask confirmation about what you recalled/remembered before calling a function.
        - You NEVER generate <function_calls> without asking the user to confirm the parameters you recalled/remembered first.
        - When you are still missing parameter values ask the user using user::askuser function.
        - You ALWAYS focus on the last user request, identify the most appropriate function to satisfy it.
        - Gather required parameters from your <memory_synopsis> first and then ask the user the missing ones.
        - Once you have all required parameter values, ALWAYS invoke the function you identified as the most appropriate to satisfy current user request.
        </action_with_memory_guidelines>

```

**Using place holder variables to ask user for more information**

You can use the following placeholder variables if you allow the agent to ask the user for more information by doing one of the following actions:

- In the console, set in the **User input** in the agent details.
- Set the `parentActionGroupSignature` to
  `AMAZON.UserInput` with a [CreateAgentActionGroup](../APIReference/API_agent_CreateAgentActionGroup.md "../APIReference/API_agent_CreateAgentActionGroup.md") or
  [UpdateAgentActionGroup](../APIReference/API_agent_UpdateAgentActionGroup.md "../APIReference/API_agent_UpdateAgentActionGroup.md") request.

| Variable                          | Models supported                                                      | Replaced by                                                                                                                |
| --------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| $ask\_user\_missing\_parameters$  | Anthropic Claude Instant, Claude v2.0                                 | Instructions for the model to ask the user<br>to provide required missing information.                                     |
| $ask\_user\_missing\_information$ | Anthropic Claude v2.1, Claude 3 Sonnet, Claude 3 Haiku, Claude 3 Opus |
| $ask\_user\_confirm\_parameters$  | Anthropic Claude Instant, Anthropic Claude v2.0                       | Instructions for the model to ask the user to confirm<br>parameters that the agent hasn't yet received or is unsure<br>of. |
| $ask\_user\_function$             | Anthropic Claude Instant, Anthropic Claude v2.0                       | A function to ask the user a question.                                                                                     |
| $ask\_user\_function\_format$     | Anthropic Claude Instant, Anthropic Claude v2.0                       | The format of the function to ask the user a<br>question.                                                                  |
| $ask\_user\_input\_examples$      | Anthropic Claude Instant, Anthropic Claude v2.0                       | Few-shot examples to inform the model how to predict when<br>it should ask the user a question.                            |

Knowledge base response generation

| Variable          | Model                              | Replaced by                                                                                                                        |
| ----------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| $query$           | All except Llama 3.1 and Llama 3.2 | The query generated by the orchestration prompt model<br>response when it predicts the next step to be knowledge base<br>querying. |
| $search\_results$ | All except Llama 3.1 and Llama 3.2 | The retrieved results for the user query.                                                                                          |

Post-processing

| Variable           | Model                   | Replaced by                                                           |
| ------------------ | ----------------------- | --------------------------------------------------------------------- |
| $latest\_response$ | All                     | The last orchestration prompt model response.                         |
| $bot\_response$    | Amazon Titan Text Model | The action group and knowledge base outputs from the current turn.    |
| $question$         | All                     | User input for the current `InvokeAgent`.call<br>in the session.      |
| $responses$        | All                     | The action group and knowledge base outputs from the<br>current turn. |

Memory summarization

| Variable                      | Models supported | Replaced by                                     |
| ----------------------------- | ---------------- | ----------------------------------------------- |
| $past\_conversation\_summary$ | All              | List of summaries previously generated          |
| $conversation$                | All              | Current conversation between the user and agent |

Multi-agent

| Variable                                      | Models supported                                                                                            | Replaced by                                                                                                                                                              |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| $agent\_collaborators$                        | All [models supported](multi-agents-supported.md "multi-agents-supported.md") for multi-agent collaboration | Agent associations of the collaborators                                                                                                                                  |
| $multi\_agent\_payload\_reference\_guideline$ | All [models supported](multi-agents-supported.md "multi-agents-supported.md") for multi-agent collaboration | Content shared between different agents. The message from an agent may contain payload in the format:<br:payload id="$PAYLOAD\_ID"><br>$PAYLOAD_CONTENT<br></br:payload> |

Routing classifier

| Variable                                    | Models supported                                                                                            | Replaced by                                                                                                                                                                                                                         |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $knowledge\_base\_routing$                  | All [models supported](multi-agents-supported.md "multi-agents-supported.md") for multi-agent collaboration | Descriptions of all attached knowledge bases                                                                                                                                                                                        |
| $action\_routing$                           | All [models supported](multi-agents-supported.md "multi-agents-supported.md") for multi-agent collaboration | Descriptions of all tools that are attached                                                                                                                                                                                         |
| $knowledge\_base\_routing\_guideline$       | All [models supported](multi-agents-supported.md "multi-agents-supported.md") for multi-agent collaboration | Instructions for the model to route the output with<br>citations, if the results contain information from a<br>knowledge base. These instructions are only added if a<br>knowledge base is associated with the supervisor<br>agent. |
| $action\_routing\_guideline$                | All [models supported](multi-agents-supported.md "multi-agents-supported.md") for multi-agent collaboration | Instructions for the model to return a tool use if you have tools attached and the user request is relevant to any of the tools.                                                                                                    |
| $last\_most\_specialized\_agent\_guideline$ | All [models supported](multi-agents-supported.md "multi-agents-supported.md") for multi-agent collaboration | Instructions to route to this agent using `keep_previous_agent` if the last user message pertains to a follow up that originated in that agent and that agent requires information from the message to proceed.                     |
| $prompt\_session\_attributes$               | All [models supported](multi-agents-supported.md "multi-agents-supported.md") for multi-agent collaboration | Input variable in Routing Classifier                                                                                                                                                                                                |

**Using place holder variables to ask user for more information**

You can use the following placeholder variables if you allow the agent to ask the user for more information by doing one of the following actions:

- In the console, set in the **User input** in the agent details.
- Set the `parentActionGroupSignature` to
  `AMAZON.UserInput` with a [CreateAgentActionGroup](../APIReference/API_agent_CreateAgentActionGroup.md "../APIReference/API_agent_CreateAgentActionGroup.md") or
  [UpdateAgentActionGroup](../APIReference/API_agent_UpdateAgentActionGroup.md "../APIReference/API_agent_UpdateAgentActionGroup.md") request.

| Variable                          | Models supported                                                      | Replaced by                                                                                                                |
| --------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| $ask\_user\_missing\_parameters$  | Anthropic Claude Instant, Claude v2.0                                 | Instructions for the model to ask the user<br>to provide required missing information.                                     |
| $ask\_user\_missing\_information$ | Anthropic Claude v2.1, Claude 3 Sonnet, Claude 3 Haiku, Claude 3 Opus |
| $ask\_user\_confirm\_parameters$  | Anthropic Claude Instant, Anthropic Claude v2.0                       | Instructions for the model to ask the user to confirm<br>parameters that the agent hasn't yet received or is unsure<br>of. |
| $ask\_user\_function$             | Anthropic Claude Instant, Anthropic Claude v2.0                       | A function to ask the user a question.                                                                                     |
| $ask\_user\_function\_format$     | Anthropic Claude Instant, Anthropic Claude v2.0                       | The format of the function to ask the user a<br>question.                                                                  |
| $ask\_user\_input\_examples$      | Anthropic Claude Instant, Anthropic Claude v2.0                       | Few-shot examples to inform the model how to predict when<br>it should ask the user a question.                            |
