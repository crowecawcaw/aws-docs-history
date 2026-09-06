


|  | 
| --- |
| **This software is not currently supported by Amazon Mechanical Turk**<br />The Amazon Mechanical Turk Command Line Tools (CLT) are not currently maintained by Amazon Mechanical Turk. If you would still like to use Amazon Mechanical Turk from the command line, use the `mturk` command in the AWS Command Line Interface (CLI). For more information, see the `mturk` section of the [ AWS CLI Command Reference ](https://docs.aws.amazon.com/cli/latest/reference/mturk/index.html).  | 

 

# approveQualificationRequests
<a name="CLTReference_ApproveQualificationRequestsCommand"></a>

## Description
<a name="w2aab9b7b2"></a>

 The `approveQualificationRequests` command approves a list of Qualification requests. You can obtain the list from a call to [getQualificationRequests](CLTReference_GetQualificationRequestsCommand.md). 

 For information about Qualifications and Qualification requests, see the [Amazon Mechanical Turk Developer Guide](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/). 

## Arguments
<a name="w2aab9b7b4"></a>

 The following table describes the arguments for the `approveQualificationRequests` command. 


| Name | Description | Required | 
| --- | --- | --- | 
| `-approvefile [filename] ` |  Specifies a tab delimited text file that contains the list of Qualification requests to approve. For information about this file, see *The Qualification approve file* in [Files Used by the Command Line Tools](CLTFilesArticle.md). <br /> Condition: Required if the `qualRequest` argument is not specified. <br />Example: `-approvefile qualification_requests_toapprove.txt` | Conditional | 
| `-force` |  Specifies *not* to prompt for manual confirmation before approving the requests. Only advanced developers should use this argument. <br />Example: `-force` | No | 
| `-help` or `-h` |  Displays the help for this operation. <br />Example: `-help` | No | 
| `-qualRequest [Qualification request ID]` |  The Qualification request IDs to approve. Multiple Qualification request IDs are comma separated. <br /> Condition: Required if the `approvefile` argument is not specified. <br /> Example: `-qualRequest TA3ZJBYP2Y7ZJSX2BBN0TZ8ZTM4F6H4ZVQ4DE8FZ`  | Conditional | 
| `-sandbox` |  Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence even if you specify the production web site in your `mturk.properties` file. <br /> Example:`-sandbox`  | No | 
| `-score [value]` |  The default score to assign for each approved Qualification request. Any scores defined in the `approvefile` override this default. <br />Example: `-score 100` | No | 

## Example
<a name="w2aab9b7b6"></a>

 The following examples for Unix and Windows show how to use the `approveQualificationRequests` command. The examples use a file named `qualifications.txt` that contains 10 requests. Each request in the file gets a score of 100. 

### Unix
<a name="w2aab9b7b6b4"></a>

 The following example demonstrates how to call this command from Unix. 

```
./approveQualificationRequests.sh -approvefile qualifications.txt -score 100
```

### Windows
<a name="w2aab9b7b6b6"></a>

 The following example demonstrates how to call this command from Microsoft Windows. 

```
approveQualificationRequests -approvefile qualifications.txt -score 100
```

## Output
<a name="w2aab9b7b8"></a>

These examples produce output similar to the following, but all 10 requests are listed.

```
You are about to grant 10 qual request(s).
To confirm this operation, please press ENTER (or press Ctrl+C to abort):
	  
[TA3ZJBYP2Y7ZJSX2BBN0TZ8ZTM4F6H4ZVQ4DE8FZ] QualRequest successfully approved with value (100)
```

## Related Commands
<a name="w2aab9b7c10"></a>

 
+  [rejectQualificationRequests](CLTReference_RejectQualificationRequestsCommand.md) 
+  [revokeQualification](CLTReference_RevokeQualificationCommand.md) 