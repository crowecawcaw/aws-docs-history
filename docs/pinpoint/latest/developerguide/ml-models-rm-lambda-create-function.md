**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Create a Lambda function for Amazon Pinpoint to invoke for a recommender model

To learn how to create a Lambda function, see [Getting Started](../../../lambda/latest/dg/getting-started.md "../../../lambda/latest/dg/getting-started.md") in the _AWS Lambda Developer Guide_. When you design and develop your function, keep
the following requirements and guidelines in mind.

## Input event data

When Amazon Pinpoint invokes a Lambda function for a recommender model, it sends a payload that
contains the configuration and other settings for the campaign or journey that's sending the
message. The payload includes an `Endpoints` object, which is a map that
associates endpoint IDs with endpoint definitions for message recipients.

The endpoint definitions use the structure defined by the [Endpoint](../apireference/apps-application-id-endpoints-endpoint-id.md "../apireference/apps-application-id-endpoints-endpoint-id.md")
resource of the Amazon Pinpoint API. However, they also include a field for a dynamic recommended
attribute named `RecommendationItems`. The `RecommendationItems` field
contains one or more recommended items for the endpoint, as returned from the Amazon Personalize
campaign. The value for this field is an ordered array of 1–5 recommended items (as
strings). The number of items in the array depends on the number of recommended items that
you configured Amazon Pinpoint to retrieve for each endpoint or user.

For example:

```
"Endpoints": {
    "endpointIDexample-1":{
        "ChannelType":"EMAIL",
        "Address":"sofiam@example.com",
        "EndpointStatus":"ACTIVE",
        "OptOut":"NONE",
        "EffectiveDate":"2020-02-26T18:56:24.875Z",
        "Attributes":{
            "AddressType":[
                "primary"
            ]
        },
        "User":{
            "UserId":"SofiaMartínez",
            "UserAttributes":{
                "LastName":[
                    "Martínez"
                ],
                "FirstName":[
                    "Sofia"
                ],
                "Neighborhood":[
                    "East Bay"
                ]
            }
        },
        "RecommendationItems":[
            "1815",
            "2009",
            "1527"
        ],
        "CreationDate":"2020-02-26T18:56:24.875Z"
    },
    "endpointIDexample-2":{
        "ChannelType":"EMAIL",
        "Address":"alejandror@example.com",
        "EndpointStatus":"ACTIVE",
        "OptOut":"NONE",
        "EffectiveDate":"2020-02-26T18:56:24.897Z",
        "Attributes":{
            "AddressType":[
                "primary"
            ]
        },
        "User":{
            "UserId":"AlejandroRosalez",
            "UserAttributes":{
                "LastName ":[
                    "Rosalez"
                ],
                "FirstName":[
                    "Alejandro"
                ],
                "Neighborhood":[
                    "West Bay"
                ]
            }
        },
        "RecommendationItems":[
            "1210",
            "6542",
            "4582"
        ],
        "CreationDate":"2020-02-26T18:56:24.897Z"
    }
}
```

In the preceding example, the relevant Amazon Pinpoint settings are:

- The recommender model is configured to retrieve three recommended items for each
  endpoint or user. (The value for the `RecommendationsPerMessage` property is
  set to `3`.) With this setting, Amazon Pinpoint retrieves and adds only the first,
  second, and third recommended items for each endpoint or user.
- The project is configured to use custom user attributes that store each user's first
  name, last name, and the neighborhood where they live. (The `UserAttributes`
  object contains the values for these attributes.)
- The project is configured to use a custom endpoint attribute
  (`AddressType`) that indicates whether the endpoint is the user's preferred
  address (channel) for receiving messages from the project. (The `Attributes`
  object contains the value for this attribute.)

When Amazon Pinpoint invokes the Lambda function and sends this payload as the event data,
AWS Lambda passes the data to the Lambda function for processing.

Each payload can contain data for up to 50 endpoints. If a segment contains more than 50
endpoints, Amazon Pinpoint invokes the function repeatedly, for up to 50 endpoints at a time, until
the function processes all the data.

## Response data and

requirements

