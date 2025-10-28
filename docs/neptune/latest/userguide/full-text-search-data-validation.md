# Validation of data mappings

Data is replicated to OpenSearch from Neptune using this process:

- If a mapping for the field in question is already present in OpenSearch:
  - If the data can be safely converted to the existing mapping using
    data validation rules, then store the field in OpenSearch.
  - If not, drop the corresponding stream update record.

- If there is no existing mapping for the field in question, find an OpenSearch
  datatype corresponding to the field's datatype in Neptune.

      + If the field data can be safely converted to the OpenSearch datatype using
       data validation rules, then store the new mapping and field data in OpenSearch.
      + If not, drop the corresponding stream update record.

  Values are validated against equivalent OpenSearch types or existing
  OpenSearch mappings rather than the Neptune types. For example, validation for
  the value `"123"` in `"123"^^xsd:int` is done against the
  `long` type rather than the `int` type.

Although Neptune attempts to replicate all data to OpenSearch, there are
cases where datatypes in OpenSearch are totally different from the ones in Neptune,
and in such cases records are skipped rather than being indexed in OpenSearch.

For example, in Neptune one property can have multiple values of different types,
whereas in OpenSearch a field must have the same type across the index.

By enabling debug logs, you can view what records have been dropped during
export from Neptune to OpenSearch. An example of a debug log entry is:

```
Dropping Record : Data type not a valid Gremlin type
<Record>
```

Datatypes are validated as follows:

- **`text`**   –  
  All values in Neptune can safely be mapped to text in OpenSearch.
- **`long`**   –  
  The following rules for Neptune datatypes apply when the OpenSearch mapping
  type is long (in the examples below, it is assumed that `"testLong"` has
  a `long` mapping type):
  - `boolean`   –  
    Invalid, cannot be converted, and the corresponding stream update record is dropped.

  Invalid Gremlin examples are:

  ```
    "testLong" : true.
    "testLong" : false.
  ```

  Invalid SPARQL examples are:

  ```
    ":testLong" : "true"^^xsd:boolean
    ":testLong" : "false"^^xsd:boolean
  ```

  - `datetime`   –  
    Invalid, cannot be converted, and the corresponding stream update record is dropped.

  An invalid Gremlin example is:

  ```
    ":testLong" :  datetime('2018-11-04T00:00:00').
  ```

  An invalid SPARQL example is:

  ```
    ":testLong" : "2016-01-01"^^xsd:date
  ```

  - `float`, `double`, or `decimal`   –  
    If the value in Neptune is an integer that can fit in 64 bits, it is valid and
    is stored in OpenSearch as a long, but if it has a fractional part, or is a
    `NaN` or an `INF`, or is larger than 9,223,372,036,854,775,807
    or smaller than -9,223,372,036,854,775,808, then it is not valid and the
    corresponding stream update record is dropped.

  Valid Gremlin examples are:

  ```
    "testLong" :  145.0.
    ":testLong" :  123
    ":testLong" :  -9223372036854775807
  ```

  Valid SPARQL examples are:

  ```
    ":testLong" : "145.0"^^xsd:float
    ":testLong" :  145.0
    ":testLong" : "145.0"^^xsd:double
    ":testLong" : "145.0"^^xsd:decimal
    ":testLong" : "-9223372036854775807"
  ```

  Invalid Gremlin examples are:

  ```
    "testLong" :  123.45
    ":testLong" :  9223372036854775900
  ```

  Invalid SPARQL examples are:

  ```
    ":testLong" :  123.45
    ":testLong" :  9223372036854775900
    ":testLong" : "123.45"^^xsd:float
    ":testLong" : "123.45"^^xsd:double
    ":testLong" : "123.45"^^xsd:decimal
  ```

  - `string`   –  
    If the value in Neptune is a string representation of an integer that can be
    contained in a 64-bit integer, then it it is valid and is converted to a
    `long` in OpenSearch. Any other string value is
    invalid for an Elasticseearch `long` mapping, and the corresponding
    stream update record is dropped.

  Valid Gremlin examples are:

  ```
    "testLong" :  "123".
    ":testLong" :  "145.0"
    ":testLong" :  "-9223372036854775807"
  ```

  Valid SPARQL examples are:

  ```
    ":testLong" : "145.0"^^xsd:string
    ":testLong" : "-9223372036854775807"^^xsd:string
  ```

  Invalid Gremlin examples are:

  ```
    "testLong" :  "123.45"
    ":testLong" :  "9223372036854775900"
    ":testLong" :  "abc"
  ```

  Invalid SPARQL examples are:

  ```
    ":testLong" : "123.45"^^xsd:string
    ":testLong" : "abc"
    ":testLong" : "9223372036854775900"^^xsd:string
  ```

