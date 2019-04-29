import time
import pyperclip
from googletrans import Translator
from win10toast import ToastNotifier



print("""
CREATOR BY;
    EMRE ATAKURU
            CYBER-WARRİOR
""")

time.sleep(3)

son_deger = ""
while True:
    time.sleep(0.3)
    translates = Translator()
    kopyalanan_deger = pyperclip.paste()
    if kopyalanan_deger != son_deger:
        son_deger = kopyalanan_deger
        print ("Değer Değişti: %s" % str(son_deger))
        c = translates.translate(son_deger,dest="tr").text
        print("""
         [>] {0} == {1}
        ----------------------------------------------------
        """.format(son_deger.upper(),c.upper()))
                
        toast = ToastNotifier()
        toast.show_toast("CEVİRİ {0}".format(pyperclip.paste()).lower(),msg=c)


