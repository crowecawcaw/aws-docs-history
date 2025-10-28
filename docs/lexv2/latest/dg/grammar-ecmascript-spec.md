# Script format

Amazon Lex V2 supports the following ECMAScript features for defining
grammars.

Amazon Lex V2 supports the following ECMAScript features when specifying
tags in the grammar. `tag-format` must be sent to
`semantics/1.0` when ECMAScript tags are used in the
grammar. For more information, see the [ECMA-262 ECMAScript 2021 language specification](https://www.ecma-international.org/publications-and-standards/standards/ecma-262/ "https://www.ecma-international.org/publications-and-standards/standards/ecma-262/") .

```
<grammar version="1.0"
xmlns="http://www.w3.org/2001/06/grammar"
xml:lang="en-US"
tag-format="semantics/1.0"
root="card_number">
```

###### Topics

- [Variable statement](ecma-variable.md "ecma-variable.md")
- [Expressions](ecma-expression.md "ecma-expression.md")
- [If statement](ecma-if.md "ecma-if.md")
- [Switch statement](ecma-switch.md "ecma-switch.md")
- [Function declarations](ecma-function.md "ecma-function.md")
- [Iteration statement](ecma-iteration.md "ecma-iteration.md")
- [Block statement](ecma-block.md "ecma-block.md")
- [Comments](ecma-comments.md "ecma-comments.md")
- [Unsupported
  statements](ecma-unsupported.md "ecma-unsupported.md")
  This document contains material from the ECMAScript standard
  (available at [https://www.ecma-international.org/publications-and-standards/standards/ecma-262/](https://www.ecma-international.org/publications-and-standards/standards/ecma-262/ "https://www.ecma-international.org/publications-and-standards/standards/ecma-262/") ). The ECMAScript language specification document is
  available from Ecma International under the following
  license.

© 2020 Ecma International

This document may be copied, published and distributed to
others, and certain derivative works of it may be prepared,
copied, published, and distributed, in whole or in part,
provided that the above copyright notice and this Copyright
License and Disclaimer are included on all such copies and
derivative works. The only derivative works that are
permissible under this Copyright License and Disclaimer are:

(i) works which incorporate all or portion of this
document for the purpose of providing commentary or
explanation (such as an annotated version of the document),

(ii) works which incorporate all or portion of this
document for the purpose of incorporating features that
provide accessibility,

(iii) translations of this document into languages other
than English and into different formats and

(iv) works by making use of this specification in standard
conformant products by implementing (for example, by copy and paste
wholly or partly) the functionality therein.

However, the content of this document itself may not be
modified in any way, including by removing the copyright
notice or references to Ecma International, except as
required to translate it into languages other than English
or into a different format.

The official version of an Ecma International document is
the English language version on the Ecma International
website. In the event of discrepancies between a translated
version and the official version, the official version shall
govern.

The limited permissions granted above are perpetual and
will not be revoked by Ecma International or its successors
or assigns. This document and the information contained
herein is provided on an "AS IS" basis and ECMA
INTERNATIONAL DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF
THE INFORMATION HEREIN WILL NOT INFRINGE ANY OWNERSHIP
RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR
FITNESS FOR A PARTICULAR PURPOSE."
