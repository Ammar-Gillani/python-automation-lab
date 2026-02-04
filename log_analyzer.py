file = open("sample_log.txt", "r")
lines = file.readlines()
file.close()
print("Total lines:", len(lines))
