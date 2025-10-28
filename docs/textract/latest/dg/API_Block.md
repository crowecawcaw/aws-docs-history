# Block

A `Block` represents items that are recognized in a document within a group
of pixels close to each other. The information returned in a `Block` object
depends on the type of operation. In text detection for documents (for example [DetectDocumentText](API_DetectDocumentText.md "API_DetectDocumentText.md")), you get information about the detected words and lines
of text. In text analysis (for example [AnalyzeDocument](API_AnalyzeDocument.md "API_AnalyzeDocument.md")), you can also get
information about the fields, tables, and selection elements that are detected in the
document.

An array of `Block` objects is returned by both synchronous and asynchronous
operations. In synchronous operations, such as [DetectDocumentText](API_DetectDocumentText.md "API_DetectDocumentText.md"), the
array of `Block` objects is the entire set of results. In asynchronous
operations, such as [GetDocumentAnalysis](API_GetDocumentAnalysis.md "API_GetDocumentAnalysis.md"), the array is returned over one
or more responses.

For more information, see [How Amazon Textract Works](how-it-works.md "how-it-works.md").

## Contents

**BlockType**

The type of text item that's recognized. In operations for text detection, the following
types are returned:

- _PAGE_ - Contains a list of the LINE `Block` objects
  that are detected on a document page.
- _WORD_ - A word detected on a document page. A word is one or
  more ISO basic Latin script characters that aren't separated by spaces.
- _LINE_ - A string of space-delimited, contiguous words that are
  detected on a document page.

In text analysis operations, the following types are returned:

- _PAGE_ - Contains a list of child `Block` objects
  that are detected on a document page.
- _KEY_VALUE_SET_ - Stores the KEY and VALUE `Block`
  objects for linked text that's detected on a document page. Use the
  `EntityType` field to determine if a KEY_VALUE_SET object is a KEY
  `Block` object or a VALUE `Block` object.
- _WORD_ - A word that's detected on a document page. A word is
  one or more ISO basic Latin script characters that aren't separated by spaces.
- _LINE_ - A string of tab-delimited, contiguous words that are
  detected on a document page.
- _TABLE_ - A table that's detected on a document page. A table
  is grid-based information with two or more rows or columns, with a cell span of one
  row and one column each.
- _TABLE_TITLE_ - The title of a table. A title is typically a
  line of text above or below a table, or embedded as the first row of a table.
- _TABLE_FOOTER_ - The footer associated with a table. A footer
  is typically a line or lines of text below a table or embedded as the last row of a
  table.
- _CELL_ - A cell within a detected table. The cell is the parent
  of the block that contains the text in the cell.
- _MERGED_CELL_ - A cell in a table whose content spans more than
  one row or column. The `Relationships` array for this cell contain data
  from individual cells.
- _SELECTION_ELEMENT_ - A selection element such as an option
  button (radio button) or a check box that's detected on a document page. Use the
  value of `SelectionStatus` to determine the status of the selection
  element.
- _SIGNATURE_ - The location and confidence score of a signature detected on a
  document page. Can be returned as part of a Key-Value pair or a detected cell.
- _QUERY_ - A question asked during the call of AnalyzeDocument. Contains an
  alias and an ID that attaches it to its answer.
- _QUERY_RESULT_ - A response to a question asked during the call
  of analyze document. Comes with an alias and ID for ease of locating in a
  response. Also contains location and confidence score.

The following BlockTypes are only returned for Amazon Textract Layout.

- `LAYOUT_TITLE` - The main title of the document.
- `LAYOUT_HEADER` - Text located in the top margin of the document.
- `LAYOUT_FOOTER` - Text located in the bottom margin of the document.
- `LAYOUT_SECTION_HEADER` - The titles of sections within a document.
- `LAYOUT_PAGE_NUMBER` - The page number of the documents.
- `LAYOUT_LIST` - Any information grouped together in list form.
- `LAYOUT_FIGURE` - Indicates the location of an image in a document.
- `LAYOUT_TABLE` - Indicates the location of a table in the document.
- `LAYOUT_KEY_VALUE` - Indicates the location of form key-values in a document.
- `LAYOUT_TEXT` - Text that is present typically as a part of paragraphs in documents.

Type: String

