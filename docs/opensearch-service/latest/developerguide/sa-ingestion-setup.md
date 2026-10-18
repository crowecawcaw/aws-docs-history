

# Setting up ingestion for a Security Analytics detector
<a name="sa-ingestion-setup"></a>

A Security Analytics detector reads from an index or an index alias. When you ingest logs into time-based indexes (for example, one index for each day), you must make sure of two things. Your detector must follow the current write index. Every new index must contain the fields and field aliases that the detector's rules reference. If either condition isn't met, the detector silently skips rules or stops producing findings after you create a new index.

This topic describes the recommended setup for one log source. You can apply the same pattern to every other log source; only the names and fields change. With this setup, you get the following behavior:
+ You write every record through the index alias, so it always lands in the index that your detector is tracking.
+ Index State Management (ISM) creates a new index and makes it the write index automatically every day through a rollover action. For more information about ISM, see [Index State Management in Amazon OpenSearch Service](ism.md).
+ Your index template creates every new index with all the fields and field aliases that the detector's rules need.

**Note**  
Create one detector for each index alias. If you have several log sources, create a separate alias, index template, ISM policy, and detector for each one. This keeps performance optimal, because each detector keeps its own internal index that tracks the fields of every index it watches. If several detectors share one alias, or one detector watches several aliases, this internal index grows larger and rolls over more often than needed.

## How the recommended setup differs from a typical setup
<a name="sa-ingestion-setup-compare"></a>

In a typical setup, you configure your log shippers to write directly to dated index names, and you rely on an Index State Management (ISM) policy to add each new index to the alias after you create it. The recommended setup changes the following behaviors.

Where you write logs  
**Recommended:** You write to the index alias, for example `detector-{{my-logs}}`.  
**Typical:** You write to the dated index, for example `{{my-logs}}-2026.10.08`.

How you create a new daily index  
**Recommended:** The ISM rollover action creates it after the current write index is one day old.  
**Typical:** The first record that you write after 00:00 UTC creates it.

How the new index joins the alias  
**Recommended:** Rollover creates the index already on the alias, as the write index.  
**Typical:** ISM adds the index to the alias a few minutes after you create it, without a write index. Until then, your detector doesn't see it.

Where field aliases come from  
**Recommended:** Your index template, plus the component template that Security Analytics manages.  
**Typical:** Only the component template that Security Analytics wrote the last time you saved the detector.

Retention  
**Recommended:** ISM deletes each index a fixed time after it stops being the write index.  
**Typical:** ISM deletes each index a fixed time after you create it.

## Terms
<a name="sa-ingestion-setup-terms"></a>

Index alias  
One name that points at one or more indexes. Your detector reads from it, and with this setup you configure your log shippers to write to it.

Write index  
The one index behind an alias that receives the records you write to the alias. You set it with `"is_write_index": true`.

Rollover  
Creating the next index and moving the write index to it. The previous index stays behind the alias for searches until ISM deletes it.

Field alias  
A second name for an existing field, for example `{{user-id}}` pointing at `{{source-event.user-id}}`. Detection rules use these names.

## Setting up ingestion for a detector
<a name="sa-ingestion-setup-procedure"></a>

The following procedure uses OpenSearch REST API requests, not SDK code. Send them to your domain endpoint with a REST client, or run them in **Dev Tools** in OpenSearch Dashboards. For more information, see [Using OpenSearch Dashboards with Amazon OpenSearch Service](dashboards.md). The domain endpoint is Region-specific, for example `https://search-{{my-domain}}.{{us-east-1}}.es.amazonaws.com`. The examples show only the path after the endpoint.

In every example, replace the following placeholders with your own values:
+ `{{my-logs}}` – The base name of your log source. It's used in the index names (`{{my-logs}}-*`), the alias (`detector-{{my-logs}}`), the index template, and the ISM policy.
+ `{{source-event}}` – The object in your log documents that contains the fields that your rules read.
+ `{{operation}}`, `{{result-status}}`, `{{user-id}}`, and `{{user-agent}}` – Example fields and field aliases. Replace them with every field and field alias that your log type and rules use.

**To set up ingestion for a detector**

