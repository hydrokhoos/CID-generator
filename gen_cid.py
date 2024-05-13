import hashlib
import sys
from cid import make_cid
from multihash import encode

def file_to_cid(file_path):
    with open(file_path, 'rb') as f:
        file_content = f.read()

    sha256_hash = hashlib.sha256(file_content).digest()

    mh_encoded = encode(sha256_hash, 'sha2-256')

    cid = make_cid(1, 'raw', mh_encoded)
    # cid = make_cid(0, 'dag-pb', mh_encoded)

    return cid

if __name__ =='__main__':
    args = sys.argv
    if len(args) < 2:
        print('arguments are too short')
        exit(1)

    cid = file_to_cid(args[1])
    print(cid)
