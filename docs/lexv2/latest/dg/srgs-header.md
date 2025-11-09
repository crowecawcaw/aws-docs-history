# Header declarations

The following table shows the header declarations supported by
the grammar slot type. For more information, see [Grammar
header declarations](https://www.w3.org/TR/speech-grammar/#S4.1 "https://www.w3.org/TR/speech-grammar/#S4.1") in the _Speech
recognition grammar specification version 1_ W3C
recommendation.

| Declaration           | Specification requirement                      | XML form                                                                                                                                          | Amazon Lex support                                 | Specification |
| --------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------- |
| Grammar version       | Required                                       | [4.3](https://www.w3.org/TR/speech-grammar/#S4.3 "https://www.w3.org/TR/speech-grammar/#S4.3"): `version` attribute<br>on `grammar` element       | Required                                           | SRGS          |
| XML namespace         | Required (XML only)                            | [4.3](https://www.w3.org/TR/speech-grammar/#S4.3 "https://www.w3.org/TR/speech-grammar/#S4.3"): `xmlns` attribute<br>on `grammar` element         | Required                                           | SRGS          |
| Document type         | Required (XML only)                            | [4.3](https://www.w3.org/TR/speech-grammar/#S4.3 "https://www.w3.org/TR/speech-grammar/#S4.3"): XML DOCTYPE                                       | Recommended                                        | SRGS          |
| Character encoding    | Recommended                                    | [4.4](https://www.w3.org/TR/speech-grammar/#S4.4 "https://www.w3.org/TR/speech-grammar/#S4.4"): `encoding`<br>attribute in XML declaration        | Recommended                                        | SRGS          |
| Language              | Required in voice mode<br>Ignored in DTMF mode | [4.5](https://www.w3.org/TR/speech-grammar/#S4.5 "https://www.w3.org/TR/speech-grammar/#S4.5"): `xml:lang`<br>attribute on `grammar`<br>element   | Required in voice mode<br>Ignored in DTMF mode     | SRGS          |
| Mode                  | Optional                                       | [4.6](https://www.w3.org/TR/speech-grammar/#S4.6 "https://www.w3.org/TR/speech-grammar/#S4.6"): `mode` attribute on<br>`grammar` element          | Optional                                           | SRGS          |
| Root rule             | Optional                                       | [4.7](https://www.w3.org/TR/speech-grammar/#S4.7 "https://www.w3.org/TR/speech-grammar/#S4.7"): `root` attribute on<br>`grammar` element          | **Required**                                       | SRGS          |
| Tag format            | Optional                                       | [4.8](https://www.w3.org/TR/speech-grammar/#S4.8 "https://www.w3.org/TR/speech-grammar/#S4.8"): `tag-format`<br>attribute on `grammar`<br>element | **String literal and<br>ECMAScript are supported** | SRGS, SISR    |
| Base URI              | Optional                                       | [4.9](https://www.w3.org/TR/speech-grammar/#S4.9 "https://www.w3.org/TR/speech-grammar/#S4.9"): `xml:base`<br>attribute on `grammar`<br>element   | Optional                                           | SRGS          |
| Pronunciation lexicon | Optional, multiple allowed                     | [4.10](https://www.w3.org/TR/speech-grammar/#S4.`0 "https://www.w3.org/TR/speech-grammar/#S4.`0"): `lexicon`<br>element                           | **Not<br>supported**                               | SRGS, PLS     |
| Metadata              | Optional, multiple allowed                     | [4.11.1](https://www.w3.org/TR/speech-grammar/#S4.11.1 "https://www.w3.org/TR/speech-grammar/#S4.11.1"): `meta`<br>element                        | Required                                           | SRGS          |
| XML metadata          | Optional, XML only                             | [4.11.2](https://www.w3.org/TR/speech-grammar/#S4.11.2 "https://www.w3.org/TR/speech-grammar/#S4.11.2"): `metadata`<br>element                    | Optional                                           | SRGS          |
| Tag                   | Optional, multiple allowed                     | [4.12](https://www.w3.org/TR/speech-grammar/#S4.12 "https://www.w3.org/TR/speech-grammar/#S4.12"): `tag`<br>element                               | **Global tags not<br>supported**                   | SRGS          |

**Example**

```
<?xml version="1.0" encoding="ISO-8859-1"?>

<!DOCTYPE grammar PUBLIC "-//W3C//DTD GRAMMAR 1.0//EN"
                  "http://www.w3.org/TR/speech-grammar/grammar.dtd">

<grammar xmlns="http://www.w3.org/2001/06/grammar"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xml:base="http://www.example.com/base-file-path"
         xsi:schemaLocation="http://www.w3.org/2001/06/grammar
                             http://www.w3.org/TR/speech-grammar/grammar.xsd"
         xml:lang="en-US"
         version="1.0"
         mode="voice"
         root="city"
         tag-format="semantics/1.0">

```
