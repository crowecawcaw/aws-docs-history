# Available Ready2Run workflows in HealthOmics

The following table lists the Ready2Run workflows that are available in HealthOmics.

You can log in to the [HealthOmics
console](https://console.aws.amazon.com/omics/home#/ready2run "https://console.aws.amazon.com/omics/home#/ready2run") to view detailed information about these workflows, including input parameters and workflow
diagrams. For pricing information about Ready2Run workflows, see [HealthOmics Pricing](https://aws.amazon.com/healthomics/pricing/ "https://aws.amazon.com/healthomics/pricing/").

###### Note

Each Ready2Run workflow has a maximum input file size. These maximum file sizes aren't adjustable.

| Workflow name                                                | Publisher           | Subscription required? | Maximum input file size (GiB) | Estimated run time (HH:MM) |
| ------------------------------------------------------------ | ------------------- | ---------------------- | ----------------------------- | -------------------------- |
| AlphaFold for 601-1200 residues                              | Google DeepMind     | No                     | 1                             | 11:15                      |
| AlphaFold for up to 600 residues                             | Google DeepMind     | No                     | 1                             | 7:30                       |
| Bases2Fastq for 2x150                                        | Element Biosciences | No                     | 1000                          | 1:45                       |
| Bases2Fastq for 2x300                                        | Element Biosciences | No                     | 1000                          | 1:30                       |
| Bases2Fastq for 2x75                                         | Element Biosciences | No                     | 500                           | 0:45                       |
| ESMFold for up to 800 residues                               | Meta Research       | No                     | 1                             | 0:15                       |
| GATK-BP fq2bam                                               | Broad Institute     | No                     | 64                            | 10:10                      |
| GATK-BP Germline bam2vcf for 30x genome                      | Broad Institute     | No                     | 39                            | 2:45                       |
| GATK-BP Germline fq2vcf for 30x genome                       | Broad Institute     | No                     | 64                            | 12:30                      |
| GATK-BP Somatic WES bam2vcf                                  | Broad Institute     | No                     | 86                            | 1:30                       |
| NVIDIA Parabricks BAM2FQ2BAM WGS for up to 30X               | NVIDIA Corporation  | No                     | 80                            | 1:39                       |
| NVIDIA Parabricks BAM2FQ2BAM WGS for up to 50X               | NVIDIA Corporation  | No                     | 120                           | 2:45                       |
| NVIDIA Parabricks BAM2FQ2BAM WGS for up to 5X                | NVIDIA Corporation  | No                     | 20                            | 0:18                       |
| NVIDIA Parabricks FQ2BAM WGS for up to 30X                   | NVIDIA Corporation  | No                     | 71                            | 1:00                       |
| NVIDIA Parabricks FQ2BAM WGS for up to 50X                   | NVIDIA Corporation  | No                     | 137                           | 1:45                       |
| NVIDIA Parabricks FQ2BAM WGS for up to 5X                    | NVIDIA Corporation  | No                     | 13                            | 0:15                       |
| NVIDIA Parabricks Germline DeepVariant WGS for up to 30X     | NVIDIA Corporation  | No                     | 71                            | 2:00                       |
| NVIDIA Parabricks Germline DeepVariant WGS for up to 50X     | NVIDIA Corporation  | No                     | 137                           | 3:30                       |
| NVIDIA Parabricks Germline DeepVariant WGS for up to 5X      | NVIDIA Corporation  | No                     | 12                            | 0:30                       |
| NVIDIA Parabricks Germline HaplotypeCaller WGS for up to 30X | NVIDIA Corporation  | No                     | 71                            | 1:15                       |
| NVIDIA Parabricks Germline HaplotypeCaller WGS for up to 50X | NVIDIA Corporation  | No                     | 137                           | 2:00                       |
| NVIDIA Parabricks Germline HaplotypeCaller WGS for up to 5X  | NVIDIA Corporation  | No                     | 13                            | 0:15                       |
| NVIDIA Parabricks Somatic Mutect2 WGS for up to 50X          | NVIDIA Corporation  | No                     | 196                           | 0:45                       |
| scRNAseq with KallistoBUStools                               | NF-Core             | No                     | 119                           | 1:30                       |
| scRNAseq with Salmon Alevin-fry                              | NF-Core             | No                     | 119                           | 2:30                       |
| scRNAseq with STARsolo                                       | NF-Core             | No                     | 119                           | 2:30                       |
| Sentieon Germline BAM WES for up to 300x                     | Sentieon, Inc.      | Yes                    | 9                             | 1:00                       |
| Sentieon Germline BAM WGS for up to 32x                      | Sentieon, Inc.      | Yes                    | 18                            | 1:30                       |
| Sentieon Germline FASTQ WES for up to 100x                   | Sentieon, Inc.      | Yes                    | 5                             | 0:45                       |
| Sentieon Germline FASTQ WES for up to 300x                   | Sentieon, Inc.      | Yes                    | 26                            | 2:00                       |
| Sentieon Germline FASTQ WGS for up to 32x                    | Sentieon, Inc.      | Yes                    | 51                            | 3:30                       |
| Sentieon LongRead for ONT                                    | Sentieon, Inc.      | Yes                    | 25                            | 1:30                       |
| Sentieon LongRead for PacBio HiFi                            | Sentieon, Inc.      | Yes                    | 58                            | 4:00                       |
| Sentieon Somatic WES                                         | Sentieon, Inc.      | Yes                    | 50                            | 2:30                       |
| Sentieon Somatic WGS                                         | Sentieon, Inc.      | Yes                    | 113                           | 4:30                       |
| Ultima Genomics DeepVariant for up to 40x                    | Ultima Genomics     | No                     | 91                            | 1:55                       |

When you use a Ready2Run workflow, your workflow is preconfigured and can't be edited. In contrast to private
workflows, Ready2Run workflows don't support the following:

- Increasing the maximum input file size
- Changing the compute resources or run storage
- Changing the workflow definition or containers
- Adding runs to a run group
- Sharing the workflow
  If the publisher has shared the Ready2Run workflow on GitHub, you can make your own private workflow based on
  the Ready2Run workflow. The following table provides links to GitHub workflows for each publisher.

| Publisher                      | Workflows on GitHub                                                                                                                                                                                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Google DeepMind, Meta Research | [Protein folding workflows](https://github.com/aws-samples/amazon-omics-tutorials/tree/main/example-workflows/protein-folding/workflows "https://github.com/aws-samples/amazon-omics-tutorials/tree/main/example-workflows/protein-folding/workflows") |
| Element Biosciences            | For information, contact Element Biosciences                                                                                                                                                                                                           |
| Broad Institute                | [GATK workflows](https://github.com/aws-samples/amazon-omics-tutorials/tree/main/example-workflows/gatk-best-practices/workflows "https://github.com/aws-samples/amazon-omics-tutorials/tree/main/example-workflows/gatk-best-practices/workflows")    |
| NVIDIA Corporation             | [Parabricks workflows](https://github.com/clara-parabricks-workflows/parabricks-omics-private-workflows "https://github.com/clara-parabricks-workflows/parabricks-omics-private-workflows")                                                            |
| nf-core                        | [NF-Core workflows](https://github.com/aws-samples/amazon-omics-tutorials/tree/main/example-workflows/nf-core/workflows/scrnaseq "https://github.com/aws-samples/amazon-omics-tutorials/tree/main/example-workflows/nf-core/workflows/scrnaseq")       |
| Sentieon                       | [Sentieon workflows](https://github.com/Sentieon/sentieon-amazon-omics "https://github.com/Sentieon/sentieon-amazon-omics")                                                                                                                            |
| Ultima Genomics                | [Ultima Genomics workflows](https://github.com/Ultimagen/healthomics-workflows "https://github.com/Ultimagen/healthomics-workflows")                                                                                                                   |
