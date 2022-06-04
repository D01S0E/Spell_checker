from hanspell import spell_checker
result = spell_checker.check(u"{0}".format(input()))
print(result.checked)