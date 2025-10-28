# Select Quoting Rules

Attribute values must be quoted with a single or double quote. If a quote appears within the attribute value, it must be escaped with the same quote symbol. These following two expressions are equivalent:

```
select * from mydomain where attr1 = 'He said, "That''s the ticket!"'
select * from mydomain where attr1 = "He said, ""That's the ticket!"""
```

Attribute and domain names may appear without quotes if they contain only letters, numbers, underscores (\_), or dollar symbols ($) and do not start with a number. You must quote all other attribute and domain names with the backtick (`).

```
select * from mydomain where `timestamp-1` > '1194393600'
```

You must escape the backtick when it appears in the attribute or domain name by replacing it with two backticks. For example, we can retrieve any items that have the attribute abc`123 set to the value 1 with this select expression:

```
select * from mydomain where `abc``123` = '1'
```

The following is the list of reserved keywords that are valid identifiers that must be backtick quoted if used as an attribute or domain name in the Select syntax.

- or
- and
- not
- from
- where
- select
- like
- null
- is
- order
- by
- asc
- desc
- in
- between
- intersection
- limit
- every
