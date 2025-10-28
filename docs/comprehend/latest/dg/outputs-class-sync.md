# Outputs for real-time analysis

## Outputs for text inputs

For text inputs, the output includes the list of classes or labels identified by the classifier analysis. The
following example shows a list with two classes.

```

"Classes": [
  {
     "Name": "abc",
     "Score": 0.2757999897003174,
     "Page": 1
  },
  {
    "Name": "xyz",
    "Score": 0.2721000015735626,
    "Page": 1
  }
]

```

## Outputs for semi-structured inputs

For a semi-structured input document, or a text file, the output can include the following additional fields:

- DocumentMetadata – Extraction information about the document. The metadata includes a list of pages in the
  document, with the number of characters extracted from each page. This field is present in the response if the
  request included the `Byte` parameter.
- DocumentType – The document type for each page in the input document. This field is present
  in the response if the request included the `Byte` parameter.
- Errors – Page-level errors that the system detected while processing the input document.
  The field is empty if the system encountered no errors.
- Warnings – Warnings detected while processing the input document. The response includes a
  warning if there is a mismatch between the input document type and the model type associated with the endpoint that you specified.
  The field is empty if the system generated no warnings.

For more details about these output fields, see [ClassifyDocument](../APIReference/API_ClassifyDocument.md "../APIReference/API_ClassifyDocument.md") in the _Amazon Comprehend API Reference_.

The following example shows the output for a one-page native PDF input document.

```
{
  "Classes": [
      {
          "Name": "123",
          "Score": 0.39570000767707825,
          "Page": 1
      },
      {
          "Name": "abc",
          "Score": 0.2757999897003174,
          "Page": 1
      },
      {
          "Name": "xyz",
          "Score": 0.2721000015735626,
          "Page": 1
      }
  ],
  "DocumentMetadata": {
      "Pages": 1,
      "ExtractedCharacters": [
          {
              "Page": 1,
              "Count": 2013
          }
      ]
  },
  "DocumentType": [
      {
          "Page": 1,
          "Type": "NATIVE_PDF"
      }
  ]
}
```
