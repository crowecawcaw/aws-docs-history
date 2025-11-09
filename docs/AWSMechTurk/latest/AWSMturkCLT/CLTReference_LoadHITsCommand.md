|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This software is<br>not currently supported by Amazon Mechanical Turk**<br>The Amazon Mechanical Turk Command Line Tools (CLT) are not currently<br>maintained by Amazon Mechanical Turk. If you would still like to use<br>Amazon Mechanical Turk from the command line, use the `mturk`<br>command in the AWS Command Line Interface (CLI). For more information,<br>see the `mturk` section of the [AWS CLI Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md") . |

 

# loadHITs

## Description

The `loadHITs` command loads HITs into Amazon Mechanical Turk. Before you can
use this command, you must create an `input` file, a `question`
file, and a `properties` file. If you are loading a single HIT, your
`question` file can contain the question information. The `question`
file is an XML file that conforms to the
[QuestionForm Data Structure](../AWSMturkAPI/ApiReference_QuestionFormDataStructureArticle.md "../AWSMturkAPI/ApiReference_QuestionFormDataStructureArticle.md").
If you are loading multiple HITs, you should create a question template file. This file has the same XML format as the
`question` file, but it contains placeholders for the fields defined in the
`input` file. For each row in the `input` file, the system inserts the
the fields into the placeholders of the template file. The number of rows in the `input`
file determines how many HITs are created. For more information about these files, see
[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").

If the HITs load successfully, this operation creates a `.success` file with the same
name as your `.input` file. That is, if your input file is called
`MyHITs.input`, then the `.success` file will be
`MyHITs.success`. If the HITs do not load successfully, this operation creates
a `.failure` file with the same name as your `.input` file. If you
want to call this command multiple times with the same input file,
you can use the `label` argument to change the name of the created file. For more
information about the `.success` file and the `.failure` file see
[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").

## Arguments

The following table describes the arguments for the `loadHITs` command.

| Name                       | Description                                                                                                                                                                                                                                                                                            | Required |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| `-help` or `-h`            | Displays the help for this operation<br>Example: `-help`                                                                                                                                                                                                                                               | No       |
| `-input [file name]`       | Specifies the input file. For information about this file, see \*The input file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Example: `-input helloworld.input`                                                                                      | Yes      |
| `-label [filename]`        | Specifies the name to use for the `.success` and the<br>`.failure` files.<br>Example: `-label survey_2`                                                                                                                                                                                                | No       |
| `-maxhits`                 | Specifies the maximum number of HITs to create. Use this for testing if you do not want to load<br>the entire input file.<br>Example: `-maxhits 1`                                                                                                                                                     | No       |
| `-preview`                 | Creates an HTML preview of the HIT instead of loading it into Amazon Mechanical Turk. The name of<br>the file is specified by the argument.<br>If the `-previewfile` argument is not specified, this operation creates a file named<br>`preview.html` in the current directory.<br>Example: `-preview` | No       |
| `-previewfile [file name]` | Specifies the name of the html preview file. This argument is used only if the `preview`<br>argument is specified.<br>Example: `-previewfile helloworld.html`                                                                                                                                          | No       |
| `-properties [file name]`  | Specifies the HIT properties file. For information about this file, see<br>\*The HIT properties file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Example: `-properties helloworld.properties`                                                       | Yes      |
| `-question [file name]`    | Specifies the question file. For information about this file, see<br>\*The question file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Example: `-question helloworld.question`                                                                       | Yes      |
| `-sandbox`                 | Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument<br>takes precedence even if you specify the production web site in your<br>`mturk.properties` file.<br>Example:`-sandbox`                                                                                           | No       |

## Example

The following examples for Unix and Windows show how to use the `loadHITs` command.
This example loads five HITs using the information found in the `survey.input`,
`survey.question`, and `survey.properties` files
found in the directory `..\survey`.

### Unix

The following example demonstrates how to call this command from Unix.

```

./loadHITs.sh -input ..\survey\survey.input -question ..\survey\survey.question -properties ..\survey\survey.properties

```

### Windows

The following example demonstrates how to call this command from Microsoft Windows.

```

loadHITs -input ..\survey\survey.input -question ..\survey\survey.question -properties ..\survey\survey.properties

```

## Output

These examples create a `.success` file with the same path and name
as the file specified by the`-input` argument. In these examples, the returned file
is `survey.sucess` in the `..\survey` directory. The command
produces the following output.

```

--[Initializing]----------
 Input: ..\survey\survey.input
 Properties: ..\survey\survey.properties
 Question File: ..\survey\survey.question
 Preview mode disabled
--[Loading HITs]----------
  Start time: Fri Dec 14 16:23:28 PST 2007
Created HIT 1: HITId=GX9P62Y4EXAZSZYRQ8EZ
Created HIT 2: HITId=2WAZRKZHC27ZV25HYXD0
Created HIT 3: HITId=R8TZ2QYQKXMZ6X1NYKN0
Created HIT 4: HITId=TA6CVRDAQBWPTNN013W0
Created HIT 5: HITId=R0AZ1KZSVWFZS75QZRF0

You may see your HIT(s) with HITTypeId 'YTXZ13ZWEYFZRBZ4V120' here:

  http://www.mturk.com/mturk/preview?groupId=YTXZ13ZWEYFZRBZ4V120

  End time: Fri Dec 14 16:23:32 PST 2007
--[Done Loading HITs]----------
  Total load time: 4 seconds.
  Successfully loaded 5 HITs.


```

## Related Commands

- [getResults](CLTReference_GetResultsCommand.md "CLTReference_GetResultsCommand.md")
