

# Excel
<a name="actions-excel"></a>

Excel actions enable you to read, update, and create Excel files in your automations. All Excel actions support both .xlsx and .xlsm file formats. Workbook identifiers maintain references across multiple operations.

**Note**  
While values can be read from .xlsm files, macro execution is not supported.

## Create New Workbook
<a name="create-new-workbook"></a>

Creates a blank Excel file. Outputs a workbook identifier you can use to update the spreadsheet in subsequent steps.

**Properties:**
+ **Workbook Identifier** (output): Variable name storing the workbook reference for future actions (default: `workbook_id`)

## Open Existing Workbook
<a name="open-existing-workbook"></a>

Loads an existing Excel file. Returns a workbook identifier you can use to update the spreadsheet in subsequent steps. Supports only Excel (.xlsx) files.

**Properties:**
+ **Excel File** (required): The .xlsx file to open, typically stored in a variable (e.g., `my_file`)
+ **Workbook Identifier** (output): Variable name storing the workbook reference (default: `workbook_id`)

**File Requirements:**
+ Must be a valid Excel (.xlsx) file
+ File must be accessible as a media file object

## Save Workbook
<a name="save-workbook"></a>

Saves updates to an Excel file. Allows you to update the file name and file type for the saved workbook.

**Properties:**
+ **File Name** (required): Name for the saved file without extension (e.g., "Monthly Report")
+ **File Type** (dropdown): Output format - currently supports XLSX (default: XLSX)
+ **Saved File** (output): Variable storing the saved file object (default: `saved_file`)

## Read Sheet
<a name="read-sheet"></a>

Gets data from a range of cells. The action stores the output in a data table variable.

**Properties:**
+ **Workbook Identifier** (required): The workbook to read from (e.g., `workbook_id`)
+ **Sheet Name** (required): Worksheet or tab name (default: "Sheet1")
+ **Cell Range** (optional): Range specification - supports multiple formats:
  + Starting cell: "A2" (reads all data from anchor point)
  + Exact range: "A1:B10"
  + Column range: "A:B"
  + Row range: "1:3"
  + Empty: reads entire sheet
+ **Include Headers** (checkbox): Treats first row as column headers when enabled. When disabled, uses default naming (Column0, Column1, etc.) (default: TRUE)
+ **Data Table** (output): Variable storing the extracted data (default: `excel_table`)

**Formula Handling:**
+ The action automatically calculates formulas and stores results in the data table.

## Read Cell
<a name="read-cell"></a>

Gets the value from a cell. Used to read an individual cell value from a worksheet.

**Properties:**
+ **Workbook Identifier** (required): The workbook to read from (e.g., `workbook_id`)
+ **Sheet Name** (required): Worksheet name (default: "Sheet1")
+ **Cell Reference** (required): Cell location (e.g., "A1")
+ **Cell Value** (output): Variable storing the cell content (default: `cell_value`)

## Write to Sheet
<a name="write-to-sheet"></a>

Outputs a data table to a sheet. Used to write a range of rows and columns to a worksheet.

**Properties:**
+ **Data Table** (required): The data table to write (e.g., `my_table`)
+ **Workbook Identifier** (required): Target workbook (e.g., `workbook_id`)
+ **Sheet Name** (required): Target worksheet (default: "Sheet1")
+ **Start at Cell** (optional): Starting position for data placement (default: "A1")
+ **Include Headers** (checkbox): Writes column headers when enabled (default: TRUE)

## Write to Cell
<a name="write-to-cell"></a>

Outputs a value to a cell. Used to update individual cells in a worksheet.

**Properties:**
+ **Value to Write** (required): Content for the cell (e.g., "Order \#12345")
+ **Workbook Identifier** (required): Target workbook (e.g., `workbook_id`)
+ **Sheet Name** (required): Target worksheet (default: "Sheet1")
+ **Cell Reference** (required): Target cell location (e.g., "A1")

## Write New Row
<a name="write-new-row"></a>

Adds a row of data to the sheet. The new row is appended to the end of the existing data.

**Properties:**
+ **Row Values** (required): Array of values for the new row, starting from first column (e.g., ["Q1", "Sales", 100])
+ **Workbook Identifier** (required): Target workbook (e.g., `workbook_id`)
+ **Sheet Name** (required): Target worksheet (default: "Sheet1")

**Data Validation:**
+ Must provide values as an array format
+ Values are written sequentially starting from the first column

## Create New Sheet
<a name="create-new-sheet"></a>

Adds a blank worksheet. The new sheet is added to the end of the workbook.

