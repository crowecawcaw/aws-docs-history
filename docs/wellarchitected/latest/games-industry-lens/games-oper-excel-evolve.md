#

Evolve

| GAMEOPS05<br>• How do you optimize your game over time? |
| ------------------------------------------------------- |
|                                                         |

**GAMEOPS_BP09: Monitor key game metrics that can help identify player trends and patterns; use the information to rebalance the game, optimize game design, and improve the infrastructure.**

In addition to game client system usage, app usage, exceptions, and crash data, it is
highly recommended that you capture game telemetry data that is sent to a game backend
system. This data should represent player activity so that you can understand how
players interact with various features in the game.

Depending on its implementation, game clients can collect telemetry data at
predefined game features or locations in a game world. The data is sent to the backend
ingestion service for processing. If the backend service is unreachable for any reason,
the clients can store the data locally on the local device until the backend service is
available again. The game designers use this telemetry data to review how players are
playing the game, and if there are any anomalies in the game. For example, player
movements and interactions with items in a map can be extracted from telemetry data and
plotted as a heat map of activities in-game by all players over a set window of time.
Such data helps the game designers identify the need to balance various elements in the
game, such as the power of a weapon, the power of an in-game character, or the
complexity of a map. The raw telemetry data is generally stored and then processed to
extract analytics that can be visualized by analysts.

The [Game Analytics Pipeline](https://aws.amazon.com/solutions/implementations/game-analytics-pipeline/ "https://aws.amazon.com/solutions/implementations/game-analytics-pipeline/")
solution implementation helps game developers launch a scalable serverless data pipeline to ingest, store, and analyze telemetry data generated from games and services. The solution supports streaming ingestion of data, allowing users to gain insights from their games and other applications within minutes.

For custom game telemetry data ingestion, storage, processing and analytics, AWS also offers a number of [specialized services for big data processing and Analytics](https://aws.amazon.com/big-data/datalakes-and-analytics/ "https://aws.amazon.com/big-data/datalakes-and-analytics/").
