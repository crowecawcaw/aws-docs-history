

# Dependency insights
<a name="next-gen-dependency-insights"></a>

After Dependency discovery is enabled, a single service can have hundreds of discovered dependencies, and reviewing that list manually to find resilience risks is time consuming. With Dependency insights, a generative AI-powered capability, you can highlight meaningful patterns across your discovered dependencies and address resilience risks without manually reviewing the full dependency list. Use Dependency insights when a service has accumulated more dependencies than you can practically review by hand.

Dependency insights produces a short summary that surfaces the following:
+ **Cross-Region dependencies** – Dependencies that resolve in a different AWS Region than the caller, which add latency and increase blast radius if the remote Region degrades.
+ **New dependencies** – Dependencies that first appeared in the last 7 days, so that you can confirm they are intentional and validate them for resilience before traffic scales.
+ **Third-party dependencies** – Non-AWS dependencies, such as Datadog, PagerDuty, or Stripe, which carry availability risk outside your control.
+ **Uneven usage patterns** – Dependencies with strong day-of-week or time-of-day variance, which may indicate undocumented scheduled jobs or batch tasks.

To keep the summary focused, Dependency insights filters out common AWS service noise – such as CloudWatch, NTP, and SSM – that does not typically indicate a resilience risk.

**Note**  
Dependency insights is available only for services that have Dependency discovery enabled and have completed an initial discovery run. For more information, see [Enabling dependency discovery for a service](next-gen-enabling-discovery.md).