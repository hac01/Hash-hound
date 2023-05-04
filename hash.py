import sys
from termcolor import colored

def main():
    hash_value = sys.argv[1]

    hash_lengths_to_algorithms = {
        16: "MD4",
        20: "SHA1",
        24: "CRC24",
        28: "SHA224",
        32: "MD5",
        40: "SHA1",
        48: "SHA384",
        56: "SHA224",
        64: ["SHA256", "HMAC-SHA256", "NTLM", "WPA"],
        96: ["SHA384", "HMAC-SHA384"],
        128: ["SHA512", "HMAC-SHA512", "FNV-1a"],
        160: "SHA1",
        256: ["SHA256", "FNV-1a", "WPA2"],
        320: "FNV-1a",
        384: "SHA384",
        512: "SHA512",
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
