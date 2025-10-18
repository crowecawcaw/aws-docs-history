# JavaScript runtime features for
 CloudFront Functions

The CloudFront Functions JavaScript runtime environment is compliant with [ECMAScript (ES) version
 5.1](https://www.ecma-international.org/ecma-262/5.1/ "https://www.ecma-international.org/ecma-262/5.1/") and also supports some features of ES versions 6 through 12.

For the most up-to-date features, we recommend that you use JavaScript runtime
 2.0.
 

The JavaScript runtime 2.0 features has the following changes compared to 1.0:


* Buffer module methods are available
* The following non-standard string prototype methods are not available:




	+ `String.prototype.bytesFrom()`
	+ `String.prototype.fromBytes()`
	+ `String.prototype.fromUTF8()`
	+ `String.prototype.toBytes()`
	+ `String.prototype.toUTF8()`
* The cryptographic module has the following changes:




	+ `hash.digest()` – Return type is changed to
	 `Buffer` if no encoding is provided
	+ `hmac.digest()` – Return type is changed to
	 `Buffer` if no encoding is provided
* For more information about additional new features, see [JavaScript runtime 2.0 features for
 CloudFront Functions](functions-javascript-runtime-20.md "functions-javascript-runtime-20.md").
###### Topics

* [JavaScript runtime 1.0
 features](functions-javascript-runtime-10.md "functions-javascript-runtime-10.md")
* [JavaScript runtime 2.0
 features](functions-javascript-runtime-20.md "functions-javascript-runtime-20.md")
