# Add annotations and metadata to segments with the

X-Ray SDK for Java

###### Note

X-Ray SDK/Daemon Maintenance Notice – On February 25th, 2026, the AWS X-Ray SDKs/Daemon will enter maintenance mode, where AWS will limit X-Ray SDK and Daemon releases to address security issues only. For more information on the support timeline, see
[X-Ray SDK and Daemon Support timeline](xray-sdk-daemon-timeline.md "xray-sdk-daemon-timeline.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

You can record additional information about requests, the
environment, or your application with annotations and metadata. You can add annotations and
metadata to the segments that the X-Ray SDK creates, or to custom subsegments that you create.

**Annotations** are
key-value pairs with string, number, or Boolean values. Annotations are indexed for use with
[filter expressions](xray-console-filters.md "xray-console-filters.md"). Use annotations to record data
that you want to use to group traces in the console, or when calling the [`GetTraceSummaries`](../api/API_GetTraceSummaries.md "../api/API_GetTraceSummaries.md")
API.

**Metadata** are key-value
pairs that can have values of any type, including objects and lists, but are not indexed for use
with filter expressions. Use metadata to record additional data that you want stored in the trace
but don't need to use with search.

In addition to annotations and metadata, you can also [record user ID strings](#xray-sdk-java-segment-userid "#xray-sdk-java-segment-userid") on segments. User IDs are
recorded in a separate field on segments and are indexed for use with search.

###### Sections

- [Recording annotations with the
  X-Ray SDK for Java](#xray-sdk-java-segment-annotations "#xray-sdk-java-segment-annotations")
- [Recording metadata with the
  X-Ray SDK for Java](#xray-sdk-java-segment-metadata "#xray-sdk-java-segment-metadata")
- [Recording user IDs with the
  X-Ray SDK for Java](#xray-sdk-java-segment-userid "#xray-sdk-java-segment-userid")

## Recording annotations with the

X-Ray SDK for Java

Use annotations to record information on segments or subsegments that you want indexed for
search.

###### Annotation Requirements

- **Keys** – The key for an X-Ray annotation can have
  up to 500 alphanumeric characters. You cannot use spaces or symbols other
  than a dot or period ( . )
- **Values** – The value for an X-Ray annotation can have up to 1,000 Unicode
  characters.
- The number of **Annotations** – You can use up to 50 annotations per
  trace.

###### To record annotations

1. Get a reference to the current segment or subsegment from `AWSXRay`.

```
import com.amazonaws.xray.AWSXRay;
import com.amazonaws.xray.entities.Segment;
...
Segment document = AWSXRay.getCurrentSegment();
```

or

```
import com.amazonaws.xray.AWSXRay;
import com.amazonaws.xray.entities.Subsegment;
...
Subsegment document = AWSXRay.getCurrentSubsegment();
```

2. Call `putAnnotation` with a String key, and a Boolean, Number, or String
   value.

```
document.putAnnotation("mykey", "my value");
```

The following example shows how to call `putAnnotation` with a String key
that includes a dot, and a Boolean, Number, or String value.

```
document.putAnnotation("testkey.test", "my value");
```

The SDK records annotations as key-value pairs in an `annotations` object in
the segment document. Calling `putAnnotation` twice with the same key overwrites
previously recorded values on the same segment or subsegment.

To find traces that have annotations with specific values, use the
`annotation[`key`]` keyword in a [filter expression](xray-console-filters.md "xray-console-filters.md").

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

## Recording metadata with the

X-Ray SDK for Java

Use metadata to record information on segments or subsegments that you don't need indexed
for search. Metadata values can be strings, numbers, Booleans, or any object that can be
serialized into a JSON object or array.

###### To record metadata

1. Get a reference to the current segment or subsegment from `AWSXRay`.

```
import com.amazonaws.xray.AWSXRay;
import com.amazonaws.xray.entities.Segment;
...
Segment document = AWSXRay.getCurrentSegment();
```

or

```
import com.amazonaws.xray.AWSXRay;
import com.amazonaws.xray.entities.Subsegment;
...
Subsegment document = AWSXRay.getCurrentSubsegment();
```

2. Call `putMetadata` with a String namespace, String key, and a Boolean,
   Number, String, or Object value.

```
document.putMetadata("`my namespace`", "`my key`", "`my value`");
```

or

Call `putMetadata` with just a key and value.

```
document.putMetadata("`my key`", "`my value`");
```

If you don't specify a namespace, the SDK uses `default`. Calling
`putMetadata` twice with the same key overwrites previously recorded values on
the same segment or subsegment.

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

## Recording user IDs with the

X-Ray SDK for Java

Record user IDs on request segments to identify the user who sent the request.

###### To record user IDs

1. Get a reference to the current segment from `AWSXRay`.

```
import com.amazonaws.xray.AWSXRay;
import com.amazonaws.xray.entities.Segment;
...
Segment document = AWSXRay.getCurrentSegment();
```

2. Call `setUser` with a string ID of the user who sent the request.

```
document.setUser("`U12345`");
```

You can call `setUser` in your controllers to record the user ID as soon as
your application starts processing a request. If you will only use the segment to set the user
ID, you can chain the calls in a single line.

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

To find traces for a user ID, use the `user` keyword in a [filter expression](xray-console-filters.md "xray-console-filters.md").
