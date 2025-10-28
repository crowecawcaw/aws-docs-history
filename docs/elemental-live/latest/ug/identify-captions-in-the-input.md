# Step 1: Identify the

source captions that you want

You must identify the captions that you want to use and assign each to a captions
selector. If you don't create any captions selectors, you will not be able to include
captions in the output. All the captions will be removed from the media.

###### To identify the captions you want

1.  Identify which captions are in the input (the provider of the input should provide
    you with this information) and identify which captions are available to you as external
    files. Identify the captions formats and, for each format, the languages.
2.  Identify which of those formats and languages that you want to use.
3.  Determine how many captions selectors to create in the input in the event, using the
    following guidance:
    - For embedded passthrough, create a single captions selector for all languages.
      All languages are passed through; there is no other option. For details, see [Information for embedded](embedded.md "embedded.md") .
    - For embedded-to-other-format, create one captions selector for each
      language.
    - For teletext passthrough, create a single captions selector for all languages
      (in fact, one captions selector for the entire content). All languages (teletext
      pages) are passed through; there is no other option. For details, see [Information for Teletext](teletext.md "teletext.md").
    - For teletext-to-other-format, create one captions selector for each
      language.
    - In all other cases, create one captions selector for each language and format
      combination.

4.  You end up with a list of captions selectors to create. For example:

        * Captions Selector 1: teletext captions in Czech
        * Captions Selector 2: teletext captions in Polish

    You are not required to use all the languages that are available. You can ignore those
    you are not interested in.
