# Connecting Amazon Q Business to

Drupal using APIs

You use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") action to connect a data source to your
Amazon Q application. You can also use the [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") action to modify an existing data source configuration.

Then, you use the
`configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") and [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") in the Amazon Q API Reference.

## Drupal JSON schema

The following is the Drupal JSON schema:

```
{
	"$schema": "http://json-schema.org/draft-04/schema#",
	"type": "object",
	"properties": {
		"connectionConfiguration": {
			"type": "object",
			"properties": {
				"repositoryEndpointMetadata": {
					"type": "object",
					"properties": {
						"hostUrl": {
							"type": "string",
							"pattern": "https:.*"
						}
					},
					"required": [
						"hostUrl"
					]
				}
			},
			"required": [
				"repositoryEndpointMetadata"
			]
		},
		"repositoryConfigurations": {
			"type": "object",
			"properties": {
				"content": {
					"type": "object",
					"properties": {
						"fieldMappings": {
							"type": "array",
							"items": [
								{
									"type": "object",
									"properties": {
										"indexFieldName": {
											"type": "string"
										},
										"indexFieldType": {
											"type": "string",
											"enum": [
												"STRING",
												"DATE"
											]
										},
										"dataSourceFieldName": {
											"type": "string"
										},
										"dateFieldFormat": {
											"type": "string",
											"pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
										}
									},
									"required": [
										"indexFieldName",
										"indexFieldType",
										"dataSourceFieldName"
									]
								}
							]
						}
					},
					"required": [
						"fieldMappings"
					]
				},
				"comment": {
					"type": "object",
					"properties": {
						"fieldMappings": {
							"type": "array",
							"items": [
								{
									"type": "object",
									"properties": {
										"indexFieldName": {
											"type": "string"
										},
										"indexFieldType": {
											"type": "string",
											"enum": [
												"STRING",
												"DATE"
											]
										},
										"dataSourceFieldName": {
											"type": "string"
										},
										"dateFieldFormat": {
											"type": "string",
											"pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
										}
									},
									"required": [
										"indexFieldName",
										"indexFieldType",
										"dataSourceFieldName"
									]
								}
							]
						}
					},
					"required": [
						"fieldMappings"
					]
				},
				"attachment": {
					"type": "object",
					"properties": {
						"fieldMappings": {
							"type": "array",
							"items": [
								{
									"type": "object",
									"properties": {
										"indexFieldName": {
											"type": "string"
										},
										"indexFieldType": {
											"type": "string",
											"enum": [
												"STRING",
												"DATE"
											]
										},
										"dataSourceFieldName": {
											"type": "string"
										},
										"dateFieldFormat": {
											"type": "string",
											"pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
										}
									},
									"required": [
										"indexFieldName",
										"indexFieldType",
										"dataSourceFieldName"
									]
								}
							]
						}
					},
					"required": [
						"fieldMappings"
					]
				}
			}
		},
		"additionalProperties": {
			"type": "object",
			"properties": {
				"isCrawlAcl": {
					"type": "boolean"
				},
				"maxFileSizeInMegaBytes": {
					"type": "string"
				},
				"fieldForUserId": {
					"type": "string"
				},
				"isCrawlArticle": {
					"type": "boolean"
				},
				"isCrawlBasicPage": {
					"type": "boolean"
				},
				"isCrawlBasicBlock": {
					"type": "boolean"
				},
				"crawlCustomContentTypesList": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"crawlCustomBlockTypesList": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"filePath": {
					"anyOf": [
						{
							"type": "string",
							"pattern": "s3:.*"
						},
						{
							"type": "string",
							"pattern": ""
						}
					]
				},
				"inclusionFileNamePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"exclusionFileNamePatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"articleTitleInclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"articleTitleExclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"pageTitleInclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"pageTitleExclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"customContentTitleInclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"customContentTitleExclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"basicBlockTitleInclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"basicBlockTitleExclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"customBlockTitleInclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"customBlockTitleExclusionPatterns": {
					"type": "array",
					"items": {
						"type": "string"
					}
				},
				"contentDefinitions": {
					"type": "array",
					"items": {
						"properties": {
							"contentType": {
								"type": "string"
							},
							"fieldDefinition": {
								"type": "array",
								"items": [
									{
										"type": "object",
										"properties": {
											"machineName": {
												"type": "string"
											},
											"type": {
												"type": "string"
											}
										},
										"required": [
											"machineName",
											"type"
										]
									}
								]
							},
							"isCrawlComments": {
								"type": "boolean"
							},
							"isCrawlFiles": {
								"type": "boolean"
							}
						}
					},
					"required": [
						"contentType",
						"fieldDefinition",
						"isCrawlComments",
						"isCrawlFiles"
					]
				}
			},
			"required": []
		},
		"type": {
			"type": "string",
			"pattern": "DRUPAL"
		},
		"authType": {
			"type": "string",
			"enum": [
				"BASIC-AUTH",
				"OAUTH2"
			]
		},
		"syncMode": {
			"type": "string",
			"enum": [
				"FORCED_FULL_CRAWL",
				"FULL_CRAWL",
				"CHANGE_LOG"
			]
		},
		"enableIdentityCrawler": {
			"type": "boolean"
		},
		"secretArn": {
			"type": "string",
			"minLength": 20,
			"maxLength": 2048
		}
	},
	"version": {
		"type": "string",
		"anyOf": [
			{
				"pattern": "1.0.0"
			}
		]
	},
	"required": [
		"connectionConfiguration",
		"repositoryConfigurations",
		"syncMode",
		"additionalProperties",
		"secretArn",
		"type"
	]
}
```

[Show moreShow less](# "#")
The following provides information on important JSON keys to configure.

| Configuration                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration                                                                                                                                                                                                       | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| repositoryEndpointMetadata                                                                                                                                                                                                    | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| hostUrl                                                                                                                                                                                                                       | The host URL of your Drupal website. For example, `https://<hostname>/<drupalsitename>`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| repositoryConfigurations                                                                                                                                                                                                      | Configuration information for the content of the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <br>• content <br>• comment <br>• attachment                                                                                                                                                                                  | A list of objects that map the attributes or field names of your Drupal files. The Drupal data source field names must exist in your Drupal custom metadata.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| additionalProperties                                                                                                                                                                                                          | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `maxFileSizeInMegaBytes`                                                                                                                                                                                                      | Specify the maximum single file size limit in MBs that Amazon Q will crawl. Amazon Q will crawl only the files within the size limit you define. The default file size is 50MB. The maximum file size should be greater than 0MB and less than or equal to 50MB.                                                                                                                                                                                                                                                                                                                                                |
| `isCrawlAcl`                                                                                                                                                                                                                  | Specify `true` to crawl access control information from documents. NoteAmazon Q Business crawls ACL information by default to ensure responses are generated only from documents your end users have access to. See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details.                                                                                                                                                                                                                                                            |
| `fieldForUserId`                                                                                                                                                                                                              | Specify field to use for `UserId` for ACL crawling.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <br>• inclusionFileNamePatterns <br>• articleTitleInclusionPatterns <br>• pageTitleInclusionPatterns <br>• customContentTitleInclusionPatterns <br>• basicBlockTitleInclusionPatterns <br>• customBlockTitleInclusionPatterns | A list of regular expression patterns to _include_ certain files in your Drupal data source. Files that match the patterns are included in the index. Files that don't match the patterns are excluded from the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.                                                                                                                                                                                                                                              |
| <br>• exclusionFileNamePatterns <br>• articleTitleExclusionPatterns <br>• pageTitleExclusionPatterns <br>• customContentTitleExclusionPatterns <br>• basicBlockTitleExclusionPatterns <br>• customBlockTitleExclusionPatterns | A list of regular expression patterns to _exclude_ certain files in your Drupal data source. Files that match the patterns are excluded from the index. Files that don't match the patterns are included in the index. If a file matches both an exclusion and inclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.                                                                                                                                                                                                                                              |
| contentDefinitions <br>• contentType <br>• fieldDefinition <br>• isCrawlComments <br>• isCrawlFiles <br>• isCrawlArticle <br>• isCrawlBasicPage <br>• isCrawlBasicBlock <br>• isCrawlCustomContentTypesList                   | Specify the content types to crawl and whether to crawl comments and attachments for your selected content types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| type                                                                                                                                                                                                                          | The type of data source. Specify `DRUPAL` as your data source type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| authType                                                                                                                                                                                                                      | The type of authentication you are using, whether `BASIC-AUTH` or `OAUTH2`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| syncMode                                                                                                                                                                                                                      | Specify whether Amazon Q should update your index by syncing all documents or only new, modified, and deleted documents. You can choose <br>• `FORCED_FULL_CRAWL` to freshly re-crawl all content and replace existing content each time your data source syncs with your index <br>• `FULL_CRAWL` to incrementally crawl only new, modified, and deleted content each time your data source syncs with your index <br>• `CHANGE_LOG` to incrementally crawl only new and modified content each time your data source syncs with your index                                                                     |
| `enableIdentityCrawler`                                                                                                                                                                                                       | `true` to activate identity crawler. Identity crawler is activated by default. Crawling identity information on users and groups with access to certain documents is useful for user context filtering. Search results are filtered based on the user or their group access to documents. NoteAmazon Q Business crawls identity information from your data source by default to ensure responses are generated only from documents end users have access to. For more information, see [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler"). |
| secretARN                                                                                                                                                                                                                     | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains the key-value pairs required to connect to your Drupal. The secret must contain a JSON structure with the following keys: **If using basic authentication:** ``{ "user name": `"user name"`, "passwords": `"password"` }`` **If using OAuth 2.0 authentication:** ``{ "Client ID": `"client_id"`, "Client secret": `"client_secret"`, "user name": `"user name"`, "password": `"password"` }``                                                                                                                                         |
| version                                                                                                                                                                                                                       | The version of this template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
