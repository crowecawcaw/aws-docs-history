

# Use async and await

CloudFront Functions JavaScript runtime functions 2.0 provide `async` and `await` syntax to handle `Promise` objects. Promises represent delayed results that can be accessed by using the `await` keyword in functions marked as `async`.

For more information about `Promise` objects, see [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

**Note**  
You must use JavaScript runtime 2.0 for the following code samples.  
`await` can be used inside `async` functions only. `async` arguments and closures are not supported.

```js
async function answer() {
    return 42;
}

// Note: async, await can be used only inside an async function. async arguments and closures are not supported.

async function handler(event) {
    // var answer_value = answer(); // returns Promise, not a 42 value
    let answer_value = await answer(); // resolves Promise, 42
    console.log("Answer"+answer_value);
    event.request.headers['answer'] = { value : ""+answer_value };
    return event.request;
}
```

The following example JavaScript code shows how to view promises with the `then` chain method. You can use `catch` to view errors.

**Warning**  
Using promise combinators (for example, `Promise.all` and `Promise.any`) and promise chain methods (for example, `then` and `catch`) can require high function memory usage. If your function exceeds the [maximum function memory](cloudfront-limits.md#limits-functions) quota, it will fail to execute. To avoid this error, we recommend that you use the `await` syntax instead of `promise` methods.  
You also can't use promise combinators to make more than one network call. A function can make only one network call per invocation. Calling `Promise.all()` with more than one network call throws an error. For more information, see [Helper methods for network calls](helper-functions-network-calls.md).

```js
async function answer() {
    return 42;
}

async function squared_answer() {
   return answer().then(value => value * value)
} 
// Note: async, await can be used only inside an async function. async arguments and closures are not supported.
async function handler(event) {
    // var answer_value = answer(); // returns Promise, not a 42 value
    let answer_value = await squared_answer(); // resolves Promise, 42
    console.log("Answer"+answer_value);
    event.request.headers['answer'] = { value : ""+answer_value };
    return event.request;
}
```