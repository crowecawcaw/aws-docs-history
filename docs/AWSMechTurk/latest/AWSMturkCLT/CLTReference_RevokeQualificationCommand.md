


|  | 
| --- |
| **This software is not currently supported by Amazon Mechanical Turk**<br />The Amazon Mechanical Turk Command Line Tools (CLT) are not currently maintained by Amazon Mechanical Turk. If you would still like to use Amazon Mechanical Turk from the command line, use the `mturk` command in the AWS Command Line Interface (CLI). For more information, see the `mturk` section of the [ AWS CLI Command Reference ](https://docs.aws.amazon.com/cli/latest/reference/mturk/index.html).  | 

 

# revokeQualification
<a name="CLTReference_RevokeQualificationCommand"></a>

## Description
<a name="w2aab9c61b2"></a>

 The `revokeQualification` command revokes a Qualification from a Worker. 

## Arguments
<a name="w2aab9c61b4"></a>

 The following table describes the arguments for the `revokeQualification` command. 


| Name | Description | Required | 
| --- | --- | --- | 
| `-help` or `-h` |  Displays the help for this operation. <br />Example: `-help` | No | 
| `-qualtypeid [Qualification Type ID]` |  The Qualification Type ID of the Qualification to revoke from the Worker. <br />Example: `-qualtypeid RWFZTKZ55ZPZXN1C8TDZ` | Yes | 
| `-reason [text]` |  The reason you are revoking the Qualification. The text must be enclosed in quotation marks. <br /> Example: `-reason "I'm sorry but your work quality is below acceptable standards."`  | No | 
| `-sandbox` |  Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence even if you specify the production web site in your `mturk.properties` file. <br /> Example:`-sandbox`  | No | 
| `-workerid [Worker ID]` |  The Worker ID of the Worker from whom to revoke the Qualification. <br />Example: `-workerid A3C4G8DMXFG5PQ` | Yes | 

## Example
<a name="w2aab9c61b6"></a>

 The following examples for Unix and Windows show how to use the `revokeQualification` command. These examples revoke a Worker's qualification and provide a reason. 

### Unix
<a name="w2aab9c61b6b4"></a>

 The following example demonstrates how to call this command from Unix. 

```
./revokeQualification.sh -qualtypeid RWFZTKZ55ZPZXN1C8TDZ -workerid A3C4G8DMXFG5PQ -reason "I'm sorry but your work quality is below acceptable standards." 
```

### Windows
<a name="w2aab9c61b6b6"></a>

 The following example demonstrates how to call this command from Microsoft Windows. 

```
revokeQualification -qualtypeid RWFZTKZ55ZPZXN1C8TDZ -workerid A3C4G8DMXFG5PQ -reason "I'm sorry but your work quality is below acceptable standards."
```

## Output
<a name="w2aab9c61b8"></a>

These examples produce the following output.

```
Revoked qual RWFZTKZ55ZPZXN1C8TDZ from A3C4G8DMXFG5PQ with reason: 
I'm sorry but your work quality is below acceptable standards.
```