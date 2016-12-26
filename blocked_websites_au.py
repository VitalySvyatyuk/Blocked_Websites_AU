import socket, os, shutil

to_git = False
with open('new_file.txt.tmp', 'w') as hosts_tmp:
    with open('new_file.txt', 'r') as hosts:
        for line in hosts:
            line = line.rstrip("\n")
            line_ips = set(line.split(" ")[1:])
            ips = ""

            new_line = socket.gethostbyname_ex(line.split(" ")[0])


            new_line_ips = set(new_line[2])

            if line_ips == new_line_ips or line_ips.issuperset(new_line_ips):
                hosts_tmp.write(line + "\n")
                print("They are the same")
            else:
                new_ips = line_ips.union(new_line_ips)

                for ip in new_ips:
                    ips += ip + " "
                new_line_to_write = new_line[0] + " " + ips.rstrip(" ") + "\n"

                hosts_tmp.write(new_line_to_write)
                print("Hey! There is a new line!")
                to_git = True

shutil.move('new_file.txt.tmp', 'new_file.txt')
if to_git:
    with open('README.md', 'a')
# print(new_lines)
# if len(new_lines) > 0:
#     with open('new_file.txt', 'w') as new_file:
#         for new_line in new_lines:
#             ips = ""
#             for ip in new_line[2]:
#                 ips += ip + " "
#             line = new_line[0] + " " + ips.rstrip(" ") + "\n"
#             new_file.write(line)

# def line_prepender(filename, line):
#     with open(filename, 'r+') as f:
#         content = f.read()
#         f.seek(0, 0)
#         f.write(line.rstrip('\r\n') + '\n' + content)
