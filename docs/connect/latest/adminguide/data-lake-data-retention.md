# Data retention in the Amazon Connect analytics data

lake

The analytics data lake retention system in Amazon Connect maintains a rolling 25-month window
of accessible data, with the cutoff date updating at 12 AM UTC. For example, if you
access the data lake on September 1, 2025, at 03:00 AM UTC, Amazon Connect will provide access to
data from August 1, 2023, 12:00 AM UTC onwards, while any data before this cutoff date
will not be accessible.

Each data lake table uses a designated timestamp field for age calculations. The
following table lists each the data lake table name and the name of their age timestamp
column.

| **Table name**                        | **Age timestamp column**       |
| ------------------------------------- | ------------------------------ |
| agent_queue_statistic_record          | interval_end_time              |
| agent_statistic_record                | interval_end_time              |
| contact_evaluation_record             | evaluation_submitted_timestamp |
| contact_flow_events                   | start_timestamp                |
| contact_lens_conversational_analytics | disconnect_timestamp           |
| contact_statistic_record              | disconnect_timestamp           |
| contact_record                        | disconnect_timestamp           |
| staff_shift_activities                | last_updated_timestamp         |
| staff_shifts                          | last_updated_timestamp         |
| staff_timeoffs                        | last_updated_timestamp         |
| staff_timeoff_intervals               | last_updated_timestamp         |
| short_term_forecasts                  | creation_timestamp             |
| long_term_forecasts                   | creation_timestamp             |
| outbound_campaign_events              | campaign_event_timestamp       |
| schedule_metrics                      | last_updated_timestamp         |
| schedule_goals                        | last_updated_timestamp         |
| bot_conversations                     | bot_conversation_end_timestamp |
| bot_intents                           | bot_conversation_end_timestamp |
| bot_slots                             | bot_conversation_end_timestamp |
| intraday_forecasts                    | creation_timestamp             |
