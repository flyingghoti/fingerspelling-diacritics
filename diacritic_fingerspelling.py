LONGEST_KEY = 2

fingerspelledLetters = {
    "A*": "a",
    "PW*": "b",
    "KR*": "c",
    "TK*": "d",
    "*E": "e",
    "SK*": "e",  # left hand stroke for E
    "TP*": "f",
    "TKPW*": "g",
    "H*": "h",
    "*EU": "i",
    "SKW*": "i",  # left hand stroke for I
    "SKWR*": "j",
    "K*": "k",
    "HR*": "l",
    "PH*": "m",
    "TPH*": "n",
    "O*": "o",
    "P*": "p",
    "KW*": "q",
    "R*": "r",
    "S*": "s",
    "T*": "t",
    "*U": "u",
    "WR*": "u",  # left hand stroke for U
    "SR*": "v",
    "W*": "w",
    "KP*": "x",
    "KWH*": "y",
    "STK*": "z",  # simpler stroke for Z
    "STKPW*": "z",
    "A*P": "A",
    "PW*P": "B",
    "KR*P": "C",
    "TK*P": "D",
    "*EP": "E",
    "SK*P": "E",  # left hand stroke for E
    "TP*P": "F",
    "TKPW*P": "G",
    "H*P": "H",
    "*EUP": "I",
    "SKW*P": "I",  # left hand stroke for I
    "SKWR*P": "J",
    "K*P": "K",
    "HR*P": "L",
    "PH*P": "M",
    "TPH*P": "N",
    "O*P": "O",
    "P*P": "P",
    "KW*P": "Q",
    "R*P": "R",
    "S*P": "S",
    "T*P": "T",
    "*UP": "U",
    "WR*P": "U",  # left hand stroke for U
    "SR*P": "V",
    "W*P": "W",
    "KP*P": "X",
    "KWH*P": "Y",
    "STK*P": "Z",  # simpler stroke for Z
    "STKPW*P": "Z"
    }

