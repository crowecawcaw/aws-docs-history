

# Knowledge
<a name="knowledge-desktop"></a>

The **Knowledge** tab in **Customize** is where you give AWS Quick access to files on your computer and control how Quick indexes them. For each folder, choose whether Quick uploads its files for full-content search, extracts information from them into your knowledge graph, both, or neither. When you add a folder, Quick can read its files on your computer, but it doesn't upload them until you turn on indexing.

## Indexing options
<a name="knowledge-indexing-options"></a>

Choose a folder to open its details pane, and then choose the **Settings** tab. Each folder has the following options.


| Option | Description | 
| --- | --- | 
| Agent access | Lets Quick read files from this folder. Turning this off removes the folder from your list, and Quick asks you to confirm first. | 
| Allow full file context for enhanced searching | Uploads the folder's files to the cloud and stores them in a space, so you can search them from the web and mobile, not only from this computer. If you turn this option off, the space isn't deleted. | 
| Index and extract into knowledge graph | Uploads the folder's files to the cloud, indexes them, and extracts information from them into your knowledge graph. Extraction counts toward your monthly usage entitlement. | 

If your administrator turns off an option, it shows **Turned off by your administrator**.

## Details
<a name="knowledge-details"></a>

The **Details** tab shows the folder's status, path, number of files, the space that stores its files, storage used, entities extracted, last sync, and indexing status. Entities extracted shows a dash until you turn on **Index and extract into knowledge graph**. To pick up changes right away, choose **Sync now**.

## Advanced settings
<a name="knowledge-advanced"></a>

On the **Settings** tab, choose **Advanced** to see more controls for the folder:
+ **Scan interval**: how often Quick scans the folder for new or changed files. This is set to every 30 minutes, and you can't change it.
+ **Max file size**: Quick skips files larger than this size. This limit applies to every folder, and you can't change it.
+ **Max file age**: index only files modified within a time window: **Last 7 days**, **Last 30 days**, **Last 90 days**, **Last year**, or **No limit**.
+ **File extensions**: index only files with these extensions. When the list is empty, Quick indexes all supported extensions.
+ **Exclude patterns**: glob patterns, such as `node_modules` or `*.tmp`, for files that Quick never indexes.
+ **KG extraction instructions**: custom instructions for knowledge graph extraction, such as which entity types to focus on.
+ **Rescan folder**: picks up new, changed, or deleted files now. Either **Allow full file context for enhanced searching** or **Index and extract into knowledge graph** must be on.
+ **Rebuild index**: extracts everything again from scratch. This requires **Index and extract into knowledge graph** to be on, and large folders might need budget approval.

If your administrator turns off knowledge graph extraction, you can't edit the extraction instructions or rebuild the index.

## Knowledge graph extraction limit
<a name="knowledge-limits"></a>

To control how much of your monthly usage goes to knowledge graph extraction, choose **Settings** next to **Add folder**. Set **Pause knowledge graph extraction** to a percentage of your total monthly entitlement, or set it to **Off**. When usage reaches that percentage, Quick pauses extraction, and the new limit applies right away. If your plan has no total monthly entitlement limit, extraction doesn't pause, and the dialog says so.

## Folder access permissions
<a name="knowledge-permissions"></a>

Quick uses operating system sandboxing to control file access. It can reach only the folders that you grant, and you can revoke access at any time by turning off **Agent access** for a folder. Each folder also has its own options for search and knowledge graph extraction, as described in [Indexing options](#knowledge-indexing-options).

Quick can also reach the system temporary folders, whatever your folder permissions are. On Windows, these are `C:\TEMP`, `C:\TMP`, `\TEMP`, and `\TMP`. On macOS, these are `/tmp`, `/var/tmp`, and `/usr/tmp`.