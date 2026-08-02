Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](qbusiness-availability-change.md "qbusiness-availability-change.md").

# Amazon Q Business availability change

## Overview

Amazon Q Business is no longer open to new customers. AWS will continue to
provide bug fixes and security updates for existing customers, however new feature
requests will no longer be considered.

We recommend that customers migrate their Q Business applications and implement any new
generative or agentic AI solutions on Amazon Quick for similar capabilities to Q Business
and more advanced features for generative BI and agentic AI use cases. Quick is an AI
assistant for work that brings all your data together—connecting Slack, Microsoft Teams
and Outlook, CRMs, databases, and documents in one place. It learns what matters to you
and your team, grounds every answer in your real business data, and goes beyond answers:
scheduling, building deliverables, creating dashboards, and acting on your behalf.

## Migration Guidance

Migration from AWS Q Business to Amazon Quick follows a phased approach, starting
with the Bring Your Own Index (BYOI) capability, which allows you to bring your existing
Q Business index to Quick without disrupting current operations. This approach allows you
to move users and apps to Quick as fast as possible, enabling access to Quick's expanded
capabilities – including Quick Flows for workflow automation, QuickSight integration for
structured data analysis, Research for in-depth research and expert insights, and Spaces
for unified knowledge management – and then migrate your data sources to the Quick Index
over time if needed.

This migration guide provides AWS Q Business customers with a comprehensive,
step-by-step pathway to transition their existing applications to Amazon Quick, including
detailed workarounds for features that are not yet available in Quick.

