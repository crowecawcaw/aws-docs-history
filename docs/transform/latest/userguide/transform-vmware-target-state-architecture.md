

# Target state architecture
<a name="transform-vmware-target-state-architecture"></a>

AWS Transform can draft a target state architecture and a detailed design for each application that you plan to migrate. The design follows lift-and-shift migration patterns. AWS Transform starts from an infrastructure document that describes the application. From that document, it answers a discovery questionnaire, draws the target architecture, and writes a Detailed Design Document. You review each output.

To start, choose the **Application Design** job type when you create a job, or add the **Application design** step to your job. You can also ask in the chat, for example, "We'd like a detailed design for one of our applications. What do you need from us?"

## What you provide
<a name="transform-vmware-target-state-architecture-inputs"></a>

For each application, upload one infrastructure document. For example, upload an interview transcript, an infrastructure requirements (IR) document, or a technical specification. Word (.docx) and PDF files are accepted.

To also generate firewall rules, upload a network connection export for the application, such as a ModelizeIT `CONNECTION.csv` file.

A server inventory, such as an RVTools export or a discovery tool export, is not enough on its own. An inventory lists your servers. It doesn't include what the design is built from: application tiers, dependencies and their ports, service tier, and recovery objectives. If you ask for a target state architecture without an infrastructure document, AWS Transform asks you for one.

## What AWS Transform produces
<a name="transform-vmware-target-state-architecture-outputs"></a>

AWS Transform delivers each of the following files in the chat for you to download.


**Target state architecture outputs**  

| Output | Format | Description | 
| --- | --- | --- | 
| Discovery questionnaire | CSV | The questionnaire answered from your infrastructure document. AWS Transform marks questions that the document doesn't answer as not mentioned. | 
| Target state architecture diagram | Draw.io (.drawio) | The AWS architecture for the application, including its on-premises and external dependencies. AWS Transform shows values that aren't known yet as TBD. | 
| Firewall rules | Markdown and CSV | Rules derived from your network connection export, with source, destination, port, and protocol. AWS Transform generates these rules only when you provide a connection export. | 
| Detailed Design Document | Markdown | A design document that summarizes the application, its current on-premises details, and the target design. | 

AWS Transform pauses three times for your review. It pauses after it answers the questionnaire, after it delivers the diagram, and after it delivers the Detailed Design Document. You can ask AWS Transform to rerun any step. Each run replaces the earlier output.

## Architecture templates
<a name="transform-vmware-target-state-architecture-templates"></a>

AWS Transform selects an architecture template that matches the application. The standard templates cover one-tier, two-tier, and three-tier applications at gold, silver, and titanium service tiers. Some templates include Citrix access or Oracle or Exadata databases. If the infrastructure document doesn't state the application's architecture and service tier, AWS Transform doesn't guess. It doesn't select a template for that application.

You can replace the standard set with your own templates. Supply a questionnaire template, Draw.io architecture templates, and a report template. You can also supply pattern cards that describe when to use each template.

Upload each file individually, not as an archive. Keep the original file names, because pattern cards refer to templates by file name. When you supply your own templates, AWS Transform uses them instead of the standard templates. If you change the templates after some applications are designed, AWS Transform lists those applications and redoes them after you agree.

## Example prompts
<a name="transform-vmware-target-state-architecture-prompts"></a>
+ "We'd like a detailed design for one of our applications. What do you need from us?"
+ "I've uploaded the discovery interview transcript for our OrderPortal application. Please work up the detailed design for OrderPortal."