

# Supported languages for business rules extraction
<a name="transform-app-mainframe-reimagine-supported"></a>

AWS Transform runs a reimagine job that analyzes your code and data, identifies business domains, extracts business logic, and generates modernization requirements for each business domain. This topic covers the business rules extraction (BRE) step of that job: the step that recovers the legacy logic from your source.

Business rules are not the final deliverable: they are the foundation of the extraction, the layer in which AWS Transform captures the legacy logic recovered from your source, and the modernization requirements are built on top of them. Those modernization requirements are the primary input for forward engineering. Understanding what business rules extraction supports therefore matters because it bounds how completely the legacy logic is recovered, and so what the modernization requirements can be built from. This topic explains how source constructs are represented in the extracted rules, lists the supported source languages, and links to a reference page for each.

The reimagine workflow runs several specialized agents. This topic describes the business rules extraction step, and the language support it describes applies to that step.

## How business rules work
<a name="transform-app-mainframe-reimagine-supported-representation"></a>

Business rules extraction produces a set of business rules, not a classification of your source statements. The categories below are not something AWS Transform emits; they are a way to understand how a given construct contributes to that output, so that you can read the language reference pages and set expectations for what appears in the rules. Not every line of source code becomes its own business rule. It helps to distinguish the statements that produce a business rule from those that contribute to one, those that only provide context, and those that are read but not represented in the rules. Each language reference page uses these same categories.


| Category | What it means | 
| --- | --- | 
| Generates a rule | The construct produces a business rule. The extracted rule is built around this action, and the surrounding logic is described in relation to it. Examples include statements that write data, present a screen, call a program, or run a database manipulation operation (such as INSERT, UPDATE, or DELETE). | 
| Contributes to a rule | The construct does not produce a rule on its own, but its effect enters the wording of a rule produced by a nearby statement. This includes conditions, computations, retrievals, and decisions that shape a rule, as well as value assignments and field initializations whose effect is preserved in the rule they feed rather than reported separately. Examples include conditional logic, loops, calculations, database reads, and value assignments. | 
| Shapes rules as context | The construct does not appear as a rule, but it resolves the fields, records, files, and keys that the rules reference, so it shapes their content. Examples include data and file declarations and record layouts. | 
| Not represented | The construct is read and recognized, but it has no effect on the extracted business rules, so it does not appear in them and does not change the logic that other rules describe. Examples include structural markers, dummy data sets, and options that do not alter business logic. | 

## Supported languages
<a name="transform-app-mainframe-reimagine-supported-languages"></a>

AWS Transform extracts business rules from the following mainframe source languages. The languages detection depends on the legacy source you provide. Select a language to see how its statements appear in the rules.
+ [COBOL z/OS](transform-app-mainframe-reimagine-cobol.md)
+ [JCL](transform-app-mainframe-reimagine-jcl.md)
+ [PL/I](transform-app-mainframe-reimagine-pli.md) (IBM Enterprise PL/I for z/OS)