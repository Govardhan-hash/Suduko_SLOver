import time
su = {"A1": "N", "B1": "A", "C1": "B", "D1": "C", "E1": "D", "F1": "E","G1":"F","H1":"G","I1":"H","J1":"I",
      "A2":"1:", 1:"_",2:"_",3:"_",4:"_",5:"_",6:"_",7:"_",8:"_",9:"_",
      "B2":"2:", 10:"_",11:"_",12:"_",13:"_",14:"_",15:"_",16:"_",17:"_",18:"_",
      "C2":"3:", 19:"_",20:"_",21:"_",22:"_",23:"_",24:"_",25:"_",26:"_",27:"_",
      "D2":"4:", 28:"_",29:"_",30:"_",31:"_",32:"_",33:"_",34:"_",35:"_",36:"_",
      "E2":"5:", 37:"_",38:"_",39:"_",40:"_",41:"_",42:"_",43:"_",44:"_",45:"_",
      "F2":"6:", 46:"_",47:"_",48:"_",49:"_",50:"_",51:"_",52:"_",53:"_",54:"_",
      "G2":"7:", 55:"_",56:"_",57:"_",58:"_",59:"_",60:"_",61:"_",62:"_",63:"_",
      "H2":"8:", 64:"_",65:"_",66:"_",67:"_",68:"_",69:"_",70:"_",71:"_",72:"_",
      "I2":"9:", 73:"_",74:"_",75:"_",76:"_",77:"_",78:"_",79:"_",80:"_",81:"_",
      }
def PrintB():
      c = 0
      for i,j in su.items():
            print(j, end = "   ")
            c += 1
            if c%10 == 0:
                  print()


def Columns(postion):
      l = []
      for j in range(1,10):
            try:
                  if (postion-j)%9 == 0:
                        l.append(su[j])
                        for i in range(1,10):
                              l.append(su[9*i + j])
            except:
                  return l


def Rows(postion):
      l = []
      for i in range(1,10):
            if postion <= i*9 and postion > (i-1)*9:
                  for j in range(1,10):
                        l.append(su[9*(i-1) + j])

      return l

def Box(postion):
      l = []
      if postion == 1 or postion == 2 or postion == 3 or postion == 10 or postion == 11 or postion == 12 or postion == 19 or postion == 20 or postion == 21:
            l.append(su[1])
            l.append(su[2])
            l.append(su[3])
            l.append(su[10])
            l.append(su[11])
            l.append(su[12])
            l.append(su[19])
            l.append(su[20])
            l.append(su[21])
      elif postion == 4 or postion == 5 or postion == 6 or postion == 13 or postion == 14 or postion == 15 or postion == 22 or postion == 23 or postion == 24:
            l.append(su[4])
            l.append(su[5])
            l.append(su[6])
            l.append(su[13])
            l.append(su[14])
            l.append(su[15])
            l.append(su[22])
            l.append(su[23])
            l.append(su[24])
      elif postion == 7 or postion == 8 or postion == 9 or postion == 16 or postion == 17 or postion == 18 or postion == 25 or postion == 26 or postion == 27:
            l.append(su[7])
            l.append(su[8])
            l.append(su[9])
            l.append(su[16])
            l.append(su[17])
            l.append(su[18])
            l.append(su[25])
            l.append(su[26])
            l.append(su[27])
      elif postion == 28 or postion == 29 or postion == 30 or postion == 37 or postion == 38 or postion == 39 or postion == 46 or postion == 47 or postion == 48:
            l.append(su[28])
            l.append(su[29])
            l.append(su[30])
            l.append(su[37])
            l.append(su[38])
            l.append(su[39])
            l.append(su[46])
            l.append(su[47])
            l.append(su[48])
      elif postion == 31 or postion == 32 or postion == 33 or postion == 40 or postion == 41 or postion == 42 or postion == 49 or postion == 50 or postion == 51:
            l.append(su[31])
            l.append(su[32])
            l.append(su[33])
            l.append(su[40])
            l.append(su[41])
            l.append(su[42])
            l.append(su[49])
            l.append(su[50])
            l.append(su[51])
      elif postion == 34 or postion == 35 or postion == 36 or postion == 43 or postion == 44 or postion == 45 or postion == 52 or postion == 53 or postion == 54:
            l.append(su[34])
            l.append(su[35])
            l.append(su[36])
            l.append(su[43])
            l.append(su[44])
            l.append(su[45])
            l.append(su[52])
            l.append(su[53])
            l.append(su[54])
      elif postion == 55 or postion == 56 or postion == 57 or postion == 64 or postion == 65 or postion == 66 or postion == 73 or postion == 74 or postion == 75:
            l.append(su[55])
            l.append(su[56])
            l.append(su[57])
            l.append(su[64])
            l.append(su[65])
            l.append(su[66])
            l.append(su[73])
            l.append(su[74])
            l.append(su[75])
      elif postion == 58 or postion == 59 or postion == 60 or postion == 67 or postion == 68 or postion == 69 or postion == 76 or postion == 77 or postion == 78:
            l.append(su[58])
            l.append(su[59])
            l.append(su[60])
            l.append(su[67])
            l.append(su[68])
            l.append(su[69])
            l.append(su[76])
            l.append(su[77])
            l.append(su[78])
      elif postion == 61 or postion == 62 or postion == 63 or postion == 70 or postion == 71 or postion == 72 or postion == 79 or postion == 80 or postion == 81:
            l.append(su[61])
            l.append(su[62])
            l.append(su[63])
            l.append(su[70])
            l.append(su[71])
            l.append(su[72])
            l.append(su[79])
            l.append(su[80])
            l.append(su[81])
      return l
