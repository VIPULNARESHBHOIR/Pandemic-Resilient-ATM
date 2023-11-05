import base64
from db import Read,Update,establish_connection 

#encrypt the password and save it to the database
def encrypt(mo_no,bank,pswd):
    en_pass=str(base64.b85encode(pswd.encode('utf-8')))
    en_pass=str(en_pass[2:7])
    establish_connection()
    Update("update customer set pin='{}' where ph_no='{}' and bank='{}'".format(en_pass,mo_no,bank))
    return True

#decrypt the password by choosing encrypted password from database
def decrypt(mo_no,bank):
    establish_connection()
    en_pass=Read("select pin from customer where ph_no='{}' and bank='{}'".format(mo_no,bank))[0][0]
    dec_pass=base64.b85decode(en_pass).decode('utf-8')
    return dec_pass


