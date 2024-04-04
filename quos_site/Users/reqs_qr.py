import random

def gen_request_qr_code():
    alp = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','0','2','3','4','5','6','7','8','9']

    l = []
    for i in range(16):
        n = random.choice(alp)
        l.append(n)

    def chunks(lst, chunk_size):
        for i in range(0, len(lst), chunk_size):
            yield lst[i:i + chunk_size]

    chunks_list = list(chunks(l, 4))

    code_request = ""
    for i in chunks_list:
        for n in i:
            code_request = code_request + str(n)
        code_request = code_request + "-"
    code_request = code_request[:-1]

    print(code_request)
    return(code_request)

if __name__ == "__main__":
    name = input("Название файл без расширения: ")
    code = input("Код: ")
