

# Working with Amazon Quick Sight Topics
<a name="topics"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  Amazon Quick administrators and authors  | 

A *Topic* in Quick Sight is the multi-dataset semantic layer that brings multiple enriched datasets together into a unified data model. Topics let you define relationships between datasets so that Quick Sight can perform runtime joins across them — whether you're building analysis visuals or asking natural language questions through Amazon Quick chat.

With Topics, you can:
+ Add up to 12 datasets to a single Topic and define relationships (join keys) between them.
+ Add custom instructions that guide the AI engine on cross-dataset logic, disambiguation rules, and business definitions.
+ Use the Topic as a data model in Quick Sight analysis sheets to build visuals with fields from multiple datasets — Quick Sight performs runtime inner joins automatically.
+ Use the Topic in Amazon Quick chat where the LLM-powered chat agent traverses relationships across datasets, generates cross-dataset SQL with appropriate joins, and returns unified answers.
+ Preserve each dataset at its native granularity — no pre-joining or denormalization required.

Each dataset in a Topic should be independently enriched with semantic metadata (column descriptions, synonyms, semantic types, and custom instructions) before being added to the Topic. For more information about enriching datasets, see [Data Preparation Experience (New)](data-prep-experience-new.md).

**Note**  
If you have existing Topics that were created before this release, they are now classified as *legacy Topics*. Legacy Topics continue to work as before. For more information, see [Working with legacy Topics](legacy-topics.md).

To learn more about working with Topics, continue to the following sections.

**Topics**
+ [How Topics work](topics-how-it-works.md)
+ [Creating Quick Sight Topics](topics-create.md)
+ [Defining relationships between datasets in a Topic](topics-relationships.md)
+ [Adding custom instructions to a Topic](topics-custom-instructions.md)
+ [Using Topics in Quick Sight analysis](topics-in-analysis.md)
+ [Using Topics in Amazon Quick chat](topics-in-chat.md)
+ [Sharing Quick Sight Topics](topics-sharing.md)
+ [Working with legacy Topics](legacy-topics.md)
+ [Work with Quick Sight Topics using the Amazon Quick Sight APIs](topics-cli.md)