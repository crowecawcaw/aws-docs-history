The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Notifications for the AWS Partner Central Benefits API

The Benefits Service provides EventBridge events for both BenefitApplications and BenefitAllocations. These events enable customers to build comprehensive event-driven architectures that respond to changes throughout the entire resources lifecycles - from initial Application through Allocation and final Fulfillment.

###### Topics

- [Complete the prerequisite to monitor events](#events-prerequites "#events-prerequites")
- [Configure Amazon EventBridge to monitor events](#eventbridge-setup "#eventbridge-setup")
- [Learn more about benefits API events](#learn-about-events "#learn-about-events")

## Complete the prerequisite to monitor events

Users require the appropriate IAM permissions to access and manage events published by
the benefits API. For more information about the available actions, resources, and
condition keys for EventBridge, see [Using IAM policy conditions in Amazon EventBridge](../../../eventbridge/latest/userguide/eb-use-conditions.md#events-pattern-detail-type "../../../eventbridge/latest/userguide/eb-use-conditions.md#events-pattern-detail-type") in the _Amazon EventBridge User
Guide_. One of the condition keys is `events:detail-type`,
which can be used to scope permissions to specific event types.

The following example policy demonstrates how to customize and scope the permissions
for the proposed events. The `AllowPutRuleForPartnercentralBenefitsEvents`
statement allows the creation of rules, but only for events from the
`aws.partnercentral-benefits` source.

For detailed IAM policy examples, refer to the AWS documentation on EventBridge permissions.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowPutRuleForPartnerCentralBenefitsEvents",
      "Effect": "Allow",
      "Action": "events:PutRule",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "events:source": "aws.partnercentral-benefits"
        }
      }
    }
  ]
}
```

## Configure Amazon EventBridge to monitor events

To monitor benefits API events, you create an EventBridge rule that matches the events that
you want to capture. You can use the AWS Management Console or the AWS SDKs to create and manage
rules. The following sections explain how to create rules using both methods. Regardless
of the method you use, you must create the rule in the US East (N. Virginia)
`us-east-1` Region.

### AWS Management Console setup

To set up an EventBridge rule using the AWS Management Console, follow the steps in [Creating rules that react to events in Amazon EventBridge](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md") in the
_Amazon EventBridge User Guide_. When creating the rule, you must set
the event bus to **default**, and create the rule in the
US East (N. Virginia) `us-east-1` Region.

Following is an example of an event rule:

```
{
    "source": ["aws.partnercentral-benefits"],
    "detail": {
        "catalog": ["AWS"]
    }
}
```

### AWS SDK setup

You can use the AWS SDKs to create and manage EventBridge rules programmatically. For
more information, see [PutRule](../../../eventbridge/latest/APIReference/API_PutRule.md "../../../eventbridge/latest/APIReference/API_PutRule.md") in the
_Amazon EventBridge API Reference_.

The following example uses the AWS SDK for Python (Boto3):

```
import boto3

client = boto3.client('events', region_name='us-east-1')