As you design and develop your Lambda function, keep the [quotas for machine learning models](quotas.md#quotas-ML-models "quotas.md#quotas-ML-models") in mind. If the function doesn't meet the
conditions defined by these quotas, Amazon Pinpoint won't be able to process and send the
message.

Also keep the following requirements in mind:

- The function must return updated endpoint definitions in the same format that was
  provided by the input event data.
- Each updated endpoint definition can contain 1–10 custom recommended
  attributes for the endpoint or user. The names of these attributes must match the
  attribute names that you specify when you configure the recommender model in
  Amazon Pinpoint.
- All custom recommended attributes have to be returned in a single
  `Recommendations` object for each endpoint or user. This requirement helps
  ensure that naming conflicts don't occur. You can add the `Recommendations`
  object to any location in an endpoint definition.
- The value for each custom recommended attribute has to be a string (single value) or
  an array of strings (multiple values). If the value is an array of strings, we recommend
  that you maintain the order of the recommended items that Amazon Personalize returned, as indicated
  in the `RecommendationItems` field. Otherwise, your content might not reflect
  the model's predictions for an endpoint or user.
- The function shouldn't modify other elements in the event data, including other
  attribute values for an endpoint or user. It should only add and return values for
  custom recommended attributes. Amazon Pinpoint won't accept updates to any other values in the
  function's response.
- The function has to be hosted in the same AWS Region as the Amazon Pinpoint project that's
  invoking the function. If the function and the project aren't in the same Region, Amazon Pinpoint
  can't send event data to the function.

If any of the preceding requirements isn't met, Amazon Pinpoint won't be able to process and send
the message to one or more endpoints. This might cause a campaign or journey activity to
fail.

Finally, we recommend that you reserve 256 concurrent executions for the
function.

Overall, your Lambda function should process the event data that's sent by Amazon Pinpoint and
return modified endpoint definitions. It can do this by iterating through each endpoint in
the `Endpoints` object and, for each endpoint, creating and setting values for
the custom recommended attributes that you want to use. The following example handler,
written in Python and continuing with the preceding example of input event data, shows
this:

```
import json
import string

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event))
    print("Received context: " +  str(context))
    segment_endpoints = event["Endpoints"]
    new_segment = dict()
    for endpoint_id in segment_endpoints.keys():
        endpoint = segment_endpoints[endpoint_id]
        if supported_endpoint(endpoint):
            new_segment[endpoint_id] = add_recommendation(endpoint)

    print("Returning endpoints: " + json.dumps(new_segment))
    return new_segment

def supported_endpoint(endpoint):
    return True

def add_recommendation(endpoint):
    endpoint["Recommendations"] = dict()

    customTitleList = list()
    customGenreList = list()
    for i,item in enumerate(endpoint["RecommendationItems"]):
        item = int(item)
        if item == 1210:
            customTitleList.insert(i, "Hanna")
            customGenreList.insert(i, "Action")
        elif item == 1527:
            customTitleList.insert(i, "Catastrophe")
            customGenreList.insert(i, "Comedy")
        elif item == 1815:
            customTitleList.insert(i, "Fleabag")
            customGenreList.insert(i, "Comedy")
        elif item == 2009:
            customTitleList.insert(i, "Late Night")
            customGenreList.insert(i, "Drama")
        elif item == 4582:
            customTitleList.insert(i, "Agatha Christie\'s The ABC Murders")
            customGenreList.insert(i, "Crime")
        elif item == 6542:
            customTitleList.insert(i, "Hunters")
            customGenreList.insert(i, "Drama")

    endpoint["Recommendations"]["Title"] = customTitleList
    endpoint["Recommendations"]["Genre"] = customGenreList

    return endpoint
```

In the preceding example, AWS Lambda passes the event data to the handler as the
`event` parameter. The handler iterates through each endpoint in the
`Endpoints` object and sets values for custom recommended attributes named
`Recommendations.Title` and `Recommendations.Genre`. The
`return` statement returns each updated endpoint definition to Amazon Pinpoint.

Continuing with the earlier example of input event data, the updated endpoint
definitions are:

```
"Endpoints":{
    "endpointIDexample-1":{
        "ChannelType":"EMAIL",
        "Address":"sofiam@example.com",
        "EndpointStatus":"ACTIVE",
        "OptOut":"NONE",
        "EffectiveDate":"2020-02-26T18:56:24.875Z",
        "Attributes":{
            "AddressType":[
                "primary"
            ]
        },
        "User":{
            "UserId":"SofiaMartínez",
            "UserAttributes":{
                "LastName":[
                    "Martínez"
                ],
                "FirstName":[
                    "Sofia"
                ],
                "Neighborhood":[
                    "East Bay"
                ]
            }
        },
        "RecommendationItems":[
            "1815",
            "2009",
            "1527"
        ],
        "CreationDate":"2020-02-26T18:56:24.875Z",
        "Recommendations":{
            "Title":[
                "Fleabag",
                "Late Night",
                "Catastrophe"
            ],
            "Genre":[
                "Comedy",
                "Comedy",
                "Comedy"
            ]
        }
    },
    "endpointIDexample-2":{
        "ChannelType":"EMAIL",
        "Address":"alejandror@example.com",
        "EndpointStatus":"ACTIVE",
        "OptOut":"NONE",
        "EffectiveDate":"2020-02-26T18:56:24.897Z",
        "Attributes":{
            "AddressType":[
                "primary"
            ]
        },
        "User":{
            "UserId":"AlejandroRosalez",
            "UserAttributes":{
                "LastName ":[
                    "Rosalez"
                ],
                "FirstName":[
                    "Alejandro"
                ],
                "Neighborhood":[
                    "West Bay"
                ]
            }
        },
        "RecommendationItems":[
            "1210",
            "6542",
            "4582"
        ],
        "CreationDate":"2020-02-26T18:56:24.897Z",
        "Recommendations":{
            "Title":[
                "Hanna",
                "Hunters",
                "Agatha Christie\'s The ABC Murders"
            ],
            "Genre":[
                "Action",
                "Drama",
                "Crime"
            ]
        }
    }
}
```

In the preceding example, the function modified the `Endpoints` object that
it received and returned the results. The `Endpoint` object for each endpoint now
contains a new `Recommendations` object, which contains `Title` and
`Genre` fields. Each of these fields stores an ordered array of three values
(as strings), where each value provides enhanced content for a corresponding recommended
item in the `RecommendationItems` field.
