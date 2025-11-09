# HealthOmics fixed size quotas

In addition to the [HealthOmics service quotas](service-quotas.md "service-quotas.md"), HealthOmics includes quotas
that have fixed sizes. You cannot request an increase for these values.

Unless otherwise noted, each quota lists the maximum value per-Region.

###### Topics

- [HealthOmics analytics fixed size quotas](#fixed-quotas-analytics "#fixed-quotas-analytics")
- [HealthOmics storage fixed size quotas](#fixed-quotas-storage "#fixed-quotas-storage")
- [HealthOmics workflow fixed size quotas](#fixed-quotas-workflows "#fixed-quotas-workflows")
- [HealthOmics Ready2Run workflow fixed size quotas](#fixed-quotas-r2r-workflows "#fixed-quotas-r2r-workflows")

## HealthOmics analytics fixed size quotas

The following table shows the maximum supported values for analytics quotas. These values aren't
adjustable.

| Name                                                         | Description                                            | Maximum | Adjustable Yes/No |
| ------------------------------------------------------------ | ------------------------------------------------------ | ------- | ----------------- |
| Analytics<br>• Maximum files per annotation store import job | The maximum number of files per annotation import job. | 1       | No                |

## HealthOmics storage fixed size quotas

The following table shows the maximum supported values for storage files. These values aren't
adjustable.

| Name                                                 | Description                                                                                      | Maximum | Adjustable Yes/No |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------- | ----------------- |
| Storage<br>• Maximum S3 access resource policy size  | The maximum size of the S3 access resource policy                                                | 15 KB   | No                |
| Storage<br>• Maximum propagated set level tags       | The maximum number of set level tag keys, per store, that propogate to the S3 object             | 5       | No                |
| Storage<br>• Maximum read sets per activation job    | The maximum number of read sets per activation job.                                              | 20      | No                |
| Storage<br>• Maximum read sets per export job        | The maximum number of read sets per export job.                                                  | 100     | No                |
| Storage<br>• Maximum read sets per import job        | The maximum number of read sets per import job.                                                  | 100     | No                |
| Storage<br>• Maximum reference stores                | The maximum number of reference stores.                                                          | 1       | No                |
| Storage<br>• Maximum part size for a direct upload   | The maximum part size for direct upload to a sequence store.                                     | 100 MB  | No                |
| Storage<br>• Maximum parts in file for direct upload | The maximum number of parts in a file for direct upload to a sequence store.                     | 10,000  | No                |
| Storage<br>• Maximum reference size                  | The maximum size of a reference file that can be imported to a reference store.                  | 15 GB   | No                |
| Storage<br>• Maximum read set source size            | The maximum size of a single source file in a read set that can be imported to a sequence store. | 976 GB  | No                |

## HealthOmics workflow fixed size quotas

The following table shows the maximum supported values for workflow quotas.
These values aren't adjustable.

| Name                                                                              | Description                                                                                                                                                                                                 | Maximum size          | Adjustable Yes/No |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ----------------- |
| Workflows<br>• Maximum run groups                                                 | The maximum number of run groups.                                                                                                                                                                           | 1000                  | No                |
| Workflows<br>• Maximum run caches                                                 | The maximum number of run caches that you can create for one account. One or more runs can<br>share the same run cache. There is no quota for the number of runs that HealthOmics can cache per<br>account. | 1000                  | No                |
| Workflows<br>• Maximum workflow versions                                          | The maximum number of workflow versions per workflow.                                                                                                                                                       | 1000                  | No                |
| Workflows<br>• CPU instance container size                                        | The maximum container image size for a CPU instance.                                                                                                                                                        | 45 GiB                | No                |
| Workflows<br>• GPU instance container size                                        | The maximum container image size for a GPU instance.                                                                                                                                                        | 95 GiB                | No                |
| GPU instance /dev/shm shared memory                                               | The maximum amount of shared memory per GPU instance.                                                                                                                                                       | 8 GB per GPU          | No                |
| Workflows<br>• Run parameter file                                                 | The maximum size of a run parameter file.                                                                                                                                                                   | 50,000 bytes          | No                |
| Workflows<br>• Workflow parameters template file                                  | The maximum number of entries and maximum file size for a workflow parameters template file. This<br>quota applies to workflows that you create using the console or API.                                   | 1,000 entries, 400 KB | No                |
| Workflows<br>• Workflow definition file size<br>• API                             | The maximum size of the workflow definition file when you create the workflow using the API<br>operation or an AWS SDK.                                                                                     | 100 MB                | No                |
| Workflows<br>• Workflow definition file size<br>• Console (direct upload)         | The maximum size of the workflow definition file that you can provide as a direct upload,<br>when you create the workflow using the console.                                                                | 4.4 MB                | No                |
| Workflows<br>• Workflow definition file size<br>• Console (upload from Amazon S3) | The maximum size of the workflow definition file that you can provide as an upload from Amazon S3,<br>when you create the workflow using the console.                                                       | 100 MB                | No                |
| Workflows<br>• Repository size                                                    | The maximum size of an external code repository.                                                                                                                                                            | 1 GiB                 | No                |
| Workflows<br>• Repository individual file size                                    | The maximum size of an individual file from an external code repository.                                                                                                                                    | 100 MiB               | No                |
| Workflows<br>• README file size                                                   | The maximum size of a README file.                                                                                                                                                                          | 500 KiB               | No                |

For suggestions on how to reduce the size of your run parameter file, see
[Managing run parameters size](workflows-run-inputs.md#run-input-file-options "workflows-run-inputs.md#run-input-file-options").

## HealthOmics Ready2Run workflow fixed size quotas

Each Ready2Run workflow has a maximum input file size. In the following table, the file size units are
listed in Gibibytes (GiB). These maximum file sizes aren't adjustable.

| Ready2Run workflow name                                      | Maximum input file size (GiB) | Adjustable (Yes/No) |
| ------------------------------------------------------------ | ----------------------------- | ------------------- |
| AlphaFold for 601-1200 residues                              | 1                             | No                  |
| AlphaFold for up to 600 residues                             | 1                             | No                  |
| Bases2Fastq for 2x150                                        | 1000                          | No                  |
| Bases2Fastq for 2x300                                        | 1000                          | No                  |
| Bases2Fastq for 2x75                                         | 500                           | No                  |
| ESMFold for up to 800 residues                               | 1                             | No                  |
| GATK-BP fq2bam                                               | 64                            | No                  |
| GATK-BP Germline bam2vcf for 30x genome                      | 39                            | No                  |
| GATK-BP Germline fq2vcf for 30x genome                       | 64                            | No                  |
| GATK-BP Somatic WES bam2vcf                                  | 86                            | No                  |
| NVIDIA Parabricks BAM2FQ2BAM WGS for up to 30X               | 80                            | No                  |
| NVIDIA Parabricks BAM2FQ2BAM WGS for up to 50X               | 120                           | No                  |
| NVIDIA Parabricks BAM2FQ2BAM WGS for up to 5X                | 20                            | No                  |
| NVIDIA Parabricks FQ2BAM WGS for up to 30X                   | 71                            | No                  |
| NVIDIA Parabricks FQ2BAM WGS for up to 50X                   | 137                           | No                  |
| NVIDIA Parabricks FQ2BAM WGS for up to 5X                    | 13                            | No                  |
| NVIDIA Parabricks Germline DeepVariant WGS for up to 30X     | 71                            | No                  |
| NVIDIA Parabricks Germline DeepVariant WGS for up to 50X     | 137                           | No                  |
| NVIDIA Parabricks Germline DeepVariant WGS for up to 5X      | 12                            | No                  |
| NVIDIA Parabricks Germline HaplotypeCaller WGS for up to 30X | 71                            | No                  |
| NVIDIA Parabricks Germline HaplotypeCaller WGS for up to 50X | 137                           | No                  |
| NVIDIA Parabricks Germline HaplotypeCaller WGS for up to 5X  | 13                            | No                  |
| NVIDIA Parabricks Somatic Mutect2 WGS for up to 50X          | 196                           | No                  |
| scRNAseq with KallistoBUStools                               | 119                           | No                  |
| scRNAseq with Salmon Alevin-fry                              | 119                           | No                  |
| scRNAseq with STARsolo                                       | 119                           | No                  |
| Sentieon Germline BAM WES for up to 300x                     | 9                             | No                  |
| Sentieon Germline BAM WGS for up to 32x                      | 18                            | No                  |
| Sentieon Germline FASTQ WES for up to 100x                   | 5                             | No                  |
| Sentieon Germline FASTQ WES for up to 300x                   | 26                            | No                  |
| Sentieon Germline FASTQ WGS for up to 32x                    | 51                            | No                  |
| Sentieon LongRead for ONT                                    | 25                            | No                  |
| Sentieon LongRead for PacBio HiFi                            | 58                            | No                  |
| Sentieon Somatic WES                                         | 50                            | No                  |
| Sentieon Somatic WGS                                         | 113                           | No                  |
| Ultima Genomics DeepVariant for up to 40x                    | 91                            | No                  |
