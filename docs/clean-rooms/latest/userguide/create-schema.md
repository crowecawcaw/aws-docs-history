# (Optional) Create a schema (advanced users)

Creating a schema manually is for advanced users.

The following is a description of the JSON schema file format for input files with or
without column headers. Advanced users can directly write or modify the schema if
desired.

###### Note

The C3R encryption client can assist you in making a schema through either the interactive
process described in [Example: Generate an encryption schema with
sealed, fingerprint, and cleartext
columns](gen-encryption-schema-csv.md#gen-encryption-schema "gen-encryption-schema-csv.md#gen-encryption-schema") or through the creation of a stub template.

## Mapped and positional table schemas

The following section describes two kinds of table schemas:

- **Mapped table schema** – This schema is used
  for encrypting .csv files with a header row and Apache Parquet
  files.
- **Positional table schema** – This schema is
  used for encrypting .csv files without a header row.

The C3R encryption client can encrypt a tabular file for a collaboration. To do this, it must
have a corresponding schema file that specifies how the encrypted output should be derived
from the input.

The C3R encryption client can help generate a schema for an `INPUT` file by running
the C3R encryption client schema command at the command line. An example of a command is `java
 -jar c3r-cli.jar schema --interactive INPUT`.

The schema specifies the following
information:

1. Which source columns map to which transformed columns in the output file through
   their header names (mapped schemas) or position (positional schemas)
2. Which target columns are to remain cleartext
3. Which target columns are to be encrypted for SELECT queries
4. Which target columns are to be encrypted for JOIN queries

This information is encoded in a table-specific JSON schema file, which consists of a
single object whose `headerRow` field is a Boolean value. The value must be
`true` for Parquet files and .csv files with a header row, and
`false` otherwise.

### Mapped table schema

The mapped schema has the following shape.

```
{
  "headerRow": true,
  "columns": [
    {
      "sourceHeader": STRING,
      "targetHeader": STRING,
      "type": TYPE,
      "pad": PAD
    },
    ...
  ]
}
```

If `headerRow` is `true`, the next field in the object is
`columns`, which contains an array of column schemas that map source headers
to target headers (that is, JSON objects describing what the output columns should
contain).

- `sourceHeader` – The `STRING` header name of the
  source column that the data is derived from.

###### Note

The same source column can be used for multiple target columns.

A column from the input file not listed as a `sourceHeader` anywhere
in the schema doesn't appear in the output file.

- `targetHeader` – The `STRING` header name of the
  corresponding column in the output file.

###### Note

This field is optional for mapped schemas. If this field is omitted, the
`sourceHeader` is re-used for the header name in the output. Either
`_fingerprint` or `_sealed` is appended if the output column
is a fingerprint column or sealed column respectively.

- `type` – The `TYPE` of the target column in the
  output file. That is, one of `cleartext`, `sealed`, or
  `fingerprint` depending on how the column will be used in the
  collaboration.
- `pad` – A field of a column schema object that is only present
  when the `TYPE` is `sealed`. Its corresponding value of
  `PAD` is an object that describes how the data should be padded before
  it's encrypted.

```
{
  "type": PAD_TYPE,
  "length": INT
}
```

To specify pre-encryption padding, `type` and `length` are
used as follows:

    + `PAD_TYPE` as `none` – No padding will be applied
     to the column's data and the `length` field is not applicable (that is,
     omitted).
    + `PAD_TYPE` as `fixed` – The column's data is
     padded to the specified `length` of bytes.
    + `PAD_TYPE` as `max` – The column's data is padded
     to the size of the longest value's byte length plus an additional
     `length` bytes.

The following is an example mapped schema, with a column of each type.

```
{
  "headerRow": true,
  "columns": [
    {
      "sourceHeader": "FullName",
      "targetHeader": "name",
      "type": "cleartext"
    },
    {
      "sourceHeader": "City",
      "targetHeader": "city_sealed",
      "type": "sealed",
      "pad": {
        "type": "max",
        "length": 16
      }
    },
    {
      "sourceHeader": "PhoneNumber",
      "targetHeader": "phone_number_fingerprint",
      "type": "fingerprint"
    },
    {
      "sourceHeader": "PhoneNumber",
      "targetHeader": "phone_number_sealed",
      "type": "sealed",
      "pad": {
        "type": "fixed",
        "length": 20
      }
    }
  ]
}
```

