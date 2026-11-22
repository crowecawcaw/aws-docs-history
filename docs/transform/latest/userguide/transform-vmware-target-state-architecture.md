

# Application design

AWS Transform can draft a lift-and-shift target architecture and a detailed design for each application that you plan to migrate. AWS Transform starts from an infrastructure document that describes the application. From that document, it answers a discovery questionnaire, draws the target architecture, and writes a Detailed Design Document. You review each output. If you upload a network connection export, AWS Transform also generates firewall rules.

After you create your job, the first chat message offers ways to start. Choose **Application Design**, or choose **Choose My Own Steps** and select **Application design**. You can also ask in the chat: "We'd like a detailed design for one of our applications. What do you need from us?"

## What you provide
<a name="transform-vmware-target-state-architecture-inputs"></a>

For each application, upload one infrastructure document, such as an infrastructure requirements document or an application discovery call transcript. You can use text, Microsoft Word (`.docx`), and PDF files.

To also get firewall rules, upload a network connection export for the application: a comma-separated values (CSV) file with one row for each connection. Include source, destination, and destination port columns, using ModelizeIT names (`HOST_FROM`, `HOST_TO`, `PORT_TO`) or common names (`SOURCE_IP`, `DEST_IP`, `DEST_PORT`).

A server inventory, such as an RVTools export, is not enough on its own. An inventory lists your servers. It doesn't include what the design is built from: application tiers, dependencies and their ports, service tier, and recovery objectives. If you ask for a lift-and-shift target architecture without an infrastructure document, AWS Transform asks you for one.

## How application design works
<a name="transform-vmware-target-state-architecture-workflow"></a>

1. AWS Transform answers the discovery questionnaire from facts in your infrastructure document. It doesn't guess or fill in common defaults. Unanswered questions read `Not mentioned` and appear as gaps. Ruled-out questions read `Not applicable` when the question offers that answer.

1. AWS Transform shows you the answers in the chat. You review them and fill in the gaps. Corrections are easiest at this point, because the diagram and the Detailed Design Document are built from these answers.

1. AWS Transform selects the architecture template that fits the application. It tells you which template it chose. When a pattern card describes the template, it also tells you why. It draws the diagram. Values that the questionnaire doesn't answer appear as `TBD`.

1. AWS Transform delivers the diagram and answered questionnaire. You review the diagram and approve it in the chat. To change the template or any content, tell AWS Transform in the chat.

1. If you uploaded a connection export, AWS Transform generates firewall rules. It tells you which rules to confirm with your security team before you allow that traffic.

1. AWS Transform writes the Detailed Design Document. You review it and approve it in the chat.

AWS Transform designs one application at a time, repeating these steps for each application. You can ask AWS Transform to rerun any step. When AWS Transform reruns a step for an application, it writes that application's files again. Files from different applications can have the same names, so download each application's files when its design is done and keep them apart.

## What AWS Transform produces
<a name="transform-vmware-target-state-architecture-outputs"></a>

AWS Transform delivers each of the following files in the chat for you to download.


| Output | Format | Description | 
| --- | --- | --- | 
| Discovery questionnaire | CSV | The questionnaire answered from your infrastructure document, based on the standard questionnaire template or the template that you provide. AWS Transform delivers it with the diagram. | 
| Lift-and-shift target architecture diagram | draw.io (.drawio) | The diagram shows the AWS architecture for the application, including its on-premises and external dependencies. It uses the standard lift-and-shift templates or the custom templates that you provide. The standard two-tier and three-tier templates have Development, quality assurance (QA), and Production pages. AWS Transform keeps the page of each environment that your document names. The QA page covers test stages such as user acceptance testing (UAT) and staging. If your document names no environment, AWS Transform keeps only Production. The single-server template has a Production page only. | 
| Firewall rules | Markdown | Rules from your connection export, with source, destination, port, protocol, and a note on each rule to confirm. AWS Transform generates these rules only when you provide a connection export. | 
| Detailed Design Document | Markdown | A design document that summarizes the application, its technical dependencies, and the target design, based on the standard Detailed Design Document template or the template that you provide. | 

## Architecture templates
<a name="transform-vmware-target-state-architecture-templates"></a>

AWS Transform selects the architecture template that matches the application. It considers the architecture, service tier, database, and Citrix access. The standard templates cover the following:
+ Single-server (one-tier) applications have one template.
+ Two-tier applications with Citrix have gold and silver templates.
+ Three-tier applications have gold and silver templates, with or without Citrix access.
+ Three-tier applications on Oracle Database 19c with Citrix access have a gold template only.
+ Three-tier applications on Oracle Exadata have gold, silver, and titanium templates. The titanium template adds a disaster recovery Region.

Gold, silver, and titanium are standard service tier names. If your document omits the architecture, AWS Transform asks instead of guessing. For an unstated or different service tier, it asks which standard tier fits.

If no template fits, as for a two-tier application without Citrix, AWS Transform tells you which answers decided it. You can then correct an answer, supply your own template and pattern card, or continue without the diagram.

For each kind of file that you don't supply, AWS Transform uses its standard one. If you supply any architecture templates, AWS Transform uses only your templates. It doesn't use the standard templates or the standard pattern cards.

Pattern cards are optional, short Markdown files describing when to use each template. Without cards, AWS Transform selects by words in the file name, such as `3-tier`, `citrix`, or `exadata`. It ignores the service tier, so if you supply more than one template, supply a card for each. You can supply:
+ A questionnaire template: a text file with each question ending in a colon.
+ draw.io architecture templates: `.drawio` or `.xml` files.
+ Pattern cards: Markdown files.
+ A Detailed Design Document template: a Markdown file.

In your own questionnaire template, keep the questions that contain `architecture pattern`, `service tier`, `Citrix server`, and `database type`. AWS Transform uses their answers to select templates. Ask for the architecture pattern as `1-tier`, `2-tier`, or `3-tier`.

Upload each file individually, not as an archive. Keep the original file names, because pattern cards refer to templates by file name. If you change any of these files later, AWS Transform lists the applications that it already designed. After you agree, it redoes them, and you approve each one again.

## How application design fits your migration plan
<a name="transform-vmware-target-state-architecture-planning"></a>

The application design describes each application's lift-and-shift target state on AWS, including its tiers and its technical dependencies on other systems. Application design is a step of its own, outside the **End-to-End Migration** journey. To add it to a job, choose it in the first chat message of your job or ask for it in the chat.

## Example prompts
<a name="transform-vmware-target-state-architecture-prompts"></a>
+ "We'd like a detailed design for one of our applications. What do you need from us?"
+ "I've uploaded the application discovery call transcript for our OrderPortal application. Please work up the detailed design for OrderPortal."
+ "I've uploaded our architecture templates and pattern cards. Use them for the rest of the applications in this job."
+ "I've uploaded the discovery call transcript for our Billing application. Design Billing next."