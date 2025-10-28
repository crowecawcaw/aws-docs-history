AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Customize your project

settings

These sections describe the kinds of project settings that you can change on the
**Preferences** tab's **Project Settings**
pane.

- [EC2 instance](#settings-project-change-ec2-instance "#settings-project-change-ec2-instance")
- [Code editor (Ace)](#settings-project-change-code-editor-ace "#settings-project-change-code-editor-ace")
- [Find in files](#settings-project-change-find-in-files "#settings-project-change-find-in-files")
- [Hints and warnings](#settings-project-change-hints-and-warnings "#settings-project-change-hints-and-warnings")
- [JavaScript
  support](#settings-project-change-javascript-support "#settings-project-change-javascript-support")
- [Build](#settings-project-change-build "#settings-project-change-build")
- [Run and debug](#settings-project-change-run-and-debug "#settings-project-change-run-and-debug")
- [Run configurations](#settings-project-change-run-configurations "#settings-project-change-run-configurations")
- [Code formatters](#settings-project-change-code-formatters "#settings-project-change-code-formatters")
- [TypeScript support](#settings-project-change-typescript-support "#settings-project-change-typescript-support")
- [PHP support](#settings-project-change-php-support "#settings-project-change-php-support")
- [Python
  support](#settings-project-change-python-support "#settings-project-change-python-support")
- [Go support](#settings-project-change-go-support "#settings-project-change-go-support")

## EC2 instance

\***\*Stop my environment\*\***

Choose when to automatically stop your environment's Amazon EC2 instance (if
used) after you close all web browser instances that are connected to the IDE
for that environment. You can choose a range of time periods from a week to 30
minutes. You can also choose never to automatically stop the Amazon EC2 instance
after exiting the AWS Cloud9 IDE.

If you want to stop the instance even sooner than 30 minutes after finishing
with the IDE, you can [stop it
manually using the console interface](stopping-instance-manually.md "stopping-instance-manually.md").

## Code editor (Ace)

\***\*Soft tabs\*\***

If selected, inserts the specified number of spaces instead of a tab
character each time you press `Tab`.

\***\*Autodetect tab size on load\*\***

If selected, AWS Cloud9 attempts to guess the tab size.

\***\*New file line endings\*\***

The type of line endings to use for new files.

Valid options include the following:

- **Windows (CRLF)** to end lines with a carriage return
  and then a line feed.
- **Unix (LF)** to end lines with just a line feed.

\***\*On save, strip whitespace\*\***

If selected, AWS Cloud9 attempts to remove what it considers to be unnecessary
spaces and tabs from a file each time that file is saved.

## Find in files

\***\*Ignore these Files\*\***

When finding in files, the types of files that AWS Cloud9 ignores.

\***\*Maximum number of files to search (in 1000)\*\***

When finding in files, the maximum number of files, in multiples of 1,000,
that AWS Cloud9 finds in the current scope.

## Hints and warnings

\***\*Warning Level\*\***

The minimum level of messages to enable.

Valid values include the following:

- **Info** to enable informational, warning, and error
  messages.
- **Warning** to enable just warning and error
  messages.
- **Error** to enable just error messages.

\***\*Mark Missing Optional Semicolons\*\***

If enabled, AWS Cloud9 flags in a file each time it notices a semicolon that
could be used in code, but that isn't used.

\***\*Mark Undeclared Variables\*\***

If enabled, AWS Cloud9 flags in a file each time it notices an undeclared
variable in code.

\***\*Mark Unused Function Arguments\*\***

If enabled, AWS Cloud9 flags in a file each time it notices an unused argument in
a function.

\***\*Ignore Messages Matching Regex\*\***

AWS Cloud9 will not display any messages matching the specified regular
expression. For more information, see [Writing a regular expression pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions#Writing_a_regular_expression_pattern "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions#Writing_a_regular_expression_pattern") in the
_JavaScript Regular Expressions_ topic
on the Mozilla Developer Network.

## JavaScript support

\***\*Customize JavaScript warnings with
.eslintrc\*\***

If enabled, AWS Cloud9 uses an `.eslintrc` file to determine
which JavaScript warnings to enable or disable. For more
information, see [Configuration File Formats](http://eslint.org/docs/user-guide/configuring#configuration-file-formats "http://eslint.org/docs/user-guide/configuring#configuration-file-formats") on the ESLint
website.

\***\*JavaScript library code completion\*\***

The JavaScript libraries that AWS Cloud9 uses to attempt to
suggest or do automatic code completion.

\***\*Format Code on Save\*\***

If enabled, AWS Cloud9 attempts to format the code in a JavaScript
file every time that file is saved.

\***\*Use builtin JSBeautify as code formatter\*\***

If enabled, AWS Cloud9 uses its internal implementation of
JSBeautify to attempt to increase the readability of code in
files.

\***\*Custom code formatter\*\***

The command for AWS Cloud9 to attempt to run when formatting code in a
JavaScript file.

## Build

\***\*Builder path in environment\*\***

The path to any custom build configurations.

## Run and debug

\***\*Runner path in environment\*\***

The path to any custom run configurations.

\***\*Preview URL\*\***

The URL to use to preview applications for the environment.

## Run configurations

The custom run configurations for this environment.

\***\*Remove selected configs\*\***

Deletes the selected run configurations.

\***\*Add new config\*\***

Creates a new run configuration.

\***\*Set as default\*\***

Sets the selected run configuration as the default run configuration.

## Code formatters

\***\*JSBeautify settings\*\***

Settings for increasing the readability of code in files.

\***\*Format Code on Save\*\***

If enabled, AWS Cloud9 attempts to apply JSBeautify
settings whenever code files are saved.

\***\*Use JSBeautify for
JavaScript\*\***

If enabled, AWS Cloud9 attempts to apply JSBeautify
settings whenever JavaScript files are saved.

\***\*Preserve empty lines\*\***

If enabled, AWS Cloud9 doesn't remove empty lines in code files.

\***\*Keep array indentation\*\***

If enabled, AWS Cloud9 preserves the indentation of element declarations
in arrays in code files.

\***\*JSLint strict whitespace\*\***

If enabled, AWS Cloud9 attempts to apply JSLint whitespace rules in code
files. For more information, see "Whitespace" in [JSLint Help](http://jslint.com/help.html "http://jslint.com/help.html").

\***\*Braces\*\***

Specifies the alignment of braces in code.

Valid values include the following:

- **Braces with control statement** to move each
  beginning and end brace to align with its related control
  statement, as needed.

For example, this code is formatted as so:

```
for (var i = 0; i < 10; i++) { if (i == 5) { console.log("Halfway done.") }}
```

Turns into this code when the file is saved:

```
for (var i = 0; i < 10; i++) {
   if (i == 5) {
      console.log("Halfway done.")
   }
}
```

- **Braces on own line** to move each brace to
  its own line, as needed.

For example, this code is formatted as so:

```
for (var i = 0; i < 10; i++) { if (i == 5) { console.log("Halfway done.") }}
```

Turns into this code when the file is saved:

```
for (var i = 0; i < 10; i++) {if (i == 5)
  {
     console.log("Halfway done.")
  }
  }
```

- **End braces on own line** to move each end
  brace to its own line, as needed.

For example, this code is formatted as so:

```
for (var i = 0; i < 10; i++) {
  if (i == 5) { console.log("Halfway done.") }
}
```

Turns into this code when the file is saved:

```
for (var i = 0; i < 10; i++) {
   if (i == 5) {
      console.log("Halfway done.")
   }
}
```

\***\*Preserve inline blocks\*\***

If enabled, AWS Cloud9 doesn't attempt to move the beginning and ending
braces for inline blocks to separate lines, if those braces are on the
same line.

\***\*Space before conditionals\*\***

If enabled, AWS Cloud9 adds a space before each conditional declaration,
as needed.

\***\*Unescape strings\*\***

If enabled, AWS Cloud9 converts escaped strings to their unescaped
equivalents. For example, converts `\n` to a newline
character and converts `\r` to a carriage return
character.

\***\*Indent inner HTML\*\***

If enabled, AWS Cloud9 indents `<head>` and
`<body>` sections in HTML code.

## TypeScript

support

\***\*Format Code on Save\*\***

If enabled, AWS Cloud9 attempts to format TypeScript code whenever
TypeScript files are saved.

\***\*Custom code formatter\*\***

The path to any custom code formatting configuration for
TypeScript code.

## PHP support

\***\*Enable PHP code completion\*\***

If enabled, AWS Cloud9 attempts to complete PHP code.

\***\*PHP completion include paths\*\***

Locations that AWS Cloud9 uses to attempt to help complete PHP
code. For example, if you have custom PHP files that you want
AWS Cloud9 to use for completion, and those files are somewhere in the
`~/environment` directory, add `~/environment`
to this path.

\***\*Format Code on Save\*\***

If enabled, AWS Cloud9 attempts to format PHP code whenever
PHP files are saved.

\***\*Custom code formatter\*\***

The path to any custom code formatting configuration for PHP
code.

## Python

support

\***\*Enable Python code completion\*\***

If enabled, AWS Cloud9 attempts to complete Python code. To set
the paths for AWS Cloud9 to use to complete Python code, use the
**PYTHONPATH** setting.

\***\*Python version\*\***

Specifies the version of Python to use.

\***\*Pylint command line options\*\***

Options for AWS Cloud9 to use for Pylint with
Python code. For more information, see the [Pylint User
Manual](https://pylint.readthedocs.io/en/latest/ "https://pylint.readthedocs.io/en/latest/") on the Pylint website.

\***\*PYTHONPATH\*\***

The paths to Python libraries and packages for AWS Cloud9 to use.
For example, if you have custom Python libraries and packages in
the `~/environment` directory, add
`~/environment` to this path.

\***\*Format Code on Save\*\***

If enabled, AWS Cloud9 attempts to format Python code whenever
Python files are saved.

\***\*Custom code formatter\*\***

The path to any custom code formatting configuration for
Python code.

## Go support

\***\*Enable Go code completion\*\***

If enabled, AWS Cloud9 attempts to complete Go code.

\***\*Format Code on Save\*\***

If enabled, AWS Cloud9 attempts to format Go code whenever
Go files are saved.

\***\*Custom code formatter\*\***

The path to any custom code formatting configuration for Go
code.
