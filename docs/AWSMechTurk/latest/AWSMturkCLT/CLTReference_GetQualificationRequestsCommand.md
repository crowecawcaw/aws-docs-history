


|  | 
| --- |
| **This software is not currently supported by Amazon Mechanical Turk**<br />The Amazon Mechanical Turk Command Line Tools (CLT) are not currently maintained by Amazon Mechanical Turk. If you would still like to use Amazon Mechanical Turk from the command line, use the `mturk` command in the AWS Command Line Interface (CLI). For more information, see the `mturk` section of the [ AWS CLI Command Reference ](https://docs.aws.amazon.com/cli/latest/reference/mturk/index.html).  | 

 

# getQualificationRequests
<a name="CLTReference_GetQualificationRequestsCommand"></a>

## Description
<a name="w2aab9c34b2"></a>

 The `getQualificationRequests` command retrieves the Qualification requests from Workers for your Qualifications. For more information about Qualifications and Qualification requests see the [Amazon Mechanical Turk Developer Guide](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/). 

## Arguments
<a name="w2aab9c34b4"></a>

 The following table describes the arguments for the `getQualificationRequests` command. 


| Name | Description | Required | 
| --- | --- | --- | 
| `-help` or `-h` |  Displays the help for this operation. <br />Example: `-help` | No | 
| `-outputfile [filename]` |  Specifies the output file. This is a tab delimited text file that contains the details of Workers' Qualification. You can then approve or reject the Qualification Requests by using [approveQualificationRequests](CLTReference_ApproveQualificationRequestsCommand.md) or [rejectQualificationRequests](CLTReference_RejectQualificationRequestsCommand.md) command. For information about this file, see *The Qualification request file* in [Files Used by the Command Line Tools](CLTFilesArticle.md). <br />Example: `-outputfile qualification_requests.txt` | Yes | 
| `-qualtypeid [Qualification Type ID]` |  Specifies the Qualification Type ID of the Qualification you want to retrieve requests for. This ID is in a `.success` file generated after you create the Qualification with the [createQualificationType](CLTReference_CreateQualificationTypeCommand.md) command. If this ID is not specified, all Qualification requests for Qualifications you own are included in the output file. <br />Example:`-qualtypeid RWFZTKZ55ZPZXN1C8TDZ` | No | 
| `-sandbox` |  Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence even if you specify the production web site in your `mturk.properties` file. <br /> Example:`-sandbox`  | No | 

## Example
<a name="w2aab9c34b6"></a>

 The following examples for Unix and Windows show how to use the `getQualificationRequests` command. These examples write the requests for all Qualification types to the file `qualrequests.txt`. 

### Unix
<a name="w2aab9c34b6b4"></a>

 The following example demonstrates how to call this command from Unix: 

```
./getQualificationRequests.sh -outputfile qualrequests.txt
```

### Windows
<a name="w2aab9c34b6b6"></a>

 The following example demonstrates how to call this command from Microsoft Windows: 

```
getQualificationRequests -outputfile qualrequests.txt
```

## Output
<a name="w2aab9c34b8"></a>

These examples retrieved four Qualfication requests and produced the following output.

```
Retrieved 4 Qualification Requests
Answers successfully saved to file: qualrequests.txt
```

## Related Commands
<a name="w2aab9c34c10"></a>

 
+  [evaluateQualificationRequests](CLTReference_EvaluateQualificationRequestsCommand.md)
+  [approveQualificationRequests](CLTReference_ApproveQualificationRequestsCommand.md)
+  [rejectQualificationRequests](CLTReference_RejectQualificationRequestsCommand.md)