- **`double`**   –  
  If the OpenSearch mapping type is `double`, the following
  rules apply (here, the "testDouble" field is assumed to have a
  `double` mapping in OpenSearch):
  - `boolean`   –  
    Invalid, cannot be converted, and the corresponding stream update record is dropped.

  Invalid Gremlin examples are:

  ```
    "testDouble" : true.
    "testDouble" : false.
  ```

  Invalid SPARQL examples are:

  ```
    ":testDouble" : "true"^^xsd:boolean
    ":testDouble" : "false"^^xsd:boolean
  ```

  - `datetime`   –  
    Invalid, cannot be converted, and the corresponding stream update record is dropped.

  An invalid Gremlin example is:

  ```
    ":testDouble" :  datetime('2018-11-04T00:00:00').
  ```

  An invalid SPARQL example is:

  ```
    ":testDouble" : "2016-01-01"^^xsd:date
  ```

  - Floating-point `NaN` or `INF`   –  
    If the value in SPARQL is a floating-point `NaN` or `INF`,
    then it is not valid and the corresponding stream update record is dropped.

  Invalid SPARQL examples are:

  ```
  "  :testDouble" : "NaN"^^xsd:float
    ":testDouble" : "NaN"^^double
    ":testDouble" : "INF"^^double
    ":testDouble" : "-INF"^^double
  ```

  - number or numeric string   –  
    If the value in Neptune is any other number or numeric string representation
    of a numnber that can safely be expressed as a `double`, then it
    is valid and is converted to a `double` in OpenSearch.
    Any other string value is invalid for an OpenSearch `double`
    mapping, and the corresponding stream update record is dropped.

  Valid Gremlin examples are:

  ```
    "testDouble" :  123
    ":testDouble" :  "123"
    ":testDouble" :  145.67
    ":testDouble" :  "145.67"
  ```

  Valid SPARQL examples are:

  ```
    ":testDouble" :  123.45
    ":testDouble" :  145.0
    ":testDouble" : "123.45"^^xsd:float
    ":testDouble" : "123.45"^^xsd:double
    ":testDouble" : "123.45"^^xsd:decimal
    ":testDouble" : "123.45"^^xsd:string
  ```

  An invalid Gremlin example is:

  ```
    ":testDouble" :  "abc"
  ```

  An Invalid SPARQL examples is:

  ```
    ":testDouble" : "abc"
  ```

- **`date`**   –  
  If the OpenSearch mapping type is `date`, Neptune
  `date` and `dateTime` value are valid, as is any
  string value that can be parsed successfully to a `dateTime`
  format.

Valid examples in either Gremlin or SPARQL are:

```
  Date(2016-01-01)
  "2016-01-01" "
  2003-09-25T10:49:41"
  "2003-09-25T10:49"
  "2003-09-25T10"
  "20030925T104941-0300"
  "20030925T104941"
  "2003-Sep-25" "
  Sep-25-2003"
  "2003.Sep.25"
  "2003/09/25"
  "2003 Sep 25" "
  Wed, July 10, '96"
  "Tuesday, April 12, 1952 AD 3:30:42pm PST"
  "123"
  "-123"
  "0"
  "-0"
  "123.00"
  "-123.00"
```

Invalid examples are:

```
  123.45
  True
  "abc"
```
