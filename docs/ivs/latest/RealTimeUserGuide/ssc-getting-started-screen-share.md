# Enabling Screen Share in IVS Server-Side

Composition

To use a fixed screen-share layout, follow the steps below.

## Create

the EncoderConfiguration Resource

The command below creates an EncoderConfiguration resource that configures server-side
composition parameters (video bitrate, framerate, and resolution).

```
aws ivs-realtime create-encoder-configuration --name "test-ssc-with-screen-share" --video={bitrate=2000000,framerate=30,height=720,width=1280}
```

Create a stage participant token with a `screen-share` attribute. Since we
will specify `screen-share` as the name of the `featured` slot, we
need to create a stage token with the `screen-share` attribute set to
`true`:

```
aws ivs-realtime create-participant-token --stage-arn "arn:aws:ivs:us-east-1:123456789012:stage/u9OiE29bT7Xp" --attributes screen-share=true
```

The response is:

```
{
   "participantToken": {
      "attributes": {
         "screen-share": "true"
      },
      "expirationTime": "2023-08-04T05:26:11+00:00",
      "participantId": "E813MFklPWLF",
      "token": "eyJhbGciOiJLTVMiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2OTExMjY3NzEsImlhdCI6MTY5MTA4MzU3MSwianRpIjoiRTgxM01Ga2xQV0xGIiwicmVzb3VyY2UiOiJhcm46YXdzOml2czp1cy1lYXN0LTE6OTI3ODEwOTY3Mjk5OnN0YWdlL3U5T2lFMjliVDdYcCIsInRvcGljIjoidTlPaUUyOWJUN1hwIiwiZXZlbnRzX3VybCI6IndzczovL3VzLWVhc3QtMS5ldmVudHMubGl2ZS12aWRlby5uZXQiLCJ3aGlwX3VybCI6Imh0dHBzOi8vYjJlYTVjMmZmMzU1Lmdsb2JhbC53aGlwLmxpdmUtdmlkZW8ubmV0IiwiYXR0cmlidXRlcyI6eyJzY3JlZW4tc2hhcmUiOiJ0cnVlIn0sImNhcGFiaWxpdGllcyI6eyJhbGxvd19wdWJsaXNoIjp0cnVlLCJhbGxvd19zdWJzY3JpYmUiOnRydWV9LCJ2ZXJzaW9uIjoiMC4zIn0.MGUCMFvMzv35O4yVzM9tIWZl7n3mmFQhleqsRSBx_G2qT2YUDlWSNg6H1vL7sAWQMeydSAIxAIvdfqt3Fh1MLiyelc9NnTjI5hL3YPKqDX6J3NDH1fksh8_5y1jztoPDy4yVA5OmtA"
   }
}
```

## Start the

Composition

To start the composition using the screen-share feature, we use this command:

```
aws ivs-realtime start-composition --stage-arn "arn:aws:ivs:us-east-1:927810967299:stage/8faHz1SQp0ik" --destinations  '[{"channel": {"channelArn": "arn:aws:ivs:us-east-1:927810967299:channel/DOlMW4dfMR8r", "encoderConfigurationArn": "arn:aws:ivs:us-east-1:927810967299:encoder-configuration/DEkQHWPVaOwO"}}]' --layout '{"grid":{"featuredParticipantAttribute":"screen-share"}}'
```

The response is:

```
{
"composition" : {
"arn" : "arn:aws:ivs:us-east-1:927810967299:composition/B19tQcXRgtoz",
"destinations" : [ {
 "configuration" : {
	"channel" : {
	   "channelArn" : "arn:aws:ivs:us-east-1:927810967299:channel/DOlMW4dfMR8r",
	   "encoderConfigurationArn" : "arn:aws:ivs:us-east-1:927810967299:encoder-configuration/DEkQHWPVaOwO"
	},
	"name" : ""
 },
 "id" : "SGmgBXTULuXv",
 "state" : "STARTING"
} ],
"layout" : {
 "grid" : {
	"featuredParticipantAttribute" : "screen-share",
	"gridGap": 2,
	"omitStoppedVideo": false,
	"videoAspectRatio": "VIDEO"
 }
},
"stageArn" : "arn:aws:ivs:us-east-1:927810967299:stage/8faHz1SQp0ik",
"startTime" : "2023-09-27T21:32:38Z",
"state" : "STARTING",
"tags" : { }
}
}
```

When the stage participant `E813MFklPWLF` joins the stage, that
participant’s video will be displayed in the featured slot, and all other stage
publishers will be rendered below the slot:

![Starting the Composition using the screen-share feature.](images/ssc_StartComposition.png)

## Stop the

Composition

To stop a composition at any point, call the StopComposition operation:

```
aws ivs-realtime stop-composition --arn arn:aws:ivs:us-east-1:927810967299:composition/B19tQcXRgtoz
```
