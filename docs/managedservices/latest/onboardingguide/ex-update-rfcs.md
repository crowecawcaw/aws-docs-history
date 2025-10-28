# Update RFCs

You can resubmit an RFC that has been rejected or that has not yet been submitted,
by updating the RFC and then submitting it, or re-submitting it. Note that most RFCs are
rejected because the specified `RequestedStartTime` has passed before
submission or the specified TimeoutInMinutes is inadequate to run the RFC (since
TimeoutInMinutes does not prolong a successful RFC, we recommend always setting this
to at least "60" and up to "360" for an Amazon EC2 or an Amazon EC2 Auto Scaling group with
long-running UserData). This section describes how to use the CLI version of the
`UpdateRfc` command to update an RFC with a new RFC parameter, or
new parameters using either stringified JSON or an updated parameters file.

This example describes using the CLI version of the AMS UpdateRfc API (see
[Update RFC](../ApiReference-cm/update-rfc.md "../ApiReference-cm/update-rfc.md")). While there are change types for updating some
resources (DNS private and public, load balancer stacks, and stack patching configuration), there is no CT to update an RFC.

We recommend that you submit one UpdateRfc operation at a time. If you submit multiple
updates, for example on a DNS stack, the updates might fail attempting to update the DNS at the same time.

REQUIRED DATA: `RfcId`: The RFC you're updating.

OPTIONAL DATA: `ExecutionParameters`: Unless you're updating a non-required
field, like `Description`, you would submit modified execution parameters to
address the issues that caused the RFC to be rejected or canceled. All submitted non-null
values overwrite those values in the original RFC.

1. Find the relevant rejected or canceled RFC, you can use this command (you can substitute
   the value with `Canceled`):

```
aws amscm list-rfc-summaries --filter Attribute=RfcStatusId,Value=Rejected
```

2. You can modify any of the following RFC parameters :

```
{
    "Description": "string",
    "ExecutionParameters": "string",
    "ExpectedOutcome": "string",
    "ImplementationPlan": "string",
    "RequestedEndTime": "string",
    "RequestedStartTime": "string",
    "RfcId": "string",
    "RollbackPlan": "string",
    "Title": "string",
    "WorstCaseScenario": "string"}
```

Example command updating the Description field:

```
aws amscm update-rfc --description "AMSTestNoOpsActionRequired" --rfc-id "`RFC_ID`" --region us-east-1
```

Example command updating the ExecutionParameters VpcId field:

```
aws amscm update-rfc  --execution-parameters "{\"VpcId\":\"`VPC_ID`\"}" --rfc-id "`RFC_ID`" --region us-east-1
```

Example command updating the RFC with an execution parameters file that contains the updates; see example execution parameters file in step 2 of:
[EC2 stack | Create](../ctref/deployment-advanced-ec2-stack-create.md "../ctref/deployment-advanced-ec2-stack-create.md"):

```
aws amscm update-rfc --execution-parameters file://CreateEc2ParamsUpdate.json --rfc-id "`RFC_ID`" --region us-east-1
```

3. Resubmit the RFC using `submit-rfc` and the same RFC ID that you have from when the
   RFC was first created:

```
aws amscm submit-rfc --rfc-id `RFC_ID`
```

If the RFC succeeds, you receive no confirmation or error messages at the command line. 4. To monitor the status of the request and to view Execution Output, run the following command.

```
aws amscm get-rfc --rfc-id `RFC_ID`
```
