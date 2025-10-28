# Tags

The following discussion applies to tags defined for grammars. For
more information, see [Tags](https://www.w3.org/TR/speech-grammar/#S2.6 "https://www.w3.org/TR/speech-grammar/#S2.6") in the _Speech recognition grammar
specification version 1_ W3C recommendation.

Based on the SRGS specification, tags can be defined in the
following ways:

1. As part of a header declaration as described in [Header declarations](srgs-header.md "srgs-header.md").
2. As part of a _<rule>_
   definition.
   The following tag formats are supported:

- `semantics/1.0` (SISR, ECMAScript)
- `semantics/1.0-literals` (SISR string
  literals)
  The following tag formats are not supported:

- `swi-semantics/1.0` (Nuance
  proprietary)
  **Example**

```
<grammar xmlns="http://www.w3.org/2001/06/grammar"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xml:base="http://www.example.com/base-file-path"
         xsi:schemaLocation="http://www.w3.org/2001/06/grammar
                             http://www.w3.org/TR/speech-grammar/grammar.xsd"
         xml:lang="en-US"
         version="1.0"
         mode="voice"
         root="city"
         tag-format="semantics/1.0-literals">
    <rule id="no">
        <one-of>
            <item>no</item>
            <item>nope</item>
            <item>no way</item>
        </one-of>
        <tag>no</tag>
    </rule>
</grammar>

```
