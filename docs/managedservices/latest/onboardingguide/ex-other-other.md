# Other | Other RFC, creating (CLI)

This example shows how to request a change that none of the available CTs address, by using the Management | Other | Other | Create CT (ct-1e1xtak34nx76).

Use this CT when you can't find a change type for what you want; however, if you are unsure about specifying parameters in an existing CT, it is better
to submit a service request for help. For information on submitting service requests, see [Service Request Examples](../userguide/serv-req-mgmt-examples.md "../userguide/serv-req-mgmt-examples.md").

This type of RFC is Approval-required, meaning that it requires AMS approval before it can be implemented.
After submitting the RFC, an AMS operator will contact you to discuss the stack that you want to deploy.

###### Note

When using manual CTs, AMS recommends that you use the ASAP **Scheduling** option
(choose **ASAP** in the console, leave start and end time blank in the API/CLI) as these CTs require an AMS operator to examine the RFC, and
possibly communicate with you before it can be approved and run. If you schedule these RFCs, be sure to allow at least 24 hours. If approval does not
happen before the scheduled start time, the RFC is rejected automatically.

REQUIRED DATA:

- `Comment`: What the RFC is for.
- `ChangeTypeId` and `ChangeTypeVersion`: Use Other | Create (`ct-1e1xtak34nx76`)
  to request new resources, use Other | Update (`ct-0xdawir96cy7k`) to change existing resources; both are `v1`.
  OPTIONAL DATA: `Priority`: Acceptable values are `High`, `Medium`, or `Low`.

_INLINE CREATE_:

- Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline). Example uses Other | Create.

```
aws amscm create-rfc --change-type-id "ct-1e1xtak34nx76" --change-type-version "1.0" --title "`TITLE`" --execution-parameters "{\"Comment\": \"`What you want created`\"}"

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

1. Create and save a JSON file for the execution parameters; example names it OtherParams.json and includes the optional `Priority` parameter:

```
{
"Comment":          "`What you want created`",
"Priority":         "`Medium`"
}
```

2. Create and save a JSON file for the RFC parameters; example names it OtherRfc.json.

```
{
"ChangeTypeId":         "ct-1e1xtak34nx76",
"ChangeTypeVersion":    "`1.0`",
"Title":                "`TITLE`"
}
```

3. Create the RFC, specifying the OtherRfc file and the OtherParams file:

```
aws amscm create-rfc --cli-input-json file://OtherRfc.json  --execution-parameters file://OtherParams.json
```

You receive the RfcId of the new RFC in the response. For example:

```
{
"RfcId": "`RFC-ID`"
}
```

4. Submit the RFC:

```
aws amscm submit-rfc --rfc-id `RFC-ID`
```

If no errors are reported, the operation was successful. 5. To monitor the status of the request and to view Execution Output:

```
aws amscm get-rfc --rfc-id `RFC-ID`
```
