**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using text transformations in AWS WAF

This section explains how to provide transformations for AWS WAF to apply before inspecting the request.

In statements that look for patterns or set constraints, you can provide
transformations for AWS WAF to apply before inspecting the request. A
transformation reformats a web request to eliminate some of the unusual
formatting that attackers use in an effort to bypass AWS WAF.

When you use this with the JSON body request component selection, AWS WAF
applies your transformations after parsing and extracting the elements to
inspect from the JSON. For more information, see [JSON body](waf-rule-statement-fields-list.md#waf-rule-statement-request-component-json-body "waf-rule-statement-fields-list.md#waf-rule-statement-request-component-json-body").

If you provide more than one transformation, you also set the order for AWS WAF
to apply them.

**WCUs** – Each text transformation is 10
WCUs.

The AWS WAF console and API documentation also provide guidance for these
settings in the following locations:

- **Rule builder** on the console –
  **Text transformation**. This option is available
  when you use request components.
- **API statement contents** –
  `TextTransformations`

###### Options for text transformations

Each transformation listing shows the console and API specifications followed by the description.

Base64 decode – `BASE64_DECODE`

AWS WAF decodes a Base64-encoded string.

Base64 decode extension – `BASE64_DECODE_EXT`

AWS WAF decodes a Base64-encoded string, but uses a forgiving
implementation that ignores characters that aren't valid.

Command line – `CMD_LINE`

This option mitigates situations where attackers might be
injecting an operating system command-line command and are using
unusual formatting to disguise some or all of the command.

Use this option to perform the following transformations:

- Delete the following characters: `\ " '
^`
- Delete spaces before the following characters: `/
(`
- Replace the following characters with a space: `,
;`
- Replace multiple spaces with one space
- Convert uppercase letters, `A-Z`, to lowercase,
  `a-z`

Compress whitespace – `COMPRESS_WHITE_SPACE`

AWS WAF compresses white space by replacing multiple spaces with one space and replacing the
following characters with a space character (ASCII 32):

- Formfeed (ASCII 12)
- Tab (ASCII 9)
- Newline (ASCII 10)
- Carriage return (ASCII 13)
- Vertical tab (ASCII 11)
- Non-breaking space (ASCII 160)

CSS decode – `CSS_DECODE`

AWS WAF decodes characters that were encoded using CSS 2.x escape rules
`syndata.html#characters`. This function uses up to
two bytes in the decoding process, so it can help to uncover ASCII
characters that were encoded using CSS encoding that wouldn’t
typically be encoded. It's also useful in countering evasion, which
is a combination of a backslash and non-hexadecimal characters. For
example, `ja\vascript` for
`javascript`.

Escape sequences decode – `ESCAPE_SEQ_DECODE`

AWS WAF decodes the following ANSI C escape sequences: `\a`, `\b`,
`\f`, `\n`, `\r`, `\t`, `\v`, `\\`, `\?`, `\'`, `\"`, `\xHH` (hexadecimal), `\0OOO`
(octal). Encodings that aren't valid remain in the
output.

Hex decode – `HEX_DECODE`

AWS WAF decodes a string of hexadecimal characters into a
binary.

HTML entity decode – `HTML_ENTITY_DECODE`

AWS WAF replaces characters that are represented in hexadecimal format
`&#xhhhh;` or decimal format `&#nnnn;` with the corresponding characters.

AWS WAF replaces the following HTML-encoded characters with unencoded characters. This list uses lowercase HTML encoding, but the handling is case insensitive, for example `&QuOt;` and `&quot;` are treated the same.

| HTML-encoded character                    | replaced with...                |
| ----------------------------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `&quot;`                                  | `"`                             |
| `&amp;`                                   | `&`                             |
| `&lt;`                                    | `<`                             |
| `&gt;`                                    | `>`                             |
| `&nbsp;` or `&NonBreakingSpace;`          | non-breaking space, decimal 160 |
| `&NewLine;`                               | `\n`, decimal 10                |
| `&Tab;`                                   | `\t`, decimal 9                 |
| `&lcub;` or `&lbrace;`                    | `{`                             |
| `&verbar;`, `&vert;`, or `&VerticalLine;` | `                               | `                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `&rcub;` or `&rbrace;`                    | `}`                             |
| `&excl;`                                  | `!`                             |
| `&num;`                                   | `#`                             |
| `&dollar;`                                | `$`                             |
| `&percent;` or `&percnt;`                 | `%`                             |
| `&apos;`                                  | `\`                             |
| `&lpar;`                                  | `(`                             |
| `&rpar;`                                  | `)`                             |
| `&ast;` or `&midast;`                     | `*`                             |
| `&plus;`                                  | `+`                             |
| `&comma;`                                 | `,`                             |
| `&period;`                                | `.`                             |
| `&sol;`                                   | `/`                             |
| `&colon;`                                 | `:`                             |
| `&semi;`                                  | `;`                             |
| `&equals;`                                | `=`                             |
| `&quest;`                                 | `?`                             |
| `&tilde;` or `&DiacriticalTilde;`         | `~`                             |
| `&minus;`                                 | `-`                             |
| `&lsqb;` or `&lbrack;`                    | `[`                             |
| `&bsol;`                                  | `\\`                            |
| `&rsqb;` or `&rbrack;`                    | `]`                             |
| `&hat;`                                   | `^`                             |
| `&lowbar;` or `&underbar;`                | `_`                             |
| `&grave;` or `&DiacriticalGrave;`         | ```                             |
|                                           |                                 | JS decode – `JS_DECODE` AWS WAF decodes JavaScript escape sequences. If a `\uHHHH` code is in the full-width ASCII code range of `FF01-FF5E`, then the higher byte is used to detect and adjust the lower byte. If not, only the lower byte is used and the higher byte is zeroed, causing a possible loss of information. Lowercase – `LOWERCASE` AWS WAF converts uppercase letters (A-Z) to lowercase (a-z). MD5 – `MD5` AWS WAF calculates an MD5 hash from the data in the input. The computed hash is in a raw binary form. None – `NONE` AWS WAF inspects the web request as received, without any text transformations. Normalize path – `NORMALIZE_PATH` AWS WAF normalizes the input string by removing multiple slashes, directory self-references, and directory back-references that are not at the beginning of the input. Normalize path Windows – `NORMALIZE_PATH_WIN` AWS WAF converts backslash characters to forward slashes and then processes the resulting string using the `NORMALIZE_PATH` transformation. Remove nulls – `REMOVE_NULLS` AWS WAF removes all `NULL` bytes from the input. Replace comments – `REPLACE_COMMENTS` AWS WAF replaces each occurrence of a C-style comment (/\* ... \*/) with a single space. It doesn't compress multiple consecutive occurrences. It replaces unterminated comments with a space (ASCII 0x20). It doesn't change a standalone termination of a comment (\*/). Replace nulls – `REPLACE_NULLS` AWS WAF replaces each `NULL` byte in the input with the space character (ASCII 0x20). SQL hex decode – `SQL_HEX_DECODE` AWS WAF decodes SQL hex data. For example, AWS WAF decodes (`0x414243`) to (`ABC`). URL decode – `URL_DECODE` AWS WAF decodes a URL-encoded value. URL decode Unicode – `URL_DECODE_UNI` Like `URL_DECODE`, but with support for Microsoft-specific `%u` encoding. If the code is in the full-width ASCII code range of `FF01-FF5E`, the higher byte is used to detect and adjust the lower byte. Otherwise, only the lower byte is used and the higher byte is zeroed. UTF8 to Unicode – `UTF8_TO_UNICODE` AWS WAF converts all UTF-8 character sequences to Unicode. This helps normalize input and it minimizes false-positives and false-negatives for non-English languages. |
