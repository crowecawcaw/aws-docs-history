# FlexMatch property

expressions

Property expressions can be used to define certain matchmaking-related properties. They
allow you to use calculations and logic when defining a property value. Property expressions
generally result in one of two forms:

- Individual player data.
- Calculated collections of individual player data.

## Common matchmaking property

expressions

A property expression identifies a specific value for a player, team, or match. The
following partial expressions illustrate how to identify teams and players:

| Goal                                                       | Input                    | Meaning                               | Output             |
| ---------------------------------------------------------- | ------------------------ | ------------------------------------- | ------------------ |
| To identify a specific team in a match:                    | `teams[red]`             | The Red team                          | Team               |
| To identify a set of specific teams in a match:            | `teams[red,blue]`        | The Red team and the Blue team        | List<Team>         |
| To identify all teams in a match:                          | `teams[*]`               | All teams                             | List<Team>         |
| To identify players in a specific team:                    | `team[red].players`      | Players in the Red team               | List<Player>       |
| To identify players in a set of specific teams in a match: | `team[red,blue].players` | Players in the match, grouped by team | List<List<Player>> |
| To identify players in a match:                            | `team[*].players`        | Players in the match, grouped by team | List<List<Player>> |

## Property expression

examples

The following table illustrates some property expressions that build on the previous
examples:

| Expression                                  | Meaning                                                                                     | Resulting Type     |
| ------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------ |
| `teams[red].players[playerId]`              | The player IDs of all players on the red team                                               | List<string>       |
| `teams[red].players.attributes[skill]`      | The "skill" attributes of all players on the red team                                       | List<number>       |
| `teams[red,blue].players.attributes[skill]` | The "skill" attributes of all players on the Red team and the Blue<br>team, grouped by team | List<List<number>> |
| `teams[*].players.attributes[skill]`        | The "skill" attributes of all players in the match, grouped by<br>team                      | List<List<number>> |

## Property expression

aggregations

Property expressions can be used to aggregate team data by using the following
functions or combinations of functions:

| Aggregation        | Input              | Meaning                                                                                               | Output       |
| ------------------ | ------------------ | ----------------------------------------------------------------------------------------------------- | ------------ |
| `min`              | List<number>       | Get the minimum of all numbers in the list.                                                           | number       |
| `max`              | List<number>       | Get the maximum of all numbers in the list.                                                           | number       |
| `avg`              | List<number>       | Get the average of all numbers in the list.                                                           | number       |
| `median`           | List<number>       | Get the median of all numbers in the list.                                                            | number       |
| `sum`              | List<number>       | Get the sum of all numbers in the list.                                                               | number       |
| `count`            | List<?>            | Get the number of elements in the list.                                                               | number       |
| `stddev`           | List<number>       | Get the standard deviation of all numbers in the list.                                                | number       |
| `flatten`          | List<List<?>>      | Turn a collection of nested lists into a single list containing all<br>elements.                      | List<?>      |
| `set_intersection` | List<List<string>> | Get a list of strings that are found in all string lists in a<br>collection.                          | List<string> |
| All above          | List<List<?>>      | All operations on a nested list operate on each sublist individually<br>to produce a list of results. | List<?>      |

The following table illustrates some valid property expressions that use aggregation
functions:

| Expression                                        | Meaning                                                                                                                                | Resulting Type |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| flatten(teams[\*].players.attributes[skill])      | The "skill" attributes of all players in the match (not<br>grouped)                                                                    | List<number>   |
| avg(teams[red].players.attributes[skill])         | The average skill of the red team players                                                                                              | number         |
| avg(teams[\*].players.attributes[skill])          | The average skill of each team in the match                                                                                            | List<number>   |
| avg(flatten(teams[\*].players.attributes[skill])) | The average skill level of all players in the match. This expression<br>gets a flattened list of player skills and then averages them. | number         |
| count(teams[red].players)                         | The number of players on the red team                                                                                                  | number         |
| count (teams[\*].players)                         | The number of players on each team in the match                                                                                        | List<number>   |
| max(avg(teams[\*].players.attributes[skill]))     | The highest team skill level in the match                                                                                              | number         |
