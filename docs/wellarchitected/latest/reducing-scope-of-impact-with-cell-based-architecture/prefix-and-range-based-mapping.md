

# Prefix and range-based mapping
<a name="prefix-and-range-based-mapping"></a>

 Prefix and range-based mapping map ranges of keys (or hashes of keys) to cells, and serves to offset the downsides of the full mapping approach while providing flexibility. 

![Diagram showing prefix and range-based mapping](http://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/images/prefix-and-range-based-mapping.jpg)


 Depending on the granularity of your service, you can further reduce the cardinality by making ranges of groups of keys. 

![Diagram showing making ranges as groups of keys](http://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/images/ranges-as-groups-of-keys.jpg)


 Advantages: 
+  Reduces the performance issue of full mapping, by grouping key and reducing the total cardinality. 

 Disadvantages: 
+  More likely to have a hot cell, as there is no control over which keys within each range might have the most traffic.