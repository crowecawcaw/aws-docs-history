

# Considerations
<a name="next-gen-insights-considerations"></a>
+ Dependency insights highlights patterns and potential risks. It does not prescribe specific fixes. Validate each insight against your application before acting on it.
+ For services with a large number of dependencies, insights prioritize the most significant patterns and risks rather than listing every dependency. A dependency might not appear in the summary even though it still appears in the full dependency list.
+ Insights are generated from discovered dependency data. Dependencies that are not captured by Dependency discovery – for example, direct IP connections – are not reflected. For more information, see [Coverage and known limitations](next-gen-discovery-limitations.md).
+ You can regenerate insights once every 24 hours per service.