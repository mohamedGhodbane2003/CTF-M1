import subprocess
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def generate_csr(private_key_pem):
    # Load the private key from PEM format
    private_key = serialization.load_pem_private_key(
        private_key_pem,
        password=None,
        backend=default_backend()
    )

    # Generate a CSR
    cmd = ["openssl", "req", "-new", "-key", "/dev/stdin", "-subj", "/CN=mooh"]
    csr_pem = subprocess.check_output(cmd, input=private_key_pem)

    return csr_pem.decode()


private_key_pem = b"""
-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCrn/8SupYNQOdA
/+GahABSQrQh7qUateNyySavX4GIwnsB3T/S57r3cYm/yoVw8Uw8O55ELhkiU93c
oEvC6cmaGJ/X85eEMJzGELPxJ7gBc9bANzXQ2bqiaZGqWq2aNwpqOaMQJbjl6JRI
zjk3pUY7yPaXfxb30ajV7rlOgcYzL2QeQzMs1vREP9/dsqWVc4ipHD/3GlAR2m2q
w6S25Hm6+gRBQir5WaXUqh+OR9B7ixMdFZpmoNFgTMl7IB0io6Gk/dFPdctA3AQY
Tk4qkDJjhDOzPTonCvdjZz6Obk/e2H6aertNYeKdiokdmHc5Ole/b8PxFFQBM3bl
Wdjux4FJAgMBAAECggEACLzYVGiF965F0nLElmSL4fmYk1VY+AtpxUq1lWj6yWRC
CstWyBgkAMbkcQyF7y+wcSzwMZSZkycVwk6x6hOTf+zVhH3XyV3dOXNDv1ka6Tiv
0VuY5JAVNwFsw7F3/wQ4MPDMGxLElLCa42WxFuLAo44SHzk+ntwrKPB4DuW/WhSF
UKX8tMrRyvGvjp7ZdbQMh78gLxrJI1p1S/yhZnAJMuX9b2haXlILoWR991nnfsXI
Q2pKO3SHgUpKFpRPrB41yNqIQKKF2poVRYS0byHNBahhzXL85LlzUxnJvHShQTok
4H5imPCwhI9tZlEjnY4pjzL9rtGKDaXx6wVdU4Nt5QKBgQDaXqOHglbCBVzuy791
sFTxcBDmzJBiwjLqRNyFaoPcGR6Y3yIjeCgzhmVm5dgFuWzGR58YQl6AkOKy5bpe
ui+5uvV8rwvH5qal1HtQiHWBnqo47JDl8dMOfk7HtOXkR+PIrwNSRflCreMN5VMM
mNwwRu1L+yqMt3H8WEIJmvhf9QKBgQDJMzgQeWnyImJ9puS8xw/NnhRWPUS4r6mC
Z6Qfz57pm6dI4KroA8x/xPWVbxaQ5npD6ycjO6I+kD86M1Zq9KOCMoAxWIVKLekw
l8axWvZEJFzONI2mo6NO96rN89c5+ocC3VXWBIdWVMT6lYVxRhk1Miyii39bkHiQ
xaf5tvGrhQKBgQCZFRVArt+RHl9azBzJLTcvFmfS1H83rHoy/tk08knD5xwrAOmW
weo0zLeTXfeFc8rMaXMfd492Q5uY3DE9rPo+EtF7ed8hYRFcWUulVjRCDO+5/iVJ
/a/+jg8+MxOiZ79IdWA3sfQeiXYNzMDeqN5bPa2mwUm/4e4Xf+uzfh82bQKBgQCG
OwidXRNEupHw+IZEN54gdOVmf6u4d2FkodaKbo67ld/uLA15iwdE+tdJIfrxIwLR
CzJqPB/LE5tLLfLqmln3w89onIEYczbO94NU0bXY0lWkMMWMNkH+rhcjHhoqES0/
yQC6Lv1HqHheIaEMaFLq/ZVvwBdwtBrroyKk49uprQKBgQCoCGjxscwtBPlknNB/
ZnzE6x9FI0GmR5EPUOE1ghdly5AI85eYRPvudrJd+LJM7UIDcqY0HxY1wKnaoaK6
wTePrXWCia7h21UzZWa3iaz/VpnhS19p1LmCU1KMBJ4QP+MDPlJjD2iOXSVzYJ4i
qCoOwhcr/UaM3Knx2Aj+iYib3g==
-----END PRIVATE KEY-----
"""

# Generate CSR using the private key
csr_pem = generate_csr(private_key_pem)

print("CSR (PEM format):\n", csr_pem)
