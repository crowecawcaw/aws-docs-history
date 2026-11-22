

# Case event payload and schema in Connect Customer Cases

When you request to include case data in the event payload, the data reflects the version of the case after that particular edit. 

Connect Customer Cases default limits guarantee that the payload will be less than 256KB (the maximum size of an EventBus event). Since you can customize the case object model (for example, you can define custom fields on case objects to capture business specific information), case event schema reflect the customizations made to the case object as shown in the following examples (for example, see how customer-specific UUIDs are being use as JSON properties). 

## Example case event payload for the case resource
<a name="example-case-event-payload"></a>

```json
// Given the limits on the "includedData" configuration
// this payload is guaranteed to less than 256KB at launch.
{
    "version": "0",
    "id": "{{event ID}}",
    "detail-type": "Amazon Connect Cases Change",
    "source": "aws.cases",
    "account": "{{your AWS account ID}}",
    "time": "2022-03-16T23:43:26Z",
    "region": "{{The AWS Region of your Connect Customer instance}}",
    "resources": [
        "arn:aws:cases:{{your Connect Customer AWS Region}}:{{your AWS account ID}}:domain/{{case domain ID}}",
        "arn:aws:cases:{{your Connect Customer AWS Region}}:{{your AWS account ID}}:domain/{{case domain ID}}/case/{{case ID}}"
    ],
    "detail": {
        "version": "0",
        "eventType": "CASE.UPDATED",
        "approximateChangeTime": "2022-03-16T23:16:57.893Z",  // Can be used for ordering
        "changedFieldIds": ["status", "last_updated_datetime"],
        "performedBy": {
            "user": {
                "userArn": "arn:aws:connect:{{your Connect Customer AWS Region}}:{{your AWS account ID}}:instance/{{connect instance ID}}/user/{{connect user ID}}"        
            },
            "iamPrincipalArn": "arn:aws:iam::{{your Connect Customer AWS Region}}:role/{{role name}}"
        },       
        "case": {
            "caseId": "{{case ID}}",
            "templateId": "{{template ID}}",
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

## Example case event payload for the related-item resource
<a name="example-case-event-payload"></a>

```json
// Given the limits on the "includedData" configuration
// this payload is guaranteed to less than 256KB
{
    "version": "0",
    "id": "{{event ID}}",
    "detail-type": "Amazon Connect Cases Change",
    "source": "aws.cases",
    "account": "{{your AWS account ID}}",
    "time": "2022-03-16T23:43:26Z",
    "region": "{{The AWS Region of your Connect Customer instance}}",
    "resources": [
        "arn:aws:cases:{{your Connect Customer AWS Region}}:{{your AWS account ID}}:domain/{{case domain ID}}",
        "arn:aws:cases:{{your Connect Customer AWS Region}}:{{your AWS account ID}}:domain/{{case domain ID}}/case/{{case ID}}/related-item/{{related-item ID}}"
    ],
    
    "detail": {   
        "version": "0",
        "eventType": "RELATED_ITEM.CREATED",
        "approximateChangeTime": "2022-03-16T23:16:57.893Z", // Can be used for ordering
        "changedAttributes": ["comment.commentText"],
        "performedBy": {
            "user": {
                "userArn": "arn:aws:connect:{{your Connect Customer AWS Region}}:{{your AWS account ID}}:instance/{{connect instance ID}}/user/{{connect user ID}}"        
            },
            "iamPrincipalArn": "arn:aws:iam::{{your Connect Customer AWS Region}}:role/{{role name}}"
        },        
        "relatedItem": {
            "relatedItemType": "Comment",
            "relatedItemId": "{{related-item ID}}",
            "caseId": "{{case id that this related item is a sub-resource of}}",
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

## Example case event payload for an SLA related item
<a name="example-case-event-payload-sla-related-item"></a>

When an SLA is created, met, or breached, the event carries a related item of type `Sla`. Creating an SLA sends `eventType` `RELATED_ITEM.CREATED`, and a later change to its status sends `RELATED_ITEM.UPDATED`. Both the `sla` object and `assignedUser` appear only when the domain's event configuration sets `relatedItemData.includeContent` to `true`.

The `fieldId` is the case field the SLA tracks, and `targetFieldValues` are the values that meet it. The field can be any single-select case field, including a custom field. For information about configuring these, see [How SLAs work in Connect Customer Cases](cases-sla.md).

The `assignedUser` is the user assigned to the case at the time of the event, and is the value that the **Select the agent who is assigned to the case** notification recipient resolves to. The payload also omits `assignedUser` when no user is assigned to the case, even if `includeContent` is `true`.

Replace {{related-item-id}}, {{case-id}}, {{region}}, {{account-id}}, {{instance-id}}, and {{user-id}} with your own values. The following JSON example shows a case event payload for an SLA related item:

```json
{
    // The envelope fields, and the other fields of "detail", match the
    // related-item example above.
    "detail": {
        "eventType": "RELATED_ITEM.UPDATED",
        "relatedItem": {
            "relatedItemType": "Sla",
            "relatedItemId": "{{related-item-id}}",
            "caseId": "{{case-id}}",
            "createdDateTime": "2026-11-19T23:16:57.893Z",

            // assignedUser and sla are present only when
            // relatedItemData.includeContent is true. assignedUser is also
            // omitted when no user is assigned to the case.
            "assignedUser": "arn:aws:connect:{{region}}:{{account-id}}:instance/{{instance-id}}/agent/{{user-id}}",

            "sla": {
                "slaConfiguration": {
                    "name": "Resolution SLA",
                    "type": "CaseField",
                    "status": "Overdue",
                    "fieldId": "custom-field-uuid-1",
                    "targetFieldValues": [
                        {
                            "stringValue": "resolved"
                        }
                    ],
                    "targetTime": "2026-11-19T23:15:00.000Z",
                    "completionTime": null
                }
            }
        }
    }
}
```

The event includes the following SLA status values.
+ `Active` – the SLA is not yet fulfilled and the target time has not passed.
+ `Met` – the SLA was fulfilled before the target time.
+ `NotMet` – the SLA was fulfilled after the target time had passed.
+ `Overdue` – the SLA is not yet fulfilled and the target time has passed.

**Note**  
The event carries these four values only. **Due soon**, which the agent workspace shows when the target time is less than 24 hours away, is presentation only and never appears in the payload. The payload sets `completionTime` only after the SLA reaches `Met` or `NotMet`.

## Example case event payload for the case resource performed by custom entity
<a name="example-case-event-payload-case-resource-custom-entity"></a>

```json
// Given the limits on the "includedData" configuration
// this payload is guaranteed to less than 256KB at launch.
{
    "version": "0",
    "id": "{{event ID}}",
    "detail-type": "Amazon Connect Cases Change",
    "source": "aws.cases",
    "account": "{{your AWS account ID}}",
    "time": "2022-03-16T23:43:26Z",
    "region": "{{The AWS Region of your Amazon Connect instance}}",
    "resources": [
        "arn:aws:cases:{{your Amazon Connect AWS Region:your AWS account ID}}:domain/{{case domain ID}}",
        "arn:aws:cases:{{your Amazon Connect AWS Region:your AWS account ID}}:domain/{{case domain ID}}/case/{{case ID}}"
    ],
    "detail": {
        "version": "0",
        "eventType": "CASE.UPDATED",
        "approximateChangeTime": "2022-03-16T23:16:57.893Z",  // Can be used for ordering
        "changedFieldIds": ["status", "last_updated_datetime"],
        "performedBy": {
            "user": {
                "customEntity": "{{your custom entity}}"        
            },
            "iamPrincipalArn": "arn:aws:iam::{{your Amazon Connect AWS Region}}:role/{{role name}}"
        },       
        "case": {
            "caseId": "{{case ID}}",
            "templateId": "{{template ID}}",
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