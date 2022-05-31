import sys 
caminho = sys.argv[1]

xseF, yseF, xidF, yidF = 0, 0, 0, 0

with open(caminho, 'r') as file:
    xseF, yseF, xidF, yidF = map(int, file.readline().split())

    for line in file:
        xse, yse, xid, yid = map(int, line.rstrip().split())
        xseF = min(xseF, xse)
        yseF = max(yseF, yse)
        xidF = max(xidF, xid)
        yidF = min(yidF, yid)

print(f"Ret: {xseF}, {yseF}, {xidF}, {yidF}")