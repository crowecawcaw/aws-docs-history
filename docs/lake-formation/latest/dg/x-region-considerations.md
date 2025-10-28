# Cross-Region data access limitations

Lake Formation supports querying Data Catalog tables across AWS Regions.
You can access data in a Region from other Regions using Amazon Athena, Amazon EMR, and AWS Glue ETL
by creating resource links in other Regions pointing to the source databases and tables.
With cross-Region table access, you can access data across Regions without copying the underlying data or the metadata into the Data Catalog.

The following limitations apply to cross-Region table access.

- Lake Formation doesn't support querying Data Catalog tables from another Region using Amazon Redshift Spectrum.
- In the Lake Formation console, the database and table views don't show the source Region database/table
  names.
- To view the list of tables under a shared database from another Region, you need to first create a resource link to the shared database, then select the resource link, and choose **View tables**.
- Lake Formation doesn't support cross-Region resource link calls made by SAML users.
- Lake Formation's cross-Region feature doesn't involve additional charges for
  data transfers.
