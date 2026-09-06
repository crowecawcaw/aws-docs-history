

# Get a list of dialable countries in Connect Customer agent workspace
<a name="3P-apps-voice-requests-listdialablecountries"></a>

 Get a list of `DialableCountry` that contains the country code and calling code that the Connect Customer instance is allowed to make calls to. 

 **Signature** 

```
listDialableCountries(): Promise<DialableCountry[]>
```

 **Usage** 

```
const dialableCountries:DialableCountry[] = await voiceClient.listDialableCountries();
```

 **Output - *DialableCountry*** 


|  **Parameter**  |  **Type**  |  **Description**  | 
| --- | --- | --- | 
|  countryCode  |  string  |  The ISO country code  | 
|  callingCode  |  string  |  The calling code for the country  | 
|  label  |  string  |  The name of the country  | 

 **Permissions required:** 

```
User.Configuration.View      
```