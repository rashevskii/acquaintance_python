arr_xyz = [[0,0,0],[0,0,1],[0,1,1],[0,1,0],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
for item in arr_xyz:
    print("Результат проверки истинности утверждения: ", not(item[0] or item[1] or item[2]) == ((not item[0]) and (not item[1]) and (not item[2])))
