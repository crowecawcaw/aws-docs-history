# HTTP input requirements

When your input file source is HTTP(S), you specify the URL rather than an Amazon S3 path.
Requirements for using HTTP(S) for input are as follows:

- All input files must be publicly readable.
- The HTTP(S) server must not require authentication.
- The HTTP(S) server must accept both HEAD and range GET requests.
- The URL that you specify can't include parameters.
  If your HTTP(S) input uses redirection, it must follow these restrictions:

- You can redirect only once from the URL that you provide as your input. You
  can't redirect to a URL that, in turn, contains a redirect.
- The HTTP(S) status response code from the initial server must be either 301 or

302.

- The HTTP(S) response from the initial server must use its
  `Location` headers to provide the URL that it's redirecting
  MediaConvert to.
