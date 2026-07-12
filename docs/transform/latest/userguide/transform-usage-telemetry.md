# Usage Telemetry

The AWS Transform IDE plugin, AWS Transform Agent Skill, and AWS Transform Kiro Power collect usage telemetry by default during transformation execution. The telemetry consists of different data points, such as, the IDE name (for example, VS Code or Kiro), the AI agent name (for example, Claude Code or OpenAI Codex), and the execution mode (local or remote). This data is used by AWS Transform to prioritize compatibility testing, as well as latency and reliability.

To disable telemetry, tell the agent during your chat session that you do not want telemetry emitted. This opt-out applies only to the current chat session and must be repeated for each new session. If you are running the AWS Transform CLI directly, set the `ATX_DISABLE_TELEMETRY=true` environment variable.
