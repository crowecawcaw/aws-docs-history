


|  | 
| --- |
| **This software is not currently supported by Amazon Mechanical Turk**<br />The Amazon Mechanical Turk Command Line Tools (CLT) are not currently maintained by Amazon Mechanical Turk. If you would still like to use Amazon Mechanical Turk from the command line, use the `mturk` command in the AWS Command Line Interface (CLI). For more information, see the `mturk` section of the [ AWS CLI Command Reference ](https://docs.aws.amazon.com/cli/latest/reference/mturk/index.html).  | 

 

# reviewResults
<a name="CLTReference_ReviewResultsCommand"></a>

## Description
<a name="w2aab9c58b2"></a>

 The `reviewResults` command allows you to approve or reject multiple assignments from a file. You use the output file from [getResults](CLTReference_GetResultsCommand.md) to specify which assignments to reject. All other assignments are approved. 

**To use the reviewResults command**

1.  Run [getResults](CLTReference_GetResultsCommand.md).

1.  Open the output file.

1.  For each assignment you want to reject, type any character in the "reject" column for that assignment.

1.  Specify the file in the `-resultsfile` argument for the `reviewResults` command. 

1.  Run the `reviewResults` command.

**Important**  
 Any mark in the "reject" column for an assignment causes the assignment to be rejected. Any unmarked assignments are accepted. 

## Arguments
<a name="w2aab9c58b4"></a>

 The following table describes the arguments for the `reviewResults` command. 


| Name | Description | Required | 
| --- | --- | --- | 
| `-help` or `-h` |  Displays the help for this operation. <br />Example: `-help` | No | 
| `-resultsfile [filename]` |  Specifies the output file from [getResults](CLTReference_GetResultsCommand.md) in which you have marked the assignments to reject. All unmarked assignments are approved. <br />Example: `-resultsfile helloworld.results` | Yes | 
| `-sandbox` |  Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence even if you specify the production web site in your `mturk.properties` file. <br /> Example:`-sandbox`  | No | 

## Example
<a name="w2aab9c58b6"></a>

 The following examples for Unix and Windows show how to use the `reviewResults` command. 

### Unix
<a name="w2aab9c58b6b4"></a>

 The following example demonstrates how to call this command from Unix. 

```
./reviewResults.sh  -resultsfile survey.results
```

### Windows
<a name="w2aab9c58b6b6"></a>

 The following example demonstrates how to call this command from Microsoft Windows. 

```
reviewResults -resultsfile survey.results
```

## Output
<a name="w2aab9c58b8"></a>

This example produces output similar to the following:

```
[BWZZVVYNNYKZ6QZT4V00QHRZNS93BANZ7ZZ2AW50] Assignment successfully approved
[5W48WR9T5X2ZYVZYNS7Z92QZ2VYWNZ1EYSWY3X4Z] Assignment successfully approved
[JYVZ4GXZ0XYZNEZ29350XXX0VR986J4YP6ZH7WZ0] Assignment successfully approved
[M0ZZXFC0J8KP56YVNWM0A0KZSCYA3YFZPJRNGR8Z] Assignment successfully approved
[1Z0ZHS5GGYQWWA83XVE05KZ4RSY233CZ0G91XAJZ] Assignment successfully approved

Assignments approved: 5/5 (100%)
Assignments rejected: 0/5 (0%)
Assignments failed: 0/5 (0%)
```

## Related Commands
<a name="w2aab9c58c10"></a>

 
+  [approveWork](CLTReference_ApproveWorkCommand.md) 
+  [rejectWork](CLTReference_RejectWorkCommand.md) 