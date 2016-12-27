import socket, os, shutil

to_git = False
with open('hosts/blocked_websites_au.tmp', 'w') as hosts_tmp:
    with open('hosts/blocked_websites_au', 'r') as hosts:
        for line in hosts:
            line = line.rstrip("\n")
            line_ip = line.split(" ")[0]
            print(line_ip)

            try:
                new_line = socket.gethostbyname_ex(line.split(" ")[0])

                if line_ip in new_line[2]:
                    hosts_tmp.write(line + "\n")
                    print("They are the same")
                else:
                    new_line_to_write = new_line[2][0] + " " + new_line[0] + "\n"
                    hosts_tmp.write(new_line_to_write)
                    print("Hey! There is a new line!")
                    to_git = True
            except socket.gaierror:
                pass

shutil.move('hosts/blocked_websites_au.tmp', 'hosts/blocked_websites_au')

# if to_git:
#     with open('README.md', 'a')

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
