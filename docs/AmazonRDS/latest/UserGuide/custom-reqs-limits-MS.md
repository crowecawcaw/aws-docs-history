# Local time zone for RDS Custom for SQL Server DB instances

The time zone of an RDS Custom for SQL Server DB instance is set by default. The current default is Coordinated Universal
Time (UTC). You can set the time zone of your DB instance to a local time zone instead, to match the time zone of your
applications.

You set the time zone when you first create your DB instance. You can create your DB
instance by using the [AWS Management Console](USER_CreateDBInstance.md "USER_CreateDBInstance.md"), the
Amazon RDS API [CreateDBInstance](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md") action, or the AWS CLI [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") command.

If your DB instance is part of a Multi-AZ deployment, then when you fail over, your time zone remains the local time zone that you set.

When you request a point-in-time restore, you specify the time to restore to. The time is
shown in your local time zone. For more information, see [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md").

The following are limitations to setting the local time zone on your DB
instance:

- You can configure the time zone for a DB instance during instance creation, but you can't modify the time zone of an existing RDS Custom for SQL Server DB instance.
- If the time zone is modified for an existing RDS Custom for SQL Server DB instance, RDS Custom changes the DB instance status to `unsupported-configuration`, and sends event notifications.
- You can't restore a snapshot from a DB instance in one time zone to a DB
  instance in a different time zone.
- We strongly recommend that you don't restore a backup file from one time zone
  to a different time zone. If you restore a backup file from one time zone to a
  different time zone, you must audit your queries and applications for the
  effects of the time zone change. For more information, see [Importing and exporting SQL Server databases using native
  backup and restore](SQLServer.Procedural.md "SQLServer.Procedural.md").

## Supported time zones

You can set your local time zone to one of the values listed in the following table.

| Time zone                       | Standard time offset | Description                                       | Notes                                                                                                      |
| ------------------------------- | -------------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Afghanistan Standard Time       | (UTC+04:30)          | Kabul                                             | This time zone doesn't observe daylight saving time.                                                       |
| Alaskan Standard Time           | (UTC–09:00)          | Alaska                                            |                                                                                                            |
| Aleutian Standard Time          | (UTC–10:00)          | Aleutian Islands                                  |                                                                                                            |
| Altai Standard Time             | (UTC+07:00)          | Barnaul, Gorno-Altaysk                            |                                                                                                            |
| Arab Standard Time              | (UTC+03:00)          | Kuwait, Riyadh                                    | This time zone doesn't observe daylight saving time.                                                       |
| Arabian Standard Time           | (UTC+04:00)          | Abu Dhabi, Muscat                                 |                                                                                                            |
| Arabic Standard Time            | (UTC+03:00)          | Baghdad                                           | This time zone doesn't observe daylight saving time.                                                       |
| Argentina Standard Time         | (UTC–03:00)          | City of Buenos Aires                              | This time zone doesn't observe daylight saving time.                                                       |
| Astrakhan Standard Time         | (UTC+04:00)          | Astrakhan, Ulyanovsk                              |                                                                                                            |
| Atlantic Standard Time          | (UTC–04:00)          | Atlantic Time (Canada)                            |                                                                                                            |
| AUS Central Standard Time       | (UTC+09:30)          | Darwin                                            | This time zone doesn't observe daylight saving time.                                                       |
| Aus Central W. Standard Time    | (UTC+08:45)          | Eucla                                             |                                                                                                            |
| AUS Eastern Standard Time       | (UTC+10:00)          | Canberra, Melbourne, Sydney                       |                                                                                                            |
| Azerbaijan Standard Time        | (UTC+04:00)          | Baku                                              |                                                                                                            |
| Azores Standard Time            | (UTC–01:00)          | Azores                                            |                                                                                                            |
| Bahia Standard Time             | (UTC–03:00)          | Salvador                                          |                                                                                                            |
| Bangladesh Standard Time        | (UTC+06:00)          | Dhaka                                             | This time zone doesn't observe daylight saving time.                                                       |
| Belarus Standard Time           | (UTC+03:00)          | Minsk                                             | This time zone doesn't observe daylight saving time.                                                       |
| Bougainville Standard Time      | (UTC+11:00)          | Bougainville Island                               |                                                                                                            |
| Canada Central Standard Time    | (UTC–06:00)          | Saskatchewan                                      | This time zone doesn't observe daylight saving time.                                                       |
| Cape Verde Standard Time        | (UTC–01:00)          | Cabo Verde Is.                                    | This time zone doesn't observe daylight saving time.                                                       |
| Caucasus Standard Time          | (UTC+04:00)          | Yerevan                                           |                                                                                                            |
| Cen. Australia Standard Time    | (UTC+09:30)          | Adelaide                                          |                                                                                                            |
| Central America Standard Time   | (UTC–06:00)          | Central America                                   | This time zone doesn't observe daylight saving time.                                                       |
| Central Asia Standard Time      | (UTC+06:00)          | Astana                                            | This time zone doesn't observe daylight saving time.                                                       |
| Central Brazilian Standard Time | (UTC–04:00)          | Cuiaba                                            |                                                                                                            |
| Central Europe Standard Time    | (UTC+01:00)          | Belgrade, Bratislava, Budapest, Ljubljana, Prague |                                                                                                            |
| Central European Standard Time  | (UTC+01:00)          | Sarajevo, Skopje, Warsaw, Zagreb                  |                                                                                                            |
| Central Pacific Standard Time   | (UTC+11:00)          | Solomon Islands, New Caledonia                    | This time zone doesn't observe daylight saving time.                                                       |
| Central Standard Time           | (UTC–06:00)          | Central Time (US and Canada)                      |                                                                                                            |
| Central Standard Time (Mexico)  | (UTC–06:00)          | Guadalajara, Mexico City, Monterrey               |                                                                                                            |
| Chatham Islands Standard Time   | (UTC+12:45)          | Chatham Islands                                   |                                                                                                            |
| China Standard Time             | (UTC+08:00)          | Beijing, Chongqing, Hong Kong, Urumqi             | This time zone doesn't observe daylight saving time.                                                       |
| Cuba Standard Time              | (UTC–05:00)          | Havana                                            |                                                                                                            |
| Dateline Standard Time          | (UTC–12:00)          | International Date Line West                      | This time zone doesn't observe daylight saving time.                                                       |
| E. Africa Standard Time         | (UTC+03:00)          | Nairobi                                           | This time zone doesn't observe daylight saving time.                                                       |
| E. Australia Standard Time      | (UTC+10:00)          | Brisbane                                          | This time zone doesn't observe daylight saving time.                                                       |
| E. Europe Standard Time         | (UTC+02:00)          | Chisinau                                          |                                                                                                            |
| E. South America Standard Time  | (UTC–03:00)          | Brasilia                                          |                                                                                                            |
| Easter Island Standard Time     | (UTC–06:00)          | Easter Island                                     |                                                                                                            |
| Eastern Standard Time           | (UTC–05:00)          | Eastern Time (US and Canada)                      |                                                                                                            |
| Eastern Standard Time (Mexico)  | (UTC–05:00)          | Chetumal                                          |                                                                                                            |
| Egypt Standard Time             | (UTC+02:00)          | Cairo                                             |                                                                                                            |
| Ekaterinburg Standard Time      | (UTC+05:00)          | Ekaterinburg                                      |                                                                                                            |
| Fiji Standard Time              | (UTC+12:00)          | Fiji                                              |                                                                                                            |
| FLE Standard Time               | (UTC+02:00)          | Helsinki, Kyiv, Riga, Sofia, Tallinn, Vilnius     |                                                                                                            |
| Georgian Standard Time          | (UTC+04:00)          | Tbilisi                                           | This time zone doesn't observe daylight saving time.                                                       |
| GMT Standard Time               | (UTC)                | Dublin, Edinburgh, Lisbon, London                 | This time zone isn't the same as Greenwich Mean Time.<br>This time zone does observe daylight saving time. |
| Greenland Standard Time         | (UTC–03:00)          | Greenland                                         |                                                                                                            |
| Greenwich Standard Time         | (UTC)                | Monrovia, Reykjavik                               | This time zone doesn't observe daylight saving time.                                                       |
| GTB Standard Time               | (UTC+02:00)          | Athens, Bucharest                                 |                                                                                                            |
| Haiti Standard Time             | (UTC–05:00)          | Haiti                                             |                                                                                                            |
| Hawaiian Standard Time          | (UTC–10:00)          | Hawaii                                            |                                                                                                            |
| India Standard Time             | (UTC+05:30)          | Chennai, Kolkata, Mumbai, New Delhi               | This time zone doesn't observe daylight saving time.                                                       |
| Iran Standard Time              | (UTC+03:30)          | Tehran                                            |                                                                                                            |
| Israel Standard Time            | (UTC+02:00)          | Jerusalem                                         |                                                                                                            |
| Jordan Standard Time            | (UTC+02:00)          | Amman                                             |                                                                                                            |
| Kaliningrad Standard Time       | (UTC+02:00)          | Kaliningrad                                       |                                                                                                            |
| Kamchatka Standard Time         | (UTC+12:00)          | Petropavlovsk-Kamchatsky – Old                    |                                                                                                            |
| Korea Standard Time             | (UTC+09:00)          | Seoul                                             | This time zone doesn't observe daylight saving time.                                                       |
| Libya Standard Time             | (UTC+02:00)          | Tripoli                                           |                                                                                                            |
| Line Islands Standard Time      | (UTC+14:00)          | Kiritimati Island                                 |                                                                                                            |
| Lord Howe Standard Time         | (UTC+10:30)          | Lord Howe Island                                  |                                                                                                            |
| Magadan Standard Time           | (UTC+11:00)          | Magadan                                           | This time zone doesn't observe daylight saving time.                                                       |
| Magallanes Standard Time        | (UTC–03:00)          | Punta Arenas                                      |                                                                                                            |
| Marquesas Standard Time         | (UTC–09:30)          | Marquesas Islands                                 |                                                                                                            |
| Mauritius Standard Time         | (UTC+04:00)          | Port Louis                                        | This time zone doesn't observe daylight saving time.                                                       |
| Middle East Standard Time       | (UTC+02:00)          | Beirut                                            |                                                                                                            |
| Montevideo Standard Time        | (UTC–03:00)          | Montevideo                                        |                                                                                                            |
| Morocco Standard Time           | (UTC+01:00)          | Casablanca                                        |                                                                                                            |
| Mountain Standard Time          | (UTC–07:00)          | Mountain Time (US and Canada)                     |                                                                                                            |
| Mountain Standard Time (Mexico) | (UTC–07:00)          | Chihuahua, La Paz, Mazatlan                       |                                                                                                            |
| Myanmar Standard Time           | (UTC+06:30)          | Yangon (Rangoon)                                  | This time zone doesn't observe daylight saving time.                                                       |
| N. Central Asia Standard Time   | (UTC+07:00)          | Novosibirsk                                       |                                                                                                            |
| Namibia Standard Time           | (UTC+02:00)          | Windhoek                                          |                                                                                                            |
| Nepal Standard Time             | (UTC+05:45)          | Kathmandu                                         | This time zone doesn't observe daylight saving time.                                                       |
| New Zealand Standard Time       | (UTC+12:00)          | Auckland, Wellington                              |                                                                                                            |
| Newfoundland Standard Time      | (UTC–03:30)          | Newfoundland                                      |                                                                                                            |
| Norfolk Standard Time           | (UTC+11:00)          | Norfolk Island                                    |                                                                                                            |
| North Asia East Standard Time   | (UTC+08:00)          | Irkutsk                                           |                                                                                                            |
| North Asia Standard Time        | (UTC+07:00)          | Krasnoyarsk                                       |                                                                                                            |
| North Korea Standard Time       | (UTC+09:00)          | Pyongyang                                         |                                                                                                            |
| Omsk Standard Time              | (UTC+06:00)          | Omsk                                              |                                                                                                            |
| Pacific SA Standard Time        | (UTC–03:00)          | Santiago                                          |                                                                                                            |
| Pacific Standard Time           | (UTC–08:00)          | Pacific Time (US and Canada)                      |                                                                                                            |
| Pacific Standard Time (Mexico)  | (UTC–08:00)          | Baja California                                   |                                                                                                            |
| Pakistan Standard Time          | (UTC+05:00)          | Islamabad, Karachi                                | This time zone doesn't observe daylight saving time.                                                       |
| Paraguay Standard Time          | (UTC–04:00)          | Asuncion                                          |                                                                                                            |
| Romance Standard Time           | (UTC+01:00)          | Brussels, Copenhagen, Madrid, Paris               |                                                                                                            |
| Russia Time Zone 10             | (UTC+11:00)          | Chokurdakh                                        |                                                                                                            |
| Russia Time Zone 11             | (UTC+12:00)          | Anadyr, Petropavlovsk-Kamchatsky                  |                                                                                                            |
| Russia Time Zone 3              | (UTC+04:00)          | Izhevsk, Samara                                   |                                                                                                            |
| Russian Standard Time           | (UTC+03:00)          | Moscow, St. Petersburg, Volgograd                 | This time zone doesn't observe daylight saving time.                                                       |
| SA Eastern Standard Time        | (UTC–03:00)          | Cayenne, Fortaleza                                | This time zone doesn't observe daylight saving time.                                                       |
| SA Pacific Standard Time        | (UTC–05:00)          | Bogota, Lima, Quito, Rio Branco                   | This time zone doesn't observe daylight saving time.                                                       |
| SA Western Standard Time        | (UTC–04:00)          | Georgetown, La Paz, Manaus, San Juan              | This time zone doesn't observe daylight saving time.                                                       |
| Saint Pierre Standard Time      | (UTC–03:00)          | Saint Pierre and Miquelon                         |                                                                                                            |
| Sakhalin Standard Time          | (UTC+11:00)          | Sakhalin                                          |                                                                                                            |
| Samoa Standard Time             | (UTC+13:00)          | Samoa                                             |                                                                                                            |
| Sao Tome Standard Time          | (UTC+01:00)          | Sao Tome                                          |                                                                                                            |
| Saratov Standard Time           | (UTC+04:00)          | Saratov                                           |                                                                                                            |
| SE Asia Standard Time           | (UTC+07:00)          | Bangkok, Hanoi, Jakarta                           | This time zone doesn't observe daylight saving time.                                                       |
| Singapore Standard Time         | (UTC+08:00)          | Kuala Lumpur, Singapore                           | This time zone doesn't observe daylight saving time.                                                       |
| South Africa Standard Time      | (UTC+02:00)          | Harare, Pretoria                                  | This time zone doesn't observe daylight saving time.                                                       |
| Sri Lanka Standard Time         | (UTC+05:30)          | Sri Jayawardenepura                               | This time zone doesn't observe daylight saving time.                                                       |
| Sudan Standard Time             | (UTC+02:00)          | Khartoum                                          |                                                                                                            |
| Syria Standard Time             | (UTC+02:00)          | Damascus                                          |                                                                                                            |
| Taipei Standard Time            | (UTC+08:00)          | Taipei                                            | This time zone doesn't observe daylight saving time.                                                       |
| Tasmania Standard Time          | (UTC+10:00)          | Hobart                                            |                                                                                                            |
| Tocantins Standard Time         | (UTC–03:00)          | Araguaina                                         |                                                                                                            |
| Tokyo Standard Time             | (UTC+09:00)          | Osaka, Sapporo, Tokyo                             | This time zone doesn't observe daylight saving time.                                                       |
| Tomsk Standard Time             | (UTC+07:00)          | Tomsk                                             |                                                                                                            |
| Tonga Standard Time             | (UTC+13:00)          | Nuku'alofa                                        | This time zone doesn't observe daylight saving time.                                                       |
| Transbaikal Standard Time       | (UTC+09:00)          | Chita                                             |                                                                                                            |
| Turkey Standard Time            | (UTC+03:00)          | Istanbul                                          |                                                                                                            |
| Turks And Caicos Standard Time  | (UTC–05:00)          | Turks and Caicos                                  |                                                                                                            |
| Ulaanbaatar Standard Time       | (UTC+08:00)          | Ulaanbaatar                                       | This time zone doesn't observe daylight saving time.                                                       |
| US Eastern Standard Time        | (UTC–05:00)          | Indiana (East)                                    |                                                                                                            |
| US Mountain Standard Time       | (UTC–07:00)          | Arizona                                           | This time zone doesn't observe daylight saving time.                                                       |
| UTC                             | UTC                  | Coordinated Universal Time                        | This time zone doesn't observe daylight saving time.                                                       |
| UTC–02                          | (UTC–02:00)          | Coordinated Universal Time–02                     | This time zone doesn't observe daylight saving time.                                                       |
| UTC–08                          | (UTC–08:00)          | Coordinated Universal Time–08                     |                                                                                                            |
| UTC–09                          | (UTC–09:00)          | Coordinated Universal Time–09                     |                                                                                                            |
| UTC–11                          | (UTC–11:00)          | Coordinated Universal Time–11                     | This time zone doesn't observe daylight saving time.                                                       |
| UTC+12                          | (UTC+12:00)          | Coordinated Universal Time+12                     | This time zone doesn't observe daylight saving time.                                                       |
| UTC+13                          | (UTC+13:00)          | Coordinated Universal Time+13                     |                                                                                                            |
| Venezuela Standard Time         | (UTC–04:00)          | Caracas                                           | This time zone doesn't observe daylight saving time.                                                       |
| Vladivostok Standard Time       | (UTC+10:00)          | Vladivostok                                       |                                                                                                            |
| Volgograd Standard Time         | (UTC+04:00)          | Volgograd                                         |                                                                                                            |
| W. Australia Standard Time      | (UTC+08:00)          | Perth                                             | This time zone doesn't observe daylight saving time.                                                       |
| W. Central Africa Standard Time | (UTC+01:00)          | West Central Africa                               | This time zone doesn't observe daylight saving time.                                                       |
| W. Europe Standard Time         | (UTC+01:00)          | Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna  |                                                                                                            |
| W. Mongolia Standard Time       | (UTC+07:00)          | Hovd                                              |                                                                                                            |
| West Asia Standard Time         | (UTC+05:00)          | Ashgabat, Tashkent                                | This time zone doesn't observe daylight saving time.                                                       |
| West Bank Standard Time         | (UTC+02:00)          | Gaza, Hebron                                      |                                                                                                            |
| West Pacific Standard Time      | (UTC+10:00)          | Guam, Port Moresby                                | This time zone doesn't observe daylight saving time.                                                       |
| Yakutsk Standard Time           | (UTC+09:00)          | Yakutsk                                           |                                                                                                            |
