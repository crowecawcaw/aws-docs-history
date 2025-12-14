**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# How AWS WAF works

You use AWS WAF to control how your protected resources respond to HTTP(S) web requests. You
do this by defining a web access control list (web ACL) and then associating it with one or more web
application resources that you want to protect. The associated resources forward incoming
requests to AWS WAF for inspection by the web ACL.

The **new console** simplifies the web ACL
configuration process. It introduces protection packs to streamline setup while maintaining full
control over your security rules.

Protection packs are the new location for web ACLs and simplify web ACL management in the
console, but they don't change the underlying web ACL functionality. When using the standard
console or the API, you'll still work directly with web ACLs.

In your protection pack (web ACL), you create rules to define traffic patterns to look for in requests and to specify the actions to take on matching requests. The action choices include the following:

- Allow the requests to go to the protected resource for processing and response.
- Block the requests.
- Count the requests.
- Run CAPTCHA or challenge checks against requests to verify human users
  and standard browser use.

###### AWS WAF components

The following are the central components of AWS WAF:

- **web ACLs** – You use a web access control list (web ACL)
  to protect a set of AWS resources. You create a web ACL and define its
  protection strategy by adding rules. Rules define criteria for inspecting
  web requests and they specify the action to take on requests that match
  their criteria. You also set a default action for the web ACL that indicates
  whether to block or allow through any requests that the rules haven't
  already blocked or allowed. For more information about web ACLs, see [Configuring protection in AWS WAF](web-acl.md "web-acl.md").

A web ACL is an AWS WAF resource.

- **Protection pack (Web ACL)s** – In the new
  console, protection packs are the new location for your web ACLs. During setup, you provide
  information about your apps and resources. AWS WAF reccomends a protection pack tailored to
  your scenario, and then creates a web ACL that contains rules, rule groups, and actions
  defined by the protection pack (web ACL) you choose. For more information about
  protection packs (web ACLs), see [Configuring protection in AWS WAF](web-acl.md "web-acl.md").

A protection pack (web ACL) is an AWS WAF resource.

- **Rules** – Each rule contains a statement that
  defines the inspection criteria, and an action to take if a web request
  meets the criteria. When a web request meets the criteria, that's a match.
  You can configure rules to block matching requests, allow them through,
  count them, or run bot controls against them that use CAPTCHA puzzles or
  silent client browser challenges. For more information about rules, see
  [AWS WAF rules](waf-rules.md "waf-rules.md").

A rule is not an AWS WAF resource. It only exists in the context of a protection pack (web ACL) or rule group.

- **Rule groups** – You can define rules directly inside
  a protection pack (web ACL) or in reusable rule groups. AWS Managed Rules and AWS Marketplace sellers provide
  managed rule groups for your use. You can also define your own rule groups.
  For more information about rule groups, see [AWS WAF rule groups](waf-rule-groups.md "waf-rule-groups.md").

A rule group is an AWS WAF resource.

- **web ACL capacity units (WCUs)** – AWS WAF uses
  WCUs to calculate and control the operating resources that are required to run your rules, rule groups, protection packs (web ACLs), or web ACLs.

A WCU is not an AWS WAF resource. It only exists in the context of a protection pack (web ACL), rule, or rule group.

## Understanding the new dashboards

Dashboards available through new provide unified visibility into your security
posture through these visualizations:

**Traffic insight recommendations** – AWS Threat
Intelligence monitors your previous 2 weeks of allowed traffic, analyzes
vulnerabilities, and provides the following:

- Traffic-based rule suggestions
- Application-specific security recommendations
- Protection optimization guidance

**Summary** – Shows request counts for all traffic
during a specified time range. You can use the following criteria to filter
traffic data:

- **Rule** – Filter by the individual
  rules in the protection pack.
- **Actions** – Show counts for specific
  actions taken on traffic like Allow, Block, Captcha, and
  Challenge.
- **Traffic type** – Only show counts
  for specific traffic types like anti-DDoS or bots.
- **Time range** – Choose from a
  selection of predefined time ranges, or set a custom range.
- **Local or UTC time** – You can set
  your preferred time format.

**Protection activity** – Visualizes your protection rules
and how their order contributes to terminating actions.

- **Traffic flow through your rules** – Show the
  traffic flow through your rules. Switch from
  **Sequential rules view** to
  **Non-sequential rules view** to see how
  rule order affects outcomes.
- **Rule actions and their outcomes** – Shows the
  terminating actions that a rule took on traffic in the specified
  time period.

**Action totals** – A chart that visualizes the
total number of actions taken on requests during a specified time range.
Use the **Overlay last 3 hours** option to compare the
current time range with the previous 3 hour time window. You can filter data
by:

- **Allow action**
- **Total actions**
- **Captcha actions**
- **Challenge actions**
- **Block actions**

**All rules** – A chart that visualizes metrics
for all rules in the protection pack.

- Use the **Overlay last 3 hours** option to
  compare the current time range with the previous 3 hour time
  window.

**Overview Dashboard** – Provides a comprehensive,
graphical view of your security status, including the following:

- **Traffic characteristics** – See an
  overview of traffic by origin, attack types, or by the device
  type of the clients that sent requests.
- **Rule characteristics** – A breakdown
  of attacks by the 10 most common rules and termnating
  actions.
- **Bots** – Visualize bot activity,
  detection, categories, and bot-related signal labels.
- **Anti-DDoS** – An overview of
  detected and mitigated layer 7 DDoS activity.
