

# Using partner-managed connectors

A partner-managed connector connects AWS DevOps Agent to a *Model Context Protocol (MCP)* server that a partner hosts. Examples include a partner's observability or incident management service. The partner publishes the connector in the [AWS DevOps Agent Tools repository](https://github.com/aws/tools-for-devops-agent) on the GitHub website. The connector defines the server's endpoints and the authentication methods that it accepts. It can also list skills that the partner recommends.

With a connector, you don't need to look up the partner's endpoint URLs, OAuth URLs, or scopes. You choose an endpoint and enter only your own credentials, and AWS DevOps Agent builds the rest of the registration from the connector. Use a connector when the partner publishes one for its MCP server. For instructions on registering any other MCP server, see [Registering an MCP server](configuring-integrations-and-knowledge-connecting-mcp-servers.html#registering-an-mcp-server-account-level).

In this topic, *connector* means the partner's definition, and *MCP server* means the registration that you create from it. The console uses the same terms.

A connector registers an MCP server, so its tools work as they do for an MCP server that you register yourself. A connector also provides the following:
+ **Fixed configuration** – The endpoint URLs, the authentication methods, and the OAuth URLs and scopes come from the connector. You can't change them.
+ **Recommended skills** – You can install the skills that the connector recommends when you add it to an Agent Space. Later, you can install more, turn them on or off, or remove them.
+ **Alert webhook** – When you add the connector to an Agent Space, AWS DevOps Agent creates a webhook so that alerts from the partner's product can start investigations. Some connectors also define the alert payload for you.

## How partner-managed connectors work
<a name="how-partner-managed-connectors-work"></a>

The following list describes who runs a connector's server and where your data goes:
+ **Server operation** – The partner operates and supports the MCP server. AWS doesn't operate it. For help with the server, use the **Support** link for the connector in the console.
+ **Connector maintenance** – Each connector shows a **Partner-managed** or **AWS-managed** badge. The badge names who maintains the connector definition.
+ **Credentials** – Your credentials go only to the URLs in the connector definition.
+ **Requests** – The endpoint that you choose belongs to the partner's region or site for your account with the partner. It can be outside the AWS Region of your Agent Space. As with any MCP server that you connect, requests to the server then leave that AWS Region.

## Registrations and versions
<a name="registrations-and-versions"></a>

The following list describes how a registration relates to Agent Spaces and to connector versions:
+ **Registration scope** – You register a connector in your AWS account, and then add the registration to each Agent Space that needs it. You can register the same connector more than once, as long as each registration has a unique name. The connector's card under **Currently registered** shows the number of registrations, for example **2 registered**.
+ **Versions** – A registration keeps the connector version that you registered. When a partner deprecates a connector, the connector no longer appears in the **Available** section, and you can't register it again. Its card under **Currently registered** shows **Deprecated**, and the page that **View all** opens can name the connector that replaces it. Existing registrations keep working until you deregister them.

## Recommended skills
<a name="recommended-skills"></a>

A recommended skill is a skill that the partner suggests for its connector, such as guidance on using the partner's tools during an investigation. Recommended skills come from the skills catalog in the AWS DevOps Agent Tools repository on the GitHub website. You can install recommended skills when you add the connector to an Agent Space. When you edit the MCP server later, you can install more skills, enable or disable installed skills, or remove them.

An installed recommended skill appears with the other skills in your Agent Space. Its content comes from the catalog, so you can't edit it. The agent loads it in the same way as any other skill. For more information about skills, see [DevOps Agent Skills](about-aws-devops-agent-devops-agent-skills-index.md).

## Before you begin
<a name="before-you-begin"></a>

To use a partner-managed connector, verify that you have the following:
+ An account with the partner that can create the credentials that the connector requires, such as an API key or an OAuth client. The connector's setup guide lists the steps in the partner's product.
+ Permission to register capability providers and to add capabilities to an Agent Space in the AWS DevOps Agent console.
+ (Optional) An existing private connection, if you reach the partner's endpoint through a private network. For more information about private connections, see [Connecting to privately hosted tools](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md).

For more information about the security considerations that apply to any MCP server, such as allowlisting only the tools that you need, see [Security considerations](configuring-integrations-and-knowledge-connecting-mcp-servers.html#security-considerations).

## Finding a connector
<a name="finding-a-connector"></a>

Find a connector to see its setup guide and recommended skills before you register it. You can start on the **Capability Providers** page or from an Agent Space.

### Finding a connector on the Capability Providers page
<a name="finding-a-connector-on-the-capability-providers-page"></a>

To find a connector on the **Capability Providers** page, complete the following steps:

1. Open the AWS DevOps Agent console at [https://console.aws.amazon.com/aidevops/home](https://console.aws.amazon.com/aidevops/home).

1. In the navigation pane, choose **Capability Providers**.

1. In the **Available** section, find the connector. To narrow the list, enter its name in **Find capability**, or filter by category or by tier (**AWS-managed** or **Partner-managed**). Each card shows the connector's badge, description, and categories.

1. Choose the connector's name.

The connector's page opens. To skip it and start the registration, you can choose **Register** on the card instead.

### Finding a connector from an Agent Space
<a name="finding-a-connector-from-an-agent-space"></a>

To find a connector from an Agent Space, complete the following steps:

1. Open the AWS DevOps Agent console at [https://console.aws.amazon.com/aidevops/home](https://console.aws.amazon.com/aidevops/home), and then select your Agent Space.

1. Choose the **Capabilities** tab.

1. In the section for the connector's category, such as **Telemetry**, **Communications**, or **DevOps**, choose **Add**.

1. In **Add a capability**, under **Partner-managed connectors**, choose **Register**.

1. In the list of connectors, choose **Select** for the connector.

The connector's page opens.

### What the connector's page shows
<a name="what-the-connectors-page-shows"></a>

The connector's page shows the following information:
+ The partner, the connector version, and its categories
+ Links to the partner's documentation and support
+ The connector's setup guide
+ The skills that the connector recommends

To start the registration, choose **Register**. For instructions on registering a connector, see [Registering a connector](#registering-a-connector).

## Registering a connector
<a name="registering-a-connector"></a>

When you register a connector, AWS DevOps Agent creates an MCP server registration in your AWS account from the connector definition. The registration has four steps. The console skips the steps that the connector doesn't need.

### Step 1: MCP server details
<a name="step-1-mcp-server-details"></a>

In this step, you name the MCP server and choose where AWS DevOps Agent connects. The step title includes the connector's name, for example **Example Corp MCP server details**.

If the step shows **Setup guide**, expand it before you fill in the form, and complete the partner's steps. They show how to create the credentials that you enter in [Step 3: Authentication configuration](#step-3-authentication-configuration). To keep a copy of the steps, choose **Copy**.

Enter the following information:
+ **Name** – Enter a short name for this MCP server. The console fills in the connector's name, which you can change. Use letters, numbers, hyphens (`-`), and underscores (`_`). The name must be unique in your AWS account. AWS DevOps Agent adds the name to the start of each tool name, and a tool name can have at most 64 characters, so keep the name short.
+ **Endpoint** – Some partners offer more than one endpoint, such as a regional site. If so, choose the endpoint that your account with the partner uses. Otherwise, the console shows the connector's endpoint. The endpoint URL appears in AWS CloudTrail logs in your account.
+ **Connector fields** – Some connectors ask for more values, such as the name of your instance with the partner. Each field shows the label that the connector gives it. Enter the value from your account with the partner.
+ **Connect to endpoint using a private connection** – (Optional) Select this option to route requests to the partner's endpoint through an existing private connection. For a connector that uses OAuth, you can choose a separate private connection for the token exchange.
+ **Advanced configuration** – (Optional) Choose a customer managed AWS Key Management Service (AWS KMS) key to encrypt the registration. For more information about encryption, see [Encryption at rest for DevOps Agent](aws-devops-agent-security-encryption-at-rest-for-devops-agent.md).

Choose **Next**.

### Step 2: Authentication method
<a name="step-2-authentication-method"></a>

In this step, you choose how AWS DevOps Agent authenticates to the partner's product. You see this step only when the connector offers more than one authentication method. The connector defines the order of the methods. Choose one of the following:
+ **API key** – AWS DevOps Agent authenticates with a key that you create in the partner's product, so you control its permissions.
+ **OAuth client credentials** – AWS DevOps Agent authenticates with a client ID and secret that you create in the partner's product.
+ **Sign in to** *partner* (for example, **Sign in to Example Corp**) – AWS DevOps Agent acts on your behalf after you sign in to the partner's product. It uses an OAuth client that the connector provides, or one that you create in the partner's product and enter in the next step.
+ **Sign in with dynamic client registration** – AWS DevOps Agent acts on your behalf after you sign in. It creates its own OAuth client with the partner, so you don't need to create or enter one.

Choose **Next**.

### Step 3: Authentication configuration
<a name="step-3-authentication-configuration"></a>

In this step, you enter the credentials that your authentication method needs. For **OAuth client credentials** and **Sign in to** *partner*, the **Defined by the connector** section lists the OAuth settings from the connector, such as the token URL, authorization URL, and scopes. You can't change them. You enter only your credentials, and any additional scopes or parameters.

The console skips this step for **Sign in with dynamic client registration**. It also skips this step for **Sign in to** *partner* when the connector provides its own OAuth client.

#### API key
<a name="api-key"></a>

For an API key, enter a value for each header that the connector lists. The connector sets the header name and any prefix, such as `Bearer `, so enter only the key.

#### OAuth client credentials
<a name="oauth-client-credentials"></a>

For OAuth client credentials, complete the following steps:

1. Enter the **Client ID** and **Client secret** that you created in the partner's product.

1. (Optional) Add **Additional scopes** and **Additional exchange parameters**. AWS DevOps Agent requests them in addition to the scopes and parameters that the connector defines.

#### Sign in to the partner
<a name="sign-in-to-the-partner"></a>

For **Sign in to** *partner*, complete the following steps:

1. If the connector doesn't provide its own OAuth client, enter the **Client ID** and **Client secret** that you created in the partner's product. If the partner supports Proof Key for Code Exchange (PKCE), you can leave the client secret empty.

1. (Optional) Add **Additional scopes**.

Choose **Next**.

### Step 4: Review and register
<a name="step-4-review-and-register"></a>

To finish the registration, complete the following steps:

1. Review the details. To change a step, choose **Edit** in the section for that step.

1. Choose **Register**.

1. If you chose a sign-in method, sign in on the partner's page that the console opens, and then approve access.

The console returns to AWS DevOps Agent, and the registration is complete. If you registered from an Agent Space, the console then opens the steps to add the connector to that Agent Space. If you registered from the **Capability Providers** page, see [Adding a connector to an Agent Space](#adding-a-connector-to-an-agent-space).

If registration fails, the console stays on the review step and shows the error. Correct the details, and then choose **Register** again.

## Adding a connector to an Agent Space
<a name="adding-a-connector-to-an-agent-space"></a>

When you add a connector to an Agent Space, you choose the tools that agents can use there, and optionally install the connector's recommended skills. If you registered the connector from the **Capability Providers** page, start from your Agent Space:

1. Open the AWS DevOps Agent console at [https://console.aws.amazon.com/aidevops/home](https://console.aws.amazon.com/aidevops/home), and then select your Agent Space.

1. Choose the **Capabilities** tab.

1. In the section for the connector's category, choose **Add**.

1. In **Add a capability**, find the MCP server that you registered from the connector, and then choose **Add**.

### Step 1: Select tools
<a name="step-1-select-tools"></a>

In this step, you choose the tools that the agent can use in this Agent Space. Select only the tools that your Agent Space needs. If you classify tools, choose **Read only**, **Mutative**, or **Destructive** for each tool. A tool with no suggested classification defaults to **Mutative**, which needs approval. If you choose **Destructive**, the console turns the tool off and shows a warning. For more information about classifying tools, see [Working with directed actions](working-with-devops-agent-working-with-directed-actions.md). For more information about the maximum number of MCP tools in an Agent Space, see [Quotas](quotas.md).

Some connectors also show **Webhook authentication type**. Choose how the partner's product authenticates to the Agent Space's alert webhook: **HMAC** (the default) or **API Key**. Connectors that define their own alerts set this for you.

To skip the optional skills step, choose **Skip to Review and save**. Otherwise, choose **Next**.

### Step 2: Select recommended skills (optional)
<a name="step-2-select-recommended-skills-optional"></a>

You see this step only when the connector recommends skills. In this step, you choose the recommended skills to install. The console lists the skills that the connector recommends, with none selected. A skill that is already installed in the Agent Space shows **Enabled** or **Disabled**, and you can't select it. Select the skills that you want to install, and then choose **Next**.

### Step 3: Review and save
<a name="step-3-review-and-save"></a>

To save the connector to the Agent Space, complete the following steps:

1. Review the tools, the skills, and the **Alert webhook** type. To change them, choose **Edit** in their section.

1. Choose **Save**.

AWS DevOps Agent adds the MCP server to the Agent Space, and then installs the skills that you selected. If a skill fails to install, a notification lists it, and the MCP server stays in the Agent Space. To try again, edit the connector in the Agent Space, and then select the skill. For instructions on editing a connector, see [Editing a connector in an Agent Space](#editing-a-connector-in-an-agent-space).

### Setting up the alert webhook
<a name="setting-up-the-alert-webhook"></a>

After you choose **Save**, the console opens **Set up alert webhook**. It opens each time that you add the connector to an Agent Space, but not when you edit the connector. After you set up the webhook, each alert sent to it starts an investigation in the Agent Space.

To set up the webhook, complete the following steps:

1. Copy the **Webhook URL**, the **Header** or **Signing secret**, and the **Request body** or **Request body format**. AWS DevOps Agent shows the secret only once.

1. (Optional) To save the URL and the secret in a file, choose **Download .csv file**.

1. Select **I've saved and stored my URL and credentials**, and then choose **Done**.

1. Set up the webhook in the partner's product. For instructions on setting up the webhook, see the connector's setup guide.

The values work as follows:
+ **Webhook URL** – The URL that the partner's product sends alerts to.
+ **Header** – For a webhook that uses a bearer token, the `Authorization: Bearer` header that the partner's product sends with each request.
+ **Signing secret** – For a webhook that signs requests, the secret that the partner's product uses to sign `timestamp:body` with HMAC-SHA256. The partner's product sends the timestamp in the `x-amzn-event-timestamp` header and the signature in the `x-amzn-event-signature` header.
+ **Request body** – For a connector that defines its alerts, the alert payload. The partner's product fills in its template values when an alert fires.
+ **Request body format** – For any other connector, the JSON format that each alert must use. Give each alert a unique `incidentId`.

Which of **Header** or **Signing secret** you see depends on how the webhook authenticates. Either the connector sets it, or you choose it in **Select tools**. It doesn't depend on the authentication method that you chose when you registered the connector.

For more information about the webhook's authentication and payload, see [Invoking DevOps Agent through Webhook](configuring-integrations-and-knowledge-invoking-devops-agent-through-webhook.md). For more information about replacing a lost secret, see [Rotating webhook credentials](configuring-integrations-and-knowledge-invoking-devops-agent-through-webhook.html#rotating-webhook-credentials).

### Where the connector appears
<a name="where-the-connector-appears"></a>

On the **Capabilities** tab, the connector appears in the section for its first category: **Telemetry**, **Pipeline**, **Communications**, or **DevOps**. A connector whose first category is **Cloud**, or that the catalog no longer lists, appears in the **MCP Server** section.

## Editing a connector in an Agent Space
<a name="editing-a-connector-in-an-agent-space"></a>

You can change the tools of a connector in an Agent Space, and install, enable, disable, or remove its recommended skills. To edit a connector, complete the following steps:

1. Open the AWS DevOps Agent console at [https://console.aws.amazon.com/aidevops/home](https://console.aws.amazon.com/aidevops/home), and then select your Agent Space.

1. On the **Capabilities** tab, select the MCP server in its section, and then choose **Edit**.

1. On **Select tools**, change the tools. The console starts from the tools that you saved. If the MCP server no longer lists a saved tool, the console removes the tool from the selection and shows a warning.

1. On **Select recommended skills**, select the skills to keep or install. To remove an installed skill, clear it.

1. (Optional) On **Set skill status**, turn each installed skill on or off. Agents use only the skills that are on. You see this step only when at least one skill stays installed.

1. On **Review and save**, review the changes to the tools and skills, and then choose **Save**.

On **Review and save**, the **Tools** table has a **Change** column, which shows **Added**, a classification change such as **Read only → Mutative**, **Removed**, **Removed (Destructive)**, or **Removed (no longer available)**. The table header shows the number of changes, for example **3 changes**.

AWS DevOps Agent saves your changes, and the alert webhook stays the same. Before you save, the review warns you if the change removes skills. It also warns you if another connector in the Agent Space recommends a skill that you disable or remove, because the change applies to that connector too. You can install a removed skill again later.

If a skill change fails, a notification lists it, and your other changes are kept. To try again, edit the connector again.

## Removing a connector from an Agent Space
<a name="removing-a-connector-from-an-agent-space"></a>

To remove a connector from an Agent Space, complete the following steps:

1. Open the AWS DevOps Agent console at [https://console.aws.amazon.com/aidevops/home](https://console.aws.amazon.com/aidevops/home), and then select your Agent Space.

1. On the **Capabilities** tab, select the MCP server in its section, and then choose **Remove**.

1. In **Remove MCP server**, review the confirmation, and then choose **Remove**.

The MCP server is removed from the Agent Space. Removing it also deletes the connector's recommended skills that are installed in the Agent Space. This includes a recommended skill that you installed on your own. A skill stays installed if another connector in the Agent Space also recommends it. The confirmation names the skill, or gives the number of skills, before anything is deleted. You can't undo this action.

If AWS DevOps Agent can't check which skills are installed, the confirmation says so. In that case, the skills stay installed, and **Remove** removes only the MCP server.

## Updating or deregistering a connector
<a name="updating-or-deregistering-a-connector"></a>

To find a connector registration, complete the following steps:

1. Open the AWS DevOps Agent console at [https://console.aws.amazon.com/aidevops/home](https://console.aws.amazon.com/aidevops/home).

1. In the navigation pane, choose **Capability Providers**.

1. Under **Currently registered**, find the connector's card, and then choose **View all**.

1. In **Registrations**, select the MCP server.

If the registration uses **Sign in to** *partner* or **Sign in with dynamic client registration**, you can sign in again without deregistering, for example after the partner revokes access. Choose **Actions**, and then choose **Update**. On the review step, leave **Authorization URL** empty, choose **Update**, and then sign in on the partner's page. AWS DevOps Agent refreshes its access, and your client credentials and Agent Space associations stay the same.

To change an API key or OAuth client credentials, or to use a newer version of the connector, deregister the MCP server and register the connector again. To deregister, first remove the MCP server from every Agent Space that uses it. For instructions on removing it, see [Removing a connector from an Agent Space](#removing-a-connector-from-an-agent-space). Then select the MCP server, choose **Actions**, and choose **Deregister**. The console deregisters the MCP server right away, without asking you to confirm.

## Troubleshooting partner-managed connectors
<a name="troubleshooting-partner-managed-connectors"></a>

Use the following information to resolve common issues with partner-managed connectors.

### "This connector doesn't define a URL for the endpoint you chose"
<a name="this-connector-doesnt-define-a-url-for-the-endpoint-you-chose"></a>

This error means that the connector definition doesn't include the endpoint that you chose. To resolve it, choose another endpoint. If the error continues, contact the connector's support.

### Registration fails because the name is in use
<a name="registration-fails-because-the-name-is-in-use"></a>

MCP server names must be unique in your AWS account. To resolve this issue, enter another name in [Step 1: MCP server details](#step-1-mcp-server-details), and then register again.

### The alert webhook page shows no credential
<a name="the-alert-webhook-page-shows-no-credential"></a>

If **Set up alert webhook** shows an error instead of the header or signing secret, AWS DevOps Agent didn't return a credential for the webhook. To get one, rotate the webhook. For instructions on rotating the webhook, see [Rotating webhook credentials](configuring-integrations-and-knowledge-invoking-devops-agent-through-webhook.html#rotating-webhook-credentials).

### Alerts don't start investigations
<a name="alerts-dont-start-investigations"></a>

The partner's product must send the request exactly as the console showed it. To resolve this issue, complete the following steps:

1. In the partner's product, check that the webhook uses the webhook URL from the console.

1. Check that each request includes the `Authorization` header, or the `x-amzn-event-timestamp` and `x-amzn-event-signature` headers for a signed webhook.

1. Check that the request body matches the **Request body** or **Request body format** from the console.

For more troubleshooting steps, see [Troubleshooting webhooks](configuring-integrations-and-knowledge-invoking-devops-agent-through-webhook.html#troubleshooting-webhooks).

## Related topics
<a name="related-topics"></a>
+ [AWS DevOps Agent Security](aws-devops-agent-security.md)
+ [Connecting MCP Servers](configuring-integrations-and-knowledge-connecting-mcp-servers.md)
+ [Connecting to privately hosted tools](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md)
+ [DevOps Agent Skills](about-aws-devops-agent-devops-agent-skills-index.md)
+ [Invoking DevOps Agent through Webhook](configuring-integrations-and-knowledge-invoking-devops-agent-through-webhook.md)
+ [Working with directed actions](working-with-devops-agent-working-with-directed-actions.md)