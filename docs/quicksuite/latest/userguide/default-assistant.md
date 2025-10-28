# System chat agent

The Amazon Quick Suite system chat agent is automatically created when you sign up for
Quick Suite. It serves as the primary interface for all users to interact with
their data and perform various tasks within the Quick Suite environment. It comes
equipped with default guardrails.

Ownership of the system chat agent is managed by the Quick Suite admin. Admins
can disable chatting with chat agents including the system chat agent using [custom permissions](create-custom-permisions-profile.md "create-custom-permisions-profile.md"). If enabled, users with non-admin
roles (authors and readers) can view, list, invoke, and use the Quick Suite chat
chat agent. Its responses are filtered based on user permissions to assets.

The Quick Suite system chat agent is set to use all chat features out of the box
with minimal customization required. While these features are also available to custom
chat agents, they must be configured during chat agent creation. The system chat agent
includes:

- Default persona as the Quick Suite assistant, with professional tone and
  response style
- File upload in chat capability enabled
- Large language model (LLM) knowledge chat enabled
- Uses default guardrails configured for chat in admin console
- Access to all spaces, topics, dashboards, knowledge bases, and actions based
  on user permissions
- Web search capabilities
  To learn how to customize a system chat agent as an Admin owner, see [Managing
  chat agent customization](manage-agent.md "manage-agent.md"). To learn how to control access to the system chat
  chat agent, see [Manage assets](manage-qs-assets.md "manage-qs-assets.md").
