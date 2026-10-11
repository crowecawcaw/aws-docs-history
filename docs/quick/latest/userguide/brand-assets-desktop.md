

# Brand assets
<a name="brand-assets-desktop"></a>

Brand assets help your organization keep a consistent brand style across the documents and presentations that people create in Amazon Quick. On the **Brand assets** tab, under **Customize**, brand managers upload your organization's brand templates or retrieve them from a connected file store. Quick extracts style elements and brand rules from those files and shows what it found so a person can review, edit, and publish it. After a brand is published, Quick can suggest its templates to users across your organization, choosing a suitable template for each task, so users don't need to find and attach a template in every chat.

Administrators control who manages brand assets by using [custom permissions](custom-permissions.md).

## How brand assets work
<a name="brand-assets-concepts"></a>

Quick organizes brand assets in two levels.

Brand  
A named collection of templates that a brand manager can publish to your whole organization. A brand starts as a draft and appears organization-wide on the **Brand assets** tab after it is published. A brand typically maps to one of your organization's brands or sub-brands, for example, AnyCompany Corporate or AnyCompany Energy Solutions. A brand is the unit that is published and shared. Brand versioning isn't available.

Template  
One design inside a brand. A brand can hold multiple templates, for example, a pitch deck, a proposal, and a one-pager, all under AnyCompany Corporate. Each template carries what Quick learned from your source file, including its style elements and its rules, so Quick can match the template to a request and apply its design.

Quick builds brand assets by extracting the following.


| Extracted | Description | 
| --- | --- | 
| Colors | Your palette, with the hex value for each color | 
| Text styles | Named styles with font family, point size, weight, and color | 
| Logos | Logo image assets found in the file | 
| Structure and outline | For documents: the section structure, heading hierarchy, and style groups | 
| Page dimensions | For documents: page size, margins, orientation, and column count | 
| When to use | The use cases this template is for. Quick uses this to match the template to a user's task. Quick writes it from the source file's context, and a brand manager can edit it. | 
| Rules | The usage rules Quick uses when generating with this template. Quick writes them from the source file's context, and a brand manager can edit them. | 

Quick uses the extracted template elements to guide content creation. Check the generated backgrounds, colors, decorative elements, icons, and images against the source template.

## Brand rules and how Quick uses them
<a name="brand-assets-rules"></a>

Brand templates carry more than colors and fonts. A well-built template often includes instructions for the people using it: which layout to use for what, how to treat icons, when a section divider belongs, and what not to put on the title slide. Quick extracts these rules alongside the visual style and uses them as guidance when it generates content with that template.

Quick produces rules in two steps:
+ **Quick populates them automatically**: during extraction, Quick reads the source file's context, such as instruction slides, speaker notes, layout guidance, and the design itself, and writes an initial set of rules as a bulleted list.
+ **A brand manager reviews and edits them**: brand managers can edit the rules inline as part of the extraction flow. They can correct anything Quick misread, remove bullets that shouldn't govern generation, and add rules that the source file didn't state. Reviewing and trimming the extracted rules for relevance helps Quick generate content that follows your brand.

## Who does what
<a name="brand-assets-roles"></a>


| Who | Browse published brands | Apply a template to generated output | Extract, refine, and publish organization-wide templates | Delete a published brand | 
| --- | --- | --- | --- | --- | 
| Brand manager: any signed-in user who holds Create and update brand kits | Yes | Yes | Yes | Yes | 
| User for whom the capability is turned off | Yes | Yes | No | No | 

