# Create a URL signature using PHP

Any web server that runs PHP can use this PHP example code to create policy
statements and signatures for private CloudFront distributions. The full example creates a
functioning webpage with signed URL links that play a video stream using CloudFront
streaming. You can download the full example from the [demo-php.zip](samples/demo-php.md "samples/demo-php.md") file.

###### Notes

- Creating a URL signature is just one part of the process of serving
  private content using a signed URL. For more information about the
  entire process, see [Use signed URLs](private-content-signed-urls.md "private-content-signed-urls.md").
- You can also create signed URLs by using the `UrlSigner`
  class in the AWS SDK for PHP. For more information, see [Class UrlSigner](../../../aws-sdk-php/v3/api/class-Aws.CloudFront.md "../../../aws-sdk-php/v3/api/class-Aws.CloudFront.md") in the
  _AWS SDK for PHP API Reference_.

###### Topics

- [Create the RSA SHA-1 signature](#sample-rsa-sign "#sample-rsa-sign")
- [Create a canned policy](#sample-canned-policy "#sample-canned-policy")
- [Create a custom policy](#sample-custom-policy "#sample-custom-policy")
- [Full code example](#full-example "#full-example")
  The following sections breaks down the code example into individual parts. You can
  find the [Full code example](#full-example "#full-example") below.

## Create the RSA SHA-1 signature

This code example does the following:

- The function `rsa_sha1_sign` hashes and signs the policy
  statement. The arguments required are a policy statement and the private
  key that corresponds with a public key that’s in a trusted key group for
  your distribution.
- Next, the `url_safe_base64_encode` function creates a
  URL-safe version of the signature.

```
function rsa_sha1_sign($policy, $private_key_filename) {
    $signature = "";

    // load the private key
    $fp = fopen($private_key_filename, "r");
    $priv_key = fread($fp, 8192);
    fclose($fp);
    $pkeyid = openssl_get_privatekey($priv_key);

    // compute signature
    openssl_sign($policy, $signature, $pkeyid);

    // free the key from memory
    openssl_free_key($pkeyid);

    return $signature;
}

function url_safe_base64_encode($value) {
    $encoded = base64_encode($value);
    // replace unsafe characters +, = and / with
    // the safe characters -, _ and ~
    return str_replace(
        array('+', '=', '/'),
        array('-', '_', '~'),
        $encoded);
}
```

The following code snippet uses the functions
`get_canned_policy_stream_name()` and
`get_custom_policy_stream_name()` to create a canned and custom
policy. CloudFront uses the policies to create the URL for streaming the video,
including specifying the expiration time.

You can then used a canned policy or a custom policy to determine how to
manage access to your content. For more information about which one to choose,
see the [Decide to use canned or custom policies for signed URLs](private-content-signed-urls.md#private-content-choosing-canned-custom-policy "private-content-signed-urls.md#private-content-choosing-canned-custom-policy") section.

## Create a canned policy

The following example code constructs a _canned_ policy
statement for the signature.

###### Note

The `$expires` variable is a date/time stamp that must be an
integer, not a string.

```
function get_canned_policy_stream_name($video_path, $private_key_filename, $key_pair_id, $expires) {
    // this policy is well known by CloudFront, but you still need to sign it, since it contains your parameters
    $canned_policy = '{"Statement":[{"Resource":"' . $video_path . '","Condition":{"DateLessThan":{"AWS:EpochTime":'. $expires . '}}}]}';
    // the policy contains characters that cannot be part of a URL, so we base64 encode it
    $encoded_policy = url_safe_base64_encode($canned_policy);
    // sign the original policy, not the encoded version
    $signature = rsa_sha1_sign($canned_policy, $private_key_filename);
    // make the signature safe to be included in a URL
    $encoded_signature = url_safe_base64_encode($signature);

    // combine the above into a stream name
    $stream_name = create_stream_name($video_path, null, $encoded_signature, $key_pair_id, $expires);
    // URL-encode the query string characters
    return $stream_name;
}
```

For more information about canned policies, see [Create a signed URL using a canned policy](private-content-creating-signed-url-canned-policy.md "private-content-creating-signed-url-canned-policy.md").

## Create a custom policy

The following example code constructs a _custom_ policy
statement for the signature.

```
function get_custom_policy_stream_name($video_path, $private_key_filename, $key_pair_id, $policy) {
    // the policy contains characters that cannot be part of a URL, so we base64 encode it
    $encoded_policy = url_safe_base64_encode($policy);
    // sign the original policy, not the encoded version
    $signature = rsa_sha1_sign($policy, $private_key_filename);
    // make the signature safe to be included in a URL
    $encoded_signature = url_safe_base64_encode($signature);

    // combine the above into a stream name
    $stream_name = create_stream_name($video_path, $encoded_policy, $encoded_signature, $key_pair_id, null);
    // URL-encode the query string characters
    return $stream_name;
}
```

For more information about custom policies, see [Create a signed URL using a custom policy](private-content-creating-signed-url-custom-policy.md "private-content-creating-signed-url-custom-policy.md").

## Full code example

The following example code provides a complete demonstration of creating CloudFront
signed URLs with PHP. You can download the full example from the [demo-php.zip](samples/demo-php.md "samples/demo-php.md") file.

In the following example, you can modify the `$policy`
`Condition` element to allow both IPv4 and IPv6 address ranges. For
an example, see [Using IPv6
addresses in IAM policies](../../../AmazonS3/latest/userguide/ipv6-access.md#ipv6-access-iam "../../../AmazonS3/latest/userguide/ipv6-access.md#ipv6-access-iam") in the
_Amazon Simple Storage Service User Guide_.

```
<?php

function rsa_sha1_sign($policy, $private_key_filename) {
    $signature = "";

    // load the private key
    $fp = fopen($private_key_filename, "r");
    $priv_key = fread($fp, 8192);
    fclose($fp);
    $pkeyid = openssl_get_privatekey($priv_key);

    // compute signature
    openssl_sign($policy, $signature, $pkeyid);

    // free the key from memory
    openssl_free_key($pkeyid);

    return $signature;
}

function url_safe_base64_encode($value) {
    $encoded = base64_encode($value);
    // replace unsafe characters +, = and / with the safe characters -, _ and ~
    return str_replace(
        array('+', '=', '/'),
        array('-', '_', '~'),
        $encoded);
}

function create_stream_name($stream, $policy, $signature, $key_pair_id, $expires) {
    $result = $stream;
    // if the stream already contains query parameters, attach the new query parameters to the end
    // otherwise, add the query parameters
    $separator = strpos($stream, '?') == FALSE ? '?' : '&';
    // the presence of an expires time means we're using a canned policy
    if($expires) {
        $result .= $separator . "Expires=" . $expires . "&Signature=" . $signature . "&Key-Pair-Id=" . $key_pair_id;
    }
    // not using a canned policy, include the policy itself in the stream name
    else {
        $result .= $separator . "Policy=" . $policy . "&Signature=" . $signature . "&Key-Pair-Id=" . $key_pair_id;
    }

    // new lines would break us, so remove them
    return str_replace('\n', '', $result);
}


function get_canned_policy_stream_name($video_path, $private_key_filename, $key_pair_id, $expires) {
    // this policy is well known by CloudFront, but you still need to sign it, since it contains your parameters
    $canned_policy = '{"Statement":[{"Resource":"' . $video_path . '","Condition":{"DateLessThan":{"AWS:EpochTime":'. $expires . '}}}]}';
    // the policy contains characters that cannot be part of a URL, so we base64 encode it
    $encoded_policy = url_safe_base64_encode($canned_policy);
    // sign the original policy, not the encoded version
    $signature = rsa_sha1_sign($canned_policy, $private_key_filename);
    // make the signature safe to be included in a URL
    $encoded_signature = url_safe_base64_encode($signature);

    // combine the above into a stream name
    $stream_name = create_stream_name($video_path, null, $encoded_signature, $key_pair_id, $expires);
    // URL-encode the query string characters
    return $stream_name;
}

function get_custom_policy_stream_name($video_path, $private_key_filename, $key_pair_id, $policy) {
    // the policy contains characters that cannot be part of a URL, so we base64 encode it
    $encoded_policy = url_safe_base64_encode($policy);
    // sign the original policy, not the encoded version
    $signature = rsa_sha1_sign($policy, $private_key_filename);
    // make the signature safe to be included in a URL
    $encoded_signature = url_safe_base64_encode($signature);

    // combine the above into a stream name
    $stream_name = create_stream_name($video_path, $encoded_policy, $encoded_signature, $key_pair_id, null);
    // URL-encode the query string characters
    return $stream_name;
}


// Path to your private key.  Be very careful that this file is not accessible
// from the web!

$private_key_filename = '/home/test/secure/example-priv-key.pem';
$key_pair_id = 'K2JCJMDEHXQW5F';

// Make sure you have "Restrict viewer access" enabled on this path behaviour and using the above Trusted key groups (recommended).
$video_path = 'https://example.com/secure/example.mp4';

$expires = time() + 300; // 5 min from now
$canned_policy_stream_name = get_canned_policy_stream_name($video_path, $private_key_filename, $key_pair_id, $expires);

// Get the viewer real IP from the x-forward-for header as $_SERVER['REMOTE_ADDR'] will return viewer facing IP. An alternative option is to use CloudFront-Viewer-Address header. Note that this header is a trusted CloudFront immutable header. Example format: IP:PORT ("CloudFront-Viewer-Address": "1.2.3.4:12345")
$client_ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
$policy =
'{'.
    '"Statement":['.
        '{'.
            '"Resource":"'. $video_path . '",'.
            '"Condition":{'.
                '"IpAddress":{"AWS:SourceIp":"' . $client_ip . '/32"},'.
                '"DateLessThan":{"AWS:EpochTime":' . $expires . '}'.
            '}'.
        '}'.
    ']' .
    '}';
$custom_policy_stream_name = get_custom_policy_stream_name($video_path, $private_key_filename, $key_pair_id, $policy);

?>

<html>

<head>
    <title>CloudFront</title>
</head>

<body>
    <h1>Amazon CloudFront</h1>
    <h2>Canned Policy</h2>
    <h3>Expires at <?php echo gmdate('Y-m-d H:i:s T', $expires); ?></h3>
    <br />

    <div id='canned'>The canned policy video will be here: <br>

        <video width="640" height="360" autoplay muted controls>
        <source src="<?php echo $canned_policy_stream_name; ?>" type="video/mp4">
        Your browser does not support the video tag.
        </video>
    </div>

    <h2>Custom Policy</h2>
    <h3>Expires at <?php echo gmdate('Y-m-d H:i:s T', $expires); ?> only viewable by IP <?php echo $client_ip; ?></h3>
    <div id='custom'>The custom policy video will be here: <br>

         <video width="640" height="360" autoplay muted controls>
         <source src="<?php echo $custom_policy_stream_name; ?>" type="video/mp4">
         Your browser does not support the video tag.
        </video>
    </div>

</body>

</html>
```

For additional URL signature examples, see the following topics:

- [Create a URL signature using Perl](CreateURLPerl.md "CreateURLPerl.md")
- [Create a URL signature using C# and the .NET Framework](CreateSignatureInCSharp.md "CreateSignatureInCSharp.md")
- [Create a URL signature using Java](CFPrivateDistJavaDevelopment.md "CFPrivateDistJavaDevelopment.md")
  Instead of using signed URLs to create the signature, you can use signed cookies.
  For more information, see [Create signed cookies using PHP](signed-cookies-PHP.md "signed-cookies-PHP.md").
