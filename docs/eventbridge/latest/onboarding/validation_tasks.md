

# Validation tasks
<a name="validation_tasks"></a>

The validation tasks in this topic are to ensure that you have considered different scenarios that customer may encounter when they consume events. For example, customers may request that the event sources are created in different AWS Regions.

## Create event source validation items
<a name="_create_event_source_validation_items"></a>

1. Ensure that you provide a UI for developers to register their AWS account with your service.

1. The UI should allow the selection of the destination AWS Region.

1. Direct AWS Identity and Access Management(IAM) access to the customer account is not requested nor required.

1. Ensure that the event source is created successfully.

1. The event source name scheme provides global uniqueness within each region (i.e. it includes an appropriate customer identifier or other unique ID).

## Send events validation items
<a name="_send_events_validation_items"></a>

1. Ensure that events are received successfully.

1. Data in the event detail and other event metadata fields is formatted appropriately and semantically correct.

## Delete event source validation items
<a name="_delete_event_source_validation_items"></a>
+ Ensure that the event source is deleted correctly.

## Repeat the validation tests for other Regions
<a name="_repeat_the_validation_tests_for_other_regions"></a>

1. The event source is created successfully.

1. Events are received successfully.

Partners are required to describe how their integration handles event sources that move from a PENDING to NONEXISTENT state, as well as the mechanism used for handling errors from the [`PutPartnerEvents`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPartnerEvents.html) API call.