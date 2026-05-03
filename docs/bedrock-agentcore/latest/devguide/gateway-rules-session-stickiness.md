# Session stickiness for weighted rules

When you use weighted rules for A/B testing or canary deployments, you want each session to receive a consistent experience across multiple requests. Without session stickiness, a session could receive different configuration bundles or route to different targets on each request. Routing to a different target means a new agent runtime with no context from previous requests, which breaks the user experience.

To solve this, the gateway supports session stickiness. When you include a session ID in your requests, the gateway stores the routing decision from the first request and reuses it for all subsequent requests in the same session.

## How session stickiness works

The gateway uses the `X-Amzn-Bedrock-AgentCore-Runtime-Session-Id` header to identify sessions. The header value must be a minimum of 33 characters.

You do not need to send this header on the first request. If the header is absent, the agent runtime auto-generates a session ID. The gateway uses that auto-generated session ID for stickiness on subsequent requests if you include it.

The stickiness flow works as follows:

1. On the first request with a session ID, the gateway selects a variant based on the configured weights and stores the decision.
2. Subsequent requests with the same session ID reuse the stored decision without re-evaluating weights.
3. Requests without a session ID are evaluated independently with no stickiness.

## Important behaviors

**Stored decisions take precedence over rule changes.** If you update a rule, existing sessions continue with the original decision. This ensures session consistency. To apply new rules to a session, start a new session with a new session ID.

**Sessions expire after 15 days of inactivity.** The expiration window resets on each request (sliding window). After a session expires, use a new session ID for new sessions to avoid unexpected routing behavior. We recommend that you do not reuse expired session IDs.

**Session state is scoped per target.** Different targets maintain independent session state.

**Supported for HTTP proxy targets only.** Session stickiness is not supported for MCP targets.
