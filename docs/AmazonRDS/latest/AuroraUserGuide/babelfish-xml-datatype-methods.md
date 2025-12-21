# Babelfish supports XML datatype methods

Starting with version 5.4.0, Babelfish now supports stored procedures sp_xml_preparedocument and sp_xml_removedocument, rowset function OPENXML() and xml dataype method .VALUE(). With these functions and procedures querying on XML data becomes much easier.

## Understanding XML procedures and methods

- sp_xml_preparedocument – The procedure sp_xml_preparedocument parses an XML text given as input and returns a handle to this document. This handle is valid during the session or until it is removed by sp_xml_removedocument.
- sp_xml_removedocument – The procedure sp_xml_removedocument invalidates the handle which was created by procedure sp_xml_preparedocument.
- OPENXML() – OPENXML provides a rowset view over an XML document. Since OPENXML is a rowset provider and it returns a set of rows, we can use OPENXML in the FROM clause just as we can use any other table, view, or table-valued function.
- VALUE() – XML Datatype method VALUE() is used to extract a value from an XML instance stored in an xml type column, parameter, or variable.

## Limitations in Babelfish XML procedures and methods

- Babelfish only supports XPATH 1.0 syntax for second argument (i.e. ROWPATTERN) of OPENXML().
- The meta-properties and flag 8 are not currently not supported in OPENXML().
- Babelfish only supports XPATH 1.0 syntax for first argument (i.e. XQuery) of VALUE() datatype method.
