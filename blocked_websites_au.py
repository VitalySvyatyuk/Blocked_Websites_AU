import socket, shutil

new_lines = []
with open('new_file.txt.tmp', 'w') as hosts_tmp:
    with open('new_file.txt', 'r') as hosts:
        for line in hosts:
            line = line.rstrip("\n")
            line_ips = set(line.split(" ")[1:])
            ips = ""
            # try:

            new_line = socket.gethostbyname_ex(line.split(" ")[0])


            new_line_ips = set(new_line[2])

            # print(line_ips)
            # print(new_line_ips)
            if line_ips == new_line_ips or line_ips.issuperset(new_line_ips):
                print(new_line[0])
                # print (line_ips)
                # print(new_line_ips)
                hosts_tmp.write(line + "\n")
                print("They are the same")
            else:
                print(new_line[0])
                new_ips = line_ips.union(new_line_ips)

                for ip in new_ips:
                    ips += ip + " "
                new_line_to_write = new_line[0] + " " + ips.rstrip(" ") + "\n"

                hosts_tmp.write(new_line_to_write)
                print("Hey! There is a new line!")

            # except:
            #     print("Exception")
            #     pass
shutil.move('new_file.txt.tmp', 'new_file.txt')

# print(new_lines)
# if len(new_lines) > 0:
#     with open('new_file.txt', 'w') as new_file:
#         for new_line in new_lines:
#             ips = ""
#             for ip in new_line[2]:
#                 ips += ip + " "
#             line = new_line[0] + " " + ips.rstrip(" ") + "\n"
#             new_file.write(line)
