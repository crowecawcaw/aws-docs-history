# Verifying C2PA manifests

After creating MP4 outputs with C2PA manifests, you can verify the manifests using C2PA-compatible tools. These tools can extract and validate the manifest, including checking the digital signature and asset hash.

A properly validated C2PA manifest confirms that:

- The manifest was signed by the specified certificate
- The content has not been modified since the manifest was created
- The actions and assertions in the manifest are intact
  For more information about C2PA and available verification tools, see the [C2PA website](https://c2pa.org "https://c2pa.org"). You can use the open-source [c2patool](https://github.com/contentauth/c2pa-rs/tree/main/cli "https://github.com/contentauth/c2pa-rs/tree/main/cli") to verify C2PA manifests in
  your media files. For example:

```
c2patool example.mp4 --info
```

A successful validation will show output similar to:

```
$ c2patool example.mp4 --info
Information for example.mp4
Manifest store size = 32000 (0.56% of file size 5705967)
Validated
One manifest
```

For more detailed information about the manifest contents, use the `--detailed`
flag:

```
c2patool example.mp4 --detailed
```

The following is an example output from c2patool:

```

$ c2patool example.mp4 --detailed
{
 "active_manifest": "urn:uuid:0b3bd0b6-9783-4adc-9609-fb29fff858da",
 "manifests": {
  "urn:uuid:0b3bd0b6-9783-4adc-9609-fb29fff858da": {
   "claim": {
    "dc:title": "example.mp4",
    "dc:format": "video/mp4",
    "instanceID": "xmp:iid:190fb451-7dc4-4878-b0d2-512d9b1c5dab",
    "claim_generator": "mediaconvert/1.0",
    "claim_generator_info": [
     {
      "name": "MediaConvert",
      "version": "1.0",
      "org.cai.c2pa_rs": "0.39.0"
     }
    ],
    "signature": "self#jumbf=/c2pa/urn:uuid:0b3bd0b6-9783-4adc-9609-fb29fff858da/c2pa.signature",
    "assertions": [
     {
      "url": "self#jumbf=c2pa.assertions/c2pa.actions",
      "hash": "P2+zrSTu2U5aGo4mNC35EWEM7vjfLho/2tTKmZ+ls+k="
     },
     {
      "url": "self#jumbf=c2pa.assertions/c2pa.hash.bmff",
      "hash": "majeRA6voTIMvHShWBR5Vqg7e4c7dVFsfTbezIzn63o="
     }
    ],
    "alg": "sha256"
   },
   "assertion_store": {
    "c2pa.actions": {
     "actions": [
      {
       "action": "c2pa.opened"
      },
      {
       "action": "c2pa.transcoded"
      }
     ]
    },
    "c2pa.hash.bmff": {
     "alg": "sha256",
     "hash": "BHZI6ml1LqBf2xLaKAzYS8uOYwWo5/Wsc30wRYmnr4M=",
     "name": "jumbf manifest",
     "exclusions": [
      {
       "data": null,
       "exact": null,
       "flags": null,
       "xpath": "/ftyp",
       "length": null,
       "subset": null,
       "version": null
      },
      {
       "data": null,
       "exact": null,
       "flags": null,
       "xpath": "/uuid",
       "length": null,
       "subset": null,
       "version": null
      },
      {
       "data": null,
       "exact": null,
       "flags": null,
       "xpath": "/free",
       "length": null,
       "subset": null,
       "version": null
      },
      {
       "data": null,
       "exact": null,
       "flags": null,
       "xpath": "/mdat",
       "length": null,
       "subset": [
        {
         "length": 8,
         "offset": 0
        }
       ],
       "version": null
      },
      {
       "data": null,
       "exact": null,
       "flags": null,
       "xpath": "/moov",
       "length": null,
       "subset": null,
       "version": null
      },
      {
       "data": null,
       "exact": null,
       "flags": null,
       "xpath": "/mfra",
       "length": null,
       "subset": null,
       "version": null
      }
     ]
    }
   },
   "signature": {
    "alg": "es256",
    "issuer": "Test Organization",
    "time": "2025-04-11T23:17:33+00:00"
   }
  }
 },
 "validation_status": [
  {
   "code": "claimSignature.validated",
   "url": "self#jumbf=/c2pa/urn:uuid:0b3bd0b6-9783-4adc-9609-fb29fff858da/c2pa.signature",
   "explanation": "claim signature valid"
  },
  {
   "code": "assertion.hashedURI.match",
   "url": "self#jumbf=/c2pa/urn:uuid:0b3bd0b6-9783-4adc-9609-fb29fff858da/c2pa.assertions/c2pa.actions",
   "explanation": "hashed uri matched: self#jumbf=c2pa.assertions/c2pa.actions"
  },
  {
   "code": "assertion.hashedURI.match",
   "url": "self#jumbf=/c2pa/urn:uuid:0b3bd0b6-9783-4adc-9609-fb29fff858da/c2pa.assertions/c2pa.hash.bmff",
   "explanation": "hashed uri matched: self#jumbf=c2pa.assertions/c2pa.hash.bmff"
  },
  {
   "code": "assertion.bmffHash.match",
   "url": "self#jumbf=/c2pa/urn:uuid:0b3bd0b6-9783-4adc-9609-fb29fff858da/c2pa.assertions/c2pa.hash.bmff",
   "explanation": "data hash valid"
  }
 ]
}
```
