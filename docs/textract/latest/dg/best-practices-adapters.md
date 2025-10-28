# Best practices for Amazon Textract Custom

Queries

Amazon Textract lets you customize the output of its pretrained Queries feature by
training and using an adapter for its base model. With Amazon Textract Custom Queries, you
can use your own documents and train an adapter to customize the base model, while
keeping control over your proprietary documents. When creating queries for your
adapters, use the following best practices. For more information about adapters, see
[Customizing your Queries Responses](textract-using-adapters.md "textract-using-adapters.md").

1. The sample data should contain layout variations and image variations that are
   representative of the documents to be used in production.
2. A minimum of five samples (per query level) are required for either training
   or testing. The more samples used for training, the better.
3. The annotated Queries should have a variety of answers. For example, if the
   answer to a query is 'Yes' or 'No,' the annotated samples should have
   occurrences of both 'Yes' and 'No,'
4. Composed queries should have logical meanings and structures. For example, to
   extract a payee name on the check, the query should be ‘Who is the payee?’ and
   not ‘What is the name?’.
5. If a value that needs to be extracted has an associated key, include the key
   in the query for better results. If there are keys that occur multiple times,
   use hierarchical questions such as ‘What is the first name under borrower?’ and
   ‘What is the first name under co-borrower?’
6. Maintain consistency in annotation style. If a field appears in multiple
   places on a document and you decide to annotate only one occurrence, follow the
   same guideline and annotate only one occurrence in all documents. Alternatively,
   if you choose to annotate all occurrences of a value, follow the same process
   for all documents.
7. Maintain consistency while annotating fields with spaces. If a field's value
   is ‘123 456 78’ and if you choose to annotate it as ‘12345678’ follow the same
   guideline for all documents. Do not change between annotating the value as ‘123
   456 78’ and ‘12345678.’
8. Annotate the data across all pages within a document even though you might run
   inference on only a few of the pages. If annotating all the pages is not
   feasible, split the document and use only the pages that you are able to
   annotate in your dataset.
9. Custom Queries does not support questions related to signatures (such as, 'Is
   the document signed?'). To know if a document is signed, use the signatures
   feature in your API request.
10. When correcting responses from pre-labeling, you can make small modifications
    to the text presented in the documents, such as correcting a few character
    errors, or removing spaces and punctuation. But if text isn't shown in the
    documents, don't enter it as a response.
11. Use the exact query used in training for inference.
12. Provide pre-labeling results only for the `source-ref` page. If you
    have pre-labeling results with Blocks that aren't from the
    `source-ref` page, it might impact performance.
