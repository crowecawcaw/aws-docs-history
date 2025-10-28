# Default calculated

attributes in Amazon Connect Customer Profiles

## Default CTR

calculated attributes

Amazon Connect Customer Profiles provides out-of-the box default attributes based on
contact records. The attributes are as follows:

**Most frequent channel**

```

{
   "CalculatedAttributeName": "_most_frequent_channel",
   "DisplayName": "Most frequent channel",
   "Description": "Returns customer's frequently used communication channel. Channels include voice, chat, task.",
   "CreatedAt": null,
   "LastUpdatedAt": null,
   "Statistic": "MAX_OCCURRENCE",
   "Conditions": {
      "Range": {
         "Value": 30,
         "Unit": "DAYS"
       },
       "ObjectCount": null
   },
   "AttributeDetails": {
      "Attributes": [
         {
            "Name": "channel"
         }
      ],
      "Expression": "{CTR.channel}"
   },
   "Tags": {
   }
}

```

**Last channel**

```

{
   "CalculatedAttributeName": "_last_channel",
   "DisplayName": "Last channel",
   "Description": "Returns customer's last communication channel. Channels include voice, chat, task.",
   "CreatedAt": null,
   "LastUpdatedAt": null,
   "Statistic": "LAST_OCCURRENCE",
   "Conditions": {
      "ObjectCount": null
   },
   "AttributeDetails": {
      "Attributes": [
         {
            "Name": "channel"
         }
       ],
       "Expression": "{CTR.channel}"
   },
   "Tags": {
   }
}

```

**Last agent identifier**

```

{
   "CalculatedAttributeName": "_last_agent_id",
   "DisplayName": "Last agent identifier",
   "Description": "Returns identifier of the last agent customer connected with.",
   "CreatedAt": null,
   "LastUpdatedAt": null,
   "Statistic": "LAST_OCCURRENCE",
   "Conditions": {
      "ObjectCount": null
   },
   "AttributeDetails": {
      "Attributes": [
         {
            "Name": "agent.id"
         }
      ],
      "Expression": "{CTR.agent.id}"
   },
   "Tags": {
   }
}

```

**Frequent caller**

```

{
   "CalculatedAttributeName": "_frequent_caller",
   "DisplayName": "Frequent caller",
   "Description": "Returns true or false based on the number of times a customer has called.",
   "CreatedAt": null,
   "LastUpdatedAt": null,
   "Statistic": "COUNT",
   "Conditions": {
      "Range": {
         "Value": 30,
         "Unit": "DAYS"
      },
      "ObjectCount": null,
      "Threshold": {
         "Value": "5",
         "Operator": "GREATER_THAN"
      }
   },
   "AttributeDetails": {
      "Attributes": [
         {
            "Name": "contactId"
         }
      ],
      "Expression": "{CTR.contactId}"
   },
   "Tags": {
   }
}

```

**Average hold time**

```

{
   "CalculatedAttributeName": "_average_hold_time",
   "DisplayName": "Average hold time",
   "Description": "Returns customer's average hold time for voice calls.",
   "CreatedAt": null,
   "LastUpdatedAt": null,
   "Statistic": "AVERAGE",
   "Conditions": {
      "Range": {
         "Value": 30,
         "Unit": "DAYS"
      },
      "ObjectCount": null
   },
   "AttributeDetails": {
      "Attributes": [
         {
            "Name": "agent.customerHoldDurationMillis"
         },
         {
            "Name": "queue.durationMillis"
         }
      ],
      "Expression": "{CTR.agent.customerHoldDurationMillis} + {CTR.queue.durationMillis}"
   },
   "Tags": {
   }
}

```

**Average call duration**

