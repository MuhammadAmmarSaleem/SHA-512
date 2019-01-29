import binascii
# input = input("Enter message \n")
st = input("Enter message \n")
constants = ["428a2f98d728ae22", "7137449123ef65cd", "b5c0fbcfec4d3b2f", "e9b5dba58189dbbc",
             "3956c25bf348b538", "59f111f1b605d019", "923f82a4af194f9b", "ab1c5ed5da6d8118",
             "d807aa98a3030242", "12835b0145706fbe", "243185be4ee4b28c", "550c7dc3d5ffb4e2",
             "72be5d74f27b896f", "80deb1fe3b1696b1", "9bdc06a725c71235", "c19bf174cf692694",
             "e49b69c19ef14ad2", "efbe4786384f25e3", "0fc19dc68b8cd5b5", "240ca1cc77ac9c65",
             "2de92c6f592b0275", "4a7484aa6ea6e483", "5cb0a9dcbd41fbd4", "76f988da831153b5",
             "983e5152ee66dfab", "a831c66d2db43210", "b00327c898fb213f", "bf597fc7beef0ee4",
             "c6e00bf33da88fc2", "d5a79147930aa725", "06ca6351e003826f", "142929670a0e6e70",
             "27b70a8546d22ffc", "2e1b21385c26c926", "4d2c6dfc5ac42aed", "53380d139d95b3df",
             "650a73548baf63de", "766a0abb3c77b2a8","81c2c92e47edaee6", "92722c851482353b",
             "a2bfe8a14cf10364", "a81a664bbc423001", "c24b8b70d0f89791", "c76c51a30654be30",
             "d192e819d6ef5218", "d69906245565a910", "f40e35855771202a", "106aa07032bbd1b8",
             "19a4c116b8d2d0c8", "1e376c085141ab53", "2748774cdf8eeb99", "34b0bcb5e19b48a8",
             "391c0cb3c5c95a63", "4ed8aa4ae3418acb", "5b9cca4f7763e373", "682e6ff3d6b2b8a3",
             "748f82ee5defb2fc", "78a5636f43172f60","84c87814a1f0ab72", "8cc702081a6439ec",
             "90befffa23631e28", "a4506cebde82bde9", "bef9a3f7b2c67915", "c67178f2e372532b",
             "ca273eceea26619c", "d186b8c721c0c207", "eada7dd6cde0eb1e", "f57d4f7fee6ed178",
             "06f067aa72176fba", "0a637dc5a2c898a6", "113f9804bef90dae", "1b710b35131c471b",
             "28db77f523047d84", "32caab7b40c72493", "3c9ebe0a15c9bebc", "431d67c49c100d4c",
             "4cc5d4becb3e42b6", "597f299cfc657e2a", "5fcb6fab3ad6faec", "6c44198c4a475817"]

def toBinary(str):
    li=list(str)
    bin=[]
    for x in li:
       num= ord(x)
       bi='{0:08b}'.format(num)
       bin.append(bi)
    return bin
mybin=toBinary(st)
def appendBits(binary):
    bin=binary
    numBits=len(bin)*8
    length=numBits
    count=1
    while length%1024 != 896%1024:
        if count==1:
             bin.append('10000000')
        else:
            bin.append('00000000')
        count=count+1
        length=len(bin)*8

    endBits = '{0:0128b}'.format(numBits)
    count1 = 1
    for x in range(len(endBits)):
        if count1 % 8 == 0:
            bin.append(endBits[count1 - 8:count1])
        count1 = count1 + 1

    return bin

messageBinary=appendBits(mybin)

def convertToHex(messageProcess):
    hexWords=[]
    words=[]
    count=0
    wordCount=0
    for x in range(len(messageProcess)):
        count = count + 1
        if count == 1:
            # hex1 = hex(int(messageProcess[x], 2))
            words.append(messageProcess[x])
        elif count>1 and count<8:
            words[wordCount] += messageProcess[x]
        elif count == 8:
            words[wordCount] += messageProcess[x]
            count = 0
            wordCount = wordCount+1
    # print(words)
    # print(len(words[15]))
    # for i in range(len(words)):
    #     hex1 = hex(int(words[i], 2))
    #     hexWords.append(hex1)
    return words

def xor(message1, message2):
    result=[]
    for i in range(len(message1)):
        if (message1[i] == "0" and message2[i] == '0') or (message2[i] == '0' and message1[i] == '0'):
            result.append("0")

        elif (message1[i] == '1' and message2[i] == '1') or (message2[i] == '1' and message1[i] == '1'):
            result.append("0")

        elif (message1[i] == '0' and message2[i] == '1') or (message2[i] == '0' and message1[i] == '1'):
            result.append("1")
        elif (message1[i] == '1' and message2[i] == '0') or (message2[i] == '1' and message1[i] == '0'):
            result.append("1")
    return result


