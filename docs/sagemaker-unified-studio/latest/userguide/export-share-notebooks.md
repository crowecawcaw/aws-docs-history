# Import and export notebooks

## Overview

Amazon SageMaker Unified Studio supports importing and exporting notebooks. You can import notebook files
from your local machine to migrate work from other environments, and export notebooks in multiple
formats for sharing and offline use.

## Import a notebook

You can import a notebook file from your local machine into your project. The import process
converts the file to a Amazon SageMaker Unified Studio notebook and recreates cells, cell outputs, and metadata from the
source file.

Supported import formats:

- Jupyter notebook (`.ipynb`)
- Amazon SageMaker Unified Studio native JSON (`.json`)
- Python script (`.py`)

###### To import a notebook

1. In the navigation pane, choose **Notebooks**.
2. Choose the dropdown arrow next to **Create notebook**, and then choose
   **Import notebook**.
3. In the **Import notebook** dialog box, choose **Choose file**,
   or drag and drop a file. The file must be in `.ipynb`, `.json`,
   or `.py` format, with a maximum size of 50 MiB.
4. Choose **Import**.

Once imported, the notebook opens and ready to use. Here, you can edit the name, description,
cells and run the notebook.

What gets preserved during import:

- All cell types: Document, Code, and Visualization
- Cell outputs and execution history, when available in the source file
- Amazon SageMaker Unified Studio metadata such as connection IDs and cell configurations, when available

The following table describes the import limits.

| Resource                          | Limit  |
| --------------------------------- | ------ |
| Maximum file size                 | 50 MiB |
| Maximum cells per notebook        | 200    |
| Maximum cell content size         | 300 KB |
| Maximum cell run results per cell | 100    |
| Maximum cell run results size     | 300 KB |

###### Note

The notebook cannot be modified while an import is in progress. Import is all-or-nothing —
either the entire notebook imports successfully, or the import fails.

## Export a notebook

You can export a notebook to your local machine in multiple formats for sharing and offline use.

Supported export formats:

- Jupyter notebook with requirements (`.zip`)
- Jupyter notebook (`.ipynb`)
- Python (`.py`)
- Notebook (`.json`)

###### To export a notebook

1. Open the notebook you want to export.
2. In the notebook toolbar, choose the more options menu (three vertical dots).
3. Choose **Download**, and then select your desired format:
   - Jupyter notebook with requirements (`.zip`) — includes the notebook and a requirements file for reproducing the environment
   - Jupyter notebook (`.ipynb`) — for use with other Jupyter-compatible environments
   - Python (`.py`) — extracts code cells as a Python script
   - Notebook (`.json`) — Amazon SageMaker Unified Studio native format

The file downloads to your local machine.

###### To download results and data

1. Execute code that generates output files or processed datasets.
2. Use the download interface to save files to your local machine or Copy to clipboard.
3. Select the output format (CSV or JSON or pdf).
