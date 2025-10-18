# HTTP 403 status code (Invalid method)

CloudFront returns a 403 (Invalid method) error if you're trying to use an HTTP method that you
 haven't specified in the CloudFront distribution. You can specify one of the following
 options for your distribution:


* CloudFront forwards only `GET` and `HEAD` requests.
* CloudFront forwards only `GET`, `HEAD`, and
 `OPTIONS` requests.
* CloudFront forwards `GET`, `HEAD`, `OPTIONS`,
 `PUT`, `PATCH`, `POST`, and
 `DELETE` requests. (If you select this option, you might need
 to restrict access to your Amazon S3 bucket or custom origin so that users can't
 perform operations that you don't want them to. For example, you might not
 want users to have permissions to delete objects from your origin.
