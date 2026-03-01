# Change response codes returned by CloudFront

You can configure CloudFront to return a different HTTP status code to the viewer than what
CloudFront received from the origin. For example, if your origin returns a 500 status code to
CloudFront, you might want CloudFront to return a custom error page and a 200 status code (OK) to
the viewer. There are a variety of reasons that you might want CloudFront to return a status
code to the viewer that is different from the one that your origin returned to
CloudFront:

- Some internet devices (some firewalls and corporate proxies, for example)
  intercept HTTP 4xx and 5xx status codes and prevent the response from being
  returned to the viewer. In this scenario, if you substitute `200`,
  the response is not intercepted.
- If you don’t care about distinguishing among different client errors or server
  errors, you can specify `400` or `500` as the value that
  CloudFront returns for all 4xx or 5xx status codes.
- You might want to return a `200` status code (OK) and a static
  website so your customers don’t know that your website is down.
  If you enable [CloudFront standard logs](AccessLogs.md "AccessLogs.md") and you configure
  CloudFront to change the HTTP status code in the response, the value of the
  `sc-status` column in the logs contains the status code that you specify.
  However, the value of the `x-edge-result-type` column is not affected. It
  contains the result type of the response from the origin. For example, suppose you
  configure CloudFront to return a status code of `200` to the viewer when the origin
  returns `404` (Not Found) to CloudFront. When the origin responds to a request with
  a `404` status code, the value in the `sc-status` column in the
  log will be `200`, but the value in the `x-edge-result-type`
  column will be `Error`.

You can configure CloudFront to return any of the following HTTP status codes along with a
custom error page:

- 200
- 400, 403, 404, 405, 414, 416
- 500, 501, 502, 503, 504
