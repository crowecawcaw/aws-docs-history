

# Knowledge Sources
<a name="knowledge-sources"></a>

Knowledge Sources are documents you share with Amazon Connect Decisions that give it context about your operations and monitoring requirements. Amazon Connect Decisions analyzes them and uses that understanding to inform how metrics, rules, and guidelines are configured in subsequent steps. Typical sources include SOPs, business policies, and operational guidelines.

**What to share:** Effective Knowledge Sources include documents that describe how your business operates and how you manage supply chain issues. Examples include:
+ Inventory management SOPs (e.g., how you respond to stockouts, when to expedite replenishment, safety stock policies)
+ Demand planning policies (e.g., how you handle seasonal demand, promotional lift, or new product introductions)
+ Supplier management guidelines (e.g., lead time assumptions, preferred carrier rules, escalation procedures)
+ Operational constraints (e.g., warehouse capacity limits, order minimums, regional fulfillment rules)

The more specific your documents are to your actual processes, the more accurately Amazon Connect Decisions can generate relevant metrics, rules, and guidelines on your behalf.
+ **Supported formats:** PDF, Word, and plain text files are supported.
+ **Template:** A Knowledge Source template is available for download to help you structure your inputs. Use it as a starting point if you do not have existing documentation.

To share a Knowledge Source:

1. From the Insights Configuration page, select the **Knowledge Sources** tab.

1. Download and complete the template if needed, or gather your existing documents.

1. Click **Upload** and select your file. Amazon Connect Decisions will process the document and confirm when it is ready to generate further configurations.

## Tips
<a name="knowledge-sources-tips"></a>
+ Share multiple sources to give Amazon Connect Decisions comprehensive context; a single SOP is a good starting point, but adding related policies and guidelines improves output quality.
+ You can share additional Knowledge Sources at any point during configuration, not only at the start. If you update a source document, share the new version to keep Amazon Connect Decisions current.
+ Knowledge Sources provide reference context; they do not directly create metrics, rules, or guidelines on their own. Use Detection and Guidelines configuration to act on what Amazon Connect Decisions learns.