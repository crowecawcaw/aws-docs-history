|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This software is<br>not currently supported by Amazon Mechanical Turk**<br>The Amazon Mechanical Turk Command Line Tools (CLT) are not currently<br>maintained by Amazon Mechanical Turk. If you would still like to use<br>Amazon Mechanical Turk from the command line, use the `mturk`<br>command in the AWS Command Line Interface (CLI). For more information,<br>see the `mturk` section of the [AWS CLI Command Reference](../../../cli/latest/reference/mturk/index.md "../../../cli/latest/reference/mturk/index.md") . |

 

# extendHITs

## Description

The `extendHITs` command extends the expiration date or increases the maximum
number of assignments for all HITs in the specified `-successfile`. If you extend
the expiration date, and the HIT has not expired, the new expiration date is the existing date plus the
amount of time specified. If the HIT has already expired, the new expiration date is the current time plus
the amount of time specified. If you add additional assignments, you must be sure that you have enough
funds to pay for the assignments.

## Arguments

The following table describes the arguments for the `extendHITs` command.

| Name                      | Description                                                                                                                                                                                                                                                                                                                                                                                     | Required |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `-assignments [integer]`  | The number of assignments to add to the HITs.<br>Example: `-assignments 12`                                                                                                                                                                                                                                                                                                                     | No       |
| `-help` or `-h`           | Displays the help for this operation.<br>Example: `-help`                                                                                                                                                                                                                                                                                                                                       | No       |
| `-hours [integer]`        | The amount of time, in hours, by which to extend the expiration date of the HITs.<br>Example: `-hours 12`                                                                                                                                                                                                                                                                                       | No       |
| `-sandbox`                | Runs this command in the Amazon Mechanical Turk sandbox. This argument takes precedence<br>even if you specify the production web site in your `mturk.properties` file.<br>Example:`-sandbox`                                                                                                                                                                                                   | No       |
| `-successfile [filename]` | The path to the `.success` file that contains the HITs to extend.<br>This is the file that [loadHITs](CLTReference_LoadHITsCommand.md "CLTReference_LoadHITsCommand.md") returns.<br>For information about this file, see \*The success file<br>• in<br>[Files Used by the Command Line Tools](CLTFilesArticle.md "CLTFilesArticle.md").<br>Example:`-successfile ..\mysurvey\mysurvey.success` | Yes      |

## Example

The following examples for Unix and Windows show how to use the `extendHITs`
command. These examples add four assignments and three hours to the five HITs in the
`.success` file.

### Unix

The following example demonstrates how to call this command from Unix.

```

./extendHITs.sh -successfile ..\mysurvey\mysurvey.success -assignments 4 -hours 3

```

### Windows

The following example demonstrates how to call this command from Microsoft Windows.

```

extendHITs -successfile ..\mysurvey\mysurvey.success -assignments 4 -hours 3

```

## Output

This example produces output similar to the following.

```

--- Starting to extend HITs ---
[0YFZ2TYJF3HZPGZV4Z40] Successfully extended HIT (1/5)
[4GMZSHZKKK9WT9M9XWA0] Successfully extended HIT (2/5)
[XYTZY0YK1W2ZTCZM9Z80] Successfully extended HIT (3/5)
[RZGZZ4Z6GXKTV5DX81B0] Successfully extended HIT (4/5)
[M26ZN61JMT9E4MG0M94Z] Successfully extended HIT (5/5)
--- Finished to extend HITs ---
  5 HITs have been extended (added 4 assignment(s), 3 hour(s))
  0 HITs failed to be extended.

```
