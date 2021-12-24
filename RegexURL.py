import re     

class ValidacaoDeSites:
        def validarSite(self):
                regex = re.compile(
                        r'^(?:http|ftp)s?://|www.' # http:// ou https://
                        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
                        r'localhost|'
                        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
                        r'(?::\d+)?' # optional port
                        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
                
                return regex

if __name__ == "__main__":
        site = ValidacaoDeSites()
        print(re.match(site.validarSite(), "https://www.example.com") is not None)
        print(re.match(site.validarSite(), "example.com") is not None) #False
        print(re.match(site.validarSite(), "www.ifpb.edu.br") is not None)
        print(re.match(site.validarSite(), "http://www.ifpb.br") is not None)
        print(re.match(site.validarSite(), "https://ifpb.br") is not None)
        print(re.match(site.validarSite(), "https://www.ifpb.edu.br") is not None)
        print(re.match(site.validarSite(), "https://www.ifpb.edu.br/tsi") is not None) 
        print(re.match(site.validarSite(), "httpss://www.ifpb.br/rc") is not None) # False
        print(re.match(site.validarSite(), "https://localhost") is not None)
        print(re.match(site.validarSite(), "https://192.168.56.10") is not None)
        print(re.match(site.validarSite(), "https://192.168.56.10:8000") is not None)
        print(re.match(site.validarSite(), "localhost") is not None) # False