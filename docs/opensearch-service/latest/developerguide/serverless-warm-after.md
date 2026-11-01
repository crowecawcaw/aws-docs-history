

# Using the warm-after setting in time series collections
<a name="serverless-warm-after"></a>

Amazon OpenSearch Serverless NextGen time series collections use a combination of hot and warm storage. You use the `index.warm.after` index setting to specify the *warm-after period*, which is how long data in an index stays in hot storage before OpenSearch Serverless moves it to warm storage. You can specify the setting when you create an index or in an index template, and you can change it later by updating the index settings. Warm storage applies to data within an index, not to the index as a whole, so an index can contain both hot and warm data at the same time.

**Note**  
The `index.warm.after` setting and warm storage apply only to NextGen time series collections. OpenSearch Serverless rejects the setting for search and vector search collections, and for OpenSearch Serverless Classic collections.

**Note**  
Changing the warm-after period only affects the new data movement to warm.

**Topics**
+ [Specifying the warm-after period](#serverless-warm-after-setting)
+ [Changing the warm-after period](#serverless-warm-after-update)
+ [Moving data to warm storage](#serverless-warm-after-transition)
+ [Resolving warm-after validation errors](#serverless-warm-after-errors)

## Specifying the warm-after period
<a name="serverless-warm-after-setting"></a>

You specify the warm-after period as a positive whole number followed by a unit suffix: `d` for days or `h` for hours (such as `7d` or `36h`). This setting is **optional**. If you don't specify it, the index uses a default warm-after period of `1d`. Other units, such as minutes or seconds, aren't supported. The value must meet the following limits:
+ The value must be at least `24h` or `1d`.
+ If the index has a data retention period (`index.data.retention`), the value can't be greater than the data retention period.
+ If the index doesn't have a data retention period, the value can't be greater than `3650d`.

When OpenSearch Serverless applies the value to an index, it removes leading zeros. For example, a value of `007d` is stored in the index settings as `7d`.

OpenSearch Serverless resolves the warm-after period for an index in the following order of precedence:

1. The `index.warm.after` setting in the create index request.

1. The `index.warm.after` setting in the index template that matches the index. If more than one index template matches, only the template with the highest priority applies. A value in the index template takes precedence over a value in any component template that the index template uses.

1. The default warm-after period of `1d`, if neither the create index request nor a matching index template specifies the setting.

The following OpenSearch REST API request creates an index named `my-logs` with a warm-after period of 7 days.

```
PUT /{{my-logs}}
{
  "settings": {
    "index": {
      "warm": {
        "after": "{{7d}}"
      }
    }
  }
}
```
+ {{my-logs}}: The name of your index.
+ {{7d}}: The warm-after period, as a positive whole number followed by `d` (days) or `h` (hours).

If neither the create index request nor a matching index template specifies the setting, the index uses a warm-after period of `1d`. To view the warm-after period of an index, send a `GET /{{my-logs}}/_settings` request.

**Note**  
OpenSearch Serverless validates the `index.warm.after` value when you create an index template or component template, and again when it creates an index from the template. When it creates the index, it checks the value against the data retention period of the new index.

## Changing the warm-after period
<a name="serverless-warm-after-update"></a>

To change the warm-after period of an existing index, update the `index.warm.after` setting. The following OpenSearch REST API request changes the warm-after period of the `my-logs` index to 3 days.

```
PUT /{{my-logs}}/_settings
{
  "index": {
    "warm": {
      "after": "{{3d}}"
    }
  }
}
```
+ {{my-logs}}: The name of your index.
+ {{3d}}: The new warm-after period, as a positive whole number followed by `d` (days) or `h` (hours).

The new value must meet the same limits as when you create an index. OpenSearch Serverless checks the new value against the current data retention period of the index. If you update `index.data.retention` and `index.warm.after` in the same request, OpenSearch Serverless checks the warm-after period against the new data retention period.

The change has the following effects:
+ Data that hasn't moved to warm storage yet uses the new warm-after period. The period is still measured from the same starting point. For more information, see the following section.
+ If you shorten the warm-after period and the new period has already elapsed for some data, that data moves to warm storage the next time OpenSearch Serverless checks for eligible data.
+ If you lengthen the warm-after period, data that hasn't moved stays in hot storage longer. Data that is already about to move to warm storage when you make the change might still move on its original schedule.
+ Data that has already moved to warm storage stays in warm storage. Lengthening the warm-after period doesn't move data back to hot storage.

**Note**  
The new value appears in the index settings immediately, but warm transitions can take approximately 15 minutes or longer to apply the change to existing data.

You can't remove the `index.warm.after` setting from an index. A request that sets the value to `null` is rejected. To change the warm-after period, specify a new valid value.

## Moving data to warm storage
<a name="serverless-warm-after-transition"></a>

OpenSearch Serverless moves data to warm storage in the order that the data was ingested. Older data in an index moves to warm storage first. Recently ingested data stays in hot storage. As a result, an index usually contains both hot and warm data.

You work with the index the same way regardless of which storage holds the data: you search, update, and delete documents through the index, and OpenSearch Serverless reads from both hot and warm storage.

OpenSearch Serverless stores the data of an index in underlying storage that it creates over time. The warm-after period is measured from when OpenSearch Serverless creates the underlying storage that holds the data. It isn't measured from when you ingest a document or from the value of a document's timestamp field. Data in the same underlying storage moves to warm storage together. Because of this, a document that you ingest after that storage is created can spend less than the full warm-after period in hot storage.

## Resolving warm-after validation errors
<a name="serverless-warm-after-errors"></a>

If the `index.warm.after` value isn't valid, or the setting isn't supported for the target, OpenSearch Serverless rejects the request with an HTTP `400` error. The error message describes the cause. In the following messages, `<value>` is the value that you specified (without leading zeros, in the messages about maximum values), and `<N>` is the data retention period of the index in days.

The value isn't a positive whole number with a `d` or `h` suffix, or is `null`.  

```
index.warm.after: invalid value '<value>', must be a positive integer with 'd' or 'h' suffix
```
The message ends with the example values `7d` and `24h`.

The value is less than `24h`.  

```
index.warm.after setting value in hours must be >= 24h
```

The value is greater than the data retention period of the index.  

```
index.warm.after: value '<value>' must be less than or equal to data retention value (<N>d)
```

The index has no data retention period and the value is greater than `3650d`.  

```
index.warm.after: value '<value>' must be less than or equal to 3650d
```

The collection is an OpenSearch Serverless Classic collection.  

```
index.warm.after setting is not supported for OpenSearch Serverless Classic collections.
```

The collection isn't a time series collection.  

```
index.warm.after setting is only supported for TIMESERIES collections
```