

# Map state input and output fields in Step Functions
<a name="input-output-fields-dist-map"></a>

**Managing state and transforming data**  
Learn about [Passing data between states with variables](workflow-variables.md) and [Transforming data with JSONata](transforming-data.md).

Map states iterate over a collection of items in a dataset. Examples of data sets include: 
+ JSON arrays and objects from previous states.
+ Individual data files stored in Amazon S3 in formats such as: JSON, JSONL, CSV, Parquet files.
+ References to multiple objects, such as: Athena manifests and Amazon S3 inventory files

A map repeats a set of steps for each item in the dataset. You can configure the input that the `Map state` receives and the output the map generates using a variety of configuration options. Step Functions applies each option in your *Distributed Map state* in the order shown in the following list. Depending on your use case, you may not need to apply all of fields.

1. [ItemReader (Map)](input-output-itemreader.md) - used to read your data items

1. [ItemsPath (Map, JSONPath only)](input-output-itemspath.md) or **Items (JSONata)** - optional; used to specify items in your dataset

1. [ItemSelector (Map)](input-output-itemselector.md) - optional; used to select and modify items in the data set 

1. [ItemBatcher (Map)](input-output-itembatcher.md) - used to process groups of items when processing large sets of items

1. [ResultWriter (Map)](input-output-resultwriter.md) - provides options for output results from child workflows