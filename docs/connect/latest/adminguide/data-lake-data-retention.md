# Data retention in the Connect Customer analytics data lake

The data lake retention system in Connect Customer maintains a rolling 25-month window
of accessible data, with the cutoff date updating at 12 AM UTC. For example, if you
access the data lake on September 1, 2025, at 03:00 AM UTC, Connect Customer will provide access to
data from August 1, 2023, 12:00 AM UTC onwards, while any data before this cutoff date
will not be accessible.

Each data lake table uses a designated timestamp field for age calculations. The
following table lists each the data lake table name and the name of their age timestamp
column.

| **Table name**                           | **Age timestamp column**          |
| ---------------------------------------- | --------------------------------- |
| agent\_queue\_statistic\_record          | interval\_end\_time               |
| agent\_statistic\_record                 | interval\_end\_time               |
| contact\_evaluation\_record              | evaluation\_submitted\_timestamp  |
| contact\_flow\_events                    | start\_timestamp                  |
| contact\_lens\_conversational\_analytics | disconnect\_timestamp             |
| contact\_statistic\_record               | disconnect\_timestamp             |
| contact\_record                          | disconnect\_timestamp             |
| staff\_shift\_activities                 | last\_updated\_timestamp          |
| staff\_shifts                            | last\_updated\_timestamp          |
| staff\_timeoffs                          | last\_updated\_timestamp          |
| staff\_timeoff\_intervals                | last\_updated\_timestamp          |
| short\_term\_forecasts                   | creation\_timestamp               |
| long\_term\_forecasts                    | creation\_timestamp               |
| outbound\_campaign\_events               | campaign\_event\_timestamp        |
| schedule\_metrics                        | last\_updated\_timestamp          |
| schedule\_goals                          | last\_updated\_timestamp          |
| bot\_conversations                       | bot\_conversation\_end\_timestamp |
| bot\_intents                             | bot\_conversation\_end\_timestamp |
| bot\_slots                               | bot\_conversation\_end\_timestamp |
| intraday\_forecasts                      | creation\_timestamp               |
