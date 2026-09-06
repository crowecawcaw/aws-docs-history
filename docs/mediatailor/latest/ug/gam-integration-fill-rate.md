

# Optimizing ad fill rate with Google Ad Manager
<a name="gam-integration-fill-rate"></a>

When you use Google Ad Manager (GAM) as your ad server with MediaTailor, your ADS template URL parameters directly affect ad fill rate and revenue. Incorrect parameter values are one of the most common causes of low fill rates.

## Recommended GAM parameters
<a name="gam-fill-rate-recommended-params"></a>

Include the following parameters in your ADS template URL to ensure GAM returns ads consistently and fills ad breaks to their full duration.

`correlator=[avail.random]`  
Ensures GAM treats each ad break as a unique request and returns fresh ads. Without this parameter, GAM might return empty responses for repeated ad breaks within the same session.

`pmxd=[session.avail_duration_ms]`  
The maximum ad pod duration in milliseconds. Use the MediaTailor dynamic variable `[session.avail_duration_ms]` so this value automatically matches the actual SCTE ad marker duration. Do not hardcode this value—if the hardcoded duration is shorter than the actual ad break, the remaining time goes unfilled.

`pmad=-1`  
The maximum number of ads per pod. Set this to `-1` to allow as many ads as available to fill the break, or set it to your desired limit (such as `10`). A low value (such as 4) artificially limits the number of ads that can fill a break, even when more inventory is available.

`vpos`  
The video position (preroll, midroll, or postroll). Set this to the value that matches your actual ad slot type. Do not use `[avail.type]`—MediaTailor does not support this variable and it will resolve to an empty value, which can cause GAM to reject the request or return low-value inventory.

## Player parameters for GAM
<a name="gam-fill-rate-player-params"></a>

Some GAM parameters require values that the publisher or player application provides at session initialization. Pass these to MediaTailor as player parameters and reference them in your ADS template URL. For details on configuring player parameters, see [MediaTailor player variables for ADS requests](variables-player.md).

`ppid=[player_params.ppid]`  
The Programmatic Publisher-Provided Identifier. Provide this publisher-assigned value so that GAM can track sessions and continue returning ads with each ad break. Without this, GAM might stop returning ads after the first break in a session.

`rdid=[player_params.rdid]` (Resettable Device Identifier)  
The device advertising ID. For CTV and Smart TV devices, programmatic ad buyers require this identifier to bid on inventory. Without it, fill rates on CTV devices can be significantly lower.

`msid=[player_params.msid]` (App ID)  
The application identifier. Like `rdid`, this is required by programmatic buyers for CTV and Smart TV device targeting.

For more information about device targeting parameters that GAM supports, see [Google Ad Manager targeting parameters](https://support.google.com/admanager/answer/10678356) on the Google website.

## Common configuration mistakes
<a name="gam-fill-rate-common-mistakes"></a>

The following configuration mistakes are common causes of low fill rates with GAM:
+ **Hardcoded `pmxd`**—Using a fixed value (such as `pmxd=60000`) when actual ad breaks are longer (such as 90 seconds) leaves the remaining time unfilled. Use `[session.avail_duration_ms]` instead.
+ **Low `pmad` value**—Setting the maximum ads per pod too low prevents GAM from filling the full break duration even when inventory is available. Use `-1` for unlimited, or set your desired limit.
+ **Missing `correlator`**—Without this parameter, GAM might return empty VAST responses for repeated ad breaks within the same session.
+ **Missing `ppid`**—Without this player parameter, GAM might stop returning ads after the first ad break in a session.
+ **Missing device ID on CTV devices**—Without `rdid`, programmatic buyers cannot target the device, which significantly reduces fill for CTV inventory.
+ **Using `vpos=[avail.type]`**—MediaTailor does not support the `[avail.type]` variable. This resolves to an empty string, which can cause request failures or low-value ad responses.
+ **Player parameter not passed at session initialization**—Your ADS template URL references a player parameter (such as `[player_params.ppid]`), but the session initialization call does not pass the corresponding value. GAM receives an empty or null value for that macro, which can cause the ad request to return no fill.