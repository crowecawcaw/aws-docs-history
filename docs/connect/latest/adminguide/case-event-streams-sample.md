# Case event payload and schema in

Amazon Connect Cases

When you request to include case data in the event payload, the data reflects the
version of the case after that particular edit.

Amazon Connect Cases default limits guarantee that the payload will be less than 256KB (the
maximum size of an EventBus event). Since you can customize the case object model (for
example, you can define custom fields on case objects to capture business specific
information), case event schema reflect the customizations made to the case object as
shown in the following examples (for example, see how customer-specific UUIDs are being
use as JSON properties).

## Example case event payload for the case

resource

```
// Given the limits on the "includedData" configuration
// this payload is guaranteed to less than 256KB at launch.
{
    "version": "0",
    "id": "`event ID`",
    "detail-type": "Amazon Connect Cases Change",
    "source": "aws.cases",
    "account": "`your AWS account ID`",
    "time": "2022-03-16T23:43:26Z",
    "region": "`The AWS Region of your Amazon Connect instance`",
    "resources": [
        "arn:aws:cases:`your Amazon Connect AWS Region`:`your AWS account ID`:domain/`case domain ID`",
        "arn:aws:cases:`your Amazon Connect AWS Region`:`your AWS account ID`:domain/`case domain ID`/case/`case ID`"
    ],
    "detail": {
        "version": "0",
        "eventType": "CASE.UPDATED",
        "approximateChangeTime": "2022-03-16T23:16:57.893Z",  // Can be used for ordering
        "changedFieldIds": ["status", "last_updated_datetime"],
        "performedBy": {
            "user": {
                "userArn": "arn:aws:connect:`your Amazon Connect AWS Region`:`your AWS account ID`:instance/`connect instance ID`/user/`connect user ID`"
            },
            "iamPrincipalArn": "arn:aws:iam::`your Amazon Connect AWS Region`:role/`role name`"
        },
        "case": {
            "caseId": "`case ID`",
            "templateId": "`template ID`",
            "createdDateTime": "2022-03-16T23:16:57.893Z",

            // This section contains only non-null field values for the
            // fields that customers have configured in the "includedData".

            // Field values included in this section reflects the case
            // after this particular change is applied.
            "fields": {
                "status": {
                    "value": {
                        "stringValue": "open"
                   }
                },
                "case_reason": {
                    "value": {
                        "stringValue": "Shipment lost"
                    }
                },
                "custom-field-uuid-1": {
                    "value": {
                        "stringValue": "Customer didn't receive the product"
                    }
                }
            }
        }
    }
}
```

## Example case event payload for the

related-item resource

```
// Given the limits on the "includedData" configuration
// this payload is guaranteed to less than 256KB
{
    "version": "0",
    "id": "`event ID`",
    "detail-type": "Amazon Connect Cases Change",
    "source": "aws.cases",
    "account": "`your AWS account ID`",
    "time": "2022-03-16T23:43:26Z",
    "region": "`The AWS Region of your Amazon Connect instance`",
    "resources": [
        "arn:aws:cases:`your Amazon Connect AWS Region`:`your AWS account ID`:domain/`case domain ID`",
        "arn:aws:cases:`your Amazon Connect AWS Region`:`your AWS account ID`:domain/`case domain ID`/case/`case ID`/related-item/`related-item ID`"
    ],

    "detail": {
        "version": "0",
        "eventType": "RELATED_ITEM.CREATED",
        "approximateChangeTime": "2022-03-16T23:16:57.893Z", // Can be used for ordering
        "changedAttributes": ["comment.commentText"],
        "performedBy": {
            "user": {
                "userArn": "arn:aws:connect:`your Amazon Connect AWS Region`:`your AWS account ID`:instance/`connect instance ID`/user/`connect user ID`"
            },
            "iamPrincipalArn": "arn:aws:iam::`your Amazon Connect AWS Region`:role/`role name`"
        },
        "relatedItem": {
            "relatedItemType": "Comment",
            "relatedItemId": "`related-item ID`",
            "caseId": "`case id that this related item is a sub-resource of`",
            "createdDateTime": "2022-03-16T23:16:57.893Z",

            // This section includes any attributes that customers have configured
            // in the "includedData" configuration.
            "comment": {
                "body": "Gave a $5 refund to customer to make them happy",
            },

            // if the related item was of type contact.
            // "contact": {
            //      "contactArn": ".......",
            // }
        }
    }
}
```

## Example

case event payload for the case resource performed by custom entity

```
// Given the limits on the "includedData" configuration
// this payload is guaranteed to less than 256KB at launch.
{
    "version": "0",
    "id": "`event ID`",
    "detail-type": "Amazon Connect Cases Change",
    "source": "aws.cases",
    "account": "`your AWS account ID`",
    "time": "2022-03-16T23:43:26Z",
    "region": "`The AWS Region of your Amazon Connect instance`",
    "resources": [
        "arn:aws:cases:`your Amazon Connect AWS Region:your AWS account ID`:domain/`case domain ID`",
        "arn:aws:cases:`your Amazon Connect AWS Region:your AWS account ID`:domain/`case domain ID`/case/`case ID`"
    ],
    "detail": {
        "version": "0",
        "eventType": "CASE.UPDATED",
        "approximateChangeTime": "2022-03-16T23:16:57.893Z",  // Can be used for ordering
        "changedFieldIds": ["status", "last_updated_datetime"],
        "performedBy": {
            "user": {
                "customEntity": "`your custom entity`"
            },
            "iamPrincipalArn": "arn:aws:iam::`your Amazon Connect AWS Region`:role/`role name`"
        },
        "case": {
            "caseId": "`case ID`",
            "templateId": "`template ID`",
            "createdDateTime": "2022-03-16T23:16:57.893Z",

            // This section contains only non-null field values for the
            // fields that customers have configured in the "includedData".

            // Field values included in this section reflects the case
            // after this particular change is applied.
            "fields": {
                "status": {
                    "value": {
                        "stringValue": "open"
                   }
                },
                "case_reason": {
                    "value": {
                        "stringValue": "Shipment lost"
                    }
                },
                "custom-field-uuid-1": {
                    "value": {
                        "stringValue": "Customer didn't receive the product"
                    }
                }
            }
        }
    }
}
```
