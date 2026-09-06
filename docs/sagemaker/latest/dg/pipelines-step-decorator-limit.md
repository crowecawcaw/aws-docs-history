

# Limitations
<a name="pipelines-step-decorator-limit"></a>

The following sections outline the limitations that you should be aware of when you use the `@step` decorator for your pipeline steps.

## Function argument limitations
<a name="pipelines-step-decorator-arg"></a>

When you pass an input argument to the `@step`-decorated function, the following limitations apply:
+ You can pass the `DelayedReturn`, `Properties` (of steps of other types), `Parameter`, and `ExecutionVariable` objects to `@step`-decorated functions as arguments. But `@step`-decorated functions do not support `JsonGet` and `Join` objects as arguments.
+ You cannot directly access a pipeline variable from a `@step` function. The following example produces an error:

  ```
  param = ParameterInteger(name="{{<parameter-name>}}", default_value=10)
  
  @step
  def func():
      print(param)
  
  func() # this raises a SerializationError
  ```
+ You cannot nest a pipeline variable in another object and pass it to a `@step` function. The following example produces an error:

  ```
  param = ParameterInteger(name="{{<parameter-name>}}", default_value=10)
  
  @step
  def func(arg):
      print(arg)
  
  func(arg=(param,)) # this raises a SerializationError because param is nested in a tuple
  ```
+ Since inputs and outputs of a function are serialized, there are restrictions on the type of data that can be passed as input or output from a function. See the *Data serialization and deserialization* section of [Invoke a remote function](train-remote-decorator-invocation.md) for more details. The same restrictions apply to `@step`-decorated functions.
+ Any object that has a boto client cannot be serialized, hence you cannot pass such objects as input to or output from a `@step`-decorated function. For example, SageMaker Python SDK client classes such as `Estimator`, `Predictor`, and `Processor` can't be serialized.

## Function imports
<a name="pipelines-step-decorator-best-import"></a>

You should import the libraries required by the step inside rather than outside the function. If you import them at global scope, you risk an import collision while serializing the function. For example, `sklearn.pipeline.Pipeline` could be overridden by `sagemaker.workflow.pipeline.Pipeline`.

## Referencing child members of function return value
<a name="pipelines-step-decorator-best-child"></a>

If you reference child members of a `@step`-decorated function's return value, the following limitations apply:
+ You can reference the child members with `[]` if the `DelayedReturn` object represents a tuple, list or dict, as shown in the following example:

  ```
  delayed_return[0]
  delayed_return["a_key"]
  delayed_return[1]["a_key"]
  ```
+ You cannot unpack a tuple or list output because the exact length of the underlying tuple or list can't be known when you invoke the function. The following example produces an error:

  ```
  a, b, c = func() # this raises ValueError
  ```
+ You cannot iterate over a `DelayedReturn` object. The following example raises an error:

  ```
  for item in func(): # this raises a NotImplementedError
  ```
+ You cannot reference arbitrary child members with '`.`'. The following example produces an error:

  ```
  delayed_return.a_child # raises AttributeError
  ```

## Existing pipeline features that are not supported
<a name="pipelines-step-decorator-best-unsupported"></a>

You cannot use the `@step` decorator with the following pipeline features:
+ [Pipeline step caching](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-caching.html)
+ [Property files](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-propertyfile.html#build-and-manage-propertyfile-property)