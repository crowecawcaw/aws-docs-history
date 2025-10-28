# Converting shell scripts with embedded BTEQ

commands to Amazon Redshift RSQL with AWS Schema Conversion Tool

You can use the AWS Schema Conversion Tool (AWS SCT) to convert shell scripts with embedded Teradata
Basic Teradata Query (BTEQ) commands to shell scripts with embedded Amazon Redshift RSQL
commands.

AWS SCT extracts Teradata BTEQ commands from your shell scripts and converts them to a
format compatible with Amazon Redshift. After you migrate the Teradata database to Amazon Redshift, you can
use these converted scripts to manage your new Amazon Redshift database.

You can also use AWS SCT to convert files with Teradata BTEQ ETL scripts to Amazon Redshift RSQL. For
more information, see [Converting Teradata BTEQ scripts to Amazon Redshift RSQL with AWS SCT](CHAP-converting-bteq-rsql.md "CHAP-converting-bteq-rsql.md").

###### Topics

- [Adding shell scripts with embedded Teradata BTEQ
  commands to your AWS SCT project](#CHAP-converting-shell-rsql-create "#CHAP-converting-shell-rsql-create")
- [Configuring substitution variables in shell
  scripts with embedded Teradata BTEQ commands with AWS SCT](#CHAP-converting-shell-rsql-variables "#CHAP-converting-shell-rsql-variables")
- [Converting shell scripts with embedded Teradata
  BTEQ commands with AWS SCT](#CHAP-converting-shell-rsql-convert "#CHAP-converting-shell-rsql-convert")
- [Managing shell scripts with embedded Teradata
  BTEQ commands with AWS SCT](#CHAP-converting-shell-rsql-manage "#CHAP-converting-shell-rsql-manage")
- [Creating an assessment report for a shell
  script conversion with AWS SCT](#CHAP-converting-shell-rsql-assessment "#CHAP-converting-shell-rsql-assessment")
- [Editing and saving your converted shell scripts with AWS SCT](#CHAP-converting-shell-rsql-save "#CHAP-converting-shell-rsql-save")

## Adding shell scripts with embedded Teradata BTEQ

commands to your AWS SCT project

You can add multiple scripts to a single AWS SCT project.

###### To add a shell script to your AWS SCT project

1. Create a new project in AWS SCT or open an existing project.
   For more information, see [Starting and managing Projects in AWS SCT](CHAP_UserInterface.md "CHAP_UserInterface.md").
2. Choose **Add source** from the menu, and then choose
   **Teradata** to add your source database to the
   project. For more information, see [Teradata databases](CHAP_Source.md "CHAP_Source.md").
3. Choose **Add target** from the menu and to add a target Amazon Redshift database to
   your AWS SCT project.

You can use a virtual Amazon Redshift target database platform. For more information, see [Mapping to virtual targets in the AWS Schema Conversion Tool](CHAP_Mapping.md "CHAP_Mapping.md"). 4. Create a new mapping rule that includes your source Teradata database and your Amazon Redshift target.
For more information, see [Mapping new data types in the AWS Schema Conversion Tool](CHAP_Mapping.md "CHAP_Mapping.md"). 5. On the **View** menu, choose **Main view**. 6. In the left panel, expand the **Scripts** node. 7. Choose **Shell**, open the context (right-click) menu, and then
choose **Load scripts**. 8. Enter the location of your source shell scripts with embedded Teradata BTEQ commands and
choose **Select folder**.

AWS SCT displays the **Load scripts** window. 9. Do one of the following:

    * If your shell scripts don't include the substitution variables, choose **No
     substitution variables**, and then choose
     **OK** to add scripts to your AWS SCT
     project.
    * If your shell scripts include the substitution variables, configure the substitution
     variables. For more information, see [Configuring substitution
     variables in shell scripts](#CHAP-converting-shell-rsql-variables "#CHAP-converting-shell-rsql-variables").

## Configuring substitution variables in shell

scripts with embedded Teradata BTEQ commands with AWS SCT

Your shell scripts can include substitution variables. For example, you can use a single
script with substitution variables to manage databases in different environments.
You can use AWS SCT to configure substitution variables in your shell scripts.

Before you run BTEQ commands with substitution variables from a shell script, make sure to
assign the values for all variables inside this shell script. AWS SCT can resolve
and convert substitution variables only after you assign their values.

###### To configure substitution variables in your shell script

1. Add your source shell scripts to your AWS SCT project. For more information, see [Adding shell scripts to your AWS SCT project](#CHAP-converting-shell-rsql-create "#CHAP-converting-shell-rsql-create").

When you add your scripts, choose **Substitution variables are
used**. 2. For **Define variable format**, enter a
regular expression that matches all substitution variables in your script.

For example, if the names of your substitution variables start with `${`
and end with `}`, use the `\$\{\w+\}` regular expression.
To match substitution variables that start either with a dollar sign or a percent sign,
use the `\$\w+|\%\w+` regular expression.

Regular expressions in AWS SCT conform to the Java regular expression syntax.
For more information, see [java.util.regex Class Pattern](https://docs.oracle.com/javase/6/docs/api/java/util/regex/Pattern.html "https://docs.oracle.com/javase/6/docs/api/java/util/regex/Pattern.html")
in the Java documentation. 3. Choose **OK** to load scripts to your AWS SCT project, and then choose
**OK** to close the **Load scripts**
window. 4. Choose **Variables** to view all discovered substitution variables and their
values. 5. For **Value**, enter the value for the substitution variable.

## Converting shell scripts with embedded Teradata

BTEQ commands with AWS SCT

Following, find how to convert shell scripts with embedded Teradata BTEQ commands to shell
scripts with embedded Amazon Redshift RSQL commands using AWS SCT.

###### To convert a shell script

1. Add your shell scripts to your AWS SCT project. For more information, see [Adding shell scripts to your AWS SCT project](#CHAP-converting-shell-rsql-create "#CHAP-converting-shell-rsql-create").
2. Configure the substitution variables. For more information, see [Configuring substitution
   variables in shell scripts](#CHAP-converting-shell-rsql-variables "#CHAP-converting-shell-rsql-variables").
3. In the left panel, expand the **Scripts** node.
4. Do one of the following:
   - To convert BTEQ commands from a single shell script, expand the
     **Shell** node, choose the script to convert, and then
     choose **Convert script** from the context (right-click)
     menu.
   - To covert multiple scripts, make sure that you select all scripts to convert. Then
     choose **Shell**, open the context (right-click) menu, and then choose
     **Convert script**.

5. Choose **OK**.

AWS SCT converts BTEQ commands in your selected shell scripts to a format compatible
with Amazon Redshift RSQL. Find your converted scripts in the
**Scripts** node in the target database panel. 6. Edit your converted Amazon Redshift RSQL scripts or save them. For more information,
see [Editing and saving your converted
shell scripts](#CHAP-converting-shell-rsql-save "#CHAP-converting-shell-rsql-save").

## Managing shell scripts with embedded Teradata

BTEQ commands with AWS SCT

You can add multiple shell scripts or remove a shell script from your AWS SCT
project.

###### To add a new shell script to your AWS SCT project

1. Expand the **Scripts** node in the left panel.
2. Choose the **Shell** node, and open the context (right-click) menu.
3. Choose **Load scripts**.
4. Enter the information that is required to add a new shell script and configure substitution
   variables. For more information, see [Adding shell scripts to your AWS SCT project](#CHAP-converting-shell-rsql-create "#CHAP-converting-shell-rsql-create") and [Configuring substitution
   variables in shell scripts](#CHAP-converting-shell-rsql-variables "#CHAP-converting-shell-rsql-variables").

###### To remove a shell script from your AWS SCT project

1. Expand the **Shell** node
   under **Scripts** in the left panel.
2. Choose the script to remove, and open the context (right-click) menu.
3. Choose **Delete script**.

## Creating an assessment report for a shell

script conversion with AWS SCT

The _shell script conversion assessment report_ provides information
about converting the BTEQ commands and SQL statements. The conversion is from your
source scripts to a format compatible with Amazon Redshift RSQL. The assessment report includes
action items for BTEQ commands and SQL statements that AWS SCT can't convert.

###### To create a shell script conversion assessment report

1. Expand the **Shell** node
   under **Scripts** in the left panel.
2. Choose the script to convert, open the context (right-click) menu, and then choose
   **Create report**.
3. View the **Summary** tab. The **Summary** tab displays
   the executive summary information from the shell script assessment report.
   It includes conversion results for all BTEQ commands and SQL statements from
   your source scripts.
4. (Optional) Save a local copy of the shell script conversion assessment report as either a
   PDF file or a comma-separated values (CSV) file:
   - To save the shell script conversion assessment report as a PDF file, choose
     **Save to PDF** at upper right.

   The PDF file contains the executive summary, action items, and
   recommendations for scripts conversion.
   - To save the shell script conversion assessment report as a CSV file, choose
     **Save to CSV** at upper right.

   The CSV file contains action items, recommended actions, and an estimated complexity
   of manual effort required to convert the scripts.

5. Choose the **Action items** tab. This tab contains a list of items that
   require manual conversion to Amazon Redshift RSQL. When you select an action item from
   the list, AWS SCT highlights the item from your source shell script that
   the action item applies to.

## Editing and saving your converted shell scripts with AWS SCT

You can edit your converted scripts in the lower panel of your AWS SCT project.
AWS SCT stores the edited script as part of your project.

###### To save your converted scripts

1. Expand the **RSQL scripts** node under **Scripts**
   in the target database panel.
2. Choose your converted script, open the context (right-click) menu, and choose
   **Save script**.
3. Enter the path to the folder to save the converted script and choose
   **Save**.

AWS SCT saves the converted script to a file and opens this file.
