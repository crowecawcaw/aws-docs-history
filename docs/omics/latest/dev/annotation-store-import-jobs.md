AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Creating import jobs for HealthOmics annotation stores

###### Topics

- [Creating an annotation import job using the API](#create-annotation-import-api "#create-annotation-import-api")
- [Additional parameters for TSV and VCF formats](#annotation-import-tsv-vcf "#annotation-import-tsv-vcf")
- [Creating TSV formatted annotation
  stores](#annotation-import-tsv-vcftsv-annotation-store-examples-tsv "#annotation-import-tsv-vcftsv-annotation-store-examples-tsv")
- [Starting VCF formatted import jobs](#vcf-annotation-store-examples "#vcf-annotation-store-examples")

## Creating an annotation import job using the API

The following example shows how to use the AWS CLI to start an annotation import job.

```
aws omics start-annotation-import-job \
           --destination-name myannostore \
           --version-name myannostore \
           --role-arn arn:aws:iam::123456789012:role/roleName \
           --items source=s3://my-omics-bucket/sample.vcf.gz
           --annotation-fields '{"VEP": "CSQ"}'
```

Annotation stores created before May 15, 2023 return an error message if the
**annotation-fields** is included. They don't return output for any API
operations involved with annotation store import jobs.

You can then use the **get-annotation-import-job** API operation and the
`job ID` parameter to learn more details about the annotation import job.

```
aws omics get-annotation-import-job --job-id 9e4198fb-fa85-446c-9301-9b823a1a8ba8
```

You receive the following response, including the annotation fields.

```
{
          "creationTime": "2023-04-11T19:09:25.049767+00:00",
          "destinationName": "parsingannotationstore",
          "versionName": "parsingannotationstore",
          "id": "9e4198fb-fa85-446c-9301-9b823a1a8ba8",
          "items": [
              {
                  "jobStatus": "COMPLETED",
                  "source": "s3://my-omics-bucket/sample.vep.vcf"
              }
          ],
          "roleArn": "arn:aws:iam::55555555555:role/roleName",
          "runLeftNormalization": false,
          "status": "COMPLETED",
          "updateTime": "2023-04-11T19:13:09.110130+00:00",
          "annotationFields" : {"VEP": "CSQ"}
       }

```

To view all annotation store import jobs, use **list-annotation-import-jobs** .

```
aws omics list-annotation-import-jobs --ids 9e4198fb-fa85-446c-9301-9b823a1a8ba8
```

The response includes the details and statuses of your annotation store import
jobs.

```
{
          "annotationImportJobs": [
          {
              "creationTime": "2023-04-11T19:09:25.049767+00:00",
              "destinationName": "parsingannotationstore",
              "versionName": "parsingannotationstore",
              "id": "9e4198fb-fa85-446c-9301-9b823a1a8ba8",
              "roleArn": "arn:aws:iam::55555555555:role/roleName",
              "runLeftNormalization": false,
              "status": "COMPLETED",
              "updateTime": "2023-04-11T19:13:09.110130+00:00",
              "annotationFields" : {"VEP": "CSQ"}
          }
          ]
      }
```

## Additional parameters for TSV and VCF formats

For TSV and VCF formats, there are additional parameters that inform the API of how to
parse your input.

###### Important

CSV annotation data that's exported with query engines directly returns information
from the dataset import. If the imported data contains formulas or commands, the file might
be subject to CSV injection. Therefore, files exported with query engines can prompt
security warnings. To avoid malicious activity, turn off links and macros when reading
export files.

The TSV parser also performs basic bioinformatics operations, like left normalization and
standardization of genomics coordinates, that are listed in the following table.

| Format type                       | Description                                                                           |
| --------------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Generic                           | Generic text file. No genomic information.                                            |
| `CHR_POS`                         | Start position - 1, Add end position, which is the same as `POS`.                     |
| `CHR_POS_REF_ALT`                 | Contains contig, 1-base position, ref and alt allele information.                     |
| `CHR_START_END_REF_ALT_ONE_BASE`  | Contains contig, start, end, ref and alt allele information. Coordinates are 1-based. |
| `CHR_START_END_ZERO_BASE`         | Contains contig, start, and end positions. Coordinates are 0-based.                   |
| `CHR_START_END_ONE_BASE`          | Contains contig, start, and end positions. Coordinates are 1-based.                   |
| `CHR_START_END_REF_ALT_ZERO_BASE` | Contains contig, start, end, ref and alt allele information. Coordinates are 0-based. | A TSV import annotation store request looks like the following example. `aws omics start-annotation-import-job \ --destination-name tsv_anno_example \ --role-arn arn:aws:iam::555555555555:role/demoRole \ --items source=s3://demodata/genomic_data.bed.gz \ --format-options '{ "tsvOptions": { "readOptions": { "header": false, "sep": "\t" } } }'` ## Creating TSV formatted annotation stores The following example creates an annotation store using a tab limited file that contains a header, rows, and comments. The coordinates are `CHR_START_END_ONE_BASED`, and it contains the HG19 gene map from the [OMIM's Synopsis of the Human Gene Map](https://www.omim.org/downloads "https://www.omim.org/downloads"). `aws omics create-annotation-store --name mimgenemap \ --store-format TSV \ --reference=referenceArn=arn:aws:omics:us-west-2:555555555555:referenceStore/6505293348/reference/2310864158 \ --store-options=tsvStoreOptions='{ annotationType=CHR_START_END_ONE_BASE, formatToHeader={CHR=chromosome, START=genomic_position_start, END=genomic_position_end}, schema=[ {chromosome=STRING}, {genomic_position_start=LONG}, {genomic_position_end=LONG}, {cyto_location=STRING}, {computed_cyto_location=STRING}, {mim_number=STRING}, {gene_symbols=STRING}, {gene_name=STRING}, {approved_gene_name=STRING}, {entrez_gene_id=STRING}, {ensembl_gene_id=STRING}, {comments=STRING}, {phenotypes=STRING}, {mouse_gene_symbol=STRING}]}'` You can import files with or without a header. To indicate this in a CLI request, use `header=false`, as shown in the following import job example. `aws omics start-annotation-import-job \ --role-arn arn:aws:iam::555555555555:role/demoRole \ --items=source=s3://amzn-s3-demo-bucket/annotation-examples/hg38_genemap2.txt \ --destination-name output-bucket \ --format-options=tsvOptions='{readOptions={sep="\t",header=false,comment="#"}}'` The following example creates an annotation store for a bed file. A bed file is a simple tab delimited file. In this example, the columns are chromosome, start, end, and region name. The coordinates are zero-based, and the data does not have a header. `aws omics create-annotation-store \ --name cexbed --store-format TSV \ --reference=referenceArn=arn:aws:omics:us-west-2:555555555555:referenceStore/6505293348/reference/2310864158 \ --store-options=tsvStoreOptions='{ annotationType=CHR_START_END_ZERO_BASE, formatToHeader={CHR=chromosome, START=start, END=end}, schema=[{chromosome=STRING}, {start=LONG}, {end=LONG}, {name=STRING}]}'` You can then import the bed file into the annotation store by using the following the CLI command. `aws omics start-annotation-import-job \ --role-arn arn:aws:iam::555555555555:role/demoRole \ --items=source=s3://amzn-s3-demo-bucket/TruSeq_Exome_TargetedRegions_v1.2.bed \ --destination-name cexbed \ --format-options=tsvOptions='{readOptions={sep="\t",header=false,comment="#"}}'` The following example creates an annotation store for a tab delimited file that contains the first few columns of a VCF file, followed by columns with annotation information. It contains genome positions with information on the chromosome, start, reference and alternate alleles, and it contains a header. `aws omics create-annotation-store --name gnomadchrx --store-format TSV \ --reference=referenceArn=arn:aws:omics:us-west-2:555555555555:referenceStore/6505293348/reference/2310864158 \ --store-options=tsvStoreOptions='{ annotationType=CHR_POS_REF_ALT, formatToHeader={CHR=chromosome, POS=start, REF=ref, ALT=alt}, schema=[ {chromosome=STRING}, {start=LONG}, {ref=STRING}, {alt=STRING}, {filters=STRING}, {ac_hom=STRING}, {ac_het=STRING}, {af_hom=STRING}, {af_het=STRING}, {an=STRING}, {max_observed_heteroplasmy=STRING}]}'` You would then import the file into the annotation store using the following the CLI command. `aws omics start-annotation-import-job \ --role-arn arn:aws:iam::555555555555:role/demoRole \ --items=source=s3://amzn-s3-demo-bucket/gnomad.genomes.v3.1.sites.chrM.reduced_annotations.tsv \ --destination-name gnomadchrx \ --format-options=tsvOptions='{readOptions={sep="\t",header=true,comment="#"}}'` The following example shows how a customer can create an annotation store for a mim2gene file. A mim2gene file provides the links between the genes in OMIM and another gene identifier. It's tab delimited and contains comments. `aws omics create-annotation-store \ --name mim2gene \ --store-format TSV \ --reference=referenceArn=arn:aws:omics:us-west-2:555555555555:referenceStore/6505293348/reference/2310864158 \ --store-options=tsvStoreOptions=' {annotationType=GENERIC, formatToHeader={}, schema=[ {mim_gene_id=STRING}, {mim_type=STRING}, {entrez_id=STRING}, {hgnc=STRING}, {ensembl=STRING}]}'` You can then import data into your store as follows. `aws omics start-annotation-import-job \ --role-arn arn:aws:iam::555555555555:role/demoRole \ --items=source=s3://xquek-dev-aws/annotation-examples/mim2gene.txt \ --destination-name mim2gene \ --format-options=tsvOptions='{readOptions={sep="\t",header=false,comment="#"}}'` ## Starting VCF formatted import jobs For VCF files, there are two additional inputs, `ignoreQualField` and `ignoreFilterField`, that ignore or include those parameters as shown. `aws omics start-annotation-import-job --destination-name annotation_example\ --role-arn arn:aws:iam::555555555555:role/demoRole \ --items source=s3://demodata/example.garvan.vcf \ --format-options '{ "vcfOptions": { "ignoreQualField": false, "ignoreFilterField": false } }'` You can also cancel an annotation store import, as shown. If the cancellation succeeds, you don't receive a response to this AWS CLI call. However, if the import job ID isn't found or the import job is completed, you receive an error message. `aws omics cancel-annotation-import-job --job-id edd7b8ce-xmpl-47e2-bc99-258cac95a508` ###### Note Your metadata import job history for **get-annotation-import-job**, **get-variant-import-job**, **list-annotation-import-jobs**, and **list-variant-import-jobs** is auto-deleted after two years. The variant and annotation data that's imported isn't auto-deleted and remains in your data stores. |
