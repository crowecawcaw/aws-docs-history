

# Amazon S3 import formats for DynamoDB
<a name="S3DataImport.Format"></a>

DynamoDB can import data in three formats: CSV, DynamoDB JSON, and Amazon Ion.

**Topics**
+ [CSV](#S3DataImport.Requesting.Formats.CSV)
+ [DynamoDB Json](#S3DataImport.Requesting.Formats.DDBJson)
+ [Amazon Ion](#S3DataImport.Requesting.Formats.Ion)

## CSV
<a name="S3DataImport.Requesting.Formats.CSV"></a>

A file in CSV format consists of multiple items delimited by newlines. By default, DynamoDB interprets the first line of an import file as the header and expects columns to be delimited by commas. You can also define headers that will be applied, as long as they match the number of columns in the file. If you define headers explicitly, the first line of the file will be imported as values. 

**Note**  
When importing from CSV files, all columns other than the hash range and keys of your base table and secondary indexes are imported as DynamoDB strings.

**Escaping double quotes**

Any double quotes characters that exist in the CSV file must be escaped. If they are not escaped, such as in this following example, the import will fail: 

```
id,value
"123",Women's Full "Length" Dress
```

This same import will succeed if the quotes are escaped with two sets of double quotes:

```
id,value
"""123""","Women's Full ""Length"" Dress"
```

Once the text has been properly escaped and imported, it will appear as it did in the original CSV file:

```
id,value
"123",Women's Full "Length" Dress
```

DynamoDB follows the standard CSV quoting convention (RFC 4180): a double quote inside a field value is escaped by preceding it with another double quote (`""`). Backslash escaping (`\"`), which is common in programming languages and in the output of many data-export tools, is *not* recognized, and a file that uses it will fail to import. If your source data uses backslash escaping, convert each escaped quote to a doubled quote before importing. For example, a value exported as:

```
"Women's \"Full Length\" Dress"
```

must be reformatted as follows before it can be imported:

```
"Women's ""Full Length"" Dress"
```

**Formatting key values**

In DynamoDB, a primary key is either a *simple* primary key (a partition key) or a *composite* primary key (a partition key and a sort key). Each key attribute holds a single scalar value. If you want a key value that combines several fields — for example, joining `organizationId` and `barcode` with a delimiter as `organizationId#barcode` — you concatenate those fields into one string and store it in a single key attribute. This concatenation is an application convention; DynamoDB stores and matches the key attribute as one value.

When you import this data from CSV, put the fully joined value in a single column whose header matches the name of the key attribute. Do not split the parts into separate columns: the import maps each column to one attribute and does not concatenate columns into a key value. For example, for a table whose partition key attribute is named `pk` and sort key attribute is named `sk`:

```
pk,sk,barcode
org123#ABC123,number#001,ABC123
org456#XYZ789,number#002,XYZ789
```

If a key value itself contains the comma delimiter, enclose the entire value in double quotes, for example `"org123,east#ABC123"`.

**Importing heterogeneous item types**

You can use a single CSV file to import different item types into one table. Define a header row that includes all attributes across your item types, and leave columns empty for attributes that don't apply to a given item. Empty columns are omitted from the imported item rather than stored as empty strings.

```
PK,SK,EntityType,Name,Email,OrderDate,Amount,ProductName,Quantity
USER#1,PROFILE,User,Alice,alice@example.com,,,,
USER#1,ORDER#2024-01-15,Order,,,2024-01-15,99.99,,
USER#1,ORDER#2024-02-10,Order,,,2024-02-10,149.50,,
PRODUCT#101,METADATA,Product,,,,,Laptop,50
PRODUCT#102,METADATA,Product,,,,,Mouse,200
USER#2,PROFILE,User,Bob,bob@example.com,,,,
USER#2,ORDER#2024-01-20,Order,,,2024-01-20,75.00,,
PRODUCT#103,METADATA,Product,,,,,Keyboard,150
USER#3,PROFILE,User,Charlie,charlie@example.com,,,,
PRODUCT#104,METADATA,Product,,,,,Monitor,30
```

In this example, user profiles, orders, and products share the same table. Each item type uses only the columns relevant to it.

## DynamoDB Json
<a name="S3DataImport.Requesting.Formats.DDBJson"></a>

A file in DynamoDB JSON format can consist of multiple Item objects. Each individual object is in DynamoDB’s standard marshalled JSON format, and newlines are used as item delimiters. This is the [JSON Lines](https://jsonlines.org/) (JSONL) format: one JSON object per line, with no enclosing array and no commas between items. As an added feature, exports from point in time are supported as an import source by default.

**Note**  
New lines are used as item delimiters for a file in DynamoDB JSON format and shouldn't be used within an item object.

```
{"Item": {"Authors": {"SS": ["Author1", "Author2"]}, "Dimensions": {"S": "8.5 x 11.0 x 1.5"}, "ISBN": {"S": "333-3333333333"}, "Id": {"N": "103"}, "InPublication": {"BOOL": false}, "PageCount": {"N": "600"}, "Price": {"N": "2000"}, "ProductCategory": {"S": "Book"}, "Title": {"S": "Book 103 Title"}}}
{"Item": {"Authors": {"SS": ["Author1", "Author2"]}, "Dimensions": {"S": "8.5 x 11.0 x 1.5"}, "ISBN": {"S": "444-444444444"}, "Id": {"N": "104"}, "InPublication": {"BOOL": false}, "PageCount": {"N": "600"}, "Price": {"N": "2000"}, "ProductCategory": {"S": "Book"}, "Title": {"S": "Book 104 Title"}}}
{"Item": {"Authors": {"SS": ["Author1", "Author2"]}, "Dimensions": {"S": "8.5 x 11.0 x 1.5"}, "ISBN": {"S": "555-5555555555"}, "Id": {"N": "105"}, "InPublication": {"BOOL": false}, "PageCount": {"N": "600"}, "Price": {"N": "2000"}, "ProductCategory": {"S": "Book"}, "Title": {"S": "Book 105 Title"}}}
```

## Amazon Ion
<a name="S3DataImport.Requesting.Formats.Ion"></a>

[Amazon Ion](https://amzn.github.io/ion-docs/) is a richly-typed, self-describing, hierarchical data serialization format built to address rapid development, decoupling, and efficiency challenges faced every day while engineering large-scale, service-oriented architectures.

When you import data in Ion format, the Ion datatypes are mapped to DynamoDB datatypes in the new DynamoDB table.


| S. No. | Ion to DynamoDB datatype conversion | B | 
| --- | --- | --- | 
| `1` | `Ion Data Type` | `DynamoDB Representation` | 
| `2` | `string` | `String (s)` | 
| `3` | `bool` | `Boolean (BOOL)` | 
| `4` | `decimal` | `Number (N)` | 
| `5` | `blob` | `Binary (B)` | 
| `6` | `list (with type annotation $dynamodb_SS, $dynamodb_NS, or $dynamodb_BS)` | `Set (SS, NS, BS)` | 
| `7` | `list` | `List` | 
| `8` | `struct` | `Map` | 

Items in an Ion file are delimited by newlines. Each line begins with an Ion version marker, followed by an item in Ion format.

**Note**  
In the following example, we've formatted items from an Ion-formatted file on multiple lines to improve readability.

```
$ion_1_0
[
  {
    Item:{
      Authors:$dynamodb_SS::["Author1","Author2"],
      Dimensions:"8.5 x 11.0 x 1.5",
      ISBN:"333-3333333333",
      Id:103.,
      InPublication:false,
      PageCount:6d2,
      Price:2d3,
      ProductCategory:"Book",
      Title:"Book 103 Title"
    }
  },
  {
    Item:{
      Authors:$dynamodb_SS::["Author1","Author2"],
      Dimensions:"8.5 x 11.0 x 1.5",
      ISBN:"444-4444444444",
      Id:104.,
      InPublication:false,
      PageCount:6d2,
      Price:2d3,
      ProductCategory:"Book",
      Title:"Book 104 Title"
    }
  },
  {
    Item:{
      Authors:$dynamodb_SS::["Author1","Author2"],
      Dimensions:"8.5 x 11.0 x 1.5",
      ISBN:"555-5555555555",
      Id:105.,
      InPublication:false,
      PageCount:6d2,
      Price:2d3,
      ProductCategory:"Book",
      Title:"Book 105 Title"
    }
  }
]
```