import sys
from termcolor import colored

def main():
    # Check for help menu
    if len(sys.argv) > 1 and (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        print('Usage: python script.py <hash_value>')
        print(''' 
        For example :- hash-hound 8d6e34f987851aa599257d3831a1af040886842f
        Output:- Algorithm used: SHA1:100 
        Here SHA1 is the hashing algorithm and 100 is Hashcat mode for ex: "-m 100"
        ''')
        return

    hash_value = sys.argv[1]

    hash_lengths_to_algorithms = {
            16: "MD4:0",
            20: "SHA1:100",
            24: "CRC24",
            28: "SHA224:5300",
            32: "MD5:0",
            40: "SHA1:100",
            48: "SHA384:14600",
            56: "SHA224:5300",
            64: ["SHA256:1400", "HMAC-SHA256:7500", "NTLM", "WPA"],
            96: ["SHA384:14700", "HMAC-SHA384:14600"],
            128: ["SHA512:1700", "HMAC-SHA512:17500", "FNV-1a"],
            160: "SHA1:100",
            256: ["SHA256:1400", "FNV-1a", "WPA2"],
            320: "FNV-1a",
            384: "SHA384:14600",
            512: "SHA512:1700",
        }

    # Identify the algorithm used for the hash value
    algorithm = hash_lengths_to_algorithms.get(len(hash_value), "Unknown algorithm")

    if isinstance(algorithm, list):
        algorithms = ", ".join(algorithm)
        print(colored(f"Matching algorithms: {algorithms}", "red"))
    else:
        print(colored(f"Algorithm used: {algorithm}", "red"))

if __name__ == "__main__":
    main()
