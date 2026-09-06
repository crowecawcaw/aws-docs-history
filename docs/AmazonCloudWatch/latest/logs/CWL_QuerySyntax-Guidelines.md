

# Fields that contain special characters
<a name="CWL_QuerySyntax-Guidelines"></a>

If a field contains non-alphanumeric characters other than the `@` symbol or the period (`.`), you must surround the field with backtick characters (```). For example, the log field `foo-bar` must be enclosed in backticks (``foo-bar``) because it contains a non-alphanumeric character, the hyphen (`-`).

For system fields that start with `@` and contain special characters in the remaining name, place the `@` symbol outside the backticks and enclose only the field name portion. For example, resource tag fields use the pattern `@aws.tag.<tagKey>`. If the tag key contains special characters such as colons, you must use the following syntax:

```
@`aws.tag.aws:cloudformation:stack-name`
```

The following example shows a filter query that uses this syntax:

```
filter @`aws.tag.aws:cloudformation:stack-name` = "my-stack"
```