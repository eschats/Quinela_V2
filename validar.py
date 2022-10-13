import re


# Valida el código (si es numérico y de longitud 6).
def validar_codigo(codigo: str) -> bool:
    return (codigo.isnumeric() and len(codigo) == 6)

# Valida el nombre (si es un texto sin espacios en blanco de entre 1 y 30 caracteres).
def validar_nombre(nombre: str) -> bool:
    nombre = nombre.strip()
    return (len(nombre) > 0 and len(nombre) <= 30)

# Valida que los créditos estén entre 1 y 9.
def validar_creditos(creditos: str) -> bool:
    creditos_texto = str(creditos)
    if creditos_texto.isnumeric():
        return (creditos >= 1 and creditos <= 9)
    else:
        return False


body_regex = re.compile('''
    ^(?!\.)                            # name may not begin with a dot
    (
      [-a-z0-9!\#$%&'*+/=?^_`{|}~]     # all legal characters except dot
      |
      (?<!\.)\.                        # single dots only
    )+
    (?<!\.)$                            # name may not end with a dot
''', re.VERBOSE | re.IGNORECASE)
domain_regex = re.compile('''
    (
      localhost
      |
      (
        [a-z0-9]
            # [sub]domain begins with alphanumeric
        (
          [-\w]*                         # alphanumeric, underscore, dot, hyphen
          [a-z0-9]                       # ending alphanumeric
        )?
      \.                               # ending dot
      )+
      [a-z]{2,}                        # TLD alpha-only
   )$
''', re.VERBOSE | re.IGNORECASE)


def is_valid_email(email):
    if not isinstance(email, str) or not email or '@' not in email:
        return False
    
    body, domain = email.rsplit('@', 1)

    match_body = body_regex.match(body)
    match_domain = domain_regex.match(domain)

    if not match_domain:
        # check for Internationalized Domain Names
        # see https://docs.python.org/2/library/codecs.html#module-encodings.idna
        try:
            domain_encoded = domain.encode('idna').decode('ascii')
        except UnicodeError:
            return False
        match_domain = domain_regex.match(domain_encoded)

    return (match_body is not None) and (match_domain is not None)



def tipo(tipos):
    if tipos == '1' or tipos == '2':
        return True
    else:
        return False