Valid Values: `KEY_VALUE_SET | PAGE | LINE | WORD | TABLE | CELL | SELECTION_ELEMENT | MERGED_CELL | TITLE | QUERY | QUERY_RESULT | SIGNATURE | TABLE_TITLE | TABLE_FOOTER | LAYOUT_TEXT | LAYOUT_TITLE | LAYOUT_HEADER | LAYOUT_FOOTER | LAYOUT_SECTION_HEADER | LAYOUT_PAGE_NUMBER | LAYOUT_LIST | LAYOUT_FIGURE | LAYOUT_TABLE | LAYOUT_KEY_VALUE`

Required: No

**ColumnIndex**

The column in which a table cell appears. The first column position is 1.
`ColumnIndex` isn't returned by `DetectDocumentText` and
`GetDocumentTextDetection`.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**ColumnSpan**

The number of columns that a table cell spans. `ColumnSpan` isn't returned by
`DetectDocumentText` and `GetDocumentTextDetection`.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**Confidence**

The confidence score that Amazon Textract has in the accuracy of the recognized text and
the accuracy of the geometry points around the recognized text.

Type: Float

Valid Range: Minimum value of 0. Maximum value of 100.

Required: No

**EntityTypes**

The type of entity.

The following entity types can be returned by FORMS analysis:

- _KEY_ - An identifier for a field on the document.
- _VALUE_ - The field text.

The following entity types can be returned by TABLES analysis:

- _COLUMN_HEADER_ - Identifies a cell that is a header of a column.
- _TABLE_TITLE_ - Identifies a cell that is a title within the
  table.
- _TABLE_SECTION_TITLE_ - Identifies a cell that is a title of a
  section within a table. A section title is a cell that typically spans an entire row
  above a section.
- _TABLE_FOOTER_ - Identifies a cell that is a footer of a table.
- _TABLE_SUMMARY_ - Identifies a summary cell of a table. A
  summary cell can be a row of a table or an additional, smaller table that contains
  summary information for another table.
- _STRUCTURED_TABLE_ - Identifies a table with column headers
  where the content of each row corresponds to the headers.
- _SEMI_STRUCTURED_TABLE_ - Identifies a non-structured table.

`EntityTypes` isn't returned by `DetectDocumentText` and
`GetDocumentTextDetection`.

Type: Array of strings

Valid Values: `KEY | VALUE | COLUMN_HEADER | TABLE_TITLE | TABLE_FOOTER | TABLE_SECTION_TITLE | TABLE_SUMMARY | STRUCTURED_TABLE | SEMI_STRUCTURED_TABLE`

Required: No

**Geometry**

The location of the recognized text on the image. It includes an axis-aligned, coarse
bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial
information.

Type: [Geometry](API_Geometry.md "API_Geometry.md") object

Required: No

**Id**

The identifier for the recognized text. The identifier is only unique for a single
operation.

Type: String

Pattern: `.*\S.*`

Required: No

**Page**

The page on which a block was detected. `Page` is returned by synchronous and
asynchronous operations. Page values greater than 1 are only returned for multipage
documents that are in PDF or TIFF format. A scanned image (JPEG/PNG) provided to an
asynchronous operation, even if it contains multiple document pages, is considered a
single-page document. This means that for scanned images the value of `Page` is
always 1.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**Query**

Type: [Query](API_Query.md "API_Query.md") object

Required: No

**Relationships**

A list of relationship objects that describe how blocks are related to each other. For
example, a LINE block object contains a CHILD relationship type with the WORD blocks that
make up the line of text. There aren't Relationship objects in the list for relationships
that don't exist, such as when the current block has no child blocks.

Type: Array of [Relationship](API_Relationship.md "API_Relationship.md") objects

Required: No

**RowIndex**

The row in which a table cell is located. The first row position is 1.
`RowIndex` isn't returned by `DetectDocumentText` and
`GetDocumentTextDetection`.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**RowSpan**

The number of rows that a table cell spans. `RowSpan` isn't returned by
`DetectDocumentText` and `GetDocumentTextDetection`.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**SelectionStatus**

The selection status of a selection element, such as an option button or check box.

Type: String

Valid Values: `SELECTED | NOT_SELECTED`

Required: No

**Text**

The word or line of text that's recognized by Amazon Textract.

Type: String

Required: No

**TextType**

The kind of text that Amazon Textract has detected. Can check for handwritten text and
printed text.

Type: String

Valid Values: `HANDWRITING | PRINTED`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/textract-2018-06-27/Block.md "../../../goto/SdkForCpp/textract-2018-06-27/Block.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/textract-2018-06-27/Block.md "../../../goto/SdkForJavaV2/textract-2018-06-27/Block.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/textract-2018-06-27/Block.md "../../../goto/SdkForRubyV3/textract-2018-06-27/Block.md")
