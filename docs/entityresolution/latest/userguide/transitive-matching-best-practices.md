

# Best practices for rule ordering
<a name="transitive-matching-best-practices"></a>

When you use transitive matching, rule ordering is critical. Follow these best practices:
+ Order rules from most specific (highest confidence) to least specific.
+ For unique identifier attributes like SSN or date of birth, arrange rules in adjacent pairs – one rule that includes the attribute and the next rule without it. This allows the system to properly handle records that lack those attributes.
+ Be aware that the number of rules affects workflow latency, because records are processed across all rule levels.