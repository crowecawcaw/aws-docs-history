

# Allow the JCE provider to extract private key secrets out of AWS CloudHSM
<a name="get-encoded-take-out-private-keys"></a>

Use the following steps to allow AWS CloudHSM JCE provider to extract your private key secrets.

**Important**  
This configuration change allows extraction of all `EXTRACTABLE` key bytes in clear from your HSM cluster. For better security, you should consider using [key wrapping methods](java-lib-supported_5.md) to extract the key out of the HSM securely. This prevents unintentional extraction of your key bytes from the HSM. 

1. Use the following commands to enable your **private** or **secret** keys to be extracted in JCE:

------
#### [ Linux ]

   ```
   $ /opt/cloudhsm/bin/configure-jce --enable-clear-key-extraction-in-software
   ```

------
#### [ Windows ]

   ```
   PS C:\> & "C:\Program Files\Amazon\CloudHSM\bin\configure-jce.exe" --enable-clear-key-extraction-in-software
   ```

------

1. Once you enable your clear key extraction, the following methods are enabled for extracting private keys into memory.


<table>
<thead>
  <tr><th>Class</th><th>Method</th><th>Format (getEncoded)</th></tr>
</thead>
<tbody>
  <tr><td>Key</td><td>getEncoded()</td><td>RAW</td></tr>
  <tr><td>ECPrivateKey</td><td>getEncoded()</td><td>PKCS#8</td></tr>
  <tr><td></td><td>getS()</td><td>N/A</td></tr>
  <tr><td>RSAPrivateCrtKey</td><td>getEncoded()</td><td>X.509</td></tr>
  <tr><td></td><td>getPrivateExponent()</td><td>N/A</td></tr>
  <tr><td></td><td>getPrimeP()</td><td>N/A</td></tr>
  <tr><td></td><td>getPrimeQ()</td><td>N/A</td></tr>
  <tr><td></td><td>getPrimeExponentP()</td><td>N/A</td></tr>
  <tr><td></td><td>getPrimeExponentQ()</td><td>N/A</td></tr>
  <tr><td></td><td>getCrtCoefficient()</td><td>N/A</td></tr>
  <tr><td>CloudHsmEdDSAPrivateKey</td><td>getEncoded()</td><td>PKCS#8</td></tr>
  <tr><td>CloudHsmMldsaPrivateKey</td><td>getEncoded()</td><td>N/A</td></tr>
</tbody>
</table>


If you want restore the default behavior and not allow JCE to export keys in clear, run the following command:

------
#### [ Linux ]

```
$ /opt/cloudhsm/bin/configure-jce --disable-clear-key-extraction-in-software
```

------
#### [ Windows ]

```
PS C:\> & "C:\Program Files\Amazon\CloudHSM\bin\configure-jce.exe" --disable-clear-key-extraction-in-software
```

------