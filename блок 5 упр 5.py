print("mypkg package initialized")

import mypkg.mymod

result1 = mypkg.mymod.test("mypkg/mymod.py")
print(f"Result from mypkg.mymod.test: {result1}")

from mypkg import mymod

result2 = mymod.test("mypkg/mymod.py")
print(f"Result from from mypkg import mymod: {result2}")

from mypkg.mymod import countLines, countChars, test

result3 = test("mypkg/mymod.py")
print(f"Result from from mypkg.mymod import test: {result3}")

line_count = countLines("mypkg/mymod.py")
char_count = countChars("mypkg/mymod.py")
print(f"Lines: {line_count}, Chars: {char_count}")
