

# Embed chat agents (legacy)

Embedding applies to legacy chat agents only. This page describes how to embed a legacy custom chat agent so that people can use it outside of AWS Quick.

## Embed custom chat agents
<a name="embed-custom-agents"></a>

You can embed a legacy custom chat agent in an external website or application so that people can interact with it outside of AWS Quick. To embed a chat agent, you must first allow the hosting domain in the AWS Quick admin settings, and then generate the embed code from the chat agent's share options.

Embedding a chat agent involves two steps:

1. **Allow the hosting domain** – A AWS Quick admin must add the domain (and optionally its subdomains) where the embedded chat agent will be hosted to the domain allow list.

1. **Generate the embed code** – The chat agent owner or an authorized user generates the embed code from the chat agent's share options.

### Allow a domain for embedded chat agents
<a name="embed-agents-allow-domain"></a>

Before you can embed a chat agent on an external website, a AWS Quick admin must add the hosting domain to the allow list. You must be a AWS Quick admin to complete this procedure. This ensures that only approved domains can host embedded chat agents.

**To allow a domain for embedding**

1. Open AWS Quick.

1. Choose the profile icon.

1. Choose **Manage account**.

1. In the navigation pane under **Security**, choose **Manage domains**.

1. In the **Domain** field, enter the domain name where you want to host the embedded chat agent (for example, `https://example.com`).

1. (Optional) Select **Include subdomains** to allow embedded chat agents on all subdomains of the specified domain.

1. Choose **Add**.

The domain now appears in the list of allowed domains. You can edit or delete existing domains by choosing the edit or delete icons next to each domain in the list.

### Generate the embed code for a chat agent
<a name="embed-agents-generate-code"></a>

After you allow the hosting domain, you can generate the embed code for a chat agent.

**To generate the embed code for a chat agent**

1. Open AWS Quick.

1. From the navigation pane, choose **Chat agents**.

1. From the **Actions** column for the chat agent you want to embed, choose the menu icon, and then choose **Edit**.

1. In the chat agent editor, choose **Share**.

1. In the share options, choose **Share via embed**.

1. Copy the provided embed code and paste it into the HTML of your website or application where you want the chat agent to appear.

The embedded chat agent is now available on your website. People who visit the page can interact with the chat agent directly.