As a more complex example, the following is an example .csv file with headers.

```
FirstName,LastName,Address,City,State,PhoneNumber,Title,Level,Notes
Jorge,Souza,12345 Mills Rd,Anytown,SC,703-555-1234,CEO,10,
Paulo,Santos,0 Street,Anytown,MD,404-555-111,CIO,9,This is a really long note that could really be a paragraph
Mateo,Jackson,1 Two St,Anytown,NY,304-555-1324,COO,9,""
Terry,Whitlock4 N St,Anytown,VA,407-555-8888,EA,7,Secret notes
Diego,Ramirez,9 Hollows Rd,Anytown,VA,407-555-1222,SDE I,4,null
John,Doe,8 Hollows Rd,Anytown,VA,407-555-4321,SDE I,4,Jane's younger brother
Jane,Doe,8 Hollows Rd,Anytown,VA,407-555-4322,SDE II,5,John's older sister
```

In the following mapped schema example, the columns `FirstName` and
`LastName` are `cleartext` columns. The `State` column
is encrypted as a `fingerprint` column and as a `sealed` column with
a padding of `none`. The remaining columns are omitted.

```
{
  "headerRow": true,
  "columns": [
    {
      "sourceHeader": "FirstName",
      "targetHeader": "GivenName",
      "type": "cleartext"
    },
    {
      "sourceHeader": "LastName",
      "targetHeader": "Surname",
      "type": "cleartext"
    },
    {
      "sourceHeader": "State",
      "targetHeader": "State_Join",
      "type": "fingerprint"
    },
    {
      "sourceHeader": "State",
      "targetHeader": "State",
      "type": "sealed",
      "pad": {
        "type": "none"
      }
    }
  ]
}
```

The following is the .csv file that results from the mapped schema.

```
givenname,surname,state_fingerprint,state
John,Doe,01:hmac:UK8s8Cn/WR2JO/To2dTxWD73aDEe2ZUXeSHy3Tv+1Mk=,01:enc:FQ3n3Ahv9BQQNWQGcugeHzHYzEZE1vapHa2Uu4SRgSAtZ3qObjPA4TcsHt+BOkMKBcnHWI13BeGG/SBqmj7vKpI=
Paulo,Santos,01:hmac:CHF4eIrtTNgAooU9v4h9Qjc+txBnMidQTjdjWuaDTTA=,01:enc:KZ5n5GtaXACco65AXk48BQO2durDNR2ULc4YxmMC8NaZZKKJiksU1IwFadAvV4iBQ1Bus5TU5c4biez3bilfTY8=
Mateo,Jackson,01:hmac:iIRnjfNBzryusIJ1w35lgNzeY1RQ1bSfq6PDHW8Xrbk=,01:enc:mLKpS5HIOSgphdEsrzhEdIp/eN9nBO2gAbIygt4OFn4LalYn9Xyj/XUWXlmn8zFe2T4kyDTD8kGOvpQEUGxAUFk=
Diego,Ramirez,01:hmac:UK8s8Cn/WR2JO/To2dTxWD73aDEe2ZUXeSHy3Tv+1Mk=,01:enc:rmZhT98Zm+IIGw1UTjMIJP4IrW/AAltBLMXcHvnYfRgmWP623VFQ6aUnhsb2MDqEw4G5Uwg5rKKZepUxx5uKbfk=
Jorge,Souza,01:hmac:3BxJdXiFFyZ8HBbYNqqEhBVqhNOd7s2ZiKUe7QiTyo8=,01:enc:vVaqWC1VRbhvkf8gnuR7q0zxVPcvEjuaglYz34+KyyLcGZLpAmsDUc6wZ07f2KvHoOySqRsEU7dG1QfdHYcTSWE=
Terry,Whitlock01:hmac:UK8s8Cn/WR2JO/To2dTxWD73aDEe2ZUXeSHy3Tv+1Mk=,01:enc:3c9VEWbODO/xbQjdGuccLvI7oZTBdPU+SyrJIyr2kudfAxbuMQ2uRdU/q7rbgyJjxZS8M2U35ILJf/lDgTyg7cM=
Jane,Doe,01:hmac:UK8s8Cn/WR2JO/To2dTxWD73aDEe2ZUXeSHy3Tv+1Mk=,01:enc:9RWv46YLveykeNZ/G0NdlYFg+AVdOnu05hHyAYTQkPLHnyX+0/jbzD/g9ZT8GCgVE9aB5bV4ooJIXHGBVMXcjrQ=
```

