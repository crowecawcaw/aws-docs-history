# Connect to Amazon Keyspaces using AWS CloudShell from the console

AWS CloudShell provides a streamlined way to connect to Amazon Keyspaces directly from the console. The AWS CloudShell integration
automatically initializes the `cqlsh-expansion` for you and establishes a connection to a specific keyspace.

## Getting started with AWS CloudShell integration

1. **Access the AWS CloudShell integration** – From the Amazon Keyspaces console,
   navigate to the keyspace you want to connect to and choose the **Connect to Keyspaces**
   AWS CloudShell button.
2. **Pre-filled setup command** – When you choose the AWS CloudShell button,
   the system provides a pre-filled command that includes the necessary initialization and connection parameters:

```
cqlsh-expansion.init ; cqlsh-expansion cassandra.`region`.amazonaws.com 9142 --ssl -`my_keyspace`
```

3. **Click **Run\*\*\*\*
4. **Wait for Amazon Keyspaces to establish the connection** – Allow time for the setup process to complete and the connection to your selected keyspace to be established.
5. **Execute commands** – When connected, you can write and execute CQL commands directly against the selected keyspace.

## Available CQLSH commands

The AWS CloudShell integration provides access to standard CQLSH functionality, including support for commands
beyond basic CQL.

- **Describe** – List and view detailed descriptions of keyspaces and tables.
- **Copy** – Export query output to a file for later processing.
- **Source** – Execute CQL statements from a file.
- **Command history navigation** – Scroll through previous commands using keyboard shortcuts.
- **Query execution** – Run queries directly from the keyboard interface.
- **Output copying** – Copy results as simple text for use in other applications.

## Feature considerations

When using the AWS CloudShell integration, consider the following trade-offs.

**The following features are not supported:**

- CQL syntax suggestions and auto-complete functionality.
- Editor tools such as show autocomplete, show tooltip, find, find and replace, redo, toggle block comments, toggle code folding, toggle line comment, and undo.

**Modified functionality:**

- **CSV downloads** – To download results as CSV format, specify the `>` operator to pipe command output:

```
SELECT * FROM my_table > file_name.csv
```

- **JSON viewing** - You can view items in JSON format without
  requiring data conversion.
- **Terminal-style interface** - The experience operates as a
  terminal interface rather than a full-featured code editor.

The AWS CloudShell integration simplifies the connection process while providing
essential CQL functionality for managing your Amazon Keyspaces data directly from the
AWS Management Console.
