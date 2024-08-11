# Esse script tem como objetivo fazer uma enumeração de forma ativa em subdomínios. (enumera utilizando resolução de DNS)

import dns.resolver
import argparse

parser = argparse.ArgumentParser(description='Escaner de diretórios simples')
parser.add_argument('-d', '--domain', help='Domínio alvo', required=True)
parser.add_argument('-w', '--wordlist', help='Wordlist para scan', required=True)
args = parser.parse_args()

domain = args.domain
wordlist = args.wordlist

def get_subdomains(domain, wordlist):
    subdomains = set()
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8']
    with open(wordlist) as f:
        wordlist = f.read().splitlines()
    for word in wordlist:
        subdomain = f"{word}.{domain}"
        try:
            answers = resolver.resolve(subdomain)
            if answers:
                subdomains.add(subdomain)
        except:
            pass
    return subdomains

subdomains = get_subdomains(domain, wordlist)
print(f"[+] ON: {subdomains}")

# Exemplo de uso: python3 subdomains-scanner.py -d google.com -w wordlist.txt
# O script irá fazer uma enumeração de subdomínios utilizando a wordlist passada como argumento.
