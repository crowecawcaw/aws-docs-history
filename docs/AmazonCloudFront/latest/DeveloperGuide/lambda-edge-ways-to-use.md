# Ways to use Lambda@Edge

There are many uses for Lambda@Edge processing with your Amazon CloudFront distribution, such as
the following examples:

- A Lambda function can inspect cookies and rewrite URLs so that users see
  different versions of a site for A/B testing.
- CloudFront can return different objects to viewers based on the device they're using
  by checking the `User-Agent` header, which includes information about
  the devices. For example, CloudFront can return different images based on the screen
  size of their device. Similarly, the function could consider the value of the
  `Referer` header and cause CloudFront to return the images to bots that
  have the lowest available resolution.
- Or you could check cookies for other criteria. For example, on a retail
  website that sells clothing, if you use cookies to indicate which color a user
  chose for a jacket, a Lambda function can change the request so that CloudFront returns
  the image of a jacket in the selected color.
- A Lambda function can generate HTTP responses when CloudFront viewer request or
  origin request events occur.
- A function can inspect headers or authorization tokens, and insert a header to
  control access to your content before CloudFront forwards the request to your
  origin.
- A Lambda function can also make network calls to external resources to confirm
  user credentials, or fetch additional content to customize a response.
  For more information, including example code, see [Lambda@Edge example functions](lambda-examples.md "lambda-examples.md").

For more information about setting up Lambda@Edge in the console, see [Tutorial: Create a basic Lambda@Edge function (console)](lambda-edge-how-it-works-tutorial.md "lambda-edge-how-it-works-tutorial.md").
