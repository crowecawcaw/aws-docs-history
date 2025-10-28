End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# CORS use-case scenarios

The following are example scenarios for using CORS:

- Scenario 1: Suppose you are distributing live streaming video in an AWS Elemental MediaStore container named _LiveVideo_. Your
  users load the video manifest endpoint `http://livevideo.mediastore.ap-southeast-2.amazonaws.com` from a specific origin
  like `www.example.com`. You want to use a JavaScript video player to access videos that are originated from this
  container via unauthenticated `GET` and `PUT` requests. A browser would typically block JavaScript
  from allowing those requests, but you can set a CORS policy on your container to explicitly enable these requests from
  `www.example.com`.
- Scenario 2: Suppose you want to host the same live stream as in Scenario 1 from your MediaStore container, but want to allow requests
  from any origin. You can configure a CORS policy to allow wildcard (\*) origins, so that requests from any origin can access the
  video.