Customers who use anonymous access and API integration of Q Business into custom
applications should contact [AWS
Support](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support") to discuss custom approaches for migrating these applications.

### Amazon Quick Features

Amazon Quick represents the next evolution of Amazon Q Business, providing a
unified platform that seamlessly accesses company data from documents, enterprise
applications, databases, data warehouses, and real-time internet information.

Amazon Quick includes several integrated capabilities: Quick Sight for interactive
data visualization; Flows for intelligent workflow automation; Automate for
streamlined business process automation; Quick Research for comprehensive data
analysis; Spaces to aggregate files, dashboards, topics, knowledge bases; and Apps
for interactive applications. Quick also includes mobile and desktop applications for
access across any device and from any location.

### Prerequisites and Planning

Before beginning migration, ensure your environment meets the following
requirements and complete an inventory of your existing Q Business resources.

#### AWS Account and Region Requirements

Both your Amazon Q Business index and Amazon Quick instance must reside
in the same AWS account and AWS Region. You must have administrator
permissions in Amazon Quick. For IDC-based implementations, AWS IAM Identity
Center must be enabled and configured, with both services authenticating through
IAM Identity Center in the same region.

#### Identity Provider Assessment

Amazon Quick's BYOI feature to connect your existing Q Business Index supports
two implementation methods. The IDC Implementation requires both Q Business and
Quick to authenticate through IAM Identity Center in the same account and region.
The Non-IDC Implementation supports native identities, AWS Managed Microsoft
AD, and IAM federation, where all Amazon Quick users automatically receive access
to connected indexes. Determine which method applies to your organization before
proceeding.

#### Inventory Existing Q Business Resources

Use the AWS CLI to export your current Q Business configurations for
planning purposes. Run the following commands to catalog your data
sources:

```

# List all data sources in your Q Business application
aws qbusiness list-data-sources \
  --application-id <your-application-id> \
  --index-id <your-index-id>

# Get detailed configuration for each data source
aws qbusiness get-data-source \
  --application-id <your-application-id> \
  --index-id <your-index-id> \
  --data-source-id <your-data-source-id>

```

These commands retrieve your connector configurations, which you will reference
during migration planning. Additionally, inventory your plugins, Q Apps, web
experience customizations, guardrails, and document attribute
configurations.

## Migration

### Step 1: Set up Quick

To subscribe to Quick:

- Sign in to your AWS account and open Quick from the AWS Management
  Console. You can find it under Analytics or by searching for Quick. Your
  AWS account number is displayed for verification purposes.
- Enter a unique account name for Quick. Enter a notification email address
  for the Quick account owner or group. This email address receives service and
  usage notifications.
- Choose the AWS Region that you want to use for your initial data storage
  capacity, called SPICE.
- Choose an authentication method that you want to connect to Quick with.
  Select from one of the following:

  - Password-based or Single-Sign On
  - IAM Identity Center
  - Single-Sign-On Only
  - Active Directory

- Review the choices that you made, then choose Create account.
- Upon completion, your Quick account is created. To open Quick, choose Go to
  Quick.

### Step 2: Connect your Q Business Index with BYOI

This step is optional but provides the fastest path to migrating your existing Q
Business Index to Quick without the need to reconnect data sources and recreate the
index in Quick. This does not affect your existing Q Business application in any way.
If you prefer to start by setting up your connections natively in Quick, skip to step
2a below.

**Implementation Steps:** Sign in to the Amazon Quick
console as an Admin or Admin Pro user, navigate to Knowledge bases, choose Create
knowledge base, select Amazon Q Business as the data source, choose the
Amazon Q Business index you want to use, provide a name and description, and
choose Create. Your Q Business chat profile is replicated in Quick, allowing
administrators and selected users to experience Quick while Q Business continues
running in parallel.

**Supported Identity Types:** BYOI supports two
authentication configurations. The IDC implementation requires both Amazon Q Business (using AWS\_IAM\_IDC) and Amazon Quick to authenticate through IAM
Identity Center. The non-IDC implementation supports Amazon Q Business using
AWS\_QUICKSIGHT\_IDP with Quick authenticating via native identities, AWS Managed
Microsoft AD, or IAM federation. In an IDC implementation, access to the knowledge
base is automatically granted only to users with access to the selected Q Business
index, and additional users require admin configuration in both consoles. In a
non-IDC implementation, all Amazon Quick users automatically receive access to
connected Q Business indexes.

**Limitations:** Be aware of the following constraints
when using BYOI. You can connect a maximum of two Amazon Q Business indexes per
region, and this quota cannot be increased. Once indexes are selected and saved, they
cannot be directly unselected. Amazon Q Business index knowledge bases cannot
be modified like other Quick knowledge bases. Q Apps, Actions, and Amazon Q Business chat guardrails are not included in the BYOI capability. Only
document types supported by Amazon Q Business are supported in the connected
index.

### Step 2a: Connect Native Data Sources Directly to Quick

Quick provides native integrations for both Knowledge Bases and Actions.

The console organizes integrations into separate categories based on their purpose.
Use Knowledge to connect data sources for Q&A and insights. Use Connectors to
set up action connectors that perform operations in external applications. The setup
process adapts based on the integration you select, your subscription, and existing
integrations.

When you set up an integration, the console guides you based on several
factors:

- **Integration capabilities** – Each
  application supports different combinations of actions and knowledge base
  creation. For example, Google Drive supports both actions and knowledge base
  creation. Web Crawler supports knowledge base creation only.
- **Subscription** – Configuring
  integrations requires an Enterprise subscription. This includes creating
  action connectors, setting up knowledge bases, and managing integration
  settings. Users with a Professional subscription can use integrations that
  have been shared with them.
- **Existing integrations** – When you
  choose a connector that already exists, the console shows your existing
  connectors before offering to create new ones.

The following examples show how different integrations guide you through different
console setup processes.

**Google Drive – Set up a knowledge
base:**

1. In the console, choose Knowledge.
2. Find Google Drive and choose the Add (+) icon.
3. Choose your authentication method and complete the sign-in flow.
4. Enter a name and description for your knowledge base.
5. Select the files and folders you want to index, then choose Create.

**Google Drive – Set up an action
connector:**

1. In the console, choose Connectors.
2. Choose the Create for your team tab.
3. Find and choose Google Drive.
4. Enter a Name for your connector. Optionally, choose + Add Description to add a description.
5. Choose your Connection type and OAuth Configuration, then complete the authentication setup.
6. Review the available actions and choose Publish.

See the Quick User Guide for integration-specific documentation.

### Step 2b: Using MCP for Data Sources Without Native Integrations

When migrating from Q Business to Amazon Quick, you may find that some Q Business
data source connectors do not have a direct native equivalent in Quick. Amazon Quick
addresses this gap through Model Context Protocol (MCP), an open standard that
defines how AI applications communicate with external tools and data sources. MCP
uses a client-server architecture where Amazon Quick acts as the MCP client,
connecting to remote MCP servers that expose structured tools such as querying
databases, calling APIs, or interacting with third-party services. Because MCP is an
open standard, customers can connect to any compatible server without building custom
integrations for each tool.

#### Setting Up MCP Integrations

Amazon Quick provides a 4-step console wizard for configuring MCP
integrations. In the Amazon Quick console, choose Integrations, then Add, then
select Model Context Protocol (MCP). Enter the integration name, description, and
MCP server endpoint URL. Next, select the authentication method—user OAuth,
service-to-service, or no authentication—and provide the appropriate
credentials. Quick then auto-discovers and registers the available tools as
actions. Finally, share the integration with other users as needed.

#### Validated MCP Integrations

Several services that lack native Quick connectors are available through
validated MCP-based integrations. These include Visier for people analytics,
HuggingFace for ML models and datasets, Intercom for customer messaging, Linear
for project management, and PagerDuty Advance for incident response and SRE
workflows. All validated MCP integrations support Chat Agents and Flows but do
not support Knowledge Base indexing.

#### MCP Limitations

When planning your migration, be aware of the following MCP constraints:
operations have a fixed 60-second timeout and will fail with an HTTP 424 error if
exceeded; custom HTTP headers are not supported; tool lists remain static after
initial registration, requiring you to delete and recreate the integration to
pick up server-side tool changes; and step-up authorization is not supported.
Additionally, MCP integrations provide action capabilities (querying, invoking
APIs) but cannot be used as knowledge base data sources for document
indexing.

#### Migration Recommendation

For Q Business customers using connectors without native Quick equivalents, the
recommended approach is to first check whether a validated MCP integration exists
for the target service. If one does not exist, evaluate whether the service
provides an MCP server or whether you can deploy a custom MCP server that wraps
the service's API. This approach allows you to maintain connectivity to all your
enterprise data sources while benefiting from Quick's advanced
capabilities.

### Step 3: Identity and Access Control Migration

#### IDC Identity Migration

For organizations using IAM Identity Center, user migration is the most
straightforward path. AWS deduplicates subscriptions across all Q Business
applications sharing the same IAM Identity Center instance, charging each user
only once for their highest subscription level. This same identity infrastructure
carries forward into Quick, making the transition seamless for IDC-based
deployments.

#### Non-IDC Identity Migration

Organizations using IAM Federation, native identities, or AWS Managed
Microsoft AD face a more complex migration. The non-IDC implementation in Quick
supports these authentication methods, and all Quick users automatically receive
access to connected indexes. However, the mapping of individual user permissions
requires manual scripting to replicate the granular access controls that existed
in Q Business. In a non-IDC implementation, because all Amazon Quick users
automatically receive access to connected Q Business indexes, you lose the
per-user and per-group access distinctions that Q Business enforced at the index
level. To restore granular access, you must segment content into separate
knowledge bases and programmatically assign permissions at the knowledge base
level within Quick Spaces.

The following example script demonstrates how to export user-to-data-source
mappings from Q Business and generate corresponding Quick knowledge base
permission assignments:

```

import boto3
import json

# Step 1: Export Q Business user/group ACL mappings
qbusiness = boto3.client('qbusiness')
quicksight = boto3.client('quicksight')

APPLICATION_ID = '<your-q-business-application-id>'
INDEX_ID = '<your-q-business-index-id>'
QUICK_ACCOUNT_ID = '<your-aws-account-id>'

# Retrieve all data sources and their associated access controls
data_sources = qbusiness.list_data_sources(
    applicationId=APPLICATION_ID,
    indexId=INDEX_ID
)['dataSources']

# Step 2: Build a mapping of data source -> authorized users/groups
access_map = {}
for ds in data_sources:
    ds_id = ds['dataSourceId']
    ds_name = ds['displayName']

    # List groups with access to this data source
    groups_response = qbusiness.list_groups(
        applicationId=APPLICATION_ID,
        indexId=INDEX_ID,
        dataSourceId=ds_id
    )
    access_map[ds_name] = {
        'data_source_id': ds_id,
        'groups': [g['groupName'] for g in groups_response.get('items', [])]
    }

print(json.dumps(access_map, indent=2))

# Step 3: Create Quick knowledge base permission assignments
# For each data source segment, assign the corresponding groups
# to the appropriate Quick Space/knowledge base
for ds_name, config in access_map.items():
    for group_name in config['groups']:
        # Use Quick APIs to grant group access to the corresponding
        # knowledge base that contains this data source's content
        print(f"Assigning group '{group_name}' access to "
              f"knowledge base for '{ds_name}'")

        # Example: Update knowledge base sharing in Quick
        # This maps to the Quick console action of sharing a
        # knowledge base with specific groups within a Space
        quicksight.update_folder_permissions(
            AwsAccountId=QUICK_ACCOUNT_ID,
            FolderId=f'kb-{ds_name.lower().replace(" ", "-")}',
            GrantPermissions=[{
                'Principal': f'arn:aws:quicksight:{QUICK_ACCOUNT_ID}:group/default/{group_name}',
                'Actions': [
                    'quicksight:DescribeFolder',
                    'quicksight:ListFolderMembers'
                ]
            }]
        )

```

This script illustrates the general pattern: extract the user and group access
mappings from Q Business, then apply equivalent permissions at the knowledge base
or Space level in Quick. Because Quick's Non-IDC mode grants blanket access to
all connected indexes, the workaround is to organize content into multiple
knowledge bases segmented by access role, then restrict each knowledge base's
sharing permissions to the appropriate groups.

#### Document-Level ACL Migration

Amazon Quick supports document-level access control lists (ACLs) for S3,
Confluence Cloud, SharePoint, and Google Drive knowledge bases. This
significantly narrows the access control gap between Q Business and Quick. For S3
knowledge bases, Quick provides two ACL configuration methods: a global ACL
configuration file that defines centralized folder-level permissions, and
document-level metadata files that provide per-document ACL entries for faster
updates. Each ACL entry supports Name (email for USER, group name for GROUP),
Type (USER or GROUP), and Access (ALLOW or DENY) controls.

ACLs must be enabled at knowledge base creation time—this setting is permanent
and cannot be changed after creation. During setup, you specify the global ACL
file location (S3 path to acl.json) and optionally a metadata files folder
location. All ACLs are resolved within the Quick namespace of the knowledge base
creator.

Quick does not ingest documents that lack an associated ACL entry, adopting a
stricter default posture. In contrast, Q Business grants all users access to S3
prefixes that do not appear in the ACL file. Organizations migrating from Q
Business should ensure all documents have explicit ACL entries before enabling
ACLs in Quick to avoid unintentional content exclusion.

For connectors where Quick does not yet support native ACL crawling, segment
content into multiple knowledge bases organized by access level and assign
team-level or role-level access to each knowledge base within Spaces.

### Step 4: Migrating Q Apps to Quick Flows

Q Apps must be migrated to Quick Flows, as Q Apps are excluded from the BYOI
capability. Follow these steps to migrate a Q App to a Quick Flow.

- Navigate to your Q Business web application in your browser using the Quick
  browser extension's hamburger menu and selecting "Go to Web App."
- Select "Apps" in the left-hand menu to view your Q Apps, then select the
  specific app you want to migrate.
- Open the Amazon Quick browser extension and click the "+" icon ("Chat with
  this tab") next to "Amazon Q." This allows Quick to analyze your Q App's
  structure and logic.
- Enter the following prompt into Amazon Quick to generate a Flow-equivalent
  description:

```

I am migrating this Amazon Q App (Q App name) into Quick as a Quick Flow.
Create a prompt that I can paste into Quick that would recreate this Q App
as a Quick Flow. Using your best effort: Identity the data sources (Company
knowledge or General knowledge) and map to Quick Flows step types (e.g.
Quick data, General knowledge, or Web search). Identity any action steps
that are utilized and map them to the available action connector within
Quick. Determine the sequence of steps in which the Flow is executed and
how each card in Q Apps will be represented in Quick Flows. Ensure the
prompts used within the Q App are copied verbatim. Output this prompt as
markdown and only output the prompt.

```

- Copy the generated prompt from Amazon Quick's response.
- Open the Amazon Quick Web Application, navigate to "Flows" in the left-hand
  menu, and click "Create Flow."
- Paste the generated prompt into the text box and click
  "Generate."
- Optimize your new Quick Flow using "Run Mode" to test behavior. Tune
  individual steps by modifying prompts, selecting output preferences
  (Versatility and Performance is the default), and adjusting creativity
  levels—lower creativity works better for steps requiring consistent
  output.
- Iterate testing and tuning until the Quick Flow replicates your Q App's
  behavior satisfactorily.
- Click "Share and Publish" to make the Flow available to your
  users.

Some Q App features like forms are not yet available in Quick Flows. Amazon Quick
will not be able to replicate these features during migration. For form-based Q Apps,
consider using Quick's structured input capabilities or maintaining those specific Q
Apps until form support is added.

## Feature Gaps and Workarounds

Not all Q Business features are available in Quick. Guardrails and User Store are
features that require workarounds in Quick. This section discusses those
workarounds.

**Guardrails and Actions**

Q Business guardrails (global controls and topic-level controls) and
Actions are explicitly excluded from the BYOI capability. This means that
content filtering rules, blocked topics, and custom action configurations
from your Q Business application will not transfer to Quick through
BYOI.

**Workaround:** Recreate content governance
policies using Quick's native configuration options. For action-based
workflows, migrate to Quick Flows which support integration with third-party
business applications and AWS service connectors.

**User Store**

Q Business provides a User Store that streamlines user and group management
across data sources. In Quick, user management operates at the knowledge base
level rather than through a centralized user store.

**Workaround:** Leverage IAM Identity Center
groups and Quick's Space-level sharing capabilities to manage user access.
Organize knowledge bases by team or role and use Space sharing to control
which groups can access specific content collections.

## Post-Migration Validation and Cutover

### Testing BYOI Responses

After connecting your Q Business index via BYOI, validate response quality by
testing representative queries against both platforms. Compare citation accuracy,
response completeness, and relevance. Note that guardrails configured in Q Business
will not apply through BYOI, so verify that Quick's native content governance meets
your requirements.

### Cutover Checklist

Before disabling your Q Business application URL, confirm that all users have been
successfully migrated and can authenticate to Quick, that response quality meets or
exceeds Q Business baselines, that any Q Apps have been successfully recreated as
Quick Flows, that document-level ACLs have been configured for applicable knowledge
bases, and that MCP integrations are functioning for data sources without native
connectors.

## Summary

Migration from AWS Q Business to Amazon Quick is a strategic upgrade that provides
access to unified structured and unstructured data analysis, advanced workflow automation
through Quick Flows and Automate, expert-level insights through Research, and unified
knowledge management through Spaces. The BYOI capability ensures a low-risk entry point
that preserves your existing data ingestion investments.

For most customers, the recommended approach is to begin with BYOI immediately to
evaluate Quick's capabilities in parallel with your existing Q Business deployment.
Address feature gaps using the workarounds documented in this guide and plan your cutover
as full feature parity is achieved.

Please contact [AWS
Support](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support") with any additional questions.
