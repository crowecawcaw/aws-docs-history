# Grammar definition

This topic shows the parts of the SRGS specification that Amazon Lex V2
supports. All of the rules are defined in the SRGS specification.
For more information, see the [Speech recognition
grammar specification version 1.0](https://www.w3.org/TR/speech-grammar/ "https://www.w3.org/TR/speech-grammar/") W3C
recommendation.

###### Topics

- [Header declarations](srgs-header.md "srgs-header.md")
- [Supported XML elements](srgs-supported-xml.md "srgs-supported-xml.md")
- [Tokens](srgs-tokens.md "srgs-tokens.md")
- [Rule reference](srgs-rule-reference.md "srgs-rule-reference.md")
- [Sequences and
  encapsulation](srgs-sequence.md "srgs-sequence.md")
- [Repeats](srgs-repeats.md "srgs-repeats.md")
- [Language](srgs-language.md "srgs-language.md")
- [Tags](srgs-tags.md "srgs-tags.md")
- [Weights](grammar-weights.md "grammar-weights.md")
  This document includes material copied and derived from the W3C
  Speech Recognition Grammar Specification Version 1.0 (available at
  [https://www.w3.org/TR/speech-grammar/](https://www.w3.org/TR/speech-grammar/ "https://www.w3.org/TR/speech-grammar/")). Citation
  information follows:

[Copyright](http://www.w3.org/Consortium/Legal/ipr-notice#Copyright "http://www.w3.org/Consortium/Legal/ipr-notice#Copyright") © 2004 [W3C®](http://www.w3.org/ "http://www.w3.org/") ([MIT](http://www.csail.mit.edu/ "http://www.csail.mit.edu/"), [ERCIM](http://www.ercim.org/ "http://www.ercim.org/"),
[Keio](http://www.keio.ac.jp/ "http://www.keio.ac.jp/"), All Rights
Reserved. W3C [liability](http://www.w3.org/Consortium/Legal/ipr-notice#Legal_Disclaimer "http://www.w3.org/Consortium/Legal/ipr-notice#Legal_Disclaimer"), [trademark](http://www.w3.org/Consortium/Legal/ipr-notice#W3C_Trademarks "http://www.w3.org/Consortium/Legal/ipr-notice#W3C_Trademarks"), [document use](http://www.w3.org/Consortium/Legal/copyright-documents "http://www.w3.org/Consortium/Legal/copyright-documents") and [software licensing](http://www.w3.org/Consortium/Legal/copyright-software "http://www.w3.org/Consortium/Legal/copyright-software") rules apply.

The SRGS specification document, a [W3C Recommendation](https://www.w3.org/2004/02/Process-20040205/tr.html#RecsW3C "https://www.w3.org/2004/02/Process-20040205/tr.html#RecsW3C"), is available from the W3C under the
following license.

License

By using and/or copying this document, or the W3C document
from which this statement is linked, you (the licensee)
agree that you have read, understood, and will comply with
the following terms and conditions:

Permission to copy, and distribute the contents of this
document, or the W3C document from which this statement is
linked, in any medium for any purpose and without fee or
royalty is hereby granted, provided that you include the
following on ALL copies of the document, or portions
thereof, that you use:

- A link or URL to the original W3C document.
- The pre-existing copyright notice of the original
  author, or if it doesn't exist, a notice (hypertext
  is preferred, but a textual representation is
  permitted) of the form: "Copyright ©
  [$date-of-document] [World Wide Web Consortium](http://www.w3.org/ "http://www.w3.org/"), ([MIT](http://www.csail.mit.edu/ "http://www.csail.mit.edu/"),
  [ERCIM](http://www.ercim.org/ "http://www.ercim.org/"), [Keio](http://www.keio.ac.jp/ "http://www.keio.ac.jp/"), [Beihang](http://ev.buaa.edu.cn/ "http://ev.buaa.edu.cn/")).
  [http://www.w3.org/Consortium/Legal/2015/doc-license](http://www.w3.org/Consortium/Legal/2015/doc-license "http://www.w3.org/Consortium/Legal/2015/doc-license")"
- _If it exists_, the STATUS of
  the W3C document.
  When space permits, inclusion of the full text of this
  **NOTICE** should be
  provided. We request that authorship attribution be provided
  in any software, documents, or other items or products that
  you create pursuant to the implementation of the contents of
  this document, or any portion thereof.

No right to create modifications or derivatives of W3C
documents is granted pursuant to this license, except as
follows: To facilitate implementation of the technical
specifications set forth in this document, anyone may
prepare and distribute derivative works and portions of this
document in software, in supporting materials accompanying
software, and in documentation of software, PROVIDED that
all such works include the notice below. HOWEVER, the
publication of derivative works of this document for use as
a technical specification is expressly prohibited.

In addition, "Code Components" —Web IDL in sections
clearly marked as Web IDL; and W3C-defined markup (HTML,
CSS, and so on) and computer programming language code clearly
marked as code examples— are licensed under the [W3C Software License](http://www.w3.org/Consortium/Legal/copyright-software "http://www.w3.org/Consortium/Legal/copyright-software").

The notice is:

"Copyright © 2015 W3C® (MIT, ERCIM, Keio,
Beihang). This software or document includes material copied
from or derived from [title and URI of the W3C
document]."

Disclaimers

THIS DOCUMENT IS PROVIDED "AS IS," AND COPYRIGHT HOLDERS
MAKE NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED,
INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE,
NON-INFRINGEMENT, OR TITLE; THAT THE CONTENTS OF THE
DOCUMENT ARE SUITABLE FOR ANY PURPOSE; NOR THAT THE
IMPLEMENTATION OF SUCH CONTENTS WILL NOT INFRINGE ANY THIRD
PARTY PATENTS, COPYRIGHTS, TRADEMARKS OR OTHER
RIGHTS.

COPYRIGHT HOLDERS WILL NOT BE LIABLE FOR ANY DIRECT,
INDIRECT, SPECIAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF
ANY USE OF THE DOCUMENT OR THE PERFORMANCE OR IMPLEMENTATION
OF THE CONTENTS THEREOF.

The name and trademarks of copyright holders may NOT be
used in advertising or publicity pertaining to this document
or its contents without specific, written prior permission.
Title to copyright in this document will at all times remain
with copyright holders.
