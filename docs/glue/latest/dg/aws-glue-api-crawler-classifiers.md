# Classifier API

The Classifier API describes AWS Glue classifier data types,
and includes the API for creating, deleting, updating, and listing classifiers.

## Data types

- [Classifier structure](#aws-glue-api-crawler-classifiers-Classifier "#aws-glue-api-crawler-classifiers-Classifier")
- [GrokClassifier structure](#aws-glue-api-crawler-classifiers-GrokClassifier "#aws-glue-api-crawler-classifiers-GrokClassifier")
- [XMLClassifier structure](#aws-glue-api-crawler-classifiers-XMLClassifier "#aws-glue-api-crawler-classifiers-XMLClassifier")
- [JsonClassifier structure](#aws-glue-api-crawler-classifiers-JsonClassifier "#aws-glue-api-crawler-classifiers-JsonClassifier")
- [CsvClassifier structure](#aws-glue-api-crawler-classifiers-CsvClassifier "#aws-glue-api-crawler-classifiers-CsvClassifier")
- [CreateGrokClassifierRequest structure](#aws-glue-api-crawler-classifiers-CreateGrokClassifierRequest "#aws-glue-api-crawler-classifiers-CreateGrokClassifierRequest")
- [UpdateGrokClassifierRequest structure](#aws-glue-api-crawler-classifiers-UpdateGrokClassifierRequest "#aws-glue-api-crawler-classifiers-UpdateGrokClassifierRequest")
- [CreateXMLClassifierRequest structure](#aws-glue-api-crawler-classifiers-CreateXMLClassifierRequest "#aws-glue-api-crawler-classifiers-CreateXMLClassifierRequest")
- [UpdateXMLClassifierRequest structure](#aws-glue-api-crawler-classifiers-UpdateXMLClassifierRequest "#aws-glue-api-crawler-classifiers-UpdateXMLClassifierRequest")
- [CreateJsonClassifierRequest structure](#aws-glue-api-crawler-classifiers-CreateJsonClassifierRequest "#aws-glue-api-crawler-classifiers-CreateJsonClassifierRequest")
- [UpdateJsonClassifierRequest structure](#aws-glue-api-crawler-classifiers-UpdateJsonClassifierRequest "#aws-glue-api-crawler-classifiers-UpdateJsonClassifierRequest")
- [CreateCsvClassifierRequest structure](#aws-glue-api-crawler-classifiers-CreateCsvClassifierRequest "#aws-glue-api-crawler-classifiers-CreateCsvClassifierRequest")
- [UpdateCsvClassifierRequest structure](#aws-glue-api-crawler-classifiers-UpdateCsvClassifierRequest "#aws-glue-api-crawler-classifiers-UpdateCsvClassifierRequest")

## Classifier structure

Classifiers are triggered during a crawl task. A classifier checks whether
a given file is in a format it can handle. If it is, the classifier creates a schema
in the form of a `StructType` object that matches that data format.

You can use the standard classifiers that AWS Glue provides,
or you can write your own classifiers to best categorize your data sources and
specify the appropriate schemas to use for them. A classifier can be a `grok`
classifier, an `XML` classifier, a `JSON` classifier,
or a custom `CSV` classifier, as specified in one of the fields in
the `Classifier` object.

###### Fields

- `GrokClassifier` – A [GrokClassifier](#aws-glue-api-crawler-classifiers-GrokClassifier "#aws-glue-api-crawler-classifiers-GrokClassifier") object.

A classifier that uses `grok`.

- `XMLClassifier` – A [XMLClassifier](#aws-glue-api-crawler-classifiers-XMLClassifier "#aws-glue-api-crawler-classifiers-XMLClassifier") object.

A classifier for XML content.

- `JsonClassifier` – A [JsonClassifier](#aws-glue-api-crawler-classifiers-JsonClassifier "#aws-glue-api-crawler-classifiers-JsonClassifier") object.

A classifier for JSON content.

- `CsvClassifier` – A [CsvClassifier](#aws-glue-api-crawler-classifiers-CsvClassifier "#aws-glue-api-crawler-classifiers-CsvClassifier") object.

A classifier for comma-separated values (CSV).

## GrokClassifier structure

A classifier that uses `grok` patterns.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the classifier.

- `Classification` – _Required:_ UTF-8 string.

An identifier of the data format that the classifier matches, such as Twitter,
JSON, Omniture logs, and so on.

- `CreationTime` – Timestamp.

The time that this classifier was registered.

- `LastUpdated` – Timestamp.

The time that this classifier was last updated.

- `Version` – Number (long).

The version of this classifier.

- `GrokPattern` – _Required:_ UTF-8 string, not less than 1 or more than 2048 bytes long, matching the [A Logstash Grok string pattern](aws-glue-api-common.md#aws-glue-api-grok-pattern "aws-glue-api-common.md#aws-glue-api-grok-pattern").

The grok pattern applied to a data store by this classifier. For more information,
see built-in patterns in [Writing
Custom Classifiers](custom-classifier.md "custom-classifier.md").

- `CustomPatterns` – UTF-8 string, not more than 16000 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

Optional custom grok patterns defined by this classifier. For more information,
see custom patterns in [Writing
Custom Classifiers](custom-classifier.md "custom-classifier.md").

## XMLClassifier structure

A classifier for `XML` content.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the classifier.

- `Classification` – _Required:_ UTF-8 string.

An identifier of the data format that the classifier matches.

- `CreationTime` – Timestamp.

The time that this classifier was registered.

- `LastUpdated` – Timestamp.

The time that this classifier was last updated.

- `Version` – Number (long).

The version of this classifier.

- `RowTag` – UTF-8 string.

The XML tag designating the element that contains each record in an XML
document being parsed. This can't identify a self-closing element (closed by
`/>`). An empty row element that contains only attributes can
be parsed as long as it ends with a closing tag (for example, `<row item_a="A"
 item_b="B"></row>` is okay, but `<row item_a="A"
 item_b="B" />` is not).

## JsonClassifier structure

A classifier for `JSON` content.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the classifier.

- `CreationTime` – Timestamp.

The time that this classifier was registered.

- `LastUpdated` – Timestamp.

The time that this classifier was last updated.

- `Version` – Number (long).

The version of this classifier.

- `JsonPath` – _Required:_ UTF-8 string.

A `JsonPath` string defining the JSON data for the classifier
to classify. AWS Glue supports a subset of JsonPath, as described
in [Writing
JsonPath Custom Classifiers](custom-classifier.md#custom-classifier-json "custom-classifier.md#custom-classifier-json").

## CsvClassifier structure

A classifier for custom `CSV` content.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the classifier.

- `CreationTime` – Timestamp.

The time that this classifier was registered.

- `LastUpdated` – Timestamp.

The time that this classifier was last updated.

- `Version` – Number (long).

The version of this classifier.

- `Delimiter` – UTF-8 string, not less than 1 or more than 1 bytes long, matching the [Custom string pattern #26](aws-glue-api-common.md#regex_26 "aws-glue-api-common.md#regex_26").

A custom symbol to denote what separates each column entry in the row.

- `QuoteSymbol` – UTF-8 string, not less than 1 or more than 1 bytes long, matching the [Custom string pattern #26](aws-glue-api-common.md#regex_26 "aws-glue-api-common.md#regex_26").

A custom symbol to denote what combines content into a single column value.
It must be different from the column delimiter.

- `ContainsHeader` – UTF-8 string (valid values: `UNKNOWN` | `PRESENT` | `ABSENT`).

Indicates whether the CSV file contains a header.

- `Header` – An array of UTF-8 strings.

A list of strings representing column names.

- `DisableValueTrimming` – Boolean.

Specifies not to trim values before identifying the type of column values.
The default value is `true`.

- `AllowSingleColumn` – Boolean.

Enables the processing of files that contain only one column.

- `CustomDatatypeConfigured` – Boolean.

Enables the custom datatype to be configured.

- `CustomDatatypes` – An array of UTF-8 strings.

A list of custom datatypes including "BINARY", "BOOLEAN", "DATE", "DECIMAL",
"DOUBLE", "FLOAT", "INT", "LONG", "SHORT", "STRING", "TIMESTAMP".

- `Serde` – UTF-8 string (valid values: `OpenCSVSerDe` | `LazySimpleSerDe` | `None`).

Sets the SerDe for processing CSV in the classifier, which will be applied
in the Data Catalog. Valid values are `OpenCSVSerDe`, `LazySimpleSerDe`,
and `None`. You can specify the `None` value when you
want the crawler to do the detection.

## CreateGrokClassifierRequest structure

Specifies a `grok` classifier for `CreateClassifier`
to create.

###### Fields

- `Classification` – _Required:_ UTF-8 string.

An identifier of the data format that the classifier matches, such as Twitter,
JSON, Omniture logs, Amazon CloudWatch Logs, and so on.

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the new classifier.

- `GrokPattern` – _Required:_ UTF-8 string, not less than 1 or more than 2048 bytes long, matching the [A Logstash Grok string pattern](aws-glue-api-common.md#aws-glue-api-grok-pattern "aws-glue-api-common.md#aws-glue-api-grok-pattern").

The grok pattern used by this classifier.

- `CustomPatterns` – UTF-8 string, not more than 16000 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

Optional custom grok patterns used by this classifier.

## UpdateGrokClassifierRequest structure

Specifies a grok classifier to update when passed to `UpdateClassifier`.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the `GrokClassifier`.

- `Classification` – UTF-8 string.

An identifier of the data format that the classifier matches, such as Twitter,
JSON, Omniture logs, Amazon CloudWatch Logs, and so on.

- `GrokPattern` – UTF-8 string, not less than 1 or more than 2048 bytes long, matching the [A Logstash Grok string pattern](aws-glue-api-common.md#aws-glue-api-grok-pattern "aws-glue-api-common.md#aws-glue-api-grok-pattern").

The grok pattern used by this classifier.

- `CustomPatterns` – UTF-8 string, not more than 16000 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

Optional custom grok patterns used by this classifier.

## CreateXMLClassifierRequest structure

Specifies an XML classifier for `CreateClassifier` to create.

###### Fields

- `Classification` – _Required:_ UTF-8 string.

An identifier of the data format that the classifier matches.

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the classifier.

- `RowTag` – UTF-8 string.

The XML tag designating the element that contains each record in an XML
document being parsed. This can't identify a self-closing element (closed by
`/>`). An empty row element that contains only attributes can
be parsed as long as it ends with a closing tag (for example, `<row item_a="A"
 item_b="B"></row>` is okay, but `<row item_a="A"
 item_b="B" />` is not).

## UpdateXMLClassifierRequest structure

Specifies an XML classifier to be updated.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the classifier.

- `Classification` – UTF-8 string.

An identifier of the data format that the classifier matches.

- `RowTag` – UTF-8 string.

The XML tag designating the element that contains each record in an XML
document being parsed. This cannot identify a self-closing element (closed
by `/>`). An empty row element that contains only attributes
can be parsed as long as it ends with a closing tag (for example, `<row
 item_a="A" item_b="B"></row>` is okay, but `<row
 item_a="A" item_b="B" />` is not).

## CreateJsonClassifierRequest structure

Specifies a JSON classifier for `CreateClassifier` to create.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the classifier.

- `JsonPath` – _Required:_ UTF-8 string.

A `JsonPath` string defining the JSON data for the classifier
to classify. AWS Glue supports a subset of JsonPath, as described
in [Writing
JsonPath Custom Classifiers](custom-classifier.md#custom-classifier-json "custom-classifier.md#custom-classifier-json").

## UpdateJsonClassifierRequest structure

Specifies a JSON classifier to be updated.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the classifier.

- `JsonPath` – UTF-8 string.

A `JsonPath` string defining the JSON data for the classifier
to classify. AWS Glue supports a subset of JsonPath, as described
in [Writing
JsonPath Custom Classifiers](custom-classifier.md#custom-classifier-json "custom-classifier.md#custom-classifier-json").

## CreateCsvClassifierRequest structure

Specifies a custom CSV classifier for `CreateClassifier`
to create.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the classifier.

- `Delimiter` – UTF-8 string, not less than 1 or more than 1 bytes long, matching the [Custom string pattern #26](aws-glue-api-common.md#regex_26 "aws-glue-api-common.md#regex_26").

A custom symbol to denote what separates each column entry in the row.

- `QuoteSymbol` – UTF-8 string, not less than 1 or more than 1 bytes long, matching the [Custom string pattern #26](aws-glue-api-common.md#regex_26 "aws-glue-api-common.md#regex_26").

A custom symbol to denote what combines content into a single column value.
Must be different from the column delimiter.

- `ContainsHeader` – UTF-8 string (valid values: `UNKNOWN` | `PRESENT` | `ABSENT`).

Indicates whether the CSV file contains a header.

- `Header` – An array of UTF-8 strings.

A list of strings representing column names.

- `DisableValueTrimming` – Boolean.

Specifies not to trim values before identifying the type of column values.
The default value is true.

- `AllowSingleColumn` – Boolean.

Enables the processing of files that contain only one column.

- `CustomDatatypeConfigured` – Boolean.

Enables the configuration of custom datatypes.

- `CustomDatatypes` – An array of UTF-8 strings.

Creates a list of supported custom datatypes.

- `Serde` – UTF-8 string (valid values: `OpenCSVSerDe` | `LazySimpleSerDe` | `None`).

Sets the SerDe for processing CSV in the classifier, which will be applied
in the Data Catalog. Valid values are `OpenCSVSerDe`, `LazySimpleSerDe`,
and `None`. You can specify the `None` value when you
want the crawler to do the detection.

## UpdateCsvClassifierRequest structure

Specifies a custom CSV classifier to be updated.

###### Fields

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the classifier.

- `Delimiter` – UTF-8 string, not less than 1 or more than 1 bytes long, matching the [Custom string pattern #26](aws-glue-api-common.md#regex_26 "aws-glue-api-common.md#regex_26").

A custom symbol to denote what separates each column entry in the row.

- `QuoteSymbol` – UTF-8 string, not less than 1 or more than 1 bytes long, matching the [Custom string pattern #26](aws-glue-api-common.md#regex_26 "aws-glue-api-common.md#regex_26").

A custom symbol to denote what combines content into a single column value.
It must be different from the column delimiter.

- `ContainsHeader` – UTF-8 string (valid values: `UNKNOWN` | `PRESENT` | `ABSENT`).

Indicates whether the CSV file contains a header.

- `Header` – An array of UTF-8 strings.

A list of strings representing column names.

- `DisableValueTrimming` – Boolean.

Specifies not to trim values before identifying the type of column values.
The default value is true.

- `AllowSingleColumn` – Boolean.

Enables the processing of files that contain only one column.

- `CustomDatatypeConfigured` – Boolean.

Specifies the configuration of custom datatypes.

- `CustomDatatypes` – An array of UTF-8 strings.

Specifies a list of supported custom datatypes.

- `Serde` – UTF-8 string (valid values: `OpenCSVSerDe` | `LazySimpleSerDe` | `None`).

Sets the SerDe for processing CSV in the classifier, which will be applied
in the Data Catalog. Valid values are `OpenCSVSerDe`, `LazySimpleSerDe`,
and `None`. You can specify the `None` value when you
want the crawler to do the detection.

## Operations

- [CreateClassifier action (Python: create_classifier)](#aws-glue-api-crawler-classifiers-CreateClassifier "#aws-glue-api-crawler-classifiers-CreateClassifier")
- [DeleteClassifier action (Python: delete_classifier)](#aws-glue-api-crawler-classifiers-DeleteClassifier "#aws-glue-api-crawler-classifiers-DeleteClassifier")
- [GetClassifier action (Python: get_classifier)](#aws-glue-api-crawler-classifiers-GetClassifier "#aws-glue-api-crawler-classifiers-GetClassifier")
- [GetClassifiers action (Python: get_classifiers)](#aws-glue-api-crawler-classifiers-GetClassifiers "#aws-glue-api-crawler-classifiers-GetClassifiers")
- [UpdateClassifier action (Python: update_classifier)](#aws-glue-api-crawler-classifiers-UpdateClassifier "#aws-glue-api-crawler-classifiers-UpdateClassifier")

## CreateClassifier action (Python: create_classifier)

Creates a classifier in the user's account. This can be a `GrokClassifier`,
an `XMLClassifier`, a `JsonClassifier`, or a `CsvClassifier`,
depending on which field of the request is present.

###### Request

- `GrokClassifier` – A [CreateGrokClassifierRequest](#aws-glue-api-crawler-classifiers-CreateGrokClassifierRequest "#aws-glue-api-crawler-classifiers-CreateGrokClassifierRequest") object.

A `GrokClassifier` object specifying the classifier to
create.

- `XMLClassifier` – A [CreateXMLClassifierRequest](#aws-glue-api-crawler-classifiers-CreateXMLClassifierRequest "#aws-glue-api-crawler-classifiers-CreateXMLClassifierRequest") object.

An `XMLClassifier` object specifying the classifier to
create.

- `JsonClassifier` – A [CreateJsonClassifierRequest](#aws-glue-api-crawler-classifiers-CreateJsonClassifierRequest "#aws-glue-api-crawler-classifiers-CreateJsonClassifierRequest") object.

A `JsonClassifier` object specifying the classifier to
create.

- `CsvClassifier` – A [CreateCsvClassifierRequest](#aws-glue-api-crawler-classifiers-CreateCsvClassifierRequest "#aws-glue-api-crawler-classifiers-CreateCsvClassifierRequest") object.

A `CsvClassifier` object specifying the classifier to create.

###### Response

- _No Response parameters._

###### Errors

- `AlreadyExistsException`
- `InvalidInputException`
- `OperationTimeoutException`

## DeleteClassifier action (Python: delete_classifier)

Removes a classifier from the Data Catalog.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the classifier to remove.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `OperationTimeoutException`

## GetClassifier action (Python: get_classifier)

Retrieve a classifier by name.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the classifier to retrieve.

###### Response

- `Classifier` – A [Classifier](#aws-glue-api-crawler-classifiers-Classifier "#aws-glue-api-crawler-classifiers-Classifier") object.

The requested classifier.

###### Errors

- `EntityNotFoundException`
- `OperationTimeoutException`

## GetClassifiers action (Python: get_classifiers)

Lists all classifier objects in the Data Catalog.

###### Request

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The size of the list to return (optional).

- `NextToken` – UTF-8 string.

An optional continuation token.

###### Response

- `Classifiers` – An array of [Classifier](#aws-glue-api-crawler-classifiers-Classifier "#aws-glue-api-crawler-classifiers-Classifier") objects.

The requested list of classifier objects.

- `NextToken` – UTF-8 string.

A continuation token.

###### Errors

- `OperationTimeoutException`

## UpdateClassifier action (Python: update_classifier)

Modifies an existing classifier (a `GrokClassifier`, an
`XMLClassifier`, a `JsonClassifier`, or a `CsvClassifier`,
depending on which field is present).

###### Request

- `GrokClassifier` – An [UpdateGrokClassifierRequest](#aws-glue-api-crawler-classifiers-UpdateGrokClassifierRequest "#aws-glue-api-crawler-classifiers-UpdateGrokClassifierRequest") object.

A `GrokClassifier` object with updated fields.

- `XMLClassifier` – An [UpdateXMLClassifierRequest](#aws-glue-api-crawler-classifiers-UpdateXMLClassifierRequest "#aws-glue-api-crawler-classifiers-UpdateXMLClassifierRequest") object.

An `XMLClassifier` object with updated fields.

- `JsonClassifier` – An [UpdateJsonClassifierRequest](#aws-glue-api-crawler-classifiers-UpdateJsonClassifierRequest "#aws-glue-api-crawler-classifiers-UpdateJsonClassifierRequest") object.

A `JsonClassifier` object with updated fields.

- `CsvClassifier` – An [UpdateCsvClassifierRequest](#aws-glue-api-crawler-classifiers-UpdateCsvClassifierRequest "#aws-glue-api-crawler-classifiers-UpdateCsvClassifierRequest") object.

A `CsvClassifier` object with updated fields.

###### Response

- _No Response parameters._

###### Errors

- `InvalidInputException`
- `VersionMismatchException`
- `EntityNotFoundException`
- `OperationTimeoutException`