```

{
   "CalculatedAttributeName": "_average_call_duration",
   "DisplayName": "Average call duration",
   "Description": "Returns customer's average call duration for voice calls.",
   "CreatedAt": null,
   "LastUpdatedAt": null,
   "Statistic": "AVERAGE",
   "Conditions": {
      "Range": {
         "Value": 30,
         "Unit": "DAYS"
       },
      "ObjectCount": null
   },
   "AttributeDetails": {
      "Attributes": [
         {
            "Name": "disconnectTimestamp"
         },
         {
            "Name": "initiationTimestamp"
         }
      ],
      "Expression": "{CTR.disconnectTimestamp} - {CTR.initiationTimestamp}"
   },
   "Tags": {
   }
}

```

**Customer's maximum hold time**

```

{
    "CalculatedAttributeName": "_maximum_hold_time",
    "DisplayName": "Customer's maximum hold time",
    "Description": "Returns customer's maximum hold time for voice calls in the past month.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "agent.customerHoldDurationMillis"
        },
        {
          "Name": "queue.durationMillis"
        }
      ],
      "Expression": "{CTR.agent.customerHoldDurationMillis} + {CTR.queue.durationMillis}"
    },
    "Statistic": "MAXIMUM",
    "Conditions": {
      "Range": {
        "Value": 30,
        "Unit": "DAYS"
      },
      "ObjectCount": null,
      "Threshold": null
    },
    "Launched": false
  }

```

## Default

profile calculated attribute

Amazon Connect Customer Profiles provides an out-of-the box default attribute based on
a profile. The attributes are as follows:

**New Customer**

```

{
   "CalculatedAttributeName": "_new_customer",
   "DisplayName": "New customer",
   "Description": "Returns true or false for new customer profiles created.",
   "CreatedAt": null,
   "LastUpdatedAt": null,
   "Statistic": "TIME_DIFFERENCE_FROM_NOW",
   "Conditions": {
      "ObjectCount": null,
      "Threshold": {
         "Value": "30",
         "Operator": "LESS_THAN"
      }
   },
   "AttributeDetails": {
      "Attributes": [
         {
            "Name": "createdAt"
         }
      ],
      "Expression": "{_profile.createdAt}"
   },
   "Tags": {
   }
}

```

## Default

asset calculated attributes

Amazon Connect Customer Profiles provides out-of-the box default attributes based on
assets. The attributes are as follows:

**Count of assets**

```
{
    "CalculatedAttributeName": "_assets_count",
    "DisplayName": "Count of assets",
    "Description": "Returns the count of assets for a customer.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "AssetId"
        }
      ],
      "Expression": "{_asset.AssetId}"
    },
    "Statistic": "COUNT",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold":null
    },
    "Launched": false
  }

```

**First asset purchased date**

```
{
    "CalculatedAttributeName": "_asset_first_occurrence",
    "DisplayName": "First asset purchased date",
    "Description": "Returns purchase date of the customer's first asset.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "PurchaseDate"
        }
      ],
      "Expression": "{_asset.PurchaseDate}"
    },
    "Statistic": "FIRST_OCCURRENCE",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold": null
    },
    "Launched": false
  }

```

**Last asset purchased date**

```
{
    "CalculatedAttributeName": "_asset_last_occurrence",
    "DisplayName": "Last asset purchased date",
    "Description": "Returns purchase date of the customer's last asset.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "PurchaseDate"
        }
      ],
      "Expression": "{_asset.PurchaseDate}"
    },
    "Statistic": "LAST_OCCURRENCE",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold": null
    },
    "Launched": false
  }

```

**Total asset price**

```
{
    "CalculatedAttributeName": "_assets_price_sum",
    "DisplayName": "Total asset price",
    "Description": "Returns customer's total asset price.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "Price"
        }
      ],
      "Expression": "{_asset.Price}"
    },
    "Statistic": "SUM",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold": null
    },
    "Launched": false
  }

```

**Average asset price**

```
{
    "CalculatedAttributeName": "_assets_price_average",
    "DisplayName": "Average asset price",
    "Description": "Returns customer's average asset price.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "Price"
        }
      ],
      "Expression": "{_asset.Price}"
    },
    "Statistic": "AVERAGE",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold": null
    },
    "Launched": false
  }

```

