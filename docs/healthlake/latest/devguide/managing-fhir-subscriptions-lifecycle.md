# The FHIR Subscription lifecycle with AWS HealthLake

Follow these steps to understand the FHIR Subscription lifecycle:

1. Create a `SubscriptionTopic`
2. Creation
   - Create a `Subscription` with status `"requested"`
   - HealthLake validates the `Subscription` configuration
   - `Subscription` _must_ reference an already existing topic
     (topic _must_ be in status `unknown`, `draft`, `active`).

3. Activation
   - If valid, HealthLake updates status of `Subscription` to `"active"`
   - While creating a `Subscription`, if the topic given was in status `"unknown"`, HealthLake
     updates the status to `"active"` once the Subscription is also active
   - Subscriptions usually take 5-10 minutes to create successfully
   - If `Subscription` does not create successfully, the status will change to `error` where
     you should perform a DELETE operation, then retry creation of a Subscription. You can view the `"error"`
     field in the Subscription resource to see why the Subscription did not create successfully.

4. Ingesting while Subscription is `active`
5. While `Subscription` is `active`
   - HealthLake monitors for events matching your criteria
   - Notifications are sent to configured endpoint when matches occur

6. Error Handling
   - HealthLake attempts retries for 14 days and then stops retrying for those events

7. Deactivation
   - A `Subscription` can be deactivated by:

   Setting an end date (automatic deactivation)

   ```
   {
     "resourceType": "Subscription",
     "meta": {
       "profile": [
         "http://hl7.org/fhir/uv/subscriptions-backport/StructureDefinition/backport-subscription"
       ]
     },
     "status": "requested",
     "end": "2026-07-31T05:38:17.2404292+00:00",
     "reason": "Test subscription for walkthrough",
     "criteria": "https://healthlake.<AWS_REGION>.amazonaws.com/datastore/<datastoreId>/r4/SubscriptionTopic/<your topic id>",
     "_criteria": {
       "extension": [
         {
           "url": "http://hl7.org/fhir/uv/subscriptions-backport/StructureDefinition/backport-filter-criteria",
           "valueString": "Encounter?subject=Patient/<patient id>"
         }
       ]
     },
     "channel": {
       "type": "event-bridge",
       "endpoint": "<your event bus arn>",
       "payload": "application/fhir+json",
       "_payload": {
         "extension": [
           {
             "url": "http://hl7.org/fhir/uv/subscriptions-backport/StructureDefinition/backport-payload-content",
             "valueCode": "id-only"
           }
         ]
       }
     }
   }
   ```

   Deleting the `Subscription` resource

   ```
   DELETE https://<baseHealthLakeURL>/Subscription/<your subscription resource id>
   ```
