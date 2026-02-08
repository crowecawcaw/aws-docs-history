# Using data masking to hide sensitive information

To conceal sensitive data stored in one or more columns of the tables being migrated, you can leverage Data Masking transformation rule actions.
Starting from version 3.5.4, AWS DMS allows the use of data masking transformation rule actions in table mapping, enabling you to alter the contents of
one or more columns during the migration process. AWS DMS loads the modified data into the target tables.

AWS Database Migration Service provides three options for data masking transformation rule actions:

- Data Masking: Digits Mask
- Data Masking: Digits Randomize
- Data Masking: Hashing Mask
  These data masking transformation rule actions can be configured in the table mapping of your replication task, similar to other transformation rules.
  The rule target should be set to the column level.

## Masking numbers in column data with a masking character

The "Data Masking: Digits Mask" transformation rule action allows you to mask numerical data in one or more columns by replacing digits with a single
ASCII printable character that you specify (excluding empty or whitespace characters).

Here's an example that masks all digits in the `cust_passport_no` column of the `customer_master` table with the masking character `'#'`
and loads the masked data into the target table:

```

                {
    "rules": [
        {
            "rule-type": "selection",
            "rule-id": "1",
            "rule-name": "1",
            "object-locator": {
                "schema-name": "cust_schema",
                "table-name": "%"
            },
            "rule-action": "include"
        },
        {
            "rule-type": "transformation",
            "rule-id": "2",
            "rule-name": "2",
            "rule-target": "column",
            "object-locator": {
                "schema-name": "cust_schema",
                "table-name": "customer_master",
                "column-name": "cust_passport_no"
            },
            "rule-action": "data-masking-digits-mask",
            "value": "#"
        }
    ]
}

```

For example, if the column `cust_passport_no` in the source table contains the record "C6BGJ566669K", the AWS DMS task will write this data to
the target table as `"C#BGJ######K"`.

## Replacing numbers in the column with random numbers

The transformation rule "Data Masking: Digits Randomize" allows you to replace each numerical digit in one or more columns with a random number.
In the following example, AWS DMS replaces every digit in the `cust_passport_no` column of the source table `customer_master` with a
random number and writes the modified data to the target table:

```

            {
    "rules": [
        {
            "rule-type": "selection",
            "rule-id": "1",
            "rule-name": "1",
            "object-locator": {
                "schema-name": "cust_schema",
                "table-name": "%"
            },
            "rule-action": "include"
        },
        {
            "rule-type": "transformation",
            "rule-id": "2",
            "rule-name": "2",
            "rule-target": "column",
            "object-locator": {
                "schema-name": "cust_schema",
                "table-name": "customer_master",
                "column-name": "cust_passport_no"
            },
            "rule-action": "data-masking-digits-randomize"
        }
    ]
}

```

For example, the AWS DMS task will transform the value `"C6BGJ566669K"` in the `cust_passport_no` column of the source table to `"C1BGJ842170K"` and write it to the target database.

## Replacing column data with hash value

The transformation rule "Data Masking: Hashing Mask" allows you to replace the column data with a hash generated using the `SHA256` algorithm.
The length of the hash will always be 64 characters, hence the target table column length should be 64 characters at minimum. Alternatively, you can add a
`change-data-type` transformation rule action to the column to increase the width of the column in the target table.

The following example generates a 64-character long hash value for the data in the `cust_passport_no` column of the source table
`customer_master` and loads the transformed data to the target table after increasing the column length:

```

{
"rules": [
{
"rule-type": "selection",
"rule-id": "1",
"rule-name": "1",
"object-locator": {
"schema-name": "cust_schema",
"table-name": "%"
},
"rule-action": "include"
},
{
"rule-type": "transformation",
"rule-id": "2",
"rule-name": "2",
"rule-target": "column",
"object-locator": {
"schema-name": "cust_schema",
"table-name": "customer_master",
"column-name": "cust_passport_no"
},
"rule-action": "change-data-type",
"data-type": {
"type": "string",
"length": "100",
"scale": ""
}
},
{
"rule-type": "transformation",
"rule-id": "3",
"rule-name": "3",
"rule-target": "column",
"object-locator": {
"schema-name": "cust_schema",
"table-name": "customer_master",
"column-name": "cust_passport_no"
},
"rule-action": "data-masking-hash-mask"
}
]
}

```

For example, if the column `cust_passport_no` of the source table contains value `“C6BGJ566669K”`, AWS DMS task will write a hash
`“7CB06784764C9030CCC41E25C15339FEB293FFE9B329A72B5FED564E99900C75”` to the target table.

## Limitations

- Each Data Masking transformation rule option is supported for specific AWS DMS data types only:

      + Data Masking: Digits Mask is supported for columns of data types: `WSTRING` and `STRING`.
      + Data Masking: Digits Randomize is supported for columns of data types: `WSTRING, STRING; NUMERIC, INT1, INT2, INT4, and INT8`
       with unsigned counterparts.
      + Data Masking: Hashing Mask is supported for columns of data types: `WSTRING` and `STRING`.

  To learn more about the mapping of AWS DMS data types to your source engine's data types, refer to the data type mapping of your source engine with AWS DMS data types.
  See source data types for [Source data types for Oracle](CHAP_Source.md#CHAP_Source.Oracle.DataTypes "CHAP_Source.md#CHAP_Source.Oracle.DataTypes"), [Source data types for SQL
  Server](CHAP_Source.md#CHAP_Source.SQLServer.DataTypes "CHAP_Source.md#CHAP_Source.SQLServer.DataTypes"), [Source data types for
  PostgreSQL](CHAP_Source.md#CHAP_Source-PostgreSQL-DataTypes "CHAP_Source.md#CHAP_Source-PostgreSQL-DataTypes"), and [Source data types for MySQL](CHAP_Source.md#CHAP_Source.MySQL.DataTypes "CHAP_Source.md#CHAP_Source.MySQL.DataTypes").

- Using a Data Masking rule action for a column with an incompatible data type will cause an error in the DMS task. Refer to DataMaskingErrorPolicy in DMS task settings to specify the error handling behavior.
  For more information about `DataMaskingErrorPolicy`, see [Error
  handling task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md").
- You may add a change-data-type transformation rule action to change the data type of the column to a compatible type if your source column type is not supported for the masking option you plan to use.
  The `rule-id` of the `change-data-type` transformation should be a smaller number than the rule-id of the masking transformation so
  that the data type change happens before masking.
- Use Data Masking: Hashing Mask action for masking Primary Key/ Unique Key/ Foreign Key columns, as the generated hash value will be unique and
  consistent. Other two masking options cannot guarantee uniqueness.
- While Data Masking: Digits Mask and Data Masking: Digits Randomize affect only the digits in the column data and does not affect the length of
  data, Data Masking: Hashing Mask modifies the entire column, length of data changes to 64 characters. Hence, the target table to be created accordingly or
  a change-data-type transformation rule should be added for the column which is being masked.
- Columns with Data Masking transformation rule action specified are excluded from data validation in AWS DMS. If the Primary Key/ Unique Key
  columns are masked, data validation will not be run for this table; validation status of such table will be equal to `No Primary key`.
