# Creating a custom terminology

You define custom terminology by creating a terminology file. Amazon Translate supports CSV, TSV, or
TMX file formats. Each entry in the file contains the source term and the equivalent
(translated) term for each target language.

After you create a terminology file, you upload the file to your Amazon Translate account.

###### Important

The source text in a custom terminology is _case-sensitive_. During
translation, Amazon Translate uses the custom terminology when it finds an exact match in the input
document.

## Terminology file formats

The following example shows a terminology file in CSV format.

**CSV (comma separated values)**

```
en,fr,es
Amazon Photos,Amazon Photos,Amazon Photos
```

The following example shows a terminology file in TMX format. A TMX file uses an XML
format that translation software often uses.

**TMX (Translation Memory eXchange)**

```
<?xml version="1.0" encoding="UTF-8"?>
 <tmx version="1.4">
  <header
     creationtool="XYZTool" creationtoolversion="0"
     datatype="PlainText" segtype="sentence"
     adminlang="en-us" srclang="en"
     o-tmf="test"/>
  <body>
    <tu>
      <tuv xml:lang="en">
        <seg>Amazon Photos</seg>
      </tuv>
      <tuv xml:lang="fr">
        <seg>Amazon Photos</seg>
      </tuv>
      <tuv xml:lang="es">
        <seg>Amazon Photos</seg>
      </tuv>
    </tu>
  </body>
 </tmx>
```

## Directionality

When you upload a custom terminology file, you set the _directionality_ value for the custom terminology. Directionality
indicates whether your terminology file specifies one source language or multiple source
languages.

For directionality, set one of the following values:

**Uni-directional**

The terminology file contains one source language (the first language in
the list). All other languages are target languages.

For example, in a CSV file, the first column contains text for the source
language, and all other columns contain text for the target
languages.

**Multi-directional**

Any language in the file can be a source language or a target language.
For example, if your terminology file contains text in English, French, and
Spanish, you can use the file for jobs that translate the following language
pairs:

- English to French
- English to Spanish
- French to English
- French to Spanish
- Spanish to English
- Spanish to French

In contrast, you would need to create three uni-directional terminology files for
these six translation jobs (one for each source language).
