# Weights

You can add the _weight_ attribute to an
element. Weight is a positive floating point value that represents
the degree to which the phrase in the item is boosted during speech
recognition. For more information, see
[Weights](https://www.w3.org/TR/speech-grammar/ "https://www.w3.org/TR/speech-grammar/") in
the Speech recognition grammar specification version 1 W3C
recommendation.

Weights must be greater than 0 and less than or equal to 10, and
can have only one decimal place. If the weight is greater than 0 and
less than 1, the phrase is negatively boosted. If the weight is
greater than 1 and less than or equal to 10, the phrase is positively
boosted. A weight of 1 is equivalent to giving no weight at all, and
there is no boosting for the phrase.

Assigning appropriate weights to items for improving speech
recognition performance is a difficult task. Here are some tips you
can follow for assigning weights:

- Start with a grammar without item weights assigned.
- Determine which patterns in the speech are frequently
  misidentified.
- Apply different values for weights until you notice an
  improvement in the speech recognition performance, and there
  are no regressions.
  **Example 1**

For example, if you have a grammar for airports, and you observe
that _New York_ is frequently misidentified as
_Newark_, you can
positively boost New York by assigning it a weight of 5.

```
<rule> id="airport">
    <one-of>
        <item>
            Boston
            <tag>out="Boston"</tag>
        </item>
        <item weight="5">
            New York
            <tag>out="New York"</tag>
        </item>
        <item>
            Newark
            <tag>out="Newark"</tag>
        </item>
    </one-of>
</rule>

```

**Example 2**

For example, you have a grammar for the airline reservation code
starting with an English alphabet followed by three digits. The
reservation code most likely starts with B or D, but you observe that
B is frequently misidentified as P, and D as T. You can positively
boost B and D.

```
<rule> id="alphabet">
    <one-of>
        <item>A<tag>out.letters+='A';</tag></item>
        <item weight="3.5">B<tag>out.letters+='B';</tag></item>
        <item>C<tag>out.letters+='C';</tag></item>
        <item weight="2.9">D<tag>out.letters+='D';</tag></item>
        <item>E<tag>out.letters+='E';</tag></item>
        <item>F<tag>out.letters+='F';</tag></item>
        <item>G<tag>out.letters+='G';</tag></item>
        <item>H<tag>out.letters+='H';</tag></item>
        <item>I<tag>out.letters+='I';</tag></item>
        <item>J<tag>out.letters+='J';</tag></item>
        <item>K<tag>out.letters+='K';</tag></item>
        <item>L<tag>out.letters+='L';</tag></item>
        <item>M<tag>out.letters+='M';</tag></item>
        <item>N<tag>out.letters+='N';</tag></item>
        <item>O<tag>out.letters+='O';</tag></item>
        <item>P<tag>out.letters+='P';</tag></item>
        <item>Q<tag>out.letters+='Q';</tag></item>
        <item>R<tag>out.letters+='R';</tag></item>
        <item>S<tag>out.letters+='S';</tag></item>
        <item>T<tag>out.letters+='T';</tag></item>
        <item>U<tag>out.letters+='U';</tag></item>
        <item>V<tag>out.letters+='V';</tag></item>
        <item>W<tag>out.letters+='W';</tag></item>
        <item>X<tag>out.letters+='X';</tag></item>
        <item>Y<tag>out.letters+='Y';</tag></item>
        <item>Z<tag>out.letters+='Z';</tag></item>
    </one-of>
</rule>

```
