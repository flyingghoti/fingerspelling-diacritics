# fingerspelling-diacritics
A dictionary for the Plover stenography application that allows for fingerspelling of non-ASCII characters.

Basic usage: write a letter using standard fingerspelling rules, then add a second stroke to add the appropriate diacritic. For example, if you suddenly find yourself needing to write about the Polish city of Łódź, and you don't already have that in your dictionary, you can fingerspell it: `HR*P/STROEBG/O*/KAOUT/D*/STKPW*/KAOUT` (i.e. "L with stroke, o with acute, d, z with acute"). And thanks to combining diacritics, you can even write "Spın̈al Tap" correctly even though there's no Unicode character for "n̈": just stroke `TPH*/TKOTS`.

Available diacritics:
* Acute accents - á: `KAOUT`
* Double acute - ő: `KAOUTS`
* Breve - ă: `PWREF`
* Caron - ǎ: `KARPB`
* Cedilla - ç: `SELD`
* Circumflex - â: `SEURBG`
* Dot - ȧ: `TKOT`
* Double dots (i.e. diaeresis or umlaut) - ä: `TKOTS`
* Dotless ı or ȷ: `TKOLT`
* Grave accents - à: `TKPWRAEUF`
* Double grave - ȁ: `TKPWRAEUFS`
* Macron - ā: `PHABG`
* Ogonek - ą: `OPBG`
* Ring - å: `REUPBG`
* Stroke - ł: `STROEBG`
* Tilde - ã: `TEULD`

There are also several special non-English letters included:
* E ligatures - a → æ or o → œ: `A*/ELG` or `O*/ELG`
* Schwa - e → ə: `*E/SWHA`
* Sharp S/Eszett - s → ß: `S*/SHARP`
* Long S - s → ſ: `S*/HROPBG`
* Fricativization: d → ð or t → þ: `TK*/TPREUBG` or `T*/TPREUBG`
* Velarization: n → ŋ: `TPH*/SRAOEL`

This dictionary cannot handle words with multiple diacritics, such as ǡ, because that would be a significant amount of additional work for characters I personally will never use. (95% of this dictionary is already stuff I'll never use, tbh; I just needed a way to write the occasional ñ or ü and figured I may as well be systematic about it.) This is a first draft; feedback is welcome.
