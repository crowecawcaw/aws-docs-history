# Amazon EventBridge events for AWS Data Exchange

AWS Data Exchange is integrated with Amazon EventBridge, formerly called Amazon CloudWatch Events. EventBridge is an event bus service
that you can use to connect your applications with data from a variety of sources. For more
information, see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md").

As a subscriber with an active subscription to a product, you receive an _event_ from AWS Data Exchange every time the provider publishes new
revisions or adds new data sets to an existing product. The event contains the
`DataSetId` and the list of `RevisionIds` that have been
published.

Providers can send notifications corresponding to data updates, data delays, schema
changes, and deprecations. Providers have the option to include comments and expected
actions for subscribers to follow. Subscribers receive these notifications as events in
Amazon EventBridge, which they can use to build automated workflows or deliver human-readable
notifications to emails and chat programs using [AWS User Notifications](../../../notifications/latest/userguide/what-is-service.md "../../../notifications/latest/userguide/what-is-service.md").

Data product related events are emitted in the AWS Region where the provider published
the data set. You must set up EventBridge rules that use these events in the same AWS Region or
see [Sending and receiving Amazon EventBridge events between AWS Regions](../../../eventbridge/latest/userguide/eb-cross-region.md "../../../eventbridge/latest/userguide/eb-cross-region.md") for more
options.

This topic provides detailed information about each event listed in the following table.
The table includes events received by a subscriber when a provider adds a data set to a
product, adds a revision to a product, revokes a revision to a product, or removes access to
a product.

