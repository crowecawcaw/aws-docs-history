# Using Amazon Q Developer for full function generation

Amazon Q can generate an entire function based on a comment that you've
written. As you finish your comment Amazon Q will suggest a function
signature. If you accept the suggestion, Amazon Q automatically advances
your cursor to the next part of the function and makes a suggestion. Even if you
enter an additional comment or line of code in between suggestions,
Amazon Q will refactor based on your input.

C

![An example of the full function completion feature using C.](images/full-function-completion-c-plus.gif)

C++

![An example of the full function completion feature using C++.](images/full-function-completion-c-plus.gif)

JavaScript
In the following example, the user generates, and then edits,
a full function based on a set of comments.

![An example of the full-function generation feature.](images/javascript_lambda_FullFunctionGeneration.gif)

In the following image, a user has written a function signature for reading a file from
Amazon S3. Amazon Q then suggests a full implementation of the `read_from_s3`
method.

![A screenshot that shows a Amazon Q recommendation to complete an entire function that reads an object from an Amazon S3 location.](images/whisper-function-read-from-s3.png)

###### Note

Sometimes, as in the previous example, Amazon Q includes `import` statements
as part of its suggestions. As a best practice, manually move these `import`
statements to the top of your file.

As another example, in the following image, a user has written a function signature.
Amazon Q then suggests a full implementation of the `quicksort` method.

![A screenshot that shows a Amazon Q recommendation for an entire function implementation of the quicksort algorithm.](images/whisper-function-quicksort.png)

Amazon Q considers past code snippets when making suggestions. In the following image,
the user in the previous example has accepted the suggested implementation for
`quicksort` above. The user then writes another function signature for a generic
`sort` method. Amazon Q then suggests an implementation based on what has already
been written.

![A screenshot that shows a Amazon Q recommendation for a function implementation based on context.](images/whisper-function-from-context-sort.png)

In the following image, a user has written a comment. Based on this comment, Amazon Q
then suggests a function signature.

![A screenshot that shows a Amazon Q recommendation for a binary search function signature based on user code comments.](images/whisper-comment-binary-search.png)

In the following image, the user in the previous example has accepted the suggested
function signature. Amazon Q can then suggest a complete implementation of the
`binary_search` function.

![A screenshot that shows a Amazon Q recommendation for a complete implementation of the binary search algorithm.](images/whisper-function-binary-search.png)

Java
The following list contains examples of how Amazon Q makes suggestions
and advances you through the entire process of creating a function.

1. In the following example, a user inputs a comment. Amazon Q suggests a function
   signature.

After the user accepts that suggestion, Amazon Q suggests a function body.

![An example of a function generated from a comment.](images/cw-c9-function-from-comment.gif) 2. In the image below, a user inputs a comment in the body of the function prior to
accepting a suggestion from Amazon Q. On the following line, Amazon Q generates a
suggestion based on the comment.

![An example of a function generated from a comment inside an existing block of code.](images/cw-c9-function-from-comment-within-block.gif)

C#
In the following example, Amazon Q recommends a full function.

![Function declaration for ListTables with AmazonDynamoDBClient parameter in code editor.](images/c-sharp-full-function.gif)

TypeScript
In the following example, Amazon Q generates a function based on the user's docstrings.

![An example of the full function completion feature.](images/typescript_vscode_function.gif)

Python
Amazon Q can generate an entire function based on a comment that you've written. As you
finish your comment, Amazon Q will suggest a function signature. If you accept the suggestion,
Amazon Q automatically advances your cursor to the next part of the function and makes a
suggestion. Even if you enter an additional comment or line of code in between suggestions,
Amazon Q will refactor based on your input.

In the following example, Amazon Q generates both a full
function and the corresponding unit test.

![An example of the full function completion feature.](images/python_pycharm_fullfunction_unittests.GIF)

The following list contains examples of how Amazon Q makes suggestions
and advances you through the entire process of creating a function.

1. In the image below, a user has input a comment. The function signature, located below
   the comment, is a suggestion from Amazon Q.

![alt_text](images/cw-jb-comment-062022.png) 2. In the image below, the user has accepted the Amazon Q suggestion for a function
signature. Accepting the suggestion automatically advanced the cursor and Amazon Q has made
a new suggestion for the function body.

![alt_text](images/cw-jb-commentfunctionadvance-062022.png) 3. In the image below, a user input a comment in the body of the function prior to
accepting a suggestion from Amazon Q. On the following line, Amazon Q has generated a new
suggestion based on the content of the comment.

![generateing a new suggestion based on the content of a comment](images/cw-jb-commentfunction-062022.png)

In this example, Amazon Q recommends a full function after the user types part of the signature.

![An example of the full function feature.](images/python_sagemakerstudio_fullfunction.gif)
