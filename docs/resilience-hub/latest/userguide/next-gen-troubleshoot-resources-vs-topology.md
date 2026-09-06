

# Difference between discovered resources and topology resources
<a name="next-gen-troubleshoot-resources-vs-topology"></a>

You might see more resources in the `ListResources` API response than appear in your topology diagram. Not all discovered resources appear in the topology view. The topology is a connectivity graph that shows how resources interact. Next generation Resilience Hub removes resources from the topology view that have no connections to other resources.