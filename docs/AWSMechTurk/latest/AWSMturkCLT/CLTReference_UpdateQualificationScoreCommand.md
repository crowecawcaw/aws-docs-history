


|  | 
| --- |
| **This software is not currently supported by Amazon Mechanical Turk**<br />The Amazon Mechanical Turk Command Line Tools (CLT) are not currently maintained by Amazon Mechanical Turk. If you would still like to use Amazon Mechanical Turk from the command line, use the `mturk` command in the AWS Command Line Interface (CLI). For more information, see the `mturk` section of the [ AWS CLI Command Reference ](https://docs.aws.amazon.com/cli/latest/reference/mturk/index.html).  | 

 

# updateQualificationScore
<a name="CLTReference_UpdateQualificationScoreCommand"></a>

## Description
<a name="w2aab9c70b2"></a>

 The `updateQualificationScore` command updates the Qualification scores for Workers. 

## Arguments
<a name="w2aab9c70b4"></a>

 The following table describes the arguments for the `updateQualificationScores` command. 


| Name | Description | Required | 
| --- | --- | --- | 
| `-help` or `-h` |  Displays the help for this operation. <br />Example: `-help` | No | 
| `-input [filename]` |  Specifies the file that contains the Worker IDs and desired Qualification scores to assign. For information about this file, see *The Worker ID file* in [Files Used by the Command Line Tools](CLTFilesArticle.md). <br />Condition: Required if the `workerid` argument is not specified.<br />Example: `-input worker_qual_scores.txt` | Conditional | 
| `-qualtypeid [Qualification Type ID` |  The Qualification Type ID to update the Qualification scores for. <br />Example: `-qualtypeid RWFZTKZ55ZPZXN1C8TDZ` | Yes | 
| `-sandbox` |  Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence even if you specify the production web site in your `mturk.properties` file. <br /> Example:`-sandbox`  | No | 
| `-score [integer value]` |  The score to assign to each Worker for the specified Qualification Type ID. <br />Condition: Required if the score is not defined in the `input` file<br />Example: `-score 50` | Conditional | 
| `-workerid [Worker ID]` |  The ID of the Worker you want to assign the score to. <br />Conditions: Required if the `input` argument is not specified.<br />Example: `-workerid A3C4G8DMXFG5PQ` | Conditional | 

## Example
<a name="w2aab9c70b6"></a>

 The following examples for Unix and Windows show how to use the `updateQualificationScore` command. These examples update the score for one Worker. 

### Unix
<a name="w2aab9c70b6b4"></a>

 The following example demonstrates how to call this command from Unix. 

```
./updateQualificationScore.sh -qualtypeid RWFZTKZ55ZPZXN1C8TDZ score 50 -workerid A3C4G8DMXFG5
```

### Windows
<a name="w2aab9c70b6b6"></a>

 The following example demonstrates how to call this command from Microsoft Windows. 

```
updateQualificationScore -qualtypeid RWFZTKZ55ZPZXN1C8TDZ score 50 -workerid A3C4G8DMXFG5
```

## Output
<a name="w2aab9c70b8"></a>

These examples produce the following output.

```
Successfully updated A3C4G8DMXFG5 score to 50
```