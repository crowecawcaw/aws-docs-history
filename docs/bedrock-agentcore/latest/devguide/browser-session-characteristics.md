# Session management

The AgentCore Browser sessions have the following characteristics:

Session timeout

Default: 900 seconds (15 minutes)

Configurable: Can be adjusted when creating sessions, up to 8 hours

Session recording

Browser sessions can be recorded for later review

Recordings include network traffic and console logs

Recordings are stored in an S3 bucket specified during browser creation

Live view

Sessions can be viewed in real-time using the live view feature

Live view is available at:
/browser-streams/aws.browser.v1/sessions/{session_id}/live-view

Automatic termination

Sessions automatically terminate after the configured timeout period

Multiple sessions

Multiple sessions can be active simultaneously for a single browser tool. Each
session maintains its own state and environment. There can be up to a maximum of 500
sessions.

Retention policy

The time to live (TTL) retention policy for the session data is 30 days.

## Using isolated sessions

AgentCore Tools enable isolation of each user session to ensure secure and
consistent reuse of context across multiple tool invocations. Session isolation is
especially important for AI agent workloads due to their dynamic and multi-step execution
patterns.

Each tool session runs in a dedicated microVM with isolated CPU, memory, and
filesystem resources. This architecture guarantees that one user's tool invocation cannot
access data from another user's session. Upon session completion, the microVM is fully
terminated, and its memory is sanitized, thereby eliminating any risk of cross-session
data leakage.
