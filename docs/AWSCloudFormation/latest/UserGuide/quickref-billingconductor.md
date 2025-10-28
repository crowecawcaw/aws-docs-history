# AWS Billing Console template snippets

This example creates one pricing plan with a 10% global markup pricing rule. This pricing plan is attached to the billing group.
The billing group also has two custom line items which applies a $10 charge and a 10% charge on top of the billing group total cost.

## JSON

```
{
   "Parameters": {
      "LinkedAccountIds": {
         "Type": "List`Number`"
      },
      "PrimaryAccountId": {
         "Type": "Number"
      }
   },
   "Resources": {
      "TestPricingRule": {
         "Type": "AWS::BillingConductor::PricingRule",
         "Properties": {
            "Name": "TestPricingRule",
            "Description": "Test pricing rule created through Cloudformation. Mark everything by 10%.",
            "Type": "MARKUP",
            "Scope": "GLOBAL",
            "ModifierPercentage": 10
         }
      },
      "TestPricingPlan": {
         "Type": "AWS::BillingConductor::PricingPlan",
         "Properties": {
            "Name": "TestPricingPlan",
            "Description": "Test pricing plan created through Cloudformation.",
            "PricingRuleArns": [
               {"Fn::GetAtt": ["TestPricingRule", "Arn"]}
            ]
         }
      },
      "TestBillingGroup": {
         "Type": "AWS::BillingConductor::BillingGroup",
         "Properties": {
            "Name": "TestBillingGroup",
            "Description": "Test billing group created through Cloudformation with 1 linked account. The linked account is also the primary account.",
            "PrimaryAccountId": {
               "Ref": "PrimaryAccountId"
            },
            "AccountGrouping": {
               "LinkedAccountIds": null
            },
            "ComputationPreference": {
               "PricingPlanArn": {
                 "Fn::GetAtt": ["TestPricingPlan", "Arn"]
               }
            }
         }
      },
      "TestFlatCustomLineItem": {
         "Type": "AWS::BillingConductor::CustomLineItem",
         "Properties": {
            "Name": "TestFlatCustomLineItem",
            "Description": "Test flat custom line item created through Cloudformation for a $10 charge.",
            "BillingGroupArn": {
              "Fn::GetAtt": ["TestBillingGroup", "Arn"]
            },
            "CustomLineItemChargeDetails": {
               "Flat": {
                  "ChargeValue": 10
               },
               "Type": "FEE"
            }
         }
      },
      "TestPercentageCustomLineItem": {
         "Type": "AWS::BillingConductor::CustomLineItem",
         "Properties": {
            "Name": "TestPercentageCustomLineItem",
            "Description": "Test percentage custom line item created through Cloudformation for a %10 additional charge on the overall total bill of the billing group.",
            "BillingGroupArn": {
              "Fn::GetAtt": ["TestBillingGroup", "Arn"]
            },
            "CustomLineItemChargeDetails": {
               "Percentage": {
                  "PercentageValue": 10,
                  "ChildAssociatedResources": [
                     {"Fn::GetAtt": ["TestBillingGroup", "Arn"]}
                  ]
               },
               "Type": "FEE"
            }
         }
      }
   }
}
```

## YAML

```
Parameters:
  LinkedAccountIds:
    Type: List`Number`
  PrimaryAccountId:
    Type: Number
Resources:
  TestPricingRule:
    Type: 'AWS::BillingConductor::PricingRule'
    Properties:
      Name: 'TestPricingRule'
      Description: 'Test pricing rule created through Cloudformation. Mark everything by 10%.'
      Type: 'MARKUP'
      Scope: 'GLOBAL'
      ModifierPercentage: 10
  TestPricingPlan:
    Type: 'AWS::BillingConductor::PricingPlan'
    Properties:
      Name: 'TestPricingPlan'
      Description: 'Test pricing plan created through Cloudformation.'
      PricingRuleArns:
        - !GetAtt TestPricingRule.Arn
  TestBillingGroup:
    Type: 'AWS::BillingConductor::BillingGroup'
    Properties:
      Name: 'TestBillingGroup'
      Description: 'Test billing group created through Cloudformation with 1 linked account. The linked account is also the primary account.'
      PrimaryAccountId: !Ref PrimaryAccountId
      AccountGrouping:
        LinkedAccountIds: !Ref LinkedAccountIds
      ComputationPreference:
        PricingPlanArn: !GetAtt TestPricingPlan.Arn
  TestFlatCustomLineItem:
    Type: 'AWS::BillingConductor::CustomLineItem'
    Properties:
      Name: 'TestFlatCustomLineItem'
      Description: 'Test flat custom line item created through Cloudformation for a $10 charge.'
      BillingGroupArn: !GetAtt TestBillingGroup.Arn
      CustomLineItemChargeDetails:
        Flat:
          ChargeValue: 10
        Type: 'FEE'
  TestPercentageCustomLineItem:
    Type: 'AWS::BillingConductor::CustomLineItem'
    Properties:
      Name: 'TestPercentageCustomLineItem'
      Description: 'Test percentage custom line item created through Cloudformation for a %10 additional charge on the overall total bill of the billing group.'
      BillingGroupArn: !GetAtt TestBillingGroup.Arn
      CustomLineItemChargeDetails:
        Percentage:
          PercentageValue: 10
          ChildAssociatedResources:
            - !GetAtt TestBillingGroup.Arn
        Type: 'FEE'
```
