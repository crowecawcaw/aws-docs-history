# Using Adapters during Inference

After creating an adapter, you are provided with an ID and version for your custom
adapter. You can provide this ID and version to [AnalyzeDocument](API_AnalyzeDocument.md "API_AnalyzeDocument.md") for synchronous document analysis, or the
[StartDocumentAnalysis](API_StartDocumentAnalysis.md "API_StartDocumentAnalysis.md") operation for asynchronous analysis. Providing the Adapter ID will automatically
integrate the adapter into the analysis process and use it to enhance predictions for
your documents.

This way, you can leverage the capabilities of `AnalyzeDocument` while
customizing it to fit your needs. When multiple adapters must be applied to different
pages in the same document, you can specify one or more adapter(s) and their respective
adapter versions as part of the API request. You can use the `Page` parameter
to specify which pages to apply an adapter to.

This is similar to how the `Page` parameter for Queries works. Note the
following:

- If a page is not specified, it is set to `["1"]` by default.
- The following characters are valid in the parameter string: `1 2 3 4 5 6
7 8 9 - *`. Blank spaces are not valid.
- When using \* to indicate all pages, it must be the only element in the
  list.
- The `Page` parameter does not overlap across adapters. A page can
  only have one adapter applied to it.
  See the following example:

```

AdaptersConfig={ 'Adapters': [ { 'AdapterId': ADAPTER_ID,'Version': '1',
'Pages': ["1-5"] }, { 'AdapterId': ADAPTER_ID, 'Version': '1', 'Pages':["6-*"] } ] })

```
