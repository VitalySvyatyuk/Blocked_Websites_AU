import socket, os, shutil, datetime


to_git = False
updates = {}
for file in os.listdir("hosts"):
    if not file.endswith('_vars') or file.endswith('.tmp'):
        PATH_TO_FILE_TMP = 'hosts/' + file + '.tmp'
        PATH_TO_FILE = 'hosts/' + file
        PATH_TO_FILE_VARS = 'hosts/' + file + '_vars'

        if not os.path.isfile(PATH_TO_FILE_VARS):
            shutil.copy(PATH_TO_FILE, PATH_TO_FILE_VARS)
        if not os.path.isfile(PATH_TO_FILE_TMP):
            os.mknod(PATH_TO_FILE_TMP)

        with open(PATH_TO_FILE_VARS, 'r') as hosts_vars:
            pass
        print(hosts_vars)
        with open(PATH_TO_FILE_TMP, 'w') as hosts_tmp:
            with open(PATH_TO_FILE, 'r') as hosts:

                update_lines = []
                for line in hosts:
                    line = line.rstrip("\n")
                    line_ip = line.split(" ")[0]

                    try:
                        new_line = socket.gethostbyname_ex(line.split(" ")[1])
                        print(new_line)
                        print(line_ip)

                        if line_ip in new_line[2]: #or line_ip in vars:
                            hosts_tmp.write(line + "\n")
                            print("They are the same")
                        else:
                            new_line_to_write = new_line[2][0] + " " + new_line[0] + "\n"
                            hosts_tmp.write(new_line_to_write)
                            print("Hey! There is a new line!->>>>>>>>>>>>")
                            to_git = True
                            update_lines.append(new_line[0] + " -> from " + line_ip + " to " + new_line[2][0])
                    except (socket.gaierror, socket.herror):
                        pass
                if len(update_lines) != 0:
                    updates[file] = update_lines

        shutil.move(PATH_TO_FILE_TMP, PATH_TO_FILE)
        if os.path.isfile(PATH_TO_FILE_TMP):
            os.remove(PATH_TO_FILE_TMP)

print(updates)
if to_git:
    with open('README.md', 'a') as readme:
        for key, values in updates.items():  
            readme.write("\n")         
            readme.write("\n<--- Update for " + key + " from " + str(datetime.datetime.now())[:19] + " : ")
            for val in values:
                readme.write("\n" + val)
            readme.write("\n")

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



# --- EMAIL SENDING FOR CHECKING SCRIPT WORKING ---
# import smtplib
# from email.mime.text import MIMEText

# computername = os.getenv('COMPUTERNAME')
# msg = MIMEText('Hello from {}'.format(datetime.datetime.now()))
# msg['Subject'] = 'Test from {}!'.format(computername)
# email_from = '{}@test.com'.format(computername)
# email_to = 'vetal_sv@bk.ru'
# msg['From'] = email_from
# msg['To'] = email_to

# s = smtplib.SMTP('127.0.0.1')
# s.sendmail(email_from, [email_to], msg.as_string())
# s.quit()