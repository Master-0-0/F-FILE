import argparse
import os


print("___________         ___________.___.____     ___________")
print("\_   _____/         \_   _____/|   |    |    \_   _____/")
print(" |    __)    ______  |    __)  |   |    |     |    __)_")
print(" |     \    /_____/  |     \   |   |    |___  |        \\")
print(" \___  /             \___  /   |___|_______ \/_______  /")
print("     \/                  \/                \/        \/")
print("by:LCC316-Master -h 参数说明")
parser = argparse.ArgumentParser(description="参数说明:")
parser.add_argument("-work", type=str, help="办公三件套", choices=['y', 'Y'])
parser.add_argument("-p", "--Pass", type=str, help="密码本，运维本", choices=['y', 'Y'])
parser.add_argument("-c", "--config", type=str, help="配置文件及备份", choices=['y', 'Y'])
parser.add_argument("-f", "--file", type=str, help="自定义查找")
parser.add_argument("-path", type=str, help="指定路径绝对路径 实例：D:/", required=True)
args = parser.parse_args()

#print(args)

def work():
    files = 'dir /a /s /b *.xls *.xlsx *.doc *.docx *.wsp *.pdf'
    message = os.popen(files)
    print(message.read())

def Passbook():
    list = ['密码', '账号', 'pass', 'login', 'user', '运维', '拓扑']
    for i in range(0, len(list)):
        files = 'dir /a /s /b *.xls *.xlsx *.doc *.docx *.txt *.wsp *.pdf | findstr "{0}"'.format(list[i])
        message = os.popen(files)
        print(message.read())
def Conifg():
    files = "dir /a /s /b *.zip *.rar *.conf *.ini *.inc *.config config.* config*.php *.pb *.properties *.sql *.mdf *.bak *.mdb *.accdb *.dmp *.MYD *.rdp"
    message = os.popen(files)
    print(message.read())

def File(files):
    files = 'dir /a /s /b | findstr "{0}"'.format(files)
    message = os.popen(files)
    print(message.read())


if __name__ == "__main__":
    #切换目录
    os.chdir(args.path)

    #调用办公
    if args.work:
        work()

    #查找密码本
    if args.Pass:
        Passbook()

    # 配置文件
    if args.config:
        Conifg()

    #自定义查找
    if args.file:
        File(args.file)




