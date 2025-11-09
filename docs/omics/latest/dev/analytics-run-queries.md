# Running queries on HealthOmics variant stores

###### Important

AWS HealthOmics variant stores and annotation stores are no longer open to new customers.
Existing customers can continue to use the service as normal.
For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

You can perform queries on your variant store using Amazon Athena. Note that genomic coordinates in variant and
annotation stores are represented as zero-based, half-closed half-open intervals.

## Run a simple query using the Athena console

The following example shows how to run a simple query.

1. Open the Athena Query editor: [Athena Query editor](https://console.aws.amazon.com/athena "https://console.aws.amazon.com/athena")
2. Under **Workgroup**, select the workgroup that you created during setup.
3. Verify that **Data source** is **AwsDataCatalog**.
4. For **Database**, select the database resource link that you created during the Lake Formation setup.
5. Copy the following query into the **Query Editor** under the **Query
   1** tab:

```
SELECT * from omicsvariants limit 10
```

6. Choose **Run** to run the query. The console populates the results table with the first
   10 rows of the **omicsvariants** table.

## Run a complex query using the Athena console

The following example shows how to run a complex query. To run this query, import `ClinVar` into the annotation
store.

###### Run a complex query

1. Open the Athena Query editor: [Athena Query editor](https://console.aws.amazon.com/athena "https://console.aws.amazon.com/athena")
2. Under**Workgroup**, select the workgroup that you created during setup.
3. Verify that **Data source** is **AwsDataCatalog**.
4. For **Database**, select the database resource link that you created during the Lake Formation setup.
5. Choose the **+** at the top right to create a new query tab named **Query
   2**.
6. Copy the following query into the **Query Editor** under the **Query
   2** tab:

```
SELECT variants.sampleid,
  variants.contigname,
  variants.start,
  variants."end",
  variants.referenceallele,
  variants.alternatealleles,
  variants.attributes AS variant_attributes,
  clinvar.attributes AS clinvar_attributes
FROM omicsvariants as variants
INNER JOIN omicsannotations as clinvar ON
  variants.contigname=CONCAT('chr',clinvar.contigname)
  AND variants.start=clinvar.start
  AND variants."end"=clinvar."end"
  AND variants.referenceallele=clinvar.referenceallele
  AND variants.alternatealleles=clinvar.alternatealleles
WHERE clinvar.attributes['CLNSIG']='Likely_pathogenic'

```

7. Choose **Run** to start running the query.
