# EventBridge event formats

###### Note

Security Hub is in preview release and is subject to change.

The **Findings Imported V2** event type uses the following event format.

###### Example

This format is used when Security Hub sends an event to EventBridge.

```
{
   "version":"0",
   "id":"CWE-event-id",
   "detail-type":"Findings Imported V2",
   "source":"aws.securityhub",
   "account":"111122223333",
   "time":"2019-04-11T21:52:17Z",
   "region":"us-west-2",
   "resources":[
      "e51603d1054aad9d9f498d82d6e81acf4cf6bc88140e8ad2273123c73b81084"
   ],
   "detail":{
      "findings": [{
         `<finding content>`
       }]
   }
}
```

Each event sends a single finding.
`<finding content>` is the content in JSON of the finding sent by the event.

For a complete list of finding attributes, see [OCSF findings in Security Hub CSPM](security-hub-adv-ocsf-findings.md "security-hub-adv-ocsf-findings.md").
