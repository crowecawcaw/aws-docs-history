# DataConverters

When your workflow implementation calls a remote activity, the inputs
passed to it and the result of executing the activity must be serialized
so they can be sent over the wire. The framework uses the DataConverter
class for this purpose. This is an abstract class that you can implement
to provide your own serializer. A default Jackson serializer–based
implementation, `JsonDataConverter`, is provided in the
framework. For more details, see the [AWS SDK for Java documentation](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/JsonDataConverter.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/JsonDataConverter.md").
Refer to the Jackson JSON Processor documentation for details about how
Jackson performs serialization as well as Jackson annotations that can be
used to influence it. The wire format used is considered part of the
contract. Hence, you can specify a `DataConverter` on your
activities and workflow interfaces by setting the
`DataConverter` property of the `@Activities` and
`@Workflow` annotations.

The framework will create objects of the `DataConverter` type you specified on `@Activities`
annotation to serialize the inputs to the activity and to deserialize its result.
Similarly, objects of the `DataConverter` type you specify on `@Workflow` annotation will be used
to serialize parameters you pass to the workflow, and in the case of child workflow, to
deserialize the result. In addition to inputs, the framework also passes additional data to
Amazon SWF—for example, exception details—the workflow serializer will be used for serializing
this data as well.

You can also provide an instance of the `DataConverter` if you don't want the framework to
automatically create it. The generated clients have constructor overloads that take a
`DataConverter`.

If you don't specify a `DataConverter` type and don't pass a
`DataConverter` object, the `JsonDataConverter` will be used by
default.
