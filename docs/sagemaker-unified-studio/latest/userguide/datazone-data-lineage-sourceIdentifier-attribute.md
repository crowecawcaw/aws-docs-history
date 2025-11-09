# The importance of

the sourceIdentifier attribute to lineage nodes

Every lineage node is uniquely identified by its sourceIdentifier (usually
provided as part of open-lineage event) in addition to system generated nodeId.
sourceIdentifier is generated using <namespace>, <name> of the node in
lineage event.

The following are examples of sourceIdentifier values for different types of
nodes:

- **Job nodes**
  - SourceIdentifier of job nodes is populated from
    <namespace>.<name> on the job node in open-lineage run
    event

- **Jobrun nodes**
  - SourceIdentifier of jobrun nodes is populated from <job's
    namespace>.<job's name>/<run_id>

- **Dataset nodes**

      + Dataset nodes representing AWS resources: sourceIdentifier is in
       ARN format




      	- AWS Glue table:
      	 arn:aws:glue:<region>:<account-id>:table/<database>/<table-name>
      	- AWS Glue table with federated sources:
      	 arn:aws:glue:<region>:<account-id>:table/<catalog><database>/<table-name>




      		* Example: catalog can be
      		 "s3tablescatalog"/"s3tablesBucket",
      		 "lakehouse\_catalog" etc
      	- Amazon Redshift table:




      		* serverless:
      		 arn:aws:redshift-serverless:<region>:<account-id>:table/workgroupName/<database>/<schema>/<table-name>
      		* provisioned:
      		 arn:aws:redshift:<region>:<account-id>:table/clusterIdentifier/<database>/<schema>/<table-name>
      	- Amazon Redshift view:




      		* serverless:
      		 arn:aws:redshift-serverless:<region>:<account-id>:view/workgroupName/<database>/<schema>/<view-name>
      		* provisioned:
      		 arn:aws:redshift:<region>:<account-id>:view/clusterIdentifier/<database>/<schema>/<view-name>
      + Dataset nodes representing SageMaker catalog resources:




      	- Asset: amazon.datazone.asset/<assetId>
      	- Listing (published asset):
      	 amazon.datazone.listing/<listingId>
      + In all other cases, dataset nodes' sourceIdentifier is populated
       using <namespace>/<name> of the dataset nodes in
       open-lineage run event




      	- https://openlineage.io/docs/spec/naming/ contains naming
      	 convention for various datastores.

  The following table contains the examples of how sourceIdentifier is generated for
  datasets of different types.

| Source for lineage event      | Sample OpenLineage event data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Source ID computed by Amazon DataZone                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS Glue ETL                  | `<br>{<br>"run": {<br>"runId":"4e3da9e8-6228-4679-b0a2-fa916119fthr",<br>"facets":{<br>"environment-properties":{<br>....<br>"environment-properties":{<br>"GLUE_VERSION":"3.0",<br>"GLUE_COMMAND_CRITERIA":"glueetl",<br>"GLUE_PYTHON_VERSION":"3"<br>}<br>}<br>}<br>},<br>.....<br>"outputs":[<br>{<br>"namespace":"namespace.output",<br>"name":"output_name",<br>"facets":{<br>"symlinks":{<br>....<br>"identifiers":[<br>{<br>"namespace":"arn:aws:glue:us-west-2:123456789012",<br>"name":"table/testdb/testtb-1",<br>"type":"TABLE"<br>}<br>]<br>}<br>}<br>}<br>]<br>}<br>` | arn:aws:glue:us-west-2:123456789012:table/testdb/testtb-1<br>If environment-properties contains GLUE_VERSION,<br>GLUE_PYTHON_VERSION, etc, Amazon DataZone uses namespace and<br>name in symlink of the dataset (input or output) to construct<br>AWS Glue table ARN for sourceIdentifier.                                                                                                                                                        |
| Amazon Redshift (Provisioned) | `<br>{<br>"run": {<br>"runId":"4e3da9e8-6228-4679-b0a2-fa916119fthr",<br>"facets":{<br>.......<br>}<br>},<br>.....<br>"inputs":[<br>{<br>"namespace":"redshift://cluster-20240715.123456789012.us-east-1.redshift.amazonaws.com:5439",<br>"name":"tpcds_data.public.dws_tpcds_7"<br>"facets":{<br>.....<br>}<br>}<br>]<br>}<br>`                                                                                                                                                                                                                                                   | arn:aws:redshift:us-east-1:123456789012:table/cluster-20240715/tpcds_data/public/dws_tpcds_7<br>If the namespace prefix is `redshift`, Amazon<br>DataZone uses that to construct the Amazon Redshift ARN using<br>values of namespace and name attributes.                                                                                                                                                                                        |
| Amazon Redshift (serverless)  | `<br>{<br>"run": {<br>"runId":"4e3da9e8-6228-4679-b0a2-fa916119fthr",<br>"facets":{<br>.......<br>}<br>},<br>.....<br>"outputs":[<br>{<br>"namespace":"redshift://workgroup-20240715.123456789012.us-east-1.redshift-serverless.amazonaws.com:5439",<br>"name":"tpcds_data.public.dws_tpcds_7"<br>"facets":{<br>.....<br>}<br>}<br>]<br>}<br>`                                                                                                                                                                                                                                     | arn:aws:redshift-serverless:us-east-1:123456789012:table/workgroup-20240715/tpcds_data/public/dws_tpcds_7<br>As per OpenLineage naming convention, namespace for Amazon<br>Redshift dataset should be `provider://{cluster_identifier<br>or workgroup}.{region_name}:{port}`.<br>If the namespace contains `redshift-serverless`,<br>Amazon DataZone uses that to construct Amazon Redshift ARN using<br>values of namespace and name attributes. |
| Any other datastore           | Recommendation is to populate namespace and name as per<br>OpenLineage convention defined in [https://openlineage.io/docs/spec/naming/](https://openlineage.io/docs/spec/naming/ "https://openlineage.io/docs/spec/naming/").                                                                                                                                                                                                                                                                                                                                                      | Amazon DataZone populates sourceIdentifier as<br><namespace>/<name>.                                                                                                                                                                                                                                                                                                                                                                              |
