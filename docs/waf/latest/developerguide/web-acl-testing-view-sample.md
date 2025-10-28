**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Viewing a sample of web requests

This section describes the protection pack (web ACL) **Sampled requests** tab in
the AWS WAF console. In this tab, you can view a graph of all of the rule matches for
web requests that AWS WAF has inspected. Additionally, if you have request sampling
enabled for the protection pack (web ACL), you can see a table view of a sample of the web requests that AWS WAF has
inspected. You can also retrieve sampled request information through the API call `GetSampledRequests`.

The sample of requests contains up to 100 requests that matched the criteria for a rule in
the protection pack (web ACL) and another 100 requests for requests that didn't match any rules and had
the protection pack (web ACL) default action applied. The requests in the sample come from all the
protected resources that have received requests for your content in the previous three
hours.

When a web request matches the criteria in a rule and the action for that rule doesn't
terminate the request evaluation, AWS WAF continues inspecting the web request using
the subsequent rules in the protection pack (web ACL). Because of this, a web request could appear
multiple times. For information about rule action behaviors, see [Using rule actions in AWS WAF](waf-rule-action.md "waf-rule-action.md").

###### To view the all rules graph and sampled requests

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. In the navigation pane, choose **protection packs (web ACLs)**.
3. Choose the name of the protection pack (web ACL) for which you want to view requests.
   The console takes you to the protection pack (web ACL)'s description, where you can edit it.
4. In the **Sampled requests** tab, you can see the following:
   - **All rules graph** – This
     graph shows the matching rules and rule actions for all web request
     evaluations that were performed during the indicated time range.

   ###### Note

   The time range for this graph is set in the protection pack (web ACL)'s **Traffic
   overview** tab, in the **Data
   filters** section. For information, see [Viewing the dashboards for a protection pack (web ACL)](web-acl-dashboards-accessing.md "web-acl-dashboards-accessing.md").
   - **Sampled requests table** –
     This table displays sampled request data for the last 3 hours.

   ###### Note

   If you aren't seeing the samples that you expect for a managed rule group,
   see the section below this procedure.

   For each entry, the table displays the following data:

   **Metric name**

   The CloudWatch metric name for the rule in the protection pack (web ACL) that
   matched the request. If a web request doesn't match any
   rule in the protection pack (web ACL), this value is
   **Default**.

   ###### Note

   If you change the name of a rule and you want the rule's metric name to reflect the change, you
   must update the metric name as well. AWS WAF doesn't automatically update the metric name for a rule when you change the rule name.
   You can change the metric name when you edit the
   rule in the console, by using the rule JSON editor. You can also change both names through the APIs and in any JSON listing that you
   use to define your protection pack (web ACL) or rule group.

   **Source IP**

   Either the IP address that the request originated from
   or, if the viewer used an HTTP proxy or an Application Load Balancer to send
   the request, the IP address of the proxy or Application Load Balancer.

   **URI**

   The part of a URL that identifies a resource, for
   example, `/images/daily-ad.jpg`.

   **Rule inside rule group**

   If the metric name identifies a rule group reference
   statement, this identifies the rule inside the rule
   group that matched the request.

   **Action**

   Indicates the action for the corresponding rule. For
   information about the possible rule actions, see [Using rule actions in AWS WAF](waf-rule-action.md "waf-rule-action.md").

   **Time**

   The time that AWS WAF received the request from the
   protected resource.

   To display additional information about the components of a web
   request, choose the name of the URI in the row of the
   request.

###### Sampled requests for rules in managed rule groups

In the console, sampled requests are available for managed rule group rules only if they
either don't have action overrides or if the action overrides use the most recent override configuration setting,
`RuleActionOverrides`. Rule action overrides that use the older `ExcludedRules` setting are not available through the console.
If you're not seeing all of the managed rule group request samples that you expect, check your protection pack (web ACL)
JSON for overrides that use the older setting. You can download the JSON from the protection pack (web ACL)'s console page.

If you see the older settings, replace them with the new settings to start making the sampled
requests available through the console. You can do this through the console by editing
the managed rule group in the protection pack (web ACL) and saving it. AWS WAF
automatically replaces any older settings with the `RuleActionOverrides` settings and sets the
rule action override to Count.
For more information about these two settings, see [JSON listing: RuleActionOverrides replaces ExcludedRules](web-acl-rule-group-override-options.md#web-acl-rule-group-override-replaces-exclude "web-acl-rule-group-override-options.md#web-acl-rule-group-override-replaces-exclude").

You can access sampled requests for a rule that has the old override in place
through the AWS WAF REST API, SDKs, or command line. For information, see
[GetSampledRequests](../APIReference/API_GetSampledRequests.md "../APIReference/API_GetSampledRequests.md")
in the _AWS WAF API Reference_.

The following shows the syntax for the command line request:

```
aws wafv2 get-sampled-requests \
  --web-acl-arn `webACL ARN` \
  --rule-metric-name `Metric name of the rule in the managed rule group` \
  --scope=`REGIONAL or CLOUDFRONT` \
  --time-window StartTime=`UTC timestamp`,EndTime=`UTC timestamp` \
  --max-items 100
```
