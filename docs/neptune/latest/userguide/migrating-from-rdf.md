# Migrating an existing graph from an RDF triple store to Amazon Neptune

If you have graph data in an RDF/SPARQL
to migrate to Amazon Neptune, you would take the following steps:

1. Export the data from your RDF triple store.
2. Convert the exported data to a [format
   that the Neptune bulk loader can import](bulk-load-tutorial-format-rdf.md "bulk-load-tutorial-format-rdf.md").
3. Store the data to be imported in Amazon Simple Storage Service (Amazon S3).
4. Using [Neptune Bulk Loader](bulk-load.md "bulk-load.md"),
   import the data from Amazon S3 into a Neptune DB cluster that you have prepared.
5. Modify your existing application to connect to Neptune's SPARQL endpoint.
   If you want to try out migrating property-graph CSV data into RDF, you can use
   the [Amazon Neptune
   CSV to RDF converter](https://github.com/aws/amazon-neptune-csv-to-rdf-converter "https://github.com/aws/amazon-neptune-csv-to-rdf-converter").
