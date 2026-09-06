


|  | 
| --- |
| **This software is not currently supported by Amazon Mechanical Turk**<br />The Amazon Mechanical Turk Command Line Tools (CLT) are not currently maintained by Amazon Mechanical Turk. If you would still like to use Amazon Mechanical Turk from the command line, use the `mturk` command in the AWS Command Line Interface (CLI). For more information, see the `mturk` section of the [ AWS CLI Command Reference ](https://docs.aws.amazon.com/cli/latest/reference/mturk/index.html).  | 

 

# Files Used by the Command Line Tools
<a name="CLTFilesArticle"></a>

 This section describes the files that the Command Line Tools use. 


| File | Description | Used by | 
| --- | --- | --- | 
| The Amazon Mechanical Turk properties file | This file is named `mturk.properties` and it must exist in the directory that you run the Command Line Tools from. <br />This is a text file that contains specific information about your AWS identifiers as well as the Amazon Mechanical Turk service endpoint.  | System | 
| The approve file | A text file that contains a list of assignment IDs and optional approval comments.<br />The first row must contain a column header named *assignmentIDToApprove*. <br />The file can have an optional column named *assignmentIdToApproveComment*. <br />Separate fields with a tab and enclose comments in quotes. |  The `-approvefile` argument of [approveWork](CLTReference_ApproveWorkCommand.md)  | 
| The failure file | A tab delimited text file that contains the rows from the input file that failed to load into Amazon Mechanical Turk. The system generates this file if failures occur when you use [loadHITs](CLTReference_LoadHITsCommand.md). You can fix the entries, rename the file, and then use it to load the HITs that failed. <br />The system creates this file with the name `[your input filename].failure`.  | Not used in command arguments. | 
| The HIT properties file | A text file that defines the properties of the HITs you are creating. Use the format `[property]:[value]` to list the properties in the file. <br />Example: `reward:$0.06` <br />For a list of properties, see [HIT Properties](#HITProperties).  | The `-properties` argument of the following commands:<br /> [loadHITs](CLTReference_LoadHITsCommand.md) <br /> [updateHITs](CLTReference_UpdateHITsCommand.md)  | 
| The input file | A tab delimited text file that contains the dynamic fields of the HIT. This file can contain any information that you need for your HIT. Amazon Mechanical Turk merges this file into your Question template file and your HIT properties file. <br />The first row of the file contains the field headings. Subsequent rows represent the custom field values for the HITs to be loaded. Each row represents one HIT (e.g. 1000 data rows = 1000 HITs).  |  The `-input` argument of the `loadHITs` command.  | 
| The output file | A tab delimited text file that contains the results of submitted HITs that are retrieved from Amazon Mechanical Turk. This file contains all data related to the submitted HITs and assignments. Each HIT in this file has a link to your **Manage HITs** page on the [Requester web site](http://requester.mturk.com/mturk/dashboard). The last column contains a tab delimited set of question/answer pairs for each question field defined in your QuestionForm.  | The `-outputfile` argument of [getResults](CLTReference_GetResultsCommand.md)  | 
| The Qualification answer file | A text file that contains the AnswerKey XML that defines the answer key for your Qualification test. The Amazon Mechanical Turk system automatically scores the test.  | The `-answer` argument of the following commands:<br /> [createQualificationType](CLTReference_CreateQualificationTypeCommand.md) <br /> [updateQualificationType](CLTReference_UpdateQualificationTypeCommand.md)  | 
| The Qualification answer key file | A text file that contains name/value pairs of your questions and expected answers. This answer key provides another method to evaluate Qualification requests by giving you control over when requests are granted. This format also provides more flexibility by allowing you to evaluate FreeTextAnswer answers which cannot be autograded by Amazon Mechanical Turk. <br />The format is `questionid=expected answer value`.  | The `-answers` argument of [evaluateQualificationRequests](CLTReference_EvaluateQualificationRequestsCommand.md)  | 
| The Qualification approve file | A tab delimited text file that contains the list of Qualification requests to approve. <br />The file must contain a column called *qualificationRequestToApprove* that contains the Qualification request IDs. <br />The file can have an optional column called *qualificationRequestToApproveValue* that lists the Qualification score to assign for each Qualification request.  |  The `-approvefile` argument of [approveQualificationRequests](CLTReference_ApproveQualificationRequestsCommand.md)  | 
| The Qualification ID file | A text file that contains the single Qualification ID you want to assign to workers. The file must have a column called *qualtypeid*.  | The `-input` argument of the following commands:<br /> [assignQualification](CLTReference_AssignQualificationCommand.md) <br /> [evaluateQualificationRequests](CLTReference_EvaluateQualificationRequestsCommand.md)  | 
| The Qualification properties file | A text file that defines the properties of the Qualification you are creating. Use the format `[property]=[value]` to list the properties in the file. <br />Example: `autogranted=false`  | The `-properties` argument of the following commands:<br /> [createQualificationType](CLTReference_CreateQualificationTypeCommand.md) <br /> [updateQualificationType](CLTReference_UpdateQualificationTypeCommand.md)  | 
| The Qualification question file | A text file that contains the QuestionForm XML that defines your Qualification test. This file is similar to the question file except that templating is not applicable.  | The `-question` argument of the following commands:<br /> [createQualificationType](CLTReference_CreateQualificationTypeCommand.md) <br /> [updateQualificationType](CLTReference_UpdateQualificationTypeCommand.md)  | 
| The Qualification reject file | A tab delimited text file that contains the list of Qualification requests to reject and optional comments. <br />The file must contain a column called *qualificationRequestToReject* that contains the Qualification request IDs. <br />The file can include an optional column called *qualificationRequestToRejectComment* that contains comments you want to provide to the Worker regarding the rejection.  |  The `-rejectfile` argument of [rejectQualificationRequests](CLTReference_RejectQualificationRequestsCommand.md)  | 
| The Qualification request file | A tab delimited text file that contains the details of the Qualification requests made by Workers.  |  The `-outputfile` argument of [getQualificationRequests](CLTReference_GetQualificationRequestsCommand.md)  | 
| The question file |  A text file that contains the QuestionForm XML that defines your HIT.   To make your QuestionForm a template and merge it with values from your input file use the syntax `${the field name}`, where the field name is the column name from the input file. Amazon Mechanical Turk uses Apache Velocity to perform the merge. For more information about merge syntax, go to [http://velocity.apache.org](http://velocity.apache.org).   |  The `-question` argument of [loadHITs](CLTReference_LoadHITsCommand.md)  | 
| The reject file | A text file that contains a list of assignment ID and optional rejection comments. <br />The first row must contain a column called *assignmentIdToReject*. <br />The file can have an optional column called *assignmentIdToRejectComment*. <br />Separate fields with a tab and enclose comments in quotes. |  The `-rejectfile` argument of the [rejectWork](CLTReference_RejectWorkCommand.md) command  | 
| The score file | A tab delimited file that contains the Worker IDs and the Qualification scores to assign. <br />The file must contain a column called * workerid* that contains the Worker IDs. <br />The file can optionally contain a column called *score* that specifies the scores to assign to Workers.  | The `-scorefile` argument of the [assignQualification](CLTReference_AssignQualificationCommand.md) command.  | 
| The success file | A tab delimited text file that contains the HIT IDs and the HIT Type IDs that were successfully loaded into Amazon Mechanical Turk. This file is generated when you load HITs using [loadHITs](CLTReference_LoadHITsCommand.md) or [updateHITs](CLTReference_UpdateHITsCommand.md). <br />The file must contain a column called *hitid*. <br />The system creates this file with the name `[your input filename].success`.  | The `-successfile` argument of the following commands:<br /> [approveWork](CLTReference_ApproveWorkCommand.md) <br /> [deleteHITs](CLTReference_DeleteHITsCommand.md) <br /> [extendHITs](CLTReference_ExtendHITsCommand.md) <br /> [getResults](CLTReference_GetResultsCommand.md) <br /> [updateHITs](CLTReference_UpdateHITsCommand.md)  | 
| The Worker ID file | A text file that contains a tab delimited list of Worker IDs to assign the Qualification to, and optional Qualification scores. <br />The file must contain a column called *workerid*. <br />The file can optionally contain a column called *score* that lists the Qualification scores to assign to each Worker.  |  The `-input` argument of the [updateQualificationScore](CLTReference_UpdateQualificationScoreCommand.md) command  | 

## HIT Properties
<a name="HITProperties"></a>

 The following table describes the HIT properties.


| Property | Description | 
| --- | --- | 
| title | Title of the HIT | 
| description | Description of the HIT | 
| keywords | Keywords to associate with the HIT | 
| reward | Reward for the HIT formatted as $0.00 USD | 
| assignments | Maximum number of assignments available for this HIT | 
| annotation | Value you use to identify this HIT You can merge values from the input file into this property. To do this, use the syntax: `${the field name}`, where the field name is the column name from the input file. Amazon Mechanical Turk uses Apache Velocity to perform the merge. For more information about merge syntax, go to [http://velocity.apache.org](http://velocity.apache.org).   | 
| assignmentduration | Amount of time, in seconds, a Worker has to complete the assignment  | 
| hitlifetime | Amount of time, in seconds, the HIT is active before it expires | 
| autoapprovaldelay | Amount of time, in seconds, before a submitted assignment is automatically approved | 
| qualification | Qualification requirements for your HIT. To specify the requirements, use the following syntax. +   **qualification.1—**Qualification Type ID <br />+   **qualification.comparator.1—**String that specifies the kind of comparison to make <br />+   **qualification.value.1—**Integer value for the comparator to use <br />+   **qualification.locale.1—**Locale value to use <br />+   **qualification.private.1—**Boolean value that specifies whether Workers who do not meet the qualification requirements can preview the HIT <br />To specify additional qualification requirements, increment the .1 suffix (e.g. `qualification.value.2`).  | 

For more information about the qualification requirements, see [QualificationRequirement Data Structure](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html). For more information about the properties see [HIT Data Structure](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_HITDataStructureArticle.html). 

## Qualification Properties
<a name="QualificationPropeties"></a>

The following table describes the qualification properties.


| Property | Description | 
| --- | --- | 
| name | Name of the Qualification | 
| description | Description of the Qualification | 
| keywords | Keywords to associate with the Qualification | 
| retrydelayinseconds | Minimum amount of time, in seconds, required before a Worker can re-request the Qualification | 
| testdurationinseconds | Amount of time, in seconds, allowed for the Worker to complete the Qualification test (if a test exists) | 
| autogranted | Specifies whether the Qualification should be autogranted upon request. This parameter is only valid if a Qualification does not have a test associated with it. Valid Values: true \| false | 