**First asset name**

```
{
    "CalculatedAttributeName": "_assets_name_first_occurrence",
    "DisplayName": "First asset name",
    "Description": "Returns name of the customer's first asset",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "AssetName"
        }
      ],
      "Expression": "{_asset.AssetName}"
    },
    "Statistic": "FIRST_OCCURRENCE",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold": null
    },
    "Launched": false
  }

```

**Last asset name**

```
{
    "CalculatedAttributeName": "_assets_name_last_occurrence",
    "DisplayName": "Last asset name",
    "Description": "Returns name of the customer's last asset.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "AssetName"
        }
      ],
      "Expression": "{_asset.AssetName}"
    },
    "Statistic": "LAST_OCCURRENCE",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold": null
    },
    "Launched": false
  }

```

## Default

case calculated attributes

Amazon Connect Customer Profiles provides out-of-the box default attributes based on
cases. The attributes are as follows:

**Count of cases**

```
{
    "CalculatedAttributeName": "_cases_count",
    "DisplayName": "Count of cases",
    "Description": "Returns the count of customer's cases for a customer.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "CaseId"
        }
      ],
      "Expression": "{_case.CaseId}"
    },
    "Statistic": "COUNT",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold":null
    },
    "Launched": false
  }

```

**First case created date**

```
{
    "CalculatedAttributeName": "_case_first_occurrence",
    "DisplayName": "First case created date",
    "Description": "Returns created date of the customer's first case.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "CreatedDate"
        }
      ],
      "Expression": "{_case.CreatedDate}"
    },
    "Statistic": "FIRST_OCCURRENCE",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold": null
    },
    "Launched": false
  }

```

**Last case created date**

```
{
    "CalculatedAttributeName": "_case_last_occurrence",
    "DisplayName": "Last case created date",
    "Description": "Returns created date of the customer's last case.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "CreatedDate"
        }
      ],
      "Expression": "{_case.CreatedDate}"
    },
    "Statistic": "LAST_OCCURRENCE",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold": null
    },
    "Launched": false
  }

```

**Count of open cases**

```
{
    "CalculatedAttributeName": "_cases_open_status_count",
    "DisplayName": "Count of open cases",
    "Description": "Returns the count of customer's open cases.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "CaseId"
        }
      ],
      "Expression": "{_case.CaseId}"
    },
    "Statistic": "COUNT",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold":null
    },
    "Filter": {
      "Include": "ALL",
      "Groups": [
        {
          "Type": "ALL",
          "Dimensions": [
            {
              "Attributes": {
                "Status": {
                  "DimensionType": "INCLUSIVE",
                  "Values": ["Open"]
                }
              }
            }
          ]
        }
      ]
    },
    "Launched": false
  }

```

**Count of closed cases**

```
{
    "CalculatedAttributeName": "_cases_closed_status_count",
    "DisplayName": "Count of closed cases",
    "Description": "Returns the count of customer's closed cases.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "CaseId"
        }
      ],
      "Expression": "{_case.CaseId}"
    },
    "Statistic": "COUNT",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold":null
    },
    "Filter": {
      "Include": "ALL",
      "Groups": [
        {
          "Type": "ALL",
          "Dimensions": [
            {
              "Attributes": {
                "Status": {
                  "DimensionType": "INCLUSIVE",
                  "Values": ["Closed"]
                }
              }
            }
          ]
        }
      ]
    },
    "Launched": false
  }

```

## Default communication record calculated attributes

Amazon Connect Customer Profiles provides out-of-the box default attributes based on
communication records. The attributes are as follows:

**Last email open date**

