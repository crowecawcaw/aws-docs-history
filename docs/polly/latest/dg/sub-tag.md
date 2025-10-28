# Pronouncing acronyms and abbreviations

_<sub>_

This tag is supported by generative, long-form, neural, and standard TTS formats.

Use the `<sub>` tag with the `alias`
attribute to substitute a different word (or pronunciation) for
selected text such as an acronym or abbreviation.

This uses the syntax:

```
<sub alias="`new word`">`abbreviation`</sub>
```

In the following example, the name "Mercury" is substituted
for the element's chemical symbol to make the audio content
clearer.

```
<speak>
     My favorite chemical element is <sub alias="Mercury">Hg</sub>, because it looks so shiny.
</speak>
```
