# Count referrers, IP addresses, or matched rules

The examples in this section query for counts of log items of interest.

- [Count the number of referrers that contain a specified term](#waf-example-count-referrers-with-specified-term "#waf-example-count-referrers-with-specified-term")
- [Count all matched IP addresses in the last 10 days that have matched excluded rules](#waf-example-count-matched-ip-addresses "#waf-example-count-matched-ip-addresses")
- [Group all counted managed rules by the number of times matched](#waf-example-group-managed-rules-by-times-matched "#waf-example-group-managed-rules-by-times-matched")
- [Group all counted custom rules by number of times matched](#waf-example-group-custom-rules-by-times-matched "#waf-example-group-custom-rules-by-times-matched")

###### Example – Count the number of referrers that contain a specified term

The following query counts the number of referrers that contain the term "amazon"
for the specified date range.

```
WITH test_dataset AS
  (SELECT header FROM waf_logs
    CROSS JOIN UNNEST(httprequest.headers) AS t(header) WHERE "date" >= '2021/03/01'
    AND "date" < '2021/03/31')
SELECT COUNT(*) referer_count
FROM test_dataset
WHERE LOWER(header.name)='referer' AND header.value LIKE '%amazon%'
```

###### Example – Count all matched IP addresses in the last 10 days that have matched excluded rules

The following query counts the number of times in the last 10 days that the IP
address matched the excluded rule in the rule group.

```
WITH test_dataset AS
  (SELECT * FROM waf_logs
    CROSS JOIN UNNEST(rulegrouplist) AS t(allrulegroups))
SELECT
  COUNT(*) AS count,
  "httprequest"."clientip",
  "allrulegroups"."excludedrules",
  "allrulegroups"."ruleGroupId"
FROM test_dataset
WHERE allrulegroups.excludedrules IS NOT NULL AND from_unixtime(timestamp/1000) > now() - interval '10' day
GROUP BY "httprequest"."clientip", "allrulegroups"."ruleGroupId", "allrulegroups"."excludedrules"
ORDER BY count DESC
```

###### Example – Group all counted managed rules by the number of times matched

If you set rule group rule actions to Count in your web ACL configuration before
October 27, 2022, AWS WAF saved your overrides in the web ACL JSON as
`excludedRules`. Now, the JSON setting for overriding a rule to Count
is in the `ruleActionOverrides` settings. For more information, see
[Action
overrides in rule groups](../../../waf/latest/developerguide/web-acl-rule-group-override-options.md "../../../waf/latest/developerguide/web-acl-rule-group-override-options.md") in the _AWS WAF Developer Guide_. To extract managed rules in Count mode from the new
log structure, query the `nonTerminatingMatchingRules` in the
`ruleGroupList` section instead of the `excludedRules`
field, as in the following example.

```
SELECT
 count(*) AS count,
 httpsourceid,
 httprequest.clientip,
 t.rulegroupid,
 t.nonTerminatingMatchingRules
FROM "waf_logs"
CROSS JOIN UNNEST(rulegrouplist) AS t(t)
WHERE action <> 'BLOCK' AND cardinality(t.nonTerminatingMatchingRules) > 0
GROUP BY t.nonTerminatingMatchingRules, action, httpsourceid, httprequest.clientip, t.rulegroupid
ORDER BY "count" DESC
Limit 50
```

###### Example – Group all counted custom rules by number of times matched

The following query groups all counted custom rules by the number of times
matched.

```
SELECT
  count(*) AS count,
         httpsourceid,
         httprequest.clientip,
         t.ruleid,
         t.action
FROM "waf_logs"
CROSS JOIN UNNEST(nonterminatingmatchingrules) AS t(t)
WHERE action <> 'BLOCK' AND cardinality(nonTerminatingMatchingRules) > 0
GROUP BY t.ruleid, t.action, httpsourceid, httprequest.clientip
ORDER BY "count" DESC
Limit 50
```

For information about the log locations for custom rules and managed rule groups, see
[Monitoring and
tuning](../../../waf/latest/developerguide/web-acl-testing-activities.md "../../../waf/latest/developerguide/web-acl-testing-activities.md") in the _AWS WAF Developer Guide_.
