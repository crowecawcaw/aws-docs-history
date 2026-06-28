# Static overlay, creating and modifying a non-running event

## Overlays at top level

|                    |                      |                           |                   |
| ------------------ | -------------------- | ------------------------- | ----------------- |
| <image\_inserter>  |                      |                           |                   |
|                    | enable\_rest         |                           |                   |
|                    | <insertable\_image>  |                           |                   |
|                    |                      | duration                  |                   |
|                    |                      | fade\_in                  |                   |
|                    |                      | fade\_out                 |                   |
|                    |                      | height                    |                   |
|                    |                      | image\_x                  |                   |
|                    |                      | image\_y                  |                   |
|                    |                      | layer                     |                   |
|                    |                      | opacity                   |                   |
|                    |                      | start\_time               |                   |
|                    |                      | width                     |                   |
|                    |                      | <image\_inserter\_input>  |                   |
|                    |                      |                           | certificate\_file |
|                    |                      |                           | interface         |
|                    |                      |                           | password          |
|                    |                      |                           | uri               |
|                    |                      |                           | username          |
|                    |                      | </image\_inserter\_input> |                   |
|                    | </insertable\_image> |                           |                   |
| </image\_inserter> |                      |                           |                   |

## Overlays in input section

**Data in <input> element**

|         |                   |                      |                           |                   |
| ------- | ----------------- | -------------------- | ------------------------- | ----------------- |
| <input> |                   |                      |                           |                   |
|         | <image\_inserter> |                      |                           |                   |
|         |                   | enable\_rest         |                           |                   |
|         |                   | <insertable\_image>  |                           |                   |
|         |                   |                      | duration                  |                   |
|         |                   |                      | fade\_in                  |                   |
|         |                   |                      | fade\_out                 |                   |
|         |                   |                      | height                    |                   |
|         |                   |                      | image\_x                  |                   |
|         |                   |                      | image\_y                  |                   |
|         |                   |                      | layer                     |                   |
|         |                   |                      | opacity                   |                   |
|         |                   |                      | start\_time               |                   |
|         |                   |                      | width                     |                   |
|         |                   |                      | <image\_inserter\_input>  |                   |
|         |                   |                      |                           | certificate\_file |
|         |                   |                      |                           | interface         |
|         |                   |                      |                           | password          |
|         |                   |                      |                           | uri               |
|         |                   |                      |                           | username          |
|         |                   |                      | </image\_inserter\_input> |                   |
|         |                   | </insertable\_image> |                           |                   |

## Overlays in Ssream assembly section

**Data in <stream\_assembly>**

|                    |                      |                        |                   |                      |                               |                   |
| ------------------ | -------------------- | ---------------------- | ----------------- | -------------------- | ----------------------------- | ----------------- |
| <stream\_assembly> |                      |                        |                   |                      |                               |                   |
|                    | <video\_description> |                        |                   |                      |                               |                   |
|                    |                      | <video\_preprocessors> |                   |                      |                               |                   |
|                    |                      |                        | <image\_inserter> |                      |                               |                   |
|                    |                      |                        |                   | enable\_rest         |                               |                   |
|                    |                      |                        |                   | <insertable\_image>  |                               |                   |
|                    |                      |                        |                   |                      | duration                      |                   |
|                    |                      |                        |                   |                      | fade\_in                      |                   |
|                    |                      |                        |                   |                      | fade\_out                     |                   |
|                    |                      |                        |                   |                      | height                        |                   |
|                    |                      |                        |                   |                      | image\_x                      |                   |
|                    |                      |                        |                   |                      | image\_y                      |                   |
|                    |                      |                        |                   |                      | layer                         |                   |
|                    |                      |                        |                   |                      | opacity                       |                   |
|                    |                      |                        |                   |                      | start\_time                   |                   |
|                    |                      |                        |                   |                      | width                         |                   |
|                    |                      |                        |                   |                      | <image\_inserter<br>\_input>  |                   |
|                    |                      |                        |                   |                      |                               | certificate\_file |
|                    |                      |                        |                   |                      |                               | interface         |
|                    |                      |                        |                   |                      |                               | password          |
|                    |                      |                        |                   |                      |                               | uri               |
|                    |                      |                        |                   |                      |                               | username          |
|                    |                      |                        |                   |                      | </image\_inserter<br>\_input> |                   |
|                    |                      |                        |                   | </insertable\_image> |                               |                   |
|                    |                      |                        | <image\_inserter> |                      |                               |                   |