### Positional table schema

The positional schema has the following shape.

```
{
  "headerRow": false,
  "columns": [
    [
      {
        "targetHeader": STRING,
        "type": TYPE,
        "pad": PAD
      },
      {
        "targetHeader": STRING,
        "type": TYPE,
        "pad": PAD
      }
    ],
    [],
    ...
  ]
}
```

If `headerRow` is `false`, the next field in the object is
`columns`, which contains an array of entries. Each entry is itself an array
of zero or more positional column schemas (no `sourceHeader` field), which are
JSON objects describing what the output should contain.

- `sourceHeader` – The `STRING` header name of the
  source column that the data is derived from.

###### Note

This field must be omitted in positional schemas. In positional schemas, the
source column is inferred by the column's corresponding index in the schema
file.

- `targetHeader` – The `STRING` header name of the
  corresponding column in the output file.

###### Note

This field is required for positional schemas.

- `type` – The `TYPE` of the target column in the
  output file. That is, one of `cleartext`, `sealed`, or
  `fingerprint` depending on how the column will be used in the
  collaboration.
- `pad` – A field of a column schema object that is only present
  when the `TYPE` is `sealed`. Its corresponding value of
  `PAD` is an object that describes how the data should be padded before
  it's encrypted.

```
{
  "type": PAD_TYPE,
  "length": INT
}
```

To specify pre-encryption padding, `type` and `length` are
used as follows:

    + `PAD_TYPE` as `none` – No padding will be applied
     to the column's data and the `length` field is not applicable (that is,
     omitted).
    + `PAD_TYPE` as `fixed` – The column's data is
     padded to the specified `length` of bytes.
    + `PAD_TYPE` as `max` – The column's data is padded
     to the size of the longest value's byte length plus an additional
     `length` bytes.


    ###### Note

    `fixed` is useful if you know ahead of time of an upper bound on
     the byte size of the column's data. An error is raised if any data in that
     column is longer than the specified `length`.

    `max` is convenient when the exact size of input data is unknown
     because it works regardless of the data's size. However, `max`
     requires additional processing time because it encrypts the data twice.
     `max` encrypts the data once when read in to the temporary file and
     once after the longest data entry in the column is known.

    Also, the length of the longest value isn't saved between invocations of the
     client. If you plan to encrypt your data in batches, or to encrypt new data
     periodically, be aware that the resulting ciphertext-lengths might vary among
     batches.

The following is an example of a positional schema.

```
{
  "headerRow": false,
  "columns": [
    [
      {
        "targetHeader": "name",
        "type": "cleartext"
      }
    ],
    [
      {
        "targetHeader": "city_sealed",
        "type": "sealed",
        "pad": {
          "type": "max",
          "length": 16
        }
      }
    ],
    [
      {
        "targetHeader": "phone_number_fingerprint",
        "type": "fingerprint"
      },
      {
        "targetHeader": "phone_number_sealed",
        "type": "sealed",
        "pad": {
          "type": "fixed",
          "length": 20
        }
      }
    ]
  ]
}
```

As a complex example, the following is an example .csv file if it didn't have the
first row with the headers.