For information about controlling access to this capability, see [Assigning brand managers](#brand-assets-admin-delegate).

## Enabling brand assets and assigning brand managers
<a name="brand-assets-admin"></a>

As an administrator, you decide who curates brand assets.

### Prerequisites
<a name="brand-assets-admin-prereqs"></a>

Brand assets are available only in Amazon Quick Enterprise edition.

Before your organization can use brand assets, make sure that:
+ Users sign in to Quick with your organization's credentials.
+ Users have access to create Word documents and PowerPoint presentations in Quick. For an overview of document generation, see [Document and visual creation with Amazon Quick](document-and-visual-creation.md). For access controls, see [Custom permissions](custom-permissions.md).
+ To extract a template directly from a file store, brand managers have access to that service and have enabled its connector in their account.

### Assigning brand managers
<a name="brand-assets-admin-delegate"></a>

Administrators can configure [custom permissions](custom-permissions.md) for the **Create and update brand kits** capability. By default, this capability is available to all users unless an administrator turns it off.

For guidance on restricting capabilities by default, see [Deny by Default](custom-permissions-governance.md).

## Extracting, refining, and publishing templates
<a name="brand-assets-manager"></a>

This section applies to brand managers, the users who hold the **Create and update brand kits** permission.

Curating a brand has three stages: extract a template from a real file, review and edit what Quick learned, and then publish so everyone in your organization can use it.

### Extracting a template
<a name="brand-assets-manager-extract"></a>

Extraction runs as a guided conversation. Quick asks where the template belongs, extracts it, and opens the result in a panel beside the chat, where you review and edit it before publishing. You can start from a file on your computer or from a template stored in a service you have connected. Both paths use the same extraction and review steps.

Quick accepts PowerPoint presentations and templates (`.pptx`, `.potx`) and Word documents and templates (`.docx`, `.dotx`). For details, see [Supported source files](#brand-assets-reference-files).<a name="brand-assets-manager-extract-procedure"></a>

**To extract a template from a file**

1. Open the **Brand assets** tab, choose **Create**, and then choose **Upload template**.

1. Select your file. Quick opens a session and attaches the file.

1. In chat, tell Quick whether to add the template to an existing brand or create a new brand. Follow the conversation to choose where the template belongs.

1. Quick extracts the template and reports what it captured: the slide and asset counts, the palette with each color named, the fonts, the inferred **When to use** text, and any gaps it found.

1. Review and edit the result in the panel that opens beside the chat. For details, see [Reviewing and editing what Quick extracted](#brand-assets-manager-refine).

### Extracting a template from a connected source
<a name="brand-assets-manager-connected"></a>

If your organization keeps approved templates in a shared document store, you can point Quick at the file where it lives. Quick retrieves the file through the connector for that service and runs the same extraction, review, and publish flow.

Support for retrieving a template depends on the connector's API. The connector must be able to retrieve the supported source file, not just information about it. There is no separate compatibility list for brand-asset sources. For general connector setup and available integrations, see [Connectors](connections-desktop.md) and [Supported integrations](supported-integrations.md).

**To extract a template from a connected source**

1. If the service isn't connected yet, follow the setup instructions in [Connectors](connections-desktop.md). Quick uses your own access to that service, so you can reach only the files that you can open yourself.

1. Open the **Brand assets** tab, choose **Create**, and then choose **Create using a connector**.

1. Identify the file. Paste its link, or describe it by name and location, for example, "the corporate deck template in the Brand Assets library." Quick retrieves the file and attaches it to the session.

1. Continue from step 3 of [To extract a template from a file](#brand-assets-manager-extract-procedure). Everything after retrieval is the same: you choose where the template belongs, Quick extracts it, and you review it before publishing.

**Note**  
Retrieving a template through a connector is a one-time pull, not an ongoing sync. If someone changes the source file, a brand manager must retrieve and extract the updated file, review it, and publish the update.

Extraction quality doesn't depend on where the file came from. The same guidance in [Supported source files](#brand-assets-reference-files) applies: a file with real layouts, named styles, and brand colors extracts better than one built with local formatting.

### Reviewing and editing what Quick extracted
<a name="brand-assets-manager-refine"></a>

The panel that opens beside the chat shows everything Quick found and lets you edit it before publishing.

Instructions  
The panel has two editable fields:  
+ **When to use**: the tasks this template is for. Quick infers these from the source file's content and purpose. Use descriptions your colleagues would use for their tasks. For example, "client-facing proposals and statements of work" is more specific than "external doc." This guidance helps Quick match a template to a request.
+ **Rules**: the bulleted guidance Quick uses when building with this template. Confirm what Quick captured, remove bullets that were never brand rules, and add rules that your source file only implied. For details, see [Brand rules and how Quick uses them](#brand-assets-rules).

Logo  
The logo assets found in the file. Remove any that were incidental rather than part of the brand, and use the add control to supply a logo that Quick missed, such as a variant for dark backgrounds.

When you're done, in the extraction form, choose **Save as draft** to keep working, or choose **Publish** to release the brand to your organization. Repeat these steps for each template in the brand. To revise a published template, open it from the **Brand assets** tab, edit it, and then choose **Publish** to make the change available to everyone. Before you publish an update, see [Publishing a brand](#brand-assets-manager-publish).

**Tip**  
Two templates compete when their **When to use** text overlaps. If Quick keeps picking the wrong one, sharpen both descriptions so the boundary between them is clear.

### Publishing a brand
<a name="brand-assets-manager-publish"></a>

**Important**  
Publishing replaces the published brand with your entire copy, not just the template you edited. If your copy is out of date, publishing can remove templates that another brand manager added or overwrite their newer changes. Templates removed this way can't be recovered. Make sure your copy includes the latest published content before you publish an update.

Before editing a published brand, ask Quick in chat to retrieve its latest published copy. Include the brand name in your request.

Until you publish, a brand is a draft that only you can see. The **Brand assets** tab shows only published brands. Unpublished drafts don't appear there, and the tab doesn't display status badges. Publishing makes the brand visible to everyone in your organization and makes its templates available for Quick to match to tasks. You can publish in two ways:
+ **From the extraction form**: choose **Publish**. To keep working and publish later, choose **Save as draft** instead.
+ **From chat**: after reviewing the extracted template, ask Quick to publish the brand to your organization, or tell it to keep the brand as a draft. The wording in the conversation can vary.

Quick confirms what it published, including which templates were included and the palette and font the brand applies. The brand then appears on the **Brand assets** tab for all users, and Quick begins offering its templates when it plans documents and presentations.

**Note**  
A draft is a working brand. You can create a presentation or document from it yourself to test it before you release it to anyone else. Publishing is the only step that makes it available to your organization.

### Updating, renaming, and reorganizing
<a name="brand-assets-manager-manage"></a>

Before you change a published brand, ask Quick in chat to retrieve its latest published copy. Include the brand name in your request. Before publishing your changes, make sure your copy includes the latest published content. For details, see the important note in [Publishing a brand](#brand-assets-manager-publish).


| Task | How | 
| --- | --- | 
| Add a template to a published brand | Extract the new template and choose the existing brand name when Quick asks where to save it. | 
| Change a template's rules or When to use text | Ask Quick in chat to open the template, and then edit the fields. | 
| Rename a brand | Ask Quick in chat to rename it, and then publish the update. | 
| Move a template to a different brand | Ask Quick in chat to move the template to a different brand, and then publish the change. | 
| Delete a published brand | Use the delete action on the brand on the Brand assets tab. | 

## For users: working with published templates
<a name="brand-assets-user"></a>

If you don't curate brand assets, you don't need to do anything to use them. Your organization's approved templates appear as template options when you create a document or presentation.

When you generate your next presentation or Word document after a brand is republished, Quick retrieves the latest published brand and refreshes your downloaded copy. You don't need to refresh it manually for either type of generation.

### Where templates appear
<a name="brand-assets-user-where"></a>

When you ask Quick to create a document or presentation, it shows you a plan before building: an outline and the design console, which has a **Visual Style** section. Quick preselects the closest match on the **Suggested** tab, so you can choose **Approve & Build** to create output that uses that template.

Quick chooses a template by matching your task against the **When to use** guidance that your brand managers wrote for each template. Your organization's approved templates are ranked ahead of built-in style presets. To choose differently, select another template from **Brands** (every brand published by your organization), upload another template in chat, choose from **Presets** (built-in Quick visual styles), or configure the look yourself in **Customize**.

## Reference
<a name="brand-assets-reference"></a>

### Supported source files
<a name="brand-assets-reference-files"></a>

Quick extracts a template from a PowerPoint or Word file. Both the working format and the native template format are accepted. Files can be up to 50 MB.


| File type | Extensions | Produces | 
| --- | --- | --- | 
| PowerPoint presentation | .pptx | A presentation template | 
| PowerPoint template | .potx | A presentation template | 
| Word document | .docx | A document template | 
| Word template | .dotx | A document template | 

If you upload any other file type, Quick shows an error that lists the accepted types.

### Permissions summary
<a name="brand-assets-reference-permissions"></a>


| Permission | Controls | Granted | Denied | 
| --- | --- | --- | --- | 
| Create and update brand kits | Who can curate brand assets. For default availability and configuration guidance, see [Assigning brand managers](#brand-assets-admin-delegate). | The user can extract, refine, publish, update, and delete brands for the organization. | The user can browse, download, and apply published brands, but can't change what the organization publishes. | 

## Troubleshooting
<a name="brand-assets-troubleshooting"></a>

**The Brand assets tab isn't available**  
Brand assets are available only in Amazon Quick Enterprise edition. Confirm that you signed in with your organization's Quick credentials rather than a social account, and that your administrator has made the feature available to your organization.

**You can't create or publish a brand**  
Ask your administrator to check whether the **Create and update brand kits** capability is turned off for you. For configuration guidance, see [Assigning brand managers](#brand-assets-admin-delegate).

**Quick can't retrieve my template from a connected source**  
Confirm that the service is connected on the **Connectors** tab and that you can open the file yourself. Quick uses your access, not an organization-wide account. If you can't open the file, ask its owner for access.

**Quick keeps picking the wrong template**  
The **When to use** guidance on the competing templates is probably too similar. A brand manager can sharpen both descriptions so the boundary between them is clear, and then publish the update.

**Generated output doesn't follow a brand rule**  
Confirm that the rule is recorded on the template, not only implied by the source file's design. A brand manager can add or correct the rule and publish the update. Review generated output against your brand guidelines before you share it.

**My generated presentation or document is missing content from the template**  
Note the template, the brand, and the request you made, and check the extraction report for any gaps Quick reported. Contact support with those details.

**A template is missing after you publish**  
Publishing uploads your entire copy of the brand, so an out-of-date copy can remove templates that others added. Templates removed this way can't be recovered. To avoid this, retrieve the latest published brand through Quick chat before editing, and make sure your copy includes the latest published content before you publish. For details, see [Publishing a brand](#brand-assets-manager-publish).