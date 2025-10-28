# Custom data identifiers

###### Topics

- [What are custom data identifiers?](#what-are-custom-data-identifiers "#what-are-custom-data-identifiers")
- [Custom data identifier
  constraints](#custom-data-identifiers-constraints "#custom-data-identifiers-constraints")
- [Using custom data identifiers in the console](#using-custom-data-identifiers-console "#using-custom-data-identifiers-console")
- [Using custom data identifiers in your data
  protection policy](#using-custom-data-identifiers "#using-custom-data-identifiers")

## What are custom data identifiers?

Custom data identifiers (CDIs) let you define your own custom regular expressions that can
be used in your data protection policy. Using custom data identifiers, you can target
business-specific personally identifiable information (PII) use cases that [managed data
identifiers](CWL-managed-data-identifiers.md "CWL-managed-data-identifiers.md") can't provide. For example, you can use a custom data identifier to look
for company-specific employee IDs. Custom data identifiers can be used in conjunction with
managed data identifiers.

## Custom data identifier

constraints

CloudWatch Logs custom data identifiers have the following limitations:

- A maximum of 10 custom data identifiers are supported for each data protection
  policy.
- Custom data identifier names have a maximum length of 128 characters. The following
  characters are supported:
  - Alphanumeric: (a-zA-Z0-9)
  - Symbols: ( '\_' | '-' )

- RegEx has a maximum length of 200 characters. The following characters
  are supported:
  - Alphanumeric: (a-zA-Z0-9)
  - Symbols: ( '\_' | '#' | '=' | '@' |'/' | ';' | ',' | '-' | ' ' )
  - RegEx reserved characters: ( '^' | '$' | '?' | '[' | ']' | '{' |
    '}' | '|' | '\\' | '\*' | '+' | '.' )

- Custom data identifiers cannot share the same name as a managed data
  identifier.
- Custom data identifiers can be specified within an account-level data protection policy or in
  log group-level data protection policies. Similar to managed data identifiers, custom data identifiers
  defined within an account-level policy work in combination with custom data identifiers defined in a log group-level policy.

## Using custom data identifiers in the console

When you use the CloudWatch console to create or edit a data protection policy, to specify a custom data
identifier you just enter a name and regular expression for the data identifier. For example,
you might enter `Employee_ID` for the name and `EmployeeID-\d{9}`
as the regular expression. This regular expression will detect and mask log events with nine numbers
after `EmployeeID-`. For example, `EmployeeID-123456789`

## Using custom data identifiers in your data

protection policy

If you are using the AWS CLI or AWS API to specify a custom data identifier, you need to include
the data identifier name and regular expression in the JSON policy used to define the data
protection policy. The following data protection policy detects and masks log events that
carry company-specific employee IDs.

1. Create a `Configuration` block within your data protection policy.
2. Enter a `Name` for your custom data identifier. For example,
   `EmployeeId`.
3. Enter a `Regex` for your custom data identifier. For example,
   `EmployeeID-\d{9}`. This regular expression will match log events
   containing `EmployeeID-` that have nine digits after `EmployeeID-`.
   For example,
   `EmployeeID-123456789`
4. Refer to the following custom data identifier in a policy statement.

```
{
    "Name": "example_data_protection_policy",
    "Description": "Example data protection policy with custom data identifiers",
    "Version": "2021-06-01",
    "Configuration": {
      "CustomDataIdentifier": [
        {"Name": "EmployeeId", "Regex": "EmployeeId-\\d{9}"}
      ]
    },
    "Statement": [
        {
            "Sid": "audit-policy",
            "DataIdentifier": [
                "EmployeeId"
            ],
            "Operation": {
                "Audit": {
                    "FindingsDestination": {
                        "S3": {
                            "Bucket": "`EXISTING_BUCKET`"
                        }
                    }
                }
            }
        },
        {
            "Sid": "redact-policy",
            "DataIdentifier": [
            "EmployeeId"
            ],
            "Operation": {
                "Deidentify": {
                    "MaskConfig": {
                    }
                }
            }
        }
    ]
}
```

5. (Optional) Continue to add additional **custom data
   identifiers** to the `Configuration` block as needed. Data
   protection policies currently support a maximum of 10 custom data identifiers.
