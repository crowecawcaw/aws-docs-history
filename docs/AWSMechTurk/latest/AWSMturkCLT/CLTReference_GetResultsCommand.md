|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This software is<br>not currently supported by Amazon Mechanical Turk**<br>The Amazon Mechanical Turk Command Line Tools (CLT) are not currently<br>maintained by Amazon Mechanical Turk. If you would still like to use<br>Amazon Mechanical Turk from the command line, use the `mturk`<br>command in the AWS Command Line Interface (CLI). For more information,<br>see the `mturk` section of the [AWS CLI Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md") . |

 

# getResults

## Description

The `getResults` command retrieves the results of HITs submitted to Amazon Mechanical Turk.
You must supply the name of a file that contains the IDs of the HITs. You can get this file from a call to
[loadHITs](CLTReference_LoadHITsCommand.md "CLTReference_LoadHITsCommand.md").

## Arguments

The following table describes the arguments for the `getResults` command.

| Name                      | Description                                                                                                                                                                                                                                                                                                                                            | Required |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| `-help` or `-h`           | Displays the help for this operation.<br>Example: `-help`                                                                                                                                                                                                                                                                                              | No       |
| `-namevaluepairs`         | Outputs the results as name-value pairs instead of column format.<br>Example: `-namevaluepairs`                                                                                                                                                                                                                                                        | No       |
| `-outputfile [filename]`  | Specifies the file in which the results are saved. For information about this file, see<br>\*The output file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Example: `-outputfile helloworld.results`                                                                                                  | Yes      |
| `-sandbox`                | Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes<br>precedence even if you specify the production web site in your<br>`mturk.properties` file.<br>Example:`-sandbox`                                                                                                                                           | No       |
| `-successfile [filename]` | Specifies the path and name of the `.success` file that<br>[loadHITs](CLTReference_LoadHITsCommand.md "CLTReference_LoadHITsCommand.md") returns.<br>For information about this file, see \*The success file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Example: `-successfile helloworld.success` | Yes      |

This command creates an output file that contains the results of submitted HITs. The file contains all data
related to the submitted HITs and assignments. Each HIT in this file has a link to your
**Manage HITs** page on the [Requester website](http://requester.mturk.com/mturk/dashboard "http://requester.mturk.com/mturk/dashboard").
Use these links to manually reject assignments, pay bonuses, or send emails to Workers.

## Example

The following examples for Unix and Windows show how to use the `getResults` command.

### Unix

The following example demonstrates how to call this command from Unix.

```

./getResults.sh -successfile survey.success -outputfile survey.results

```

### Windows

The following example demonstrates how to call this command from Microsoft Windows.

```

getResults -successfile survey.success -outputfile survey.results

```

## Output

This example writes the results to the survey.results file and produces output similar to the following:

```

--[Retrieving Results]----------
Retrieved HIT 1/10, 832TY7YE5HKWS1H10YR0
Retrieved HIT 2/10, EW2ZHA4R3R7Z4WY5XZAZ
Retrieved HIT 3/10, 5YJ0T51KASD63A4J5YW0
Retrieved HIT 4/10, 0X5PSKYBVXNZPXZHCY0Z
Retrieved HIT 5/10, FWDE79ST7Y6A025QVXHZ
Retrieved HIT 6/10, X3YPN7HBFRXJ1KYMPGWZ
Retrieved HIT 7/10, YZJEZWZ3QW6Z28D9DG90
Retrieved HIT 8/10, 2J5Z5MZ91A06JFGRYYGZ
Retrieved HIT 9/10, PYMPVMRPPWVZTJN9RXE0
Retrieved HIT 10/10, N9PZZ0YW0Y9ZZQZPQH3Z
--[Done Retrieving Results]----------

Results have been written to file 'survey.results'.

Assignments completed: 30/30 (100%)
         Time elapsed: 0:05:16 (h:mm:ss)
  Average submit time: 13.7 seconds

```

## Related Commands

- [approveWork](CLTReference_ApproveWorkCommand.md "CLTReference_ApproveWorkCommand.md")
- [rejectWork](CLTReference_RejectWorkCommand.md "CLTReference_RejectWorkCommand.md")
