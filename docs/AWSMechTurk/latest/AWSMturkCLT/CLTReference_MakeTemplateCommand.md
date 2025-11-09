|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This software is<br>not currently supported by Amazon Mechanical Turk**<br>The Amazon Mechanical Turk Command Line Tools (CLT) are not currently<br>maintained by Amazon Mechanical Turk. If you would still like to use<br>Amazon Mechanical Turk from the command line, use the `mturk`<br>command in the AWS Command Line Interface (CLI). For more information,<br>see the `mturk` section of the [AWS CLI Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md") . |

 

# makeTemplate

## Description

The `makeTemplate` command creates a copy of a sample application. After you run the
sample applications that the Amazon Mechanical Turk Command Line Tools provide, you might want to create
your own application, probably one that is similar to one of the sample applications. The
`makeTemplate` command makes it easy for you to replicate one of the samples
in a different directory.

You can make a template of a HIT-generating sample, such as the Hello World sample or the Best Image sample. For these
templates, run the `makeTemplate` command from the
`[Command Line Tools installation directory]\hits` directory.

You can also make templates of Qualification-generating samples, such as the Assign Qualification sample. For these
templates, run the `makeTemplate` from the
`Command Line Tools installation directory]\qualifications` directory.

## Arguments

The following table describes the arguments for the `makeTemplate` command.

| Name                         | Description                                                                                                                                                                                                                      | Required |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `-help` or `-h`              | Displays the help for this operation.<br>Example: `-help`                                                                                                                                                                        | No       |
| `-os [Dos or Unix]`          | The type of the operating system.<br>Example: `-os Dos`                                                                                                                                                                          | Yes      |
| `-sandbox`                   | Runs this command in the Amazon Mechanical Turk sandbox for testing.<br>This argument takes precedence even if you specify the production web site in your mturk.properties file.<br>Example:`-sandbox`                          | No       |
| `-scriptTemplateDir [path]`  | The relative path to the script directory.<br>Example:`-scriptTemplateDir ../etc/templates/hits`                                                                                                                                 | Yes      |
| `-target [directory name]`   | Specifies the name of the directory to create. This determines the directory where the new files will be copied.<br>This name is also used for the files that are created in this directory.<br>Example: `-target weathersurvey` | Yes      |
| `-targetRootDir [path]`      | The relative path to the root of the target directory.<br>Example:`-targetRootDir ../hits`                                                                                                                                       | Yes      |
| `-template [directory name]` | The name of the sample directory you are making the template from.<br>Example:`-template image_category`                                                                                                                         | Yes      |
| `-templateRootDir [path]`    | The relative path to the root of the template directory.<br>Example:`-templateRootDir ../samples`                                                                                                                                | Yes      |
| `-type [template type]`      | The type of the template, Hit or Qual.<br>Example:`-type Hit`                                                                                                                                                                    | Yes      |

When you run this command for HIT-type samples, the Command Line Tools creates the new directory and copies
the `.input`, `.question`, and `.properties` files from
the specified sample. It creates these files with the name specified in the `-target` option.
The Command Line Tools also creates new `run.cmd`, `getResults.cmd`, and
`approveAndDeleteResults.cmd` files.

When you run this command for qualification-type samples, the Command Line Tools creates the new directory and
copies the `.answer`,`.question`, and `.properties` files
from the specified sample. It creates these files with the name specified in the `-target` option.
The Command Line Tools also creates new `createQualification.cmd`,
`updateQualification.cmd`, and `deactivateQualification.cmd` files.

## Example

The following examples for Unix and Windows show how to use the `makeTemplate` command.

### Unix

The following example demonstrates how to call this command from Unix.

```

./makeTemplate.sh -target my_survey -template best_image

```

### Windows

The following example demonstrates how to call this command from Microsoft Windows.

```

makeTemplate -template helloworld  -target newhelloworld3 -os Dos -type Hit -templateRootDir ..\samples -targetRootDir ..\hits -scriptTemplateDir ..\etc\templates\hits

```

## Output

These examples produce the following output.

```

Copying resource file: ..\hits\my_survey\my_survey.question
Copying resource file: ..\hits\my_survey\my_survey.properties
Copying resource file: ..\hits\my_survey\my_survey.input
Generating script: ..\hits\my_survey\run.cmd
Generating script: ..\hits\my_survey\getResults.cmd
Generating script: ..\hits\my_survey\approveAndDeleteResults.cmd

```
