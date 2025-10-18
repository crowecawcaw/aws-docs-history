Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchRead

Performs all the read operations in a batch. 


## Request Syntax



```
POST /amazonclouddirectory/2017-01-11/batchread HTTP/1.1
x-amz-data-partition: `DirectoryArn`
x-amz-consistency-level: `ConsistencyLevel`
Content-type: application/json

{
   "Operations": [ 
      { 
         "GetLinkAttributes": { 
            "AttributeNames": [ "`string`" ],
            "TypedLinkSpecifier": { 
               "IdentityAttributeValues": [ 
                  { 
                     "AttributeName": "`string`",
                     "Value": { 
                        "BinaryValue": `blob`,
                        "BooleanValue": `boolean`,
                        "DatetimeValue": `number`,
                        "NumberValue": "`string`",
                        "StringValue": "`string`"
                     }
                  }
               ],
               "SourceObjectReference": { 
                  "Selector": "`string`"
               },
               "TargetObjectReference": { 
                  "Selector": "`string`"
               },
               "TypedLinkFacet": { 
                  "SchemaArn": "`string`",
                  "TypedLinkName": "`string`"
               }
            }
         },
         "GetObjectAttributes": { 
            "AttributeNames": [ "`string`" ],
            "ObjectReference": { 
               "Selector": "`string`"
            },
            "SchemaFacet": { 
               "FacetName": "`string`",
               "SchemaArn": "`string`"
            }
         },
         "GetObjectInformation": { 
            "ObjectReference": { 
               "Selector": "`string`"
            }
         },
         "ListAttachedIndices": { 
            "MaxResults": `number`,
            "NextToken": "`string`",
            "TargetReference": { 
               "Selector": "`string`"
            }
         },
         "ListIncomingTypedLinks": { 
            "FilterAttributeRanges": [ 
               { 
                  "AttributeName": "`string`",
                  "Range": { 
                     "EndMode": "`string`",
                     "EndValue": { 
                        "BinaryValue": `blob`,
                        "BooleanValue": `boolean`,
                        "DatetimeValue": `number`,
                        "NumberValue": "`string`",
                        "StringValue": "`string`"
                     },
                     "StartMode": "`string`",
                     "StartValue": { 
                        "BinaryValue": `blob`,
                        "BooleanValue": `boolean`,
                        "DatetimeValue": `number`,
                        "NumberValue": "`string`",
                        "StringValue": "`string`"
                     }
                  }
               }
            ],
            "FilterTypedLink": { 
               "SchemaArn": "`string`",
               "TypedLinkName": "`string`"
            },
            "MaxResults": `number`,
            "NextToken": "`string`",
            "ObjectReference": { 
               "Selector": "`string`"
            }
         },
         "ListIndex": { 
            "IndexReference": { 
               "Selector": "`string`"
            },
            "MaxResults": `number`,
            "NextToken": "`string`",
            "RangesOnIndexedValues": [ 
               { 
                  "AttributeKey": { 
                     "FacetName": "`string`",
                     "Name": "`string`",
                     "SchemaArn": "`string`"
                  },
                  "Range": { 
                     "EndMode": "`string`",
                     "EndValue": { 
                        "BinaryValue": `blob`,
                        "BooleanValue": `boolean`,
                        "DatetimeValue": `number`,
                        "NumberValue": "`string`",
                        "StringValue": "`string`"
                     },
                     "StartMode": "`string`",
                     "StartValue": { 
                        "BinaryValue": `blob`,
                        "BooleanValue": `boolean`,
                        "DatetimeValue": `number`,
                        "NumberValue": "`string`",
                        "StringValue": "`string`"
                     }
                  }
               }
            ]
         },
         "ListObjectAttributes": { 
            "FacetFilter": { 
               "FacetName": "`string`",
               "SchemaArn": "`string`"
            },
            "MaxResults": `number`,
            "NextToken": "`string`",
            "ObjectReference": { 
               "Selector": "`string`"
            }
         },
         "ListObjectChildren": { 
            "MaxResults": `number`,
            "NextToken": "`string`",
            "ObjectReference": { 
               "Selector": "`string`"
            }
         },
         "ListObjectParentPaths": { 
            "MaxResults": `number`,
            "NextToken": "`string`",
            "ObjectReference": { 
               "Selector": "`string`"
            }
         },
         "ListObjectParents": { 
            "MaxResults": `number`,
            "NextToken": "`string`",
            "ObjectReference": { 
               "Selector": "`string`"
            }
         },
         "ListObjectPolicies": { 
            "MaxResults": `number`,
            "NextToken": "`string`",
            "ObjectReference": { 
               "Selector": "`string`"
            }
         },
         "ListOutgoingTypedLinks": { 
            "FilterAttributeRanges": [ 
               { 
                  "AttributeName": "`string`",
                  "Range": { 
                     "EndMode": "`string`",
                     "EndValue": { 
                        "BinaryValue": `blob`,
                        "BooleanValue": `boolean`,
                        "DatetimeValue": `number`,
                        "NumberValue": "`string`",
                        "StringValue": "`string`"
                     },
                     "StartMode": "`string`",
                     "StartValue": { 
                        "BinaryValue": `blob`,
                        "BooleanValue": `boolean`,
                        "DatetimeValue": `number`,
                        "NumberValue": "`string`",
                        "StringValue": "`string`"
                     }
                  }
               }
            ],
            "FilterTypedLink": { 
               "SchemaArn": "`string`",
               "TypedLinkName": "`string`"
            },
            "MaxResults": `number`,
            "NextToken": "`string`",
            "ObjectReference": { 
               "Selector": "`string`"
            }
         },
         "ListPolicyAttachments": { 
            "MaxResults": `number`,
            "NextToken": "`string`",
            "PolicyReference": { 
               "Selector": "`string`"
            }
         },
         "LookupPolicy": { 
            "MaxResults": `number`,
            "NextToken": "`string`",
            "ObjectReference": { 
               "Selector": "`string`"
            }
         }
      }
   ]
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[ConsistencyLevel](#API_BatchRead_RequestSyntax "#API_BatchRead_RequestSyntax")**


Represents the manner and timing in which the successful write or update of an object
 is reflected in a subsequent read operation of that same object.


Valid Values: `SERIALIZABLE | EVENTUAL`





**[DirectoryArn](#API_BatchRead_RequestSyntax "#API_BatchRead_RequestSyntax")**


The Amazon Resource Name (ARN) that is associated with the [Directory](API_Directory.md "API_Directory.md").
 For more information, see [Arn Examples](arns.md "arns.md").


Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[Operations](#API_BatchRead_RequestSyntax "#API_BatchRead_RequestSyntax")**


A list of operations that are part of the batch.


Type: Array of [BatchReadOperation](API_BatchReadOperation.md "API_BatchReadOperation.md") objects


Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "Responses": [ 
      { 
         "ExceptionResponse": { 
            "Message": "***string***",
            "Type": "***string***"
         },
         "SuccessfulResponse": { 
            "GetLinkAttributes": { 
               "Attributes": [ 
                  { 
                     "Key": { 
                        "FacetName": "***string***",
                        "Name": "***string***",
                        "SchemaArn": "***string***"
                     },
                     "Value": { 
                        "BinaryValue": ***blob***,
                        "BooleanValue": ***boolean***,
                        "DatetimeValue": ***number***,
                        "NumberValue": "***string***",
                        "StringValue": "***string***"
                     }
                  }
               ]
            },
            "GetObjectAttributes": { 
               "Attributes": [ 
                  { 
                     "Key": { 
                        "FacetName": "***string***",
                        "Name": "***string***",
                        "SchemaArn": "***string***"
                     },
                     "Value": { 
                        "BinaryValue": ***blob***,
                        "BooleanValue": ***boolean***,
                        "DatetimeValue": ***number***,
                        "NumberValue": "***string***",
                        "StringValue": "***string***"
                     }
                  }
               ]
            },
            "GetObjectInformation": { 
               "ObjectIdentifier": "***string***",
               "SchemaFacets": [ 
                  { 
                     "FacetName": "***string***",
                     "SchemaArn": "***string***"
                  }
               ]
            },
            "ListAttachedIndices": { 
               "IndexAttachments": [ 
                  { 
                     "IndexedAttributes": [ 
                        { 
                           "Key": { 
                              "FacetName": "***string***",
                              "Name": "***string***",
                              "SchemaArn": "***string***"
                           },
                           "Value": { 
                              "BinaryValue": ***blob***,
                              "BooleanValue": ***boolean***,
                              "DatetimeValue": ***number***,
                              "NumberValue": "***string***",
                              "StringValue": "***string***"
                           }
                        }
                     ],
                     "ObjectIdentifier": "***string***"
                  }
               ],
               "NextToken": "***string***"
            },
            "ListIncomingTypedLinks": { 
               "LinkSpecifiers": [ 
                  { 
                     "IdentityAttributeValues": [ 
                        { 
                           "AttributeName": "***string***",
                           "Value": { 
                              "BinaryValue": ***blob***,
                              "BooleanValue": ***boolean***,
                              "DatetimeValue": ***number***,
                              "NumberValue": "***string***",
                              "StringValue": "***string***"
                           }
                        }
                     ],
                     "SourceObjectReference": { 
                        "Selector": "***string***"
                     },
                     "TargetObjectReference": { 
                        "Selector": "***string***"
                     },
                     "TypedLinkFacet": { 
                        "SchemaArn": "***string***",
                        "TypedLinkName": "***string***"
                     }
                  }
               ],
               "NextToken": "***string***"
            },
            "ListIndex": { 
               "IndexAttachments": [ 
                  { 
                     "IndexedAttributes": [ 
                        { 
                           "Key": { 
                              "FacetName": "***string***",
                              "Name": "***string***",
                              "SchemaArn": "***string***"
                           },
                           "Value": { 
                              "BinaryValue": ***blob***,
                              "BooleanValue": ***boolean***,
                              "DatetimeValue": ***number***,
                              "NumberValue": "***string***",
                              "StringValue": "***string***"
                           }
                        }
                     ],
                     "ObjectIdentifier": "***string***"
                  }
               ],
               "NextToken": "***string***"
            },
            "ListObjectAttributes": { 
               "Attributes": [ 
                  { 
                     "Key": { 
                        "FacetName": "***string***",
                        "Name": "***string***",
                        "SchemaArn": "***string***"
                     },
                     "Value": { 
                        "BinaryValue": ***blob***,
                        "BooleanValue": ***boolean***,
                        "DatetimeValue": ***number***,
                        "NumberValue": "***string***",
                        "StringValue": "***string***"
                     }
                  }
               ],
               "NextToken": "***string***"
            },
            "ListObjectChildren": { 
               "Children": { 
                  "***string***" : "***string***" 
               },
               "NextToken": "***string***"
            },
            "ListObjectParentPaths": { 
               "NextToken": "***string***",
               "PathToObjectIdentifiersList": [ 
                  { 
                     "ObjectIdentifiers": [ "***string***" ],
                     "Path": "***string***"
                  }
               ]
            },
            "ListObjectParents": { 
               "NextToken": "***string***",
               "ParentLinks": [ 
                  { 
                     "LinkName": "***string***",
                     "ObjectIdentifier": "***string***"
                  }
               ]
            },
            "ListObjectPolicies": { 
               "AttachedPolicyIds": [ "***string***" ],
               "NextToken": "***string***"
            },
            "ListOutgoingTypedLinks": { 
               "NextToken": "***string***",
               "TypedLinkSpecifiers": [ 
                  { 
                     "IdentityAttributeValues": [ 
                        { 
                           "AttributeName": "***string***",
                           "Value": { 
                              "BinaryValue": ***blob***,
                              "BooleanValue": ***boolean***,
                              "DatetimeValue": ***number***,
                              "NumberValue": "***string***",
                              "StringValue": "***string***"
                           }
                        }
                     ],
                     "SourceObjectReference": { 
                        "Selector": "***string***"
                     },
                     "TargetObjectReference": { 
                        "Selector": "***string***"
                     },
                     "TypedLinkFacet": { 
                        "SchemaArn": "***string***",
                        "TypedLinkName": "***string***"
                     }
                  }
               ]
            },
            "ListPolicyAttachments": { 
               "NextToken": "***string***",
               "ObjectIdentifiers": [ "***string***" ]
            },
            "LookupPolicy": { 
               "NextToken": "***string***",
               "PolicyToPathList": [ 
                  { 
                     "Path": "***string***",
                     "Policies": [ 
                        { 
                           "ObjectIdentifier": "***string***",
                           "PolicyId": "***string***",
                           "PolicyType": "***string***"
                        }
                     ]
                  }
               ]
            }
         }
      }
   ]
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[Responses](#API_BatchRead_ResponseSyntax "#API_BatchRead_ResponseSyntax")**


A list of all the responses for each batch read.


Type: Array of [BatchReadOperationResponse](API_BatchReadOperationResponse.md "API_BatchReadOperationResponse.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


Access denied or directory not found. Either you don't have permissions for this directory or the directory does not exist. Try calling [ListDirectories](API_ListDirectories.md "API_ListDirectories.md") and check your permissions.


HTTP Status Code: 403




**DirectoryNotEnabledException** 


Operations are only permitted on enabled directories.


HTTP Status Code: 400




**InternalServiceException** 


Indicates a problem that must be resolved by Amazon Web Services. This might be a transient error in which case you can retry your request until it succeeds. Otherwise, go to the [AWS Service Health Dashboard](http://status.aws.amazon.com/ "http://status.aws.amazon.com/") site to see if there are any operational issues with the service.


HTTP Status Code: 500




**InvalidArnException** 


Indicates that the provided ARN value is not valid.


HTTP Status Code: 400




**LimitExceededException** 


Indicates that limits are exceeded. See [Limits](../developerguide/limits.md "../developerguide/limits.md") for more information.


HTTP Status Code: 400




**RetryableConflictException** 


Occurs when a conflict with a previous successful write is detected. For example, if a write operation occurs on an object and then an attempt is made to read the object using “SERIALIZABLE” consistency, this exception may result. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.


HTTP Status Code: 409




**ValidationException** 


Indicates that your request is malformed in some manner. See the exception
 message.


HTTP Status Code: 400




## Examples


The following examples are formatted for legibility.


### Example Request


This example illustrates one usage of BatchRead.



```
POST /amazonclouddirectory/2017-01-11/batchread HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 18
x-amz-data-partition: arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8
x-amz-consistency-level: EVENTUAL
X-Amz-Date: 20170922T233414Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20170922/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-consistency-level;x-amz-data-partition;x-amz-date, Signature=dcf33d791a3f742d04edde6107c4795918d7e034c32f0029a49c95a9fe79cd40

{
	"Operations": []
}
```

### Example Response


This example illustrates one usage of BatchRead.



```
HTTP/1.1 200 OK
x-amzn-RequestId: f6f0b320-a3e4-11e7-b86b-239c40918c06
Date: Thu, 22 Sep 2017 00:35:44 GMT
x-amzn-RequestId: f6f0b320-a3e4-11e7-b86b-239c40918c06
Content-Type: application/json
Content-Length: 521

{
	"Responses": []
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/BatchRead "https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/BatchRead")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/BatchRead "https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/BatchRead")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchRead "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchRead")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/BatchRead "https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/BatchRead")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchRead "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchRead")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/BatchRead "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/BatchRead")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/BatchRead "https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/BatchRead")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/BatchRead "https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/BatchRead")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/BatchRead "https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/BatchRead")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchRead "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchRead")
