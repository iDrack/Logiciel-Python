#!/usr/bin/python3

def crypte():
    print("Nom du fichier à crypter:")
    fin = (input())
    print()
    print("Nom du fichier de sortie:")
    fout = (input())
    cle = int(input("Clé: "))

    with open (fout,"w") as f1:
        with open (fin,"r") as f2:
            content = f2.read()
            for e in content:
                x = ord(e)
                if (x > 64 and x < 91) or (x > 96 and x < 123):
                    if x > 64 and x < 91:
                        code = x+cle
                        if code >= 91:
                            code = code-26
                            f1.write(chr(code))
                        else:
                            f1.write(chr(code))
                        
                    elif (x > 96 and x < 123):
                        code = x+cle
                        if code >= 123:
                            code = code-26
                            f1.write(chr(code))    
                        else:
                            f1.write(chr(code))
                                   
                else:
                    f1.write(str(e))
        f2.close()
    f1.close()

crypte()

def decrypte():
    print("Nom du fichier à décrypter:")
    fin = (input())
    print()
    print("Nom du fichier de sortie:")
    fout = (input())
    cle = int(input("Clé: "))

    with open (fout,"w") as f1:
        with open (fin,"r") as f2:
            content = f2.read()
            for e in content:
                x = ord(e)
                if (x > 64 and x < 91) or (x > 96 and x < 123):
                    if x > 64 and x < 91:
                        code = x-cle
                        if code <= 64:
                            code = code-26
                            f1.write(chr(code))
                        else:
                            f1.write(chr(code))
                        
                    elif (x > 96 and x < 123):
                        code = x-cle
                        if code <= 96:
                            code = code-26
                            f1.write(chr(code))    
                        else:
                            f1.write(chr(code))
                                   
                else:
                    f1.write(str(e))
        f2.close()
    f1.close()
    
decrypte()
