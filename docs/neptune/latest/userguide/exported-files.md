# Files exported by Neptune-Export

and `neptune-export`

When an export is complete, the export files are published to the Amazon S3 location you have
specified. All files published to Amazon S3 are encrypted using Amazon S3 server-side encryption
(`SSE-S3`). The folders and files published to Amazon S3 vary depending on whether
you are exporting property-graph or RDF data. If you open the Amazon Amazon S3 location where
the files are published, you see the following content:

###### Locations of exported files in Amazon S3

- **`nodes/`**   –  
  This folder contains node data files in either a comma-separated value (CSV)
  or a JSON format.

In Neptune, nodes can have one or more labels. Nodes with different
individual labels (or different combinations of multiple labels) are written
to different files, meaning that no individual file contains data for nodes
with different combinations of labels. If a node has multiple labels, these
labels are sorted alphabetically before they are assigned to a file.

- **`edges/`**   –  
  This folder contains edge data files in either a comma-separated value (CSV)
  or a JSON format.

As with the nodes files, edge data is written to different files based on
a combinations of their labels. For purposes of model-training, edge data is
assigned to different files based on a combination of the edge's label plus
the labels of the edge's start and end nodes.

- **`statements/`**   –  
  This folder contains **RDF** data files in
  Turtle, N-Quads, N-Triples, or JSON format.
- **`config.json`**   –  
  This file contains the _schema_ of the graph as inferred by
  the export process.
- **`lastEventId.json`**   –  
  This file contains the `commitNum` and `opNum` of the last
  event on the database's Neptune streams. The export process only includes this
  file if you set the `includeLastEventId` export parameter to
  `true`, and the database from which you are exporting data has
  [Neptune streams](streams-using.md "streams-using.md") enabled.
