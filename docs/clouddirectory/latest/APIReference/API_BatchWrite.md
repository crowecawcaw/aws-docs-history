Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchWrite

Performs all the write operations in a batch. Either all the operations succeed or
 none.


## Request Syntax



```
PUT /amazonclouddirectory/2017-01-11/batchwrite HTTP/1.1
x-amz-data-partition: `DirectoryArn`
Content-type: application/json

{
   "Operations": [ 
      { 
         "AddFacetToObject": { 
            "ObjectAttributeList": [ 
               { 
                  "Key": { 
                     "FacetName": "`string`",
                     "Name": "`string`",
                     "SchemaArn": "`string`"
                  },
                  "Value": { 
                     "BinaryValue": `blob`,
                     "BooleanValue": `boolean`,
                     "DatetimeValue": `number`,
                     "NumberValue": "`string`",
                     "StringValue": "`string`"
                  }
               }
            ],
            "ObjectReference": { 
               "Selector": "`string`"
            },
            "SchemaFacet": { 
               "FacetName": "`string`",
               "SchemaArn": "`string`"
            }
         },
         "AttachObject": { 
            "ChildReference": { 
               "Selector": "`string`"
            },
            "LinkName": "`string`",
            "ParentReference": { 
               "Selector": "`string`"
            }
         },
         "AttachPolicy": { 
            "ObjectReference": { 
               "Selector": "`string`"
            },
            "PolicyReference": { 
               "Selector": "`string`"
            }
         },
         "AttachToIndex": { 
            "IndexReference": { 
               "Selector": "`string`"
            },
            "TargetReference": { 
               "Selector": "`string`"
            }
         },
         "AttachTypedLink": { 
            "Attributes": [ 
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
         },
         "CreateIndex": { 
            "BatchReferenceName": "`string`",
            "IsUnique": `boolean`,
            "LinkName": "`string`",
            "OrderedIndexedAttributeList": [ 
               { 
                  "FacetName": "`string`",
                  "Name": "`string`",
                  "SchemaArn": "`string`"
               }
            ],
            "ParentReference": { 
               "Selector": "`string`"
            }
         },
         "CreateObject": { 
            "BatchReferenceName": "`string`",
            "LinkName": "`string`",
            "ObjectAttributeList": [ 
               { 
                  "Key": { 
                     "FacetName": "`string`",
                     "Name": "`string`",
                     "SchemaArn": "`string`"
                  },
                  "Value": { 
                     "BinaryValue": `blob`,
                     "BooleanValue": `boolean`,
                     "DatetimeValue": `number`,
                     "NumberValue": "`string`",
                     "StringValue": "`string`"
                  }
               }
            ],
            "ParentReference": { 
               "Selector": "`string`"
            },
            "SchemaFacet": [ 
               { 
                  "FacetName": "`string`",
                  "SchemaArn": "`string`"
               }
            ]
         },
         "DeleteObject": { 
            "ObjectReference": { 
               "Selector": "`string`"
            }
         },
         "DetachFromIndex": { 
            "IndexReference": { 
               "Selector": "`string`"
            },
            "TargetReference": { 
               "Selector": "`string`"
            }
         },
         "DetachObject": { 
            "BatchReferenceName": "`string`",
            "LinkName": "`string`",
            "ParentReference": { 
               "Selector": "`string`"
            }
         },
         "DetachPolicy": { 
            "ObjectReference": { 
               "Selector": "`string`"
            },
            "PolicyReference": { 
               "Selector": "`string`"
            }
         },
         "DetachTypedLink": { 
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
         "RemoveFacetFromObject": { 
            "ObjectReference": { 
               "Selector": "`string`"
            },
            "SchemaFacet": { 
               "FacetName": "`string`",
               "SchemaArn": "`string`"
            }
         },
         "UpdateLinkAttributes": { 
            "AttributeUpdates": [ 
               { 
                  "AttributeAction": { 
                     "AttributeActionType": "`string`",
                     "AttributeUpdateValue": { 
                        "BinaryValue": `blob`,
                        "BooleanValue": `boolean`,
                        "DatetimeValue": `number`,
                        "NumberValue": "`string`",
                        "StringValue": "`string`"
                     }
                  },
                  "AttributeKey": { 
                     "FacetName": "`string`",
                     "Name": "`string`",
                     "SchemaArn": "`string`"
                  }
               }
            ],
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
         "UpdateObjectAttributes": { 
            "AttributeUpdates": [ 
               { 
                  "ObjectAttributeAction": { 
                     "ObjectAttributeActionType": "`string`",
                     "ObjectAttributeUpdateValue": { 
                        "BinaryValue": `blob`,
                        "BooleanValue": `boolean`,
                        "DatetimeValue": `number`,
                        "NumberValue": "`string`",
                        "StringValue": "`string`"
                     }
                  },
                  "ObjectAttributeKey": { 
                     "FacetName": "`string`",
                     "Name": "`string`",
                     "SchemaArn": "`string`"
                  }
               }
            ],
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





**[DirectoryArn](#API_BatchWrite_RequestSyntax "#API_BatchWrite_RequestSyntax")**


The Amazon Resource Name (ARN) that is associated with the [Directory](API_Directory.md "API_Directory.md").
 For more information, see [Arn Examples](arns.md "arns.md").


Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[Operations](#API_BatchWrite_RequestSyntax "#API_BatchWrite_RequestSyntax")**


A list of operations that are part of the batch.


Type: Array of [BatchWriteOperation](API_BatchWriteOperation.md "API_BatchWriteOperation.md") objects


Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "Responses": [ 
      { 
         "AddFacetToObject": { 
         },
         "AttachObject": { 
            "attachedObjectIdentifier": "***string***"
         },
         "AttachPolicy": { 
         },
         "AttachToIndex": { 
            "AttachedObjectIdentifier": "***string***"
         },
         "AttachTypedLink": { 
            "TypedLinkSpecifier": { 
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
         },
         "CreateIndex": { 
            "ObjectIdentifier": "***string***"
         },
         "CreateObject": { 
            "ObjectIdentifier": "***string***"
         },
         "DeleteObject": { 
         },
         "DetachFromIndex": { 
            "DetachedObjectIdentifier": "***string***"
         },
         "DetachObject": { 
            "detachedObjectIdentifier": "***string***"
         },
         "DetachPolicy": { 
         },
         "DetachTypedLink": { 
         },
         "RemoveFacetFromObject": { 
         },
         "UpdateLinkAttributes": { 
         },
         "UpdateObjectAttributes": { 
            "ObjectIdentifier": "***string***"
         }
      }
   ]
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[Responses](#API_BatchWrite_ResponseSyntax "#API_BatchWrite_ResponseSyntax")**


A list of all the responses for each batch write.


Type: Array of [BatchWriteOperationResponse](API_BatchWriteOperationResponse.md "API_BatchWriteOperationResponse.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


Access denied or directory not found. Either you don't have permissions for this directory or the directory does not exist. Try calling [ListDirectories](API_ListDirectories.md "API_ListDirectories.md") and check your permissions.


HTTP Status Code: 403




**BatchWriteException** 


A `BatchWrite` exception has occurred.


HTTP Status Code: 400




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


This example illustrates one usage of BatchWrite.



```
PUT /amazonclouddirectory/2017-01-11/batchwrite HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 18
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20170922/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-data-partition;x-amz-date, Signature=e539506cd67ac7a753fa37aa58272f4c7bda369fc0f6b4f7bff6bea0f0fcd4af
x-amz-data-partition: arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY
X-Amz-Date: 20170922T232444Z
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8

{
	"Operations": []
}
```

### Example Response


This example illustrates one usage of BatchWrite.



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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/BatchWrite "https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/BatchWrite")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/BatchWrite "https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/BatchWrite")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchWrite "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchWrite")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/BatchWrite "https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/BatchWrite")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchWrite "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchWrite")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/BatchWrite "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/BatchWrite")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/BatchWrite "https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/BatchWrite")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/BatchWrite "https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/BatchWrite")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/BatchWrite "https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/BatchWrite")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchWrite "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchWrite")