def Add():
      o = "y"
      x = ""
      y = 0
      PrintB()
      while o == "y":
            while True:
                  x = input("Which Column")
                  if x in "ABCDEFGHI":
                        break
            while True:
                  y = input("Which Row")
                  if y in "123456789":
                        y = int(y)
                        break
            r = 0
            if x == "A":
                  r = 1
            elif x == "B":
                  r = 2
            elif x == "C":
                  r = 3
            elif x == "D":
                  r = 4
            elif x == "E":
                  r = 5
            elif x == "F":
                  r = 6
            elif x == "G":
                  r = 7
            elif x == "H":
                  r = 8
            elif x == "I":
                  r = 9
            su[r + 9*(y - 1)] = int(input("What is the number on this space"))
            PrintB()
            o = input("want to continue?: y/n")
#Main body
Add()
start_time = time.perf_counter()

PrintB()

fixed = []
for i,j in su.items():
      if j != "_":
            fixed.append(i)
v = 1
na = []
tried = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],
12:[],13:[],14:[],15:[],16:[],17:[],18:[],19:[],20:[],21:[],22:[],
23:[],24:[],25:[],26:[],27:[],28:[],29:[],30:[],31:[],32:[],
33:[],34:[],35:[],36:[],37:[],38:[],39:[],40:[],41:[],42:[],
43:[],44:[],45:[],46:[],47:[],48:[],49:[],
50:[],51:[],52:[],53:[],54:[],55:[],56:[],57:[],58:[],59:[],
60:[],61:[],62:[],63:[],64:[],65:[],66:[],67:[],68:[],69:[],
70:[],71:[],72:[],73:[],74:[],75:[],76:[],77:[],78:[],79:[],
80:[],81:[]}
while v < 82:
      F = "a"
      if v in fixed:
            v = v + 1
            F = "J"
            continue
      if v == 81 and v in fixed:
            break
      na = Box(v) + Rows(v) + Columns(v) + tried[v]
      tr = 1
      placed = False

      while tr < 10:
            if tr not in na and F != "J":
                  su[v] = tr
                  placed = True
                  break
            else:
                  tried[v].append(tr)
            tr += 1
      if placed:
            v += 1   # move forward
      else:
            if F != "J" and v > 0:
                  tried[v] = []
                  su[v] = 0
                  v -= 1
                  while v in fixed and v > 1:
                        v -= 1

PrintB()
end_time = time.perf_counter()
print(f"Executed in {end_time - start_time:0.8f} seconds")


