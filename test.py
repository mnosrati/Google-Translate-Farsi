from Translate import Translate


translation = Translate()
translation.translate("protect")

print (translation.Farsi)
print (translation.Farsi_POS)
print (translation.English_POS)
print (translation.English_DEF)
print (translation.English_EXM)
print (translation.Example)
print (translation.Synonym)

translation.close()
