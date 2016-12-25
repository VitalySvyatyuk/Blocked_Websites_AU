import socket

new_lines = []
with open('blocked_websites_au.txt', 'r') as hosts:
    for line in hosts:
        line = line.rstrip('\n')
        try:
            new_line = socket.gethostbyname_ex(line)
            if new_line != line:
                new_lines.append(new_line)
        except:
            pass

# if len(new_lines) > 0:
#     with open('blocked_websites_au.txt', 'w') as hosts:
#         