# Using Markdown in the Console

Some services in the AWS Management Console, such as Amazon CloudWatch, support the use of [Markdown](https://en.wikipedia.org/wiki/Markdown "https://en.wikipedia.org/wiki/Markdown") in certain fields. This
topic explains the types of Markdown formatting supported in the console.

###### Contents

- [Paragraphs, Line Spacing, and Horizontal
  Lines](#aws-markdown-paragraphs "#aws-markdown-paragraphs")
- [Headings](#aws-markdown-headings "#aws-markdown-headings")
- [Text Formatting](#aws-markdown-formatting "#aws-markdown-formatting")
- [Links](#aws-markdown-links "#aws-markdown-links")
- [Lists](#aws-markdown-lists "#aws-markdown-lists")
- [Tables and Buttons (CloudWatch Dashboards)](#aws-markdown-tables "#aws-markdown-tables")

## Paragraphs, Line Spacing, and Horizontal

Lines

Paragraphs are separated by a blank line. To make sure that the blank line between the
paragraphs renders when it is converted to HTML, add a new line with a non-break space
(`&nbsp;`) and then a blank line. Repeat this pair of lines to insert
multiple blank lines one after the other, as in the following example:

```
&nbsp;

&nbsp;

```

To create a horizontal rule that separates the paragraphs, add a new line with three
hyphens in a row: `---`

```
Previous paragraph.
---
Next paragraph.
```

To create a text block with monospace type, add a line with three backticks
(**`**). Enter the text to show in monospace type. Then, add another
new line with three backticks. The following example shows text that will be formatted
to monospace type when displayed:

```

```

This appears in a text box with a background shading.
The text is in monospace.

```

```

## Headings

To create headings, use the pound sign (**#**). A single pound sign and a
space indicate a top-level heading. Two pound signs create a second-level heading, and
three pound signs create a third-level heading. The following examples show a top-level,
second-level, and third-level heading:

```
 # Top-level heading
```

```
 ## Second-level heading
```

```
 ### Third-level heading
```

## Text Formatting

To format text as italic, surround it with a single underscore ( **\_** )
or asterisk (**\***) on each side.

```
*This text appears in italics.*
```

To format text as bold, surround it with double underscores or double asterisks on
each side.

```
**This text appears in bold.**
```

To format text as strikethrough, surround it with two tildes (**~**) on
each side.

```
~~This text appears in strikethrough.~~
```

## Links

To add a text hyperlink, enter the link text surrounded by square brackets
(**[**
**]**), followed by the full URL in parentheses (**(**
**)**), as in the following example:

```
Choose [`link_text`](http://my.example.com).
```

## Lists

To format lines as part of a bulleted list, add them on separate lines that start with
with a single asterisk (**\***) and then a space, as in the following
example:

```
Here is a bulleted list:
* Ant
* Bug
* Caterpillar
```

To format lines as part of a numbered list, add them on separate lines that start with
with a number, a period (**.**), and a space, as in the following
example:

```
Here is a numbered list:
1. Do the first step
2. Do the next step
3. Do the final step
```

## Tables and Buttons (CloudWatch Dashboards)

CloudWatch dashboards text widgets support Markdown tables and buttons.

To create a table, separate columns using vertical bars (**|**) and rows
using new lines. To make the first row a header row, insert a line between the header
row and the first row of values. Then, add at least three hyphens (**-**)
for each column in the table. Separate columns using vertical bars. The following
example shows Markdown for a table with two columns, a header row, and two rows of
data:

```
Table | Header
----|-----
Amazon Web Services | AWS
1 | 2
```

The Markdown text in the previous example creates the following table:

| Table               | Header |
| ------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon Web Services | AWS    |
| 1                   | 2      | In a CloudWatch dashboard text widget, you can also format a hyperlink to appear as a button. To create a button, use `[button:`Button text`]`, followed by the full URL in parentheses(**(** **)**), as in the following example: `[button:Go to AWS](http://my.example.com) [button:primary:This button stands out even more](http://my.example.com)` |