```
Jorge,Souza,12345 Mills Rd,Anytown,SC, 703 -555 -1234,CEO, 10,
Paulo,Santos, 0 Street,Anytown,MD, 404-555-111,CIO, 9,This is a really long note that could really be a paragraph
Mateo,Jackson, 1 Two St,Anytown,NY, 304-555-1324,COO, 9, ""
Terry,Whitlock, 4 N St,Anytown,VA, 407-555-8888,EA, 7,Secret notes
Diego,Ramirez, 9 Hollows Rd,Anytown,VA, 407-555-1222,SDE I, 4,null
John,Doe, 8 Hollows Rd,Anytown,VA, 407-555-4321,SDE I, 4,Jane's younger brother
Jane,Doe, 8 Hollows Rd,Anytown,VA, 407-555-4322,SDE II, 5,John's older sister
```

The positional schema has the following form.

```
{
  "headerRow": false,
  "columns": [
    [
      {
        "targetHeader": "GivenName",
        "type": "cleartext"
      }
    ],
    [
      {
        "targetHeader": "Surname",
        "type": "cleartext"
      }
    ],
    [],
    [],
    [
      {
        "targetHeader": "State_Join",
        "type": "fingerprint"
      },
      {
        "targetHeader": "State",
        "type": "sealed",
        "pad": {
          "type": "none"
        }
      }
    ],
    [],
    [],
    [],
    []
  ]
}
```

The preceding schema produces the following output file with a header row containing
the specified target headers.

```
givenname,surname,state_fingerprint,state
Mateo,Jackson,01:hmac:iIRnjfNBzryusIJ1w35lgNzeY1RQ1bSfq6PDHW8Xrbk=,01:enc:ENS6QD3cMVl9vQEGfe9MNWfR0UOupchswZFr94zOMG5jY/Q8m/Y5SA89dJwKpT5rGPp8e36h6klwDoslpFzGvU0=
Jorge,Souza,01:hmac:3BxJdXiFFyZ8HBbYNqqEhBVqhNOd7s2ZiKUe7QiTyo8=,01:enc:LKo0zirq2++XEIIIMNRjAsGMdyWUDwYaum0B+IFP+rUf1BNeZDJjtFe1Z+zbZfXQWwJy52Rt7HqvAb2WIK1oMmk=
Paulo,Santos,01:hmac:CHF4eIrtTNgAooU9v4h9Qjc+txBnMidQTjdjWuaDTTA=,01:enc:MyQKyWxJ9kvK1xDQQtXlUNwv3F+yrBRr0xrUY/1BGg5KFgOn9pK+MZ7g+ZNqZEPcPz4lht1u0t/wbTaqzOCLXFQ=
Jane,Doe,01:hmac:UK8s8Cn/WR2JO/To2dTxWD73aDEe2ZUXeSHy3Tv+1Mk=,01:enc:Pd8sbITBfb0/ttUB4svVsgoYkDfnDvgkvxzeci0Yxq54rLSwccy1o3/B50C3cpkkn56dovCwzgmmPNwrmCmYtb4=
Terry,Whitlock01:hmac:UK8s8Cn/WR2JO/To2dTxWD73aDEe2ZUXeSHy3Tv+1Mk=,01:enc:Qmtzu3B3GAXKh2KkRYTiEAaMopYedsSdF2e/ADUiBQ9kv2CxKPzWyYTD3ztmKPMka19dHre5VhUHNpO3O+j1AQ8=
Diego,Ramirez,01:hmac:UK8s8Cn/WR2JO/To2dTxWD73aDEe2ZUXeSHy3Tv+1Mk=,01:enc:ysdg+GHKdeZrS/geBIooOEPLHG68MsWpx1dh3xjb+fG5rmFmqUcJLNuuYBHhHAlxchM2WVeV1fmHkBX3mvZNvkc=
John,Doe,01:hmac:UK8s8Cn/WR2JO/To2dTxWD73aDEe2ZUXeSHy3Tv+1Mk=,01:enc:9uX0wZuO7kAPAx+Hf6uvQownkWqFSKtWS7gQIJSe5aXFquKWCK6yZN0X5Ea2N3bn03Uj1kh0agDWoiP9FRZGJA4=
```
