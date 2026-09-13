

# Knowledge
<a name="knowledge-desktop"></a>

The Knowledge tab in Customize is where you give Amazon Quick access to files on your computer and control how Quick indexes them. For each folder, choose whether Quick uploads its files for full-content search, extracts information from them into your knowledge graph, both, or neither. Adding a folder grants access only; indexing stays off until you turn it on.

## Indexing options
<a name="knowledge-indexing-options"></a>

Open a folder's details pane and choose **Settings** to find these options under Indexing.


| Option | Description | 
| --- | --- | 
| Allow full file context for enhanced searching | Uploads and indexes this folder's files so Quick can search across their full content, including in scheduled and background work. When this option is on, it shows estimated monthly usage as a percentage of the monthly indexing budget. | 
| Always remember file information | Uploads this folder's files and extracts people, projects, and dates from them into your knowledge graph. When this option is on, it shows estimated monthly usage as a percentage of the monthly budget available for extraction. | 
| Agent access | Lets Quick read files from this folder. A folder in your list always has agent access, so turning this off removes the folder. Quick asks you to confirm first. | 

## Details
<a name="knowledge-details"></a>

The Details tab reports Files, Size, and Entities extracted. Entities extracted shows a dash until you turn on Always remember file information. Choose **Files** to jump to the advanced settings. Choose **Sync** at the top of the pane to pick up changes immediately.

## Advanced settings
<a name="knowledge-advanced"></a>

Choose **Advanced** on the Settings tab to reach the per-folder indexing controls. Scan interval (every 30 minutes) and Max file size are read-only; files larger than the maximum are skipped. You can set Max file age to index only files modified within a window, restrict File extensions, add Exclude patterns as glob patterns that Quick never indexes, and give knowledge graph extraction instructions to guide entity extraction. Rescan folder picks up changes incrementally. Rebuild index rebuilds from scratch and shows a cost estimate first.

## Search indexing limits
<a name="knowledge-limits"></a>

Global search-indexing limits apply across all indexed folders. Indexing stops automatically when free disk space falls below 8.0 GiB. You set a storage limit for the knowledge database, a maximum file size for indexing (larger files are skipped but remain available through direct search), and a maximum folder size for indexing.

## Folder access permissions
<a name="knowledge-permissions"></a>

To set what Quick can do with a folder, choose **Manage permissions** and set an access level: Full Access (read and write), Read Only, or Ask Each Time. You can adjust individual read and write operations independently.