# Step 4: Generate an encryption schema for a

tabular file

To encrypt data, an encryption schema describing how the data will be used is required.
This section describes how the C3R encryption client assists in generating an encryption schema for a
CSV file with a header row or a Parquet file.

You only need to do this once per file. After the schema exists, it can be re-used to
encrypt the same file (or any file with identical column names). If the column names or
desired encryption schema changes, you must update the schema file. For more information, see
[(Optional) Create a schema (advanced users)](create-schema.md "create-schema.md").

###### Important

It is paramount that all collaborating parties use the same shared secret key.
Collaborating parties should also coordinate column names to match if they will be
JOINed or otherwise compared for equality in queries. Otherwise, the SQL
queries might produce unexpected or incorrect results. However, this is not necessary if the
collaboration creator enabled the `allowJoinsOnColumnsWithDifferentNames`
encryption setting during collaboration creation. For more information about
encryption-relevant settings, see [Cryptographic computing parameters](crypto-computing-parameters.md "crypto-computing-parameters.md").

When run in schema mode, the C3R encryption client goes through the input file column by column,
prompting you if and how that column should be treated. If the file contains many columns that
aren't wanted for the encrypted output, the interactive schema generation might become tedious
because you must skip each undesired column. To avoid this, you could manually write a schema,
or create a simplified version of the input file featuring only the wanted columns. Then, the
interactive schema generator could be run on that reduced file. The C3R encryption client outputs
information about the schema file and asks you how the source columns should be included or
encrypted (if at all) in the target output.

For each source column in the input file, you are prompted for:

1. How many target columns should be generated
2. How each target column should be encrypted (if at all)
3. The name of each target column
4. How data should be padded before encryption if the column is being encrypted as a
   sealed column

###### Note

When you encrypt data for a column that has been encrypted as a sealed
column, you must determine which data needs padding. The C3R encryption client suggests a default
padding during schema generation that pads all entries in a column to the same
length.

When determining the length for `fixed`, note that padding is in bytes, not
bits.

The following is a decision table for creating the schema.

| Schema decision table                                 | Decision | Number of target columns from source column <‘name-of-column’> ?                | Target column type: [c] cleartext, [f] fingerprint,<br>or [s] sealed<br>? | Target column headername <default 'name-of-column'>           | Add suffix <suffix> to header to indicate how it was encrypted, [y] yes or [n]<br>no <default 'yes'>                                                            | <‘name-of-column_sealed’> padding type: [n] one, [f] fixed, or [m] max<br><default ’max’> |
| ----------------------------------------------------- | -------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Leave the column unencrypted.                         | 1        | **c**                                                                           | Not applicable                                                            | Not applicable                                                | Not<br>applicable                                                                                                                                               |
| Encrypt the column as a fingerprint column.           | 1        | **f**                                                                           | Choose default or enter a new header name.                                | Enter `y` to choose default (`_fingerprint`) or enter<br>`n`. | Not applicable                                                                                                                                                  |
| Encrypt the column as a sealed column.                | 1        | **s**                                                                           | Choose default or enter a new header name.                                | Enter `y` to choose default (`_sealed`) or enter<br>`n`.      | Choose padding type .<br>For more information, see [(Optional) Create a schema (advanced users)](create-schema.md "create-schema.md").                          |
| Encrypt the column as both fingerprint and<br>sealed. | 2        | Enter first target column: **f\*<br>• .<br>Enter second target column: **s\*\*. | Choose the target headers for each target column.                         | Enter `y` to choose default or enter `n.`                     | Choose padding type (for sealed columns only).<br>For more information, see [(Optional) Create a schema (advanced users)](create-schema.md "create-schema.md"). |

The following are two examples of how to create encryption schemas. The exact content of
your interaction depends on the input file and the responses that you provide.

###### Examples

