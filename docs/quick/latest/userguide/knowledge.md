

# Knowledge

Knowledge in AWS Quick is how you give your agents and chat access to your content so they can find, cite, and reason over it. On the web, you provide knowledge through knowledge bases in the cloud. A knowledge base connects to a data source, indexes its content, and makes that content searchable for AI analysis.

## Cloud knowledge with knowledge bases
<a name="knowledge-web-knowledge-bases"></a>

On the web, you provide knowledge to Quick through knowledge bases in the cloud. You create a knowledge base by connecting to a data source, such as a supported application or a web crawler, and Quick indexes its content so your agents and chat can search and cite it. For more information about how knowledge bases work, see [How knowledge bases work](knowledge-base-integrations.md#how-knowledge-bases-work).

For more information about creating knowledge bases, see [Creating knowledge bases in AWS Quick](creating-knowledge-bases-creating-knowledge-bases.md). For more information about managing existing knowledge bases, see [Managing knowledge bases in Quick](managing-knowledge-bases-managing-knowledge-bases.md).

## Local folder access
<a name="knowledge-web-local-folders"></a>

Giving Quick access to folders on your computer is a capability of the AWS Quick desktop application. On the web, you work with cloud knowledge bases instead. When you grant folder access in the AWS Quick desktop application and turn on full-content indexing, those files are uploaded to a space, so you can search them from the web as well.

In the AWS Quick desktop application, you give Quick access to files on your computer and control how Quick indexes them. For each folder, you choose whether Quick uploads its files for full-content search, extracts information from them into your knowledge graph, both, or neither. When you add a folder, Quick can read its files on your computer, but it doesn't upload them until you turn on indexing.

### Indexing options
<a name="knowledge-local-indexing"></a>

Choose a folder to open its details pane, and then choose the **Settings** tab. Each folder has the following options.


| Option | Description | 
| --- | --- | 
| Agent access | Lets Quick read files from this folder. Turning this off removes the folder from your list, and Quick asks you to confirm first. | 
| Allow full file context for enhanced searching | Uploads the folder's files to the cloud and stores them in a space, so you can search them from the web and mobile, not only from this computer. If you turn this option off, the space isn't deleted. | 
| Index and extract into knowledge graph | Uploads the folder's files to the cloud, indexes them, and extracts information from them into your knowledge graph. Extraction counts toward your monthly usage entitlement. | 

If your administrator turns off an option, it shows **Turned off by your administrator**.

### Folder details
<a name="knowledge-local-details"></a>

The **Details** tab shows the folder's status, path, number of files, the space that stores its files, storage used, entities extracted, last sync, and indexing status. Entities extracted shows a dash until you turn on **Index and extract into knowledge graph**. To pick up changes right away, choose **Sync now**.

### Advanced settings
<a name="knowledge-local-advanced"></a>

On the **Settings** tab, choose **Advanced** to see more controls for the folder.
+ **Scan interval** sets how often Quick scans the folder for new or changed files. It is set to every 30 minutes, and you can't change it.
+ **Max file size** makes Quick skip files larger than this size. This limit applies to every folder, and you can't change it.
+ **Max file age** indexes only files modified within a time window: **Last 7 days**, **Last 30 days**, **Last 90 days**, **Last year**, or **No limit**.
+ **File extensions** indexes only files with these extensions. When the list is empty, Quick indexes all supported extensions.
+ **Exclude patterns** are glob patterns, such as `node_modules` or `*.tmp`, for files that Quick never indexes.
+ **KG extraction instructions** are custom instructions for knowledge graph extraction, such as which entity types to focus on.
+ **Rescan folder** picks up new, changed, or deleted files now. Either **Allow full file context for enhanced searching** or **Index and extract into knowledge graph** must be on.
+ **Rebuild index** extracts everything again from scratch. This requires **Index and extract into knowledge graph** to be on, and large folders might need budget approval.

If your administrator turns off knowledge graph extraction, you can't edit the extraction instructions or rebuild the index.

### Knowledge graph extraction limit
<a name="knowledge-local-limits"></a>

To control how much of your monthly usage goes to knowledge graph extraction, choose **Settings** next to **Add folder**. Set **Pause knowledge graph extraction** to a percentage of your total monthly entitlement, or set it to **Off**. When usage reaches that percentage, Quick pauses extraction, and the new limit applies right away. If your plan has no total monthly entitlement limit, extraction doesn't pause, and the dialog says so. For more information about your knowledge graph, see [Your knowledge graph and My context](knowledge-graph.md).

### Folder access permissions
<a name="knowledge-local-permissions"></a>

Quick uses operating system sandboxing to control file access. It can reach only the folders that you grant, and you can revoke access at any time by turning off **Agent access** for a folder. Each folder also has its own options for search and knowledge graph extraction, as described in [Indexing options](#knowledge-local-indexing).

Quick can also reach the system temporary folders, whatever your folder permissions are. On Windows, these are `C:\TEMP`, `C:\TMP`, `\TEMP`, and `\TMP`. On macOS, these are `/tmp`, `/var/tmp`, and `/usr/tmp`.