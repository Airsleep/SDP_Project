contents = []
cnt = 0
with open(r"C:\Users\gnaro\Desktop\SDP_Project\iread\data\mouse_test.txt", "r") as f:
    for row in f:
        contents.append(row.replace("\t", "^").split("^")[9])
        cnt += 1
    if cnt == 1:
        raise

# print(contents[0][9])
# print(type(contents[0]))
