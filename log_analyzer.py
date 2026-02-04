file = open("sample_log.txt", "r")
lines = file.readlines()
file.close()
error_count = 0
for line in lines:
  if "ERROR" in line:
    error_count += 1
    
print("Total lines:", len(lines))
print("Error lines:", error_count)
