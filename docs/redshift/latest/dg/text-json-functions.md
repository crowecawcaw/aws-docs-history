

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Text-based JSON functions
<a name="text-json-functions"></a>

The functions in this section parse JSON values as VARCHAR. For parsing JSON, we recommend you instead use the following functions, which parse JSON values as SUPER. Amazon Redshift parses SUPER values more efficiently than VARCHAR.
+  [JSON\_PARSE function](JSON_PARSE.md) 
+  [CAN\_JSON\_PARSE function](CAN_JSON_PARSE.md) 
+  [JSON\_SERIALIZE function](JSON_SERIALIZE.md) 
+  [JSON\_SERIALIZE\_TO\_VARBYTE function](JSON_SERIALIZE_TO_VARBYTE.md) 

**Topics**
+ [IS\_VALID\_JSON function](IS_VALID_JSON.md)
+ [IS\_VALID\_JSON\_ARRAY function](IS_VALID_JSON_ARRAY.md)
+ [JSON\_ARRAY\_LENGTH function](JSON_ARRAY_LENGTH.md)
+ [JSON\_EXTRACT\_ARRAY\_ELEMENT\_TEXT function](JSON_EXTRACT_ARRAY_ELEMENT_TEXT.md)
+ [JSON\_EXTRACT\_PATH\_TEXT function](JSON_EXTRACT_PATH_TEXT.md)