# Step 1: Create an Amazon Kendra Index

Begin by creating an Amazon Kendra index of documents that answer customer questions. An index
provides a search API for client queries. You create the index from source documents.
Amazon Kendra returns answers it finds in indexed documents to the bot, which displays them to
the agent.

The quality and accuracy of the responses suggested by Amazon Kendra depend on the documents
that you index. Documents should include files that are frequently accessed by the agent
and must be stored in an S3 bucket. You can index unstructured and semi-structured data
in .html, Microsoft Office (.doc, .ppt), PDF, and text formats.

To create an Amazon Kendra index, see [Getting started with an S3 bucket
(console)](../../../kendra/latest/dg/gs-console.md "../../../kendra/latest/dg/gs-console.md") in the _Amazon Kendra Developer Guide_.

To add questions and answers (FAQs) that help answer customer queries, see [Adding questions
and answers](../../../kendra/latest/dg/in-creating-faq.md "../../../kendra/latest/dg/in-creating-faq.md") in the _Amazon Kendra Developer Guide_. For this
tutorial, use the [ML_FAQ.csv file on GitHub.](https://github.com/awsdocs/amazon-lex-developer-guide/blob/master/example_apps/agent_assistance_bot/ML_FAQ.csv "https://github.com/awsdocs/amazon-lex-developer-guide/blob/master/example_apps/agent_assistance_bot/ML_FAQ.csv")

## Next step

[Step 2: Create an Amazon Lex V2 Bot](agent-step-2.md "agent-step-2.md")
