# Working with XML-Restricted Characters

You can store data in Amazon SimpleDB through the REST interface. All results are returned in XML
documents.

XML does not support certain Unicode characters (the NUL character, anything in XML's
RestrictedChar category, and permanently undefined Unicode characters). However, you can
accidentally send them through the REST API. For more information about these
characters, go to section 2.2 of the [XML 1.1
specification](http://www.w3.org/TR/xml11/ "http://www.w3.org/TR/xml11/").

To ensure that you can read all the data you sent via REST, if a response contains invalid XML
characters, Amazon SimpleDB automatically Base64-encodes the UTF-8 octets of the text.

When a returned element is Base64-encoded, its encoding element is set to `base64`.
The following example shows Base64-encoded results from a GetAttributes operation.

```
<GetAttributesResponse xmlns="http://sdb.amazonaws.com/doc/2009-04-15/">
  <GetAttributesResult>
    <Attribute>
      <Name>...</Name>
      <Value encoding="base64">...</Value>
    </Attribute>
    <Attribute>
      <Name encoding="base64">...</Name>
      <Value encoding="base64">...</Value>
    </Attribute>
  </GetAttributesResult>
 </GetAttributesResponse>
```

The following example shows a Base64-encoded result from a Select operation.

```
<SelectResponse xmlns="http://sdb.amazonaws.com/doc/2009-04-15/">
  <SelectResult>
    <Item>
      <Name>...</Name>
      <Attribute>
        <Name>...</Name>
        <Value encoding="base64">...</Value>
      </Attribute>
      <Attribute>
        <Name encoding="base64">...</Name>
        <Value encoding="base64">...</Value>
      </Attribute>
    </Item>
  </SelectResult>
 </SelectResponse>
```

When designing your application, make sure to scrub any data for invalid characters or design
your application to handle Base64-encoded results.
