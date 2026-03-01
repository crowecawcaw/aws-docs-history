# String functions

###### Important

Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can continue to use the feature as usual. [Learn more](https://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/ "https://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/")

Amazon S3 Select supports the following string functions.

###### Topics

- [CHAR_LENGTH, CHARACTER_LENGTH](#s3-select-sql-reference-char-length "#s3-select-sql-reference-char-length")
- [LOWER](#s3-select-sql-reference-lower "#s3-select-sql-reference-lower")
- [SUBSTRING](#s3-select-sql-reference-substring "#s3-select-sql-reference-substring")
- [TRIM](#s3-select-sql-reference-trim "#s3-select-sql-reference-trim")
- [UPPER](#s3-select-sql-reference-upper "#s3-select-sql-reference-upper")

## CHAR_LENGTH, CHARACTER_LENGTH

`CHAR_LENGTH` (or `CHARACTER_LENGTH`) counts the number of
characters in the specified string.

###### Note

`CHAR_LENGTH` and `CHARACTER_LENGTH` are
synonyms.

### Syntax

```
CHAR_LENGTH ( `string` )
```

### Parameters

_`string`_

The target string that the function operates on.

### Examples

```
CHAR_LENGTH('')          -- 0
CHAR_LENGTH('abcdefg')   -- 7
```

## LOWER

Given a string, `LOWER` converts all uppercase characters to lowercase
characters. Any non-uppercased characters remain unchanged.

### Syntax

```
LOWER ( `string` )
```

### Parameters

_`string`_

The target string that the function operates on.

### Examples

```
LOWER('AbCdEfG!@#$') -- 'abcdefg!@#$'
```

## SUBSTRING

Given a string, a start index, and optionally a length, `SUBSTRING` returns the
substring from the start index up to the end of the string, or up to the length
provided.

###### Note

The first character of the input string has an index position of 1.

- If `start` is < 1, with no length specified, then the index position is
  set to 1.
- If `start` is < 1, with a length specified, then the index position is
  set to `start + length -1`.
- If `start + length -1` < 0, then an empty string is returned.
- If `start + length -1` > = 0, then the substring starting at index position
  1 with the length `start + length - 1` is returned.

### Syntax

```
SUBSTRING( `string` FROM `start` [ FOR `length` ] )
```

### Parameters

_`string`_

The target string that the function operates on.

_`start`_

The start position of the string.

_`length`_

The length of the substring to return. If not present, proceed
to the end of the string.

### Examples

```
SUBSTRING("123456789", 0)      -- "123456789"
SUBSTRING("123456789", 1)      -- "123456789"
SUBSTRING("123456789", 2)      -- "23456789"
SUBSTRING("123456789", -4)     -- "123456789"
SUBSTRING("123456789", 0, 999) -- "123456789"
SUBSTRING("123456789", 1, 5)   -- "12345"
```

## TRIM

Trims leading or trailing characters from a string. The default character to remove is a
space (`' '`).

### Syntax

```
TRIM ( [[LEADING | TRAILING | BOTH `remove_chars`] FROM] `string` )
```

### Parameters

_`string`_

The target string that the function operates on.

`LEADING` | `TRAILING` | `BOTH`

This parameter indicates whether to trim leading or trailing characters, or both
leading and trailing characters.

_`remove_chars`_

The set of characters to remove. `remove_chars`
can be a string with a length > 1. This function returns the
string with any character from
`remove_chars`
found at the beginning or end of the string that was
removed.

### Examples

```
TRIM('       foobar         ')               -- 'foobar'
TRIM('      \tfoobar\t         ')            -- '\tfoobar\t'
TRIM(LEADING FROM '       foobar         ')  -- 'foobar         '
TRIM(TRAILING FROM '       foobar         ') -- '       foobar'
TRIM(BOTH FROM '       foobar         ')     -- 'foobar'
TRIM(BOTH '12' FROM '1112211foobar22211122') -- 'foobar'
```

## UPPER

Given a string, `UPPER` converts all lowercase characters to uppercase
characters. Any non-lowercased characters remain unchanged.

### Syntax

```
UPPER ( `string` )
```

### Parameters

_`string`_

The target string that the function operates on.

### Examples

```
UPPER('AbCdEfG!@#$') -- 'ABCDEFG!@#$'
```
