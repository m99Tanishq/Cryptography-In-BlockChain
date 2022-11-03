from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def generate_keys():   # Generating Keys
    private = rsa.generate_private_key(
        public_exponent=65537,
        key_size = 2048,
    )
    public = private.public_key()
    return private,public

def sign(message,private): # Signature
    message = bytes(str(message), 'utf-8') #Converting Message to Bytes
    signature = private.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
    ) 
    return signature

if __name__ == '__main__':

    pr,pu = generate_keys();
    print(pr)
    print(pu)

    message ="PREVET! ТАНИШК" #Message
    sig = sign(message,pr)
    print(sig)



def verify(message, sig, public): #Verification
   message = bytes(str(message), 'utf-8') #Converting Message to Bytes
   try:
    public.verify(
     sig,
     message,
     padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
    )
    return True
   except:
    return False 
    
correct = verify(message, sig, pu);
if correct:
    print("Successful")
else:
    print("Unsucessful")