def phi1(word):
    original=word
    rotr19 = rightShift(original,19)
    rotr61 =  rightShift(original,61)
    shr6 =  LeftShift(original,6)
    temp=xor(rotr19,rotr61)
    result=xor(temp,shr6)
    return result

def phi0(word):
    original=word
    rotr1 = rightShift(original, 1)
    rotr8 = rightShift(original, 8)
    shr7 = LeftShift(original, 7)
    temp= xor(rotr1,rotr8)
    result= xor(temp,shr7)
    return result

def LeftShift(message,n):
    message1 = list(message)
    for i in range(n):
        for x in range(len(message1)-1):
            message1[x]=message1[x+1]
        message1[len(message1)-1] = '0'
    return message1

def rightShift(message,n):
    message1=list(message)
    # print(message1)
    for i in range(n):
        # print(i)
        x = len(message1) - 1
        last = message1[x]
        # y=1
        for y in range(len(message1)-1):
            if x-y-1 >= 0:
                message1[x-y]=message1[x-y-1]
        message1[0] = last
    return message1

def add(mes1, mes2):
    carry=0
    result=[]
    x=len(mes1)-1
    for i in range(len(mes1)):
        if mes1[x-i] == '1' and mes2[x-i] == '1':
            if carry == 1:
                result.append("1")
                carry=1
            elif carry == 0:
                result.append("0")
                carry =1

        elif  mes1[x-i] == '1' and mes2[x-i] == '0':
            if carry == 1:
                result.append("0")
                carry = 1
            elif carry == 0:
                result.append("1")
                carry = 0

        elif mes1[x - i] == '0' and mes2[x - i] == '1':
            if carry == 1:
                result.append("0")
                carry = 1
            elif carry == 0:
                result.append("1")
                carry = 0

        elif mes1[x - i] == '0' and mes2[x - i] == '0':
            if carry == 1:
                result.append("1")
                carry = 0
            elif carry == 0:
                result.append("0")
                carry = 0
    if carry == 1:
        result.append("1")
    finalresult=[]
    fresult=[]
    t=len(result)-1
    for s in range(len(result)):
        finalresult.append(result[t-s])
    # print(len(finalresult))
    if len(finalresult) > 64:
        num = int(''.join(finalresult), 2)
        remain = num%(2**64)
        toBin = "{0:064b}".format(remain)
        finalresult=list(toBin)
     # print(finalresult)
    return finalresult

def EightyWord(hexWords):

    for i in range(16,80):
        sigma1= phi1(hexWords[i-2])
        temp=list(hexWords[i-7])
        sigma2=phi0(hexWords[i-15])
        temp2=list(hexWords[i-16])

        result=add(sigma1,temp)
        result2=add(result,sigma2)
        finalResult=add(result2,temp2)
        word=''.join(finalResult)
        hexWords.append(word)
    return hexWords


def hexToBinary64(li):

    # hex=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    scale = 16  ## equals to hexadecimal
    k = []
    num_of_bits = 64
    for x in li:
        r = bin(int(x, scale))[2:].zfill(num_of_bits)
        k.append(r)
    return k

def convertBuffersToBinary():
    bufferInital = ["6A09E667F3BCC908","BB67AE8584CAA73B", "3C6EF372FE94F82B", "A54FF53A5F1D36F1", "510E527FADE682D1", "9B05688C2B3E6C1F"
        ,"1F83D9ABFB41BD6B", "5BE0CD19137E2179"]
    buffer_binary= hexToBinary64(bufferInital)
    # buffer.a_bin= buffer_binary[0]
    # buffer.b_bin = buffer_binary[1]
    # buffer.c_bin = buffer_binary[2]
    # buffer.d_bin = buffer_binary[3]
    # buffer.e_bin = buffer_binary[4]
    # buffer.f_bin = buffer_binary[5]
    # buffer.g_bin = buffer_binary[6]
    # buffer.h_bin = buffer_binary[7]
    return buffer_binary
def saveIntialBuffer(buffer):
    temp=[]
    for t in buffer:
        temp.append(t)
    return temp
