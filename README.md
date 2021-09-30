# Google-Translate-Farsi
This piece of code has 3 parts:
- Translate.py
- test.py
- driver (folder) containing the Google Chrome driver ver 75.0.3770.80

The file <b>Translate.py</b> is the main class of the program, that uses Selenium to connect to the Google Translate and fetch the meaning of the words.
So, in order to use this script, you must install Selenium on your system using the following command:
```python -m pip install selenium```   or   ```pip install selenium```

Also, if you are using a different version of Google Chrome (I used ver 75.0.3770.80), you can download the compatible driver file from  the following link and replace the driver file in the "driver" folder with your version. Please note that the chromedriver must be the same version of your installed Chrome:

https://sites.google.com/a/chromium.org/chromedriver/downloads


# How to use?
Simple run the test.py. Here is the example:

```
from Translate import Translate

t = Translate()
t.translate("quadratic")

print (t.Farsi)
print (t.Farsi_POS)
print (t.English_POS)
print (t.English_DEF)
print (t.English_EXM)
print (t.Example)
print (t.Synonym)

t.close()
```

The output will be like this:

```
['درجه دوم؛ چهار گانه؛ وابسته بدرجه دوم هم چندی']
['Adjective']
['adjective', 'noun']
['involving the second and no higher power of an unknown quantity or variable.', 'a quadratic equation.']
['a quadratic equation', 'Historically, imaginary numbers first came to light when trying to solve cubic equations, rather than quadratics .']
['He was able to use his methods to prove many results in the theory of quadratic forms and number theory.', "Smith also extended Gauss's theorem on real quadratic forms to complex quadratic forms.", 'In 1826 Cauchy, in the context of quadratic forms in n variables, used the term ‘tableau’ for the matrix of coefficients.', 'Find the 2 roots and a continued fraction for a root of these quadratic equations.', 'If f = 0, then the quartic in y is actually a quadratic equation in the variable y 2.', "This is certainly possible and the Babylonians' understanding of quadratics adds some weight to the claim.", 'The thought that quadratics are now seen as ‘high brow’ really does, once again, make me despair.', 'The sparseness of the quadratics is what is important here.', "For that matter quadratics aren't all that tough.", 'Historically, imaginary numbers first came to light when trying to solve cubic equations, rather than quadratics .']
Noun
quadratic equation
```

Enjoy ;)


