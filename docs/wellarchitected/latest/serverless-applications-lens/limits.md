# Limits

In addition to what is covered in the Well-Architected Framework, consider reviewing
limits for burst and spiky use cases. For example, API Gateway and Lambda have different limits for
steady and burst request rates. Use scaling layers and asynchronous patterns when possible,
and perform load testing to ensure that your current account limits can sustain your actual
customer demand.
