class EmailObfuscator:
    def __init__(self, obfuscation_char='x'):
        self.obfuscation_char = obfuscation_char

    def obfuscate(self, email):
        if '@' not in email:
            return 'Некорретно введён адрес'
        username, domain = email.split('@')
        obfuscated_username = self.obfuscation_char * len(username)
        return f"{obfuscated_username}@{domain}"


class PhoneObfuscator:
    def __init__(self, obfuscation_char='x'):
        self.obfuscation_char = obfuscation_char

    def obfuscate(self, phone, num_chars_to_obfuscate=3):
        res = ''
        count = 0
        for i in range(-1, -len(phone) - 1, -1):
            if phone[i] != ' ':
                if count < num_chars_to_obfuscate:
                    res += self.obfuscation_char
                    count += 1
                else:
                    res += phone[i]
            else:
                res += phone[i]
        res = ' '.join([i.strip() for i in res.split()])
        return res[::-1]


class SkypeObfuscator:
    def __init__(self, obfuscation_char='x'):
        self.obfuscation_char = obfuscation_char

    def obfuscate(self, skype):
        if skype.startswith('skype:'):
            return f"skype:{self.obfuscation_char * 3}"
        elif '<a href="skype:' in skype:
            start = skype.find('skype:') + len('skype:')
            end = skype.find('?call')
            if end == -1:
                end = skype.find('"', start)
            obfuscated_username = self.obfuscation_char * 3
            return skype[:start] + obfuscated_username + skype[end:]
        return skype

