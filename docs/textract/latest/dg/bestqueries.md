

# Best practices for Queries

## Example Queries
<a name="example-queries"></a>

Download the [Example Queries document](samples/Example%20Queries.zip) to see examples of queries for common document types across mortgage, insurance, healthcare, and tax industries.

## General best practices for Queries
<a name="generalbestqueries"></a>

### Extracting cells from tables
<a name="w2aac22c41c11b7b3"></a>

Construct a query that contains words from both row header and column header.

Examples, for the image below:

*Query 1: What date was the 2nd dose administered?*

*Answer 1: 2/8/2021*

*Query 2: Who is the manufacturer of the 1st dose?*

*Answer 2: Pfizer*

![Sample vaccination record card showing personal details like name, date of birth, ID number, and entries for multiple vaccine doses with product name, date, and healthcare professional initials.](https://docs.aws.amazon.com/textract/latest/dg/images/best-practice-cells.png)


### Extracting tables using Queries
<a name="w2aac22c41c11b7b5"></a>

Extraction of entire tables or whole rows or columns of information using Queries is not supported.

### Long answers
<a name="w2aac22c41c11b7b7"></a>

Long answers increase response latency and can lead to timeouts. Try to ask questions with expected answers of less than 100 words.

### Passing only hints
<a name="w2aac22c41c11b7b9"></a>

Passing only the key name as the question will work when trying to extract standard key-value pairs from a form. Frame full questions for all other extraction use cases.

Examples, for the image below:

*Query 1: Borrower's Name.*

*Answer 1: Carlos Salazar*

*Query 2: Social Security Number.*

*Answer 2: 999-99-9999*

![Form field for borrower details including name, social security number, marital status, and address.](https://docs.aws.amazon.com/textract/latest/dg/images/best-practice-hints.png)


### General phrasing of questions
<a name="w2aac22c41c11b7c11"></a>

Where possible, use words from the document to construct the query.
+ While Queries tries to do acronym and/or synonym matching for some common industry terms (SSN vs Tax ID vs Social Security Number), using language directly from the document will improve results.
+ Example: If the document says "job progress", try to avoid calling it using other variations like "project progress" or "program progress" or "job status".

In general, ask a natural language question that starts with "What is / Where is / Who is...". The exception to this rule is when trying to extract standard key-value pairs, in which case you can pass the key name as a query.

Avoid ill-formed or grammatically incorrect questions since these could result in unexpected answers. 
+ Example of ill-formed Query: When?
+ Example of well-formed Query: When was the first vaccine dose administered?

Be as specific as possible. Some examples follow:
+ When the document contains multiple sections (for example, "Borrower" and "Co-Borrower") and both sections have a field called SSN, ask: "What is the SSN for Borrower?" and "What is the SSN for Co-Borrower?"
+ When the document has multiple date-related fields, be specific in the query language and ask "What is the date the document was signed on?" or "What is the date of birth of the applicant?" Avoid asking ambiguous questions like "What is the date?"

If you know the layout of the document beforehand, giving location hints improves the accuracy of the results. For example, "What is the date at the top?" or "What is the date on the left?" or "What is the date at the bottom?"

## Setting up pages for Queries
<a name="querypages"></a>

When working with Queries for multipage documents, you can use the `Page` parameter to specify which pages to look for the query answer on. What follows is a list of best practices for setting up Pages:
+ If a page is not specified, it is set to `["1"]` by default.
+ The following characters are allowed in the parameter's string: `0 1 2 3 4 5 6 7 8 9 - *`. No whitespace is allowed.
+ When using \* to indicate all pages, it must be the only element in the list.
+ You can use page intervals, such as `["1-3", "1-1", "4-*"]`. Where `*` indicates the last page of the document.
+ Specified pages must be greater than 0 and less than or equal to the number of pages in the document.