def andBinary(l_m1, l_m2):
    resultAnd=[]
    for g in range(len(l_m1)):
        if (l_m1[g] == '1' and l_m2[g] == '1'):
            resultAnd.append('1')
        elif (l_m1[g] == '1' and l_m2[g] == '0'):
            resultAnd.append('0')
        elif (l_m1[g] == '0' and l_m2[g] == '1'):
            resultAnd.append('0')
        elif (l_m1[g] == '0' and l_m2[g] == '0'):
            resultAnd.append('0')
    return resultAnd

def notBinary(l_m):
    resultNot=[]
    for s in range(len(l_m)):
        if l_m[s] == "1":
            resultNot.append("0")
        elif l_m[s] == "0":
            resultNot.append("1")
    return resultNot

def Ch(e,f,g):
    temp1=list(e)
    temp2=list(f)
    temp3 = list(g)
    eAndF= andBinary(temp1, temp2)
    notE=notBinary(temp1)
    notE_AndG= andBinary(notE, temp3)
    result = xor(eAndF,notE_AndG)
    return result

def sigmaE(e):
    sigE=e
    # print('e: ',sigE)
    rotr14 = rightShift(sigE,14)
    rotr18 = rightShift(sigE,18)
    rotr41 = rightShift(sigE,41)
    result = xor(rotr14,rotr18)
    finalResult= xor(result,rotr41)
    return finalResult

def sigmaA(a):
    rotr28 = rightShift(a, 28)
    rotr34 = rightShift(a, 34)
    rotr39 = rightShift(a, 39)
    result = xor(rotr28, rotr34)
    finalResult = xor(result, rotr39)
    return finalResult

def Maj(a,b,c):
    temp1=list(a)
    temp2=list(b)
    temp3=list(c)
    aAndB= andBinary(temp1,temp2)
    aAndC= andBinary(temp1,temp3)
    bAndC= andBinary(temp2,temp3)
    result=xor(aAndB,aAndC)
    finalResult= xor(result,bAndC)
    return finalResult

def T1(s_h,l_ch,l_sigE,word,Kt):
    l_h=list(s_h)
    l_word=list(word)
    l_K= list(Kt)
    hPlusCh = add(l_h,l_ch)
    hPlusChPlusE = add(hPlusCh,l_sigE)
    tempWt = add(hPlusChPlusE,l_word)
    tempK_final = add(tempWt,l_K)
    return tempK_final

def T2(l_sigA, l_Maj):
    final=add(l_sigA,l_Maj)
    return final

def AddInitialFinalBuffer(buffer, temp):
    finalResult=[]
    for i in range(len(buffer)):
        temp2= list(buffer[i])
        temp3= list(temp[i])
        result=add(temp2,temp3)
        str_result=''.join(result)
        finalResult.append(str_result)
    return finalResult


def SHA(message):
   count = 0
   messageProcess = []
   binary_constants = hexToBinary64(constants)
   buffer = convertBuffersToBinary()
   for i in range(len(message)):
       count = count + 1
       if count <=127:
           messageProcess.append(message[i])
       elif count== 128:
           messageProcess.append(message[i])
           #proceess message. make count=0
           count=0
           Words=convertToHex(messageProcess)
           wordsEighty=EightyWord(Words)
           temp=saveIntialBuffer(buffer)
           for z in range(80):
               Ch1=Ch(buffer[4],buffer[5],buffer[6])
               sigmaE1= sigmaE(buffer[4])
               sigmaA1 = sigmaA(buffer[0])
               Maj1 = Maj(buffer[0],buffer[1],buffer[2])
               l_t1 = T1(buffer[7],Ch1,sigmaE1,wordsEighty[z],binary_constants[z])
               l_t2 = T2(sigmaA1,Maj1)
               buffer[7]=buffer[6] #h=g
               buffer[6]=buffer[5] #g=f
               buffer[5]=buffer[4] #f=e
               temp_buff3=list(buffer[3])
               l_temp_buff3=add(l_t1,temp_buff3) #e=d+T1
               str_l_temp_buff3=''.join(l_temp_buff3)
               buffer[4]=str_l_temp_buff3
               buffer[3]=buffer[2] #d=c
               buffer[2]=buffer[1] #c=b
               buffer[1]=buffer[0] #b=a
               l_tempT1_T2=add(l_t1,l_t2)
               str_tempT1_T2=''.join(l_tempT1_T2)
               buffer[0]=str_tempT1_T2

           buffer = AddInitialFinalBuffer(buffer, temp)


   print(" Hash code 512bits in binary: ",buffer)
   hexWords = []
   for i in range(len(buffer)):
       hex1 = hex(int(buffer[i], 2))
       hexWords.append(hex1)
   print(" Hash code 512bits in hexadecimal: ", hexWords)

SHA(messageBinary)

