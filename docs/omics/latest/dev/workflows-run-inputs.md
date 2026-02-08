# HealthOmics run inputs

If the workflow definition specifies input files for the workflow or workflow tasks, HealthOmics stages the files to a
scratch volume that's dedicated to the workflow run. These input files are read-only, which prevents tasks from
modifying potential inputs to other tasks in the workflow. For directory imports, the directories are also
read-only.

Many genomics applications assume that index files are co-located with the sequence files (such as a companion
`bai` file for a `bam` file). To include index files, specify them as task inputs in the
workflow definition.

###### Topics

- [Managing run parameters size](#run-input-file-options "#run-input-file-options")
- [Amazon S3 input parameter formats](#s3-run-input-formats "#s3-run-input-formats")
- [Amazon S3 input archive states](#s3-run-input-archive "#s3-run-input-archive")

## Managing run parameters size

When you start a run, you specify run inputs in the run parameters JSON object or file. You can specify up to 50 KB of run parameters for the workflow. You can use the following techniques to
remain within this size constraint:

- **Use directory imports**

To specify a large number of input files, specify one parameter as the Amazon S3 location that contains all the
files, rather than specifying a parameter for each file location. For more information, see the next topic
(Amazon S3 input parameter formats).

- **Use a sample sheet**

A sample sheet is a CSV or TSV file with one column for the fastq.gz address (or two for paired read) and
additional columns for metadata such as sample names. You specify the sample sheet as a run input parameter
instead of a parameter for each input file.

Your workflow defines how your sample sheet maps to data structures in the workflow. While you could write
code for sample sheets in WDL and CWL, they're more common in NextFlow. For an example, see [sample sheet](https://github.com/nf-core/scrnaseq/blob/master/assets/samplesheet.csv "https://github.com/nf-core/scrnaseq/blob/master/assets/samplesheet.csv") on the
**nf-core** GitHub site.

## Amazon S3 input parameter formats

For an input parameter that accepts an Amazon S3 location, the parameter can specify the location of one file or a
whole directory of files. Using a directory has the following advantages:

- Convenience – You specify the directory name as the parameter. You don't list each file name.
- Compactness – The input parameter maximum file size is 50 KB. If you provide a long list of input
  file names, you can exceed this maximum.

Amazon S3 is a flat object-storage system, so it doesn't support directories. You group files into a "directory" by
giving each file the same object key prefix. For more information about Amazon S3 object key prefixes, see [Organizing objects using
prefixes](../../../AmazonS3/latest/userguide/using-prefixes.md "../../../AmazonS3/latest/userguide/using-prefixes.md").

HealthOmics interprets the input parameter value as follows:

- If the Amazon S3 location doesn't end with a forward slash or use the glob pattern, HealthOmics expects the parameter
  value to be the key for one Amazon S3 object.

For example, you specify `s3://myfiles/runs/inputs/a/file1.fastq` to input file1.fastq

- If the Amazon S3 location ends with a forward slash, HealthOmics interprets the parameter value as an Amazon S3 prefix. It
  loads all the Amazon S3 objects with that prefix.

For example, you can specify `s3://myfiles/runs/inputs/a/` to load all objects whose keys start
with this prefix.

- For Nextflow, HealthOmics paritally supports the glob pattern for Amazon S3 URIs in input parameters.

For example, you can specify `“s3://myfiles/runs/inputs/a/*.gz”` to input all .gz files whose
keys start with this prefix.

### Nextflow Handling of Glob pattern in Amazon S3 inputs

| Glob Pattern                      | HealthOmics Match Behavior                                                                                                                                                                                                                | Notes                             |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| s3://bucket/directory/\*.txt      | Matches all `.txt` objects at any depth under the prefix s3://bucket/directory/. For example, matches s3://bucket/directory/abc.txt or s3://bucket/directory/subDir/123.txt etc.                                                          |                                   |
| s3://bucket/directory/\*\*/\*.txt | Matches all `.txt` objects at any depth under the prefix s3://bucket/directory/. For example, matches s3://bucket/directory/abc.txt or s3://bucket/directory/subDir/123.txt etc.                                                          | In S3, `**` is equivalent to `*`. |
| s3://bucket/directory/{a,b}.txt   | s3://bucket/directory/a.txt, s3://bucket/directory/b.txt                                                                                                                                                                                  |                                   |
| s3://bucket/directory/?.txt       | Matches objects at the prefix root whose filename is a single character followed by `.txt`. For example, it matches s3://bucket/directory/a.txt but not s3://bucket/directory/someDir/a.txt or s3://bucket/directory/someDir/subDir/a.txt |                                   |
| s3://bucket/directory/[0-9].txt   | s3://bucket/directory/0.txt, s3://bucket/directory/1.txt, ... ,s3://bucket/directory/9.txt                                                                                                                                                |                                   |
| s3://bucket/directory/[0-9].txt   | s3://bucket/directory/1.txt, s3://bucket/directory/2.txt, s3://bucket/directory/3.txt                                                                                                                                                     |                                   |
| s3://bucket/directory/[0-9].txt   | s3://bucket/directory/b.txt, s3://bucket/directory/c.txt, ... ,s3://bucket/directory/Y.txt                                                                                                                                                |                                   |

### Language-specific handling of double-slash in Amazon S3 inputs

HealthOmics retains the native engine behavior for each workflow engine when handling double-slashes in Amazon S3 URIs,
so that you don't need to make any changes to your workflows when you migrate them to HealthOmics. The following
sections describe how each engine handles various scenarios.

#### WDL

If the input parameter includes a double-slash in the middle or at the end of the URI, the WDL engine
retains the double-slash.

| Input parameter                       | Expected location                     |
| ------------------------------------- | ------------------------------------- |
| s3://myfiles/runs/inputs//file1.fastq | s3://myfiles/runs/inputs//file1.fastq |
| s3://myfiles/runs/inputs//            | s3://myfiles/runs/inputs//            |

#### Nextflow

If the input parameter includes a double-slash in the middle of the URI, the Nextflow engine retains
double-slash. For a double-slash at the end of the URI, the Nextflow engine resolves it to a single
slash.

| Input parameter                       | Expected location                     |
| ------------------------------------- | ------------------------------------- |
| s3://myfiles/runs/inputs//file1.fastq | s3://myfiles/runs/inputs//file1.fastq |
| s3://myfiles//runs/inputs//\*.gz      | s3://myfiles//runs/inputs//\*.gz      |
| s3://myfiles//runs/inputs//           | s3://myfiles//runs/inputs/            |

#### CWL

If the input parameter includes a double-slash in the middle or at the end of the URI, the CWL engine
retains the double-slash.

| Input parameter                        | Expected location                      |
| -------------------------------------- | -------------------------------------- |
| s3://myfiles//runs/inputs//file1.fastq | s3://myfiles//runs/inputs//file1.fastq |
| s3://myfiles//runs/inputs//            | s3://myfiles//runs/inputs//            |

## Amazon S3 input archive states

HealthOmics can retrieve Amazon S3 objects that S3 delivers in real time. For objects that are in the following archived
storage states, **restore** the objects to make them available to HealthOmics:

- Flexible Retrieval or Deep Archive storage classes in Amazon S3 Glacier.
- Archived Access or Deep Archive Access tiers in Intelligent tiering.

For information about restoring objects, see [Restoring an archived object](../../../AmazonS3/latest/userguide/restoring-objects.md "../../../AmazonS3/latest/userguide/restoring-objects.md") in the _Amazon S3 User Guide_.
