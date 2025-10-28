Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# HLLSKETCH type

Use the HLLSKETCH data type for HyperLogLog sketches. Amazon Redshift supports
HyperLogLog sketch representations that are either sparse or dense. Sketches begin
as sparse and switch to dense when the dense format is more efficient to minimize
the memory footprint that is used.

Amazon Redshift automatically transitions a sparse HyperLogLog sketch when importing,
exporting, or printing sketches in the following JSON format.

```
{"logm":15,"sparse":{"indices":[4878,9559,14523],"values":[1,2,1]}}
```

Amazon Redshift uses a string representation in a Base64 format to represent a dense
HyperLogLog sketch.

Amazon Redshift uses the following string representation in a Base64 format to
represent a dense HyperLogLog sketch.

```
"ABAABA..."
```

The maximum size of a HLLSKETCH object is 24,580 bytes when used in raw
compression.
