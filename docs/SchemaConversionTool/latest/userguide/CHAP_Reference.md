# CLI Reference for AWS Schema Conversion Tool

This section describes how to get started with the AWS SCT command line interface (CLI).
Also, this section provides information about the key commands and usage modes. For a full
reference of AWS SCT CLI commands, see [Reference material](#CHAP_Reference.Download "#CHAP_Reference.Download").

###### Topics

- [Prerequisites for using the AWS SCT
  command line interface](#CHAP_Reference.Prerequisites "#CHAP_Reference.Prerequisites")
- [AWS SCT CLI interactive mode](#CHAP_Reference.InteractiveMode "#CHAP_Reference.InteractiveMode")
- [Getting AWS SCT CLI scenarios](#CHAP_Reference.Scenario "#CHAP_Reference.Scenario")
- [Editing AWS SCT CLI scenarios](#CHAP_Reference.Editing "#CHAP_Reference.Editing")
- [AWS SCT CLI script mode](#CHAP_Reference.ScriptMode "#CHAP_Reference.ScriptMode")
- [AWS SCT CLI reference material](#CHAP_Reference.Download "#CHAP_Reference.Download")

## Prerequisites for using the AWS SCT

command line interface

Download and install the latest version of Amazon Corretto 11. For more information, see
[Downloads for Amazon Corretto 11](../../../corretto/latest/corretto-11-ug/downloads-list.md "../../../corretto/latest/corretto-11-ug/downloads-list.md") in the _Amazon Corretto 11 User Guide_.

Download and install the latest version of AWS SCT. For more information, see [Installing AWS Schema Conversion Tool](CHAP_Installing.md "CHAP_Installing.md").

## AWS SCT CLI interactive mode

You can use the AWS SCT command line interface in interactive mode. In this mode,
you enter commands into the console one by one. You can use this interactive mode to
learn more about CLI commands or download the most commonly used CLI scenarios.

To convert your source database schema in AWS SCT, run a sequence operation:
create a new project, connect to source and target databases, create mapping rules, and
convert database objects. Because this workflow can be complex, we recommend using scripts
in the AWS SCT CLI mode. For more information, see [Script mode](#CHAP_Reference.ScriptMode "#CHAP_Reference.ScriptMode").

You can run the AWS SCT CLI commands from the `app` folder of your AWS SCT installation
path. In Windows, the default installation path is `C:\Program Files\AWS Schema Conversion Tool\`.
Make sure that this folder includes the `AWSSchemaConversionToolBatch.jar` file.

To enter the AWS SCT CLI interactive mode, use the following command after you complete the
prerequisites.

```
java -jar AWSSchemaConversionToolBatch.jar -type interactive
```

Now you can run AWS SCT CLI commands. Make sure that you end your commands with `/`
in a new line. Also, make sure that you use straight single quotation marks (`'`) before
and after the values of command parameters.

###### Note

If the preceding command returns `Unexpected error`, try the following:

```
java -Djdk.jar.maxSignatureFileSize=20000000 -jar AWSSchemaConversionToolBatch.jar
```

To see the list of available commands in AWS SCT CLI interactive mode, run the following command.

```
help
/
```

To view information about an AWS SCT CLI command, use the following command.

```
help -command: '`command_name`'
/
```

In the preceding example, replace `command_name` with the name of a command.

To view information about parameters of an AWS SCT CLI command, use the following command.

```
help -command: '`command_name`' -parameters: '`parameters_list`'
/
```

In the preceding example, replace `command_name` with the name of a command.
Then, replace `parameters_list` with a list of parameter names separated by a
comma.

To run a script from a file in AWS SCT CLI interactive mode, use the following command.

```
ExecuteFile -file: '`file_path`'
/
```

In the preceding example, replace `file_path` with the path to your file with
a script. Make sure that your file has an `.scts` extension.

To exit AWS SCT CLI interactive mode, run the `quit` command.

### Examples

The following example displays the information about the `Convert` command.

```
help -command: 'Convert'
/
```

The following example displays the information about two parameters of the `Convert` command.

```
help -command: 'Convert' -parameters: 'filter, treePath'
/
```

## Getting AWS SCT CLI scenarios

To get the most commonly used AWS SCT scenarios, you can use the `GetCliScenario` command.
You can run this command in interactive mode, then edit the downloaded templates. Use the edited files
in script mode.

The `GetCliScenario` command saves the selected template or all available
templates to the specified directory. The template contains the complete set of commands to
run a script. Make sure that you edit the file paths, database credentials, object names, and
other data in these templates. Also, make sure that you remove the commands that you don't use
and add new commands to the script where needed.

To run the `GetCliScenario` command, complete the prerequisites and enter AWS SCT CLI
interactive mode. For more information, see [Interactive mode](#CHAP_Reference.InteractiveMode "#CHAP_Reference.InteractiveMode").

Next, use the following syntax to run the `GetCliScenario` command and get the AWS SCT
scenarios.

```
GetCliScenario -type: '`template_type`' -directory: '`file_path`'
/
```

In the preceding example, replace `template_type` with one of the template types
from the following table. Next, replace `file_path` with the path the folder
where you want to download scripts. Make sure that AWS SCT can access this folder without requesting admin
rights. Also, make sure that you use straight single quotation marks (`'`) before
and after the values of command parameters.

To download all AWS SCT CLI templates, run the preceding command without the `-type` option.

The following table includes the types of AWS SCT CLI templates that you can download.
For each template, the table includes the file name and the description of operations that you can run
using the script.

| Template type                 | File name                                    | Description                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BTEQScriptConversion          | `BTEQScriptConversionTemplate.scts`          | Converts Teradata Basic Teradata Query (BTEQ), FastExport, FastLoad, and<br>MultiLoad scripts to Amazon Redshift RSQL. For more information, see [Converting Data Using ETL](CHAP-converting-etl.md "CHAP-converting-etl.md").                                                                                                                             |
| ConversionApply               | `ConversionTemplate.scts`                    | Converts source database schemas and applies the converted code to the target database.<br>Optionally, saves the converted code as a SQL script, and saves the assessment report. For more information,<br>see [Converting schemas](CHAP_Converting.md "CHAP_Converting.md").                                                                              |
| GenericAppConversion          | `GenericApplicationConversionTemplate.scts`  | Converts SQL code embedded into your applications with the generic AWS SCT application<br>converter. For more information, see [SQL code](CHAP_Converting.App.md "CHAP_Converting.App.md").                                                                                                                                                                |
| HadoopMigration               | `HadoopMigrationTemplate.scts`               | Migrates your on-premises Hadoop cluster to Amazon EMR. For more information, see<br>[Connecting to Apache Hadoop databases with the AWS Schema Conversion Tool](CHAP_Source.md "CHAP_Source.md").                                                                                                                                                         |
| HadoopResumeMigration         | `HadoopResumeMigrationTemplate.scts`         | Resumes an interrupted migration of your on-premises Hadoop cluster to Amazon EMR.<br>For more information, see [Connecting to Apache Hadoop databases with the AWS Schema Conversion Tool](CHAP_Source.md "CHAP_Source.md").                                                                                                                              |
| Informatica                   | `InformaticaConversionTemplate.scts`         | Converts SQL code embedded into your Informatica extract, transform, and load (ETL) scripts.<br>Configures connections to your source and target databases in your ETL scripts, and saves converted scripts<br>after the conversion. For more information, see [Informatica ETL scripts](CHAP-converting-informatica.md "CHAP-converting-informatica.md"). |
| LanguageSpecificAppConversion | `LanguageSpecificAppConversionTemplate.scts` | Converts SQL code embedded into your C#, C++, Java, and Pro\*C applications with the AWS SCT<br>application converter. For more information, see [Converting application SQL](CHAP_Converting.md "CHAP_Converting.md").                                                                                                                                    |
| OozieConversion               | `OozieConversionTemplate.scts`               | Converts your Apache Oozie workflows to AWS Step Functions. For more information, see<br>[Connecting to Apache Oozie workflows with the AWS Schema Conversion Tool](CHAP_Source.md "CHAP_Source.md").                                                                                                                                                      |
| RedshiftAgent                 | `DWHDataMigrationTemplate.scts`              | Converts source data warehouse schemas and applies the converted code to the target Amazon Redshift database.<br>Then registers a data extraction agent, creates and starts a data migration task. For more information,<br>see [Migrating from a data warehouse](agents.md "agents.md").                                                                  |
| ReportCreation                | `ReportCreationTemplate.scts`                | Creates a database migration report for several source database schemas. Then saves this report<br>as a CSV of PDF file. For more information, see [Assessment report](CHAP_AssessmentReport.md "CHAP_AssessmentReport.md").                                                                                                                               |
| SQLScriptConversion           | `SQLScriptConversionTemplate.scts`           | Converts SQL\*Plus or TSQL scripts to PL/SQL and saves converted scripts. Also, saves an assessment<br>report.                                                                                                                                                                                                                                             |

After you download the AWS SCT CLI template, use the text editor to configure the script
to run on your source and target databases. Next, use the AWS SCT CLI script mode to run your script.
For more information, see [AWS SCT CLI script mode](#CHAP_Reference.ScriptMode "#CHAP_Reference.ScriptMode").

### Examples

The following example downloads all templates into the `C:\SCT\Templates` folder.

```
GetCliScenario -directory: 'C:\SCT\Templates'
/
```

The following example downloads the template for the `ConversionApply` operation into
the `C:\SCT\Templates` folder.

```
GetCliScenario -type: 'ConversionApply' -directory: 'C:\SCT\Templates'
/
```

## Editing AWS SCT CLI scenarios

After you downloaded scenario templates, configure them to get working scripts that
can run on your databases.

For all templates, make sure that you provide the path to the drivers for your
source and target databases. For more information, see [Installing JDBC drivers for AWS Schema Conversion Tool](CHAP_Installing.md "CHAP_Installing.md").

Make sure that you include the database credentials for source and target databases. Also, make
sure that you set up mapping rules to describe a source-target pair for your conversion
project. For more information, see [Data type mapping](CHAP_Mapping.md "CHAP_Mapping.md").

Next, configure the scope of the operations to run. You can remove the commands that you don't use
or add new commands to the script.

For example, suppose that you plan to convert all schemas in your source Oracle database to PostgreSQL.
Then you plan to save your database migration assessment report as a PDF and apply the converted code to
the target database. In this case, you can use the template for the `ConversionApply` operation.
Use the following procedure to edit your AWS SCT CLI template.

###### To edit the AWS SCT CLI template for the `ConversionApply` operation

1. Open the `ConversionTemplate.scts` that you downloaded. For more information, see [Examples](#CHAP_Reference.Scenario.Examples "#CHAP_Reference.Scenario.Examples").
2. Remove **CreateFilter**, **Convert -filter**,
   **ApplyToTarget -filter**, **SaveTargetSQL**,
   **SaveTargetSQLbyStatement**, and **SaveReportCSV** operations from
   your script.
3. For **oracle_driver_file** in the **SetGlobalSettings**
   operation, enter the path to your Oracle driver. Then, for **postgresql_driver_file**,
   enter the path to your PostgreSQL driver.

If you use other database engines, use appropriate names for the settings. For a full list of
global settings that you can set in the **SetGlobalSettings** operation, see
**Global settings matrix** in the [Reference material](#CHAP_Reference.Download "#CHAP_Reference.Download"). 4. (Optional) For **CreateProject**, enter the name of your project and the location
for your local project file. If you choose to proceed with the default values, make sure that AWS SCT
can create files in the `C:\temp` folder without requesting admin rights. 5. For **AddSource**, enter the IP address of your source database server. Also,
enter the user name, password, and port to connect to your source database server. 6. For **AddTarget**, enter the IP address of your target database server. Also,
enter the user name, password, and port to connect to your target database server. 7. (Optional) For **AddServerMapping**, enter the source and target database objects
that you want to add to a mapping rule. You can use `sourceTreePath` and `targetTreePath`
parameters to specify the path to the database objects. Optionally, you can use `sourceNamePath`
and `targetNamePath` to specify the names of the database objects. For more information, see
**Server mapping commands** in the [Reference material](#CHAP_Reference.Download "#CHAP_Reference.Download").

The default values of the **AddServerMapping** operation map all source schemas
with your target database. 8. Save the file and then use the script mode to run it. For more information, see [Script mode](#CHAP_Reference.ScriptMode "#CHAP_Reference.ScriptMode").

## AWS SCT CLI script mode

After you create an AWS SCT CLI script or edit a template, you can run it with the
`RunSCTBatch` command. Make sure that you save your file with the CLI script
as an `.scts` extension.

You can run AWS SCT CLI scripts from the `app` folder of your AWS SCT installation path.
In Windows, the default installation path is `C:\Program Files\AWS Schema Conversion Tool\`. Make
sure that this folder includes the `RunSCTBatch.cmd` or `RunSCTBatch.sh` file. Also,
this folder should include the `AWSSchemaConversionToolBatch.jar` file.

Alternatively, you can add the path to the `RunSCTBatch` file in the `PATH`
environment variable on your operating system. After you update the `PATH` environment variable,
you can run AWS SCT CLI scripts from any folder.

To run an AWS SCT CLI script, use the following command in Windows.

```
RunSCTBatch.cmd --pathtoscts "`file_path`"
```

In the preceding example, replace `file_path` with the path
to your file with a script.

To run an AWS SCT CLI script, use the following command in Linux.

```
RunSCTBatch.sh --pathtoscts "`file_path`"
```

In the preceding example, replace `file_path` with the path
to your file with a script.

You can provide optional parameters in this command, such as database credentials,
the level of details in the console output, and others. For more information, download
the AWS SCT command line interface reference at [Reference material](#CHAP_Reference.Download "#CHAP_Reference.Download").

### Examples

The following example runs the `ConversionTemplate.scts` script in the
`C:\SCT\Templates` folder. You can use this example in Windows.

```
RunSCTBatch.cmd --pathtoscts "C:\SCT\Templates\ConversionTemplate.scts"
```

The following example runs the `ConversionTemplate.scts` script in the
`/home/user/SCT/Templates` directory. You can use this example in Linux.

```
RunSCTBatch.sh --pathtoscts "/home/user/SCT/Templates/ConversionTemplate.scts"
```

## AWS SCT CLI reference material

You can find reference material about the AWS Schema Conversion Tool command line interface (CLI) in the following
guide: [AWS Schema Conversion Tool CLI
Reference](https://s3.amazonaws.com/publicsctdownload/AWS+SCT+CLI+Reference.pdf "https://s3.amazonaws.com/publicsctdownload/AWS+SCT+CLI+Reference.pdf").
