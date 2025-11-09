|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This software is<br>not currently supported by Amazon Mechanical Turk**<br>The Amazon Mechanical Turk Command Line Tools (CLT) are not currently<br>maintained by Amazon Mechanical Turk. If you would still like to use<br>Amazon Mechanical Turk from the command line, use the `mturk`<br>command in the AWS Command Line Interface (CLI). For more information,<br>see the `mturk` section of the [AWS CLI Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md") . |

 

# updateHITs

## Description

The `updateHITs` command updates properties of HITs that are already on Amazon Mechanical Turk.

All properties of a HIT can be modified:

- Title
- Description
- Keywords
- AssignmentDurationInSeconds
- AutoApprovalDelayInSeconds
- Qualification requirements

###### Important

The Reward property can only be updated for HITs that do not have any assignments that
have been accepted, submitted, approved or rejected.

## Arguments

The following table describes the arguments for the `updateHITs` command.

| Name                     | Description                                                                                                                                                                                                                                                                                                                                            | Required |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| `-properties [filename]` | The HIT properties file that contains the new properties for the HITs.<br>The HITs are updated with all the values defined in this file.<br>For information about this file, see \*The HIT properties file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Example: `-properties helloworld.properties` | Yes      |
| `-help` or `-h`          | Displays the help for this operation.<br>Example: `-help`                                                                                                                                                                                                                                                                                              | No       |
| `-sandbox`               | Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes<br>precedence even if you specify the production web site in your<br>`mturk.properties` file.<br>Example:`-sandbox`                                                                                                                                           | No       |
| `-success [filename]`    | Specifies the success file that contains the IDs of the HITs to be updated. For information<br>about this file, see \*The success file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Example: `-success helloworld.success`                                                                           | Yes      |

## Example

The following examples for Unix and Windows show how to use the `updateHITs` command.
These examples update four HITs in the file `..\survey\survey.success` with the new properties
in the file `..\survey\survey.properties`

### Unix

The following example demonstrates how to call this command from Unix.

```

./updateHITs.sh -success ..\survey\survey.success -properties ..\survey\survey.properties

```

### Windows

The following example demonstrates how to call this command from Microsoft Windows.

```

updateHITs -success ..\survey\survey.success -properties ..\survey\survey.properties

```

## Output

These examples produce the following output.

```

--[Initializing]----------
 Success File: ..\survey\survey.success
 Properties: ..\survey\survey.properties
--[Updating HITs]----------
  Start time: Fri Dec 14 16:48:03 PST 2007
  Input: 4 hitids
  New HITTypeId: SWZZPTZ7Y14ZY8WXNZH0
Updated HIT #0 (4GMZSHZKKK9WT9M9XWA0) to new HITTypeId SWZZPTZ7Y14ZY8WXNZH0
Updated HIT #1 (XYTZY0YK1W2ZTCZM9Z80) to new HITTypeId SWZZPTZ7Y14ZY8WXNZH0
Updated HIT #2 (RZGZZ4Z6GXKTV5DX81B0) to new HITTypeId SWZZPTZ7Y14ZY8WXNZH0
Updated HIT #3 (M26ZN61JMT9E4MG0M94Z) to new HITTypeId SWZZPTZ7Y14ZY8WXNZH0
  End time: Fri Dec 14 16:48:05 PST 2007
--[Done Updating HITs]----------
4 HITS were processed
4 HITS were updated
  Total load time: 2 seconds.


```
