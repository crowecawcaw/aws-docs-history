


|  | 
| --- |
| **This software is not currently supported by Amazon Mechanical Turk**<br />The Amazon Mechanical Turk Command Line Tools (CLT) are not currently maintained by Amazon Mechanical Turk. If you would still like to use Amazon Mechanical Turk from the command line, use the `mturk` command in the AWS Command Line Interface (CLI). For more information, see the `mturk` section of the [ AWS CLI Command Reference ](https://docs.aws.amazon.com/cli/latest/reference/mturk/index.html).  | 

 

# evaluateQualificationRequests
<a name="CLTReference_EvaluateQualificationRequestsCommand"></a>

## Description
<a name="w2aab9c25b2"></a>

 The `evaluateQualificationRequests` command evaluates the answers submitted by Workers so you can approve or reject the Qualification requests. You can use the `preview` argument to view the results before you approve them. If you run this command without the `preview` argument, the request is approved or rejected. 

 This command uses an answer key file to automatically review Workers' test results and determine if the Qualification request should be approved or rejected. 

**Tip**  
 This allows you to specify free text answers that can be automatically processed. This overcomes a limitation of the Amazon Mechanical Turk system where FreeTextAnswer type answers cannot be auto-graded. 

 All questions must be answered correctly in order for the Qualification request to be approved. A Qualification score of 100 is assigned for approvals. 

 For more information about Qualifications, see the [Amazon Mechanical Turk Developer Guide](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/). 

## Arguments
<a name="w2aab9c25b4"></a>

 The following table describes the arguments for the `evaluateQualificationRequests` command. 


| Name | Description | Required | 
| --- | --- | --- | 
| `-answers [filename] ` |  Specifies the file that contains the answer key. For information about this file, see *The Qualification answer key file* in [Files Used by the Command Line Tools](CLTFilesArticle.md). <br />Example: `-answers qualification.answerkey` | Yes | 
| `-help` or `-h` |  Displays the help for this operation. <br />Example: `-help` | No | 
| `-input [filename] ` |  Specifies the file that contains the Qualification ID you want to assign to Workers. This file contains a single Qualification ID. This ID is found in a `.success` file generated after you create the Qualification with the [createQualificationType](CLTReference_CreateQualificationTypeCommand.md) operation. For information about this file, see *The Qualification ID file* in [Files Used by the Command Line Tools](CLTFilesArticle.md). <br />Condition: Required if the `qualtypeid` argument is not specified.<br />Example: `-input qualification.properties.success` | Conditional | 
| `-preview` |  Specifies that you want to preview the outcome of the Qualification request evaluations before submitting the decisions to Amazon Mechanical Turk. <br />Example: `-preview` | No | 
| `-qualtypeid [Qualification Type ID] ` |  Specifies the Qualification Type ID for which to evaluate the Qualification requests. <br />Condition: Required if the `input` argument is not specified.<br />Example: `-qualtypeid RWFZTKZ55ZPZXN1C8TDZ` | Conditional | 
| `-sandbox` |  Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence even if you specify the production web site in your `mturk.properties` file. <br /> Example:`-sandbox`  | No | 

## Example
<a name="w2aab9c25b6"></a>

 The following examples for Unix and Windows show how to use the `evaluateQualificationRequests` command. These examples preview the results. 

### Unix
<a name="w2aab9c25b6b4"></a>

 The following example demonstrates how to call this command from Unix. 

```
./evaluateQualificationRequests.sh -answers qualification.answerkey -qualtypeid RWFZTKZ55ZPZXN1C8TDZ -preview
```

### Windows
<a name="w2aab9c25b6b6"></a>

 The following example demonstrates how to call this command from Microsoft Windows. 

```
evaluateQualificationRequests -answers qualification.answerkey -qualtypeid RWFZTKZ55ZPZXN1C8TDZ -preview
```

## Output
<a name="w2aab9c25b8"></a>

These examples produce the following output.

```
Preview flag is set. Qualification requests will not be approved or rejected.
---[Worker A3C4G8DMFSG5PQ]--------------------------------------------------------------
Question question1:CORRECT [The answer key 'false' matches the given answer 'false']
Question question2:CORRECT [The answer key 'true' matches the given answer 'true']
Question question3:CORRECT [The answer key '1' matches the given answer '1']
Worker A3C4G8DMFSG5PQ has PASSED your test and scored 100
---------------------------------------------------------------------------------------
```

## Related Commands
<a name="w2aab9c25c10"></a>

 
+  [getQualificationRequests](CLTReference_GetQualificationRequestsCommand.md) 