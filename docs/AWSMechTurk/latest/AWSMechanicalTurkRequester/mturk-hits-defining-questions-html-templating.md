# Templating

When using Mechanical Turk tasks it's common to use a template approach to reuse the same
question definition on multiple tasks. For example, the following can be used to gather
keywords for a single image, but wouldn't be as useful when collecting keywords for
thousands of images.

```

<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>
<crowd-form>
     <img src="https://my-bucket.s3.amazonaws.com/img1234.jpg">
<p>Provide three keywords for the image above:</p>
<p><input type="text" name="keyword1"></p>
<p><input type="text" name="keyword2"></p>
<p><input type="text" name="keyword3"></p>
</crowd-form>
 

```

To enable reuse of this HTML, you can replace the image URL with a template variable
surrounded by curly braces as shown below. We've also added the URL as a
_hidden_ form element to make it easier to process the results by
including the source URL alongside the keywords workers provide.

```

<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>
<crowd-form>
     <img src="${url}">
     <input type="hidden" name="url" value="${url}">
<p>Provide three keywords for the image above:</p>
<p><input type="text" name="keyword1"></p>
<p><input type="text" name="keyword2"></p>
<p><input type="text" name="keyword3"></p>
</crowd-form>
 

```

When you iterate through the list of images, you can then simply perform a
find/replace on the `${url}` value in the HTML so that each task has a unique
question corresponding to an image URL.

Note that the `${}` syntax used above is also used for tasks created using
the Mechanical Turk requester website. There are a variety of different templating languages and
libraries you can use to render your task interface. It's recommended you choose a library
that works best for you in your desired programming language.
