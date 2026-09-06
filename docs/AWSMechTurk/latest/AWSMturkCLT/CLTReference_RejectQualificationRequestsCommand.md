


|  | 
| --- |
| **This software is not currently supported by Amazon Mechanical Turk**<br />The Amazon Mechanical Turk Command Line Tools (CLT) are not currently maintained by Amazon Mechanical Turk. If you would still like to use Amazon Mechanical Turk from the command line, use the `mturk` command in the AWS Command Line Interface (CLI). For more information, see the `mturk` section of the [ AWS CLI Command Reference ](https://docs.aws.amazon.com/cli/latest/reference/mturk/index.html).  | 

 

# rejectQualificationRequests
<a name="CLTReference_RejectQualificationRequestsCommand"></a>

## Description
<a name="w2aab9c49b2"></a>

 The `rejectQualificationRequests` command rejects Workers' Qualification requests. 

## Arguments
<a name="w2aab9c49b4"></a>

 The following table describes the arguments for the `rejectQualificationRequests` command. 


| Name | Description | Required | 
| --- | --- | --- | 
| `-force` |  Specifies *not* to prompt for manual confirmation before performing the reject operation. Only advanced developers should use this argument. <br />Example: `-force` | No | 
| `-help` or `-h` |  Displays the help for this operation. <br />Example: `-help` | No | 
| `-qualRequest [Qualification request ID]` |  Specifies the Qualification request ID(s) to reject. You can specify multiple Qualification request IDs in a comma-separated list. The list (or single ID) must be enclosed in quotation marks. <br />Conditions: Required if the `rejectfile` argument is not specified.<br /> Example: `-qualRequest "789RVWYBAZW00EXAMPLE951RVWYBAZW00EXAMPLE"`  | Conditional | 
| `-rejectfile [filename]` |  Specifies a file that contains the list of Qualification requests to reject. For information about this file, see *The Qualification reject file* in [Files Used by the Command Line Tools](CLTFilesArticle.md). <br />Conditions: Required if the `qualRequest` argument is not specified.<br />Example: `-rejectfile qualification_requests_toreject.txt` | Conditional | 
| `-sandbox` |  Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence even if you specify the production web site in your `mturk.properties` file. <br /> Example:`-sandbox`  | No | 

## Example
<a name="w2aab9c49b6"></a>

 The following examples for Unix and Windows show how to use the `rejectQualificationRequests` command. These examples reject one Qualification request listed in the file `toreject.txt`. 

### Unix
<a name="w2aab9c49b6b4"></a>

 The following example demonstrates how to call this command from Unix. 

```
./rejectQualificationRequests.sh -rejectfile toreject.txt 
```

### Windows
<a name="w2aab9c49b6b6"></a>

 The following example demonstrates how to call this command from Microsoft Windows. 

```
rejectQualificationRequests -rejectfile toreject.txt
```

## Output
<a name="w2aab9c49b8"></a>

These examples produce the following output.

```
You are about to reject 1 qualification request(s). Are you sure?
To confirm this operation, please press ENTER (or press Ctrl+C to abort):

If you would like to supply a comment to the worker(s), please type it below then press ENTER. 
If not, just hit ENTER:
	
[789RVWYBAZW00EXAMPLE951RVWYBAZW00EXAMPLE] Qualification request successfully rejected
```