response = client.put_rule(
    Name='MyBenefitApplicationCreatedRule',
    EventPattern=
    '{
        "source": ["aws.partnercentral-benefits"],
        "detail-type": ["Benefit Application Created"],
        "detail": {"catalog": ["AWS"]}
    }',
    State='ENABLED'
)
print('Rule ARN:', response['RuleArn'])
```

## Learn more about benefits API events

The following sections describe the benefits API event types, scenarios that trigger
them, and event examples.

### Event types

Following are the event types and their triggers.

#### Benefit Applications

- [Benefit Application Created](#benefit-application-created "#benefit-application-created"): When a Benefit Application is created
- [Benefit Application In Review](#benefit-application-in-review "#benefit-application-in-review"): When a Benefit Application is submitted or when the Application transitions from Action Required back to In Review, this event is triggered.
- [Benefit Application Action Required](#benefit-application-action-required "#benefit-application-action-required"): This event occurs when an internal reviewer updates the application status to indicate that the partner needs to provide additional information, clarification, or modifications before the review can continue.
- [Benefit Application Rejected](#benefit-application-rejected "#benefit-application-rejected"): This event occurs when an internal reviewer updates the application status to indicate that the application does not meet the benefit criteria or requirements and has been declined
- [Benefit Application Approved](#benefit-application-approved "#benefit-application-approved"): This event occurs when an internal reviewer updates the application status to indicate that the application has been approved for benefit allocation.
- [Benefit Application Stage Changed](#benefit-application-stage-changed "#benefit-application-stage-changed"): This event occurs when an internal reviewer updates the stage of the application during review processes such as Business Review, AWS Review, Financial Review, etc.

#### Benefit Allocations

- [Benefit Allocation Activated](#benefit-allocation-activated "#benefit-allocation-activated"): When a Benefit Allocation is created or updated back to Activated by an internal service.
- [Benefit Allocation Inactivated](#benefit-allocation-inactivated "#benefit-allocation-inactivated"): This event occurs when an internal reviewer updates the allocation status or when a Benefit Allocation expires automatically.
- [Benefit Allocation Fulfilled](#benefit-allocation-fulfilled "#benefit-allocation-fulfilled"): This event occurs when an internal reviewer updates the allocation status to indicate that the allocation has been completely utilized.

### Example events

The following sections provide examples of the events listed earlier in the
previous section.

###### Topics

- [Benefit Application Created](#benefit-application-created "#benefit-application-created")
- [Benefit Application In Review](#benefit-application-in-review "#benefit-application-in-review")
- [Benefit Application Action Required](#benefit-application-action-required "#benefit-application-action-required")
- [Benefit Application Rejected](#benefit-application-rejected "#benefit-application-rejected")
- [Benefit Application Approved](#benefit-application-approved "#benefit-application-approved")
- [Benefit Application Stage Changed](#benefit-application-stage-changed "#benefit-application-stage-changed")
- [Benefit Allocation Activated](#benefit-allocation-activated "#benefit-allocation-activated")
- [Benefit Allocation Inactivated](#benefit-allocation-inactivated "#benefit-allocation-inactivated")
- [Benefit Allocation Fulfilled](#benefit-allocation-fulfilled "#benefit-allocation-fulfilled")

#### Benefit Application Created

##### Triggering Context

The Benefit Application Created event is published to Amazon EventBridge when a new Benefit Application is successfully created through the Benefits Service. This event occurs when the CreateBenefitApplication API call completes successfully, indicating that a partner has initiated a request for a specific benefit.

This event represents the beginning of the benefit application lifecycle and provides customers with immediate notification when new applications are submitted to their account.

##### Recipients

The owning account will receive the event for the Benefit Allocation.

##### Example

```
{
  "id": "7gh88765-k0jh-d08g-i292-2ff1796m030n",
  "detail-type": "Benefit Application Created",
  "source": "aws.partnercentral-benefits",
  "account": "123456789012",
  "time": "2025-02-10T15:45:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:partnercentral:us-east-1:123456789012:benefit-application/benappl-12345abcdef123"
  ],
  "detail": {
    "catalog": "AWS",
    "benefitApplication": {
      "id": "benappl-12345abcdef123",
      "fulfillmentTypes": ["CREDITS"],
      "status": "PENDING_SUBMISSION",
      "revision": "hh7e8400-e29b-41d4-a716-446655440012"
    },
    "benefit": {
      "id": "ben-xyz789uvw012",
      "name": "AWS Partner Credits",
      "program": ["AWS Partner Network"]
    }
  }
}
```

#### Benefit Application In Review

##### Triggering Context

The Benefit Application In Review event is published to Amazon EventBridge when a Benefit Application transitions to the IN\_REVIEW status through the Benefits Service. This event occurs when:

- A partner submits their application via the SubmitBenefitApplication API call
- An application transitions from ACTION\_REQUIRED back to IN\_REVIEW after the partner addresses feedback
- An application is recalled and then resubmitted

This event indicates that the application has entered the formal review process and is being evaluated by AWS internal teams.

##### Recipients

The owning account will receive the event for the Benefit Allocation.

##### Example

```
{
  "id": "8hi99876-l1ki-e19h-j303-3gg2807n141o",
  "detail-type": "Benefit Application In Review",
  "source": "aws.partnercentral-benefits",
  "account": "123456789012",
  "time": "2025-02-10T16:00:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:partnercentral:us-east-1:123456789012:benefit-application/benappl-12345abcdef123"
  ],
  "detail": {
    "catalog": "AWS",
    "benefitApplication": {
      "id": "benappl-12345abcdef123",
      "fulfillmentTypes": ["CREDITS"],
      "status": "IN_REVIEW",
      "stage": "BUSINESS_REVIEW",
      "revision": "ii8f9511-f30c-52e5-b827-557766551123"
    },
    "benefit": {
      "id": "ben-xyz789uvw012",
      "name": "AWS Partner Credits",
      "program": ["AWS Partner Network"]
    }
  }
}
```

#### Benefit Application Action Required

##### Triggering Context

The Benefit Application Action Required event is published to Amazon EventBridge when a Benefit Application transitions to the ACTION\_REQUIRED status through the Benefits Service. This event occurs when an internal reviewer updates the application status via the UpdateBenefitApplicationInternal API to indicate that the partner needs to provide additional information, clarification, or modifications before the review can continue.

This event represents a critical point in the application lifecycle where partner intervention is needed to move the application forward in the review process.

##### Recipients

The owning account will receive the event for the Benefit Allocation

##### Example

```
{
  "id": "9ij00987-m2lj-f20i-k414-4hh3918o252p",
  "detail-type": "Benefit Application Action Required",
  "source": "aws.partnercentral-benefits",
  "account": "123456789012",
  "time": "2025-02-12T10:30:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:partnercentral:us-east-1:123456789012:benefit-application/benappl-12345abcdef123"
  ],
  "detail": {
    "catalog": "AWS",
    "benefitApplication": {
      "id": "benappl-12345abcdef123",
      "fulfillmentTypes": ["CREDITS"],
      "status": "ACTION_REQUIRED",
      "stage": "BUSINESS_REVIEW",
      "revision": "jj9g0622-g41d-63f6-c938-668877662234"
    },
    "benefit": {
      "id": "ben-xyz789uvw012",
      "name": "AWS Partner Credits",
      "program": ["AWS Partner Network"]
    }
  }
}
```

#### Benefit Application Rejected

##### Triggering Context

The Benefit Application Rejected event is published to Amazon EventBridge when a Benefit Application transitions to the REJECTED status through the Benefits Service. This event occurs when an internal reviewer updates the application status via the UpdateBenefitApplicationInternal API to indicate that the application does not meet the benefit criteria or requirements and has been declined.

This event represents a terminal state in the application lifecycle where the application has been formally declined and will not proceed to benefit allocation.

##### Recipients

The owning account will receive the event for the Benefit Allocation.

##### Example

```
{
  "id": "0kl11098-n3mk-g31j-l525-5ii4029p363q",
  "detail-type": "Benefit Application Rejected",
  "source": "aws.partnercentral-benefits",
  "account": "123456789012",
  "time": "2025-02-15T14:20:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:partnercentral:us-east-1:123456789012:benefit-application/benappl-12345abcdef123"
  ],
  "detail": {
    "catalog": "AWS",
    "benefitApplication": {
      "id": "benappl-12345abcdef123",
      "fulfillmentTypes": ["CREDITS"],
      "status": "REJECTED",
      "revision": "kk0h1733-h52e-74g7-d049-779988773345"
    },
    "benefit": {
      "id": "ben-xyz789uvw012",
      "name": "AWS Partner Credits",
      "program": ["AWS Partner Network"]
    }
  }
}
```

#### Benefit Application Approved

##### Triggering Context

The Benefit Application Approved event is published to Amazon EventBridge when a Benefit Application transitions to the APPROVED status through the Benefits Service. This event occurs when an internal reviewer updates the application status via the UpdateBenefitApplicationInternal API to indicate that the application meets all benefit criteria and requirements and has been approved for benefit allocation.

This event represents a successful completion of the application review process and typically triggers the creation of a corresponding Benefit Allocation.

##### Recipients

The owning account will receive the event for the Benefit Allocation.

##### Example

```
{
  "id": "1lm22109-o4nl-h42k-m636-6jj5130q474r",
  "detail-type": "Benefit Application Approved",
  "source": "aws.partnercentral-benefits",
  "account": "123456789012",
  "time": "2025-02-14T16:45:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:partnercentral:us-east-1:123456789012:benefit-application/benappl-12345abcdef123"
  ],
  "detail": {
    "catalog": "AWS",
    "benefitApplication": {
      "id": "benappl-12345abcdef123",
      "fulfillmentTypes": ["CREDITS"],
      "status": "APPROVED",
      "revision": "ll1i2844-i63f-85h8-e150-880099884456"
    },
    "benefit": {
      "id": "ben-xyz789uvw012",
      "name": "AWS Partner Credits",
      "program": ["AWS Partner Network"]
    }
  }
}
```

#### Benefit Application Stage Changed

##### Triggering Context

The Benefit Application Stage Changed event is published to Amazon EventBridge when a Benefit Application's review stage is updated through the Benefits Service. This event occurs when an internal reviewer updates the Stage of the application to one of the possible Enum values (FINANCE\_REVIEW, BUSINESS\_REVIEW, TECH\_REVIEW and AWS\_REVIEW).

Unlike status changes, stage changes are read-only informational updates that provide visibility into the internal review workflow progression without requiring partner action.

##### Recipients

The owning account will receive the event for the Benefit Allocation.

##### Example

```
{
  "id": "2mn33210-p5om-i53l-n747-7kk6241r585s",
  "detail-type": "Benefit Application Stage Changed",
  "source": "aws.partnercentral-benefits",
  "account": "123456789012",
  "time": "2025-02-13T11:15:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:partnercentral:us-east-1:123456789012:benefit-application/benappl-12345abcdef123"
  ],
  "detail": {
    "catalog": "AWS",
    "benefitApplication": {
      "id": "benappl-12345abcdef123",
      "fulfillmentTypes": ["CREDITS"],
      "status": "IN_REVIEW",
      "stage": "FINANCIAL_REVIEW",
      "revision": "mm2j3955-j74g-96i9-f261-991100995567"
    },
    "benefit": {
      "id": "ben-xyz789uvw012",
      "name": "AWS Partner Credits",
      "program": ["AWS Partner Network"]
    }
  }
}
```

#### Benefit Allocation Activated

##### Triggering Context

The Benefit Allocation Activated event is published to Amazon EventBridge when a Benefit Allocation transitions to the ACTIVE status through the Benefits Service. This event occurs when an internal reviewer updates the allocation status via the UpdateBenefitAllocationInternal API to reactivate a previously inactive allocation.

This event typically occurs when an allocation that was temporarily inactivated (due to expiration, policy changes, or administrative reasons) is restored to active status, making the benefits available for partner utilization again.

##### Recipients

The AWS Account belonging to the Partner will receive the message. In other words, the AWS Account which owns the resource.

##### Sample Event

```
{
  "id": "3no44321-q6pn-j64m-o858-8ll7352s696t",
  "detail-type": "Benefit Allocation Activated",
  "source": "aws.partnercentral-benefits",
  "account": "123456789012",
  "time": "2025-03-01T08:15:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:partnercentral:us-east-1:123456789012:benefit-allocation/benalloc-abc123def456"
  ],
  "detail": {
    "catalog": "AWS",
    "benefitAllocation": {
      "id": "benalloc-abc123def456",
      "fulfillmentType": "CREDITS",
      "status": "ACTIVE"
    },
    "benefitApplication": {
      "id": "benappl-12345abcdef123"
    },
    "benefit": {
      "id": "ben-xyz789uvw012",
      "name": "AWS Partner Credits",
      "program": ["AWS Partner Network"]
    }
  }
}
```

#### Benefit Allocation Inactivated

##### Triggering Context

The Benefit Allocation Inactivated event is published to Amazon EventBridge when a Benefit Allocation transitions to the INACTIVE status through the Benefits Service. This event occurs when an internal reviewer updates the allocation status via the UpdateBenefitAllocationInternal API or when a Benefit Allocation expires automatically.

This event typically occurs when an allocation is temporarily suspended (due to expiration, policy changes, compliance issues, or administrative reasons), making the benefits unavailable for partner utilization until reactivated.

##### Recipients

The AWS Account belonging to the Partner will receive the message. In other words, the AWS Account which owns the resource.

##### Sample Event

```
{
  "id": "4op55432-r7qo-k75n-p969-9mm8463t707u",
  "detail-type": "Benefit Allocation Inactivated",
  "source": "aws.partnercentral-benefits",
  "account": "123456789012",
  "time": "2025-06-30T23:59:59Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:partnercentral:us-east-1:123456789012:benefit-allocation/benalloc-abc123def456"
  ],
  "detail": {
    "catalog": "AWS",
    "benefitAllocation": {
      "id": "benalloc-abc123def456",
      "fulfillmentType": "CREDITS",
      "status": "INACTIVE"
    },
    "benefitApplication": {
      "id": "benappl-12345abcdef123"
    },
    "benefit": {
      "id": "ben-xyz789uvw012",
      "name": "AWS Partner Credits",
      "program": ["AWS Partner Network"]
    }
  }
}
```

#### Benefit Allocation Fulfilled

##### Triggering Context

The Benefit Allocation Fulfilled event is published to Amazon EventBridge when a Benefit Allocation transitions to the FULFILLED status through the Benefits Service. This event occurs when an internal reviewer updates the allocation status via the UpdateBenefitAllocationInternal API to indicate that the allocation has been completely utilized or that the benefit terms have been satisfied.

This event represents the completion of the benefit lifecycle, indicating that the partner has successfully utilized the allocated benefit or that the allocation has reached its natural conclusion.

##### Recipients

The AWS Account belonging to the Partner will receive the message. In other words, the AWS Account which owns the resource.

##### Sample Event

```
{
  "id": "5pq66543-s8rp-l86o-q070-0nn9574u818v",
  "detail-type": "Benefit Allocation Fulfilled",
  "source": "aws.partnercentral-benefits",
  "account": "123456789012",
  "time": "2025-12-15T17:30:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:partnercentral:us-east-1:123456789012:benefit-allocation/benalloc-abc123def456"
  ],
  "detail": {
    "catalog": "AWS",
    "benefitAllocation": {
      "id": "benalloc-abc123def456",
      "fulfillmentType": "CREDITS",
      "status": "FULFILLED"
    },
    "benefitApplication": {
      "id": "benappl-12345abcdef123"
    },
    "benefit": {
      "id": "ben-xyz789uvw012",
      "name": "AWS Partner Credits",
      "program": ["AWS Partner Network"]
    }
  }
}
```
