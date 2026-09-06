

# Browsing job attachments in Deadline Cloud
<a name="browse-job-attachments"></a>

Use the job attachments browser in the Deadline Cloud monitor to see the file structure of your job's input and output attachments. You can selectively download files, navigate the folder hierarchy, and filter by input or output. For supported file types, you can also preview content inline without downloading.

The attachments browser displays both input files (submitted with the job) and output files (produced by workers during processing). You can filter the view to show only inputs, only outputs, or all files together.

## Opening the attachments browser
<a name="browse-job-attachments-open"></a>

You can open the attachments browser from a job, step, or task. The scope of files displayed depends on the level from which you open the browser.

**To browse attachments for a job**

1. Follow the steps in [View and manage job details in Deadline Cloud](view-a-job.md) to view a list of jobs.

1. Select the job that you want to browse attachments for.

1. From the **Actions** menu, choose **Browse attachments**.

To view attachments for a specific step or task, select the step or task, and then choose **Browse attachments** from the **Actions** menu. When you browse at the step or task level, the browser shows only the output files that the step or task produced.

You can also open the context menu on a job, step, or task and choose **Browse attachments**.

## Navigating and filtering files
<a name="browse-job-attachments-navigate"></a>

The attachments browser displays files in an expandable tree structure organized by their original file paths. Use the following controls to navigate:
+ **Segment control** – Switch between viewing **All**, **Output**, or **Input** files.
+ **Text filter** – Filter the file list by name to find specific files.
+ **Previewable files only** – Turn on the **Previewable files only** toggle to show only files that support inline preview. Use this toggle when a folder mixes previewable files, such as JPG images, with formats that don't support preview, such as EXR images. Stepping through previews then skips the files without one.
+ **Folder expansion** – Choose a folder to expand or collapse its contents.

## Downloading files
<a name="browse-job-attachments-download"></a>

You can download individual files or a selection of files from the attachments browser.

**To download selected files**

1. In the attachments browser, select the checkboxes next to the files or folders that you want to download. Selecting a folder selects all files within that folder.

1. Choose **Download**.

1. Choose a download method:
   + **AWS Command Line Interface (AWS CLI)** – Downloads files to your storage profile paths, preserving the original directory structure. Use this method for large files or when you need files in their original locations.
   + **Browser download** – Downloads the selected files as a ZIP archive directly in your browser. Use this method for quick access to a small number of files. A warning appears when the total size exceeds 500 MB.

**Note**  
On the Deadline Cloud monitor desktop application (Windows, macOS, and Linux), the AWS CLI download runs directly without requiring you to copy a command. The desktop application also supports downloading files to their original storage profile paths.

## Previewing files
<a name="browse-job-attachments-preview"></a>

For supported file types, the attachments browser can display an inline preview without downloading the file.

**To preview a file**

1. In the attachments browser, select a file name in the table.

1. View the details panel that opens on the side. The panel shows metadata such as file size, path, and modification date. For supported file types, an inline preview loads automatically.

1. (Optional) To open a full-screen preview, choose the expand icon that appears when you hover over a file row.

The following file types support inline preview:
+ Images: PNG, JPG, JPEG, GIF, BMP, WebP, SVG, ICO
+ Text: TXT, LOG, JSON, XML, YAML, YML, CSV, MD, INI, CFG, CONF, SH, BAT, PY, JS, TS, TSX, JSX, HTML, CSS, TOML
+ Video: MP4, WebM, OGG
+ Audio: MP3, WAV, OGG, FLAC, AAC, WebM