# When (departure and arrival)

Specifies the time for route calculation. The time not only determines the timestamps for departure and arrival but also influences the traffic data to be used.

| Parameter      | Description                                                                                                                                                                                        | Routes | Routes Matrix | Isoline | Optimize Waypoint | Snap To Road |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------------- | ------- | ----------------- | ------------ |
| Departure Time | Time of departure from the Origin. If neither arrival nor departure time is provided, dynamic traffic information is not used, and only free-flow speeds based on historical traffic are applied.  | Yes    | Yes           | Yes     | Yes               | No           |
| Depart Now     | Uses the current time as the time of departure from the Origin.                                                                                                                                    | Yes    | Yes           | Yes     | No                | No           |
| Arrival Time   | Time of arrival at the destination. If neither arrival nor departure time is provided, dynamic traffic information is not used, and only free-flow speeds based on historical traffic are applied. | Yes    | No            | Yes     | No                | No           |
