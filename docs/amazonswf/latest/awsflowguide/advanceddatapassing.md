# Passing Data to Asynchronous Methods

###### Topics

- [Passing Collections and Maps to Asynchronous
  Methods](#advanceddatapassing.collections "#advanceddatapassing.collections")
- [Settable<T>](#advanceddatapassing.settable "#advanceddatapassing.settable")
- [@NoWait](#advanceddatapassing.nowait "#advanceddatapassing.nowait")
- [Promise<Void>](#advanceddatapassing.promise "#advanceddatapassing.promise")
- [AndPromise and OrPromise](#advanceddatapassing.andorpromise "#advanceddatapassing.andorpromise")
  The use of `Promise<`T`>` has been explained in
  previous sections. Some advanced use cases of
  `Promise<`T`>` are discussed here.

## Passing Collections and Maps to Asynchronous

Methods

The framework supports passing arrays, collections, and maps as `Promise` types to
asynchronous methods. For example, an asynchronous method may take
`Promise<ArrayList<String>>` as an argument as shown in the following listing.

```
@Asynchronous
public void printList(Promise<List<String>> list) {
    for (String s: list.get()) {
        activityClient.printActivity(s);
    }
}
```

Semantically, this behaves as any other `Promise` typed parameter and the asynchronous
method will wait until the collection becomes available before executing. If the members of
a collection are `Promise` objects, then you can make the framework wait for all members to
become ready as shown in the following snippet. This will make the asynchronous method wait
on each member of the collection to become available.

```
@Asynchronous
public void printList(@Wait List<Promise<String>> list) {
  for (Promise<String> s: list) {
      activityClient.printActivity(s);
  }
}
```

Note that the `@Wait` annotation must be used on the parameter to indicate
that it contains `Promise` objects.

Note also that the activity `printActivity` takes a
`String` argument but the matching method in the generated
client takes a Promise<String>. We are calling the method on the
client and not invoking the activity method directly.

## Settable<T>

`Settable<`T`>` is a derived type of
`Promise<T>` that provides a set method that allows you to manually set the
value of a `Promise`. For example, the following workflow waits for a signal to
be received by waiting on a `Settable<?>`, which is set in the signal
method:

```
public class MyWorkflowImpl implements MyWorkflow{
   final Settable<String> result = new Settable<String>();

   //@Execute method
   @Override
   public Promise<String> start() {
      return done(result);
   }

   //Signal
   @Override
   public void manualProcessCompletedSignal(String data) {
      result.set(data);
   }

   @Asynchronous
   public Promise<String> done(Settable<String> result){
       return result;
   }
}
```

A `Settable<?>` can also be chained to another promise at a time. You can
use `AndPromise` and `OrPromise` to group promises. You can unchain a
chained `Settable` by calling the `unchain()` method on it. When
chained, the `Settable<?>` automatically becomes ready when the promise that it
is chained to becomes ready. Chaining is especially useful when you want to use a promise
returned from within the scope of a `doTry()` in other parts of your program.
Because `TryCatchFinally` is used as a nested class, you can't declare a
`Promise<>` in the parent's scope and set it in `doTry()`. This
is because Java requires variables to be declared in parent scope and used in nested classes
to be marked final. For example:

```
@Asynchronous
public Promise<String> chain(final Promise<String> input) {
    final Settable<String> result = new Settable<String>();

    new TryFinally() {

        @Override
        protected void doTry() throws Throwable {
            Promise<String> resultToChain = activity1(input);
            activity2(resultToChain);

            // Chain the promise to Settable
            result.chain(resultToChain);
        }

        @Override
        protected void doFinally() throws Throwable {
            if (result.isReady()) { // Was a result returned before the exception?
                // Do cleanup here
            }
        }
    };

    return result;
}
```

A `Settable` can be chained to one promise at a time. You can unchain a
chained `Settable` by calling the `unchain()` method on it.

## @NoWait

When you pass a `Promise` to an asynchronous method, by default, the framework will wait for the
`Promise`(s) to become ready before executing the method (except for collection types). You may
override this behavior by using the `@NoWait` annotation on parameters in the declaration of the
asynchronous method. This is useful if you are passing in `Settable<T>`, which will be set by the
asynchronous method itself.

## Promise<Void>

Dependencies in asynchronous methods are implemented by passing the `Promise`
returned by one method as an argument to another. However, there may be cases where you want
to return `void` from a method, but still want other asynchronous methods to
execute after its completion. In such cases, you can use `Promise<Void>` as
the return type of the method. The `Promise` class provides a static
`Void` method that you can use to create a `Promise<Void>`
object. This `Promise` will become ready when the asynchronous method finishes
execution. You can pass this `Promise` to another asynchronous method just like
any other `Promise` object. If you are using `Settable<Void>`, then
call the set method on it with null to make it ready.

## AndPromise and OrPromise

`AndPromise` and `OrPromise` allow you to group multiple `Promise<>`
objects into a single logical promise. An `AndPromise` becomes ready when all promises used to
construct it become ready. An `OrPromise` becomes ready when any promise in the collection of promises
used to construct it becomes ready. You can call `getValues()` on `AndPromise` and
`OrPromise` to retrieve the list of values of the constituent promises.