- [Example: Generate an encryption schema for a
  fingerprint column and a cleartext column](#gen-encryption-schema_join "#gen-encryption-schema_join")
- [Example: Generate an encryption schema with
  sealed, fingerprint, and cleartext
  columns](#gen-encryption-schema "#gen-encryption-schema")

## Example: Generate an encryption schema for a

fingerprint column and a cleartext column

In this example, for `ads.csv`, there are only two columns:
`username` and `ad_variant`. For these columns, we want the
following:

- For the `username` column to be encrypted as a `fingerprint`
  column
- For the `ad_variant` column to be a `cleartext` column

###### To generate an encryption schema for a fingerprint column and a

cleartext column

1. (_Optional_) To ensure the c3r-cli.jar
   file and file to be encrypted are present:
   1. Navigate to the desired directory and run `ls` (if using a
      Mac or Unix/Linux) or
      `dir` if using Windows).
   2. View the list of tabular data files (for example, .csv) and choose a file to
      encrypt.

   In this example, `ads.csv` is the file that we want to
   encrypt.

2. From the CLI, run the following command to create a schema interactively.

`java -jar c3r-cli.jar schema ads.csv --interactive
 --output=ads.json`

###### Note

    * You can run `java --jar PATH/TO/c3r-cli.jar`. Or, if
     you have added `PATH/TO/c3r-cli.jar` to your CLASSPATH
     environment variable, you can also run the class name. The C3R encryption client will
     look in the CLASSPATH to find it (for example, `java
     com.amazon.psion.cli.Main`).
    * The `--interactive` flag selects the interactive mode for
     developing the schema. This walks the user through a wizard for creating the
     schema. Users with advanced skills can create their own schema JSON without using
     the wizard. For more information, see [(Optional) Create a schema (advanced users)](create-schema.md "create-schema.md").
    * The `--output` flag sets an output name. If you don't include the
     `--output` flag, the C3R encryption client tries to pick a default output
     name (such as `<input>.out.csv` or for the schema,
     `<input>.json`).

3. For `Number of target columns from source column ‘username’?`, enter
   `1` and then press **Enter**.
4. For `Target column type: [c]leartext, [f]ingerprint, or [s]ealed?`, enter
   `f` and then press **Enter**.
5. For `Target column headername <default 'username'>`, press
   **Enter**.

The default name ‘`username`’ is used. 6. For `Add suffix '_fingerprint' to header to indicate how it was encrypted,
 [y]es or [n]o <default 'yes'>`, enter `y` and then press
**Enter**.

###### Note

The interactive mode suggests suffixes to add to the encrypted column headers
(`_fingerprint` for fingerprint columns and
`_sealed` for sealed columns). The suffixes might be
helpful when you're performing tasks such as uploading data to AWS services or
creating AWS Clean Rooms collaborations. These suffixes can help indicate what can be done
with the encrypted data in each column. For example, things will not work if you
encrypt a column as a sealed column (`_sealed`) and try to
JOIN on it or try the reverse. 7. For `Number of target columns from source column ‘ad_variant’?`, enter
`1` and then press **Enter**. 8. For `Target column type: [c]leartext, [f]ingerprint, or [s]ealed?`, enter
`c` and then press **Enter**. 9. For `Target column headername <default 'username'>`, press
**Enter**.

The default name ‘`ad_variant`’ is used.

The schema is written to a new file called `ads.json`.

###### Note

You can view the schema by opening it in any text editor, such as
Notepad on Windows or TextEdit on
macOS. 10. You are now ready to [encrypt data](encrypt-data.md "encrypt-data.md").

## Example: Generate an encryption schema with

sealed, fingerprint, and cleartext
columns

In this example, for `sales.csv`, there are three columns:
`username` , `purchased`, and `product`. For these
columns, we want the following:

- For the `product` column to be a `sealed` column
- For the `username` column to be encrypted as a `fingerprint`
  column
- For the `purchased` column to be a `cleartext` column

###### To generate an encryption schema with sealed,

fingerprint, and cleartext columns

1. (_Optional_) To ensure the c3r-cli.jar
   file and file to be encrypted are present:
   1. Navigate to the desired directory and run `ls` (if using a
      Mac or Unix/Linux) or
      `dir` if using Windows).
   2. View the list of tabular data files (.csv) and choose a file to encrypt.

   In this example, `sales.csv` is the file that we want to
   encrypt.

2. From the CLI, run the following command to create a schema interactively.

`java -jar c3r-cli.jar schema sales.csv --interactive
 --output=sales.json`

###### Note

    * The `--interactive` flag selects the interactive mode for
     developing the schema. This walks the user through a guided workflow for creating
     the schema.
    * If you are an advanced user, you can create your own schema JSON without using
     the guided workflow. For more information, see [(Optional) Create a schema (advanced users)](create-schema.md "create-schema.md").
    * For .csv files with no column headers, see the `--noHeaders` flag
     for the schema command available in the CLI.
    * The `--output` flag sets an output name. If you don't include the
     `--output` flag, the C3R encryption client tries to pick a default output
     name (such as `<input>.out` or for the schema,
     `<input>.json`).

3. For `Number of target columns from source column ‘username’?`, enter
   `1` and then press **Enter**.
4. For `Target column type: [c]leartext, [f]ingerprint, or [s]ealed?`, enter
   `f` and then press **Enter**.
5. For `Target column headername <default 'username'>`, press
   **Enter**.

The default name ‘`username`’ is used. 6. For `Add suffix '_fingerprint' to header to indicate how it was encrypted,
 [y]es or [n]o <default 'yes'>`, enter `y` and then press
**Enter**. 7. For `Number of target columns from source column ‘purchased’?`, enter
`1` and then press **Enter**. 8. For `Target column type: [c]leartext, [f]ingerprint, or [s]ealed?`, enter
`c` and then press **Enter**. 9. For `Target column headername <default 'purchased'>`, press
**Enter**.

The default name ‘`purchased`’ is used. 10. For `Number of target columns from source column ‘product’?`, enter
`1` and then press **Enter**. 11. For `Target column type: [c]leartext, [f]ingerprint, or [s]ealed?`, enter
`s` and then press **Enter**. 12. For `Target column headername <default 'product'>`, press
**Enter**.

The default name ‘`product`’ is used. 13. For `‘product_sealed’ padding type: [n]one, [f]ixed, or [m]ax <default
 ’max’?>`, press **Enter** to choose the default. 14. For `Byte-length beyond max length to pad cleartext to in
 ‘product_sealed’ <default ‘0’>?` press **Enter** to choose
the default.

The schema is written to a new file called `sales.json`. 15. You are now ready to [encrypt data](encrypt-data.md "encrypt-data.md").
