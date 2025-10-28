# Determining the number of captions selectors needed

- If you are setting up teletext passthrough captions, create only one captions
  selector, even if you want to include multiple languages in the output. With this
  scenario, all languages are automatically extracted and are automatically included in
  the output.
- If you are setting up teletext-to-other, create one captions selector for each
  language that you want to include in the output. For example, one selector to extract
  English teletext, and one selector to extract Swedish teletext.
- If you are setting up teletext passthrough in some outputs and teletext-to-other
  in other outputs, create individual selectors for the teletext-to-other, one for each
  language being converted. Do not worry about a selector for the teletext passthrough
  output. Elemental Live will extract all the data in the teletext, even though there is
  not a selector to explicitly specify this action.