```
{
    "CalculatedAttributeName": "_campaign_email_last_open",
    "DisplayName": "Last email open date",
    "Description": "Returns the last email open date of the customer.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "Events.Open.UpdatedDate"
        }
      ],
      "Expression": "{_communicationRecord.Events.Open.UpdatedDate}"
    },
    "Statistic": "LAST_OCCURRENCE",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold": null
    },
    "Filter": {
      "Include": "ALL",
      "Groups": [
        {
          "Type": "ALL",
          "Dimensions": [
            {
              "Attributes": {
                "Attributes.ChannelSubType": {
                  "DimensionType": "INCLUSIVE",
                  "Values": ["connect:Email"]
                },
                "Events.Open.EventType": {
                  "DimensionType": "INCLUSIVE",
                  "Values": ["Open"]
                }
              }
            }
          ]
        }
      ]
    },
    "Launched": false
  }

```

**Email open count**

```
{
    "CalculatedAttributeName": "_campaign_email_open_count",
    "DisplayName": "Email open count",
    "Description": "Returns the number of times emails were opened by a customer.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "CommunicationRecordId"
        }
      ],
      "Expression": "{_communicationRecord.CommunicationRecordId}"
    },
    "Statistic": "COUNT",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold": null
    },
    "Filter": {
      "Include": "ALL",
      "Groups": [
        {
          "Type": "ALL",
          "Dimensions": [
            {
              "Attributes": {
                "Attributes.ChannelSubType": {
                  "DimensionType": "INCLUSIVE",
                  "Values": ["connect:Email"]
                },
                "Events.Open.EventType": {
                  "DimensionType": "INCLUSIVE",
                  "Values": ["Open"]
                }
              }
            }
          ]
        }
      ]
    },
    "Launched": false
  }

```

**Email delivery count**

```
{
    "CalculatedAttributeName": "_campaign_email_delivery_count",
    "DisplayName": "Email delivery count",
    "Description": "Returns the number of times emails were delivered to a customer.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "CommunicationRecordId"
        }
      ],
      "Expression": "{_communicationRecord.CommunicationRecordId}"
    },
    "Statistic": "COUNT",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold": null
    },
    "Filter": {
      "Include": "ALL",
      "Groups": [
        {
          "Type": "ALL",
          "Dimensions": [
            {
              "Attributes": {
                "Attributes.ChannelSubType": {
                  "DimensionType": "INCLUSIVE",
                  "Values": ["connect:Email"]
                },
                "Events.Delivery.EventType": {
                  "DimensionType": "INCLUSIVE",
                  "Values": ["Delivery"]
                }
              }
            }
          ]
        }
      ]
    },
    "Launched": false
  }

```

**SMS delivered count**

```
{
    "CalculatedAttributeName": "_campaign_sms_delivery_count",
    "DisplayName": "SMS delivered count",
    "Description": "Returns the number of times SMS were delivered to a customer.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "CommunicationRecordId"
        }
      ],
      "Expression": "{_communicationRecord.CommunicationRecordId}"
    },
    "Statistic": "COUNT",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold": null
    },
    "Filter": {
      "Include": "ALL",
      "Groups": [
        {
          "Type": "ALL",
          "Dimensions": [
            {
              "Attributes": {
                "Attributes.ChannelSubType": {
                  "DimensionType": "INCLUSIVE",
                  "Values": ["connect:SMS"]
                },
                "Events.TEXT_DELIVERED.EventType": {
                  "DimensionType": "INCLUSIVE",
                  "Values": ["TEXT_DELIVERED"]
                }
              }
            }
          ]
        }
      ]
    },
    "Launched": false
  }

```

**Last SMS blocked date**

