

# Babelfish supports XML datatype methods
<a name="babelfish-xml-datatype-methods"></a>

Starting with version 4.4.0, Babelfish now supports the xml datatype method .EXIST().

Starting with version 5.4.0, Babelfish now supports stored procedures sp\_xml\_preparedocument and sp\_xml\_removedocument, rowset function OPENXML() and xml datatype method .VALUE().

Starting with version 5.7.0, Babelfish now supports the xml datatype method .QUERY().

With these functions and procedures querying on XML data becomes much easier.

## Understanding XML procedures and methods
<a name="babelfish-xml-datatype-methods-overview"></a>
+ **sp\_xml\_preparedocument** – The procedure sp\_xml\_preparedocument parses an XML text given as input and returns a handle to this document. This handle is valid during the session or until it is removed by sp\_xml\_removedocument.
+ **sp\_xml\_removedocument** – The procedure sp\_xml\_removedocument invalidates the handle which was created by procedure sp\_xml\_preparedocument.
+ **OPENXML()** – OPENXML provides a rowset view over an XML document. Since OPENXML is a rowset provider and it returns a set of rows, we can use OPENXML in the FROM clause just as we can use any other table, view, or table-valued function.
+ **EXIST()** – XML Datatype method EXIST() is used to check whether an XQuery expression returns a nonempty result against an XML instance, and returns a bit (1 for true, 0 for false).
+ **VALUE()** – XML Datatype method VALUE() is used to extract a value from an XML instance.
+ **QUERY()** – XML Datatype method QUERY() is used to query an XML instance and returns the result as untyped XML.

## Limitations in Babelfish XML procedures and methods
<a name="babelfish-xml-datatype-methods-limitations"></a>
+ Babelfish only supports XPATH 1.0 syntax for second argument (that is, ROWPATTERN) of OPENXML().
+ The meta-properties and flag 8 are not currently supported in OPENXML().
+ Babelfish only supports XPATH 1.0 syntax for the XQuery argument of the EXIST(), VALUE() and QUERY() datatype methods.
+ XML datatype methods EXIST(), VALUE() and QUERY() require the XML instance to be a well-formed XML document (single root element), invoking them on an XML content (multiple top-level elements) is currently not supported. This difference is due to a more strict handling of XML documents in PostgreSQL.