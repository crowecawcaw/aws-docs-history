# Consume metadata embedded in a Kinesis video stream

To consume the metadata in a Kinesis video stream, use an implementation of
`MkvTagProcessor`:

```
public interface MkvTagProcessor {
        default void process(MkvTag mkvTag, Optional<FragmentMetadata> currentFragmentMetadata) {
            throw new NotImplementedException("Default FragmentMetadataVisitor.MkvTagProcessor");
        }
        default void clear() {
            throw new NotImplementedException("Default FragmentMetadataVisitor.MkvTagProcessor");
	    }
    }
}
```

This interface is found in the [FragmentMetadataVisitor](parser-library-write.md#parser-library-write-FMV "parser-library-write.md#parser-library-write-FMV") class in the [Watch output from cameras using parser library](parser-library.md "parser-library.md").

The `FragmentMetadataVisitor` class contains an implementation of
`MkvTagProcessor`:

```
public static final class BasicMkvTagProcessor implements FragmentMetadataVisitor.MkvTagProcessor {
    @Getter
    private List<MkvTag> tags = new ArrayList<>();

    @Override
    public void process(MkvTag mkvTag, Optional<FragmentMetadata> currentFragmentMetadata) {
        tags.add(mkvTag);
    }

    @Override
    public void clear() {
        tags.clear();
	}
}

```

The `KinesisVideoRendererExample` class contains an example of how to use a
`BasicMkvTagProcessor`. In the following example, a
`BasicMkvTagProcessor` is added to the
`MediaProcessingArguments` of an application:

```
if (renderFragmentMetadata) {
    getMediaProcessingArguments = KinesisVideoRendererExample.GetMediaProcessingArguments.create(
        Optional.of(new FragmentMetadataVisitor.BasicMkvTagProcessor()));
```

The `BasicMkvTagProcessor.process` method is called when fragment metadata arrives. You can
retrieve the accumulated metadata with `GetTags`. To retrieve a single metadata item, first call
`clear` to clear the collected metadata, and then retrieve the metadata items again.