```
  {
    "CalculatedAttributeName": "_campaign_sms_last_stop",
    "DisplayName": "Last SMS blocked date",
    "Description": "Returns the last SMS blocked date of the customer.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "Events.TEXT_BLOCKED.UpdatedDate"
        }
      ],
      "Expression": "{_communicationRecord.Events.TEXT_BLOCKED.UpdatedDate}"
    },
    "Statistic": "LAST_OCCURRENCE",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold": null
    },
    "Filter": {
      "Include": "ANY",
      "Groups": [
        {
          "Type": "ALL",
          "Dimensions": [
            {
              "Attributes": {
                "Attributes.ChannelSubType": {
                  "DimensionType": "INCLUSIVE",
                  "Values": ["connect:SMS"]
                },
                "Events.TEXT_BLOCKED.EventType": {
                  "DimensionType": "INCLUSIVE",
                  "Values": ["TEXT_BLOCKED"]
                }
              }
            }
          ]
        }
      ]
    },
    "Launched": false
  }

```

**Last SMS carrier blocked date**

```
{
    "CalculatedAttributeName": "_campaign_sms_last_stop_carrier",
    "DisplayName": "Last SMS carrier blocked date",
    "Description": "Returns the last SMS carrier blocked date of the customer.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "Events.TEXT_CARRIER_BLOCKED.UpdatedDate"
        }
      ],
      "Expression": "{_communicationRecord.Events.TEXT_CARRIER_BLOCKED.UpdatedDate}"
    },
    "Statistic": "LAST_OCCURRENCE",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold": null
    },
    "Filter": {
      "Include": "ANY",
      "Groups": [
        {
          "Type": "ALL",
          "Dimensions": [
            {
              "Attributes": {
                "Attributes.ChannelSubType": {
                  "DimensionType": "INCLUSIVE",
                  "Values": ["connect:SMS"]
                },
                "Events.TEXT_CARRIER_BLOCKED.EventType": {
                  "DimensionType": "INCLUSIVE",
                  "Values": ["TEXT_CARRIER_BLOCKED"]
                }
              }
            }
          ]
        }
      ]
    },
    "Launched": false
  }

```

## Default

order calculated attributes

Amazon Connect Customer Profiles provides out-of-the box default attributes based on
orders. The attributes are as follows:

**Count of orders**

```
{
    "CalculatedAttributeName": "_orders_count",
    "DisplayName": "Count of orders",
    "Description": "Returns the count of orders for a customer.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "OrderId"
        }
      ],
      "Expression": "{_order.OrderId}"
    },
    "Statistic": "COUNT",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold":null
    },
    "Launched": false
  }

```

**First order created date**

```
{
    "CalculatedAttributeName": "_order_first_occurrence",
    "DisplayName": "First order created date",
    "Description": "Returns created date of the customer's first order.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "CreatedDate"
        }
      ],
      "Expression": "{_order.CreatedDate}"
    },
    "Statistic": "FIRST_OCCURRENCE",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold": null
    },
    "Launched": false
  }

```

**Last order created date**

```
{
    "CalculatedAttributeName": "_order_last_occurrence",
    "DisplayName": "Last order created date",
    "Description": "Returns created date of the customer's last order.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "CreatedDate"
        }
      ],
      "Expression": "{_order.CreatedDate}"
    },
    "Statistic": "LAST_OCCURRENCE",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold": null
    },
    "Launched": false
  }

```

**Total price of all orders**

```
{
    "CalculatedAttributeName": "_orders_total_price_sum",
    "DisplayName": "Total price of all orders",
    "Description": "Returns sum of total price for all customer's orders.",
    "Statistic": "SUM",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "TotalPrice"
        }
      ],
      "Expression": "{_order.TotalPrice}"
    },
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold":null
    },
    "Launched": false
  }

```

**Orders average of total price**

```
{
    "CalculatedAttributeName": "_orders_total_price_average",
    "DisplayName": "Orders average of total price",
    "Description": "Returns average of total price for all customer's orders.",
    "AttributeDetails": {
      "Attributes": [
        {
          "Name": "TotalPrice"
        }
      ],
      "Expression": "{_order.TotalPrice}"
    },
    "Statistic": "AVERAGE",
    "Conditions": {
      "Range": null,
      "ObjectCount": null,
      "Threshold": null
    },
    "Launched": false
  }

```
