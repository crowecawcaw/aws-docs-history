# Filtering what fields are indexed in Neptune full-text search

There are two fields in the CloudFormation template details that let you specify property
or predicate keys or datatypes to exclude from OpenSearch indexing:

## Filter by property or predicate name

You can use the optional CloudFormation template parameter named `Properties to exclude
 from being inserted into Elastic Search Index` to provide a comma-delimited
list of property or predicate keys to exclude from OpenSearch indexing.

For example, suppose you set this parameter to `bob`:

```
"Properties to exclude from being inserted into Elastic Search Index" : bob
```

In that case, the stream record of the following Gremlin update query would be dropped
rather than going into the index:

```
g.V("1").property("bob", "test")
```

Similarly, you could set the parameter to `http://my/example#bob`:

```
"Properties to exclude from being inserted into Elastic Search Index" : http://my/example#bob
```

In that case, the stream record of the following SPARQL update query would be dropped
rather than going into the index:

```
PREFIX ex: <http://my/example#>
INSERT DATA { ex:s1 ex:bob "test"}.
```

If you don't enter anything in this CloudFormation template parameter, all the property
keys not otherwise excluded will be indexed.

## Filter by property or predicate value type

You can use the optional CloudFormation template parameter named `Datatypes to exclude
 from being inserted into Elastic Search Index` to provide a comma-delimited
list of property or predicate value datatypes to exclude from OpenSearch indexing.

For SPARQL, you don't need to list the full XSD type URI, you can just list
the datatype token. Valid datatype tokens that you can list are:

- `string`
- `boolean`
- `float`
- `double`
- `dateTime`
- `date`
- `time`
- `byte`
- `short`
- `int`
- `long`
- `decimal`
- `integer`
- `nonNegativeInteger`
- `nonPositiveInteger`
- `negativeInteger`
- `unsignedByte`
- `unsignedShort`
- `unsignedInt`
- `unsignedLong`

For Gremlin, valid datatypes to list are:

- `string`
- `date`
- `bool`
- `byte`
- `short`
- `int`
- `long`
- `float`
- `double`

For example, suppose you set this parameter to `string`:

```
"Datatypes to exclude from being inserted into Elastic Search Index" : string
```

In that case, the stream record of the following Gremlin update query would be dropped
rather than going into the index:

```
g.V("1").property("myStringval", "testvalue")
```

Similarly, you could set the parameter to `int`:

```
"Datatypes to exclude from being inserted into Elastic Search Index" : int
```

In that case, the stream record of the following SPARQL update query would be dropped
rather than going into the index:

```
PREFIX ex: <http://my/example#>
PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
INSERT DATA { ex:s1 ex:bob "11"^^xsd:int }.
```

If you don't enter anything in this CloudFormation template parameter, all the properties
whose values can be safely converted to OpenSearch equivalents will be indexed.
Listed types that are unsupported by the query language are ignored.
