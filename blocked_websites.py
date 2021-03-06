import socket, os, shutil, datetime
 
to_git = False
updates = {}
for file in os.listdir("vars"):
    if file.endswith("_vars"):
        PATH_TO_FILE = 'hosts/' + file.rstrip("_vars")
        PATH_TO_FILE_TMP = 'vars/' + file.rstrip("_vars") + ".tmp"
        PATH_TO_FILE_VARS = 'vars/' + file
        PATH_TO_FILE_DEAD = 'dead/' + file.rstrip("_vars") + "_dead"

        if not os.path.isfile(PATH_TO_FILE_TMP):
            os.mknod(PATH_TO_FILE_TMP)

        with open(PATH_TO_FILE_TMP, 'w') as hosts_tmp:
            with open(PATH_TO_FILE_VARS, 'r') as _vars:
                with open(PATH_TO_FILE_DEAD, 'w') as _dead:
                    update_lines = []
                    for line in _vars:
                        line = line.rstrip("\n")
                        line_ips = set(line.split(" ")[1:])
                        ips = ""
             
                        try:
                            new_line = socket.gethostbyname_ex(line.split(" ")[0])

                            new_line_ips = set(new_line[2])

                            if line_ips == new_line_ips or line_ips.issuperset(new_line_ips):
                                hosts_tmp.write(line + "\n")
                                print "They are the same"
                            else:
                                new_ips = line_ips.union(new_line_ips)
             
                                for ip in new_ips:
                                    ips += ip + " "
                                new_line_to_write = new_line[0] + " " + ips.rstrip(" ") + "\n"
             
                                hosts_tmp.write(new_line_to_write)
                                print "Hey! There is a new line!->>>>>>>>>>"
                                to_git = True
                                update_lines.append(new_line[0])
                        except (socket.gaierror, socket.herror):
                            hosts_tmp.write(line.split(" ")[0] + "\n")
                            if not os.path.isfile(PATH_TO_FILE_DEAD):
                                shutil.mknod(PATH_TO_FILE_DEAD)
                            _dead.write(line.split(" ")[0] + "\n")
                    if len(update_lines) != 0:
                        updates[file] = update_lines

        shutil.move(PATH_TO_FILE_TMP, PATH_TO_FILE_VARS)
        if os.path.isfile(PATH_TO_FILE_TMP):
            os.remove(PATH_TO_FILE_TMP)

        if not os.path.isfile(PATH_TO_FILE):
            shutil.mknod(PATH_TO_FILE)

        with open(PATH_TO_FILE_VARS, 'r') as _vars:
            with open(PATH_TO_FILE, 'w') as hosts:
                for _var in _vars:
                    try:
                        new_host_line = _var.split(" ")[1].rstrip("\n") + " " + _var.split(" ")[0]
                        hosts.write(new_host_line + "\n")
                    except IndexError:
                        pass
print updates

if to_git:
    import sh
    with open('README.md', 'a') as readme:
        for key, values in updates.items():  
            readme.write("\n")         
            readme.write("\n<--- Update for " + key + " from " + str(datetime.datetime.now())[:19] + " --->")
            for val in values:
                readme.write("\n\n" + val)
            readme.write("\n")

    
    git = sh.git.bake(_cwd=os.getcwd())
    git.add('*')
    git.commit(m='Update ' + str(datetime.datetime.now())[:19])
    git.push('origin', 'master')


# --- EMAIL SENDING FOR CHECKING SCRIPT WORKING ---
# import smtplib
# from email.mime.text import MIMEText
# if to_git:
#     to_g = "Commited to Git"
# else:
#     to_g = "Nothing to commit"
# computername = os.getenv('COMPUTERNAME')
# msg = MIMEText('Hello from {} {}'.format(datetime.datetime.now(), to_g))
# msg['Subject'] = 'Test from {}!'.format(computername)
# email_from = '{}@test.com'.format(computername)
# email_to = 'd357cbh@yandex.ru'
# msg['From'] = email_from
# msg['To'] = email_to

# s = smtplib.SMTP('127.0.0.1')
# s.sendmail(email_from, [email_to], msg.as_string())
# s.quit()