diacritics = {
    # ACUTE
    "KAOUT": {
        "a": "á",
        "c": "ć",
        "e": "é",
        "i": "í",
        "l": "ĺ",
        "n": "ń",
        "o": "ó",
        "r": "ŕ",
        "s": "ś",
        "u": "ú",
        "y": "ý",
        "z": "ź",
        "A": "Á",
        "C": "Ć",
        "E": "É",
        "I": "Í",
        "L": "Ĺ",
        "N": "Ń",
        "O": "Ó",
        "R": "Ŕ",
        "S": "Ś",
        "U": "Ú",
        "Y": "Ý",
        "Z": "Ź",
        "default": "X́"
    },
    # BREVE
    "PWREF": {
        "a": "ă",
        "e": "ĕ",
        "g": "ğ",
        "i": "ĭ",
        "o": "ŏ",
        "u": "ŭ",
        "A": "Ă",
        "E": "Ĕ",
        "G": "Ğ",
        "I": "Ĭ",
        "O": "Ŏ",
        "U": "Ŭ",
        "default": "X̆"
    },
    # CARON
    "KARPB": {
        "a": "ǎ",
        "c": "č",
        "d": "ď",
        "e": "ě",
        "g": "ǧ",
        "h": "ȟ",
        "i": "ǐ",
        "j": "ǰ",
        "k": "ǩ",
        "l": "ľ",
        "n": "ň",
        "o": "ǒ",
        "r": "ř",
        "s": "š",
        "t": "ť",
        "u": "ǔ",
        "z": "ž",
        "A": "Ǎ",
        "C": "Č",
        "D": "Ď",
        "E": "Ě",
        "G": "Ǧ",
        "H": "Ȟ",
        "I": "Ǐ",
        "J": "J̌",
        "K": "Ǩ",
        "L": "Ľ",
        "N": "Ň",
        "O": "Ǒ",
        "R": "Ř",
        "S": "Š",
        "T": "Ť",
        "U": "Ǔ",
        "Z": "Ž",
        "default": "X̌"
    },
    # CEDILLA
    "SELD": {
        "c": "ç",
        "d": "ḑ",
        "e": "ȩ",
        "g": "ģ",
        "h": "ḩ",
        "k": "ķ",
        "l": "ļ",
        "n": "ņ",
        "r": "ŗ",
        "s": "ş",
        "t": "ţ",
        "C": "Ç",
        "D": "Ḑ",
        "E": "Ȩ",
        "G": "Ģ",
        "H": "Ḩ",
        "K": "Ķ",
        "L": "Ļ",
        "N": "Ņ",
        "R": "Ŗ",
        "S": "Ş",
        "T": "Ţ",
        "default": "X̧"
    },
    # CIRCUMFLEX
    "SEURBG": {
        "a": "â",
        "c": "ĉ",
        "e": "ê",
        "g": "ĝ",
        "h": "ĥ",
        "i": "î",
        "j": "ĵ",
        "o": "ô",
        "s": "ŝ",
        "u": "û",
        "w": "ŵ",
        "y": "ŷ",
        "z": "ẑ",
        "A": "Â",
        "C": "Ĉ",
        "E": "Ê",
        "G": "Ĝ",
        "H": "Ĥ",
        "I": "Î",
        "J": "Ĵ",
        "O": "Ô",
        "S": "Ŝ",
        "U": "Û",
        "W": "Ŵ",
        "Y": "Ŷ",
        "Z": "Ẑ",
        "default": "X̂"
    },
    # DOT
    "TKOT": {
        "a": "ȧ",
        "b": "ḃ",
        "c": "ċ",
        "d": "ḋ",
        "e": "ė",
        "f": "ḟ",
        "g": "ġ",
        "h": "ḣ",
        "l": "ŀ",
        "m": "ṁ",
        "n": "ṅ",
        "o": "ȯ",
        "p": "ṗ",
        "r": "ṙ",
        "s": "ṡ",
        "t": "ṫ",
        "w": "ẇ",
        "x": "ẋ",
        "y": "ẏ",
        "z": "ż",
        "A": "Ȧ",
        "B": "Ḃ",
        "C": "Ċ",
        "D": "Ḋ",
        "E": "Ė",
        "F": "Ḟ",
        "G": "Ġ",
        "H": "Ḣ",
        "I": "İ",
        "L": "Ŀ",
        "M": "Ṁ",
        "N": "Ṅ",
        "O": "Ȯ",
        "P": "Ṗ",
        "R": "Ṙ",
        "S": "Ṡ",
        "T": "Ṫ",
        "W": "Ẇ",
        "X": "Ẋ",
        "Y": "Ẏ",
        "Z": "Ż",
        "default": "Ẋ"
    },
    # DOTLESS
    "TKOLT": {
        "i": "ı",
        "j": "ȷ"
    },
    # DOUBLE ACUTE
    "KAOUTS": {
        "o": "ő",
        "u": "ű",
        "O": "Ő",
        "U": "Ű",
        "default": "X̋"
    },
    # DOUBLE DOTS (aka diaeresis/umlaut)
    "TKOTS": {
        "a": "ä",
        "e": "ë",
        "i": "ï",
        "h": "ḧ",
        "o": "ö",
        "t": "ẗ",
        "u": "ü",
        "w": "ẅ",
        "x": "ẍ",
        "y": "ÿ",
        "A": "Ä",
        "E": "Ë",
        "I": "Ï",
        "H": "Ḧ",
        "O": "Ö",
        "U": "Ü",
        "W": "Ẅ",
        "X": "Ẍ",
        "Y": "Ÿ",
        "default": "Ẍ"
    },
    # DOUBLE GRAVE
    "TKPWRAEUFS": {
        "a": "ȁ",
        "e": "ȅ",
        "i": "ȉ",
        "o": "ȍ",
        "r": "ȑ",
        "u": "ȕ",
        "A": "Ȁ",
        "E": "Ȅ",
        "I": "Ȉ",
        "O": "Ȍ",
        "R": "Ȑ",
        "U": "Ȕ",
        "default": "X̏"
    },
    # GRAVE
    "TKPWRAEUF": {
        "a": "à",
        "e": "è",
        "i": "ì",
        "n": "ǹ",
        "o": "ò",
        "u": "ù",
        "w": "ẁ",
        "y": "ỳ",
        "A": "À",
        "E": "È",
        "I": "Ì",
        "N": "Ǹ",
        "O": "Ò",
        "U": "Ù",
        "W": "Ẁ",
        "Y": "Ỳ",
        "default": "X̀"
    },
    # MACRON
    "PHABG": {
        "a": "ā",
        "e": "ē",
        "g": "ḡ",
        "i": "ī",
        "o": "ō",
        "u": "ū",
        "y": "ȳ",
        "A": "Ā",
        "E": "Ē",
        "G": "Ḡ",
        "I": "Ī",
        "O": "Ō",
        "U": "Ū",
        "Y": "Ȳ",
        "default": "X̄"
    },
    # OGONEK
    "OPBG": {
        "a": "ą",
        "e": "ę",
        "i": "į",
        "o": "ǫ",
        "u": "ų",
        "default": "X̨"
    },
    # RING
    "REUPBG": {
        "a": "å",
        "u": "ů",
        "w": "ẘ",
        "y": "ẙ",
        "A": "Å",
        "U": "Ů",
        "default": "X̊"
    },
    # STROKE
    "STROEBG": {
        "c": "ȼ",
        "d": "đ",
        "e": "ɇ",
        "g": "ǥ",
        "h": "ħ",
        "i": "ɨ",
        "j": "ɉ",
        "l": "ł",
        "o": "ø",
        "r": "ɍ",
        "t": "ŧ",
        "y": "ɏ",
        "z": "ƶ",
        "A": "Ⱥ",
        "B": "Ƀ",
        "C": "Ȼ",
        "D": "Đ",
        "E": "Ɇ",
        "G": "Ǥ",
        "H": "Ħ",
        "I": "Ɨ",
        "J": "Ɉ",
        "L": "Ł",
        "O": "Ø",
        "R": "Ɍ",
        "T": "Ŧ",
        "Y": "Ɏ",
        "Z": "Ƶ",
        "default": "X̵"
    },
    # TILDE
    "TEULD": {
        "a": "ã",
        "e": "ẽ",
        "i": "ĩ",
        "l": "ɫ",
        "n": "ñ",
        "o": "õ",
        "u": "ũ",
        "v": "ṽ",
        "y": "ỹ",
        "A": "Ã",
        "E": "Ẽ",
        "I": "Ĩ",
        "L": "Ɫ",
        "N": "Ñ",
        "O": "Õ",
        "U": "Ũ",
        "V": "Ṽ",
        "Y": "Ỹ",
        "default": "X̃"
    },
    # E LIGATURE
    "ELG": {
        "a": "æ",
        "o": "œ",
        "A": "Æ",
        "O": "Œ",
    },
    # SCHWA
    "SWHA": {
        "e": "ə",
        "E": "Ə",
    },
    # SHARP (Eszett)
    "SHARP": {
        "s": "ß",
        "S": "ẞ"
    },
    # LONG S
    "HROPBG": {
        "s": "ſ"
    },
    # FRICATIVE (eth and thorn)
    "TPREUBG": {
        "d": "ð",
        "t": "þ",
        "D": "Ð",
        "T": "Þ",
    },
    # VELARIZED (eng)
    "SRAOEL": {
        "n": "ŋ",
        "N": "Ŋ",
    },
}

def lookup(outline):
    assert len(outline) <= LONGEST_KEY
    letterStroke = outline[0];
    if letterStroke not in fingerspelledLetters:
        raise KeyError
    letter = fingerspelledLetters[letterStroke]
    prefix = ""
    if letter == letter.lower():
        prefix = "{>}"

    if len(outline) != 2:
        raise KeyError
    assert len(outline) == 2
    diacriticStroke = outline[1]
    if diacriticStroke not in diacritics:
        raise KeyError
    diacriticData = diacritics[diacriticStroke]
    if letter not in diacriticData:
        if "default" not in diacriticData:
            raise KeyError
        return prefix + "{&" + diacriticData["default"].replace("X", letter) + "}"
    return prefix + "{&" + diacriticData[letter] + "}"
