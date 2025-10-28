# Query responses and response types

###### Note

Feature support varies by index type and search API being used. To see if this
feature is supported for the index type and search API you’re using, see [Index
types](hiw-index-types.md "hiw-index-types.md").

Amazon Kendra supports different query responses and response types.

## Query responses

A call to the [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") API returns
information about the results of a search. The results are in an array of[QueryResultItem](../APIReference/API_QueryResultItem.md "../APIReference/API_QueryResultItem.md") objects (`ResultItems`). Each
`QueryResultItem` includes a summary of the result. Document
attributes associated with the query result are included.

###### Summary information

The summary information varies depending on the type of result. In each case,
it includes document text that matches the search term. It also includes
highlight information that you can use to highlight the search text in your
application's output. For example, if the search term is _what is the
height of the Space Needle?_, the summary information includes
text location for the words _height_ and _space
needle_. For information about response types, see [Query responses and response types](query-responses-types.md "query-responses-types.md").

###### Document attributes

Each result contains document attributes for the document that matches a
query. Some of the attributes are predefined, such as `DocumentId`,
`DocumentTitle`, and `DocumentUri`. Others are custom
attributes that you define. You can use document attributes to filter the
response from the `Query` API. For example, you might want only the
documents written by a specific author or a specific version of a document. For
more information, see [Filtering and facet search](filtering.md "filtering.md"). You
specify document attributes when you add documents to an index. For more
information, see [Custom fields or
attributes](custom-attributes.md "custom-attributes.md").

The following is sample JSON code for a query result. Note the document attributes
in `DocumentAttributes` and `AdditionalAttributes`.

```
{
    "QueryId": "`query-id`",
    "ResultItems": [
        {
            "Id": "`result-id`",
            "Type": "ANSWER",
            "AdditionalAttributes": [
                {
                    "Key": "AnswerText",
                    "ValueType": "TEXT_WITH_HIGHLIGHTS_VALUE",
                    "Value": {
                        "TextWithHighlightsValue": {
                            "Text": "`text`",
                            "Highlights": [
                                {
                                    "BeginOffset": 55,
                                    "EndOffset": 90,
                                    "TopAnswer": false
                                }
                            ]
                        }
                    }
                }
            ],
            "DocumentId": "`document-id`",
            "DocumentTitle": {
                "Text": "`title`"
            },
            "DocumentExcerpt": {
                "Text": "`text`",
                "Highlights": [
                    {
                        "BeginOffset": 0,
                        "EndOffset": 300,
                        "TopAnswer": false
                    }
                ]
            },
            "DocumentURI": "`uri`",
            "DocumentAttributes": [],
            "ScoreAttributes": "`score`",
            "FeedbackToken": "`token`"
        },
        {
            "Id": "`result-id`",
            "Type": "ANSWER",
            "Format": "TABLE",
            "DocumentId": "`document-id`",
            "DocumentTitle": {
                "Text": "`title`"
            },
            "TableExcerpt": {
                "Rows": [{
                    "Cells": [{
                        "Header": true,
                        "Highlighted": false,
                        "TopAnswer": false,
                        "Value": "`value`"
                    }, {
                        "Header": true,
                        "Highlighted": false,
                        "TopAnswer": false,
                        "Value": "`value`"
                    }, {
                        "Header": true,
                        "Highlighted": false,
                        "TopAnswer": false,
                        "Value": "`value`"
                    }, {
                        "Header": true,
                        "Highlighted": false,
                        "TopAnswer": false,
                        "Value": "`value`"
                    }]
                }, {
                    "Cells": [{
                        "Header": false,
                        "Highlighted": false,
                        "TopAnswer": false,
                        "Value": "`value`"
                    }, {
                        "Header": false,
                        "Highlighted": false,
                        "TopAnswer": false,
                        "Value": "`value`"
                    }, {
                        "Header": false,
                        "Highlighted": true,
                        "TopAnswer": true,
                        "Value": "`value`"
                    }, {
                        "Header": false,
                        "Highlighted": false,
                        "TopAnswer": false,
                        "Value": "`value`"
                    ]}
                  }],
                    "TotalNumberofRows": `number`
			},
            "DocumentURI": "`uri`",
            "ScoreAttributes": "`score`",
            "FeedbackToken": "`token`"
        },
        {
            "Id": "`result-id`",
            "Type": "DOCUMENT",
            "AdditionalAttributes": [],
            "DocumentId": "`document-id`",
            "DocumentTitle": {
                "Text": "`title`",
                "Highlights": []
            },
            "DocumentExcerpt": {
                "Text": "`text`",
                "Highlights": [
                    {
                        "BeginOffset": 74,
                        "EndOffset": 77,
                        "TopAnswer": false
                    }
                ]
            },
            "DocumentURI": "`uri`",
            "DocumentAttributes": [
                {
                    "Key": "_source_uri",
                    "Value": {
                        "StringValue": "`uri`"
                    }
                }
            ],
            "ScoreAttributes": "`score`",
            "FeedbackToken": "`token`",
        }
    ],
    "FacetResults": [],
    "TotalNumberOfResults": `number`
}
```

## Response types

Amazon Kendra returns three types of query response.

- Answer (includes table answer)
- Document
- Question and answer

The type of the response is returned in the `Type` response field of
the [QueryResultItem](../APIReference/API_QueryResultItem.md "../APIReference/API_QueryResultItem.md") object.

### Answer

Amazon Kendra detected one or more question answers in the response. A
factoid is the response to a who, what, when, or where question such as
_Where is the nearest service center to me?_
Amazon Kendra returns text in the index that best matches the query. The
text is in the `AnswerText` field and contains highlight information
for the search term within the response text. `AnswerText` includes
the full document excerpt with highlighted text, while
`DocumentExcerpt` includes the truncated (290 characters)
document excerpt with highlighted text.

Amazon Kendra only returns one answer per document, and that is the
answer with the highest confidence. To return multiple answers from a document,
you must split the document into multiple documents.

```
{
    'AnswerText': {
        'TextWithHighlights': [
            {
                'BeginOffset': 271,
                'EndOffset': 279,
                'TopAnswer': False
            },
            {
                'BeginOffset': 481,
                'EndOffset': 489,
                'TopAnswer': False
            },
            {
                'BeginOffset': 547,
                'EndOffset': 555,
                'TopAnswer': False
            },
            {
                'BeginOffset': 764,
                'EndOffset': 772,
                'TopAnswer': False
            }
        ],
        'Text': 'Asynchronousoperationscan\n''alsoprocess\n''documentsthatareinPDF''format.UsingPDFformatfilesallowsyoutoprocess''multi-page\n''documents.\n''Forinformationabouthow''AmazonTextractrepresents\n''documentsasBlockobjects,
        ''seeDocumentsandBlockObjects.\n''\n''\n''\n''Forinformationaboutdocument''limits,
        seeLimitsinAmazonTextract.\n''\n''\n''\n''TheAmazonTextractsynchronous''operationscanprocessdocumentsstoredinanAmazon\n''S3Bucketoryoucanpass''base64encodedimagebytes.\n''Formoreinformation,
        see''CallingAmazonTextractSynchronousOperations.''Asynchronousoperationsrequireinputdocuments\n''tobesuppliedinanAmazon''S3Bucket.'
    },
    'DocumentExcerpt': {
        'Highlights': [
            {
                'BeginOffset': 0,
                'EndOffset': 300,
                'TopAnswer': False
            }
        ],
        'Text': 'Asynchronousoperationscan\n''alsoprocess\n''documentsthatareinPDF''format.UsingPDFformatfilesallowsyoutoprocess''multi-page\n''documents.\n''ForinformationabouthowAmazon''Textractrepresents\n'''
    },
    'Type': 'ANSWER'
}
```

### Document

Amazon Kendra returns ranked documents for those that match the search
term. The ranking is based on the confidence that Amazon Kendra has in the
accuracy of the search result. Information about the matching document is
returned in the [QueryResultItem](../APIReference/API_QueryResultItem.md "../APIReference/API_QueryResultItem.md"). It includes the title of the document. The excerpt
includes highlight information for search text and the section of matching text
in the document. The URI for matching documents is in the `SourceURI`
document attribute. The following sample JSON shows the document summary for a
matching document.

```
{
    'DocumentTitle': {
        'Highlights': [
            {
                'BeginOffset': 7,
                'EndOffset': 15,
                'TopAnswer': False
            },
            {
                'BeginOffset': 97,
                'EndOffset': 105,
                'TopAnswer': False
            }
        ],
        'Text': 'AmazonTextractAPIPermissions: Actions,
        \n''Permissions,
        andResourcesReference-''AmazonTextract'
    },
    'DocumentExcerpt': {
        'Highlights': [
            {
                'BeginOffset': 68,
                'EndOffset': 76,
                'TopAnswer': False
            },
            {
                'BeginOffset': 121,
                'EndOffset': 129,
                'TopAnswer': False
            }
        ],
        'Text': '...LoggingandMonitoring\tMonitoring\n''\tCloudWatchMetricsforAmazonTextract\n''\tLoggingAmazonTextractAPICallswithAWSCloudTrail\n''\tAPIReference\tActions\tAnalyzeDocument\n''\tDetectDocumentText\n''\tGetDocumentAnalysis...'
    },
    'Type': 'DOCUMENT'
}
```

### Question and answer

A question and answer response is returned when Amazon Kendra matches a
question with one of the frequently asked questions in your index. The response
includes the matching question and answer in the [QueryResultItem](../APIReference/API_QueryResultItem.md "../APIReference/API_QueryResultItem.md") field. It also includes highlight information for
query terms detected in query string. The following JSON shows a question and
answer response. Note that the response includes the question text.

```
{
    'AnswerText': {
        'TextWithHighlights': [

        ],
        'Text': '605feet'
    },
    'DocumentExcerpt': {
        'Highlights': [
            {
                'BeginOffset': 0,
                'EndOffset': 8,
                'TopAnswer': False
            }
        ],
        'Text': '605feet'
    },
    'Type': 'QUESTION_ANSWER',
    'QuestionText': {
        'Highlights': [
            {
                'BeginOffset': 12,
                'EndOffset': 18,
                'TopAnswer': False
            },
            {
                'BeginOffset': 26,
                'EndOffset': 31,
                'TopAnswer': False
            },
            {
                'BeginOffset': 32,
                'EndOffset': 38,
                'TopAnswer': False
            }
        ],
        'Text': 'whatistheheightoftheSpaceNeedle?'
    }
}
```

For information about adding question and answer text to an index, see [Creating
FAQ](in-creating-faq.md "in-creating-faq.md").
