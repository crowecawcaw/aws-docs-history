# Create signed cookies using PHP

The following code example is similar to the example in the [Create a URL signature using PHP](CreateURL_PHP.md "CreateURL_PHP.md") in that it creates a
link to a video. However, instead of signing the URL in the code, this example signs
the cookies with the `create_signed_cookies()` function. The client-side
player uses the cookies to authenticate each request to the CloudFront
distribution.

This approach is useful to stream content, such as HTTP Live Streaming (HLS) or
Dynamic Adaptive Streaming over HTTP (DASH), where the client needs to make multiple
requests to retrieve the manifest, segments, and related playback assets. By using
signed cookies, the client can authenticate each request without needing to generate
a new signed URL for each segment.

###### Note

- Creating a URL signature is just one part of the process of serving
  private content using signed cookies. For more information, see [Use signed cookies](private-content-signed-cookies.md "private-content-signed-cookies.md").

###### Topics

- [Create the RSA SHA-1
  signature](#create-rsa-sha-1signature-cookies "#create-rsa-sha-1signature-cookies")
- [Create the signed cookies](#create-the-signed-cookie "#create-the-signed-cookie")
- [Full code](#full-code-signed-cookies "#full-code-signed-cookies")
  The following sections breaks down the code example into individual parts. You can
  find the complete [code sample](#full-code-signed-cookies "#full-code-signed-cookies")
  below.

## Create the RSA SHA-1

signature

This code example does the following:

1. The function `rsa_sha1_sign` hashes and signs the policy
   statement. The arguments required are a policy statement and the private
   key that corresponds with a public key that’s in a trusted key group for
   your distribution.
2. Next, the `url_safe_base64_encode` function creates a
   URL-safe version of the signature.

```
function rsa_sha1_sign($policy, $private_key_filename) {
    $signature = "";
    $fp = fopen($private_key_filename, "r");
    $priv_key = fread($fp, 8192);
    fclose($fp);
    $pkeyid = openssl_get_privatekey($priv_key);
    openssl_sign($policy, $signature, $pkeyid);
    openssl_free_key($pkeyid);
    return $signature;
}

function url_safe_base64_encode($value) {
    $encoded = base64_encode($value);
    return str_replace(
        array('+', '=', '/'),
        array('-', '_', '~'),
        $encoded);
}
```

## Create the signed cookies

The following code constructs a creates the signed cookies, using the
following cookie attributes: `CloudFront-Expires`,
`CloudFront-Signature`, and `CloudFront-Key-Pair-Id`.
The code uses a custom policy.

```
function create_signed_cookies($resource, $private_key_filename, $key_pair_id, $expires, $client_ip = null) {
    $policy = array(
        'Statement' => array(
            array(
                'Resource' => $resource,
                'Condition' => array(
                    'DateLessThan' => array('AWS:EpochTime' => $expires)
                )
            )
        )
    );

    if ($client_ip) {
        $policy['Statement'][0]['Condition']['IpAddress'] = array('AWS:SourceIp' => $client_ip . '/32');
    }

    $policy = json_encode($policy);
    $encoded_policy = url_safe_base64_encode($policy);
    $signature = rsa_sha1_sign($policy, $private_key_filename);
    $encoded_signature = url_safe_base64_encode($signature);

    return array(
        'CloudFront-Policy' => $encoded_policy,
        'CloudFront-Signature' => $encoded_signature,
        'CloudFront-Key-Pair-Id' => $key_pair_id
    );
}
```

For more information, see [Set signed
cookies using a custom policy](private-content-setting-signed-cookie-custom-policy.md "private-content-setting-signed-cookie-custom-policy.md").

## Full code

The following example code provides a complete demonstration of creating
CloudFront signed cookies with PHP. You can download the full example from the
[demo-php.zip](samples/demo-php.md "samples/demo-php.md") file.

In the following example, you can modify the `$policy Condition`
element to allow both IPv4 and IPv6 address ranges. For an example, see [Using IPv6 addresses in IAM policies](../../../AmazonS3/latest/userguide/ipv6-access.md#ipv6-access-iam "../../../AmazonS3/latest/userguide/ipv6-access.md#ipv6-access-iam") in the
_Amazon Simple Storage Service User
Guide_.

```
<?php

function rsa_sha1_sign($policy, $private_key_filename) {
    $signature = "";
    $fp = fopen($private_key_filename, "r");
    $priv_key = fread($fp, 8192);
    fclose($fp);
    $pkeyid = openssl_get_privatekey($priv_key);
    openssl_sign($policy, $signature, $pkeyid);
    openssl_free_key($pkeyid);
    return $signature;
}

function url_safe_base64_encode($value) {
    $encoded = base64_encode($value);
    return str_replace(
        array('+', '=', '/'),
        array('-', '_', '~'),
        $encoded);
}

function create_signed_cookies($resource, $private_key_filename, $key_pair_id, $expires, $client_ip = null) {
    $policy = array(
        'Statement' => array(
            array(
                'Resource' => $resource,
                'Condition' => array(
                    'DateLessThan' => array('AWS:EpochTime' => $expires)
                )
            )
        )
    );

    if ($client_ip) {
        $policy['Statement'][0]['Condition']['IpAddress'] = array('AWS:SourceIp' => $client_ip . '/32');
    }

    $policy = json_encode($policy);
    $encoded_policy = url_safe_base64_encode($policy);
    $signature = rsa_sha1_sign($policy, $private_key_filename);
    $encoded_signature = url_safe_base64_encode($signature);

    return array(
        'CloudFront-Policy' => $encoded_policy,
        'CloudFront-Signature' => $encoded_signature,
        'CloudFront-Key-Pair-Id' => $key_pair_id
    );
}



$private_key_filename = '/home/test/secure/example-priv-key.pem';
$key_pair_id = 'K2JCJMDEHXQW5F';
$base_url = 'https://d1234.cloudfront.net';

$expires = time() + 3600; // 1 hour from now

// Get the viewer real IP from the x-forward-for header as $_SERVER['REMOTE_ADDR'] will return viewer facing IP. An alternative option is to use CloudFront-Viewer-Address header. Note that this header is a trusted CloudFront immutable header. Example format: IP:PORT ("CloudFront-Viewer-Address": "1.2.3.4:12345")
$client_ip = $_SERVER['HTTP_X_FORWARDED_FOR'];


// For HLS manifest and segments (using wildcard)
$hls_resource = $base_url . '/sign/*';
$signed_cookies = create_signed_cookies($hls_resource, $private_key_filename, $key_pair_id, $expires, $client_ip);

// Set the cookies
$cookie_domain = parse_url($base_url, PHP_URL_HOST);
foreach ($signed_cookies as $name => $value) {
    setcookie($name, $value, $expires, '/', $cookie_domain, true, true);
}

?>

<!DOCTYPE html>
<html>
<head>
    <title>CloudFront Signed HLS Stream with Cookies</title>
</head>
<body>
    <h1>Amazon CloudFront Signed HLS Stream with Cookies</h1>
    <h2>Expires at <?php echo gmdate('Y-m-d H:i:s T', $expires); ?> only viewable by IP <?php echo $client_ip; ?></h2>

    <div id='hls-video'>
        <video id="video" width="640" height="360" controls></video>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
    <script>
        var video = document.getElementById('video');
        var manifestUrl = '<?php echo $base_url; ?>/sign/manifest.m3u8';

        if (Hls.isSupported()) {
            var hls = new Hls();
            hls.loadSource(manifestUrl);
            hls.attachMedia(video);
        }
        else if (video.canPlayType('application/vnd.apple.mpegurl')) {
            video.src = manifestUrl;
        }
    </script>
</body>
</html>
```

Instead of using signed cookies, you can use signed URLs. For more
information, see [Create a URL signature using PHP](CreateURL_PHP.md "CreateURL_PHP.md").
