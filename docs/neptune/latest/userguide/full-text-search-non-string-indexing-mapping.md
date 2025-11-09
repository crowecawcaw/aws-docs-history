# Mapping of SPARQL and Gremlin datatypes to OpenSearch

New datatype mappings in OpenSearch are created based on the datatype
being used in the property or object. Because some fields contain values of
different types, the initial mapping may exclude some values of the field.

Neptune datatypes map to OpenSearch datatypes as follows:

| SPARQL types                                                                                                                                                  | Gremlin types                        | OpenSearch types |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ---------------- |
| `XSD:int`<br>`XSD:unsignedInt`<br>`XSD:integer`<br>`XSD:byte`<br>`XSD:unsignedByte`<br>`XSD:short`<br>`XSD:unsignedShort`<br>`XSD:long`<br>`XSD:unsignedLong` | `byte`<br>`short`<br>`int`<br>`long` | `long`           |
| `XSD:float`<br>`XSD:double`<br>`XSD:decimal`                                                                                                                  | `float`<br>`double`                  | `double`         |
| `XSD:boolean`                                                                                                                                                 | `bool`                               | `boolean`        |
| `XSD:datetime`<br>`XSD:date`                                                                                                                                  | `date`                               | `date`           |
| `XSD:string`<br>`XSD:time`                                                                                                                                    | `string`                             | `text`           |
| _Custom datatype_                                                                                                                                             | _N/A_                                | `text`           |
| _Any other datatype_                                                                                                                                          | _N/A_                                | `text`           |

For example, the following Gremlin update query causes a new mapping for
"newField" to be added to OpenSearch, namely `{ "type" : "double" }`:

```
g.V("1").property("newField" 10.5)
```

Similarly, the following SPARQL update query causes a new mapping for
"ex:byte" to be added to OpenSearch, namely `{ "type" : "long" }`:

```
PREFIX ex: <http://my/example#>
PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>

INSERT DATA { ex:test ex:byte "123"^^xsd:byte }.
```

###### Note

As you can see, an item mapped from Neptune to OpenSearch may end up
with a different datatype in OpenSearch than it has in Neptune. However, there
is an explicit text field in OpenSearch, "datatype", that records the datatype
that the item has in Neptune.