1. **Create or update the index template.** The template keeps your existing fields and settings, and adds the following:
   + `index.plugins.index_state_management.rollover_alias` – Tells ISM which alias to roll over for indexes that it creates from this template.
   + Every field that your detector's rules read, with its type.
   + A field alias for every field name that your rules use, so that a new index never depends on the component template that Security Analytics manages.

   The following `PUT _index_template` REST API request shows the structure. Replace `{{my-logs}}`, `{{source-event}}`, and the example fields and field aliases with your own values.

   ```
   PUT _index_template/{{my-logs}}
   {
     "index_patterns": ["{{my-logs}}-*"],
     "priority": 0,
     "template": {
       "settings": {
         "index.number_of_shards": 1,
         "index.number_of_replicas": 1,
         "index.refresh_interval": "10s",
         "index.plugins.index_state_management.rollover_alias": "detector-{{my-logs}}"
       },
       "mappings": {
         "properties": {
           "@timestamp": { "type": "date" },
           "log_source":  { "type": "keyword" },
           "{{source-event}}": {
             "properties": {
               "{{operation}}":     { "type": "keyword" },
               "{{result-status}}": { "type": "keyword" },
               "{{user-id}}":       { "type": "keyword" },
               "{{user-agent}}":    { "type": "text", "fields": { "keyword": { "type": "keyword", "ignore_above": 256 } } }
             }
           },
           "{{operation}}":      { "type": "alias", "path": "{{source-event.operation}}" },
           "{{operation-name}}": { "type": "alias", "path": "{{source-event.operation}}" },
           "{{result-status}}":  { "type": "alias", "path": "{{source-event.result-status}}" },
           "{{status}}":         { "type": "alias", "path": "{{source-event.result-status}}" },
           "{{user-id}}":        { "type": "alias", "path": "{{source-event.user-id}}" },
           "{{user-agent}}":     { "type": "alias", "path": "{{source-event.user-agent}}" }
         }
       }
     }
   }
   ```

   Note the following about the template:
   + Include a field alias for every field name that an enabled rule references, including names that no current index has yet. Security Analytics skips rules whose fields are missing from the index without reporting an error.
   + When a new rule needs another field, add the field and its field alias to this template before you enable the rule.

   When you create the detector in step 5, Security Analytics creates a component template named `.opensearch-sap-alias-mappings-component-detector-{{my-logs}}`. It adds that component template to the `composed_of` list of the index template that matches your indexes. Don't remove that entry if it's present. OpenSearch applies the mappings under `template.mappings` after `composed_of`. As a result, new indexes get every field alias that you declare here, regardless of what the component template contains.

   For more information about index templates, see [Index templates](https://docs.opensearch.org/latest/im-plugin/index-templates/) on the OpenSearch website.

1. **Create the ISM policy.** The policy rolls the index over every day. It then deletes each index a fixed time after it stops being the write index. The following `PUT _plugins/_ism/policies` REST API request rolls over after one day and deletes two hours after rollover. This keeps roughly 26 hours of data behind the alias. Adjust `min_index_age` and `min_rollover_age` to match your retention requirement, and replace `{{my-logs}}` with your own value.

   ```
   PUT _plugins/_ism/policies/{{my-logs}}-rollover
   {
     "policy": {
       "description": "Roll over daily through detector-{{my-logs}}; delete 2h after rollover.",
       "default_state": "hot",
       "ism_template": [
         { "index_patterns": ["{{my-logs}}-*"], "priority": 100 }
       ],
       "states": [
         {
           "name": "hot",
           "actions": [
             { "retry": { "count": 3, "backoff": "exponential", "delay": "1m" },
               "rollover": { "min_index_age": "1d" } }
           ],
           "transitions": [
             { "state_name": "delete", "conditions": { "min_rollover_age": "2h" } }
           ]
         },
         {
           "name": "delete",
           "actions": [
             { "retry": { "count": 3, "backoff": "exponential", "delay": "1m" },
               "delete": {} }
           ],
           "transitions": []
         }
       ]
     }
   }
   ```

   The policy uses the following settings:
   + `rollover.min_index_age` – After the write index reaches this age, ISM creates the next index and moves the write index to it.
   + `min_rollover_age` – ISM deletes the previous index this long after it rolls over. Because your detector has already moved on to the new write index, the previous index only needs to stay long enough for late records and in-flight detector runs.
   + `ism_template.priority` – If an existing ISM policy already matches the same index pattern, give the new policy a higher priority so that new indexes pick it up. Indexes already under the old policy keep it and retire on their existing schedule. For more information about ISM templates, see [ISM templates](ism.md#ism-template).

   For more information about ISM policies, see [Index State Management in Amazon OpenSearch Service](ism.md).

1. **Create the first index and set the write index.** The following `PUT` REST API request creates the first index of the new series with the alias set as its write index. Replace `{{my-logs}}` with your own value.

   ```
   PUT %3C{{my-logs}}-%7Bnow%2Fd%7D-000001%3E
   {
     "aliases": {
       "detector-{{my-logs}}": { "is_write_index": true }
     }
   }
   ```

   Note the following about this request:
   + You URL-encode the index name `<{{my-logs}}-{now/d}-000001>` in the request. It creates an index such as `{{my-logs}}-2026.10.08-000001`, using the current UTC day. Each rollover creates the next one, for example `{{my-logs}}-2026.10.09-000002`. The names keep the date, and they still match the index template and the ISM template patterns.
   + `"is_write_index": true` makes this index the one that receives the records you write to the alias. Any existing dated indexes stay on the alias for searches, but you don't write to them through it.
   + From now on, ISM moves the write index on every rollover. You don't need to change the alias manually.

1. **Point ingestion at the alias.** Change the destination of your ingestion pipeline or log shipper from the dated index name to the alias, for example `detector-{{my-logs}}`. Every record, including late ones, now lands in the current write index, which your detector is always tracking.

   Do this right after step 3, so that you don't write any records to a dated index after the new series has started.

1. **Create the detector.** Create the detector in OpenSearch Dashboards or with the Security Analytics API, and set its data source to the alias (`detector-{{my-logs}}`), not to a dated index or an index pattern. Create one detector for each alias.

   When you save the detector, Security Analytics does two things:
   + It reads the field aliases from the current write index and records them against its rules. Rules whose fields are present start producing findings.
   + It writes the component template `.opensearch-sap-alias-mappings-component-detector-{{my-logs}}` from the field aliases present on the write index at that moment, and adds it to the `composed_of` list of your index template. Because you also declared every field alias in your index template, new indexes get all of them regardless of what the component template contains.

   If you later edit the detector, keep the alias as its input. For more information about creating detectors, see [Creating detectors](https://docs.opensearch.org/latest/security-analytics/sec-analytics-config/detectors-config/) on the OpenSearch website.

## Moving an existing log source to this setup
<a name="sa-ingestion-setup-cutover"></a>

If you're moving an existing log source to this setup, perform steps 1 through 5 of the preceding procedure in order. In step 5, if a detector already exists for the log source, open it in OpenSearch Dashboards, choose **Edit**, and save it without changing anything so that it re-reads the field aliases from the new write index. Keep its data source set to the alias.

The last dated index that you created under the old setup stays on the alias until your existing policy removes and deletes it on its usual schedule.

## What happens every day
<a name="sa-ingestion-setup-daily"></a>

After you complete the setup, the following cycle repeats every day without any action from you.

Throughout the day  
Your shippers write to `detector-{{my-logs}}`, and records land in the write index, for example `{{my-logs}}-2026.10.09-000002`. Your detector reads them continuously.

About one day after the last rollover  
ISM rolls over: it creates `{{my-logs}}-2026.10.10-000003` from your index template, with every field and field alias, and makes it the write index. The previous index stays on the alias.

Immediately after rollover  
New records land in the new index. Your detector tracks the new write index from its first record.

Two hours after rollover (or your configured `min_rollover_age`)  
ISM deletes the previous index.

## Verifying the setup
<a name="sa-ingestion-setup-verify"></a>

Use the following REST API requests to confirm that the setup works. Send them to your domain endpoint, and replace `{{my-logs}}` and `{{detector-id}}` with your own values.

Write index  
Run `GET _cat/aliases/detector-{{my-logs}}?v`. You should see exactly one index with `is_write_index` set to `true`.

Policy  
Run `GET _plugins/_ism/explain/{{my-logs}}-*`. New indexes should be on the `{{my-logs}}-rollover` policy in the `hot` state.

Field aliases  
Run `GET {{my-logs}}-*/_mapping/field/{{user-id,operation}}`. Each field alias should be present on every new index.

Detector health  
Run `GET _plugins/_security_analytics/alerts?alertState=ERROR&detector_id={{detector-id}}`. You should see no new error alerts.

Detection across rollover  
Review the findings for the hours around each rollover. Findings should continue through the rollover with no gap.