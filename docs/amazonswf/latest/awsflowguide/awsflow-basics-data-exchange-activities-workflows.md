# AWS Flow Framework Basic Concepts: Data Exchange Between Activities and Workflows

When you call an asynchronous activity client method, it immediately returns a _Promise_
(also known as a _Future_) object, which represents the activity method's return value. Initially,
the Promise is in an unready state and the return value is undefined. After the activity method completes its task
and returns, the framework marshals the return value across the network to the workflow worker, which assigns a value
to the Promise and puts the object in a ready state.

Even if an activity method has no return value, you can still use the Promise for managing
workflow execution. If you pass a returned Promise to an activity client method or an
asynchronous workflow method, it defers execution until the object is ready.

If you pass one or more Promises to an activity client method, the framework queues the task but defers
scheduling it until all the objects are ready. It then extracts the data from each Promise and marshals it across the
internet to the activity worker, which passes it to the activity method as a standard type.

###### Note

If you need to transfer large amounts of data between workflow and activity workers, the preferred approach
is to store the data in a convenient location and just pass the retrieval information. For example, you can store
the data in an Amazon S3 bucket and pass the associated URL.

## The Promise<T> Type

The `Promise<T>` type is similar in some ways to the Java
`Future<T>` type. Both types represent values returned by asynchronous
methods and are initially undefined. You access an object's value by calling its
`get` method. Beyond that, the two types behave quite differently.

- `Future<T>` is a synchronization construct that allows an application to wait on an
  asynchronous method's completion. If you call `get` and the object isn't ready, it blocks until
  the object is ready.
- With `Promise<T>`, synchronization is handled by the framework. If you call
  `get` and the object isn't ready, `get` throws an exception.

The primary purpose of `Promise<T>` is to manage data flow from one activity to another. It
ensures that an activity doesn't execute until the input data is valid. In many cases, workflow workers don't need
to access `Promise<T>` objects directly; they simply pass the objects from one activity to
another and let the framework and the activity workers handle the details. To access a
`Promise<T>` object's value in a workflow worker, you must be certain that the object is ready
before calling its `get` method.

- The preferred approach is to pass the `Promise<T>` object to an asynchronous workflow
  method and process the values there. An asynchronous method defers execution until all of its input
  `Promise<T>` objects are ready, which guarantees that you can safely access their
  values.
- `Promise<T>` exposes an `isReady` method that returns `true` if
  the object is ready. Using `isReady` to poll a `Promise<T>` object isn't
  recommended, but `isReady` is useful in certain circumstances.

The AWS Flow Framework for Java also includes a `Settable<T>` type, which is derived from
`Promise<T>` and has similar behavior. The difference is that the framework usually sets the
value of a `Promise<T>` object and the workflow worker is responsible for setting the value of a
`Settable<T>`.

There are some circumstance where a workflow worker needs to create a `Promise<T>` object and
set its value. For example, an asynchronous method that returns a `Promise<T>` object needs to
create a return value.

- To create an object that represents a typed value, call the static `Promise.asPromise`
  method, which creates a `Promise<T>` object of the appropriate type, sets its value, and
  puts it in the ready state.
- To create a `Promise<Void>` object, call the static `Promise.Void`
  method.

###### Note

`Promise<T>` can represent any valid type. However, if the data must be marshaled
across the internet, the type must be compatible with the data converter. See the next section for
details.

## Data Converters and Marshaling

The AWS Flow Framework marshals data across the internet by using a data converter. By default, the framework uses a
data converter that is based on the [Jackson JSON processor](https://github.com/codehaus/jackson "https://github.com/codehaus/jackson").
However, this converter has some limitations. For example, it can't marshal maps that don't use strings as keys.
If the default converter isn't sufficient for your application, you can implement a custom data converter. For
details, see [DataConverters](dataconverters.md "dataconverters.md").
