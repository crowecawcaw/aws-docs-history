# Tear Down the Application Deployment

Once you are finished with the tutorial, you will want to tear down the deployment so you are not charged for the resources.

The following is a generic stack delete operation. You'll want to submit it twice, once for the HA 2-Tier stack and once for the S3
bucket stack. As a final follow-through, submit a service request that all snapshots for the S3 bucket (include the S3 bucket stack ID in
the service request) be deleted. They are automatically deleted after 10 days, but deleting them early saves a little bit of cost.

This walkthrough provides an example of using the AMS console to delete an S3 stack; this procedure applies to deleting any stack using the AMS console.

###### Note

If deleting an S3 bucket, it must be emptied of objects first.

REQUIRED DATA:

- `StackId`: The stack to use. You can find this by looking at the AMS Console **Stacks** page, available through a link in the left nav.
  Using the AMS SKMS API/CLI, run the For the AMS SKMS API reference, see the **Reports** tab in the AWS Artifact Console. operation (`list-stack-summaries` in the CLI).
- The change type ID for this walkthrough is `ct-0q0bic0ywqk6c`, the version is "1.0", to find out the latest version, run this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value=ct-0q0bic0ywqk6c
```

_INLINE CREATE_:

- Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline). E

```
aws amscm create-rfc --change-type-id "ct-0q0bic0ywqk6c" --change-type-version "1.0" --title "Delete My Stack" --execution-parameters "{\"StackId\":\"`STACK_ID`\"}"

```

- Submit the RFC using the RFC ID returned in the create RFC operation. Until submitted, the RFC remains in the `Editing` state and is not acted on.

```
aws amscm submit-rfc --rfc-id `RFC_ID`
```

- Monitor the RFC status and view execution output:

```
aws amscm get-rfc --rfc-id `RFC_ID`
```

_TEMPLATE CREATE_:

1. Output the RFC template to a file in your current folder; example names it DeleteStackRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > DeleteStackRfc.json
```

2. Modify and save the DeleteStackRfc.json file. Since deleting a stack has only one execution parameter, the execution parameters can be in the
   DeleteStackRfc.json file itself (there is no need to create a separate JSON file with execution parameters).

The internal quotation marks in the ExecutionParameters JSON extension must be escaped with a backslash (\). Example without start and end time:

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-0q0bic0ywqk6c",
"Title":                "`Delete-My-Stack-RFC`"
"ExecutionParameters":  "{
        \"StackId\":\"`STACK_ID`\"}"
}
```

3. Create the RFC:

```
aws amscm create-rfc --cli-input-json file://DeleteStackRfc.json
```

You receive the RfcId of the new RFC in the response. For example:

```
{
"RfcId": "daaa1867-ffc5-1473-192a-842f6b326102"
}
```

Save the ID for subsequent steps. 4. Submit the RFC:

```
aws amscm submit-rfc --rfc-id `RFC_ID`
```

If the RFC succeeds, you receive no confirmation at the command line. 5. To monitor the status of the request and to view Execution Output:

```
aws amscm get-rfc --rfc-id `RFC_ID` --query "Rfc.{Status:Status.Name,Exec:ExecutionOutput}" --output table
```
