# Sample questions to ask AWS IoT SiteWise Assistant

###### Note

The SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025 . If you would like to use SiteWise Monitor,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[SiteWise Monitor availability change](../appguide/iotsitewise-monitor-availability-change.md "../appguide/iotsitewise-monitor-availability-change.md").

###### Note

- The AWS IoT SiteWise Assistant must use a dataset with an [Amazon Kendra](../../../kendra/latest/dg/what-is-kendra.md "../../../kendra/latest/dg/what-is-kendra.md") index for enterprise level knowledge and guidance. If you do not have a Amazon Kendra index, see
  [Creating an index](../../../kendra/latest/dg/create-index.md "../../../kendra/latest/dg/create-index.md") to create one. Adding a
  [dataset](concept-overview.md#concept-dataset "concept-overview.md#concept-dataset") improves the quality of the Assistant's response. See
  [Create a dataset](assistant-console-create-dataset.md "assistant-console-create-dataset.md") to learn more.
- Some questions require AWS IoT TwinMaker integration. See [Integrate AWS IoT TwinMaker and AWS IoT SiteWise](integrate-tm.md "integrate-tm.md") for details.

Some follow up questions to ask the Assistant after getting an alarm summary in the dashboard, as part of the same conversation.

- Show the details of the asset from the summary above?
- What is the hierarchical path from root to the mentioned asset?
- What are the dependent descendant assets of the mentioned asset?
- What are the dependent assets of the mentioned asset that have active alarms?
- Find all assets that have active alarms.

Some follow up questions to ask the Assistant after getting an property summary in the dashboard, as part of the same conversation.

- Perform the same analysis for the last 24 hours.
- Find documentation related to the above mentioned properties.
- Provide the details of asset id 1da67d28-14f8-4f71-a06a-386f0425a21d/asset name Demo Turbine Asset 1.

Invoke the AWS IoT SiteWise Assistant from the API.

- Generate alarm summary for alarm name **windSpeedAlarm** in asset id `d591e153-e5cf-4206-96bb-ce3c119d9d2d`.
- Generate alarm summary for the last 12 hours/2 days/1 week for alarm name **windSpeedAlarm** in asset id `d591e153-e5cf-4206-96bb-ce3c119d9d2d`.
- Generate property summary for property id `ab187fb7-d74b-44d9-bd9b-f2f19a9137cc` in asset id `d591e153-e5cf-4206-96bb-ce3c119d9d2d`
- Generate property summary for the last 12 hours/2 days/1 week for property id `ab187fb7-d74b-44d9-bd9b-f2f19a9137cc`
  in asset id `d591e153-e5cf-4206-96bb-ce3c119d9d2d`.
- Find the assets with asset name Turbine.
- Give me the current property values of property id `5356168c-3390-456f-802c-9f6e047810d4` in
  asset id `d591e153-e5cf-4206-96bb-ce3c119d9d2d`, `3cbb084e-1ded-4b08-9f21-1b47b2fb86fd`.
- What is the relationship between asset id `d591e153-e5cf-4206-96bb-ce3c119d9d2d`
  and asset id `3cbb084e-1ded-4b08-9f21-1b47b2fb86fd`.
- Find documentation on how to fix wind turbine low RPM issue.
- Generate a property summary for property alias **WindSpeed**.
- What are the pre-operation checks according to my knowledge base?
