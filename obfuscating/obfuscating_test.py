from obfuscating import EmailObfuscator, PhoneObfuscator, SkypeObfuscator


def test_email_obfuscator():
    obfuscator = EmailObfuscator('x')
    assert obfuscator.obfuscate('aaa@aaa.com') == 'xxx@aaa.com'
    assert obfuscator.obfuscate('aaaa@aaa.com') == 'xxxx@aaa.com'
    assert obfuscator.obfuscate('a@a.com') == 'x@a.com'
    print("Тесты под email пройдены.")


def test_phone_obfuscator():
    obfuscator = PhoneObfuscator('x')
    assert obfuscator.obfuscate('+7 666 777 888') == '+7 666 777 xxx'
    assert obfuscator.obfuscate('+7 666 777       888', 5) == '+7 666 7xx xxx'
    assert obfuscator.obfuscate('+7 666 777       888', 25) == 'xx xxx xxx xxx'
    print("Тесты под номер телефона пройдены.")


def test_skype_obfuscator():
    obfuscator = SkypeObfuscator('x')
    assert obfuscator.obfuscate('skype:alex.max') == 'skype:xxx'
    assert obfuscator.obfuscate('<a href="skype:alex.max?call">skype</a>') == '<a href="skype:xxx?call">skype</a>'
    print("Тесты под скайп пройдены.")


test_email_obfuscator()
test_phone_obfuscator()
test_skype_obfuscator()
