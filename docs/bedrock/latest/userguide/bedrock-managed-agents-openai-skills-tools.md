

# Add skills and tools
<a name="bedrock-managed-agents-openai-skills-tools"></a>

Skills provide reusable instructions. Tools perform operations. BMA reads skills from the execution environment and can connect to MCP servers that run in that environment.

## Add a skill
<a name="bedrock-managed-agents-openai-skills-tools-add-a-skill"></a>

A skill is a directory containing a `SKILL.md` file. Place skill directories under a path listed in the session's `environment.capability_directories`.

For the self-hosted example, create a skill in your workspace:

```
mkdir -p "$BMA_WORKSPACE_DIRECTORY/skills/hello-docs"
cat > "$BMA_WORKSPACE_DIRECTORY/skills/hello-docs/SKILL.md" <<'EOF'
---
name: hello-docs
description: Verify the documentation example in this workspace.
---

When asked to run hello-docs, write the text BMA_DOCS_VERIFIED to
verified.txt in the current workspace, read it back, and return that text.
EOF
```

The revised example defaults its capability directory to `$BMA_WORKSPACE_DIRECTORY/skills`. Create the session after making the skill available, attach the exec server, then submit:

```
./scripts/bma/2.submit-turn.sh "Run the hello-docs skill."
./scripts/bma/3.read-result.sh
```

Confirm that `verified.txt` contains `BMA_DOCS_VERIFIED` and that the returned items report a successful command.

Skills are filesystem content; S3 is not a required source. You can include skill files in a container image, mount them from storage, or place them on a host. The skill's commands and dependencies must exist in the environment where it runs. A portable file format does not guarantee that a skill's instructions will work unchanged on every host or model.

## Skills on AgentCore Runtime
<a name="bedrock-managed-agents-openai-skills-tools-skills-on-agentcore-runtime"></a>

The AgentCore example seeds the bundle's `acr/skills/` directory into the skills bucket. S3 Files mounts it at `/mnt/bma/skills`, and the adapter copies it to `/mnt/workspace/skills` for capability discovery.

Skills are filesystem content; S3 is not a required source. See [File system configurations for AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html) for more options.

## Add a STDIO MCP server
<a name="bedrock-managed-agents-openai-skills-tools-add-a-stdio-mcp-server"></a>

The example bundle includes a read-only Python MCP server, `mcp/word_count.py`. Its `word_count` tool counts words in supplied text. It uses only the Python standard library.

From `self-hosted/`, configure the server before creating a new session:

```
export BMA_MCP_LABEL=word_tools
export BMA_MCP_COMMAND="$(command -v python3)"
export BMA_MCP_CWD="$BMA_WORKSPACE_DIRECTORY"
MCP_SCRIPT="$(cd ../mcp && pwd)/word_count.py"
export BMA_MCP_ARGS_JSON="$(jq -cn --arg script "$MCP_SCRIPT" '[$script]')"
export BMA_MCP_ALLOWED_TOOLS_JSON='["word_count"]'
export BMA_STATE_FILE="$PWD/scripts/bma/.mcp-session.env"

./scripts/bma/0.create-session.sh
```

In a second terminal, set the same `BMA_STATE_FILE`, select your BMA client profile, and attach the exec server. Then submit:

```
./scripts/bma/2.submit-turn.sh \
  'Use the word_count MCP tool to count the words in "Bedrock agents execute tasks". Return the tool result.'
./scripts/bma/3.read-result.sh
```

Inspect the MCP-call item and confirm a word count of `4`. Delete the session and stop its exec server when finished.

For AgentCore Runtime, the MCP executable and any dependencies must be present in the container image. Use absolute container paths for `command`, `args`, and `cwd`; a path on your deployment machine is not available inside the Runtime.

## Configure multiple servers
<a name="bedrock-managed-agents-openai-skills-tools-configure-multiple-servers"></a>

Set `BMA_MCP_SERVERS_JSON` to an array of server definitions. For example:

```
[
  {
    "server_label": "my_server",
    "transport": {
      "type": "stdio",
      "command": "/opt/tools/my-server",
      "args": [],
      "cwd": "/mnt/workspace",
      "env": {},
      "env_vars": []
    },
    "allowed_tools": ["lookup_record"]
  }
]
```

Server labels must be unique. `env` supplies explicit environment values, and `env_vars` names variables to inherit from the execution environment. Forward only the variables required by the tool. Avoid placing credentials in configuration values that might be stored with the session or printed in logs.

Use `allowed_tools` to expose only the tools needed for the task. MCP tool names and input schemas come from the server. Validate model-generated arguments in the tool implementation, and enforce authorization before accessing external resources.

## Memory and files
<a name="bedrock-managed-agents-openai-skills-tools-memory-and-files"></a>

The session conversation provides context across turns. The execution environment can also use files as a working area. These mechanisms do not automatically create a long-term memory system shared across sessions. The preview does not provide a built-in long-term memory integration; provision and authorize any application-specific datastore separately.

Subagents and programmatic tool calling (code mode) are not supported in this preview. Do not enable them in a session configuration.