| Actions                                                                                              | Event received                                                        | Related topic                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Adds a file-based data set to a product and publishes it                                             | `Data Sets Published To Product`                                      | [Events for adding file-based data sets](#events-add-data-sets "#events-add-data-sets")                                                                                                            |
| Adds an Amazon S3 data access data set to a product and publishes it                                 | `Amazon S3 Data Access Data Sets Published To Product`                | [Events for adding Amazon S3 data access<br>data sets](#events-add-s3-data-access-data-sets "#events-add-s3-data-access-data-sets")                                                                |
| Adds an AWS Lake Formation data permission data set and publishes it                                 | `AWS Lake Formation Data Permission Data Set Published To<br>Product` | [Events for adding AWS Lake Formation data permission<br>data sets](#events-add-LF-data-sets "#events-add-LF-data-sets")                                                                           |
| Adds an Amazon Redshift data set to a product and publishes it                                       | `Redshift Data Shares Data Sets Published To Product`                 | [Events for adding Amazon Redshift datashare data sets](#events-add-RS-data-sets "#events-add-RS-data-sets")                                                                                       |
| Adds an Amazon API Gateway data set to a product and publishes it                                    | `API Gateway API Data Sets Published To Product`                      | [Events for adding Amazon API Gateway API<br>data sets](#events-add-api-gateway-api-data-sets "#events-add-api-gateway-api-data-sets")                                                             |
| Adds a file-based data set revision to a product and publishes it                                    | `Revision Published To Data Set`                                      | [Events for adding revisions](#events-add-revisions "#events-add-revisions")                                                                                                                       |
| Adds an Amazon S3 data access data set revision to a product and publishes<br>it                     | `Revision Published to Amazon S3 Data Access Data Set`                | [Events for adding Amazon S3 data access data set<br>revisions](#events-add-s3-revisions "#events-add-s3-revisions")                                                                               |
| Adds an AWS Lake Formation data permission data set revision to a product and<br>publishes it        | `Revision Published To Lake Formation Data Permission Data Set`       | [Events for adding AWS Lake Formation data permission data<br>set revisions (Preview)](#events-add-LF-revision "#events-add-LF-revision")                                                          |
| Adds an Amazon Redshift datashare data set revision to a product and publishes<br>it                 | `Revision Published To Redshift Data Shares Data Set`                 | [Events for adding Amazon Redshift datashare data set<br>revisions](#events-add-RS-revision "#events-add-RS-revision")                                                                             |
| Adds an Amazon API Gateway data set revision to a product and publishes it                           | `Revision Published To API Gateway API Data Set`                      | [Events for adding<br>Amazon API Gateway API data set revisions](#events-add-api-gateway-api-data-sets-revisions "#events-add-api-gateway-api-data-sets-revisions")                                |
| Revokes revision to a product                                                                        | `Revision Revoked`                                                    | [Events for revoking revisions](#events-revoke-revisions "#events-revoke-revisions")                                                                                                               |
| Takes an action on their Amazon Redshift resources that \*might<br>• remove access from a subscriber | `Action Performed On Redshift Data Share By Provider`                 | [Events for an action performed on an Amazon Redshift<br>resource](#events-RS-action "#events-RS-action")                                                                                          |
| Takes an action on their Amazon Redshift resources that removes access from a<br>subscriber          | `Redshift Data Share Access Lost`                                     | [Events for losing access to an Amazon Redshift<br>datashare](#events-RS-lost-access "#events-RS-lost-access")                                                                                     |
| Sends a notification for a data update                                                               | `Data Updated in Data Set`                                            | [Events for<br>a provider-generated notification of a data update](#events-provider-generated-notification-of-data-update "#events-provider-generated-notification-of-data-update")                |
| Sends a notification for a schema change                                                             | `Schema Change Planned for Data Set`                                  | [Events<br>for a provider-generated notification of a schema change](#events-provider-generated-notification-of-schema-change "#events-provider-generated-notification-of-schema-change")          |
| Sends a notification for a data delay                                                                | `Data Set Update Delayed`                                             | [Events for a<br>provider-generated notification of a data delay](#events-provider-generated-notification-of-data-delay "#events-provider-generated-notification-of-data-delay")                   |
| Sends a notification for a data deprecation                                                          | `Deprecation Planned for Data Set`                                    | [Events for<br>a provider-generated notification of a data deprecation](#events-provider-generated-notification-of-data-deprecation "#events-provider-generated-notification-of-data-deprecation") |
| Sends an event when a data consumer accepts a data grant                                             | `Data Grant Accepted`                                                 | [Events for accepting a data grant](#data-grant-accepted-event "#data-grant-accepted-event")                                                                                                       |
| Sends an event when a data producer extends a data grant                                             | `Data Grant Extended`                                                 | [Events for extending data grants](#data-grant-extended-event "#data-grant-extended-event")                                                                                                        |
| Sends an event when a data producer revokes a data grant                                             | `Data Grant Revoked`                                                  | [Events for revoking a data grant](#data-grant-revoked-event "#data-grant-revoked-event")                                                                                                          |
| Auto-export job completed                                                                            | `Auto-export Job Completed`                                           | [Events for an auto-export job completed](#events-auto-export-job-complete "#events-auto-export-job-complete")                                                                                     |
| Auto-export job failed                                                                               | `Auto-export Job Failed`                                              | [Events for an auto-export job<br>failed](#events-auto-export-job-failed "#events-auto-export-job-failed")                                                                                         |

###### Note

AWS Data Exchange emits events on a best effort basis. For more information about event delivery,
see [Events from AWS services](../../../eventbridge/latest/userguide/eb-service-event.md "../../../eventbridge/latest/userguide/eb-service-event.md").

## Events for adding file-based data sets

When a provider adds file-based data sets to a product and publishes it, the
subscriber receives an event with the `Data Sets Published
 To Product` detail type.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Data Sets Published To Product",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2020-07-29T18:24:04Z`",
    "region": "`us-east-1`",
    "resources":  [
        "prod-`uEXAMPLEabc1d`"
    ],
    "detail":  {
        "DataSetIds":  [
            "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
            "`5bgd734EXAMPLE100f7gdd9EXAMPLEe9`"
        ],
        "DataSets": [
            {
               "Id" : "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
               "Name": "`Data_Set_Hello_World_One`"
            },
            {
               "Id" : "`5bgd734EXAMPLE100f7gdd9EXAMPLEe9`",
               "Name": "`Data_Set_Hello_World_Two`"
            }
        ],
        "Product":
         {
            "Id" : "prod-`uEXAMPLEabc1d`",
            "Name": "`Product_Hello_World`"
         }
    }
}
```

## Events for adding Amazon S3 data access

data sets

When a provider adds an Amazon S3 data access data set to a product and publishes it, the
subscriber receives an event with the following detail type: `Amazon S3
 Data Access Data Set(s) Published To Product`.

The following example shows the event body for the detail type.

```
{
	"version": "0",
	"id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
	"detail-type": "S3 Data Access Data Set(s) Published to Product",
	"source": "aws.dataexchange",
	"account": "`123456789012`",
	"time": "`2020-07-29T18:24:04Z`",
	"region": "`us-east-1`",
	"resources": [
		"prod-`uEXAMPLEabc1d`"
	],
	"detail": {
		"DataSetIds": [
			"`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
			"`5bgd734EXAMPLE100f7gdd9EXAMPLEe9`"
		],
		"DataSets": [{
				"Id": "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
				"Name": "`Data_Set_Hello_World_One`"
			},
			{
				"Id": "`5bgd734EXAMPLE100f7gdd9EXAMPLEe9`",
				"Name": "`Data_Set_Hello_World_Two`"
			}
		],
		"Product": {
			"Id": "prod-`uEXAMPLEabc1d`",
			"Name": "`Product_Hello_World`"
		}
	}
}
```

## Events for adding AWS Lake Formation data permission

data sets

When a provider adds an AWS Lake Formation data permission data set to a product and publishes
it, the subscriber receives an event with the `Lake
 Formation Data Permission Data Sets Published To Product` detail type.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Lake Formation Data Permission Data Sets Published To Product",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2021-12-15T18:24:04Z`",
    "region": "`us-east-1`",
    "resources": [
        "prod-`uEXAMPLEabc1d`"
    ],
    "detail": {
        "DataSetIds": [
            "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
            "`5bgd734EXAMPLE100f7gdd9EXAMPLEe9`"
        ],
        "DataSets": [
            {
                "Id": "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
                "Name": "`Data_Set_Hello_World_One`"
            },
            {
                "Id": "`5bgd734EXAMPLE100f7gdd9EXAMPLEe9`",
                "Name": "`Data_Set_Hello_World_Two`"
            }
        ],
        "Product": {
            "Id": "prod-`uEXAMPLEabc1d`",
            "Name": "`Product_Hello_World`"
        }
    }
}
```

## Events for adding Amazon Redshift datashare data sets

When a provider adds an Amazon Redshift datashare data set to a product and publishes it, the
subscriber receives an event with the `Redshift Data Shares
 Data Sets Published To Product` detail type.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Redshift Data Shares Data Sets Published To Product",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2021-12-15T18:24:04Z`",
    "region": "`us-east-1`",
    "resources":  [
        "prod-`uEXAMPLEabc1d`"
    ],
    "detail":  {
        "DataSetIds":  [
            "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
            "`5bgd734EXAMPLE100f7gdd9EXAMPLEe9`"
        ],
        "DataSets": [
            {
               "Id" : "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
               "Name": "`Data_Set_Hello_World_One`"
            },
            {
               "Id" : "`5bgd734EXAMPLE100f7gdd9EXAMPLEe9`",
               "Name": "`Data_Set_Hello_World_Two`"
            }
        ],
        "Product":
        {
            "Id" : "`prod-uEXAMPLEabc1d`",
            "Name": "`Product_Hello_World`"
        }

    }
}
```

## Events for adding Amazon API Gateway API

data sets

When a provider adds an Amazon API Gateway API data set to a product and publishes it, the
subscriber receives an event with the `Amazon API Gateway Data Sets
 Published To Product` detail type.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "API Gateway API Data Sets Published To Product",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2021-12-15T18:24:04Z`",
    "region": "`us-east-1`",
    "resources":  [
        "prod-`uEXAMPLEabc1d`"
    ],
    "detail":  {
        "DataSetIds":  [
            "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
            "`5bgd734EXAMPLE100f7gdd9EXAMPLEe9`"
        ],
        "DataSets":  [
            {
                "Id" : "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
                "Name": "`Data_Set_Hello_World_One`"
            },
            {
                "Id" : "`5bgd734EXAMPLE100f7gdd9EXAMPLEe9`",
                "Name": "`Data_Set_Hello_World_Two`"
            }
        ],
        "Product":  {
            "Id" : "prod-`uEXAMPLEabc1d`",
            "Name": "`Product_Hello_World`"
        }
    }
}
```

## Events for adding revisions

When a provider adds a data set to a product and publishes it, the subscriber receives
an event with the `Revision Published To Data Set` detail type.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Revision Published To Data Set",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2020-07-29T04:16:28Z`",
    "region": "`us-east-1`",
    "resources":  [
        "`aae4c2cdEXAMPLE54f9369dEXAMPLE66`"
    ],
    "detail":  {
        "RevisionIds":  [
            "`3afc623EXAMPLE099e6fcc8EXAMPLEe7`"
        ],
        "Revisions": [
            {
                "Id" : "`3afc623EXAMPLE099e6fcc8EXAMPLEe7`",
                "Comment": "`Revision_Comment_One`"
            }
         ],
        "DataSets":  [
            {
                "Id" : "`aae4c2cdEXAMPLE54f9369dEXAMPLE66`",
                "Name": "`Data_Set_Hello_World_One`"
            }
         ],
        "Product":  {
            "Id" : "prod-`uEXAMPLEabc1d`",
            "Name": "`Product_Hello_World`"
        }
    }
}
```

## Events for adding Amazon S3 data access data set

revisions

When a provider adds an Amazon S3 data access data set revision to a product and publishes
it, the subscriber receives an event with the `Revision
 Published To Amazon S3 Data Access Data Set` detail type.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Revision Published to S3 Data Access Data Set(s)",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2020-07-29T04:16:28Z`",
    "region": "`us-east-1`",
    "resources":  [
        "`aae4c2cdEXAMPLE54f9369dEXAMPLE66`"
    ],
    "detail":  {
        "RevisionIds":  [
            "`3afc623EXAMPLE099e6fcc8EXAMPLEe7`"
        ],
        "Revisions": [
            {
                "Id" : "`3afc623EXAMPLE099e6fcc8EXAMPLEe7`",
                "Comment": "`Revision_Comment_One`"
            }
         ],
        "DataSets":  [
            {
                "Id" : "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
                "Name": "`Data_Set_Hello_World_One`"
            }
         ],
        "Product":  {
            "Id" : "prod-`uEXAMPLEabc1d`",
            "Name": "`Product_Hello_World`"
        }
    }
}
```

## Events for adding AWS Lake Formation data permission data

set revisions (Preview)

When a provider adds an AWS Lake Formation data permission data set revision to a product and
publishes it, the subscriber receives an event with the `Revision Published to Lake
 Formation Data Permission Data Set` detail type.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Revision Published to Lake Formation Data Permission Data Set",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2021-12-15T18:24:04Z`",
    "region": "`us-east-1`",
    "resources": [
        "prod-`uEXAMPLEabc1d`"
    ],
    "detail": {
        "DataSetIds": [
            "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
            "`5bgd734EXAMPLE100f7gdd9EXAMPLEe9`"
        ],
        "DataSets": [
            {
                "Id": "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
                "Name": "`Data_Set_Hello_World_One`"
            },
            {
                "Id": "`5bgd734EXAMPLE100f7gdd9EXAMPLEe9`",
                "Name": "`Data_Set_Hello_World_Two`"
            }
        ],
        "Product": {
            "Id": "prod-`uEXAMPLEabc1d`",
            "Name": "`Product_Hello_World`"
        }
    }
}
```

## Events for adding Amazon Redshift datashare data set

revisions

When a provider adds an Amazon Redshift datashare data set revision to a product and publishes
it, the subscriber receives an event with the `Revision
 Published To Redshift Data Shares Data Set` detail type.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Revision Published To Redshift Data Shares Data Set",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2021-12-15T18:24:04Z`",
    "region": "`us-east-1`",
    "resources":  [
        "`aae4c2cdEXAMPLE54f9369dEXAMPLE66`"
    ],
    "detail":  {
        "RevisionIds":  [
            "`3afc623EXAMPLE099e6fcc8EXAMPLEe7`"
        ],
        "Revisions": [
            {
                "Id" : "`3afc623EXAMPLE099e6fcc8EXAMPLEe7`",
                "Comment": "`Revision_Comment_One,`"
            }
         ],
        "DataSets":  [
            {
                "Id" : "`aae4c2cdEXAMPLE54f9369dEXAMPLE66`",
                "Name": "`Data_Set_Hello_World_One`"
            }
         ],
        "Product":  {
            "Id" : "prod-`uEXAMPLEabc1d`",
            "Name": "`Product_Hello_World`"
        }
    }
}
```

## Events for adding

Amazon API Gateway API data set revisions

When a provider adds an Amazon API Gateway API data set revision to a product and publishes it,
the subscriber receives an event with the `Revision
 Published To API Gateway Data Set` detail type.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Revision Published To API Gateway API Data Set",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2021-12-15T18:24:04Z`",
    "region": "`us-east-1`",
    "resources":  [
        "`aae4c2cdEXAMPLE54f9369dEXAMPLE66`"
    ],
    "detail":  {
        "RevisionIds":  [
            "`3afc623EXAMPLE099e6fcc8EXAMPLEe7`"
        ],
        "Revisions": [
            {
                "Id" : "`3afc623EXAMPLE099e6fcc8EXAMPLEe7`",
                "Comment": "`Revision_Comment_One`"
            }
         ],
        "DataSets":  [
            {
                "Id" : "aae4c2cdEXAMPLE54f9369dEXAMPLE66",
                "Name": "`Data_Set_Hello_World_One`"
            }
         ],
        "Product":  {
            "Id" : "prod-u`EXAMPLEabc1d`",
            "Name": "`Product_Hello_World`"
        }
    }
}
```

The following table describes the API Gateway API data set revision error codes.

| Error code                          | Message                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CLUSTER_DELETED`                   | `The datashare is unavailable because the provider deleted their<br>cluster. Please contact the provider for more<br>information.`                                                                                                       | This message is sent when the datashare is no longer available<br>because the provider deleted the cluster containing the<br>datashare.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `CLUSTER_ENCRYPTION_DISABLED`       | `The datashare is unavailable because the provider disabled<br>encryption on their cluster. Please contact the provider for more<br>information.`                                                                                        | This message is sent when the datashare is no longer available<br>because the provider disabled encryption on their cluster. To use a<br>datashare, both the provider and the subscriber must have encryption<br>enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `DATASHARE_DELETED`                 | `The datashare is unavailable because the provider deleted the<br>datashare. Please contact the provider for more<br>information.`                                                                                                       | This message is sent when the datashare is no longer available<br>because the provider deleted it. The provider must create a new<br>datashare so that you can regain access to the data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `DATASHARE_DEAUTHORIZED`            | `The datashare is unavailable because the provider de-authorized<br>the datashare. Please contact the provider for more<br>information.`                                                                                                 | This message is sent when the datashare is no longer available<br>because the provider reauthorized the datashare. The provider must<br>create a new datashare so that you can regain access to the<br>data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `DATASHARE_PUBLIC_CONSUMER_BLOCKED` | `You cannot access a non-publicly accessible datashare from a<br>publicly accessible cluster. You must turn off public accessibility<br>on your cluster to access this datashare. Please contact your<br>provider for more information.` | This message is sent when a provider sets the **Publicly accessible\*<br>• option to **Disable*<br>• on the cluster that contains<br>their datashare. If the subscriber's cluster has the \*\*Publicly accessible*<br>• option set to<br>**Disable**, it will not affect<br>their ability to access the datashare. For the subscriber to access<br>the datashare, either the subscriber must set the **Publicly accessible\*<br>• option to **Disable*<br>• on their cluster, or the<br>provider must set the \*\*Publicly<br>accessible*<br>• option to **Enable\*<br>• on their cluster.<br>**Disable*<br>• on the cluster that contains<br>their datashare. If the subscriber's cluster has the \*\*Publicly accessible*<br>• option set to **Disable**, it will not affect their ability to<br>access the datashare. For the subscriber to access the datashare, either<br>the subscriber must set the **Publicly<br>accessible\*<br>• option to **Disable*<br>• on their cluster, or the provider must set the \*\*Publicly accessible*<br>• option to \*_Enable_<br>• on their cluster. |

## Events for revoking revisions

When a provider revokes a revision to a product and publishes it, the subscriber
receives an event with the `Revision Revoked` detail type.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Revision Revoked",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2022-02-17T21:25:06Z`",
    "region": "`us-east-1`",
    "resources":  [
        "`aae4c2cdEXAMPLE54f9369dEXAMPLE66`"
    ],
    "detail":  {
        "RevisionIds":  [
            "`3afc623EXAMPLE099e6fcc8EXAMPLEe7`"
        ],
        "RevocationComment": "`example revocation comment`",
        "Revisions": [
            {
                "Id" : "`3afc623EXAMPLE099e6fcc8EXAMPLEe7`",
                "Comment": "`Revision_Comment_One`"
            }
         ],
        "DataSets":  [
            {
                "Id" : "`aae4c2cdEXAMPLE54f9369dEXAMPLE66`",
                "Name": "`Data_Set_Hello_World_One`"
            }
         ],
        "Product":  {
            "Id" : "prod-`uEXAMPLEabc1d`",
            "Name": "`Product_Hello_World`"
        }
    }
}
```

## Events for an action performed on an Amazon Redshift

resource

When a provider takes an action on their Amazon Redshift resources that _might_ remove access from a subscriber, the subscriber receives an event
with the `Action Performed On Redshift Data Share By
 Provider` detail type.

For example, if a provider changes the data share's public accessibility setting from
`true` to `false`, the subscriber receives an event.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Action Performed On Redshift Data Share By Provider",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2021-12-15T18:24:04Z`",
    "region": "`us-east-1`",
    "resources":  [
        "arn:aws:redshift:`us-east-1`:`098765432123`:datashare:`01234567-2590-7654-1234-f57ea0081234`/`test_data_share`"
    ],
    "detail":  {
        "Message": "`This is an example message which explains why you may have lost access.`",
        "AssociatedProducts":  [
            {
                "ProductId": "`aae4c2cdEXAMPLE54f9369dEXAMPLE66`",
                "DataSetIds":  [
                    "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`"
                ],
                "DataSets":  [
                    {
                        "Id" : "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
                        "Name": "`Data_Set_Hello_World_One`"
                    }
                ],
                "Product":  {
                    "Id" : "`aae4c2cdEXAMPLE54f9369dEXAMPLE66`",
                    "Name": "`Product_Hello_World`"
                }
            }
        ]
    }
}
```

## Events for losing access to an Amazon Redshift

datashare

When a provider takes an action on their Amazon Redshift resources that removes access from a
subscriber, the subscriber receives an event with the `Redshift Data Share Access Lost` detail type.

For example, if a provider deletes an Amazon Redshift datashare or deletes a cluster, the
subscriber receives an event.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Redshift Data Share Access Lost",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2021-12-15T18:24:04Z`",
    "region": "`us-east-1`",
    "resources":  [
        "arn:aws:redshift:`us-east-1`:`098765432123`:datashare:`01234567-2590-7654-1234-f57ea0081234`/`test_data_share`"
    ],
    "detail":  {
        "Message": "`This is an example message which explains why you may have lost access.`",
        "AssociatedProducts":  [
            {
                "ProductId": "`aae4c2cdEXAMPLE54f9369dEXAMPLE66`",
                "DataSetIds":  [
                    "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`"
                ],
                "DataSets":  [
                    {
                        "Id" : "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
                        "Name": "`Data_Set_Hello_World_One`"
                    }
                ],
                "Product":  {
                    "Id" : "prod-`uEXAMPLEabc1d`",
                    "Name": "`Product_Hello_World`"
                }
            }
        ]
    }
}

```

## Events for an auto-export job completed

After an auto-export job moves all the data in a newly published File data set
revision to the subscriber's chosen Amazon S3 bucket, the subscriber receives an event with the
`Auto-export Job Completed` detail type.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Auto-export Job Completed",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2020-07-29T18:24:04Z`",
    "region": "`us-east-1`",
    "resources": [
        "prod-`uEXAMPLEabc1d`"
    ],
    "detail": {
        "RevisionIds": [
            "`3afc623EXAMPLE099e6fcc8EXAMPLEe7`"
        ],
        "Revisions": [{
            "Id": "`3afc623EXAMPLE099e6fcc8EXAMPLEe7`",
            "Comment": "`Revision_Comment_One`"
        }],
        "DataSetIds": [
            "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
        ],
        "DataSets": [{
            "Id": "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
            "Name": "`Data_Set_Hello_World_One`"
        }, ],
        "Product": {
            "Id": "prod-`uEXAMPLEabc1d`",
        }
    }
}
```

## Events for an auto-export job

failed

When an auto-export job fails, the subscriber receives an event with the `Auto-export Job
 Failed` detail type.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Auto-Export job failed",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2020-07-29T18:24:04Z`",
    "region": "`us-east-1`",
    "resources": [
        "`prod-uEXAMPLEabc1d`"
    ],
    "detail": {
        "RevisionIds": [
            "`3afc623EXAMPLE099e6fcc8EXAMPLEe7`"
        ],
        "Revisions": [{
            "Id": "`3afc623EXAMPLE099e6fcc8EXAMPLEe7`",
            "Comment": "`Revision_Comment_One`"
        }],
        "DataSetIds": [
            "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
            "`5bgd734EXAMPLE100f7gdd9EXAMPLEe9`"
        ],
        "DataSets": [{
                "Id": "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
                "Name": "`Data_Set_Hello_World_One`"
            },
            {
                "Id": "`5bgd734EXAMPLE100f7gdd9EXAMPLEe9`",
                "Name": "`Data_Set_Hello_World_Two`"
            }
        ],
        "Product": {
            "Id": "prod-`uEXAMPLEabc1d`",
        }
    }
}
```

## Events for

a provider-generated notification of a data update

When a provider sends a notification for a data update, the subscriber receives an
event with the `Data Updated in Data
 Set` detail type.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Data Updated in Data Set",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2023-08-21T10:29:48Z`",
    "region": "`us-east-1`",
    "resources": [
        "arn:aws:dataexchange:`us-east-1`::data-sets/`b5538f9f45e4613d448eb9eEXAMPLEc6`"
    ],
    "detail": {
        "DataSet": {
            "Id": "`b5538f9f45e4613d448eb9eEXAMPLEc6`",
            "Name": "`Example Data Set`",
            "AssetType": "S3_DATA_ACCESS"
        },
        "Product": {
            "Id": "prod-`7ip6EXAMPLEhs`",
            "Name": "`Example Data Product`",
            "ProviderContact": "`no-reply@marketplace.aws`"
        },
        "Notification": {
            "Comment": "`This is a test DATA_UPDATE notification.`",
            "Type": "DATA_UPDATE",
            "Details": {
                "DataUpdate": {
                    "DataUpdatedAt": "`2023-07-12T00:00:00Z`"
                }
            },
            "Scope": {
                "S3DataAccesses": [{
                    "KeyPrefixes": [
                        "`KeyPrefix`"
                    ],
                    "Keys": [
                        "`KeyA`",
                        "`KeyB`"
                    ]
                }]
            }
        }
    }
}

```

## Events

for a provider-generated notification of a schema change

When a provider sends a notification for a schema change, the subscriber receives an
event with the `Schema Change Planned for Data
 Set` detail type.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Schema Change Planned for Data Set",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2023-08-21T10:29:48Z`",
    "region": "`us-east-1`",
    "resources": [
        "arn:aws:dataexchange:`us-east-1`::data-sets/`b5538f9f45e4613d448eb9eEXAMPLEc6`"
    ],
    "detail": {
        "DataSet": {
            "Id": "`b5538f9f45e4613d448eb9eEXAMPLEc6`",
            "Name": "`Example Data Set`",
            "AssetType": "S3_DATA_ACCESS"
        },
        "Product": {
            "Id": "prod-`7ip6EXAMPLEhs`",
            "Name": "`Example Data Product`",
            "ProviderContact": "`no-reply@marketplace.aws`"
        },
        "Notification": {
            "Comment": "`This is a test SCHEMA_CHANGE notification.`",
            "Type": "SCHEMA_CHANGE",
            "Details": {
                "SchemaChange": {
                    "Changes": [{
                            "Type": "`ADD`",
                            "Description": "`This object is being added to the bucket, or a field is being added to the object.`",
                            "Name": "`KeyA`"
                        },
                        {
                            "Type": "`REMOVE`",
                            "Description": "`This object is being removed from the bucket or a field is being removed from the object.`",
                            "Name": "`KeyB`"
                        },
                        {
                            "Type": "`MODIFY`",
                            "Description": "`The usage or meaning of this key prefix is changing, or something is changing about every file under this key prefix.`",
                            "Name": "`KeyPrefix`"
                        }
                    ],
                    "SchemaChangeAt": "`2023-09-08T13:46:01Z`"
                }
            },
            "Scope": {
                "S3DataAccesses": [{
                    "KeyPrefixes": [
                        "`KeyPrefix`"
                    ],
                    "Keys": [
                        "`KeyA`",
                        "`KeyB`"
                    ]
                }]
            }
        }
    }
}
```

## Events for a

provider-generated notification of a data delay

When a provider sends a notification for a data delay, the subscriber receives an
event with the following detail type: **Data Set Update
Delayed**.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Data Set Update Delayed",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "2023-08-21T10:29:48Z",
    "region": "`us-east-1`",
    "resources": [
        "arn:aws:dataexchange:`us-east-1`::data-sets/`b5538f9f45e4613d448eb9eEXAMPLEc6`"
    ],
    "detail": {
        "DataSet": {
            "Id": "`b5538f9f45e4613d448eb9eEXAMPLEc6`",
            "Name": "`Example Data Set`",
            "AssetType": "S3_DATA_ACCESS"
        },
        "Product": {
            "Id": "`prod-7ip6EXAMPLEhs`",
            "Name": "`Example Data Product`",
            "ProviderContact": "`no-reply@marketplace.aws`"
        },
        "Notification": {
            "Comment": "`This is a test DATA_DELAY notification.`",
            "Type": "DATA_DELAY",
            "Scope": {
                "S3DataAccesses": [{
                    "KeyPrefixes": [
                        "`KeyPrefix`"
                    ],
                    "Keys": [
                        "`KeyA`",
                        "`KeyB`"
                    ]
                }]
            }
        }
    }
}
```

## Events for

a provider-generated notification of a data deprecation

When a provider sends a notification for a data deprecation, the subscriber receives
an event with the `Deprecation Planned for Data
 Set` detail type.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Deprecation Planned for Data Set",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2023-08-21T10:29:48Z`",
    "region": "`us-east-1`",
    "resources": [
        "arn:aws:dataexchange:`us-east-1`::data-sets/`b5538f9f45e4613d448eb9eEXAMPLEc6`"
    ],
    "detail": {
        "DataSet": {
            "Id": "`b5538f9f45e4613d448eb9eEXAMPLEc6`",
            "Name": "`Example Data Set`",
            "AssetType": "S3_DATA_ACCESS"
        },
        "Product": {
            "Id": "prod-`7ip6EXAMPLEhs`",
            "Name": "`Example Data Product`",
            "ProviderContact": "`no-reply@marketplace.aws`"
        },
        "Notification": {
            "Comment": "`This is a test DEPRECATION notification.`",
            "Type": "DEPRECATION",
            "Details": {
                "Deprecation": {
                    "DeprecationAt": "`2023-09-08T13:46:01Z`"
                }
            },
            "Scope": {
                "S3DataAccesses": [{
                    "KeyPrefixes": [
                        "`KeyPrefix`"
                    ],
                    "Keys": [
                        "`KeyA`",
                        "`KeyB`"
                    ]
                }]
            }
        }
    }
}
```

## Events for accepting a data grant

When a data consumer accepts a data grant, the data owner receives an event with the `Data Grant Accepted` detail type.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Data Grant Accepted",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2022-02-17T21:25:06Z`",
    "region": "`us-east-1`",
    "resources":  [
        "arn:aws:dataexchange:`us-east-1`::data-sets/`4afc623EXAMPLE099e6fcc8EXAMPLEe8`"
    ],
    "detail":  {
        "DataSets":  [
            {
                "Id" : "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
                "Name": "`Data_Set_Hello_World_One`"
            }
         ],
        "DataGrant":  {
            "Arn" : "arn:aws:dataexchange:`us-east-1`:`123456789012`:data-grants/`4afc623EXAMPLE099e6fcc8EXAMPLEe9`",
            "Name": "`DataGrant_Hello_World`"
        }
    }
}
```

## Events for extending data grants

When a data owner extends a data grant, the data consumer receives an event with the `Data Grant Extended` detail type.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Data Grant Extended",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2022-02-17T21:25:06Z`",
    "region": "`us-east-1`",
    "resources":  [
        "arn:aws:dataexchange:`us-east-1`::data-sets/`4afc623EXAMPLE099e6fcc8EXAMPLEe8`"
    ],
    "detail":  {
        "DataSets":  [
            {
                "Id" : "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
                "Name": "`Data_Set_Hello_World_One`"
            }
         ],
         "DataGrant":  {
            "Arn" : "arn:aws:dataexchange:`us-east-1`:`123456789012`:data-grants/`4afc623EXAMPLE099e6fcc8EXAMPLEe9`",
            "Name": "`DataGrant_Hello_World`"
        }
    }
}
```

## Events for revoking a data grant

When a data owner revokes a data grant, the data consumer receives an event with the `Data Grant Revoked` detail type.

The following example shows the event body for the detail type.

```
{
    "version": "0",
    "id": "`dc529cb6-2e23-4c5f-d020-EXAMPLE92231`",
    "detail-type": "Data Grant Revoked",
    "source": "aws.dataexchange",
    "account": "`123456789012`",
    "time": "`2022-02-17T21:25:06Z`",
    "region": "`us-east-1`",
    "resources":  [
        "arn:aws:dataexchange:`us-east-1`::data-sets/`4afc623EXAMPLE099e6fcc8EXAMPLEe8`"
    ],
    "detail":  {
        "DataSets":  [
            {
                "Id" : "`4afc623EXAMPLE099e6fcc8EXAMPLEe8`",
                "Name": "`Data_Set_Hello_World_One`"
            }
         ],
         "DataGrant":  {
            "Arn" : "arn:aws:dataexchange:`us-east-1`:`123456789012`:data-grants/`4afc623EXAMPLE099e6fcc8EXAMPLEe9`",
            "Name": "`DataGrant_Hello_World`"
        }
    }
}
```
