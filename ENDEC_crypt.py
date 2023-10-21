import base64
from db import Read,Update,establish_connection 

def encrypt(mo_no,bank,pswd):
    en_pass=str(base64.b85encode(pswd.encode('utf-8')))
    en_pass=str(en_pass[2:7])
    #print(en_pass)
    establish_connection()
    Update("update customer set pin='{}' where ph_no='{}' and bank='{}'".format(en_pass,mo_no,bank))
    return True

def decrypt(mo_no,bank):
    establish_connection()
    en_pass=Read("select pin from customer where ph_no='{}' and bank='{}'".format(mo_no,bank))[0][0]
    #print(en_pass)
    dec_pass=base64.b85decode(en_pass).decode('utf-8')
    #print(dec_pass)
    return dec_pass


