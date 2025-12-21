# Recording annotations, metadata, and user IDs

###### Note

X-Ray SDK/Daemon Maintenance Notice – On February 25th, 2026, the AWS X-Ray SDKs/Daemon will enter maintenance mode, where AWS will limit X-Ray SDK and Daemon releases to address security issues only. For more information on the support timeline, see
[X-Ray SDK and Daemon Support timeline](xray-sdk-daemon-timeline.md "xray-sdk-daemon-timeline.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

In the game model class, the application records `Game` objects in a [metadata](xray-sdk-java-segment.md#xray-sdk-java-segment-metadata "xray-sdk-java-segment.md#xray-sdk-java-segment-metadata") block each time it saves a game in
DynamoDB. Separately, the application records game IDs in [annotations](xray-sdk-java-segment.md#xray-sdk-java-segment-annotations "xray-sdk-java-segment.md#xray-sdk-java-segment-annotations") for use with [filter expressions](xray-console-filters.md "xray-console-filters.md").

###### Example [`src/main/java/scorekeep/GameModel.java`](https://github.com/awslabs/eb-java-scorekeep/tree/xray/src/main/java/scorekeep/GameModel.java "https://github.com/awslabs/eb-java-scorekeep/tree/xray/src/main/java/scorekeep/GameModel.java") – Annotations and

metadata

```
import com.amazonaws.xray.AWSXRay;
import com.amazonaws.xray.entities.Segment;
import com.amazonaws.xray.entities.Subsegment;
...
  public void saveGame(Game game) throws SessionNotFoundException {
    // wrap in subsegment
    `Subsegment subsegment = AWSXRay.beginSubsegment("## GameModel.saveGame");`
    try {
      // check session
      String sessionId = game.getSession();
      if (sessionModel.loadSession(sessionId) == null ) {
        throw new SessionNotFoundException(sessionId);
      }
      `Segment segment = AWSXRay.getCurrentSegment();
 subsegment.putMetadata("resources", "game", game);
 segment.putAnnotation("gameid", game.getId());`
      mapper.save(game);
    } catch (Exception e) {
      subsegment.addException(e);
      throw e;
    } finally {
      `AWSXRay.endSubsegment();`
    }
  }
```

In the move controller, the application records [user IDs](xray-sdk-java-segment.md#xray-sdk-java-segment-userid "xray-sdk-java-segment.md#xray-sdk-java-segment-userid") with `setUser`. User IDs
are recorded in a separate field on segments and are indexed for use with search.

###### Example [src/main/java/scorekeep/MoveController.java](https://github.com/awslabs/eb-java-scorekeep/tree/xray/src/main/java/scorekeep/MoveController.java "https://github.com/awslabs/eb-java-scorekeep/tree/xray/src/main/java/scorekeep/MoveController.java") – User ID

```
import com.amazonaws.xray.AWSXRay;
...
  @RequestMapping(value="/{userId}", method=RequestMethod.POST)
  public Move newMove(@PathVariable String sessionId, @PathVariable String gameId, @PathVariable String userId, @RequestBody String move) throws SessionNotFoundException, GameNotFoundException, StateNotFoundException, RulesException {
    `AWSXRay.getCurrentSegment().setUser(userId);`
    return moveFactory.newMove(sessionId, gameId, userId, move);
  }
```
