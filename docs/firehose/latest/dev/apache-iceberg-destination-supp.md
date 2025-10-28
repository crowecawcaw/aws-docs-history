# Understand supported data

types

Firehose supports all the primitive and complex data types that Apache Iceberg supports.
For more information, see [Schemas and Data
Types](https://iceberg.apache.org/spec/#schemas-and-data-types "https://iceberg.apache.org/spec/#schemas-and-data-types"). When sending binary data as a string, you must use Firehose supported
encoding types - Basic Base64, MIME Base64, URL and filename safe Base64, and Hex. For
Timestamp data types, you must always send in microseconds.

## Data types examples

The following section shows examples of different data types.

**MapType**

```
{
    "destination_column_0": {"WP5o0JOkuIQcDPcsvpJJygF1xzaOSq0wUlgTwuIeCEzgVneGxA":"PO3ReF3auyDqbfonx9Cd8NTmcQnqnw7JuZOCWwI1jqgQKpsdMASWuU9rzb98Nm0WQe6l7i8TTEgH5gpqohIaQ58xwquYYho3ephkXfCgLryWdAhcyNcKf5SR8Xc5iv1SSsucXDqSoEceYiHTN6","eJbYbzmmasbNjun5WQhDgW81WJBQJWY0XwcNmgUn2qj2f7X5VWVAwnH1u3DzuglPicBOKLAWesjLXciJJYMn3E3vE7FgUZCAeo6Haf7":"XLnTauZzUiesOCv1kcI8QgO3eH0zEkiJiaExywuNoVk1feh4FpTL","vgHzvjlfqXG6gVnvKqMu18YiOvEqixeoK3DhcGafkkVfE9MVSDHBhc9L2OsF5dIasTWhKYYQnZrzxro3Fc1bzgKm1UHiYRrtg5eKHTJUW4fC8qR65Y73HynS0hRNfdD0miQi4jaENTrnona348iIjiVL9mvYR":"VsVIcn1RAEWYyIRH2iOPzIBzZBWJYjjcPGOlRt6PfE0Gt97dfkOZ7MpNNXTtJ1g3AUHoAvpo6asfWDKELcHmZEgu5eo8fga","8UjOp19MIgfe1DMzIWbE44":"CtenADor4MMiZfRq6eN0LLKEcsn5qVHLsQrBsHjqocb1dIUZ8fk1Bo2YIzT0rcPxx0LAbzOHx","8FSZWB13VL9csnpX7RAcajIlUcnO7vH8qjkaVMYFD3uS0QlJ5gQL63DLih7Mh6TwVOhWbrTAEK4zffn5iyWKhYqslG79UiRn9A35zdYeLt6rJUS71Yu9HWybxhoYBRwX0wCd9YjJAiTKxNunvKTEyqgEM2BcavcAT5RENSa819Y3nDGhdekmdhkUP1J6tcsEGio3":"liMdGIy12FC5iGlETX1pkfQZr6BrTAI7nvzlQUd7xELs2JVSXUGG9OmY3EFPvQ8IS7h4vyJikvTgczun6JMrq6Cw6Xs083FUh9LQpXfQCBXafhBCPIWwLtRX5ilMf8ZJ6ndJTDiFCrhXuFPC","2puYqZivt4CrkeLsmcuPw38oUkEUnpXrXfK1e9WafRJqN3pR1rakR2RFq5jyQcYkQXnOjdQi2cxthoSnA":"icdnS1DMLt950mwURyUR8tENXk3vJgGmTabJHmIuRSyoWHY7LbyGnRN8U1lQyOTRPCxkE7zKrSFOe13Jo1dlWDClVrxUUrrYb2Hc61zmbCagXcfp5FQhqDL5gMeK4wW32g","ZtTLkLZBcUdem2bBu4F7ngM3JxG8CLyRwdVxXMhPB0zeBEnGVRxUqjmwZIZ4H3e":"rrF4n8bPvzkUhslj2kGDodvpoGGswlOhDaCnLGW0cq3FNbDFj1PAn95VHiUul5d8tmt8kmA0Rgr24dT70vPfERpVHPlXcyXTg8o","0lipyfJwb45pGxet5rggbUoWByZdmRvuSJyPGdhZz2IjPNr5pkGUuc0beVwiwgIu2dNXRJFT25xz8dYP67fasdzkNsxqfWFmOjZvW5b":"V4qDnpR9ZgYflvGnIiScYnzsrDW797UGDMZjEg0nIrkmRrnc6FYXPlm0aiUBXuK6ZGNsfRmEl0kw6GHuUtYMUCcWIfwUo5wK8n0s3KTzMGOPsjl5MTaA8HWqUIMc3q3JlIZOXAFAENj7EtduzPpHBKRHWDbtmjjGtSsx8GNmZ108Gv43J92Q5G","qbgztJdIywmuKauxGnmRBSKMVmtyreab6dITzul47t2QiIQ5fEXQ4J5OonT5":"6JB70Wd1rwxBQR36b5MqMgXHr7TYZSLJ9xTIHFCSkknxcuvmbot6xEkTv9ijtoLEQrxr9fwI8wsMCXsSYV7j3Fs4VPH8loyZMtYYbtUbuljLHjwJye1hlMeiLy","jwy5FY9Mi0vAo5w6l7tRM2Q4sKGaT9s":"5m4glPW6k7fm3zPYT2hVR1MfraLG8TEGPCUemRqC36KHbLoNCxLjGfaYLAI2CeE4IuMa1WIlrsXvPgVIvH7LSQED7uQfedVN4KZavMQycBqJrYkZpHdMO9JaMSo5N4ncNuvs0pgLLSketqdW8qUOjZvdnMTLcZpJFioQGVGL7HCWvWm4qxhKjHOxi0zua2hROLnMkK","HNGNf2jAaR6A07QHxF6KY0Ce4wITpCKQNTlkHWDqAm48ocUjWaTRmc8jBGN0Gs8iZalJiTLzJrquHVThx":"QneTrdTPwtT3sEuRc1KdYZNsfrDTBeKX3tPNovIB7ZTuQGbgtf70mIvGnt8vmdDyDKleDdF9WjESkAsz42PpJHpqYtwqwJbUbB47VfSMF4sNJRPo0eaZceqzDyHHNu6xJs","oKEKH0tyt2o42iXQffNvKrhkZHS6bqcqGIkSCMxrTbgRWl0sTiCpPzfkoY1XwMBRxAYuYRimZ3W5nM58clYiOxL2oVYdA2":"9FsQsrpJKN","bekToN5OdByhB9DRS7wb5daFxDI6KGBHSecKzl6n5UEjxaAp4dO0KTXlzzflR7YRrPDrR3pQAiy7Y1tYry":"dcwHnwApWtoZWtwzI1Syv6ak0XZPMmk7Tyq1pi3qB0axsPyRJztmjYslzW07muyAMiRIzX2SfMulhTAtjoHahwb6xLLdTrL9FfQvR"},
    "destination_column_1": "{\"{\\\"destination_nested_column_0\\\": \\\"18:56:14.974\\\", \\\"destination_nested_column_1\\\": 241.86246}\":\"M07kAvYdHvBh61F7RzfxtEd39YQI33LnM2NbGS67DOFFsRUyUUujKT5VnK7Wtfz1mHNeIix6FAY9cYpwTdedgr9XnFwG0BHMO51LZPYXerDqAUmqhldyKUvxy1KMQkU\",\"{\\\"destination_nested_column_0\\\": \\\"18:56:14.974\\\", \\\"destination_nested_column_1\\\": 562.56384}\":\"9GlxhDCt95LxBo51HybBZihqOqf6EU8jrDu7NMpxtGB2dY6q6kXpvxIrFuMdqHCJKIZIcDikwggLniUm8kgE4d\",\"{\\\"destination_nested_column_0\\\": \\\"18:56:14.974\\\", \\\"destination_nested_column_1\\\": 496.03268}\":\"keTJZYLNvLRB50DMKzEI6M0AM4mueyNnA1m2YVnYdDwyxUpPqkb72Q6LiX0B9s8gCjZ6trW6C1PFk9KNBIpxYsj5Tc5Xsl13go3qLqFRwsFiW7peHp6xBJ7NcJm4RxSbIDEnTr1FLpmnKC18VZeY\",\"{\\\"destination_nested_column_0\\\": \\\"18:56:14.974\\\", \\\"destination_nested_column_1\\\": 559.0878}\":\"mG0ZET84BUF28E312UCIWgmypyQFSUODH9NAMAnF3LJEutbooZWcBt97PP5AHaopNvC8pQZ4mGXB9hmVmjUNmuj5QanyxXrKtCU8uivE3R8jPx3jur0iepx9ckgbHF7J13lDCXW92a\",\"{\\\"destination_nested_column_0\\\": \\\"18:56:14.974\\\", \\\"destination_nested_column_1\\\": 106.845245}\":\"aidoVYrzu8gcLRkVVUyTKCN9gqTUFYi8uJQsrXEFEYl1f9ool7JhAtg9QKG5BBu67Ngb95ENsNKQyCHNImSu5x4hMnmHUB6qRkfOsk9BzTqkM\"}"
}
```

**DecimalType**

```
{
    "destination_column_0": 9455262425851.1342772,
    "destination_column_1": "9455262425851.1342772",
    "destination_column_2": 9455262425852
}
```

**BinaryType (base64-default, base64-mime, base64-url-safe,
hex)**

```
{
    "destination_column_0": "AsYhnHD\/Ra54hITl1daNV9glOjtWPEfopH+PjgUKHYB6K7UcYi4K19b80wD4J\/93x5tyh+0y+k5cMljVRlmfIkIuLxl9ERBiPPLhf4+yoJ2k70VavPnYWmNLs1hLDHlfeEMIfVhrqOGzJMoA+CBAWXfIuiG420JSQP5iAx5xFG\/mOfkM5zYothje8OGXltdthcCL6WYBiP0SlwXcE0uMeRfwclAc9fTOBz6RzdJlHhUDjoAXg+4cvly27F82XpuGMNwpUj98AOrgbh2MoU9yvsM9ZrjD0eGVgOZP8Ky7Za4oE\/oK8j+qABF6XV712iA6pVtTNJFvX6Ey3ssNYvno+LYF5ZsySs2rB5AbVM73RfOPqdS\/c\/r3MEqoEqt+nPx6eGam4WSA+0swztt7aLdrlX6yK7xJeIJ0rTlIDBo0ZUaw011ykY\/8Bvy+4byoPlmr4Z5yhN1z3ZTOkx7eDR6xMv+vDVsDBtItVazDwHgDy41r\/hQNeNedPKrozc8TY9k7wZre\/6V2lCa3BmT8Uu9b9ydjR9z+fCSdG+VRv35nz5kdqdKy8YIrynYs4eOcjh8jH3UwVYrYQcnWkBAfF7Xk9CoPVnL3ciHZtyiZOaTGIj9rO0xX\/W5dGe9\/4YChs6LbD584kxLTxvHgSl4vadaTGNKci3SvNmZNsz8ducxtNXF\/Tv2DUub465hzgpaLPur3+MB+kfdN2YXUfqb+xJAgxThWfUe151nrH0EPow9lgSlp21rUBGznJAvPRl1ExGIAuc7JYAoUrJUkx5Hfl6PekPDhqt7+yJwCB8qxhTTryxo+bjtai4ndRCGcuCaxT8KkOcXsS37urd3YGSDMinZdMNVc646s25415qK6nBRlqqAY8+EYmcUIVB9XcNdke4zoUfhVQoruwidzDU\/kFafoulo5DEoMOyaH1N2HCSxG5tZXNQocSZPaY8efZYMCpmDXsPAzkmgSkYRDSu\/r3wUqROa2tGK5\/pQY24v+Jq0U\/jQ99GShlU283nZ85ot2ocbtMAgD\/WsrSEh6lNt9RaI3HfA7\/HcH\/fgr9jsTtxDgZhabTBwwDwX0zjWGx1bCuTLKBN7byxg9ZvAVgqwPS4HERLer5T5UkKf74zn9Eq3HYH1Q5JpyDUx+im7mte1sprf1+A24kksVU\/MD9aP9N8\/QDsQ13gkhOn5KwFMz3BC2Vw5gL+gGNHFKDRL6wGIfhuYcx9LucolZ1yNy9Gbb3ioWSSufyFpyXqtndDLPI5QS1SJpJm2KDyqcH1SmRLIhd9MNRUC73EAEm+NO5wxPzBRSjhCHZpf8SrYITWJl7K3XzGOfPFh2NgES3jMP9cvSXO6yyICcep2HBYGbFflni89+Rw==",
    "destination_column_1": "AsYhnHD\/Ra54hITl1daNV9glOjtWPEfopH+PjgUKHYB6K7UcYi4K19b80wD4J\/93x5tyh+0y+k5c\r\nMljVRlmfIkIuLxl9ERBiPPLhf4+yoJ2k70VavPnYWmNLs1hLDHlfeEMIfVhrqOGzJMoA+CBAWXfI\r\nuiG420JSQP5iAx5xFG\/mOfkM5zYothje8OGXltdthcCL6WYBiP0SlwXcE0uMeRfwclAc9fTOBz6R\r\nzdJlHhUDjoAXg+4cvly27F82XpuGMNwpUj98AOrgbh2MoU9yvsM9ZrjD0eGVgOZP8Ky7Za4oE\/oK\r\n8j+qABF6XV712iA6pVtTNJFvX6Ey3ssNYvno+LYF5ZsySs2rB5AbVM73RfOPqdS\/c\/r3MEqoEqt+\r\nnPx6eGam4WSA+0swztt7aLdrlX6yK7xJeIJ0rTlIDBo0ZUaw011ykY\/8Bvy+4byoPlmr4Z5yhN1z\r\n3ZTOkx7eDR6xMv+vDVsDBtItVazDwHgDy41r\/hQNeNedPKrozc8TY9k7wZre\/6V2lCa3BmT8Uu9b\r\n9ydjR9z+fCSdG+VRv35nz5kdqdKy8YIrynYs4eOcjh8jH3UwVYrYQcnWkBAfF7Xk9CoPVnL3ciHZ\r\ntyiZOaTGIj9rO0xX\/W5dGe9\/4YChs6LbD584kxLTxvHgSl4vadaTGNKci3SvNmZNsz8ducxtNXF\/\r\nTv2DUub465hzgpaLPur3+MB+kfdN2YXUfqb+xJAgxThWfUe151nrH0EPow9lgSlp21rUBGznJAvP\r\nRl1ExGIAuc7JYAoUrJUkx5Hfl6PekPDhqt7+yJwCB8qxhTTryxo+bjtai4ndRCGcuCaxT8KkOcXs\r\nS37urd3YGSDMinZdMNVc646s25415qK6nBRlqqAY8+EYmcUIVB9XcNdke4zoUfhVQoruwidzDU\/k\r\nFafoulo5DEoMOyaH1N2HCSxG5tZXNQocSZPaY8efZYMCpmDXsPAzkmgSkYRDSu\/r3wUqROa2tGK5\r\n\/pQY24v+Jq0U\/jQ99GShlU283nZ85ot2ocbtMAgD\/WsrSEh6lNt9RaI3HfA7\/HcH\/fgr9jsTtxDg\r\nZhabTBwwDwX0zjWGx1bCuTLKBN7byxg9ZvAVgqwPS4HERLer5T5UkKf74zn9Eq3HYH1Q5JpyDUx+\r\nim7mte1sprf1+A24kksVU\/MD9aP9N8\/QDsQ13gkhOn5KwFMz3BC2Vw5gL+gGNHFKDRL6wGIfhuYc\r\nx9LucolZ1yNy9Gbb3ioWSSufyFpyXqtndDLPI5QS1SJpJm2KDyqcH1SmRLIhd9MNRUC73EAEm+NO\r\n5wxPzBRSjhCHZpf8SrYITWJl7K3XzGOfPFh2NgES3jMP9cvSXO6yyICcep2HBYGbFflni89+Rw==",
    "destination_column_2": "AsYhnHD_Ra54hITl1daNV9glOjtWPEfopH-PjgUKHYB6K7UcYi4K19b80wD4J_93x5tyh-0y-k5cMljVRlmfIkIuLxl9ERBiPPLhf4-yoJ2k70VavPnYWmNLs1hLDHlfeEMIfVhrqOGzJMoA-CBAWXfIuiG420JSQP5iAx5xFG_mOfkM5zYothje8OGXltdthcCL6WYBiP0SlwXcE0uMeRfwclAc9fTOBz6RzdJlHhUDjoAXg-4cvly27F82XpuGMNwpUj98AOrgbh2MoU9yvsM9ZrjD0eGVgOZP8Ky7Za4oE_oK8j-qABF6XV712iA6pVtTNJFvX6Ey3ssNYvno-LYF5ZsySs2rB5AbVM73RfOPqdS_c_r3MEqoEqt-nPx6eGam4WSA-0swztt7aLdrlX6yK7xJeIJ0rTlIDBo0ZUaw011ykY_8Bvy-4byoPlmr4Z5yhN1z3ZTOkx7eDR6xMv-vDVsDBtItVazDwHgDy41r_hQNeNedPKrozc8TY9k7wZre_6V2lCa3BmT8Uu9b9ydjR9z-fCSdG-VRv35nz5kdqdKy8YIrynYs4eOcjh8jH3UwVYrYQcnWkBAfF7Xk9CoPVnL3ciHZtyiZOaTGIj9rO0xX_W5dGe9_4YChs6LbD584kxLTxvHgSl4vadaTGNKci3SvNmZNsz8ducxtNXF_Tv2DUub465hzgpaLPur3-MB-kfdN2YXUfqb-xJAgxThWfUe151nrH0EPow9lgSlp21rUBGznJAvPRl1ExGIAuc7JYAoUrJUkx5Hfl6PekPDhqt7-yJwCB8qxhTTryxo-bjtai4ndRCGcuCaxT8KkOcXsS37urd3YGSDMinZdMNVc646s25415qK6nBRlqqAY8-EYmcUIVB9XcNdke4zoUfhVQoruwidzDU_kFafoulo5DEoMOyaH1N2HCSxG5tZXNQocSZPaY8efZYMCpmDXsPAzkmgSkYRDSu_r3wUqROa2tGK5_pQY24v-Jq0U_jQ99GShlU283nZ85ot2ocbtMAgD_WsrSEh6lNt9RaI3HfA7_HcH_fgr9jsTtxDgZhabTBwwDwX0zjWGx1bCuTLKBN7byxg9ZvAVgqwPS4HERLer5T5UkKf74zn9Eq3HYH1Q5JpyDUx-im7mte1sprf1-A24kksVU_MD9aP9N8_QDsQ13gkhOn5KwFMz3BC2Vw5gL-gGNHFKDRL6wGIfhuYcx9LucolZ1yNy9Gbb3ioWSSufyFpyXqtndDLPI5QS1SJpJm2KDyqcH1SmRLIhd9MNRUC73EAEm-NO5wxPzBRSjhCHZpf8SrYITWJl7K3XzGOfPFh2NgES3jMP9cvSXO6yyICcep2HBYGbFflni89-Rw==",
    "destination_column_3": "02c6219c70ff45ae788484e5d5d68d57d8253a3b563c47e8a47f8f8e050a1d807a2bb51c622e0ad7d6fcd300f827ff77c79b7287ed32fa4e5c3258d546599f22422e2f197d1110623cf2e17f8fb2a09da4ef455abcf9d85a634bb3584b0c795f7843087d586ba8e1b324ca00f820405977c8ba21b8db425240fe62031e71146fe639f90ce73628b618def0e19796d76d85c08be9660188fd129705dc134b8c7917f072501cf5f4ce073e91cdd2651e15038e801783ee1cbe5cb6ec5f365e9b8630dc29523f7c00eae06e1d8ca14f72bec33d66b8c3d1e19580e64ff0acbb65ae2813fa0af23faa00117a5d5ef5da203aa55b5334916f5fa132decb0d62f9e8f8b605e59b324acdab07901b54cef745f38fa9d4bf73faf7304aa812ab7e9cfc7a7866a6e16480fb4b30cedb7b68b76b957eb22bbc49788274ad39480c1a346546b0d35d72918ffc06fcbee1bca83e59abe19e7284dd73dd94ce931ede0d1eb132ffaf0d5b0306d22d55acc3c07803cb8d6bfe140d78d79d3caae8cdcf1363d93bc19adeffa5769426b70664fc52ef5bf7276347dcfe7c249d1be551bf7e67cf991da9d2b2f1822bca762ce1e39c8e1f231f7530558ad841c9d690101f17b5e4f42a0f5672f77221d9b7289939a4c6223f6b3b4c57fd6e5d19ef7fe180a1b3a2db0f9f389312d3c6f1e04a5e2f69d69318d29c8b74af36664db33f1db9cc6d35717f4efd8352e6f8eb987382968b3eeaf7f8c07e91f74dd985d47ea6fec49020c538567d47b5e759eb1f410fa30f65812969db5ad4046ce7240bcf465d44c46200b9cec9600a14ac9524c791df97a3de90f0e1aadefec89c0207cab18534ebcb1a3e6e3b5a8b89dd44219cb826b14fc2a439c5ec4b7eeeadddd81920cc8a765d30d55ceb8eacdb9e35e6a2ba9c1465aaa018f3e11899c508541f5770d7647b8ce851f855428aeec227730d4fe415a7e8ba5a390c4a0c3b2687d4dd87092c46e6d657350a1c4993da63c79f658302a660d7b0f0339268129184434aefebdf052a44e6b6b462b9fe9418db8bfe26ad14fe343df464a1954dbcde767ce68b76a1c6ed300803fd6b2b48487a94db7d45a2371df03bfc7707fdf82bf63b13b710e066169b4c1c300f05f4ce3586c756c2b932ca04dedbcb183d66f01582ac0f4b81c444b7abe53e5490a7fbe339fd12adc7607d50e49a720d4c7e8a6ee6b5ed6ca6b7f5f80db8924b1553f303f5a3fd37cfd00ec435de09213a7e4ac05333dc10b6570e602fe80634714a0d12fac0621f86e61cc7d2ee728959d72372f466dbde2a16492b9fc85a725eab677432cf239412d52269266d8a0f2a9c1f54a644b22177d30d4540bbdc40049be34ee70c4fcc14528e10876697fc4ab6084d6265ecadd7cc639f3c5876360112de330ff5cbd25ceeb2c8809c7a9d8705819b15f9678bcf7e47"
}
```

**TimeType (Epoch in Microseconds, LocalTime Java
Object)**

```
{
    "destination_column_0": 68175096000,
    "destination_column_1": "18:56:15.096"
}
```

**TimestampType.withZone (Epoch in Microseconds,
OffsetDateTime Java Object, LocalDateTime Java Object)**

```
{
    "destination_column_0": 1725476175099000,
    "destination_column_1": "2024-09-04T18:56:15.099Z",
    "destination_column_2": "2024-09-04T18:56:15.099"
}
```

**DoubleType**

```
{
    "destination_column_0": 9.18477568715142,
    "destination_column_1": "9.18477568715142"
}
```

**BooleanType**

```
{
    "destination_column_0": true,
    "destination_column_1": "false",
    "destination_column_2": 1,
    "destination_column_3": 0
}
```

**FloatType**

```
{
    "destination_column_0": 0.6242226,
    "destination_column_1": "0.6242226"
}
```

**IntegerType**

```
{
    "destination_column_0": 7,
    "destination_column_1": "7"
}
```

**TimestampType.withoutZone (Epoch in Microseconds,
LocalDateTime Java Object, OffsetDateTime Java Object, ZonedDateTime Java
Object)**

```
{
    "destination_column_0": 1725476175114000,
    "destination_column_1": "2024-09-04T18:56:15.114",
    "destination_column_2": "2024-09-04T18:56:15.114Z",
    "destination_column_3": "2024-09-04T18:56:15.114-07:00"
}
```

**DateType**

```
{
    "destination_column_0": 19970,
    "destination_column_1": "2024-09-04"
}
```

**LongType**

```
{
    "destination_column_0": 8,
    "destination_column_1": "8"
}
```

**UUIDType (UUID Java Object)**

```
{
    "destination_column_0": "21c5521c-a6d4-48d4-b2c8-7f6d842f72c3"
}
```

**ListType**

```
{
    "destination_column_0": ["s1FSrgb0lGDxfn2iYT0EtlP47aHSjwmLZgrdr1JqRs0dmbeCcQoaLr4Xhi2KIVvmus9ppFdpWIcOHnJ0omhAPhXH0ynsaicCqnpQ8VAYp4bBPDgangwz9KOz60d0qSqCFxwEhoXjV4AouN5mwW","VUYtsT1pcw8q5WBxOiL47IZqea4fFloZwV7iJanDrvqK6AGa1yBuQyqd6R0axrcz8wcGBP","blsmImCYglNKNBcThVuKGeLOmKJdX19pRMR08ayc1EXN2rP7dIRfbhkk76XgAR3IsIwpB0jiQG8PW40PSlzn4sxUMN5wwQgyxmkZbk3e0dW0uqwVIm7KFkOPEHNmqgw01cT9KKMBwXkOGUmtX1","1234567890abcdef0","2234567890abcdef0"],
    "destination_column_1": "[{\"destination_nested_column_0\":\"bb00f8e6-db82-4241-a5c5-0d9c0d2f71a4\",\"destination_nested_column_1\":907.35345},{\"destination_nested_column_0\":\"2c77b702-d405-4fe1-beee-fb541d7ab833\",\"destination_nested_column_1\":544.0026},{\"destination_nested_column_0\":\"68389200-d6b1-413d-bcd9-fdb931708395\",\"destination_nested_column_1\":153.683},{\"destination_nested_column_0\":\"bc31cbaa-39cd-4e2f-b357-9ea9ce75532b\",\"destination_nested_column_1\":977.5165},{\"destination_nested_column_0\":\"b7d627f9-0d5b-41b7-903a-525488259fba\",\"destination_nested_column_1\":434.17215},{\"destination_nested_column_0\":\"06b6ec1e-1952-4582-b285-46aaf40064b8\",\"destination_nested_column_1\":580.33124},{\"destination_nested_column_0\":\"f04b3bbf-61ad-4c5c-8740-6f666f57c431\",\"destination_nested_column_1\":550.75793}]"
}
```
