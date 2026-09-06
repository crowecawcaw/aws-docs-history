

# Customizing synchronization for S3 Files
<a name="s3-files-synchronization-customizing"></a>

S3 Files lets you control how data flows between your file system and linked S3 bucket through a synchronization configuration. The default settings balance latency and cost for most workloads, but you can tune them to match your access patterns. Importing more data up front reduces read latency at the cost of higher storage and write charges. Importing less data keeps storage costs low but means more reads are served from S3 with higher latency. Each configuration has two components: import data rules, which control what data is copied onto the file system and when, and expiration data rules, which control how long unused data stays on the file system. You can update these rules using the AWS Management Console or the PutSynchronizationConfiguration API.

## Import data rules
<a name="s3-files-sync-import-rules"></a>

Import data rules control how data is copied from your bucket to the file system. You can have a maximum of 10 import data rules per file system. Each import data rule has the following parameters:

**prefix** – The S3 prefix that the rule applies to. Specify an empty string ("") for the entire bucket (file system scope) or a specific prefix (for example, "data/ml/") within the file system. The prefix must end with a forward slash (/), unless specifying the entire bucket with "". You must include exactly one import rule for the root directory. Default: "" (entire bucket or file system scope).

**trigger** – When to import data: ON\_DIRECTORY\_FIRST\_ACCESS or ON\_FILE\_ACCESS. Default: ON\_DIRECTORY\_FIRST\_ACCESS.
+ **ON\_DIRECTORY\_FIRST\_ACCESS** – File data is imported when you first access a directory. For example, when you first access a directory by listing its contents or opening a file within it, data is imported for all immediate children files in that directory smaller than the sizeLessThan threshold. This option is useful for workloads that require low latency when first accessing files.
+ **ON\_FILE\_ACCESS** – File data is imported only when a file is read for the first time. This option minimizes the data imported at the cost of higher latency on first read.

**sizeLessThan** – Maximum file size (in bytes) to automatically import. While S3 Files imports metadata for all files, it only imports data for files smaller than this threshold. Minimum: 0 bytes (no data imported, metadata will still be imported). Maximum: 52,673,613,135,872 bytes (48 TiB). Default: 131,072 bytes (128 KiB).

### Prefix matching behavior
<a name="s3-files-sync-prefix-matching"></a>

When multiple import data rules match a file, S3 Files applies the rule with the most specific prefix. For example, assume you have three rules:
+ Rule 1: prefix = "" (entire bucket), sizeLessThan = 64 KiB, trigger = ON\_FILE\_ACCESS
+ Rule 2: prefix = "hot/", sizeLessThan = 1 MiB, trigger = ON\_DIRECTORY\_FIRST\_ACCESS
+ Rule 3: prefix = "hot/largeData/", sizeLessThan = 256 KiB, trigger = ON\_DIRECTORY\_FIRST\_ACCESS

For a file at hot/largeData/data.txt, S3 Files applies Rule 3. For a file at hot/data.txt, S3 Files applies Rule 2. For a file at cold/data.txt, S3 Files applies Rule 1 because there is no specific rule for the cold/ prefix.

## Expiration data rules
<a name="s3-files-sync-expiration-rules"></a>

Expiration data rules control when unused data is removed from the file system to optimize storage costs. S3 Files removes data after it has not been read for a specified duration and its changes have already been synchronized to the S3 bucket. Whenever a file is read, its expiration timer resets, extending the time that data remains in the file system. You can specify the following parameter in expiration data rules:

**daysAfterLastAccess** – Number of days after last read when data is removed from the file system. Minimum: 1 day. Maximum: 365 days. Default: 30 days.

If you have long-running workloads that frequently access the same data, consider longer expiration periods (30–90 days). For temporary data, consider shorter periods (1–7 days).

## Example configurations
<a name="s3-files-sync-example-configs"></a>

**General purpose file share (default configuration)** – A team of developers and data scientists mounts an S3 file system to share code, configuration files, and small datasets. Most files are under 128 KiB and are read repeatedly throughout the day. The default configuration works well for this workload: ON\_DIRECTORY\_FIRST\_ACCESS imports metadata and small file data when any file in a directory is first accessed, which works well when files in the same directory are likely to be accessed together, such as source files in a project or configuration files in a deployment. Subsequent access by any user is fast. When a user opens a large file such as a log archive, S3 Files automatically streams it directly from S3 for high throughput. The 30-day expiration window keeps actively used files on the file system without manual cleanup.

**ML training with repeated reads** – A training job reads thousands of small files (<10 MiB) repeatedly across multiple epochs. To minimize latency, set a high sizeLessThan threshold (for example, 10 MiB) with ON\_DIRECTORY\_FIRST\_ACCESS so that file data is preloaded when the training script first lists each directory. Set a short expiration (for example, 3 days) so that data is removed from the file system promptly after the training job completes.

**Agentic workloads with broad file discovery** – An AI agent explores a large repository of documents, code, or knowledge base files to answer queries, reading many small files once as it searches for relevant context. Set sizeLessThan to 0 so that no data is imported onto the file system. The agent can browse the full directory tree at low latency to discover files, while each file read is served directly from S3. This keeps costs low for workloads that touch many files unpredictably but rarely revisit the same file, and scales naturally as you add more agents reading in parallel.

**Hot and cold prefixes** – A file system contains both frequently accessed configuration files under `config/` and infrequently accessed archive data under `archive/`. Create two import rules: one for `config/` with a high sizeLessThan and ON\_DIRECTORY\_FIRST\_ACCESS, and one for `archive/` with sizeLessThan set to 0 and ON\_FILE\_ACCESS. This keeps configuration files on the file system for fast access while avoiding storage costs for archive data that is rarely read.