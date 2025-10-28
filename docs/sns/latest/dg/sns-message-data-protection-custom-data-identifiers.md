# Using custom data

identifiers in Amazon SNS

Custom data identifiers (CDIs) let you define your own custom regular expressions that can
be used in your data protection policy. Using custom data identifiers, you can target
business-specific personally identifiable information (PII) use cases that [managed data identifiers](sns-message-data-protection-managed-data-identifiers.md "sns-message-data-protection-managed-data-identifiers.md")
can't provide. For example, you can use a custom data identifier to look for company-specific
employee IDs. Custom data identifiers can be used in conjunction with managed data
identifiers.

## What are custom data identifiers?

Custom data identifiers (CDIs) let you define your own custom regular expressions that can
be used in your data protection policy. Using custom data identifiers, you can target
business-specific personally identifiable information (PII) use cases that [managed data
identifiers](sns-message-data-protection-managed-data-identifiers.md "sns-message-data-protection-managed-data-identifiers.md") can't provide. For example, you can use a custom data identifier to look
for company-specific employee IDs. Custom data identifiers can be used in conjunction with
managed data identifiers.

## Using custom data identifiers in your data

protection policy

The following data protection policy instructs the Amazon SNS topic to detect payloads that
carry company-specific employee IDs, then mask these IDs using the hash symbol (#).

1. Create a `Configuration` block within your data protection policy.
2. Enter a `Name` for your custom data identifier. For example,
   `EmployeeId`.
3. Enter a `Regex` for your custom data identifier. For example,
   `EID-\d{9}-US`.
4. Refer to the following custom data identifier in a policy statement.

```
 {
  "Name": "__example_data_protection_policy",
  "Description": "Example data protection policy",
  "Version": "2021-06-01",
  "Configuration": {
    `"CustomDataIdentifier": [
 {"Name": "EmployeeId", "Regex": "EID-\d{9}-US"`}
    ]
  },
  "Statement": [
    {
      "DataDirection": "Inbound",
      "Principal": ["*"],
      `"DataIdentifier": [
 "EmployeeId"`
      ],
      "Operation": {
        "Deidentify": {
          `"MaskConfig"`: {
            `"MaskWithCharacter"`: `"#"`
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

## Custom data identifier

constraints

Amazon SNS custom data identifiers have the following limitations:

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
- Custom data identifiers must be specified in every data protection policy for each
  Amazon SNS topic.
