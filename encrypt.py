"""
This here is a code to demonstrate you the function of Asymmetric Cryptography in python
and how verification works in Blockchain how Messsage/transaction/files get verifired with the help of
Digital Signature + Message + Public key before getting mined on the Blockchain

By Muntazir Mehdi aka AmariS1

Get all my social links here -- https://linktr.ee/mehdii.wani

"""

from cryptography.hazmat.primitives.asymmetric import rsa
import  private
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
#from cryptography.exceptions.InvalidSignature  import TnvalidSignature

#Frist we define the function to generate keys
def generate_keys():
    private = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public = private.public_key()
    return private,public

#Now a function to sign your message 
def sign(message,private):
    message = bytes(str(message),'utf-8') #to covert meesage to bytes.
    
    signature = private.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

#here we verify our message using signature, message and public key generated.
def verify(message,dig_sig,public):
    message = bytes(str(message),'utf-8')
    # try:                                  #This code here is if ypu got any kind of exception while running the code
    #     public = private.public_key()
    #     public.verify(
    #         dig_sig,
    #         message,
    #         padding.PSS(
    #             mgf=padding.MGF1(hashes.SHA256()),
    #             salt_length=padding.PSS.MAX_LENGTH
    #         ),
    #         hashes.SHA256()
    #     )
    #     return True
    # except exception.InvalidSignature :
    #     return False
    # except:
    #     print("error in pub key")
    #     return False
    public.verify(
        dig_sig,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return True

#Hnow we call the functions here 

if __name__=='__main__':
    prv_key,pub_key = generate_keys()
    print('\nThis is the private key \n',prv_key)   # Prints Private Key
    print( "\n\nThis is the public key \n",pub_key) # Prints Public Key

    message = "this is the message to be encrypted" # here we write the message that we want to encrypt 
    dig_sig = sign(message,prv_key)
    print('\n\nThis is the Digital Signature Generated for the message\n',dig_sig) # prints Su=ignature of the message 
    check = verify(message,dig_sig,pub_key)
    if check:
        print("\n\nverification sucessful\n\n")
    else:
        print('\n\nverification failed\n\n')