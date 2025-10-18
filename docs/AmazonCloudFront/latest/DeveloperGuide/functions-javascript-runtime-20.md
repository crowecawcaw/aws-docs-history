# JavaScript runtime 2.0 features for
 CloudFront Functions

The CloudFront Functions JavaScript runtime environment is compliant with [ECMAScript (ES) version
 5.1](https://262.ecma-international.org/5.1/ "https://262.ecma-international.org/5.1/") and also supports some features of ES versions 6 through 12. It also
 provides some nonstandard methods that are not part of the ES specifications. The following
 topics list all supported features in this runtime.

###### Topics

* [Core features](#writing-functions-javascript-features-core-20 "#writing-functions-javascript-features-core-20")
* [Primitive
 objects](#writing-functions-javascript-features-primitive-objects-20 "#writing-functions-javascript-features-primitive-objects-20")
* [Built-in
 objects](#writing-functions-javascript-features-builtin-objects-20 "#writing-functions-javascript-features-builtin-objects-20")
* [Error types](#writing-functions-javascript-features-error-types-20 "#writing-functions-javascript-features-error-types-20")
* [Globals](#writing-functions-javascript-features-globals-20 "#writing-functions-javascript-features-globals-20")
* [Built-in
 modules](#writing-functions-javascript-features-builtin-modules-20 "#writing-functions-javascript-features-builtin-modules-20")
* [Restricted
 features](#writing-functions-javascript-features-restricted-features-20 "#writing-functions-javascript-features-restricted-features-20")

## Core features


The following core features of ES are supported.




**Types**

All ES 5.1 types are supported. This includes boolean values, numbers,
 strings, objects, arrays, functions, and regular expressions.



**Operators**

All ES 5.1 operators are supported.


The ES 7 exponentiation operator (`**`) is supported.



**Statements**

The following ES 5.1 statements are supported:



* `break`
* `catch`
* `continue`
* `do-while`
* `else`
* `finally`
* `for`
* `for-in`
* `if`
* `label`
* `return`
* `switch`
* `throw`
* `try`
* `var`
* `while`

The following ES 6 statements are supported:



* `const`
* `let`

The following ES 8 statements are supported:



* `async`
* `await`

###### Note

`async`, `await`, `const`,
 and `let` are supported in JavaScript runtime 2.0.

`await` can be used inside `async` functions only. `async` arguments and closures are not supported.



**Literals**

ES 6 template literals are supported: multiline strings, expression
 interpolation, and nesting templates.



**Functions**

All ES 5.1 function features are supported.


ES 6 arrow functions are supported, and ES 6 rest parameter syntax is
 supported.



**Unicode**

Source text and string literals can contain Unicode-encoded characters.
 Unicode code point escape sequences of six characters (for example,
 `\uXXXX`) are also supported.



**Strict mode**

Functions operate in strict mode by default, so you don’t need to add a
 `use strict` statement in your function code. This cannot be
 changed.




## Primitive
 objects


The following primitive objects of ES are supported.




**Object**

The following ES 5.1 methods on objects are supported:



* `Object.create()` (without properties list)
* `Object.defineProperties()`
* `Object.defineProperty()`
* `Object.freeze()`
* `Object.getOwnPropertyDescriptor()`
* `Object.getOwnPropertyDescriptors()`
* `Object.getOwnPropertyNames()`
* `Object.getPrototypeOf()`
* `Object.isExtensible()`
* `Object.isFrozen()`
* `Object.isSealed()`
* `Object.keys()`
* `Object.preventExtensions()`
* `Object.seal()`

The following ES 6 methods on objects are supported:



* `Object.assign()`

The following ES 8 methods on objects are supported:



* `Object.entries()`
* `Object.values()`

The following ES 5.1 prototype methods on objects are supported:



* `Object.prototype.hasOwnProperty()`
* `Object.prototype.isPrototypeOf()`
* `Object.prototype.propertyIsEnumerable()`
* `Object.prototype.toString()`
* `Object.prototype.valueOf()`

The following ES 6 prototype methods on objects are supported:



* `Object.prototype.is()`
* `Object.prototype.setPrototypeOf()`


**String**

The following ES 5.1 methods on strings are supported:



* `String.fromCharCode()`

The following ES 6 methods on strings are supported:



* `String.fromCodePoint()`

The following ES 5.1 prototype methods on strings are supported:



* `String.prototype.charAt()`
* `String.prototype.concat()`
* `String.prototype.indexOf()`
* `String.prototype.lastIndexOf()`
* `String.prototype.match()`
* `String.prototype.replace()`
* `String.prototype.search()`
* `String.prototype.slice()`
* `String.prototype.split()`
* `String.prototype.substr()`
* `String.prototype.substring()`
* `String.prototype.toLowerCase()`
* `String.prototype.trim()`
* `String.prototype.toUpperCase()`

The following ES 6 prototype methods on strings are supported:



* `String.prototype.codePointAt()`
* `String.prototype.endsWith()`
* `String.prototype.includes()`
* `String.prototype.repeat()`
* `String.prototype.startsWith()`

The following ES 8 prototype methods on strings are supported:



* `String.prototype.padStart()`
* `String.prototype.padEnd()`

The following ES 9 prototype methods on strings are supported:



* `String.prototype.trimStart()`
* `String.prototype.trimEnd()`

The following ES 12 prototype methods on strings are supported:



* `String.prototype.replaceAll()`


###### Note

`String.prototype.replaceAll()` is new in
 JavaScript runtime 2.0.


**Number**

ALL ES 5 numbers are supported.


The following ES 6 properties on numbers are supported:



* `Number.EPSILON`
* `Number.MAX_SAFE_INTEGER`
* `Number.MIN_SAFE_INTEGER`
* `Number.MAX_VALUE`
* `Number.MIN_VALUE`
* `Number.NaN`
* `Number.NEGATIVE_INFINITY`
* `Number.POSITIVE_INFINITY`

The following ES 6 methods on numbers are supported:



* `Number.isFinite()`
* `Number.isInteger()`
* `Number.isNaN()`
* `Number.isSafeInteger()`
* `Number.parseInt()`
* `Number.parseFloat()`

The following ES 5.1 prototype methods on numbers are supported:



* `Number.prototype.toExponential()`
* `Number.prototype.toFixed()`
* `Number.prototype.toPrecision()`

ES 12 numeric separators are supported.


###### Note

ES 12 numeric separators are new in JavaScript runtime 2.0.




## Built-in
 objects


The following built-in objects of ES are supported.




**Math**

All ES 5.1 math methods are supported.


###### Note

In the CloudFront Functions runtime environment, the
 `Math.random()` implementation uses OpenBSD
 `arc4random` seeded with the timestamp of when the
 function runs.


The following ES 6 math properties are supported:



* `Math.E`
* `Math.LN10`
* `Math.LN2`
* `Math.LOG10E`
* `Math.LOG2E`
* `Math.PI`
* `Math.SQRT1_2`
* `Math.SQRT2`

The following ES 6 math methods are supported:



* `Math.abs()`
* `Math.acos()`
* `Math.acosh()`
* `Math.asin()`
* `Math.asinh()`
* `Math.atan()`
* `Math.atan2()`
* `Math.atanh()`
* `Math.cbrt()`
* `Math.ceil()`
* `Math.clz32()`
* `Math.cos()`
* `Math.cosh()`
* `Math.exp()`
* `Math.expm1()`
* `Math.floor()`
* `Math.fround()`
* `Math.hypot()`
* `Math.imul()`
* `Math.log()`
* `Math.log1p()`
* `Math.log2()`
* `Math.log10()`
* `Math.max()`
* `Math.min()`
* `Math.pow()`
* `Math.random()`
* `Math.round()`
* `Math.sign()`
* `Math.sinh()`
* `Math.sin()`
* `Math.sqrt()`
* `Math.tan()`
* `Math.tanh()`
* `Math.trunc()`


**Date**

All ES 5.1 `Date` features are supported.


###### Note

For security reasons, `Date` always returns the same
 value—the function’s start time—during the lifetime of a
 single function run. For more information, see [Restricted
 features](functions-javascript-runtime-10.md#writing-functions-javascript-features-restricted-features "functions-javascript-runtime-10.md#writing-functions-javascript-features-restricted-features").



**Function**

The following ES 5.1 prototype methods are supported:



* `Function.prototype.apply()`
* `Function.prototype.bind()`
* `Function.prototype.call()`

Function constructors are not supported.



**Regular expressions**

All ES 5.1 regular expression features are supported. The regular
 expression language is Perl compatible.


The following ES 5.1 prototype accessor properties are supported:



* `RegExp.prototype.global`
* `RegExp.prototype.ignoreCase`
* `RegExp.protoype.multiline`
* `RegExp.protoype.source`
* `RegExp.prototype.sticky`
* `RegExp.prototype.flags`


###### Note

`RegExp.prototype.sticky` and
 `RegExp.prototype.flags` are new in JavaScript
 runtime 2.0.

The following ES 5.1 prototype methods are supported:



* `RegExp.prototype.exec()`
* `RegExp.prototype.test()`
* `RegExp.prototype.toString()`
* `RegExp.prototype[@@replace]()`
* `RegExp.prototype[@@split]()`


###### Note

`RegExp.prototype[@@split]()` is new in JavaScript
 runtime 2.0.

The following ES 5.1 instance properties are supported:



* `lastIndex`

ES 9 named capture groups are supported.



**JSON**

The following ES 5.1 methods are supported:



* `JSON.parse()`
* `JSON.stringify()`


**Array**

The following ES 5.1 methods on arrays are supported:



* `Array.isArray()`

The following ES 6 methods on arrays are supported:



* `Array.of()`

The following ES 5.1 prototype methods are supported:



* `Array.prototype.concat()`
* `Array.prototype.every()`
* `Array.prototype.filter()`
* `Array.prototype.forEach()`
* `Array.prototype.indexOf()`
* `Array.prototype.join()`
* `Array.prototype.lastIndexOf()`
* `Array.prototype.map()`
* `Array.prototype.pop()`
* `Array.prototype.push()`
* `Array.prototype.reduce()`
* `Array.prototype.reduceRight()`
* `Array.prototype.reverse()`
* `Array.prototype.shift()`
* `Array.prototype.slice()`
* `Array.prototype.some()`
* `Array.prototype.sort()`
* `Array.prototype.splice()`
* `Array.prototype.unshift()`

The following ES 6 prototype methods are supported



* `Array.prototype.copyWithin()`
* `Array.prototype.fill()`
* `Array.prototype.find()`
* `Array.prototype.findIndex()`

The following ES 7 prototype methods are supported:



* `Array.prototype.includes()`


**Typed arrays**

The following ES 6 typed array constructors are supported:



* `Float32Array`
* `Float64Array`
* `Int8Array`
* `Int16Array`
* `Int32Array`
* `Uint8Array`
* `Uint8ClampedArray`
* `Uint16Array`
* `Uint32Array`

The following ES 6 methods are supported:



* `TypedArray.from()`
* `TypedArray.of()`


###### Note

`TypedArray.from()` and
 `TypedArray.of()` are new in JavaScript runtime
 2.0.

The following ES 6 prototype methods are supported:



* `TypedArray.prototype.copyWithin()`
* `TypedArray.prototype.every()`
* `TypedArray.prototype.fill()`
* `TypedArray.prototype.filter()`
* `TypedArray.prototype.find()`
* `TypedArray.prototype.findIndex()`
* `TypedArray.prototype.forEach()`
* `TypedArray.prototype.includes()`
* `TypedArray.prototype.indexOf()`
* `TypedArray.prototype.join()`
* `TypedArray.prototype.lastIndexOf()`
* `TypedArray.prototype.map()`
* `TypedArray.prototype.reduce()`
* `TypedArray.prototype.reduceRight()`
* `TypedArray.prototype.reverse()`
* `TypedArray.prototype.some()`
* `TypedArray.prototype.set()`
* `TypedArray.prototype.slice()`
* `TypedArray.prototype.sort()`
* `TypedArray.prototype.subarray()`
* `TypedArray.prototype.toString()`


###### Note

`TypedArray.prototype.every()`,
 `TypedArray.prototype.fill()`,
 `TypedArray.prototype.filter()`,
 `TypedArray.prototype.find()`,
 `TypedArray.prototype.findIndex()`,
 `TypedArray.prototype.forEach()`,
 `TypedArray.prototype.includes()`,
 `TypedArray.prototype.indexOf()`,
 `TypedArray.prototype.join()`,
 `TypedArray.prototype.lastIndexOf()`,`TypedArray.prototype.map()`,
 `TypedArray.prototype.reduce()`,
 `TypedArray.prototype.reduceRight()`,
 `TypedArray.prototype.reverse()`, and
 `TypedArray.prototype.some()` are new in
 JavaScript runtime 2.0.


**ArrayBuffer**

The following ES 6 methods on ArrayBuffer are supported:



* `isView()`

The following ES 6 prototype methods on ArrayBuffer are supported:



* `ArrayBuffer.prototype.slice()`


**Promise**

The following ES 6 methods on promises are supported:



* `Promise.all()`
* `Promise.allSettled()`
* `Promise.any()`
* `Promise.reject()`
* `Promise.resolve()`
* `Promise.race()`


###### Note

`Promise.all()`, `Promise.allSettled()`,
 `Promise.any()`, and `Promise.race()`
 are new in JavaScript runtime 2.0.

The following ES 6 prototype methods on promises are supported:



* `Promise.prototype.catch()`
* `Promise.prototype.finally()`
* `Promise.prototype.then()`


**DataView**

The following ES 6 prototype methods are supported:



* `DataView.prototype.getFloat32()`
* `DataView.prototype.getFloat64()`
* `DataView.prototype.getInt16()`
* `DataView.prototype.getInt32()`
* `DataView.prototype.getInt8()`
* `DataView.prototype.getUint16()`
* `DataView.prototype.getUint32()`
* `DataView.prototype.getUint8()`
* `DataView.prototype.setFloat32()`
* `DataView.prototype.setFloat64()`
* `DataView.prototype.setInt16()`
* `DataView.prototype.setInt32()`
* `DataView.prototype.setInt8()`
* `DataView.prototype.setUint16()`
* `DataView.prototype.setUint32()`
* `DataView.prototype.setUint8()`


###### Note

All Dataview ES 6 prototype methods are new in JavaScript
 runtime 2.0.


**Symbol**

The following ES 6 methods are supported:



* `Symbol.for()`
* `Symbol.keyfor()`


###### Note

All Symbol ES 6 methods are new in JavaScript runtime
 2.0.


**Text Decoder**

The following prototype methods are supported:



* `TextDecoder.prototype.decode()`

The following prototype accessor properties are supported:



* `TextDecoder.prototype.encoding`
* `TextDecoder.prototype.fatal`
* `TextDecoder.prototype.ignoreBOM`


**Text Encoder**

The following prototype methods are supported:



* `TextEncoder.prototype.encode()`
* `TextEncoder.prototype.encodeInto()`



## Error types


The following error objects are supported:



* `Error`
* `EvalError`
* `InternalError`
* `RangeError`
* `ReferenceError`
* `SyntaxError`
* `TypeError`
* `URIError`

## Globals


The `globalThis` object is supported.


The following ES 5.1 global functions are supported:



* `decodeURI()`
* `decodeURIComponent()`
* `encodeURI()`
* `encodeURIComponent()`
* `isFinite()`
* `isNaN()`
* `parseFloat()`
* `parseInt()`

The following ES 6 global functions are supported:



* `atob()`
* `btoa()`


###### Note

`atob()` and `btoa()` are new in JavaScript runtime
 2.0.

The following global constants are supported:



* `NaN`
* `Infinity`
* `undefined`
* `arguments`

## Built-in
 modules


The following built-in modules are supported.


###### Modules

* [Buffer](#writing-functions-javascript-features-builtin-modules-buffer-20 "#writing-functions-javascript-features-builtin-modules-buffer-20")
* [Query string](#writing-functions-javascript-features-builtin-modules-query-string-20 "#writing-functions-javascript-features-builtin-modules-query-string-20")
* [Crypto](#writing-functions-javascript-features-builtin-modules-crypto-20 "#writing-functions-javascript-features-builtin-modules-crypto-20")

### Buffer


The module provides the following methods:



* `Buffer.alloc(size[, fill[, encoding]])`


Allocate a `Buffer`.




	+ `size`: Buffer size. Enter an integer.
	+ `fill`: Optional. Enter a string, `Buffer`,
	 Uint8Array, or integer. Default is `0`.
	+ `encoding`: Optional. When `fill` is a
	 string, enter one of the following: `utf8`,
	 `hex`, `base64`, `base64url`.
	 Default is `utf8`.
* `Buffer.allocUnsafe(size)`


Allocate a non-initialized `Buffer`.




	+ `size`: Enter an integer.
* `Buffer.byteLength(value[, encoding])`


Return the length of a value, in bytes.




	+ `value`: A string, `Buffer`, TypedArray,
	 Dataview, or Arraybuffer.
	+ `encoding`: Optional. When `value` is a
	 string, enter one of the following: `utf8`,
	 `hex`, `base64`, `base64url`.
	 Default is `utf8`.
* `Buffer.compare(buffer1, buffer2)`


Compare two `Buffer`s to help sort arrays. Returns
 `0` if they're the same, `-1` if
 `buffer1` comes first, or `1` if
 `buffer2` comes first.




	+ `buffer1`: Enter a `Buffer`.
	+ `buffer2`: Enter a different
	 `Buffer`.
* `Buffer.concat(list[, totalLength])`


Concatenate multiple `Buffer`s. Returns `0` if none.
 Returns up to `totalLength`.




	+ `list`: Enter a list of `Buffer`s. Note this
	 will be truncated to `totalLength`.
	+ `totalLength`: Optional. Enter an unsigned integer. Use
	 sum of `Buffer` instances in list if blank.
* `Buffer.from(array)`


Create a `Buffer` from an array.




	+ `array`: Enter a byte array from `0` to
	 `255`.
* `Buffer.from(arrayBuffer, byteOffset[, length]))`


Create a view from `arrayBuffer`, starting at offset
 `byteOffset` with length `length`.




	+ `arrayBuffer`: Enter a `Buffer`
	 array.
	+ `byteOffset`: Enter an integer.
	+ `length`: Optional. Enter an integer.
* `Buffer.from(buffer)`


Create a copy of the `Buffer`.




	+ `buffer`: Enter a `Buffer`.
* `Buffer.from(object[, offsetOrEncoding[, length]])`


Create a `Buffer` from an object. Returns
 `Buffer.from(object.valueOf(), offsetOrEncoding, length)` if
 `valueOf()` is not equal to the object.




	+ `object`: Enter an object.
	+ `offsetOrEncoding`: Optional. Enter an integer or
	 encoding string.
	+ `length`: Optional. Enter an integer.
* `Buffer.from(string[, encoding])`


Create a `Buffer` from a string.




	+ `string`: Enter a string.
	+ `encoding`: Optional. Enter one of the following:
	 `utf8`, `hex`, `base64`,
	 `base64url`. Default is `utf8`.
* `Buffer.isBuffer(object)`


Check if `object` is a Buffer. Returns `true` or
 `false`.




	+ `object`: Enter an object.
* `Buffer.isEncoding(encoding)`


Check if `encoding` is supported. Returns `true` or
 `false`.




	+ `encoding`: Optional. Enter one of the following:
	 `utf8`, `hex`, `base64`,
	 `base64url`. Default is `utf8`.

The module provides the following buffer prototype methods:



* `Buffer.prototype.compare(target[, targetStart[, targetEnd[,
 sourceStart[, sourceEnd]]]])`


Compare `Buffer` with target. Returns `0` if they're
 the same, `1` if `buffer` comes first, or
 `-1` if `target` comes first.




	+ `target`: Enter a `Buffer`.
	+ `targetStart`: Optional. Enter an integer. Default is
	 0.
	+ `targetEnd`: Optional. Enter an integer. Default is
	 `target` length.
	+ `sourceStart`: Optional. Enter an integer. Default is
	 0.
	+ `sourceEnd`: Optional. Enter an integer. Default is
	 `Buffer` length.
* `Buffer.prototype.copy(target[, targetStart[, sourceStart[,
 sourceEnd]]])`


Copy buffer to `target`.




	+ `target`: Enter a `Buffer` or
	 `Uint8Array`.
	+ `targetStart`: Optional. Enter an integer. Default is
	 0.
	+ `sourceStart`: Optional. Enter an integer. Default is
	 0.
	+ `sourceEnd`: Optional. Enter an integer. Default is
	 `Buffer` length.
* `Buffer.prototype.equals(otherBuffer)`


Compare `Buffer` to `otherBuffer`. Returns
 `true` or `false`.




	+ `otherBuffer`: Enter a string.
* `Buffer.prototype.fill(value[, offset[, end][,
 encoding])`


Fill `Buffer` with `value`.




	+ `value`: Enter a string, `Buffer`, or
	 integer.
	+ `offset`: Optional. Enter an integer.
	+ `end`: Optional. Enter an integer.
	+ `encoding`: Optional. Enter one of the following:
	 `utf8`, `hex`, `base64`,
	 `base64url`. Default is `utf8`.
* `Buffer.prototype.includes(value[, byteOffset][,
 encoding])`


Search for `value` in `Buffer`. Returns
 `true` or `false`.




	+ `value`: Enter a string, `Buffer`,
	 `Uint8Array`, or integer.
	+ `byteOffset`: Optional. Enter an integer.
	+ `encoding`: Optional. Enter one of the following:
	 `utf8`, `hex`, `base64`,
	 `base64url`. Default is `utf8`.
* `Buffer.prototype.indexOf(value[, byteOffset][,
 encoding])`


Search for first `value` in `Buffer`. Returns
 `index` if found; returns `-1` if not
 found.




	+ `value`: Enter a string, `Buffer`,
	 Unit8Array, or integer from 0 to 255.
	+ `byteOffset`: Optional. Enter an integer.
	+ `encoding`: Optional. Enter one of the following if
	 `value` is a string: `utf8`,
	 `hex`, `base64`, `base64url`.
	 Default is `utf8`.
* `Buffer.prototype.lastIndexOf(value[, byteOffset][,
 encoding])`


Search for last `value` in `Buffer`. Returns
 `index` if found; returns `-1` if not
 found.




	+ `value`: Enter a string, `Buffer`,
	 Unit8Array, or integer from 0 to 255.
	+ `byteOffset`: Optional. Enter an integer.
	+ `encoding`: Optional. Enter one of the following if
	 `value` is a string: `utf8`,
	 `hex`, `base64`, `base64url`.
	 Default is `utf8`.
* `Buffer.prototype.readInt8(offset)`


Read `Int8` at `offset` from
 `Buffer`.




	+ `offset`: Enter an integer.
* `Buffer.prototype.readIntBE(offset, byteLength)`


Read `Int` as big-endian at `offset` from
 `Buffer`.




	+ `offset`: Enter an integer.
	+ `byteLength`: Optional. Enter an integer from
	 `1` to `6`.
* `Buffer.prototype.readInt16BE(offset)`


Read `Int16` as big-endian at `offset` from
 `Buffer`.




	+ `offset`: Enter an integer.
* `Buffer.prototype.readInt32BE(offset)`


Read `Int32` as big-endian at `offset` from
 `Buffer`.




	+ `offset`: Enter an integer.
* `Buffer.prototype.readIntLE(offset, byteLength)`


Read `Int` as little-endian at `offset` from
 `Buffer`.




	+ `offset`: Enter an integer.
	+ `byteLength`: Enter an integer from `1` to
	 `6`.
* `Buffer.prototype.readInt16LE(offset)`


Read `Int16` as little-endian at `offset` from
 `Buffer`.




	+ `offset`: Enter an integer.
* `Buffer.prototype.readInt32LE(offset)`


Read `Int32` as little-endian at `offset` from
 `Buffer`.




	+ `offset`: Enter an integer.
* `Buffer.prototype.readUInt8(offset)`


Read `UInt8` at `offset` from
 `Buffer`.




	+ `offset`: Enter an integer.
* `Buffer.prototype.readUIntBE(offset, byteLength)`


Read `UInt` as big-endian at `offset` from
 `Buffer`.




	+ `offset`: Enter an integer.
	+ `byteLength`: Enter an integer from `1` to
	 `6`.
* `Buffer.prototype.readUInt16BE(offset)`


Read `UInt16` as big-endian at `offset` from
 `Buffer`.
* + `offset`: Enter an integer.
* `Buffer.prototype.readUInt32BE(offset)`


Read `UInt32` as big-endian at `offset` from
 `Buffer`.




	+ `offset`: Enter an integer.
* `Buffer.prototype.readUIntLE(offset, byteLength)`


Read `UInt` as little-endian at `offset` from
 `Buffer`.




	+ `offset`: Enter an integer.
	+ `byteLength`: Enter an integer from `1` to
	 `6`.
* `Buffer.prototype.readUInt16LE(offset)`


Read `UInt16` as little-endian at `offset` from
 `Buffer`.




	+ `offset`: Enter an integer.
* `Buffer.prototype.readUInt32LE(offset)`


Read `UInt32` as little-endian at `offset` from
 `Buffer`.




	+ `offset`: Enter an integer.
* `Buffer.prototype.readDoubleBE([offset])`


Read a 64-bit double as big-endian at `offset` from
 `Buffer`.




	+ `offset`: Optional. Enter an integer.
* `Buffer.prototype.readDoubleLE([offset])`


Read a 64-bit double as little-endian at `offset` from
 `Buffer`.




	+ `offset`: Optional. Enter an integer.
* `Buffer.prototype.readFloatBE([offset])`


Read a 32-bit float as big-endian at `offset` from
 `Buffer`.




	+ `offset`: Optional. Enter an integer.
* `Buffer.prototype.readFloatLE([offset])`


Read a 32-bit float as little-endian at `offset` from
 `Buffer`.




	+ `offset`: Optional. Enter an integer.
* `Buffer.prototype.subarray([start[, end]])`


Returns a copy of `Buffer` that is offset and cropped with a
 new `start` and `end`.




	+ `start`: Optional. Enter an integer. Default is
	 0.
	+ `end`: Optional. Enter an integer. Default is buffer
	 length.
* `Buffer.prototype.swap16()`


Swap the `Buffer` array byte order, treating it as an array of
 16-bit numbers. `Buffer` length must be divisible by 2, or you
 will receive an error.
* `Buffer.prototype.swap32()`


Swap the `Buffer` array byte order, treating it as an array of
 32-bit numbers . `Buffer` length must be divisible by 4, or you
 will receive an error.
* `Buffer.prototype.swap64()`


Swap the `Buffer` array byte order, treating it as an array of
 64-bit numbers. `Buffer` length must be divisible by 8, or you
 will receive an error.
* `Buffer.prototype.toJSON()`


Returns `Buffer` as a JSON.
* `Buffer.prototype.toString([encoding[, start[, end]]])`


Convert `Buffer`, from `start` to `end`,
 to encoded string.




	+ `encoding`: Optional. Enter one of the following:
	 `utf8`, `hex`, `base64`, or
	 `base64url`. Default is `utf8`.
	+ `start`: Optional. Enter an integer. Default is
	 0.
	+ `end`: Optional. Enter an integer. Default is buffer
	 length.
* `Buffer.prototype.write(string[, offset[, length]][,
 encoding])`


Write encoded `string` to `Buffer` if there is
 space, or a truncated `string` if there is not enough
 space.




	+ `string`: Enter a string.
	+ `offset`: Optional. Enter an integer. Default is
	 0.
	+ `length`: Optional. Enter an integer. Default is the
	 length of the string.
	+ `encoding`: Optional. Optionally enter one of the
	 following: `utf8`, `hex`, `base64`,
	 or `base64url`. Default is `utf8`.
* `Buffer.prototype.writeInt8(value, offset, byteLength)`


Write `Int8`
`value` of `byteLength` at `offset` to
 `Buffer`.




	+ `value`: Enter an integer.
	+ `offset`: Enter an integer
	+ `byteLength`: Enter an integer from `1` to
	 `6`.
* `Buffer.prototype.writeIntBE(value, offset, byteLength)`


Write `value` at `offset` to
 `Buffer`, using big-endian.




	+ `value`: Enter an integer.
	+ `offset`: Enter an integer
	+ `byteLength`: Enter an integer from `1` to
	 `6`.
* `Buffer.prototype.writeInt16BE(value, offset,
 byteLength)`


Write `value` at `offset` to
 `Buffer`, using big-endian.




	+ `value`: Enter an integer.
	+ `offset`: Enter an integer
	+ `byteLength`: Enter an integer from `1` to
	 `6`.
* `Buffer.prototype.writeInt32BE(value, offset,
 byteLength)`


Write `value` at `offset` to
 `Buffer`, using big-endian.




	+ `value`: Enter an integer.
	+ `offset`: Enter an integer
	+ `byteLength`: Enter an integer from `1` to
	 `6`.
* `Buffer.prototype.writeIntLE(offset, byteLength)`


Write `value` at `offset` to
 `Buffer`, using little-endian.




	+ `offset`: Enter an integer.
	+ `byteLength`: Enter an integer from `1` to
	 `6`.
* `Buffer.prototype.writeInt16LE(offset, byteLength)`


Write `value` at `offset` to
 `Buffer`, using little-endian.




	+ `offset`: Enter an integer.
	+ `byteLength`: Enter an integer from `1` to
	 `6`.
* `Buffer.prototype.writeInt32LE(offset, byteLength)`


Write `value` at `offset` to
 `Buffer`, using little-endian.




	+ `offset`: Enter an integer.
	+ `byteLength`: Enter an integer from `1` to
	 `6`.
* `Buffer.prototype.writeUInt8(value, offset, byteLength)`


Write `UInt8`
`value` of `byteLength` at `offset` to
 `Buffer`.




	+ `value`: Enter an integer.
	+ `offset`: Enter an integer
	+ `byteLength`: Enter an integer from `1` to
	 `6`.
* `Buffer.prototype.writeUIntBE(value, offset,
 byteLength)`


Write `value` at `offset` to `Buffer`, using big-endian.




	+ `value`: Enter an integer.
	+ `offset`: Enter an integer
	+ `byteLength`: Enter an integer from `1` to
	 `6`.
* `Buffer.prototype.writeUInt16BE(value, offset,
 byteLength)`


Write `value` at `offset` to `Buffer`, using big-endian.




	+ `value`: Enter an integer.
	+ `offset`: Enter an integer
	+ `byteLength`: Enter an integer from `1` to
	 `6`.
* `Buffer.prototype.writeUInt32BE(value, offset,
 byteLength)`


Write `value` at `offset` to `Buffer`, using big-endian.




	+ `value`: Enter an integer.
	+ `offset`: Enter an integer
	+ `byteLength`: Enter an integer from `1` to
	 `6`.
* `Buffer.prototype.writeUIntLE(value, offset,
 byteLength)`


Write `value` at `offset` to `Buffer`, using little-endian.




	+ `value`: Enter an integer.
	+ `offset`: Enter an integer
	+ `byteLength`: Enter an integer from `1` to
	 `6`.
* `Buffer.prototype.writeUInt16LE(value, offset,
 byteLength)`


Write `value` at `offset` to `Buffer`, using little-endian.




	+ `value`: Enter an integer.
	+ `offset`: Enter an integer
	+ `byteLength`: Enter an integer from `1` to
	 `6`.
* `Buffer.prototype.writeUInt32LE(value, offset,
 byteLength)`


Write `value` at `offset` to `Buffer`, using little-endian.




	+ `value`: Enter an integer.
	+ `offset`: Enter an integer
	+ `byteLength`: Enter an integer from `1` to
	 `6`.
* `Buffer.prototype.writeDoubleBE(value, [offset])`


Write `value` at `offset` to `Buffer`, using big-endian.




	+ `value`: Enter an integer.
	+ `offset`: Optional. Enter an integer. Default is
	 0.
* `Buffer.prototype.writeDoubleLE(value, [offset])`


Write `value` at `offset` to `Buffer`, using little-endian.




	+ `value`: Enter an integer.
	+ `offset`: Optional. Enter an integer. Default is
	 0.
* `Buffer.prototype.writeFloatBE(value, [offset])`


Write `value` at `offset` to `Buffer`, using big-endian.




	+ `value`: Enter an integer.
	+ `offset`: Optional. Enter an integer. Default is
	 0.
* `Buffer.prototype.writeFloatLE(value, [offset])`


Write `value` at `offset` to `Buffer`, using little-endian.




	+ `value`: Enter an integer.
	+ `offset`: Optional. Enter an integer. Default is
	 0.

The following instance methods are supported:



* `buffer[index]`


Get and set octet (byte) at `index` in `Buffer`. 




	+ Get a number from `0` to `255`. Or set a
	 number from from `0` to `255`.

The following instance properties are supported:



* `buffer`


Get the `ArrayBuffer` object for the buffer.
* `byteOffset`


Get the `byteOffset` of the buffer's `Arraybuffer`
 object.
* `length`


Get the buffer byte count.

###### Note

All Buffer module methods are new in JavaScript runtime 2.0.


### Query string


###### Note

The [CloudFront Functions event
 object](functions-event-structure.md "functions-event-structure.md") automatically parses URL query strings for you. That means
 that in most cases you don’t need to use this module.


The query string module (`querystring`) provides methods for parsing
 and formatting URL query strings. You can load the module using
 `require('querystring')`. The module provides the following
 methods.




`querystring.escape(*string*)`

URL-encodes the given `string`, returning an escaped query
 string. The method is used by `querystring.stringify()` and
 should not be used directly.



`querystring.parse(*string*[,
 *separator*[, *equal*[, *options*]]])`

Parses a query string (`string`) and returns an
 object.


The `separator` parameter is a substring for delimiting key
 and value pairs in the query string. By default it is
 `&`.


The `equal` parameter is a substring for delimiting keys
 and values in the query string. By default it is `=`.


The `options` parameter is an object with the following
 keys:




`decodeURIComponent *function*`

A function to decode percent-encoded characters in the
 query string. By default it is
 `querystring.unescape()`.



`maxKeys *number*`

The maximum number of keys to parse. By default it is
 `1000`. Use a value of `0` to
 remove the limitations for counting keys.




By default, percent-encoded characters within the query string are
 assumed to use the UTF-8 encoding. Invalid UTF-8 sequences are replaced
 with the `U+FFFD` replacement character.


For example, for the following query string:



```
'name=value&abc=xyz&abc=123'
```

The return value of `querystring.parse()` is:



```
{
name: 'value',
abc: ['xyz', '123']
}
```

`querystring.decode()` is an alias for
 `querystring.parse()`.



`querystring.stringify(*object*[,
 *separator*[, *equal*[, *options*]]])`

Serializes an `object` and returns a query string.


The `separator` parameter is a substring for delimiting key
 and value pairs in the query string. By default it is
 `&`.


The `equal` parameter is a substring for delimiting keys
 and values in the query string. By default it is `=`.


The `options` parameter is an object with the following
 keys:




`encodeURIComponent *function*`

The function to use for converting URL-unsafe characters
 to percent-encoding in the query string. By default it is
 `querystring.escape()`.




By default, characters that require percent-encoding within the query
 string are encoded as UTF-8. To use a different encoding, specify the
 `encodeURIComponent` option.


For example, for the following code:



```
querystring.stringify({ name: 'value', abc: ['xyz', '123'], anotherName: '' });
```

The return value is:



```
'name=value&abc=xyz&abc=123&anotherName='
```

`querystring.encode()` is an alias for
 `querystring.stringify()`.



`querystring.unescape(*string*)`

Decodes URL percent-encoded characters in the given
 `string`, returning an unescaped query string. This
 method is used by `querystring.parse()` and should not be
 used directly.




### Crypto


The cryptographic module (`crypto`) provides standard hashing and
 hash-based message authentication code (HMAC) helpers. You can load the module using
 `require('crypto')`.


**Hashing methods**




`crypto.createHash(*algorithm*)`

Creates and returns a hash object that you can use to generate hash
 digests using the given algorithm: `md5`, `sha1`,
 or `sha256`.



`hash.update(*data*)`

Updates the hash content with the given `data`.



`hash.digest([*encoding*])`

Calculates the digest of all of the data passed using
 `hash.update()`. The encoding can be `hex`,
 `base64`, or `base64url`.




**HMAC methods**




`crypto.createHmac(*algorithm*,
 *secret key*)`

Creates and returns an HMAC object that uses the given
 `algorithm` and `secret key`. The algorithm
 can be `md5`, `sha1`, or
 `sha256`.



`hmac.update(*data*)`

Updates the HMAC content with the given `data`.



`hmac.digest([*encoding*])`

Calculates the digest of all of the data passed using
 `hmac.update()`. The encoding can be `hex`,
 `base64`, or `base64url`.




## Restricted
 features


The following JavaScript language features are either unsupported or restricted due to
 security concerns.




**Dynamic code evaluation**

Dynamic code evaluation is not supported. Both `eval()` and
 `Function` constructors throw an error if attempted. For
 example, `const sum = new Function('a', 'b', 'return a + b')`
 throws an error.



**Timers**

The `setTimeout()`, `setImmediate()`, and
 `clearTimeout()` functions are not supported. There is no
 provision to defer or yield within a function run. Your function must
 synchronously run to completion.



**Date and timestamps**

For security reasons, there is no access to high-resolution timers. All
 `Date` methods to query the current time always return the
 same value during the lifetime of a single function run. The returned
 timestamp is the time when the function started running. Consequently, you
 cannot measure elapsed time in your function.



**File system access**

There is no file system access. For example, there is no `fs`
 module for file system access like there is in Node.js.



**Process access**

There is no process access. For example, there is no `process`
 global object for processing information access like there is in
 Node.js.



**Environment variables**

There is no access to environment variables. Instead, you can use CloudFront KeyValueStore
 to create a centralized datastore of key-value pairs for your
 CloudFront Functions. CloudFront KeyValueStore enables dynamic updates to your configuration data
 without needing to deploy code changes. For more information, see [Amazon CloudFront KeyValueStore](kvs-with-functions.md "kvs-with-functions.md").



**Network access**

There is no support for network calls. For example, XHR, HTTP(S), and
 socket are not supported.
