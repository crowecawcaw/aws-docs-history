

# AI guardrails in AWS Quick

AWS Quick takes a defense-in-depth approach to help keep chat interactions safe and responsible in the AWS Quick web experience. Multiple safety layers work together, each addressing different risks at different points in an interaction. No single layer is designed to catch every risk on its own.

Usage of AWS Quick AI features is subject to the [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/) on the AWS website.

The following topics describe how these controls work and how to configure them.

**Topics**
+ [How AI safety controls work together](#guardrails-how-controls-work-together)
+ [Enterprise Guardrails (preview)](#guardrails-enterprise)
+ [Blocked words and phrases](#guardrails-blocked-phrases)

## How AI safety controls work together
<a name="guardrails-how-controls-work-together"></a>

AWS Quick uses the following controls together:

Model safety controls  
With Quick, the models that you use have their own safety controls, which are designed to refuse requests for harmful content.

Prompt-level safety instructions  
Quick instructs the model to promote responsible behavior, resist attempts to override safety settings, and avoid exposing internal system information.

External content marking  
When connectors and remote Model Context Protocol (MCP) servers return content, Quick is designed to mark it as external data. It's also designed to instruct the model not to follow instructions in that content. The marking is an instruction to the model, not a filter. For more information, see [Two-condition model for adversarial content risk](sec-agentic-security.md#sec-agentic-security-two-condition-model).

Response rendering  
Quick is designed to remove disallowed HTML from chat responses and to limit the types of links and images that a response can include. You can also choose whether links in responses are clickable. For more information, see [Configure clickable external links in chat responses](manage-agent.md#configure-clickable-links).

Access and permission controls  
Identity, data-access, and action-permission controls limit what data and operations are available during an interaction. These limits match the signed-in person's permissions. For more information about identity and permissions, see [Identity and access management in Quick](identity.md) and [Custom permissions](custom-permissions.md).

Administrator-configured controls  
You can create guardrail policies that screen user prompts for harmful content, denied topics, filtered words and phrases, prompt attacks, and sensitive information, and then assign those policies to users, groups, or your whole account. You can also set up blocked words and phrases for chat interactions in the AWS Quick web experience. For more information, see [Enterprise Guardrails (preview)](#guardrails-enterprise) and [Blocked words and phrases](#guardrails-blocked-phrases).

These controls help reduce risk. However, they do not replace your responsibility to configure access, permissions, agents, flows, and data sources for your use case.

## Enterprise Guardrails (preview)
<a name="guardrails-enterprise"></a>

Enterprise Guardrails is in public preview for AWS Quick and is subject to change. The preview is available to select customers using Quick Enterprise edition. To request access, contact your AWS account team. After your account is enabled, **Guardrails** appears in Quick Admin.

Enterprise Guardrails applies across the AWS Quick desktop, mobile, and web experiences. For the AWS Regions where Enterprise Guardrails is available, and which features each of these experiences supports in each AWS Region, see [URLs, endpoints, and IP addresses](regions.md#regions-qs).

With Enterprise Guardrails, you create guardrail policies that define how Quick screens the prompts that users enter in chat. You assign each policy to individual users, to groups from your enterprise identity provider (IdP), or to the account as a default. Each policy runs in one of two modes. In Detect mode, Quick evaluates prompts and logs policy matches without blocking anything, so you can measure the effect of a policy before you enforce it. In Enforce mode, Quick blocks prompts that match the policy and displays a message to the user.

### What a guardrail policy contains
<a name="guardrails-enterprise-policy-contents"></a>

Each guardrail policy has a name, an optional description, an enforcement mode, a coverage setting, and the following controls.

Content filters  
Quick filters prompts in five categories. Hate covers slurs, dehumanization, and calls for discrimination based on identity. Insults covers personal attacks, demeaning language, and bullying. Sexual covers sexually explicit content, graphic descriptions, and solicitation. Violence covers graphic injury, torture, weapons instructions, and glorification of harm. Misconduct covers financial fraud guidance, instructions for illegal activity, and social engineering tactics. You set the strength of each category to None, Low, Medium, or High. If you don't set a category, it is None, which turns the category off.

Denied topics  
You define topics that users can't discuss in chat. Each topic has a name, an optional definition, and up to five example phrases that help Quick recognize the topic.

Word filters  
You list words and phrases that Quick blocks in prompts, such as confidential project names or client names.

Prompt attack detection  
Quick detects prompt injection and jailbreak attempts. You set the strength to None, Low, Medium, or High. If you don't set it, it is None. In the console, this setting is under **Threat detection**.

Sensitive information (PII)  
Quick detects 29 types of personally identifiable information (PII) in five groups, listed in the following table. Quick checks only the types that you select. In the preview, the only available action is Block.

Coverage  
With the coverage setting, you control which interaction surfaces the guardrail inspects. In the preview, the only interaction surface is User input, which is what the user sends to the model. If you clear User input, the guardrail doesn't inspect anything.

When you create a guardrail policy, you start from one of three baselines and then adjust individual controls. Standard is selected by default. Every baseline starts in Enforce mode, checks user input, blocks all 29 sensitive information types, and has no denied topics or word filters. Relaxed sets content filters and prompt attack detection to Medium. Standard and Strict set them to High. In the preview, Standard and Strict apply the same settings.

Quick detects the following 29 sensitive information types, grouped into five groups.


**Sensitive information types by group**  

| Group | Number of types | Entity types | 
| --- | --- | --- | 
| Financial | 7 | Credit/debit card number, Credit/debit card CVV, Credit/debit card expiry, PIN, US bank account number, International bank account number (IBAN), SWIFT code | 
| Personal | 10 | Name, Address, Geographic location, Date of birth, Age, Username, Password, Driving license number, License plate, Vehicle identification number (VIN) | 
| Technical | 3 | IP address, MAC address, Device ID | 
| Healthcare | 6 | Medical record number, Healthcare biometric, Healthcare condition, Healthcare medication, Healthcare provider, Healthcare treatment | 
| Government ID | 3 | US Social Security number, US Individual Taxpayer Identification Number (ITIN), US passport number | 

### Who a guardrail policy applies to
<a name="guardrails-enterprise-who-applies"></a>

You can assign a guardrail policy to the following:
+ An individual user
+ A group from your IdP
+ The account default, which applies to everyone not covered by a user or group assignment, including users added later

You can't assign a guardrail policy to a role (Author or Reader).

Assignments apply within a Quick namespace. A guardrail policy that you assign in one namespace doesn't apply to users or groups in another namespace, and the account default applies to everyone in that namespace who isn't covered by a user or group assignment. If your account has more than one namespace, the assignments panel shows a list of namespaces, and you choose the namespace that you want to manage.

When more than one level applies to a user, the most specific level determines the user's guardrails. A user level assignment takes priority over group level assignments, and a group level assignment takes priority over the account default. To give one member of a group different guardrails, assign a policy directly to that user.

When more than one policy applies at the same level, for example when a user belongs to two groups that each have a policy, Quick combines the policies and uses the stricter setting for each control. Enforce takes priority over Detect, the higher strength applies for each content filter and for prompt attack detection, and Quick checks a PII entity type if any of the policies turns it on. Quick combines the denied topics and the word filters from all of the policies.

The following table shows the effective guardrail for a user who belongs to two groups that have different policies.


**Example: effective guardrails for a user in two groups**  

| Control | Group A policy | Group B policy | Effective for the user | 
| --- | --- | --- | --- | 
| Mode | Detect | Enforce | Enforce | 
| Hate content filter | Low | High | High | 
| Prompt attack detection | None | Medium | Medium | 
| PII: US Social Security number | Off | On | On | 
| Denied topics | Unreleased products | Competitor pricing | Both topics | 

### What the preview checks
<a name="guardrails-enterprise-preview-checks"></a>

In the preview, Quick checks the prompt that the user enters in chat. The preview doesn't check the following:
+ Model responses.
+ Content that agents send to tools and receive from tools.
+ The contents of files that a user attaches to a prompt. Quick checks the text that the user types and the file name only.

In the preview, Quick blocks prompts that contain a selected PII entity type. Replacing or masking PII in a prompt instead of blocking it isn't available.

### Guardrail quotas
<a name="guardrails-enterprise-quotas"></a>

The API and the Quick Admin console enforce the following quotas. These quotas are fixed. They aren't managed in Service Quotas, and you can't request an increase.


**Guardrail quotas**  

| Resource | Quota | 
| --- | --- | 
| Guardrail policies per account | 200 | 
| Policy name | 1 to 100 characters | 
| Policy description | Up to 200 characters | 
| Denied topics per policy | 30 | 
| Denied topic name | 1 to 100 characters | 
| Denied topic definition | Up to 240 characters | 
| Example phrases per denied topic | 5, up to 160 characters each | 
| Word filter entries per policy | 1,000 | 
| Word filter entry | 1 to 50 characters, with no leading or trailing spaces | 
| Assignments per import file | 500 | 
| Assignments per download file | 10,000 | 

### Create a guardrail policy
<a name="guardrails-enterprise-create"></a>

Use the following procedures to create a guardrail policy. First, add the policy details and select a baseline. Then configure the controls, set coverage, and create the policy.

**To add the guardrail details and baseline**

1. Sign in to Quick as an administrator, open Quick Admin, and then choose **Guardrails**.

1. Choose **Create guardrail**.

1. On the **Add guardrail details** page, enter a name and, optionally, a description, and then choose **Next**.

1. On the **Set content guardrails** page, select a baseline: **Relaxed**, **Standard**, or **Strict**.

After you set the baseline, use the following procedure to configure the controls and create the guardrail.

**To configure the controls and create the guardrail**

1. On the **Content filters and safety** page, adjust the strength of each content filter category and of prompt attack detection.
   + To add a denied topic, choose **Add**, enter a topic name, a definition, and up to five example phrases, and then choose **Add denied topic**.
   + To add word filters, choose **Add**, enter words or phrases separated by commas or new lines, and then choose **Add words**.
   + To add denied topics or word filters from a .csv or text file, choose **Import**. For denied topics, use one topic name per line, or a .csv file with the header row name, definition, examples. Separate multiple examples in one cell with a vertical bar (\|).

1. On the **Data protection** page, select the sensitive information types that you want the guardrail to block, and then choose **Next**.

1. On the **Set coverage** page, keep **User input** selected, and then choose **Next**.

1. On the **Review configuration** page, review the summary, and then choose an enforcement mode. To test a new guardrail, choose **Detect** and review the logged matches before you switch to **Enforce**.

1. Choose **Create guardrail**. To create the guardrail and assign it in one step, choose **Create and assign**.

### Assign a guardrail policy
<a name="guardrails-enterprise-assign"></a>

Use the following procedure to assign a guardrail policy.

**To assign a guardrail policy**

1. In Quick Admin, choose **Guardrails**.

1. For the guardrail that you want to assign, open the options menu in the **Actions** column, and then choose **Assign**. The assignments panel lists the current assignments under **Users**, **Groups**, and **Account**. If your account has more than one namespace, choose the namespace from the list at the top of the panel.

1. In **Find assignees**, search for the user or group that you want to assign. To narrow the search, select **Users**, **Groups**, or **Account** from the list next to the search box. Matches appear under **Not assigned to this guardrail**. Choose **Add user** or **Add group** next to the match.

1. To make the guardrail the account default, expand **Account**, and then choose **Add account** next to your account.

1. In **Confirm assignment changes**, review the change, and then choose **Confirm & apply**.

From the assignments panel, you can also import assignments from a .csv file and download the current list of assignments. The **Download** and **Import** actions are in the options menu next to **Currently assigned to this guardrail**. **Download** produces a .csv file that includes the user, group, account, and namespace (for example, default). Each import file can contain up to 500 assignments. To import more, upload additional files. A download includes up to 10,000 assignments in one file. If a policy has more than 10,000 assignments, the file contains the first 10,000 and Quick displays a warning that not all assignments are included.

You can also manage user, group, and account assignments with the AWS Quick API. For more information, see the [Quick API reference](https://docs.aws.amazon.com/quicksight/latest/APIReference/Welcome.html).

### Check the effective guardrail for a user, group, or account
<a name="guardrails-enterprise-check-coverage"></a>

Use **Check coverage** to see which guardrail applies to a user, group, or account after Quick resolves all of its assignments. On the **Guardrails** page, open the **Check coverage** panel, and then search for a user, group, or account. Under **Resolution**, the panel lists each assignment that applies, marks the one that Quick applies, and marks the others as overridden. Under **Effective behavior**, the panel summarizes the content safety, data protection, and coverage settings that result.

## Blocked words and phrases
<a name="guardrails-blocked-phrases"></a>

You can block up to 50 words or phrases in chat interactions in the AWS Quick web experience. This applies to chat agents and flows. Each entry can contain up to 36 characters. Quick checks both user requests and generated responses for these phrases. These checks match whole words and phrases, regardless of capitalization. They aren't designed to catch misspellings, character substitutions, or encoded text. Quick doesn't block any words or phrases by default.

### Add blocked words and phrases
<a name="guardrails-add-blocked-phrases"></a>

Use the following procedure to add blocked words and phrases for chat agents and flows in the AWS Quick web experience.

**To add blocked words and phrases**

1. Sign in to Quick and choose **Manage Quick**.

1. From the navigation pane, choose **Customization**, and then choose **Chat agent customization**.

1. In **Chat agent customization**, under **Guardrails and safety controls**, choose **Add** to add blocked words and phrases. You can add up to 50 words and phrases. Each entry can contain up to 36 characters.

### Edit blocked words and phrases
<a name="guardrails-edit-blocked-phrases"></a>

Use the following procedure to add or remove blocked words and phrases for chat agents and flows in the AWS Quick web experience.

**To edit blocked words and phrases**

1. Sign in to Quick and choose **Manage Quick**.

1. From the navigation pane, choose **Customization**, and then choose **Chat agent customization**.

1. In **Chat agent customization**, under **Guardrails and safety controls**, choose **Remove** to remove existing entries, or choose **Add** to add entries. You can add up to 50 words and phrases. Each entry can contain up to 36 characters.