**Properties:**
+ **Workbook Identifier** (required): Target workbook (e.g., `workbook_id`)
+ **Sheet Name** (required): Name for the new worksheet (e.g., "Sales Data")

## Copy Sheet
<a name="copy-sheet"></a>

Creates a copy of the worksheet. The new sheet is created within the same workbook.

**Properties:**
+ **Workbook Identifier** (required): Target workbook (e.g., `workbook_id`)
+ **Sheet Name to Copy** (required): Source worksheet name (e.g., "Original Sheet")
+ **New Sheet Name** (required): Name for the duplicated sheet (e.g., "Original Sheet (Copy)")

## Rename Sheet
<a name="rename-sheet"></a>

Updates the name of an existing worksheet.

**Properties:**
+ **Workbook Identifier** (required): Target workbook (e.g., `workbook_id`)
+ **Current Sheet Name** (required): Existing worksheet name (e.g., "Sheet1")
+ **Updated Sheet Name** (required): New name for the worksheet (e.g., "Q1 Data")

## Delete Sheet
<a name="delete-sheet"></a>

Removes a sheet from a workbook. Cannot delete the last remaining sheet of a workbook.

**Properties:**
+ **Workbook Identifier** (required): Target workbook (e.g., `workbook_id`)
+ **Sheet Name to Delete** (required): Worksheet to remove (e.g., "Sheet1")

**Constraints:**
+ Cannot delete the last remaining sheet in a workbook

## Set Cell Color
<a name="set-cell-color"></a>

Updates cell background color. Used to highlight a specific range of cells.

**Properties:**
+ **Cell Color** (required): RGB hex code format (e.g., "FF0000" for red)
+ **Workbook Identifier** (required): Target workbook (e.g., `workbook_id`)
+ **Sheet Name** (required): Target worksheet (e.g., "Sheet1")
+ **Cell Range** (required): Range to format - supports:
  + Single cell: "A1"
  + Exact range: "A1:B10"
  + Column range: "A:B"
  + Row range: "1:3"

## Get Cell Color
<a name="get-cell-color"></a>

Reads the cell background color. Outputs the color in RGB hex code format (e.g., "FF0000" for red).

**Properties:**
+ **Workbook Identifier** (required): Source workbook (e.g., `workbook_id`)
+ **Sheet Name** (required): Source worksheet (e.g., "Sheet1")
+ **Cell Reference** (required): Cell to read (e.g., "A1")
+ **Cell Color** (output): Variable storing RGB hex code (default: `cell_color`)

## Hide Rows
<a name="hide-rows"></a>

Makes rows hidden in the sheet. The data remains intact but is not visible.

**Properties:**
+ **Workbook Identifier** (required): Target workbook (e.g., `workbook_id`)
+ **Sheet Name** (required): Target worksheet (e.g., "Sheet1")
+ **Start Row** (required): First row number to hide (Excel numbering starts at 1)
+ **End Row** (optional): Last row number to hide. If empty, only the start row is hidden

**Row Numbering:**
+ Excel row numbers start at 1 (not 0)
+ Must provide integer values

## Unhide Rows
<a name="unhide-rows"></a>

Makes hidden rows visible. Used to show previously hidden rows.

**Properties:**
+ **Workbook Identifier** (required): Target workbook (e.g., `workbook_id`)
+ **Sheet Name** (required): Target worksheet (e.g., "Sheet1")
+ **Start Row** (required): First row number to unhide (Excel numbering starts at 1)
+ **End Row** (optional): Last row number to unhide. If empty, only the start row is made visible

## Best practices and limitations
<a name="excel-best-practices-limitations"></a>

### Workbook Identifier Management
<a name="excel-workbook-identifier-management"></a>
+ Store workbook identifiers in descriptive variables (e.g., `sales_workbook`, `report_file`)
+ Reuse the same identifier across multiple actions on the same workbook
+ Always create or open a workbook before performing data operations

### Range Specifications
<a name="excel-range-specifications"></a>
+ Use exact ranges ("A1:B10") for precise data operations
+ Use column ranges ("A:B") when working with entire columns
+ Use row ranges ("1:3") for header or summary operations
+ Leave range empty to process entire sheets

### Performance Optimization
<a name="excel-performance-optimization"></a>
+ Read entire ranges when possible instead of individual cells
+ Batch write operations using data tables rather than individual cell writes
+ Save workbooks only when all modifications are complete

### Limitation
<a name="excel-limitation"></a>

File compatibility is limited to modern Excel (.xlsx) format only - legacy Excel (.xls) files are not supported.